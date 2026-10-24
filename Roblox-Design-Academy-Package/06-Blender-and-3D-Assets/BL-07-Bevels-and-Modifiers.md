---
title: "BL-07 — Bevels and modifiers (intentional use)"
tags: [blender, modifiers, bevel, workflow]
note_type: "procedure"
evidence: "Blender 5.2 manual + bpy introspection + exercises"
---

# BL-07 — Bevels and modifiers (intentional use)

## Modifiers that matter for Roblox props
| Modifier | Use | Watch out for |
|---|---|---|
| **Mirror** | Symmetric objects; edit one half | Apply before UV-unwrapping if the UVs must differ |
| **Bevel** (Limit: Angle; Harden Normals) | Edge highlights | Overlaps on thin parts → *Clamp Overlap* (manual: "limits the width … so that edges cannot cause overlapping intersections") |
| **Weighted Normal** (Keep Sharp) | Flat shading on big faces with smooth bevels | Needs smooth shading on the faces |
| **Solidify** | Give thickness to planes (Roblox needs volume) | Inner faces count toward triangles |
| **Array** | Repeated planks, fence posts, chain links | Apply it, or export with modifiers applied |
| **Decimate** (Collapse / Un-Subdivide / Planar) | Reduce triangles; Planar for flat-surface forms | Collapse can wreck UVs and silhouettes; check the silhouette after |
| **Boolean** | Cut holes and windows | Creates n-gons and slivers; clean up after |
| **Wireframe** | Inspection renders ("wire over clay") | Not for export |
| **Smooth by Angle** | Auto smooth in Blender ≥ 4.1 | Pinned last |
`bpy` in Blender 5.2.3 lists 50+ modifier types. The list above is what most Roblox props need.

## Order matters
Typical stack: Mirror → Boolean → Bevel → Weighted Normal → (Smooth by Angle last). Bevel after Boolean, so the cut edges get bevelled too. Weighted Normal after Bevel, so it sees the final faces.

## Apply or keep?
- Keep modifiers live while designing; apply at export (`use_mesh_modifiers=True` in the FBX exporter) or explicitly with `rbx_shapes.apply_modifiers` when later steps need the final geometry (joining, QC, UV packing).
- **Always QC the evaluated mesh**, which is what gets exported. `rbx_qc` evaluates through the depsgraph.

## Acceptance criteria
Each modifier has a reason; the stack order is documented in the asset note; QC runs on the evaluated result.
