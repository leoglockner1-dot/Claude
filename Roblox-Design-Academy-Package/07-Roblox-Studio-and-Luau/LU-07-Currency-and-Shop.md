---
title: "LU-07 — Server-authoritative currency and shop purchase"
tags: [luau, economy, shop, security]
note_type: "procedure"
evidence: "tested (CLI + mocked engine)"
code: "_tools/luau/src/Currency.luau, _tools/luau/src/ShopServer.luau"
---

# LU-07 — Server-authoritative currency and shop purchase

## Purpose
A purchase flow that cannot be exploited by changing prices, quantities or distance, and that gives the client a clear result.

## Dependencies
`Currency`, `Validate`, `TokenBucket`, `PlayerData` (to save on leave). The engine is injected through `deps`; see the header of [`ShopServer.luau`](../_tools/luau/src/ShopServer.luau) for the Roblox wiring.

## Flow (from Roblox's "In-game shop" guidance)
1. Rate limit (`TokenBucket`, 5/10 s).
2. Validate shape: `{ itemId: string ≤32 [%w_], qty: integer 1–10 }`, with no extra keys.
3. Look the item up in the **server** catalog. The price never comes from the client.
4. Per-item limit (`maxQty`).
5. Context: character within 20 studs of the shop, plus 6 studs latency tolerance.
6. `Currency.spend`, which refuses an overspend instead of clamping. Then update the inventory.
7. Return `(true, { balance, owned })` or `(false, reason)`.

## Currency rules
- Store balances as **integers**. Validate amounts as finite, positive integers under a per-transaction cap.
- Every change has a `reason` and goes into a bounded log, which helps with support and debugging. For audit-grade history, write to a separate store.
- `Currency.load` treats garbage saves (strings, NaN, negatives) as 0, so bad data cannot crash the session.

## Client side
- Disable the Buy button while the request is pending, so double-clicking does not fire twice. The server still rate-limits.
- On success, play the purchase feedback ([R04 Upgrade purchase](../18-Skill-Training/Design-Recipes/R04-Upgrade-Purchase-Interaction.md)). On failure, show the reason near the button for about 2 s.

## Common mistakes
- Granting the item before spending (or without checking that the spend succeeded).
- Putting prices in a replicated ModuleScript **and** trusting them from the client. A replicated catalog is fine for display, but the server must use its own copy.
- No distance check, which allows remote buying from anywhere.

## Test cases (passing; `tests/run_all.luau` → ShopServer)
- Full purchase: balance 100 → 60, sword owned = 1.
- Exploits rejected with the balance unchanged: NaN qty, extra `price` key, unknown item, string payload.
- Player 500 studs away → `"too far from shop"`.
- 50 rapid requests → 5 accepted.
- On leave: wallet unloaded, limiter cleared, data saved under `User_<id>` with the coins preserved.

## Acceptance criteria
All of the above pass, and a Studio playtest with 2 clients shows each client's balance updating independently.

## References
- https://create.roblox.com/docs/scripting/security/client-server-boundary#in-game-shop
