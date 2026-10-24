"""Export helpers that follow Roblox's documented Blender export settings, plus a round-trip check.

Sources (Roblox Creator Docs, commit 4e795e6, read 2026-10-24):
- art/modeling/export-requirements.md: FBX -> Path Mode Copy + Embed Textures, Apply Scalings =
  FBX Unit Scale, Add Leaf Bones off, Bake Animation off unless animated.
- art/blender.md: Limit to Selected, Forward = Z Forward, Up = Y Up; glTF needs no extra scaling.

The round trip re-imports the file into an empty Blender scene and compares dimensions. It proves the
file is readable and keeps its size *in Blender*; it does NOT prove how Studio's Importer scales it.
Verify in Studio (Importer preview, Scale Unit = Stud) before trusting a new pipeline.
"""
import os

import bpy


def _select_only(objs):
    bpy.ops.object.select_all(action='DESELECT')
    for o in objs:
        o.select_set(True)
    bpy.context.view_layer.objects.active = objs[0]


def export_fbx(objs, path, animated=False):
    _select_only(objs)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    bpy.ops.export_scene.fbx(
        filepath=path, use_selection=True, object_types={'MESH', 'ARMATURE', 'EMPTY'},
        apply_scale_options='FBX_SCALE_UNITS', global_scale=1.0, apply_unit_scale=True,
        axis_forward='Z', axis_up='Y', use_mesh_modifiers=True, mesh_smooth_type='FACE',
        add_leaf_bones=False, bake_anim=animated, path_mode='COPY', embed_textures=True)
    return path


def export_gltf(objs, path):
    _select_only(objs)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    bpy.ops.export_scene.gltf(filepath=path, use_selection=True, export_format='GLB',
                              export_yup=True, export_apply=True, export_materials='EXPORT')
    return path


def export_obj(objs, path):
    _select_only(objs)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    bpy.ops.wm.obj_export(filepath=path, export_selected_objects=True, apply_modifiers=True,
                          forward_axis='NEGATIVE_Z', up_axis='Y', export_materials=True)
    return path


def round_trip_dimensions(path):
    """Import `path` into a fresh scene and return the overall size (x, y, z) of imported meshes."""
    bpy.ops.wm.read_factory_settings(use_empty=True)
    ext = os.path.splitext(path)[1].lower()
    if ext == '.fbx':
        bpy.ops.import_scene.fbx(filepath=path)
    elif ext in ('.glb', '.gltf'):
        bpy.ops.import_scene.gltf(filepath=path)
    elif ext == '.obj':
        bpy.ops.wm.obj_import(filepath=path, forward_axis='NEGATIVE_Z', up_axis='Y')
    meshes = [o for o in bpy.context.scene.objects if o.type == 'MESH']
    from mathutils import Vector
    pts = [o.matrix_world @ Vector(c) for o in meshes for c in o.bound_box]
    size = [max(p[i] for p in pts) - min(p[i] for p in pts) for i in range(3)]
    return {'file': os.path.basename(path), 'meshes': len(meshes), 'size_blender_axes': [round(s, 3) for s in size],
            'bytes': os.path.getsize(path)}
