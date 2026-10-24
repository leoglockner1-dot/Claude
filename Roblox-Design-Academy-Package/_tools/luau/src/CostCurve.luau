--!strict
--[[
	CostCurve: upgrade/level pricing that stays predictable, overflow-safe and cheap to evaluate.

	Curves (level is 0-based: cost(0) is the price of the FIRST purchase):
	  linear       base + step * level
	  exponential  base * growth ^ level          (classic incremental/tycoon curve)
	  polynomial   base * (level + 1) ^ power     (gentler late game than exponential)

	Design notes (academy, see 05-Progression-and-Economy):
	  - Exponential with growth 1.07-1.15 is common in incremental games; it makes every purchase feel
	    similar relative to income only if income also grows multiplicatively. Test both curves together.
	  - Numbers above 2^53 lose integer precision in doubles. `cost` clamps to MAX_SAFE and reports it.
]]

local CostCurve = {}

CostCurve.MAX_SAFE = 2 ^ 53

export type Curve = {
	kind: "linear" | "exponential" | "polynomial",
	base: number,
	step: number?, -- linear
	growth: number?, -- exponential
	power: number?, -- polynomial
	round: boolean?, -- default true: whole-number prices
}

function CostCurve.cost(c: Curve, level: number): (number, boolean)
	assert(level >= 0 and level % 1 == 0, "level must be a non-negative integer")
	local raw: number
	if c.kind == "linear" then
		raw = c.base + (c.step or 0) * level
	elseif c.kind == "exponential" then
		raw = c.base * (c.growth or 1) ^ level
	else
		raw = c.base * (level + 1) ^ (c.power or 1)
	end
	if c.round ~= false then
		raw = math.floor(raw + 0.5)
	end
	if raw ~= raw or raw > CostCurve.MAX_SAFE then
		return CostCurve.MAX_SAFE, true
	end
	return raw, false
end

-- Total price of buying levels [from, to) one after another (what a "buy x10" button charges).
function CostCurve.total(c: Curve, from: number, to: number): number
	local sum = 0
	for level = from, to - 1 do
		local price, clamped = CostCurve.cost(c, level)
		sum += price
		if clamped or sum >= CostCurve.MAX_SAFE then
			return CostCurve.MAX_SAFE
		end
	end
	return sum
end

-- How many consecutive levels starting at `level` the player can afford with `money`
-- (what a "buy max" button purchases), and what they cost. Linear scan with an upper bound;
-- prices are monotonic so it stops at the first unaffordable level.
function CostCurve.maxAffordable(c: Curve, level: number, money: number, cap: number?): (number, number)
	local count, spent = 0, 0
	local limit = cap or 10000
	while count < limit do
		local price = CostCurve.cost(c, level + count)
		if spent + price > money then
			break
		end
		spent += price
		count += 1
	end
	return count, spent
end

-- Seconds of income needed for the next level: the metric that actually describes pacing.
function CostCurve.secondsToAfford(c: Curve, level: number, incomePerSecond: number): number
	if incomePerSecond <= 0 then
		return math.huge
	end
	return CostCurve.cost(c, level) / incomePerSecond
end

return CostCurve
