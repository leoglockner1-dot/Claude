---
title: "BL-12 — Asset organization and naming"
tags: [blender, organization, naming, pipeline]
note_type: "procedure"
evidence: "Roblox docs (name suffixes) + academy conventions"
---

# BL-12 — Asset organization and naming

## Conventions (academy)
- File: `Category_Name.blend` (e.g. `Prop_Chest.blend`), with variants inside as collections: `Prop_Chest_Toy`, `Prop_Chest_Premium`.
- Objects: `Name_Part` (e.g. `Toy_Body`, `Toy_Lid`, `Toy_GoldTrim`). The names carry into Studio as MeshPart names.
- Materials: by role (`Wood`, `Gold`, `Stone`), shared across assets for consistent colour.
- Helper objects prefixed `_` (e.g. `_Ground`, `_Wire_*`) are excluded from export.
- One collection per exportable asset; export with *Limit to Selected*.

## Roblox naming that changes import behaviour (parts/meshes docs)
| Suffix | Becomes |
|---|---|
| `_Att` | `Attachment` (handy for VFX sockets, grip points, sound sources) |
| `_OuterCage` | `WrapTarget` |
| `_InnerCage` + `_OuterCage` | `WrapLayer` |
Use `_Att` empties or tiny meshes for attachment points such as `Chest_Lid_Att` (where the open VFX spawns) or `Pickaxe_Tip_Att` (spark origin).

## Folder layout next to the .blend
```
Prop_Chest/
  Prop_Chest.blend
  refs/            reference board + sources.txt (URLs, licences)
  textures/        *.png (if any)
  export/          Prop_Chest_Toy.fbx / .glb
  renders/         inspection set + QC JSON
```

## Acceptance criteria
Names match between Blender, the export file and Studio; helper objects excluded; reference sources recorded.
