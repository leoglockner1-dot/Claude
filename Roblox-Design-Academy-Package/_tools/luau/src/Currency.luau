--!strict
--[[
	Currency: server-authoritative wallet with validated, logged transactions.

	Rules from Roblox security guidance (server authority; validate values; NaN/inf):
	  - only the server mutates balances; clients only *request* actions through remotes
	  - every amount is validated (finite, positive integer, within a per-transaction cap)
	  - a spend that would go negative is refused, never clamped
	Every change gets a reason string, kept in a bounded log for debugging/support (not persistence).
]]

export type Wallet = {
	balances: { [number]: number },
	log: { { userId: number, delta: number, reason: string, balance: number } },
	logLimit: number,
	maxBalance: number,
	maxPerTx: number,
}

local Currency = {}

export type Options = { maxBalance: number?, maxPerTx: number?, logLimit: number? }

function Currency.new(opts: Options?): Wallet
	local o: Options = opts or {}
	return {
		balances = {},
		log = {},
		logLimit = o.logLimit or 200,
		maxBalance = o.maxBalance or 1e15,
		maxPerTx = o.maxPerTx or 1e12,
	}
end

local function validAmount(w: Wallet, amount: unknown): (boolean, string?)
	if type(amount) ~= "number" or amount ~= amount or amount == math.huge or amount == -math.huge then
		return false, "invalid amount"
	end
	if amount <= 0 or amount % 1 ~= 0 then
		return false, "amount must be a positive integer"
	end
	if amount > w.maxPerTx then
		return false, "amount above per-transaction cap"
	end
	return true, nil
end

local function record(w: Wallet, userId: number, delta: number, reason: string)
	table.insert(w.log, { userId = userId, delta = delta, reason = reason, balance = w.balances[userId] })
	if #w.log > w.logLimit then
		table.remove(w.log, 1)
	end
end

function Currency.balance(w: Wallet, userId: number): number
	return w.balances[userId] or 0
end

function Currency.grant(w: Wallet, userId: number, amount: unknown, reason: string): (boolean, string?)
	local ok, err = validAmount(w, amount)
	if not ok then
		return false, err
	end
	local a = amount :: number
	local new = math.min(Currency.balance(w, userId) + a, w.maxBalance)
	w.balances[userId] = new
	record(w, userId, a, reason)
	return true, nil
end

function Currency.spend(w: Wallet, userId: number, amount: unknown, reason: string): (boolean, string?)
	local ok, err = validAmount(w, amount)
	if not ok then
		return false, err
	end
	local a = amount :: number
	local bal = Currency.balance(w, userId)
	if bal < a then
		return false, "insufficient funds"
	end
	w.balances[userId] = bal - a
	record(w, userId, -a, reason)
	return true, nil
end

-- Load from saved data: tolerate garbage (old saves, corruption) by falling back to 0.
function Currency.load(w: Wallet, userId: number, saved: unknown)
	if type(saved) == "number" and saved == saved and saved >= 0 and saved <= w.maxBalance then
		w.balances[userId] = math.floor(saved)
	else
		w.balances[userId] = 0
	end
end

function Currency.unload(w: Wallet, userId: number): number
	local b = Currency.balance(w, userId)
	w.balances[userId] = nil
	return b
end

return Currency
