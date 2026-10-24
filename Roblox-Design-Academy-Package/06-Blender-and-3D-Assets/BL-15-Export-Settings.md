---
title: "BL-15 — Export settings (FBX, glTF, OBJ)"
tags: [blender, export, fbx, gltf]
note_type: "procedure"
evidence: "Roblox docs + tested exports (bpy 5.2.3)"
code: "_tools/blender/rbx_export.py"
---

# BL-15 — Export settings (FBX, glTF, OBJ)

## FBX (Roblox export-requirements + Blender guide)
UI: File > Export > FBX → **Limit to Selected** · Path Mode **Copy** + **Embed Textures** · Apply Scalings **FBX Unit Scale** · Forward **Z Forward**, Up **Y Up** · Armature: **Add Leaf Bones off** · **Bake Animation off** unless animated.

Script (tested):
```python
bpy.ops.export_scene.fbx(filepath=path, use_selection=True,
    apply_scale_options='FBX_SCALE_UNITS', global_scale=1.0, apply_unit_scale=True,
    axis_forward='Z', axis_up='Y', use_mesh_modifiers=True, mesh_smooth_type='FACE',
    add_leaf_bones=False, bake_anim=False, path_mode='COPY', embed_textures=True)
```

## glTF / GLB
Roblox notes that glTF does not need the FBX scaling workarounds.
```python
bpy.ops.export_scene.gltf(filepath=path, use_selection=True, export_format='GLB', export_yup=True, export_apply=True)
```

## OBJ
```python
bpy.ops.wm.obj_export(filepath=path, export_selected_objects=True, apply_modifiers=True, forward_axis='NEGATIVE_Z', up_axis='Y')
```
OBJ carries no rig or animation. It is fine for static meshes.

## Verified in this session
- Exports of 3 chests and 7 props (FBX + GLB) all succeeded; file sizes 18–57 KB.
- The round-trip re-import in Blender reproduced the source dimensions exactly ([BL-14](BL-14-Roblox-Import-Scale-and-Pivots.md)).
- Files are in `Assets/Original/Blender/*/export/`, so you can test them in Studio.

## Not verified
Studio import of these files. **Next step for a human or agent with Studio:** import `chest_premium.fbx` and `chest_premium.glb` with Scale Unit = Stud and check they come in about 2.7 studs wide.

## Sources
Accessed 2026-10-24. Roblox pages from the creator-docs repository (commit 4e795e6); Blender pages from the 5.2 LTS manual (the URLs use `latest`, which served 5.2 on that date).
- [Export requirements](https://create.roblox.com/docs/art/modeling/export-requirements)
- [glTF export](https://create.roblox.com/docs/art/modeling/gltf-export)
- [Use Blender with Roblox](https://create.roblox.com/docs/art/blender)
- [bpy 5.2.3 on PyPI](https://pypi.org/project/bpy/) — operator and property names confirmed by introspection in this environment
