---
title: "TUT-07 — Detect hits with raycasts and validate them"
tags: [tutorial, luau, raycast, combat, validation]
note_type: "tutorial-procedure"
source: "https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/detect-hits"
source_author: "Roblox Creator Documentation"
licence: "Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution."
accessed: "2026-10-24"
evidence: "[SRC] = what the tutorial says; [ANALYSIS] = our reading; [SIM-TESTED] = reproduced in a Luau simulation; [HYP] = untested"
---

# TUT-07 — Detect hits with raycasts and validate them

**Skill:** Cast rays for hits on the client, then re-check angle, distance and obstruction on the server before applying damage.

## Source and access
- Source: [https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/detect-hits](https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/detect-hits)
- Author: Roblox (official documentation). Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution.
- Access: Read the Markdown source of the page from the public Roblox/creator-docs repository (commit 4e795e6), accessed 2026-10-24. Images, videos and the linked sample places (.rbxl) were **not** opened, and no step was performed in Roblox Studio.

## Workflow in the tutorial [SRC]
1. `castLaserRay()` raycasts from the camera, excluding the shooter's character; `RaycastResult` gives Instance, Position, Normal, Material, Distance.
2. The server checks: the ray direction is within `BLAST_ANGLE_SANITY_CHECK_TOLERANCE_DEGREES` of the expected angle; the hit position is within the distance tolerance of the target character; `isRayPathObstructed` re-casts to see if a wall is in between.
3. Damage comes from the blaster's `damagePerHit` attribute and is applied with `TakeDamage`, which respects ForceFields.

## Decisions and the reasons the tutorial gives [SRC]
| Decision | Reason |
|---|---|
| Raycast ignores `CanCollide` by default. | The tutorial points out decorative parts must be excluded with `CanQuery` or filters. |
| Three independent checks. | Each blocks a different cheat: aim snapping, teleported hits, shooting through walls. |
| `TakeDamage` instead of setting Health. | Respects spawn protection. |

## Our analysis
- **[ANALYSIS]** The obstruction check is the one most hobby games skip; without it, client-reported hits through walls are accepted.
- **[ANALYSIS]** Use `CanQuery = false` on foliage and glass you want shots to pass through, and say so in the level design notes ([Environmental Communication](../12-Level-Design/Environmental-Communication.md)).

## Common mistakes
- Not excluding the shooter → rays hit your own arm.
- Trusting the client's claimed target without re-casting.
- Forgetting decorative parts block rays (CanQuery).

## Troubleshooting
| Symptom | Likely cause / fix |
|---|---|
| Shots stop at invisible parts | Set `CanQuery = false` or add them to the filter. |
| Hits rejected near corners | Obstruction re-cast from a slightly different origin; add a small tolerance. |

## Reusable procedure (ours)
1. Client: raycast with a filter excluding self; send origin, direction, claimed hit.
2. Server: validate angle, distance to target, and obstruction with its own raycast.
3. Apply damage with `TakeDamage`; show hit markers from the server's confirmation.

## Exercise
Write the three checks as pure functions and unit-test them with the [TestKit](../07-Roblox-Studio-and-Luau/LU-25-Testing-Strategy.md) (no engine needed for angle and distance math).

### Acceptance criteria
- [ ] Angle check rejects a 30° deviation and accepts 2°.
- [ ] Distance check rejects a hit 50 studs from the target.
- [ ] Each check has at least one passing and one failing test.

## Related
- [LU-05 Server Validation](../07-Roblox-Studio-and-Luau/LU-05-Server-Validation.md)
- [LU-25 Testing Strategy](../07-Roblox-Studio-and-Luau/LU-25-Testing-Strategy.md)
