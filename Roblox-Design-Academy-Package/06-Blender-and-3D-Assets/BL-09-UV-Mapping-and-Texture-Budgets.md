---
title: "BL-09 — UV mapping and texture budgets"
tags: [blender, uv, textures, budgets]
note_type: "procedure"
evidence: "Roblox texture specs + Blender manual + Roblox Blender guide"
---

# BL-09 — UV mapping and texture budgets

## When you need UVs
Only when the mesh uses an image texture: a colour map, PBR set, palette texture or trim sheet. Flat-colour meshes without textures don't need UVs.

## Roblox requirements (texture-specifications)
- **One UV set** per mesh; UVs inside **0–1**; overlaps allowed (useful for mirrored or repeated parts).
- Textures up to 4096²; the engine streams lower mips first.
- Sizing guidance: ~**256²** for 5×5-stud objects, **512²** for 10×10, **1024²** for 20×20. For PBR: 256² per 2×2×2-stud volume, stepping up for larger assets (64–128² for tiny 1×1×1 items).
- Normal maps: OpenGL tangent space only.

## Blender tools (manual + Roblox guide)
| Tool | Use |
|---|---|
| Mark Seam + Unwrap | Organic or curved parts; seams hidden in natural breaks |
| Smart UV Project | Fast first pass for hard-surface props |
| Follow Active Quads | Grid-like strips (planks, belts, trims) mapped to trim sheets |
| Cube/Cylinder/Sphere Projection | Simple primitives |
| Pack Islands | Fit within 0–1 with margin (UV > Pack Islands) |

## Texel density
Keep a consistent density across assets of one game (e.g. 256 px per 2 studs) so details don't look sharp on one prop and blurry on its neighbour. The Roblox guidance above is a ready-made density.

## Trim sheets and palettes (memory savers)
- **Trim sheet:** one texture with horizontal strips (wood, metal edge, rivets). Many meshes map their faces onto strips; the Roblox Blender guide and the environmental-art curriculum recommend this for adding visual complexity without extra textures.
- **Palette texture:** a tiny image of colour swatches. Each face's UVs sit inside one swatch, so many colours fit in one material. Ideal for stylized props under the one-material rule ([BL-08](BL-08-Materials-and-Color.md)).

## Acceptance criteria
QC: UV sets ≤ 1 and 0 loops outside 0–1; the texture size follows the budget table; texel density is consistent with the asset set.
