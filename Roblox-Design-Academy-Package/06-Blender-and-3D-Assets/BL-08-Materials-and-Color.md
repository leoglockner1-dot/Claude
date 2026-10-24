---
title: "BL-08 — Materials and colour for Roblox assets"
tags: [blender, materials, color, palette, roblox]
note_type: "procedure"
evidence: "Roblox docs + executed palette exercise (BL-EX-07)"
---

# BL-08 — Materials and colour for Roblox assets

## Constraints (Roblox)
- **One material per mesh** (texture-specifications).
- Options for colour on a MeshPart: `MeshPart.Color` plus a Roblox `Material` (no texture); `TextureID` (one colour texture); `SurfaceAppearance` (PBR maps, alpha modes including TintMask); `MaterialVariant` (custom material with physical properties).
- The Studio Importer reads Blender textures connected to Principled BSDF ([BL-10](BL-10-PBR-and-SurfaceAppearance.md)). **How it treats a Principled Base Color with no texture was not verified in this session.** Check it in the Importer preview.

## Three ways to give a multi-colour prop its colours
| Approach | How | Best for | Evidence here |
|---|---|---|---|
| **Split by material** | Separate mesh per colour role; set `MeshPart.Color`/`Material` in Studio | Hero props needing different surface response (metal shine) | Chests BL-EX-04 (3–4 meshes each) |
| **Palette texture** | One mesh, UVs inside swatches of a tiny palette PNG | Many small props; fewer objects | [BL-EX-07](Exercises/BL-EX-07-Palette-Single-Material.md): mean colour difference 1.8/255; metallic highlight lost |
| **Full texture / PBR** | Unwrap and paint or bake | Realistic or detailed assets | Not executed (docs only) |

## Colour decisions (design)
- **Value first:** make sure the main parts differ in brightness, not just hue (test greyscale). The toy chest's red-brown body vs light gold trim reads in greyscale; the premium chest's dark walnut vs brass is more subtle, and that is part of why it is harder to read at 64 px.
- **Saturation by role:** gameplay-relevant objects (pickups, interactables) get higher saturation or emission than the environment ([World-to-UI Consistency](../11-Visual-Identity/World-to-UI-Consistency.md)).
- **Shared material library:** reuse named materials (`Wood`, `Gold`, `Stone`) across assets so colours match. In code, `rbx_scene.material(name, …)` reuses a material when the name exists.
- **Linear vs sRGB:** Principled Base Color values are linear. Convert to sRGB when writing palette PNGs or matching UI hex colours. Skipping this makes colours drift (handled in `palette_convert`).

## Acceptance criteria
≤ 1 material per mesh (QC); colour roles distinguishable in greyscale; any palette PNG is generated from the same source values as the materials.

## Sources
Accessed 2026-10-24. Roblox pages from the creator-docs repository (commit 4e795e6); Blender pages from the 5.2 LTS manual (the URLs use `latest`, which served 5.2 on that date).
- [Assign textures](https://create.roblox.com/docs/art/modeling/assign-textures)
- [SurfaceAppearance](https://create.roblox.com/docs/art/modeling/surface-appearance)
