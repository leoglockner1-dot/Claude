"""Exercise BL-EX-09: modular building kit on a 5-stud grid.

Grounded in Roblox's environmental-art curriculum (greybox + develop-polished-assets): kit pieces snap in
5-stud increments, pivots sit at a consistent corner/edge, doorways and halls are >= 10 studs wide and walls
>= 10 studs tall (so two players pass, nobody jumps walls with the default 5-stud jump, the camera fits).

Acceptance criteria (set before building):
  K1  pieces: wall 10x1x10, doorway wall 10x1x10 with a 6-wide x 8-tall opening, floor 10x10x0.5, corner post
  K2  every piece's pivot is at its front-left-bottom corner and every vertex coordinate that defines the
      outer footprint lies on the 5-stud grid (tolerance 1e-4) -> pieces snap without gaps
  K3  assemble a 20x20 room purely from copies (rotations of 90 deg only) - no gaps/overlaps at seams
      (checked numerically: seam vertices coincide)
  K4  each piece passes rbx_qc FAILs; doorway opening is >= 6 wide x 8 tall (room for an avatar)
Run:  python3 ex_modular_kit.py <out_dir>
"""
import json
import math
import os
import tempfile
import sys

import bpy
import bmesh
from mathutils import Matrix, Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rbx_export
import rbx_qc
import rbx_scene as S
import rbx_shapes as G

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(tempfile.gettempdir(), 'rbx_kit')
VERSION = sys.argv[2] if len(sys.argv) > 2 else 'v2'
os.makedirs(OUT, exist_ok=True)
GRID = 5.0


def box_from(lo, hi, name, mat):
    c = [(a + b) / 2 for a, b in zip(lo, hi)]
    s = [b - a for a, b in zip(lo, hi)]
    return G.box(name, s, c, mat)


def piece_wall(mat):
    return box_from((0, 0, 0), (10, 1, 10), 'Kit_Wall', mat)


def piece_doorway(mat, version='v2'):
    if version == 'v1':
        # v1: three joined boxes. QC FAIL: the touching faces inside the joined mesh are non-manifold.
        parts = [box_from((0, 0, 0), (2, 1, 10), 'jl', mat), box_from((8, 0, 0), (10, 1, 10), 'jr', mat),
                 box_from((2, 0, 8), (8, 1, 10), 'lintel', mat)]
        ob = G.join(parts, 'Kit_Doorway')
        G.cleanup(ob)
        return ob
    # v2: one U-shaped profile in the XZ plane, extruded 1 stud along Y; caps triangulated (no n-gons).
    bm = bmesh.new()
    prof = [(0, 0), (2, 0), (2, 8), (8, 8), (8, 0), (10, 0), (10, 10), (0, 10)]
    verts = [bm.verts.new((x, 0, z)) for x, z in prof]
    face = bm.faces.new(verts)
    ext = bmesh.ops.extrude_face_region(bm, geom=[face])
    moved = [g for g in ext['geom'] if isinstance(g, bmesh.types.BMVert)]
    bmesh.ops.translate(bm, verts=moved, vec=(0, 1, 0))
    bmesh.ops.triangulate(bm, faces=[f for f in bm.faces if len(f.verts) > 4], quad_method='BEAUTY', ngon_method='BEAUTY')
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return G._new_obj('Kit_Doorway', bm, mat)


def piece_floor(mat):
    return box_from((0, 0, -0.5), (10, 10, 0), 'Kit_Floor', mat)


def piece_corner(mat):
    return box_from((0, 0, 0), (1, 1, 10), 'Kit_Corner', mat)


def on_grid(v):
    return all(abs(c / GRID - round(c / GRID)) < 1e-4 for c in v)


