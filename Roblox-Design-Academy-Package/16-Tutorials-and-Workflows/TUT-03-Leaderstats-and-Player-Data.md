---
title: "TUT-03 — Record and display player data (leaderstats)"
tags: [tutorial, luau, leaderstats, player-data]
note_type: "tutorial-procedure"
source: "https://create.roblox.com/docs/tutorials/curriculums/core/scripting/record-and-display-player-data"
source_author: "Roblox Creator Documentation"
licence: "Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution."
accessed: "2026-10-24"
evidence: "[SRC] = what the tutorial says; [ANALYSIS] = our reading; [SIM-TESTED] = reproduced in a Luau simulation; [HYP] = untested"
---

# TUT-03 — Record and display player data (leaderstats)

**Skill:** Keep per-player values in a server module and mirror them to the built-in leaderboard.

## Source and access
- Source: [https://create.roblox.com/docs/tutorials/curriculums/core/scripting/record-and-display-player-data](https://create.roblox.com/docs/tutorials/curriculums/core/scripting/record-and-display-player-data)
- Author: Roblox (official documentation). Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution.
- Access: Read the Markdown source of the page from the public Roblox/creator-docs repository (commit 4e795e6), accessed 2026-10-24. Images, videos and the linked sample places (.rbxl) were **not** opened, and no step was performed in Roblox Studio.

## Workflow in the tutorial [SRC]
1. A `PlayerData` ModuleScript on the server holds a table keyed by player, with `getValue`/`updateValue(player, key, fn)`.
2. A `Leaderboard` module creates a `leaderstats` Folder with `IntValue`s under each Player; Roblox shows these in the player list automatically.
3. Gameplay scripts change values only through the module, which then updates the leaderboard.

## Decisions and the reasons the tutorial gives [SRC]
| Decision | Reason |
|---|---|
| Data lives in a module table, the leaderboard is a view. | One source of truth; the UI can change without touching the data logic. |
| `updateValue` takes a function. | The read-modify-write happens in one place, which avoids lost updates between two scripts. |

## Our analysis
- **[ANALYSIS]** This is the right shape: the `leaderstats` values are display only. Games that read balances *back* from `leaderstats` (or from client UI) invite bugs.
- **[ANALYSIS]** The module does not persist data; it is session-only. Persistence is the separate [TUT-13](TUT-13-Save-Player-Data-Safely.md) workflow, and our tested [PlayerData module](../07-Roblox-Studio-and-Luau/LU-08-Player-Data-Persistence.md) adds a load-success flag that the tutorial chain lacks.
- **[ANALYSIS]** Clean up the table entry on `PlayerRemoving`, after saving, to avoid a slow memory leak on long-running servers.

## Common mistakes
- Naming the folder anything but exactly `leaderstats` (lowercase) — it won't show.
- Putting strings/large numbers in IntValue (use abbreviation in custom UI, [LU-27](../07-Roblox-Studio-and-Luau/LU-27-HUD-Number-Formatting.md)).
- More than ~4 stats: the player list gets crowded.

## Troubleshooting
| Symptom | Likely cause / fix |
|---|---|
| Stats don't appear | Folder created after the player list read it is fine; check the exact name and that it is parented to the Player. |
| Values differ between scripts | Someone writes the IntValue directly; route all writes through the module. |

## Reusable procedure (ours)
1. Server module owns the data table.
2. Expose get/update functions; `update` takes a transform function.
3. Mirror selected keys to `leaderstats` after every update.
4. On leave: save (if persistent), then clear the entry.

## Exercise
Add a `Deaths` stat incremented by the hazard from TUT-02, using only the module API.

### Acceptance criteria
- [ ] No script other than the module writes an IntValue.
- [ ] Deaths and Coins both show in the list and survive respawn.
- [ ] Leaving and rejoining in the same server session shows a fresh entry (no stale data).

## Related
- [LU-02 Project Architecture](../07-Roblox-Studio-and-Luau/LU-02-Project-Architecture.md)
- [LU-08 Player Data Persistence](../07-Roblox-Studio-and-Luau/LU-08-Player-Data-Persistence.md)
- [HUD Layouts](../01-UI-UX/HUD-Layouts.md)
