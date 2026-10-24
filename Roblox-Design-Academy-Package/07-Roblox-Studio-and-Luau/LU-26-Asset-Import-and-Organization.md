---
title: "LU-26 — Asset import and organization in Studio"
tags: [studio, assets, import, organization, performance]
note_type: "procedure"
evidence: "official docs; not executed"
---

# LU-26 — Asset import and organization in Studio

## Purpose
Bring meshes, images and audio into Studio so they keep scale and orientation, reuse asset ids (for instancing), and stay findable.

## Facts (studio/importer, parts/meshes, art/blender, performance docs)
- The **3D Importer** previews meshes before import, flags issues and rejects meshes with errors. Name suffixes are converted automatically: `_Att` → `Attachment`, `_OuterCage` → `WrapTarget`, `_InnerCage` + `_OuterCage` → `WrapLayer`.
- Blender→Studio importer settings from Roblox's Blender guide: enable *Insert Using Scene Position* if you kept positions; **World Forward = Front**, **World Up = Top**; **Scale Unit = Stud**; *Import Only as a Model* to group several objects.
- The **Asset Manager** bulk-imports images, audio and meshes, but not rigged/skinned/animated meshes, accessories, or characters with facial animation.
- Instancing: identical meshes with the same `MeshContent` and the same texture (or SurfaceAppearance) are drawn in one draw call. Importing a whole scene at once often gives each copy a different asset id. **Import assets individually, then duplicate in Studio.**

## Procedure
1. Export from Blender with the documented settings ([BL-15](../06-Blender-and-3D-Assets/BL-15-Export-Settings.md)).
2. Import one asset at a time; check the preview for scale against a reference (a 5-stud-tall character or a 4×4 stud part) and for orientation.
3. Set collision fidelity per role ([BL-17](../06-Blender-and-3D-Assets/BL-17-Collision-Fidelity.md)) and `RenderFidelity` (Automatic unless there is a reason).
4. Put the master copy in `ServerStorage/Assets/<Category>` (or `ReplicatedStorage` if clients clone it). Place copies in Workspace by duplicating, not re-importing.
5. Name consistently: `Category_Name_Variant` (e.g. `Prop_Chest_Toy`), matching the Blender object names.
6. Packages for assets reused across places (update once, propagate).

## Common mistakes
- Re-importing the same rock 30 times (30 asset ids, no instancing).
- Ignoring importer warnings.
- Mixing scale workflows (FBX Unit Scale vs 0.01 scene scale) between artists. Pick one ([BL-00](../06-Blender-and-3D-Assets/BL-00-Blender-to-Roblox-Pipeline.md)).

## Test cases
- Run the docs' snippet that prints `MeshPart` names with `MeshId`. Repeated ids mean good reuse; same-name/different-id lines mean likely duplicates.
- A character stands next to the asset: the size matches the design brief.

## Acceptance criteria
Every repeated prop uses one asset id; importer warnings resolved or documented; naming matches the source files.

## References
- https://create.roblox.com/docs/studio/importer · https://create.roblox.com/docs/parts/meshes · https://create.roblox.com/docs/art/blender · https://create.roblox.com/docs/performance-optimization/improve#rendering
