---
title: "TUT-01 — Script an upgrade button (server-validated purchase)"
tags: [tutorial, luau, shop, remotes, security]
note_type: "tutorial-procedure"
source: "https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-an-upgrade-button"
source_author: "Roblox Creator Documentation"
licence: "Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution."
accessed: "2026-10-24"
evidence: "[SRC] = what the tutorial says; [ANALYSIS] = our reading; [SIM-TESTED] = reproduced in a Luau simulation; [HYP] = untested"
---

# TUT-01 — Script an upgrade button (server-validated purchase)

**Skill:** Let a client button request a purchase that the server checks and applies (coins → jump power).

## Source and access
- Source: [https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-an-upgrade-button](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-an-upgrade-button)
- Author: Roblox (official documentation). Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution.
- Access: Read the Markdown source of the page from the public Roblox/creator-docs repository (commit 4e795e6), accessed 2026-10-24. Images, videos and the linked sample places (.rbxl) were **not** opened, and no step was performed in Roblox Studio.

## Workflow in the tutorial [SRC]
1. A `RemoteFunction` (`IncreaseJumpPowerFunction`) lives in ReplicatedStorage; the client `LocalScript` calls `InvokeServer` inside `pcall` when the button's `Activated` fires.
2. The server's `OnServerInvoke` handler reads coins from a server-side `PlayerData` module, returns `false` if coins < cost, otherwise raises jump power, deducts coins and updates the leaderboard, then returns `true`.
3. Jump power is reapplied on every `CharacterAdded`, because a new character starts with default values.
4. The client only shows the result (a warning when the server says "not enough coins").

## Decisions and the reasons the tutorial gives [SRC]
| Decision | Reason |
|---|---|
| Coins are checked on the server, not in the LocalScript. | The client can be modified; only the server's copy of the data is trustworthy (stated by the tutorial and the Roblox security docs). |
| `RemoteFunction` rather than `RemoteEvent`. | The client wants an answer (purchased or not) to show feedback. |
| Jump power stored in player data and reapplied on spawn. | Humanoid properties reset with each new character. |

## Our analysis
- **[SIM-TESTED] Race window.** `onPurchaseJumpIncrease` checks coins, then calls `updateJumpPower`, which can yield on `player.Character or player.CharacterAdded:Wait()`, and only *then* deducts coins. Two invocations while the character is absent both pass the check. Ported to plain Luau in `_tools/luau/tests/tutorial_repros.luau`: with 5 coins and cost 5, two clicks gave coins = −5 and two upgrades. Moving the deduction before anything that can yield gave coins = 0 and one upgrade. The window is narrow in practice (only while `Character` is nil); this was **not** reproduced in Studio.
- **[ANALYSIS] Hanging thread on leave.** `onPlayerRemoved` calls `updateJumpPower`, which waits on `CharacterAdded` if the character is already gone, a wait that never resumes. Harmless per player but it leaks a thread.
- **[ANALYSIS] Client error on failure.** The client calls `error(purchased)` when the invoke fails, which turns a network hiccup into a script error instead of user feedback. Show a retry message instead ([AV-05 Error/Denied](../08-Animation-and-Game-Feel/Recipes/AV-05-Error-Denied.md)).
- **[ANALYSIS]** There is no rate limit on the remote; a modified client can invoke it in a loop. Pair with [LU-06 Rate Limiting](../07-Roblox-Studio-and-Luau/LU-06-Rate-Limiting.md).

## Common mistakes
- Deducting currency on the client and telling the server the new total.
- Checking the price on the client only ("button greyed out") and trusting any request that arrives.
- Forgetting to reapply the upgrade after respawn: it works once, then silently disappears.

## Troubleshooting
| Symptom | Likely cause / fix |
|---|---|
| Upgrade lost after dying | Reapply from player data in `CharacterAdded`. |
| `InvokeServer` hangs | The server handler errored or never returned; `OnServerInvoke` must always return. |
| Coins negative in logs | Check-then-yield-then-deduct ordering (see analysis); deduct first. |

## Reusable procedure (ours)
1. Create one remote per action in ReplicatedStorage; name it after the verb (`RequestPurchase`).
2. Server handler: validate argument types → rate-limit → read price from a server table (never from the client) → check funds → **deduct** → apply the effect → return the result.
3. Keep anything that can yield (character waits, DataStore calls) after the deduction, or re-check funds after the yield.
4. Client: disable the button while waiting, show success or denial from the returned value; never compute the balance.
5. Reapply persistent effects on `CharacterAdded`.

## Exercise
Build a two-item shop (speed, jump) with one remote. Prices live in a server ModuleScript. Add a 0.5 s per-player cooldown.

### Acceptance criteria
- [ ] Sending a negative or string item id from the command bar does nothing and is logged.
- [ ] Spamming the button 20 times with exactly one item's worth of coins buys exactly one item.
- [ ] Upgrades persist across a respawn.
- [ ] The shop logic passes the same kind of test as `ShopServer` in [LU-07](../07-Roblox-Studio-and-Luau/LU-07-Currency-and-Shop.md).

## Related
- [LU-04 Remotes](../07-Roblox-Studio-and-Luau/LU-04-Remotes.md)
- [LU-05 Server Validation](../07-Roblox-Studio-and-Luau/LU-05-Server-Validation.md)
- [LU-07 Currency and Shop](../07-Roblox-Studio-and-Luau/LU-07-Currency-and-Shop.md)
- [R04 Upgrade Purchase Interaction](../18-Skill-Training/Design-Recipes/R04-Upgrade-Purchase-Interaction.md)
