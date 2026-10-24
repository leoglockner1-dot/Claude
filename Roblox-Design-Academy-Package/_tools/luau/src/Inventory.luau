--!strict
--[[
	Inventory: slot-limited, stack-aware item storage (server-side model; the UI only mirrors it).

	- item definitions live on the server (`defs`): stack size and whether the item is tradable
	- add() returns how many actually fit, so callers can drop or mail the remainder instead of
	  silently deleting rewards (a classic "my loot vanished" bug report)
	- remove() is all-or-nothing, so crafting/selling can never take half of a cost
]]

export type Def = { maxStack: number }
export type Slot = { id: string, count: number }
export type Inv = { slots: { Slot }, capacity: number, defs: { [string]: Def } }

local Inventory = {}

function Inventory.new(capacity: number, defs: { [string]: Def }): Inv
	return { slots = {}, capacity = capacity, defs = defs }
end

function Inventory.count(inv: Inv, id: string): number
	local n = 0
	for _, s in inv.slots do
		if s.id == id then
			n += s.count
		end
	end
	return n
end

function Inventory.add(inv: Inv, id: string, amount: number): number
	local def = inv.defs[id]
	assert(def, "unknown item " .. id)
	assert(amount > 0 and amount % 1 == 0, "amount must be a positive integer")
	local left = amount
	for _, s in inv.slots do -- top up existing stacks first
		if s.id == id and s.count < def.maxStack then
			local put = math.min(def.maxStack - s.count, left)
			s.count += put
			left -= put
			if left == 0 then
				return amount
			end
		end
	end
	while left > 0 and #inv.slots < inv.capacity do
		local put = math.min(def.maxStack, left)
		table.insert(inv.slots, { id = id, count = put })
		left -= put
	end
	return amount - left
end

function Inventory.remove(inv: Inv, id: string, amount: number): boolean
	if Inventory.count(inv, id) < amount then
		return false
	end
	local left = amount
	for i = #inv.slots, 1, -1 do -- take from the last stacks so the first ones stay full
		local s = inv.slots[i]
		if s.id == id then
			local take = math.min(s.count, left)
			s.count -= take
			left -= take
			if s.count == 0 then
				table.remove(inv.slots, i)
			end
			if left == 0 then
				break
			end
		end
	end
	return true
end

-- Atomic multi-item cost (crafting): either every input is removed or none.
function Inventory.consume(inv: Inv, costs: { [string]: number }): boolean
	for id, n in costs do
		if Inventory.count(inv, id) < n then
			return false
		end
	end
	for id, n in costs do
		Inventory.remove(inv, id, n)
	end
	return true
end

return Inventory
