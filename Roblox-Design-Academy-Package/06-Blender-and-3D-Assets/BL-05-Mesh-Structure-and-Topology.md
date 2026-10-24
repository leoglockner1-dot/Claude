---
title: "BL-05 — Mesh structure and topology"
tags: [blender, topology, geometry, deformation]
note_type: "procedure"
evidence: "Roblox specs + Blender manual + academy QC findings"
---

# BL-05 — Mesh structure and topology

## What Roblox requires (art/modeling/specifications)
Watertight; no n-gons (quads where possible); volume (no zero thickness); ≤ 20,000 triangles per mesh. Rigs: ≤ 4 bone influences per vertex.

## Static props vs deforming meshes
| | Static prop | Deforming (rigged) mesh |
|---|---|---|
| Triangles OK? | Yes. Triangles are fine and the engine triangulates anyway | Avoid in bend areas |
| Quads | Optional | Needed for clean edge loops |
| Edge loops | Only where shape needs them | **At every joint**: 2–3 loops around elbows, knees, hinges, so they bend without collapsing |
| Poles (5+ edges at a vertex) | Harmless | Keep them out of bend zones |

## Real topology failures found by QC in this academy
| Defect | Where | Cause | Fix |
|---|---|---|---|
| N-gons (FAIL) | Half-cylinder lid caps, crystal base | Single cap face with 13+ or 6 vertices | Triangle fan from a centre vertex |
| Non-manifold edges (FAIL) | Same lids, after the first fix | Fan centre vertex sat on the bottom edge but the bottom quad did not use it → **T-junction** | Bottom split into two quads that share the centre vertex |
| Zero-area face (WARN) | Cartoon chest metal | Taper + bevel produced a degenerate face | `dissolve_degenerate` cleanup after modifiers |
Details: [FC-BL-03](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-BL-03-Ngon-Fix-Created-T-Junction.md). **Lesson:** a fix for one QC rule can break another. Re-run the full QC after every geometry fix.

## Procedure
1. Select > Select All by Trait > Non Manifold and Interior Faces, then fix.
2. Mesh > Clean Up > Merge by Distance, Delete Loose, Degenerate Dissolve.
3. Normals: Shift+N (Recalculate Outside); Face Orientation overlay (blue = out, red = in).
4. N-gons: Select > Select All by Trait > Faces by Sides (> 4), then triangulate or re-cut.
5. Run `rbx_qc` on the **evaluated** mesh (modifiers applied).

## Acceptance criteria
QC: 0 n-gons, 0 non-manifold edges, 0 inward faces, 0 loose vertices; deforming meshes show loops at every joint.

## Sources
Accessed 2026-10-24. Roblox pages from the creator-docs repository (commit 4e795e6); Blender pages from the 5.2 LTS manual (the URLs use `latest`, which served 5.2 on that date).
- [Mesh specifications](https://create.roblox.com/docs/art/modeling/specifications)
- Blender manual: [Mesh Structure](https://docs.blender.org/manual/en/latest/modeling/meshes/structure.html)
- Blender manual: [Editing Normals](https://docs.blender.org/manual/en/latest/modeling/meshes/editing/mesh/normals.html)
