---
title: "BL-03 — Low-poly and stylized modeling workflow"
tags: [blender, low-poly, stylized, workflow]
note_type: "procedure"
evidence: "official Blender/Roblox docs + academy exercises"
---

# BL-03 — Low-poly and stylized modeling workflow

## Purpose
Efficient stylized props that read clearly and stay well under Roblox budgets.

## Workflow
1. **Blockout** with primitives at real stud scale (Unit System None, 1 unit = 1 stud). Put a 5-stud reference capsule in the scene for scale.
2. **Silhouette pass** ([BL-02](BL-02-Shape-Language-Silhouette-Proportion.md)).
3. **Form pass:** Edit Mode tools that Roblox's Blender guide highlights: Extrude (E), Inset (I), Loop Cut, Bevel (Ctrl+B), Bridge Edge Loops, Fill (Alt+F) and Make Face (F) to keep the mesh watertight, and Dissolve to remove geometry without holes.
4. **Style choice: faceted or smooth.**
   - *Faceted low-poly:* flat shading, few large planes. Use Decimate **Planar** (it "reduces details on forms comprised of mainly flat surfaces", per the Blender 5.2 manual), or limited dissolve as in `rbx_shapes.rock`.
   - *Soft/toy:* large bevels with 3–4 segments and smooth shading.
5. **Detail budget pass:** add only details that read at the gameplay distance; remove the rest.
6. **Clean up:** merge by distance, delete loose, recalculate normals (Shift+N), no n-gons. Run [`rbx_qc`](../_tools/blender/rbx_qc.py).

## Facet scale controls the style (evidence)
In [BL-EX-01](Exercises/BL-EX-01-Stylized-Rocks.md), the same noise displacement with `detail=2, chunk=0.35` gave many small facets (reads "low-poly sphere"). `detail=1, chunk=0.6` gave fewer, bigger planes (reads "stylized rock"). Facet size, not polygon count, defines the look.

## Common mistakes
- Uniform tiny facets everywhere (the "ugly low-poly sphere" look).
- Subdividing for smoothness and then flat shading it.
- Leaving hidden bottom faces on ground props: wasted triangles. The rock builder bisects at the ground and fills the cut, so the base is flat and closed (watertight, as the spec requires).

## Acceptance criteria
Passes [BL-20](BL-20-Modeling-Quality-Framework.md) visual and geometry categories; triangle count noted.
