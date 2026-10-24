---
title: "Tutorial and Workflow Index"
tags: [tutorial, index, workflow]
note_type: "index"
---

# Tutorials and Workflows

16 official Roblox tutorials converted into reusable procedures. Each note separates **what the tutorial says [SRC]** from **our analysis [ANALYSIS]**, and gives a procedure, an exercise and acceptance criteria.

## How these were made (and what was not done)
- Text read from the Markdown source of the Roblox creator-docs repository (commit 4e795e6), accessed 2026-10-24. Docs prose is CC BY 4.0 and code samples MIT.
- **Not done:** images, videos and sample places were not opened, and **no step was performed in Roblox Studio**. Studio is not available in this environment.
- **Tested:** two defects found in tutorial code were reproduced by porting the logic to plain Luau (`_tools/luau/tests/tutorial_repros.luau`, 6 specs, all passing). These are simulations of the logic, not live Studio runs.
- **Not covered:** YouTube tutorials. Video pages are blocked by this environment's network policy, so no video tutorial was watched.

## Evidence labels
| Label | Meaning |
|---|---|
| [SRC] | Stated by the tutorial |
| [ANALYSIS] | Our interpretation of the tutorial's code or advice |
| [SIM-TESTED] | Reproduced in a Luau simulation in this package |
| [OBS — our exercise] | Observed in one of our own executed exercises |
| [HYP] | Untested suggestion |

## Notes
| Note | Tutorial | Topics | Defect reproduced |
|---|---|---|---|
| [TUT-01](TUT-01-Upgrade-Button-Server-Purchase.md) | Script an upgrade button (server-validated purchase) | luau, shop, remotes | yes |
| [TUT-02](TUT-02-Player-Hazards-and-Collectibles.md) | Create player hazards and touch collectibles | luau, touched, hazards | — |
| [TUT-03](TUT-03-Leaderstats-and-Player-Data.md) | Record and display player data (leaderstats) | luau, leaderstats, player-data | — |
| [TUT-04](TUT-04-Round-Loop-and-Team-Points.md) | Add rounds with team points (laser tag curriculum) | luau, rounds, teams | — |
| [TUT-05](TUT-05-Spawn-Respawn-and-Teams.md) | Spawn, respawn and team setup | luau, spawning, teams | — |
| [TUT-06](TUT-06-Blaster-Client-Server-Validation.md) | Implement blasters (client prediction, server validation) | luau, combat, validation | — |
| [TUT-07](TUT-07-Hit-Detection-Raycast-Validation.md) | Detect hits with raycasts and validate them | luau, raycast, combat | — |
| [TUT-08](TUT-08-Greybox-Three-Lane-Map.md) | Greybox an environment (three-lane map) | level-design, greybox, layout | — |
| [TUT-09](TUT-09-Polished-Assets-Trim-Sheets-Modular-Kits.md) | Develop polished assets: art style, textures, trim sheets, modular kits, props | environment-art, trim-sheets, modular-kit | — |
| [TUT-10](TUT-10-Optimize-Environment-Performance.md) | Optimize an environment (parameters, duplicates, geometry, transparency) | performance, environment-art, optimization | — |
| [TUT-11](TUT-11-UI-Visual-Hierarchy-and-Wireframes.md) | UI design curriculum: art style, visual hierarchy, wireframes, implementation | ui, wireframe, hierarchy | — |
| [TUT-12](TUT-12-HUD-Health-Meter.md) | Create a HUD health meter (safe areas, tweens, colour ramp) | ui, hud, tween | — |
| [TUT-13](TUT-13-Save-Player-Data-Safely.md) | Save player data (and the load-failure trap) | luau, datastore, persistence | yes |
| [TUT-14](TUT-14-Proximity-Prompts.md) | Proximity prompts for interactions | ui, interaction, prompts | — |
| [TUT-15](TUT-15-Particle-Explosion-Burst.md) | Use particles for explosions (burst with Emit) | vfx, particles, explosion | — |
| [TUT-16](TUT-16-In-Game-and-3D-Audio.md) | In-game sounds and 3D audio (positional, feedback, roll-off) | audio, sound, 3d-audio | — |

## Learning paths
- **Scripting fundamentals:** TUT-02 → TUT-03 → TUT-01 → TUT-13
- **Multiplayer combat:** TUT-05 → TUT-06 → TUT-07 → TUT-04
- **Environment art:** TUT-08 → TUT-09 → TUT-10
- **UI:** TUT-11 → TUT-12 → TUT-14
- **Feel:** TUT-15 → TUT-16, then the [AV recipes](../08-Animation-and-Game-Feel/Recipes/AV-Recipe-Index.md)

## Patterns across the tutorials
1. **Server authority is taught consistently**; the gaps are in ordering and failure paths (TUT-01 check-then-yield, TUT-13 save after a failed load), not in where code runs.
2. **The gameplay-scripting curriculum is the strongest on validation** (TUT-06, TUT-07): thresholds calibrated from logs, angle, distance and obstruction checks.
3. **Beginner tutorials use `Touched` and `GetChildren()` once** (TUT-02, TUT-13). That is fine for learning, but it needs tags and server distance checks in production.
4. **Art tutorials converge on grids and pivots** (TUT-08, TUT-09). The 5-stud module links level design to asset production.
5. **Feedback is rarely telegraphed.** The hazard and explosion tutorials kill instantly; add warning cues.

## Related
- [Luau Training Index](../07-Roblox-Studio-and-Luau/Luau-Training-Index.md)
- [Blender Training Index](../06-Blender-and-3D-Assets/Blender-Training-Index.md)
- [Failure and Correction Index](../15-Anti-Patterns-and-Failure-Cases/Failure-and-Correction-Index.md)
