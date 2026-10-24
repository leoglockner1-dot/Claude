--!strict
--[[
	Receipts: the decision logic of MarketplaceService.ProcessReceipt for developer products,
	following the flow in Roblox's "Player data and purchasing" sample
	(create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing):

	  1. player data not loaded yet           -> NotProcessedYet (Roblox retries later)
	  2. PurchaseId already recorded AND saved -> PurchaseGranted (never grant twice)
	  3. PurchaseId recorded but NOT yet saved -> try to save; granted only if the save succeeds
	  4. new PurchaseId: grant in memory, record the id, save; PurchaseGranted only after the save succeeds

	The engine-facing callback is a thin adapter (shown in LU-10). Everything here is pure so the
	"never grant twice / never lose a purchase" rules are testable. Keep the processed list bounded
	(the sample keeps recent ids) - this module keeps the newest `keep` ids.
]]

export type Decision = "PurchaseGranted" | "NotProcessedYet"

export type Profile = {
	processed: { string }, -- PurchaseIds, oldest first
	savedProcessed: { [string]: boolean }, -- ids known to be persisted
	grant: (productId: number) -> boolean, -- applies the product to in-memory data; false = unknown product
}

local Receipts = {}

local function has(list: { string }, id: string): boolean
	return table.find(list, id) ~= nil
end

-- receipt: { PurchaseId: string, ProductId: number, PlayerId: number }
-- getProfile(PlayerId) -> Profile? (nil while loading or after leaving)
-- save(PlayerId) -> boolean (true only when the data store write succeeded)
function Receipts.process(
	receipt: { PurchaseId: string, ProductId: number, PlayerId: number },
	getProfile: (number) -> Profile?,
	save: (number) -> boolean,
	keep: number?
): Decision
	local profile = getProfile(receipt.PlayerId)
	if not profile then
		return "NotProcessedYet"
	end
	local id = receipt.PurchaseId
	if has(profile.processed, id) then
		if profile.savedProcessed[id] then
			return "PurchaseGranted"
		end
	else
		if not profile.grant(receipt.ProductId) then
			-- Unknown product: do not record it, do not grant. Returning NotProcessedYet keeps
			-- Roblox retrying, which is right if a server update will add the product handler.
			return "NotProcessedYet"
		end
		table.insert(profile.processed, id)
		local limit = keep or 100
		while #profile.processed > limit do
			local old = table.remove(profile.processed, 1) :: string
			profile.savedProcessed[old] = nil
		end
	end
	if save(receipt.PlayerId) then
		for _, pid in profile.processed do
			profile.savedProcessed[pid] = true
		end
		return "PurchaseGranted"
	end
	return "NotProcessedYet"
end

return Receipts
