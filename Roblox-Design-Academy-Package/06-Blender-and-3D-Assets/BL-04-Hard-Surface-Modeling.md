---
title: "BL-04 — Hard-surface modeling for game props"
tags: [blender, hard-surface, bevel, normals]
note_type: "procedure"
evidence: "Blender 5.2 manual + academy exercises"
---

# BL-04 — Hard-surface modeling for game props

## Purpose
Mechanical and manufactured objects (chests, tools, machines, buildings) with crisp, believable edges at low polygon cost.

## Key technique: bevel + weighted normals (Blender 5.2 manual)
- **Bevel modifier, Limit Method = Angle:** "only bevels edges whose angle … is less than 180 degrees", so sharp edges get bevelled and smooth surfaces stay untouched.
- **Harden Normals** (Bevel > Shading): "the per-vertex face normals of the bevel faces are adjusted to match the surrounding faces … keep the surrounding faces flat … with the bevel faces shading smoothly into them." It needs custom split normals (Blender adds the attribute automatically).
- **Weighted Normal modifier:** weights normals by face area and keeps large faces flat. *Keep Sharp* preserves sharp edges.
- Result: 1–2 bevel segments look like a smooth rounded edge without subdivision support loops.

In code: [`rbx_shapes.bevel(ob, width, segments, angle_deg, harden=True)`](../_tools/blender/rbx_shapes.py) adds Bevel (Angle limit, harden normals), sets smooth shading, then adds Weighted Normal (Keep Sharp).

## Bevel width carries the style
| Style | Bevel width (relative to object size) | Segments | Example |
|---|---|---|---|
| Premium/realistic | 1–2% | 1–2 | Premium chest: 0.03 on a 2.6-stud body |
| Stylized standard | 3–6% | 2–3 | — |
| Toy/chunky | 8–12% | 3–4 | Toy chest: 0.28 on a 3-stud body |
These ratios come from the exercises here, not from an external standard. Use them as calibrated starting points.

## Procedure
1. Model clean base forms with real thickness: no zero-thickness planes, which Roblox requires.
2. Separate parts by material role (wood, metal). Roblox allows one material per mesh, so either keep them as separate meshes or use a palette texture ([BL-08](BL-08-Materials-and-Color.md)).
3. Add the bevel by angle, then Weighted Normal; inspect the shading under a single strong light.
4. Overlap parts slightly (trim into body) instead of making them touch exactly. Exact contact plus bevels leaves visible gaps. *Real case:* the cartoon chest's hinge gap ([FC-BL-05](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-BL-05-Exact-Contact-Leaves-Gap.md)).
5. Apply modifiers before export (or rely on "apply modifiers" in the exporter). QC the evaluated mesh.

## Custom normals and export (to verify)
FBX export with `mesh_smooth_type='FACE'` writes smoothing; custom normals are exported in the mesh normals. Whether Studio keeps the hardened normals exactly was **not verified here**. Check the shading in Studio after import.

## Common mistakes
- Bevel width that is too uniform across parts of very different size (a tiny lock with the same bevel as the body).
- Smooth shading without weighted/hardened normals → gradients across big flat faces.
- Booleans that leave n-gons and slivers. Clean up after.

## Acceptance criteria
Big faces shade flat; bevels catch the highlight; no shading gradients across flat faces in the 3/4 render; QC passes.

## Sources
Accessed 2026-10-24. Roblox pages from the creator-docs repository (commit 4e795e6); Blender pages from the 5.2 LTS manual (the URLs use `latest`, which served 5.2 on that date).
- Blender manual: [Bevel Modifier](https://docs.blender.org/manual/en/latest/modeling/modifiers/generate/bevel.html)
- Blender manual: [Weighted Normal Modifier](https://docs.blender.org/manual/en/latest/modeling/modifiers/normals/weighted_normal.html)
