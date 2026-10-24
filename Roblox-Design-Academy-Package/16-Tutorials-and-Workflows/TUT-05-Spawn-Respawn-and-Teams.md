---
title: "TUT-05 — Spawn, respawn and team setup"
tags: [tutorial, luau, spawning, teams, forcefield]
note_type: "tutorial-procedure"
source: "https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/spawn-respawn"
source_author: "Roblox Creator Documentation"
licence: "Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution."
accessed: "2026-10-24"
evidence: "[SRC] = what the tutorial says; [ANALYSIS] = our reading; [SIM-TESTED] = reproduced in a Luau simulation; [HYP] = untested"
---

# TUT-05 — Spawn, respawn and team setup

**Skill:** Control where and how players appear, including spawn protection and team assignment.

## Source and access
- Source: [https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/spawn-respawn](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/spawn-respawn) · [https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/create-teams](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/create-teams)
- Author: Roblox (official documentation). Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution.
- Access: Read the Markdown source of the page from the public Roblox/creator-docs repository (commit 4e795e6), accessed 2026-10-24. Images, videos and the linked sample places (.rbxl) were **not** opened, and no step was performed in Roblox Studio.

## Workflow in the tutorial [SRC]
1. Teams are created under the `Teams` service with distinct `TeamColor`s matching SpawnLocations.
2. SpawnLocations provide a ForceField for a short time after spawning; the curriculum customises how that looks in first person.
3. Damage elsewhere in the curriculum uses `Humanoid:TakeDamage`, which respects the ForceField.
4. Player connections created for a character are stored per player and disconnected when the player leaves.

## Decisions and the reasons the tutorial gives [SRC]
| Decision | Reason |
|---|---|
| Spawn protection via the built-in ForceField. | Prevents spawn-camping without extra code; `TakeDamage` already honours it. |
| Store connections per player. | Avoids leaks and duplicate handlers on respawn. |

## Our analysis
- **[ANALYSIS]** Setting `Health` directly (as in TUT-02) bypasses ForceFields; `TakeDamage` does not. Choose deliberately: kill volumes may *want* to ignore protection, weapons should not.
- **[ANALYSIS]** The per-player connection table is the same pattern as our [Signal + janitor](../07-Roblox-Studio-and-Luau/LU-20-Signals-and-Cleanup.md) module.

## Common mistakes
- Team colours not matching SpawnLocation `TeamColor` → everyone spawns at the default spawn.
- Connecting `CharacterAdded` handlers inside `CharacterAdded` → handlers multiply each respawn.

## Troubleshooting
| Symptom | Likely cause / fix |
|---|---|
| Damage ignored right after spawn | Expected: ForceField. Shorten `SpawnLocation.Duration` if needed. |
| Handler runs twice after respawn | Connections not cleaned up; store and disconnect. |

## Reusable procedure (ours)
1. Create Teams and matching SpawnLocations.
2. Decide spawn protection duration and how it looks.
3. Route all weapon damage through `TakeDamage`.
4. Per player: store connections; disconnect on `PlayerRemoving`.

## Exercise
Two teams, one lobby, 3 s spawn protection shown by a client-side outline instead of the default bubble.

### Acceptance criteria
- [ ] Weapon damage is ignored for 3 s after spawn; lava (TUT-02) still kills, by design, and this is documented.
- [ ] After 10 respawns, the number of connections per player is constant (print a count).

## Related
- [LU-20 Signals and Cleanup](../07-Roblox-Studio-and-Luau/LU-20-Signals-and-Cleanup.md)
- [Low-Population Design](../13-Onboarding-and-Multiplayer/Multiplayer/Low-Population-Design.md)
