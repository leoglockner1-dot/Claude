---
title: "TUT-08 — Greybox an environment (three-lane map)"
tags: [tutorial, level-design, greybox, layout]
note_type: "tutorial-procedure"
source: "https://create.roblox.com/docs/tutorials/curriculums/environmental-art/greybox-your-environment"
source_author: "Roblox Creator Documentation"
licence: "Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution."
accessed: "2026-10-24"
evidence: "[SRC] = what the tutorial says; [ANALYSIS] = our reading; [SIM-TESTED] = reproduced in a Luau simulation; [HYP] = untested"
---

# TUT-08 — Greybox an environment (three-lane map)

**Skill:** Block out a playable space with simple parts and test it before any art is made.

## Source and access
- Source: [https://create.roblox.com/docs/tutorials/curriculums/environmental-art/greybox-your-environment](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/greybox-your-environment)
- Author: Roblox (official documentation). Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution.
- Access: Read the Markdown source of the page from the public Roblox/creator-docs repository (commit 4e795e6), accessed 2026-10-24. Images, videos and the linked sample places (.rbxl) were **not** opened, and no step was performed in Roblox Studio.

## Workflow in the tutorial [SRC]
1. Explains the three-lane layout: opposing spawn zones, interior/middle/exterior primary lanes, cross lanes, and **combat pockets** where cross lanes meet the middle lane.
2. Sets transform snapping to **5 studs and 90°** so geometry aligns.
3. Keeps every doorway and hallway at least **10 studs wide** and walls at least **10 studs tall**, so two players can pass and the camera fits.
4. Builds floors, elevation changes with wedges (to break sightlines), perimeter walls, spawn rooms and combat pockets; playtests throughout.

## Decisions and the reasons the tutorial gives [SRC]
| Decision | Reason |
|---|---|
| Greybox before art. | Layout problems are cheap to fix with blocks and expensive after modelling. |
| Snap to 5 studs. | Everything lines up, and later modular art (TUT-09) can follow the same grid. |
| Elevation changes. | Break long sightlines and create advantage positions. |

## Our analysis
- **[ANALYSIS]** The 5-stud grid is the link between level design and asset production: our [modular kit exercise](../06-Blender-and-3D-Assets/Exercises/BL-EX-09-Modular-Building-Kit.md) uses the same increments.
- **[HYP]** The 10-stud minimum is a good default for third-person Roblox cameras generally, not only shooters; test with the widest avatar scale.

## Common mistakes
- Detailing too early.
- Corridors under 10 studs → camera clipping and body-blocking.
- No sightline breaks → the longest lane dominates.

## Troubleshooting
| Symptom | Likely cause / fix |
|---|---|
| Camera clips into walls | Widen to ≥ 10 studs or raise ceilings. |
| One lane never used | It's longer or more exposed; shorten it or add cover. |

## Reusable procedure (ours)
1. Pick a layout pattern and draw it top-down.
2. Set snapping (5 studs, 90°).
3. Block floors → elevation → walls → spawns → encounter spaces.
4. Playtest with several players; mark problems on the map.
5. Iterate until routes are balanced, then hand off to art.

## Exercise
Greybox the island for 'Last Boat Out' (Core Loop Library): dock, 4 part locations, 2 lava-blockable paths.

### Acceptance criteria
- [ ] All corridors ≥ 10 studs wide; all geometry on the 5-stud grid.
- [ ] Each part location reachable by two routes.
- [ ] A top-down screenshot with routes annotated is saved next to the place file.

## Related
- [Environmental Communication](../12-Level-Design/Environmental-Communication.md)
