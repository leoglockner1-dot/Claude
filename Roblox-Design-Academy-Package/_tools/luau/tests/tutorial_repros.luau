--!strict
-- Reproductions of two defects found while converting official Roblox tutorials into procedures
-- (see 16-Tutorials-and-Workflows/TUT-01 and TUT-13). The tutorial logic is ported line by line into
-- plain Luau with fakes for the engine parts it touches. These are simulations, not Studio runs:
-- they show the logic allows the bad outcome, not how often it happens live.
-- From _tools/luau:  luau tests/tutorial_repros.luau
local T = require("./TestKit")

---------------------------------------------------------------------------------------------------
-- Fakes
---------------------------------------------------------------------------------------------------
type FakeStore = { data: { [number]: any }, failReads: boolean }

local function newStore(): FakeStore
	return { data = {}, failReads = false }
end

local function getAsync(store: FakeStore, key: number): any
	if store.failReads then
		error("502: API Services rejected request") -- message is illustrative
	end
	return store.data[key]
end

local function setAsync(store: FakeStore, key: number, value: any)
	store.data[key] = value
end

-- A one-shot event whose Wait() suspends the calling coroutine until Fire().
type FakeEvent = { waiting: { thread }, fire: (self: FakeEvent) -> () }
local function newEvent(): FakeEvent
	local ev = { waiting = {} } :: any
	function ev.fire(self: FakeEvent)
		local list = self.waiting
		self.waiting = {}
		for _, co in list do
			local ok, err = coroutine.resume(co)
			assert(ok, err)
		end
	end
	return ev
end
local function waitFor(ev: FakeEvent)
	table.insert(ev.waiting, coroutine.running())
	coroutine.yield()
end

---------------------------------------------------------------------------------------------------
-- 1. "Save player data" tutorial (GoldManager): a failed load followed by collecting gold lets the
--    autosave overwrite the player's real saved gold.
---------------------------------------------------------------------------------------------------
local GOLD_VALUE = 10

local function makeGoldManager(store: FakeStore, fixed: boolean)
	local playerGold: { [number]: number } = {}
	local loaded: { [number]: boolean } = {}
	local m = {}

	function m.processGoldTouch(userId: number)
		if fixed and not loaded[userId] then
			return -- fix: no earning (and so no saving) until the load succeeded
		end
		-- tutorial: playerGold[userId] = (playerGold[userId] or 0) + GOLD_VALUE
		playerGold[userId] = (playerGold[userId] or 0) + GOLD_VALUE
	end

	function m.onPlayerAdded(userId: number)
		local success, storedGold = pcall(getAsync, store, userId)
		if success then
			playerGold[userId] = storedGold or 0
			loaded[userId] = true
		end
		-- tutorial: on failure it only shows an alert and warns; playerGold stays nil
	end

	function m.autosaveTick(userId: number)
		-- tutorial: if playerGold[userId] then saveGold(player, playerGold[userId]) end
		if playerGold[userId] and (not fixed or loaded[userId]) then
			setAsync(store, userId, playerGold[userId])
		end
	end

	return m
end

T.describe("Tutorial repro: save-player-data GoldManager", function()
	T.it("tutorial logic: failed load + one gold chunk + autosave overwrites 500 saved gold with 10", function()
		local store = newStore()
		store.data[1] = 500
		local gm = makeGoldManager(store, false)
		store.failReads = true
		gm.onPlayerAdded(1)
		store.failReads = false
		gm.processGoldTouch(1)
		gm.autosaveTick(1)
		T.eq(store.data[1], 10, "the saved 500 gold was replaced")
	end)
	T.it("fix (loaded flag gates earning and saving): saved value survives", function()
		local store = newStore()
		store.data[1] = 500
		local gm = makeGoldManager(store, true)
		store.failReads = true
		gm.onPlayerAdded(1)
		store.failReads = false
		gm.processGoldTouch(1)
		gm.autosaveTick(1)
		T.eq(store.data[1], 500)
	end)
	T.it("tutorial logic: normal path still works (control)", function()
		local store = newStore()
		store.data[1] = 500
		local gm = makeGoldManager(store, false)
		gm.onPlayerAdded(1)
		gm.processGoldTouch(1)
		gm.autosaveTick(1)
		T.eq(store.data[1], 510)
	end)
end)

---------------------------------------------------------------------------------------------------
-- 2. "Script an upgrade button" tutorial: the coin check happens before a call that can yield
--    (player.Character or player.CharacterAdded:Wait()), and coins are deducted after it. Two
--    invocations during the yield both pass the check.
---------------------------------------------------------------------------------------------------
local JUMP_COIN_COST = 5
local JUMP_POWER_INCREMENT = 1

local function makeShop(deductFirst: boolean)
	local data = { coins = 5, jump = 0 }
	local player = { character = nil :: any, characterAdded = newEvent() }

	local function updateJumpPower()
		data.jump += JUMP_POWER_INCREMENT
		-- tutorial: local character = player.Character or player.CharacterAdded:Wait()
		if player.character == nil then
			waitFor(player.characterAdded)
		end
	end

	local function onPurchaseJumpIncrease(): boolean
		if data.coins < JUMP_COIN_COST then
			return false
		end
		if deductFirst then
			data.coins -= JUMP_COIN_COST -- fix: commit the cost before anything that can yield
			updateJumpPower()
		else
			updateJumpPower() -- tutorial order: may yield here
			data.coins -= JUMP_COIN_COST
		end
		return true
	end

	-- Each OnServerInvoke call runs in its own thread, so model each click as a coroutine.
	local function invoke()
		local co = coroutine.create(onPurchaseJumpIncrease)
		local ok, err = coroutine.resume(co)
		assert(ok, err)
	end

	return data, player, invoke
end

T.describe("Tutorial repro: script-an-upgrade-button", function()
	T.it("tutorial order: two purchases while the character is absent -> coins go negative", function()
		local data, player, invoke = makeShop(false)
		invoke()
		invoke()
		player.character = {}
		player.characterAdded:fire()
		T.eq(data.coins, -5, "both calls passed the check with 5 coins")
		T.eq(data.jump, 2)
	end)
	T.it("deduct-first order: second purchase is refused", function()
		local data, player, invoke = makeShop(true)
		invoke()
		invoke()
		player.character = {}
		player.characterAdded:fire()
		T.eq(data.coins, 0)
		T.eq(data.jump, 1)
	end)
	T.it("tutorial order with a character present behaves (control)", function()
		local data, player, invoke = makeShop(false)
		player.character = {}
		invoke()
		invoke()
		T.eq(data.coins, 0)
		T.eq(data.jump, 1)
	end)
end)

T.finish()
