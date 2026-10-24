--!strict
--[[
	WeightedLoot: weighted random rewards with an optional pity counter and published odds.

	- rng is injected: in Roblox pass `function() return rng:NextNumber() end` with rng = Random.new();
	  tests pass a seeded generator so results are reproducible.
	- odds() returns each entry's probability so the game can show odds before a roll. (Roblox's
	  policy on paid random items requires disclosing odds before purchase - check the current
	  "Paid random items" policy text before shipping; this module only makes disclosure easy.)
	- Pity: after `pity.after` rolls without an entry of `pity.rarity` or better, the next roll is forced
	  to that tier. Pity changes the effective odds; disclose that too.
]]

export type Entry = { id: string, weight: number, rarity: number } -- rarity: higher = rarer
export type Pity = { rarity: number, after: number }

export type Table = {
	entries: { Entry },
	total: number,
	pity: Pity?,
	misses: { [number]: number }, -- per player: rolls since last pity-tier result
	rng: () -> number,
}

local WeightedLoot = {}

function WeightedLoot.new(entries: { Entry }, rng: () -> number, pity: Pity?): Table
	local total = 0
	for _, e in entries do
		assert(e.weight > 0 and e.weight == e.weight, "weights must be positive numbers: " .. e.id)
		total += e.weight
	end
	assert(total > 0, "loot table is empty")
	return { entries = entries, total = total, pity = pity, misses = {}, rng = rng }
end

function WeightedLoot.odds(t: Table): { [string]: number }
	local out = {}
	for _, e in t.entries do
		out[e.id] = e.weight / t.total
	end
	return out
end

local function pick(t: Table, minRarity: number?): Entry
	local pool, total = t.entries, t.total
	if minRarity then
		local filtered = {}
		total = 0
		for _, e in t.entries do
			if e.rarity >= minRarity then
				table.insert(filtered, e)
				total += e.weight
			end
		end
		pool = filtered
	end
	local r = t.rng() * total
	for _, e in pool do
		r -= e.weight
		if r < 0 then
			return e
		end
	end
	return pool[#pool] -- floating point edge: r landed exactly on total
end

function WeightedLoot.roll(t: Table, userId: number): (Entry, boolean)
	local p = t.pity
	if p then
		local misses = t.misses[userId] or 0
		local forced = misses + 1 >= p.after
		local e = pick(t, if forced then p.rarity else nil)
		if e.rarity >= p.rarity then
			t.misses[userId] = 0
		else
			t.misses[userId] = misses + 1
		end
		return e, forced
	end
	return pick(t), false
end

-- Small deterministic PRNG for tests and offline simulation (xorshift32). Not for security.
function WeightedLoot.seeded(seed: number): () -> number
	local s = bit32.bor(seed, 1)
	return function()
		s = bit32.bxor(s, bit32.lshift(s, 13))
		s = bit32.bxor(s, bit32.rshift(s, 17))
		s = bit32.bxor(s, bit32.lshift(s, 5))
		return s / 4294967296
	end
end

return WeightedLoot