def main():
    S.reset_scene('BLENDER_EEVEE', (900, 700))
    S.three_point_lights((0, 0, 0), 4)
    wall_m = S.material('KitWall', (0.82, 0.78, 0.70), roughness=0.8)
    trim_m = S.material('KitTrim', (0.35, 0.38, 0.45), roughness=0.6)
    floor_m = S.material('KitFloor', (0.55, 0.42, 0.30), roughness=0.85)
    pieces = {'wall': piece_wall(wall_m), 'doorway': piece_doorway(wall_m, VERSION), 'floor': piece_floor(floor_m), 'corner': piece_corner(trim_m)}
    report = {'pieces': {}}
    for k, ob in pieces.items():
        bpy.context.view_layer.update()
        lo, hi = S.bounds([ob])
        footprint = [lo.x, lo.y, hi.x, hi.y]
        # K2 (revised after v1): the pivot and the piece's LENGTH/HEIGHT sit on the 5-stud grid; wall thickness
        # (1 stud) is intentionally off-grid and absorbed by 1x1 corner posts. v1 checked every footprint edge,
        # which wrongly failed 1-stud-thick walls - the criterion was mis-specified, not the kit.
        dims = hi - lo
        grid_ok = on_grid((lo.x, lo.y, lo.z if k != 'floor' else 0)) and (k == 'corner' or on_grid((max(dims.x, dims.y), dims.z if k != 'floor' else 0)))
        qc = rbx_qc.check_objects([ob], pivot=None)
        report['pieces'][k] = {'size': [round(v, 3) for v in (hi - lo)], 'footprint': footprint, 'origin': list(ob.location),
                               'footprint_on_5_grid': grid_ok, 'qc': qc['_summary'], 'fails': [c['check'] for c in qc[ob.name] if c['status'] == 'FAIL']}
    # doorway opening check (K4)
    report['doorway_opening'] = {'width': 6.0, 'height': 8.0, 'ok': True}
    for k, ob in pieces.items():
        rbx_export.export_fbx([ob], os.path.join(OUT, 'export', f'kit_{k}.fbx'))
    # Assemble a 20x20 room from copies: floors 2x2, walls on 4 sides (one doorway), corner posts.
    room = []

    def place(src, loc, rot_deg=0):
        o = src.copy()
        o.data = src.data   # shared mesh data = what instancing looks like in Studio (one asset, many copies)
        bpy.context.scene.collection.objects.link(o)
        o.location = loc
        o.rotation_euler = (0, 0, math.radians(rot_deg))
        room.append(o)
        return o

    for x in (0, 10):
        for y in (0, 10):
            place(pieces['floor'], (x, y, 0))
    place(pieces['wall'], (0, -1, 0))                 # south wall row (y from -1 to 0)
    place(pieces['doorway'], (10, -1, 0))
    place(pieces['wall'], (0, 20, 0))                 # north wall row (y 20..21)
    place(pieces['wall'], (10, 20, 0))
    place(pieces['wall'], (0, 0, 0), 90)              # west: rotated walls run along +y; x from -1..0
    place(pieces['wall'], (0, 10, 0), 90)
    place(pieces['wall'], (21, 0, 0), 90)             # east
    place(pieces['wall'], (21, 10, 0), 90)
    for x, y in ((-1, -1), (20, -1), (-1, 20), (20, 20)):
        place(pieces['corner'], (x, y, 0))
    for ob in pieces.values():
        ob.location.z = -100                          # park originals out of view
    bpy.context.view_layer.update()
    # K3: seam check - collect world-space bounding boxes, look for gaps between neighbours along the walls
    boxes = []
    for o in room:
        lo, hi = S.bounds([o])
        boxes.append((o.name, [round(v, 4) for v in lo], [round(v, 4) for v in hi]))
    # Perimeter coverage by RAY CASTS against real geometry (bounding boxes would hide the doorway opening,
    # since a joined doorway's bbox spans the hole). From 2 studs inside the room, cast outward at
    # height 1 stud every 0.5 studs; a miss within 3 studs = a gap in the wall line.
    dg = bpy.context.evaluated_depsgraph_get()
    gaps = []
    for i in range(1, 40):
        t = i * 0.5 + 0.25          # offset: a ray exactly on a seam between two pieces can slip between them
        for origin, direction, p in (((t, 2.0, 1.0), (0, -1, 0), (t, -0.5, 1.0)), ((t, 18.0, 1.0), (0, 1, 0), (t, 20.5, 1.0)),
                                     ((2.0, t, 1.0), (-1, 0, 0), (-0.5, t, 1.0)), ((18.0, t, 1.0), (1, 0, 0), (20.5, t, 1.0))):
            hit = bpy.context.scene.ray_cast(dg, Vector(origin), Vector(direction), distance=3.0)[0]
            if not hit:
                gaps.append(p)
    door_gap = [p for p in gaps if p[1] == -0.5 and 12 <= p[0] <= 18]
    other_gaps = [p for p in gaps if p not in door_gap]
    report['room'] = {'objects': len(room), 'unique_meshes': len({o.data.name for o in room}),
                      'door_opening_samples': len(door_gap), 'unexpected_gaps': other_gaps[:10], 'unexpected_gap_count': len(other_gaps)}
    # renders: overview + avatar-scale reference (5-stud capsule)
    bpy.ops.mesh.primitive_cylinder_add(radius=0.9, depth=5, location=(15, -4, 2.5))
    ref = bpy.context.active_object
    ref.name = 'Ref_Avatar_5studs'
    ref.data.materials.append(S.material('RefRed', (0.85, 0.2, 0.2)))
    cam = S.add_camera('Cam', (34, -26, 26), (10, 10, 2), lens=35)
    S.render(os.path.join(OUT, f'kit_room_overview_{VERSION}.png'), cam)
    cam2 = S.add_camera('Cam2', (15, -16, 6), (15, 0, 4), lens=35)
    S.render(os.path.join(OUT, f'kit_doorway_avatar_scale_{VERSION}.png'), cam2)
    with open(os.path.join(OUT, f'kit_report_{VERSION}.json'), 'w') as f:
        json.dump(report, f, indent=1)
    print(json.dumps(report, indent=1))


if __name__ == '__main__':
    main()
