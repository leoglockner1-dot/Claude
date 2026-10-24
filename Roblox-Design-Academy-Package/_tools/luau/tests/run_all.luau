--!strict
-- Runs every academy Luau spec. From _tools/luau:  luau tests/run_all.luau
local T = require("./TestKit")

local NaN = 0 / 0
local INF = math.huge

local Validate = require("../src/Validate")
local TokenBucket = require("../src/TokenBucket")
local CostCurve = require("../src/CostCurve")
local WeightedLoot = require("../src/WeightedLoot")
local Currency = require("../src/Currency")
local PlayerData = require("../src/PlayerData")
local Retry = require("../src/Retry")
local RoundMachine = require("../src/RoundMachine")
local Feel = require("../src/Feel")
local Signal = require("../src/Signal")
local ShopServer = require("../src/ShopServer")
local MockRoblox = require("../mocks/MockRoblox")
local Receipts = require("../src/Receipts")
local Inventory = require("../src/Inventory")

T.describe("Validate", function()
	T.it("rejects NaN and infinity even though they are numbers", function()
		T.falsy((Validate.number(NaN, { min = 0, max = 100 })))
		T.falsy((Validate.number(INF)))
		T.falsy((Validate.number(-INF)))
		T.truthy((Validate.number(5, { min = 0, max = 100 })))
	end)
	T.it("documents why: NaN passes naive range checks", function()
		local naive = not (NaN < 0 or NaN > 1000000)
		T.truthy(naive, "naive range check accepted NaN (this is the bug the docs warn about)")
	end)
	T.it("enforces integer and range", function()
		T.falsy((Validate.number(1.5, { integer = true })))
		T.falsy((Validate.number(-1, { min = 0 })))
		T.falsy((Validate.number(11, { max = 10 })))
	end)
	T.it("caps string length by default and checks utf8", function()
		T.falsy((Validate.str(string.rep("a", 201))))
		T.truthy((Validate.str("hello")))
		T.falsy((Validate.str("\255\254")))
		T.falsy((Validate.str("abc", { pattern = "^%d+$" })))
	end)
	T.it("shape rejects smuggled extra keys and metatables", function()
		local schema = { itemId = Validate.Str({ maxLen = 32 }), qty = Validate.Number({ min = 1, max = 99, integer = true }) }
		T.truthy((Validate.shape({ itemId = "sword", qty = 2 }, schema)))
		local ok, err = Validate.shape({ itemId = "sword", qty = 2, price = 0 }, schema)
		T.falsy(ok)
		T.truthy(string.find(err :: string, "unexpected key"), err)
		T.falsy((Validate.shape(setmetatable({ itemId = "a", qty = 1 }, {}), schema)))
		T.falsy((Validate.shape({ itemId = "sword", qty = NaN }, schema)))
		T.falsy((Validate.shape("sword", schema)))
	end)
	T.it("array rejects holes, extra keys and oversize", function()
		local n = Validate.Number({ integer = true })
		T.truthy((Validate.array({ 1, 2, 3 }, n, 5)))
		T.falsy((Validate.array({ 1, 2, 3, 4, 5, 6 }, n, 5)))
		T.falsy((Validate.array({ [1] = 1, [3] = 3 }, n, 5)))
		T.falsy((Validate.array({ 1, 2, x = 3 } :: any, n, 5)))
	end)
end)

T.describe("TokenBucket", function()
	local clock = 0
	local now = function()
		return clock
	end
	T.it("allows a burst of `capacity`, then refuses", function()
		local tb = TokenBucket.new(5, 10, now)
		for _ = 1, 5 do
			T.truthy(tb:allow(1))
		end
		T.falsy(tb:allow(1))
	end)
	T.it("refills at capacity/window per second", function()
		clock = 0
		local tb = TokenBucket.new(5, 10, now)
		for _ = 1, 5 do
			tb:allow(1)
		end
		clock = 1.9
		T.falsy(tb:allow(1), "0.95 tokens after 1.9 s")
		clock = 2.0
		T.truthy(tb:allow(1), "1 token after 2 s")
	end)
	T.it("tracks players independently and forgets on leave", function()
		clock = 0
		local tb = TokenBucket.new(1, 10, now)
		T.truthy(tb:allow(1))
		T.truthy(tb:allow(2))
		T.falsy(tb:allow(1))
		tb:forget(1)
		T.eq(tb.buckets[1], nil)
	end)
end)

