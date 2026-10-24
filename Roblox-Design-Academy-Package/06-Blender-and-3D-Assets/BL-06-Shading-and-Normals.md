---
title: "BL-06 — Shading and normals"
tags: [blender, normals, shading, version-sensitive]
note_type: "procedure"
evidence: "Blender 5.2 manual + bpy introspection"
---

# BL-06 — Shading and normals

## Facts (Blender 5.2 LTS manual, verified 2026-10-24)
- **Shade Flat / Shade Smooth** set per-face smoothing.
- **Shade Auto Smooth** "adds a Smooth By Angle Modifier to automatically set the sharpness of mesh edges based on the angle between the neighboring faces", pinned as the last modifier. **Version note:** before Blender 4.1, auto smooth was a mesh-data checkbox. Many tutorials still show it. In 5.2 use `object.shade_auto_smooth` or `object.shade_smooth_by_angle` (both exist, as confirmed by bpy introspection).
- **Custom split normals** are needed for Harden Normals (Bevel) and the Weighted Normal modifier.
- Normals editing tools (Edit Mode > Mesh > Normals): Flip, Recalculate, Set from Faces, Point to Target, Merge/Split/Average, Set Face Strength (used by Weighted Normal's *Face Influence*).

## Choosing a shading approach
| Look | Approach |
|---|---|
| Faceted low-poly (rocks, crystals, gems) | Shade Flat; every face shows as a plane |
| Rounded toy/cartoon | Shade Smooth plus enough segments in bevels/curves |
| Hard-surface with crisp edges | Smooth + Bevel (harden normals) + Weighted Normal ([BL-04](BL-04-Hard-Surface-Modeling.md)) |
| Mixed (smooth surfaces, sharp corners) | Shade Auto Smooth (angle ~30–40°) or mark edges Sharp |

## Diagnosing shading defects
- Dark gradient across a large flat face → smooth shading without weighted normals: add Weighted Normal or split edges.
- Black faces or patches → inverted normals: Shift+N. `rbx_qc` reports "faces pointing inward".
- A seam visible on a curved surface → sharp edge marked by mistake, or split vertices: merge by distance.

## Roblox note
Studio renders the normals stored in the imported mesh. Whether custom normals survive import exactly was **not verified** here. Inspect in Studio under the game's lighting.

## Sources
Accessed 2026-10-24. Roblox pages from the creator-docs repository (commit 4e795e6); Blender pages from the 5.2 LTS manual (the URLs use `latest`, which served 5.2 on that date).
- Blender manual: [Shading (object)](https://docs.blender.org/manual/en/latest/scene_layout/object/editing/shading.html)
- Blender manual: [Editing Normals](https://docs.blender.org/manual/en/latest/modeling/meshes/editing/mesh/normals.html)
- Blender manual: [Weighted Normal Modifier](https://docs.blender.org/manual/en/latest/modeling/modifiers/normals/weighted_normal.html)
- [bpy 5.2.3 on PyPI](https://pypi.org/project/bpy/) — operator and property names confirmed by introspection in this environment
