---
title: "CL-13 — Blender Asset and Export"
tags: [checklist, blender, 3d, export]
note_type: "checklist"
---

# CL-13 — Blender Asset and Export

Mark each item ✅ verified (write how), ❌ failed (write what), ⬜ not checked. **Never tick an item you did not check.** Items marked *(auto)* are checked by `_tools/blender/rbx_qc.py`; attach its JSON. The source of each rule is in brackets: **[Roblox]** spec, **[doc]** documented guidance, **[house]** academy rule.

## Shape and read
- [ ] Reads correctly as a silhouette at gameplay distance (front, side, gameplay views) [house]
- [ ] Recognisable at the smallest size it will appear on screen (`render_at_size`) [house]
- [ ] Detail is at silhouette level: no geometry players cannot see [doc]
- [ ] Not a copy of a reference asset's identity [house]

## Mesh
- [ ] Triangle count within the asset's budget (and under the Roblox per-mesh limit) *(auto)* [Roblox/house]
- [ ] No n-gons (or triangulated deliberately) *(auto)* [house]
- [ ] Watertight where it should be: no non-manifold edges, loose verts, zero-area faces *(auto)* [house]
- [ ] Normals face outward (skipped on open cards) *(auto)* [house]
- [ ] Parts that touch overlap slightly, so no seam shows after bevels ([FC-BL-05](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-BL-05-Exact-Contact-Leaves-Gap.md)) [house]

## Transforms and pivot
- [ ] Scale and rotation applied *(auto)* [house]
- [ ] Pivot where the asset is used: base (placed), centre (spins), grip (held), kit corner (modular) *(auto)* [doc]
- [ ] View layer updated before reading transforms in scripts ([FC-BL-06](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-BL-06-Stale-Matrix-World.md)) [house]
- [ ] Modular pieces: consistent pivot and sizes divisible by the smallest module ([TUT-09](../16-Tutorials-and-Workflows/TUT-09-Polished-Assets-Trim-Sheets-Modular-Kits.md)) [doc]

## Materials and UVs
- [ ] ≤ 1 material per mesh unless justified *(auto)* [house]
- [ ] One UV set, within 0–1 unless the texture tiles *(auto)* [Roblox texture spec/house]
- [ ] Texture size justified (≤ 1024 for environment textures; cost rises near the maximum) [doc]

## Export
- [ ] FBX: unit scale and axes per [BL-15](../06-Blender-and-3D-Assets/BL-15-Export-Settings.md); no leaf bones; textures handled [doc/house]
- [ ] Round-trip re-import dimensions match (`round_trip_dimensions`) [house]
- [ ] Names follow [BL-12](../06-Blender-and-3D-Assets/BL-12-Asset-Organization-and-Naming.md); no duplicate re-imports creating new asset IDs [doc]
- [ ] Collision fidelity chosen per use ([BL-17](../06-Blender-and-3D-Assets/BL-17-Collision-Fidelity.md)) [doc]
- [ ] **Studio import checked**, or written down as *not verified* [house]

## Process
- [ ] Criteria written before v1 ([Self-Critique Loop](../18-Skill-Training/Self-Critique-Loop.md))
- [ ] Every version logged, failed ones included
- [ ] Full QC re-run after the last fix

## Based on
[BL-00 Pipeline](../06-Blender-and-3D-Assets/BL-00-Blender-to-Roblox-Pipeline.md) · [BL-20 Modeling Quality Framework](../06-Blender-and-3D-Assets/BL-20-Modeling-Quality-Framework.md) · [BL-16 Performance Budgets](../06-Blender-and-3D-Assets/BL-16-Performance-Budgets.md)
