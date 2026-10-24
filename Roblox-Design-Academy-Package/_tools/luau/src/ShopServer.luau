--!strict
--[[
	ShopServer: a complete server-side purchase handler, written against injected dependencies so it
	runs both in Roblox and in the CLI tests (with mocks/MockRoblox.luau).

	Request flow (Roblox security guidance, "In-game shop" and "Weapon targeting" sections):
	  1. rate limit       - TokenBucket per player (5 requests / 10 s burst)
	  2. type/structure   - Validate.shape: exact keys, bounded strings, finite integer qty
	  3. value            - item exists in the SERVER catalog (price never comes from the client)
	  4. context          - player character within SHOP_RANGE studs of the shop
	  5. state change     - Currency.spend, then inventory; both on the server
	Returns (ok, result|error) so the client can show a reason.

	Roblox wiring (thin, not tested here):
	  local shop = ShopServer.new({
	      remote = ReplicatedStorage.Remotes.BuyItem,           -- RemoteFunction
	      playerAdded = Players.PlayerAdded, playerRemoving = Players.PlayerRemoving,
	      characterPosition = function(p) local r = p.Character and p.Character:FindFirstChild("HumanoidRootPart")
	                                        return r and { x = r.Position.X, y = r.Position.Y, z = r.Position.Z } end,
	      shopPosition = { x = 0, y = 0, z = 0 }, clock = os.clock,
	      load = function(key) return store:GetAsync(key) end, save = function(key, data) store:SetAsync(key, data) end,
	  })
	(For real saves wrap load/save with Retry.call and prefer UpdateAsync - see 07-Roblox-Studio-and-Luau/LU-08.)
]]

local Validate = require("./Validate")
local TokenBucket = require("./TokenBucket")
local Currency = require("./Currency")
local PlayerData = require("./PlayerData")

export type Vec = { x: number, y: number, z: number }
export type PlayerLike = { UserId: number }

export type Deps = {
	setInvokeHandler: (name: string, handler: (player: PlayerLike, payload: unknown) -> (boolean, any)) -> (),
	onPlayerRemoving: (fn: (player: PlayerLike) -> ()) -> (),
	characterPosition: (player: PlayerLike) -> Vec?,
	shopPosition: Vec,
	clock: () -> number,
	save: (key: string, data: any) -> (),
}

local CATALOG: { [string]: { price: number, maxQty: number } } = {
	sword = { price = 40, maxQty = 1 },
	potion = { price = 5, maxQty = 10 },
}
local SHOP_RANGE = 20 -- studs, plus latency tolerance below
local LATENCY_TOLERANCE = 6

local payloadSchema = {
	itemId = Validate.Str({ maxLen = 32, pattern = "^[%w_]+$" }),
	qty = Validate.Number({ min = 1, max = 10, integer = true }),
}

local ShopServer = {}
ShopServer.__index = ShopServer

export type Shop = typeof(setmetatable(
	{} :: {
		deps: Deps,
		wallet: Currency.Wallet,
		limiter: TokenBucket.TokenBucket,
		inventory: { [number]: { [string]: number } },
	},
	ShopServer
))

local function dist(a: Vec, b: Vec): number
	return math.sqrt((a.x - b.x) ^ 2 + (a.y - b.y) ^ 2 + (a.z - b.z) ^ 2)
end

function ShopServer.new(deps: Deps): Shop
	local self = setmetatable({
		deps = deps,
		wallet = Currency.new(),
		limiter = TokenBucket.new(5, 10, deps.clock),
		inventory = {},
	}, ShopServer)
	deps.setInvokeHandler("BuyItem", function(player, payload)
		return self:buy(player, payload)
	end)
	deps.onPlayerRemoving(function(player)
		self:release(player)
	end)
	return self
end

function ShopServer.buy(self: Shop, player: PlayerLike, payload: unknown): (boolean, any)
	if not self.limiter:allow(player.UserId) then
		return false, "slow down"
	end
	local ok, err = Validate.shape(payload, payloadSchema)
	if not ok then
		return false, "bad request: " .. (err or "?")
	end
	local req = payload :: { itemId: string, qty: number }
	local item = CATALOG[req.itemId]
	if not item then
		return false, "unknown item"
	end
	local owned = self:owned(player, req.itemId)
	if owned + req.qty > item.maxQty then
		return false, "limit reached"
	end
	local pos = self.deps.characterPosition(player)
	if not pos or dist(pos, self.deps.shopPosition) > SHOP_RANGE + LATENCY_TOLERANCE then
		return false, "too far from shop"
	end
	local spent, why = Currency.spend(self.wallet, player.UserId, item.price * req.qty, "buy " .. req.itemId)
	if not spent then
		return false, why
	end
	local inv = self.inventory[player.UserId] or {}
	inv[req.itemId] = owned + req.qty
	self.inventory[player.UserId] = inv
	return true, { balance = Currency.balance(self.wallet, player.UserId), owned = inv[req.itemId] }
end

function ShopServer.grant(self: Shop, player: PlayerLike, amount: number)
	Currency.grant(self.wallet, player.UserId, amount, "grant")
end

function ShopServer.balance(self: Shop, player: PlayerLike): number
	return Currency.balance(self.wallet, player.UserId)
end

function ShopServer.owned(self: Shop, player: PlayerLike, itemId: string): number
	local inv = self.inventory[player.UserId]
	return if inv then inv[itemId] or 0 else 0
end

function ShopServer.release(self: Shop, player: PlayerLike)
	local data = PlayerData.defaults()
	data.coins = Currency.unload(self.wallet, player.UserId)
	data.inventory = self.inventory[player.UserId] or {}
	self.deps.save(PlayerData.key(player.UserId), (PlayerData.toSave(data)))
	self.inventory[player.UserId] = nil
	self.limiter:forget(player.UserId)
end

return ShopServer
