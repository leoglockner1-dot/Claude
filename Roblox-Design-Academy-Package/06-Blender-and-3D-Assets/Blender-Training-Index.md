---
title: "Blender and 3D Assets — Training Index"
tags: [blender, index, 3d]
note_type: "index"
---

# Blender and 3D Assets — Training Index

A curriculum for **production-ready** 3D assets for Roblox, plus a tested Python toolkit. Everything marked *executed* was built and inspected in this session with **Blender 5.2.3 (`bpy` from PyPI, headless Linux)**. The renders are real outputs, defects included.

**Rule zero:** a beautiful render is not proof of a production-ready asset. Judge with the [Modeling Quality Framework](BL-20-Modeling-Quality-Framework.md): visual, geometry, presentation and Roblox integration, separately.

## Start here
1. [BL-00 — Blender-to-Roblox pipeline: facts and defaults](BL-00-Blender-to-Roblox-Pipeline.md)
2. [BL-20 — Modeling Quality Framework](BL-20-Modeling-Quality-Framework.md)
3. [BL-19 — Blender Python automation (toolkit)](BL-19-Blender-Python-Automation.md)

## Procedures
| # | Topic |
|---|---|
| BL-01 | [Reference gathering](BL-01-Reference-Gathering.md) |
| BL-02 | [Shape language, silhouette, proportion](BL-02-Shape-Language-Silhouette-Proportion.md) |
| BL-03 | [Low-poly and stylized modeling](BL-03-Low-Poly-Stylized-Modeling.md) |
| BL-04 | [Hard-surface modeling](BL-04-Hard-Surface-Modeling.md) |
| BL-05 | [Mesh structure and topology](BL-05-Mesh-Structure-and-Topology.md) |
| BL-06 | [Shading and normals](BL-06-Shading-and-Normals.md) |
| BL-07 | [Bevels and modifiers](BL-07-Bevels-and-Modifiers.md) |
| BL-08 | [Materials and colour](BL-08-Materials-and-Color.md) |
| BL-09 | [UV mapping and texture budgets](BL-09-UV-Mapping-and-Texture-Budgets.md) |
| BL-10 | [PBR and SurfaceAppearance](BL-10-PBR-and-SurfaceAppearance.md) |
| BL-11 | [Lighting and rendering: inspection vs presentation](BL-11-Lighting-and-Rendering.md) |
| BL-12 | [Asset organization and naming](BL-12-Asset-Organization-and-Naming.md) |
| BL-13 | [Rigging and animation export](BL-13-Rigging-and-Animation-Export.md) |
| BL-14 | [Roblox import, scale and pivots](BL-14-Roblox-Import-Scale-and-Pivots.md) |
| BL-15 | [Export settings](BL-15-Export-Settings.md) |
| BL-16 | [Performance budgets](BL-16-Performance-Budgets.md) |
| BL-17 | [Collision fidelity](BL-17-Collision-Fidelity.md) |
| BL-18 | [Technical troubleshooting](BL-18-Technical-Troubleshooting.md) |
| BL-19 | [Blender Python automation](BL-19-Blender-Python-Automation.md) |
| BL-20 | [Modeling Quality Framework](BL-20-Modeling-Quality-Framework.md) |
| BL-21 | [Procedural variation without sameness](BL-21-Procedural-Variation.md) |

## Practical exercises
| # | Exercise | Status | Iterations | Key lesson |
|---|---|---|---|---|
| BL-EX-01 | [Stylized rocks](Exercises/BL-EX-01-Stylized-Rocks.md) | ✅ executed | 2 | Facet size, not triangle count, makes the style (204 → 56 tris, better read) |
| BL-EX-02 | [Collectible gem and coin](Exercises/BL-EX-02-Collectible-Gem-and-Coin.md) | ✅ executed | 3 | A same-material emboss is invisible at small sizes; a stale-matrix pivot bug |
| BL-EX-03 | [Crystal cluster](Exercises/BL-EX-03-Crystal-Cluster.md) | ✅ executed | 2 | Size hierarchy; n-gon caps |
| BL-EX-04 | [Treasure chest × 3 directions](Exercises/BL-EX-04-Treasure-Chests.md) | ✅ executed | 4 | Judge silhouettes at the gameplay angle; QC regressions from fixes |
| BL-EX-05 | [Pickaxe tool](Exercises/BL-EX-05-Pickaxe-Tool.md) | ✅ executed | 3 | A failed fix tells you the real cause (profile, not thickness) |
| BL-EX-06 | [Stylized tree](Exercises/BL-EX-06-Stylized-Tree.md) | ✅ executed | 1 (passed) | Don't change what passed |
| BL-EX-07 | [Palette: one mesh, one material](Exercises/BL-EX-07-Palette-Single-Material.md) | ✅ executed | 1 | Colours kept (Δ 1.8/255); material response lost |
| BL-EX-08 | [Furniture set](Exercises/BL-EX-08-10-13-Unexecuted-Exercise-Specs.md) | ⏳ spec only | — | — |
| BL-EX-09 | [Modular building kit (5-stud grid)](Exercises/BL-EX-09-Modular-Building-Kit.md) | ✅ executed | 2 | Profiles not joined boxes; validate your validator |
| BL-EX-10 | [Mechanical lever](Exercises/BL-EX-08-10-13-Unexecuted-Exercise-Specs.md) | ⏳ spec only | — | — |
| BL-EX-11 | [Animated pickup export](Exercises/BL-EX-11-Animated-Pickup.md) | ✅ executed | 1 | Blender 5.x layered actions |
| BL-EX-12 | [VFX geometry](Exercises/BL-EX-12-VFX-Geometry.md) | ✅ executed | 2 | QC must know about open cards |
| BL-EX-13 | [Stylized character](Exercises/BL-EX-08-10-13-Unexecuted-Exercise-Specs.md) | ⏳ spec only | — | — |

## What was not verified (applies to all exercises)
- **No asset was imported into Roblox Studio** (not available here). Scale, orientation, colour, collision and shading in Studio remain unverified; the FBX/GLB files are in `Assets/Original/Blender/*/export/` for that test.
- Blender application UI workflows were not exercised. The `bpy` module ran the same operators headless.