T.describe("CostCurve", function()
	local exp: CostCurve.Curve = { kind = "exponential", base = 10, growth = 1.15 }
	T.it("first purchase costs base", function()
		T.eq((CostCurve.cost(exp, 0)), 10)
		T.eq((CostCurve.cost({ kind = "linear", base = 5, step = 3 }, 4)), 17)
		T.eq((CostCurve.cost({ kind = "polynomial", base = 2, power = 2 }, 2)), 18)
	end)
	T.it("total matches the sum of single purchases", function()
		local sum = 0
		for l = 3, 12 do
			sum += (CostCurve.cost(exp, l))
		end
		T.eq(CostCurve.total(exp, 3, 13), sum)
	end)
	T.it("maxAffordable never overspends and buys the most possible", function()
		local count, spent = CostCurve.maxAffordable(exp, 0, 1000)
		T.truthy(spent <= 1000)
		T.truthy(spent + (CostCurve.cost(exp, count)) > 1000, "next level should be unaffordable")
	end)
	T.it("clamps instead of losing precision past 2^53", function()
		local price, clamped = CostCurve.cost(exp, 400)
		T.truthy(clamped)
		T.eq(price, CostCurve.MAX_SAFE)
	end)
	T.it("pacing helper: seconds to afford", function()
		T.eq(CostCurve.secondsToAfford(exp, 0, 2), 5)
		T.eq(CostCurve.secondsToAfford(exp, 0, 0), math.huge)
	end)
end)

T.describe("WeightedLoot", function()
	local entries: { WeightedLoot.Entry } = {
		{ id = "common", weight = 70, rarity = 1 },
		{ id = "rare", weight = 25, rarity = 2 },
		{ id = "legendary", weight = 5, rarity = 3 },
	}
	T.it("odds sum to 1 and match weights", function()
		local t = WeightedLoot.new(entries, WeightedLoot.seeded(1))
		local o = WeightedLoot.odds(t)
		T.near(o.common + o.rare + o.legendary, 1, 1e-9)
		T.near(o.legendary, 0.05, 1e-9)
	end)
	T.it("observed frequencies converge to the published odds (100k rolls)", function()
		local t = WeightedLoot.new(entries, WeightedLoot.seeded(12345))
		local counts: { [string]: number } = { common = 0, rare = 0, legendary = 0 }
		for _ = 1, 100000 do
			local e = WeightedLoot.roll(t, 1)
			counts[e.id] += 1
		end
		T.near(counts.legendary / 100000, 0.05, 0.005)
		T.near(counts.common / 100000, 0.70, 0.01)
	end)
	T.it("pity forces the tier after N misses and resets", function()
		local always = function()
			return 0.0
		end -- always picks the first entry (common) unless forced
		local t = WeightedLoot.new(entries, always, { rarity = 3, after = 10 })
		for i = 1, 9 do
			local e, forced = WeightedLoot.roll(t, 7)
			T.eq(e.id, "common", "roll " .. i)
			T.falsy(forced)
		end
		local e, forced = WeightedLoot.roll(t, 7)
		T.eq(e.id, "legendary")
		T.truthy(forced)
		T.eq(t.misses[7], 0)
	end)
	T.it("effectiveOdds shows the forced pity roll as 100% for the pity tier", function()
		local t = WeightedLoot.new(entries, function(): number
			return 0.0
		end, { rarity = 3, after = 10 })
		T.near(WeightedLoot.effectiveOdds(t, 5).legendary, 0.05, 1e-9, "before any misses: base odds")
		for _ = 1, 9 do
			WeightedLoot.roll(t, 5)
		end
		local o = WeightedLoot.effectiveOdds(t, 5)
		T.eq(o.legendary, 1)
		T.eq(o.common, 0)
	end)
	T.it("rejects bad weights", function()
		T.throws(function()
			WeightedLoot.new({ { id = "x", weight = 0 / 0, rarity = 1 } }, function(): number
				return math.random()
			end)
		end, "weights")
	end)
end)

