---
title: "TUT-04 — Add rounds with team points (laser tag curriculum)"
tags: [tutorial, luau, rounds, teams, attributes]
note_type: "tutorial-procedure"
source: "https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/add-rounds"
source_author: "Roblox Creator Documentation"
licence: "Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution."
accessed: "2026-10-24"
evidence: "[SRC] = what the tutorial says; [ANALYSIS] = our reading; [SIM-TESTED] = reproduced in a Luau simulation; [HYP] = untested"
---

# TUT-04 — Add rounds with team points (laser tag curriculum)

**Skill:** Run a repeating match loop: reset scores, open team spawns, play until a goal or timer, return everyone to a lobby.

## Source and access
- Source: [https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/add-rounds](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/add-rounds)
- Author: Roblox (official documentation). Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution.
- Access: Read the Markdown source of the page from the public Roblox/creator-docs repository (commit 4e795e6), accessed 2026-10-24. Images, videos and the linked sample places (.rbxl) were **not** opened, and no step was performed in Roblox Studio.

## Workflow in the tutorial [SRC]
1. `startRoundLoopAsync()` resets each Team's `teamPoints` **attribute** to 0.
2. It sets the lobby `SpawnLocation.Neutral = false` so players respawn only at their team zones, then spawns everyone.
3. Hits add points to the team attribute; the HUD listens with `GetAttributeChangedSignal`.
4. When a team reaches the goal (or time runs out) the round ends: `Neutral = true` again, players are reloaded into the lobby, and the loop waits for the next round.

## Decisions and the reasons the tutorial gives [SRC]
| Decision | Reason |
|---|---|
| Scores as attributes on Team objects. | Attributes replicate to clients, so the HUD can display them without a custom remote. |
| Toggle the Neutral spawn instead of moving players by CFrame. | Uses the engine's spawn system; respawns during the round go to the right place automatically. |
| Store points per team, not only on players. | The tutorial notes points must survive players leaving mid-round. |

## Our analysis
- **[ANALYSIS]** The loop is an implicit state machine (intermission → active → ended). Making the states explicit, as in our tested [RoundMachine](../07-Roblox-Studio-and-Luau/LU-11-Round-Loop.md), makes edge cases testable: what if all players leave during *active*?
- **[ANALYSIS]** Replicated attributes are writable only by the server, so clients can display but not forge team points — a safe default for scoreboards.
- **[HYP]** For low-population servers, a fixed point goal can make rounds drag; scale the goal with player count ([CL-10](../23-Quality-Checklists/CL-10-Multiplayer-and-Low-Population.md)).

## Common mistakes
- Forgetting to re-enable the Neutral spawn: players who join between rounds spawn in a team zone.
- Using `wait()` loops that drift; use `task.wait` and a deadline timestamp.
- Not handling a round where one team empties.

## Troubleshooting
| Symptom | Likely cause / fix |
|---|---|
| HUD shows stale score after rejoining | Read the attribute once on setup, then subscribe to changes. |
| Players spawn in the wrong place | Check `Neutral`, `TeamColor` and `AllowTeamChangeOnTouch` on each SpawnLocation. |

## Reusable procedure (ours)
1. Write the states and transitions down first (table).
2. Keep round data on server-owned instances (attributes) so clients read it for free.
3. Use spawn properties for placement; reload characters at state changes.
4. Handle: player joins mid-round, team empties, server has 1 player.
5. End every round with a results moment ([AV-13 Victory](../08-Animation-and-Game-Feel/Recipes/AV-13-Victory.md)).

## Exercise
Implement a 3-state round loop (Intermission 10 s, Active 60 s, Results 5 s) for 'Obsidian Rush' from the [Core Loop Library](../03-Core-Gameplay-Loops/Core-Loop-Library.md).

### Acceptance criteria
- [ ] A player joining during Active waits in the lobby or joins a team according to a stated rule.
- [ ] If all players leave, the loop returns to Intermission without errors.
- [ ] State transitions are logged once each.

## Related
- [LU-11 Round Loop](../07-Roblox-Studio-and-Luau/LU-11-Round-Loop.md)
- [Loading, Death and Round Transitions](../01-UI-UX/Loading-Death-and-Round-Transitions.md)
