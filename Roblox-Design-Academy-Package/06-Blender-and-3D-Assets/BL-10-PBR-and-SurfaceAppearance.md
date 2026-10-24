---
title: "BL-10 — PBR textures and SurfaceAppearance"
tags: [blender, pbr, textures, roblox]
note_type: "procedure"
evidence: "Roblox docs (surface-appearance, assign-textures, texture-specifications)"
---

# BL-10 — PBR textures and SurfaceAppearance

## Roblox facts
- `SurfaceAppearance` (a child of a MeshPart) applies PBR maps: **ColorMap** (albedo, may include alpha), **NormalMap** (OpenGL tangent space), **RoughnessMap**, **MetalnessMap**, plus an emissive mask with `EmissiveStrength`/`EmissiveTint`.
- Albedo is RGB 24-bit; roughness, metalness and emissive mask are 8-bit single-channel greyscale.
- **AlphaMode:** `Overlay` (default; transparent areas reveal `MeshPart.Color`), `Transparency` (see-through), `TintMask` (blends a tinted ColorMap over the untinted one), `Opaque` (ignore alpha).
- PBR maps override `MeshPart.TextureID`. If both a SurfaceAppearance and a MaterialVariant are set, the SurfaceAppearance maps win.
- To import textures with the mesh, connect image nodes in Blender to Principled BSDF: Color → Base Color; metallic → Metallic; roughness → Roughness; normal → *Normal Map* node → Normal. Then export the FBX with Path Mode Copy + Embed Textures.

## Procedure
1. UV unwrap ([BL-09](BL-09-UV-Mapping-and-Texture-Budgets.md)).
2. Author or bake maps at the budgeted resolution.
3. Albedo should contain colour only, with no baked lighting (or very subtle AO for stylized work, applied consistently across the game).
4. Wire the maps in Blender as above; export; import; verify in Studio under daylight and indoor lighting.
5. Use `Overlay` + `MeshPart.Color` for player-customizable tints. `TintMask` gives tintable regions.

## Stylized vs PBR
Many successful Roblox styles use flat colours or simple gradients with no PBR at all. PBR helps with realistic materials (metal, wet stone) and costs texture memory. Choose by art direction ([Art Direction Styles](../11-Visual-Identity/Art-Direction-Styles.md)), not by default.

## Not verified here
None of the academy's exercise assets use PBR maps. This note is documentation-based; a PBR exercise in Studio is listed in [Remaining gaps](../00-Start-Here/Research-Tracker.md).
