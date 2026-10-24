---
title: "BL-20 — Modeling Quality Framework (four separate verdicts)"
tags: [blender, quality, rubric, critique, framework]
note_type: "framework"
evidence: "academy framework; applied with real renders in BL-EX-01..06"
---

# BL-20 — Modeling Quality Framework

**Rule zero: a beautiful render is not proof of a production-ready asset.** Judge four categories **separately**. Each has its own evidence, and an asset passes only when all four pass for its intended use.

| Category | Question | Evidence required | Tool in this academy |
|---|---|---|---|
| **1. Visual quality** | Does it read as the intended thing, at the intended distance, in the intended art direction? | Flat silhouette (front **and** gameplay angle), 3/4 view, downscaled renders (64/32 px), side-by-side with style references | `render_silhouette`, `render_at_size` |
| **2. Geometry quality** | Is the mesh fit for purpose: budget, topology, normals, no defects? | Wire-over-clay render, QC report (tris, n-gons, non-manifold, flipped faces, loose verts) | `rbx_qc.check_objects`, `render_views` (wire) |
| **3. Presentation quality** | Do the camera, light and background reveal the asset honestly? | Orthographic set + hero render, compared | `render_views` vs hero render |
| **4. Roblox integration** | Scale, pivot, collision, materials, organization, performance, and seen in Studio? | QC (scale/rotation applied, pivot, ≤1 material, UV set), FBX/GLB round trip, **Studio import check** | `rbx_qc`, `rbx_export.round_trip_dimensions`, Studio |

## 1. Visual quality checklist
- [ ] **Silhouette is distinctive.** The black silhouette alone identifies the object, at the **gameplay camera angle** (elevated 3/4), not just in front view. *Lesson from [BL-EX-04](Exercises/BL-EX-04-Treasure-Chests.md): the premium chest was a plain rectangle in front view and read correctly only at 3/4.*
- [ ] **Proportions are intentional.** Exaggeration (toy, cartoon) or restraint (premium) is a choice, applied consistently.
- [ ] **Primary / secondary / tertiary shapes** are balanced. Big shape first, then medium features, then small details; small details never break the primary read.
- [ ] **Readable at intended distance and size.** Check 64 px and 32 px versions. Rocks and props seen from far away need fewer, larger forms.
- [ ] **Fits the art direction.** Bevel size, colour saturation and edge sharpness match the game's other assets ([Art Direction Styles](../11-Visual-Identity/Art-Direction-Styles.md)).
- [ ] **Coherent materials and colours.** Material roles are distinguishable: wood vs metal vs treasure.
- [ ] **No unnecessary noise.** Every detail earns its triangles and pixels.

## 2. Geometry quality checklist
- [ ] Within budget for its role (Roblox hard limit: 20k triangles per mesh; most props should be far below. This academy's chests use 1.0–1.9k tris for the whole assembly).
- [ ] No n-gons (Roblox spec), no non-manifold edges (watertight), no zero-area faces, no loose vertices.
- [ ] Normals point outward; smoothing is intentional (flat for faceted styles; smooth plus weighted normals for bevelled hard-surface).
- [ ] Animated (deforming) assets have edge loops at bend points ([BL-05](BL-05-Mesh-Structure-and-Topology.md)).
- [ ] Modifiers are applied, or applied on export, on purpose. The QC evaluates the mesh **with modifiers applied**.
- [ ] No hidden internal faces wasting triangles; intersections only where they are invisible and harmless.

## 3. Presentation quality checklist
- [ ] Orthographic front/side/top plus a perspective 3/4, all at the same scale. The hero shot is extra, never a replacement.
- [ ] Lighting reveals form: a key light from an upper side, fill, and rim to separate the silhouette from the background.
- [ ] Background is neutral and does not share the asset's main colour.
- [ ] Assets with a non-base pivot are lifted for inspection, so the ground does not hide them (a real defect found in [BL-EX-02/05 v1](Exercises/BL-EX-02-Collectible-Gem-and-Coin.md)).
- [ ] The render does not hide defects that would show in game. Check the wire view and a flat-lit view.

## 4. Roblox integration checklist
- [ ] Scale verified in studs against a 5-stud classic avatar (or 6–6.5 for humanoid-proportion avatars).
- [ ] Pivot at a meaningful point: bottom-centre for props; centre for spinning pickups; the **grip** for tools.
- [ ] Object scale = 1 and rotation = 0 (applied).
- [ ] One material per mesh, a single UV set, UVs within 0–1 if textured.
- [ ] Collision fidelity chosen for gameplay ([BL-17](BL-17-Collision-Fidelity.md)).
- [ ] Repeated props reuse one asset id ([LU-26](../07-Roblox-Studio-and-Luau/LU-26-Asset-Import-and-Organization.md)).
- [ ] **Seen in Studio** after import: scale, orientation, colour/material, collision. If you could not check this, say so.

## Scoring (for benchmarks)
Each category: **Pass / Pass with notes / Fail**, with one sentence of evidence each. The overall result is the *lowest* category. Do not average; a gorgeous asset with a broken pivot is still a Fail for integration.

## Sources
Accessed 2026-10-24. Roblox pages from the creator-docs repository (commit 4e795e6); Blender pages from the 5.2 LTS manual (the URLs use `latest`, which served 5.2 on that date).
- [Mesh specifications](https://create.roblox.com/docs/art/modeling/specifications)