T.describe("Currency", function()
	T.it("grants and spends with validation", function()
		local w = Currency.new()
		T.truthy((Currency.grant(w, 1, 100, "quest")))
		T.truthy((Currency.spend(w, 1, 30, "shop")))
		T.eq(Currency.balance(w, 1), 70)
	end)
	T.it("refuses overspend, NaN, negatives, fractions", function()
		local w = Currency.new()
		Currency.grant(w, 1, 10, "start")
		T.falsy((Currency.spend(w, 1, 11, "shop")))
		T.falsy((Currency.spend(w, 1, NaN, "exploit")))
		T.falsy((Currency.grant(w, 1, -5, "exploit")))
		T.falsy((Currency.grant(w, 1, 1.5, "exploit")))
		T.falsy((Currency.grant(w, 1, INF, "exploit")))
		T.eq(Currency.balance(w, 1), 10)
	end)
	T.it("loads garbage saves as zero", function()
		local w = Currency.new()
		Currency.load(w, 1, "lots")
		T.eq(Currency.balance(w, 1), 0)
		Currency.load(w, 2, NaN)
		T.eq(Currency.balance(w, 2), 0)
		Currency.load(w, 3, 42.9)
		T.eq(Currency.balance(w, 3), 42)
	end)
	T.it("keeps a bounded log", function()
		local w = Currency.new({ logLimit = 3 })
		for i = 1, 5 do
			Currency.grant(w, 1, i, "t" .. i)
		end
		T.eq(#w.log, 3)
		T.eq(w.log[1].reason, "t3")
	end)
end)

T.describe("PlayerData", function()
	T.it("new players get defaults", function()
		local d, notes = PlayerData.fromSave(nil)
		T.eq(d.version, PlayerData.VERSION)
		T.eq(d.coins, 0)
		T.eq(notes[1], "new player")
	end)
	T.it("migrates v1 -> v3 (gold renamed, settings grouped)", function()
		local d, notes = PlayerData.fromSave({ gold = 250, musicVolume = 0.2, level = 4 })
		T.eq(d.coins, 250)
		T.eq(d.settings.music, 0.2)
		T.eq(d.settings.sfx, 0.8, "filled from defaults")
		T.eq(d.level, 4)
		T.eq((d :: any).gold, nil)
		T.eq(#notes, 2)
	end)
	T.it("drops wrong types and NaN instead of keeping them", function()
		local d = PlayerData.fromSave({ version = 3, coins = "999", level = 0 / 0, inventory = { sword = 1, bad = "x", [5] = 3 } })
		T.eq(d.coins, 0)
		T.eq(d.level, 1)
		T.eq(d.inventory.sword, 1)
		T.eq(d.inventory.bad, nil)
	end)
	T.it("refuses to load saves from a newer server version", function()
		T.throws(function()
			PlayerData.fromSave({ version = PlayerData.VERSION + 1 })
		end, "newer")
	end)
	T.it("size guard warns on large data", function()
		local d = PlayerData.defaults()
		for i = 1, 20000 do
			d.inventory["item_" .. i] = i
		end
		local _, warn = PlayerData.toSave(d)
		T.truthy(warn)
	end)
	T.it("uses a static key", function()
		T.eq(PlayerData.key(123), "User_123")
	end)
end)

T.describe("Retry", function()
	T.it("succeeds after transient failures and waits with backoff", function()
		local calls, waited = 0, {}
		local ok, value = Retry.call(function()
			calls += 1
			if calls < 3 then
				error("throttled")
			end
			return "saved"
		end, {
			wait = function(s: number)
				table.insert(waited, s)
			end,
			rng = function(): number
				return 0.5
			end,
		} :: Retry.Options)
		T.truthy(ok)
		T.eq(value, "saved")
		T.eq(calls, 3)
		T.eq(waited[1], 1)
		T.eq(waited[2], 2)
	end)
	T.it("stops on non-retryable errors", function()
		local calls = 0
		local ok = Retry.call(function()
			calls += 1
			error("invalid key")
		end, {
			isRetryable = function(e: any): boolean
				return not string.find(tostring(e), "invalid")
			end,
		} :: Retry.Options)
		T.falsy(ok)
		T.eq(calls, 1)
	end)
	T.it("caps delay", function()
		local d = Retry.delays({ attempts = 8, baseDelay = 1, maxDelay = 16 })
		T.eq(d[#d], 16)
		T.eq(#d, 7)
	end)
end)

T.describe("RoundMachine", function()
	local cfg = { minPlayers = 2, intermission = 10, roundLength = 60, results = 5 }
	T.it("waits for minPlayers, then runs a full cycle", function()
		local m = RoundMachine.new(cfg)
		local seen = {}
		RoundMachine.onEnter(m, function(s)
			table.insert(seen, s)
		end)
		RoundMachine.setPlayers(m, 1)
		T.eq(m.state, "Waiting")
		RoundMachine.setPlayers(m, 2)
		T.eq(m.state, "Intermission")
		RoundMachine.step(m, 10)
		T.eq(m.state, "Playing")
		RoundMachine.finish(m, "Red")
		T.eq(m.state, "Results")
		T.eq(m.winner, "Red")
		RoundMachine.step(m, 5)
		T.eq(m.state, "Intermission")
		T.eq(table.concat(seen, ","), "Intermission,Playing,Results,Intermission")
	end)
	T.it("ends the round when players drop below minimum", function()
		local m = RoundMachine.new(cfg)
		RoundMachine.setPlayers(m, 3)
		RoundMachine.step(m, 10)
		RoundMachine.setPlayers(m, 1)
		T.eq(m.state, "Results")
		RoundMachine.step(m, 5)
		T.eq(m.state, "Waiting")
	end)
	T.it("times out a round with no winner", function()
		local m = RoundMachine.new(cfg)
		RoundMachine.setPlayers(m, 2)
		RoundMachine.step(m, 10)
		RoundMachine.step(m, 61)
		T.eq(m.state, "Results")
		T.eq(m.winner, nil)
	end)
end)

T.describe("Feel", function()
	T.it("easing curves start at 0 and end at 1", function()
		for name, f in Feel.ease do
			T.near(f(0), 0, 1e-9, name)
			T.near(f(1), 1, 1e-9, name)
		end
	end)
	T.it("backOut overshoots (that is the point)", function()
		local peak = 0
		for i = 0, 100 do
			peak = math.max(peak, Feel.ease.backOut(i / 100))
		end
		T.truthy(peak > 1.05 and peak < 1.15, "peak " .. peak)
	end)
	T.it("critically damped spring settles without overshoot", function()
		local x, v = 0, 0
		local maxX = 0
		for _ = 1, 120 do
			x, v = Feel.springStep(x, v, 1, 12, 1 / 60)
			maxX = math.max(maxX, x)
		end
		T.near(x, 1, 1e-3)
		T.truthy(maxX <= 1 + 1e-9, "overshoot " .. maxX)
	end)
	T.it("spring is stable with a huge frame time (lag spike)", function()
		local x, v = Feel.springStep(0, 0, 1, 12, 5)
		T.near(x, 1, 1e-6)
		T.truthy(v == v)
	end)
	T.it("formats numbers for HUDs", function()
		T.eq(Feel.abbreviate(999), "999")
		T.eq(Feel.abbreviate(1234), "1.23K")
		T.eq(Feel.abbreviate(9870000), "9.87M")
		T.eq(Feel.abbreviate(12345678), "12.3M")
		T.eq(Feel.abbreviate(-1500), "-1.50K")
		T.eq(Feel.abbreviate(999999), "999K", "truncates, never rounds up to 1.00M")
		T.eq(Feel.commas(1234567), "1,234,567")
		T.eq(Feel.commas(100), "100")
		T.eq(Feel.clock(75), "1:15")
	end)
end)

T.describe("Signal", function()
	T.it("fires listeners and supports disconnect during fire", function()
		local s = Signal.new()
		local log = {}
		local c2: any = nil
		s:connect(function(v)
			table.insert(log, "a" .. v)
			c2:disconnect()
		end)
		c2 = s:connect(function(v)
			table.insert(log, "b" .. v)
		end)
		s:fire(1) -- snapshot: b still runs this time? No - it was disconnected before its turn
		s:fire(2)
		T.eq(table.concat(log, ","), "a1,a2")
		T.eq(s:count(), 1)
	end)
	T.it("janitor cleans everything in reverse order", function()
		local j = Signal.janitor()
		local order = {}
		j:add(function()
			table.insert(order, 1)
		end)
		local s = Signal.new()
		j:add(s:connect(function() end))
		j:add(function()
			table.insert(order, 3)
		end)
		T.eq(j:clean(), 3)
		T.eq(table.concat(order, ","), "3,1")
		T.eq(s:count(), 0)
	end)
end)

T.describe("ShopServer (integration with mocks)", function()
	T.it("full purchase flow through a mocked RemoteFunction", function()
		local env = MockRoblox.new()
		local shop = ShopServer.new(env.deps)
		local p = env:addPlayer(101, { x = 0, y = 0, z = 0 })
		shop:grant(p, 100)
		local ok, res = env:invoke(p, "BuyItem", { itemId = "sword", qty = 1 })
		T.truthy(ok, tostring(res))
		T.eq(shop:balance(p), 60)
		T.eq(shop:owned(p, "sword"), 1)
	end)
	T.it("rejects exploit payloads", function()
		local env = MockRoblox.new()
		local shop = ShopServer.new(env.deps)
		local p = env:addPlayer(102, { x = 0, y = 0, z = 0 })
		shop:grant(p, 100)
		T.falsy((env:invoke(p, "BuyItem", { itemId = "sword", qty = 0 / 0 })))
		T.falsy((env:invoke(p, "BuyItem", { itemId = "sword", qty = 1, price = 0 })))
		T.falsy((env:invoke(p, "BuyItem", { itemId = "godmode", qty = 1 })))
		T.falsy((env:invoke(p, "BuyItem", "sword")))
		T.eq(shop:balance(p), 100)
	end)
	T.it("enforces shop distance (context validation)", function()
		local env = MockRoblox.new()
		local shop = ShopServer.new(env.deps)
		local p = env:addPlayer(103, { x = 500, y = 0, z = 0 })
		shop:grant(p, 100)
		local ok, err = env:invoke(p, "BuyItem", { itemId = "sword", qty = 1 })
		T.falsy(ok)
		T.eq(err, "too far from shop")
	end)
	T.it("rate-limits spam", function()
		local env = MockRoblox.new()
		local shop = ShopServer.new(env.deps)
		local p = env:addPlayer(104, { x = 0, y = 0, z = 0 })
		shop:grant(p, 100000)
		local accepted = 0
		for _ = 1, 50 do
			if env:invoke(p, "BuyItem", { itemId = "potion", qty = 1 }) then
				accepted += 1
			end
		end
		T.eq(accepted, 5, "burst capacity")
	end)
	T.it("cleans up when the player leaves", function()
		local env = MockRoblox.new()
		local shop = ShopServer.new(env.deps)
		local p = env:addPlayer(105, { x = 0, y = 0, z = 0 })
		shop:grant(p, 10)
		env:removePlayer(p)
		T.eq(shop:balance(p), 0)
		T.eq(shop.limiter.buckets[105], nil)
		T.eq(env.saved["User_105"].coins, 10, "saved on leave")
	end)
end)

T.describe("Receipts (ProcessReceipt decisions)", function()
	local function setup()
		local coins = 0
		local profile: Receipts.Profile = {
			processed = {},
			savedProcessed = {},
			grant = function(productId: number): boolean
				if productId == 111 then
					coins += 100
					return true
				end
				return false
			end,
		}
		return profile, function()
			return coins
		end
	end
	local r = { PurchaseId = "p1", ProductId = 111, PlayerId = 9 }
	T.it("waits while the profile is not loaded", function()
		T.eq(Receipts.process(r, function()
			return nil
		end, function()
			return true
		end), "NotProcessedYet")
	end)
	T.it("grants once even if Roblox calls again (retry/duplicate)", function()
		local profile, coins = setup()
		local get = function()
			return profile
		end
		local ok = function()
			return true
		end
		T.eq(Receipts.process(r, get, ok), "PurchaseGranted")
		T.eq(Receipts.process(r, get, ok), "PurchaseGranted")
		T.eq(coins(), 100, "granted exactly once")
	end)
	T.it("does not confirm a purchase whose save failed, and does not double-grant on retry", function()
		local profile, coins = setup()
		local get = function()
			return profile
		end
		T.eq(Receipts.process(r, get, function()
			return false
		end), "NotProcessedYet")
		T.eq(coins(), 100)
		T.eq(Receipts.process(r, get, function()
			return true
		end), "PurchaseGranted")
		T.eq(coins(), 100, "the retry saved, it did not grant again")
	end)
	T.it("unknown products are not recorded or granted", function()
		local profile, coins = setup()
		T.eq(Receipts.process({ PurchaseId = "p2", ProductId = 999, PlayerId = 9 }, function()
			return profile
		end, function()
			return true
		end), "NotProcessedYet")
		T.eq(coins(), 0)
		T.eq(#profile.processed, 0)
	end)
end)

T.describe("Inventory", function()
	local defs = { ore = { maxStack = 50 }, sword = { maxStack = 1 } }
	T.it("stacks, then opens new slots, then reports what did not fit", function()
		local inv = Inventory.new(3, defs)
		T.eq(Inventory.add(inv, "ore", 120), 120)
		T.eq(#inv.slots, 3)
		T.eq(Inventory.add(inv, "ore", 40), 30, "only 30 fit in the third stack")
		T.eq(Inventory.add(inv, "sword", 1), 0, "full")
	end)
	T.it("remove is all-or-nothing", function()
		local inv = Inventory.new(5, defs)
		Inventory.add(inv, "ore", 60)
		T.falsy(Inventory.remove(inv, "ore", 61))
		T.eq(Inventory.count(inv, "ore"), 60)
		T.truthy(Inventory.remove(inv, "ore", 15))
		T.eq(Inventory.count(inv, "ore"), 45)
		T.eq(#inv.slots, 1, "emptied stack removed")
	end)
	T.it("consume takes every cost or none", function()
		local inv = Inventory.new(5, defs)
		Inventory.add(inv, "ore", 10)
		T.falsy(Inventory.consume(inv, { ore = 5, sword = 1 }))
		T.eq(Inventory.count(inv, "ore"), 10)
	end)
end)

local _, failed = T.finish()
if failed > 0 then
	error(failed .. " test(s) failed")
end
