---
title: "TUT-13 — Save player data (and the load-failure trap)"
tags: [tutorial, luau, datastore, persistence, data-loss]
note_type: "tutorial-procedure"
source: "https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/save-player-data"
source_author: "Roblox Creator Documentation"
licence: "Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution."
accessed: "2026-10-24"
evidence: "[SRC] = what the tutorial says; [ANALYSIS] = our reading; [SIM-TESTED] = reproduced in a Luau simulation; [HYP] = untested"
---

# TUT-13 — Save player data (and the load-failure trap)

**Skill:** Persist player progress with DataStoreService: load on join, autosave, save on leave, store positions as tables.

## Source and access
- Source: [https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/save-player-data](https://create.roblox.com/docs/tutorials/use-case-tutorials/data-storage/save-player-data)
- Author: Roblox (official documentation). Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution.
- Access: Read the Markdown source of the page from the public Roblox/creator-docs repository (commit 4e795e6), accessed 2026-10-24. Images, videos and the linked sample places (.rbxl) were **not** opened, and no step was performed in Roblox Studio.

## Workflow in the tutorial [SRC]
1. Enable Studio access to API services; data store calls run only on the server (the tutorial explains why the client is blocked).
2. `saveGold` wraps `SetAsync` in `pcall` and warns on failure; load wraps `GetAsync` in `pcall`; on failure it alerts the player.
3. Autosave every 30 s in a coroutine loop while `player.Parent` is set; save again on `PlayerRemoving`.
4. Positions are saved as `{X, Y, Z}` tables (data stores can't hold Vector3/CFrame) on `CharacterRemoving` and restored with `PivotTo` on `CharacterAdded`.

## Decisions and the reasons the tutorial gives [SRC]
| Decision | Reason |
|---|---|
| Server-only access. | Clients could steal or overwrite other players' data otherwise. |
| Autosave plus save on leave. | Leave-only saving loses data on crashes. |
| Tables for vectors. | Only basic types can be stored. |

## Our analysis
- **[SIM-TESTED] Failed load → overwritten save.** If `GetAsync` fails, `playerGold[userId]` stays nil — but collecting a chunk runs `(playerGold[userId] or 0) + GOLD_VALUE`, creating an entry, and the autosave then calls `SetAsync` with that small number. Ported in `_tools/luau/tests/tutorial_repros.luau`: a stored 500 became **10** after one failed load, one chunk and one autosave. A `loaded` flag that gates earning and saving keeps 500. Not reproduced in Studio; it needs a real DataStore read failure, which is rare but documented as possible.
- **[ANALYSIS] No `game:BindToClose`.** The final script has no shutdown handler, so on server shutdown up to 30 s of progress can be lost (PlayerRemoving saves may not finish). Roblox's *Player data and purchasing* page describes a `BindToClose` callback that saves and releases session locks on shutdown.
- **[ANALYSIS] `SetAsync` without session locking.** Two servers (quick server hop) can write over each other. `UpdateAsync` or a session lock is the safer pattern — implemented and tested in our [PlayerData module](../07-Roblox-Studio-and-Luau/LU-08-Player-Data-Persistence.md).
- **[ANALYSIS]** Saving position on `CharacterRemoving` also fires on death, so players can be restored at the spot where they died (e.g. in lava). Validate the saved position (inside map bounds, not in a hazard) before `PivotTo`.
- **[ANALYSIS]** Gold collection here is `Touched`-based (see [TUT-02](TUT-02-Player-Hazards-and-Collectibles.md) on range exploits).

## Common mistakes
- Saving after a failed load (this tutorial's trap).
- No `BindToClose`.
- Saving every change instead of batching → throttled requests.
- Saving Instances or Vector3s directly.

## Troubleshooting
| Symptom | Likely cause / fix |
|---|---|
| `StudioAccessToApisNotAllowed` | Enable API services in Game Settings → Security. |
| Data reset for some players | Look for saves that run when the load failed; add a loaded flag. |
| Request throttling warnings | Lower autosave frequency; respect budgets (`GetRequestBudgetForRequestType`). |

## Reusable procedure (ours)
1. Load with retries ([Retry](../07-Roblox-Studio-and-Luau/LU-21-Error-Handling.md)); on final failure mark the session **not loaded** and block saving (and ideally earning).
2. Keep data in a server table; mark dirty on change.
3. Autosave dirty sessions on an interval; save on leave and in `BindToClose`.
4. Use `UpdateAsync`/session locking for anything valuable.
5. Store plain tables; version the schema.

## Exercise
Run `bash _tools/luau/run_tests.sh <luau-bin>` and read both GoldManager repro specs; then add a `BindToClose` step to the fixed version in your own place.

### Acceptance criteria
- [ ] Your implementation never writes when the load failed (simulate by forcing `GetAsync` to error).
- [ ] Shutting down a server in Studio with a changed value saves it.
- [ ] Rejoining after dying in a hazard does not respawn you inside it.

## Related
- [LU-08 Player Data Persistence](../07-Roblox-Studio-and-Luau/LU-08-Player-Data-Persistence.md)
- [LU-21 Error Handling](../07-Roblox-Studio-and-Luau/LU-21-Error-Handling.md)
