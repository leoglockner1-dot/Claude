---
title: "TUT-10 — Optimize an environment (parameters, duplicates, geometry, transparency)"
tags: [tutorial, performance, environment-art, optimization]
note_type: "tutorial-procedure"
source: "https://create.roblox.com/docs/tutorials/curriculums/environmental-art/optimize-your-experience"
source_author: "Roblox Creator Documentation"
licence: "Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution."
accessed: "2026-10-24"
evidence: "[SRC] = what the tutorial says; [ANALYSIS] = our reading; [SIM-TESTED] = reproduced in a Luau simulation; [HYP] = untested"
---

# TUT-10 — Optimize an environment (parameters, duplicates, geometry, transparency)

**Skill:** Reduce memory and GPU cost of a finished environment without changing gameplay.

## Source and access
- Source: [https://create.roblox.com/docs/tutorials/curriculums/environmental-art/optimize-your-experience](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/optimize-your-experience) · [https://create.roblox.com/docs/tutorials/curriculums/environmental-art/assemble-an-asset-library](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/assemble-an-asset-library)
- Author: Roblox (official documentation). Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution.
- Access: Read the Markdown source of the page from the public Roblox/creator-docs repository (commit 4e795e6), accessed 2026-10-24. Images, videos and the linked sample places (.rbxl) were **not** opened, and no step was performed in Roblox Studio.

## Workflow in the tutorial [SRC]
1. Review physics/render parameters per asset: e.g. disable `CastShadow` on edge foliage; asset-library page covers Anchored, CanCollide, CanTouch, CanQuery, CastShadow, DoubleSided, CollisionFidelity, RenderFidelity.
2. Remove duplicate textures/meshes: identical imports get different asset IDs and cost extra; use packages so instances share one ID.
3. Optimize geometry: combine groups into one asset (the tower example: 8 draw calls → 1) **near the end**, because combined assets can't be edited separately; reduce polygon counts; update packages instead of creating new IDs.
4. Delete layered transparencies to reduce overdraw (e.g. stacked foliage planes).
5. Use the MicroProfiler to see where frame time goes.

## Decisions and the reasons the tutorial gives [SRC]
| Decision | Reason |
|---|---|
| Measure first (MicroProfiler). | Optimize what is expensive, not what looks suspicious. |
| Combine late. | Combining removes per-part editing. |

## Our analysis
- **[ANALYSIS]** Duplicate asset IDs are a workflow failure, not an art failure: they come from re-importing iterations. Fix it at the source with packages and a naming convention ([BL-12](../06-Blender-and-3D-Assets/BL-12-Asset-Organization-and-Naming.md)).
- **[ANALYSIS]** Overdraw from layered transparency matches our VFX advice to limit overlapping translucent particles ([AV-23](../08-Animation-and-Game-Feel/Recipes/AV-23-Performance-Aware-Effects.md)).

## Common mistakes
- Combining meshes early and then needing to recolour one part.
- CanTouch/CanQuery left on for thousands of decorative parts.
- Precise collision fidelity on decorative meshes.

## Troubleshooting
| Symptom | Likely cause / fix |
|---|---|
| Low FPS near foliage | Overdraw; remove layered transparent planes or reduce density. |
| Memory high despite few unique assets | Duplicate IDs from re-imports; replace with package instances. |

## Reusable procedure (ours)
1. Profile on a low-end target (MicroProfiler).
2. Parameters pass: CanTouch/CanQuery/CastShadow/CollisionFidelity per asset type.
3. Duplicate pass: one ID per unique mesh/texture.
4. Geometry pass: combine static groups; reduce tri counts.
5. Transparency pass.
6. Re-profile and record before/after numbers.

## Exercise
Take a scene of 200 decorative parts; apply the parameter pass and record the change.

### Acceptance criteria
- [ ] A before/after table of MicroProfiler frame time or draw calls exists.
- [ ] No gameplay part lost collision it needs (walk the level).

## Related
- [CL-09 Performance](../23-Quality-Checklists/CL-09-Performance.md)
- [BL-16 Performance Budgets](../06-Blender-and-3D-Assets/BL-16-Performance-Budgets.md)
- [BL-17 Collision Fidelity](../06-Blender-and-3D-Assets/BL-17-Collision-Fidelity.md)
- [LU-23 Performance Profiling](../07-Roblox-Studio-and-Luau/LU-23-Performance-Profiling.md)
