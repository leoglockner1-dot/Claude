---
title: "LU-09 — Developer product receipts"
tags: [luau, monetization, datastore]
note_type: "procedure"
evidence: "tested (CLI) + official docs"
code: "_tools/luau/src/Receipts.luau"
---

# LU-09 — Developer product receipts

## Purpose
Grant every paid developer product **exactly once**, and never confirm a purchase that was not saved.

## The decision table (from the official "Player data and purchasing" sample)
| Situation | Return |
|---|---|
| Player's data is not loaded (joining, or left) | `NotProcessedYet`, so Roblox retries later |
| PurchaseId already processed **and saved** | `PurchaseGranted` |
| PurchaseId processed but not yet saved | try to save → `PurchaseGranted` only if the save succeeds |
| New PurchaseId | grant in memory, record the id, save → `PurchaseGranted` only if the save succeeds, otherwise `NotProcessedYet` |

`Receipts.process(receipt, getProfile, save)` implements this. The processed-id list is bounded (keeps the newest 100).

## Wiring sketch (not executed here)
```lua
MarketplaceService.ProcessReceipt = function(receipt)
    local decision = Receipts.process(receipt, getProfile, function(userId) return saveNow(userId) end)
    return Enum.ProductPurchaseDecision[decision]
end
```
- Assign `ProcessReceipt` **once**, in one server script.
- `getProfile` must return nil until the player's data has loaded. It must not yield forever; the official sample also stops waiting when the player leaves.

## Common mistakes
- Granting, then returning `PurchaseGranted` before the save succeeded. If the server crashes, the player paid and lost the item.
- Not recording PurchaseIds. A retried callback then grants twice.
- Unknown ProductId treated as granted. This module refuses: no grant, not recorded, `NotProcessedYet`.

## Test cases (passing)
Waits while the profile is not loaded; grants once across duplicate calls; a failed save is not confirmed and the retry does not double-grant; unknown products are neither recorded nor granted.

## Acceptance criteria
Tests pass. Studio test purchase (test purchases in Studio do not charge Robux) shows the grant once; repeated callbacks do not re-grant.

## References
- https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing
- https://create.roblox.com/docs/production/monetization/developer-products
