"""Shared harness for Blender exercises: inspect -> QC -> export -> round-trip, one asset at a time.

inspect_asset() is the academy's standard evidence set for a 3D asset:
  <stem>_front/side/top.png (orthographic), <stem>_threequarter.png, <stem>_wire.png (wire over clay),
  <stem>_silhouette.png (front) and <stem>_silhouette_gameplay.png (elevated 3/4),
  <stem>_sizes.png (3/4 render at 512/150/64/32 px), QC JSON, FBX + GLB, round-trip JSON.
"""
import json
import os

import bpy

import rbx_export
import rbx_qc
import rbx_scene as S


def center_on_origin(objs, pivot_obj=None, pivot='bottom-center'):
    """Move an assembly so `pivot_obj` (default: first object) has its pivot at the world origin,
    then set every object's origin to the world origin."""
    ref = pivot_obj or objs[0]
    lo, hi = S.bounds([ref])
    target = ((lo.x + hi.x) / 2, (lo.y + hi.y) / 2, lo.z if pivot == 'bottom-center' else (lo.z + hi.z) / 2)
    for o in objs:
        o.location.x -= target[0]
        o.location.y -= target[1]
        o.location.z -= target[2]
    bpy.ops.object.select_all(action='DESELECT')
    for o in objs:
        o.select_set(True)
    bpy.context.view_layer.objects.active = objs[0]
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bpy.context.scene.cursor.location = (0, 0, 0)
    for o in objs:
        bpy.ops.object.select_all(action='DESELECT')
        o.select_set(True)
        bpy.context.view_layer.objects.active = o
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')


def inspect_asset(objs, out_dir, stem, export=True, pivot='bottom-center', qc_pivot=None):
    """Render the evidence set and run QC. Other meshes in the scene are hidden from renders."""
    scene_meshes = [o for o in bpy.context.scene.objects if o.type == 'MESH' and not o.name.startswith('_')]
    for o in scene_meshes:
        o.hide_render = o not in objs
    # Assets whose pivot is not at their base (spinning pickups, tools held at the grip) would be cut by
    # the ground plane in inspection renders (seen in BL-EX-02/05 v1). Lift them for the renders only.
    bpy.context.view_layer.update()
    lo, _ = S.bounds(objs)
    lift = max(0.0, -lo.z + 0.05) if lo.z < -1e-4 else 0.0
    for o in objs:
        o.location.z += lift
    bpy.context.view_layer.update()
    files = S.render_views(objs, out_dir, stem, res=480)
    S.render_silhouette(objs, os.path.join(out_dir, f'{stem}_silhouette.png'))
    S.render_silhouette(objs, os.path.join(out_dir, f'{stem}_silhouette_gameplay.png'), view='gameplay')
    S.render_at_size(os.path.join(out_dir, f'{stem}_threequarter.png'), os.path.join(out_dir, f'{stem}_sizes.png'))
    for o in objs:
        o.location.z -= lift
    bpy.context.view_layer.update()
    rep = rbx_qc.check_objects(objs, pivot=qc_pivot)
    lo, hi = S.bounds(objs)
    rep['_summary']['size_studs'] = [round(v, 3) for v in (hi - lo)]
    rbx_qc.save_report(rep, os.path.join(out_dir, f'{stem}_qc.json'))
    exports = []
    if export:
        exports = [rbx_export.export_fbx(objs, os.path.join(out_dir, 'export', f'{stem}.fbx')),
                   rbx_export.export_gltf(objs, os.path.join(out_dir, 'export', f'{stem}.glb'))]
    for o in scene_meshes:
        o.hide_render = False
    return rep, exports, files


def round_trips(exports, out_json):
    rt = [rbx_export.round_trip_dimensions(p) for p in exports]
    with open(out_json, 'w') as f:
        json.dump(rt, f, indent=1)
    return rt


def fails(rep):
    return [(m, c['check'], c['value']) for m, cs in rep.items() if m != '_summary' for c in cs if c['status'] in ('FAIL', 'WARN')]
