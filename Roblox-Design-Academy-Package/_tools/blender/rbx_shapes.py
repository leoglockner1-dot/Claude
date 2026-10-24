"""Small, readable geometry builders used by the academy exercises (Blender 5.2, bpy + bmesh).

Every builder returns a mesh object with modifiers applied, origin at world (0,0,0) unless stated,
and one material. Shapes are intentionally simple: the exercises are about proportion, silhouette,
bevel scale and material contrast, not about clever procedural tricks.
"""
import math
import random

import bpy  # must come first: with the pip 'bpy' module, bmesh only exists after bpy is imported
import bmesh
from mathutils import Euler, Matrix, Vector, noise


def _new_obj(name, bm, mat=None):
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(name, me)
    bpy.context.scene.collection.objects.link(ob)
    if mat:
        me.materials.append(mat)
    return ob


def apply_modifiers(ob):
    bpy.context.view_layer.objects.active = ob
    for m in list(ob.modifiers):
        bpy.ops.object.modifier_apply(modifier=m.name)
    cleanup(ob)
    return ob


def cleanup(ob, merge=1e-5):
    """Merge coincident verts, dissolve zero-area faces, fix winding. Run after modifiers/joins."""
    bm = bmesh.new()
    bm.from_mesh(ob.data)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=merge)
    bmesh.ops.dissolve_degenerate(bm, dist=merge, edges=bm.edges)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(ob.data)
    bm.free()
    return ob


def bevel(ob, width, segments=2, angle_deg=40, harden=True):
    """Bevel by angle, then Weighted Normal so large flat faces shade flat and bevels catch light."""
    m = ob.modifiers.new('Bevel', 'BEVEL')
    m.width = width
    m.segments = segments
    m.limit_method = 'ANGLE'
    m.angle_limit = math.radians(angle_deg)
    m.harden_normals = harden
    if harden:
        for f in ob.data.polygons:
            f.use_smooth = True
        wn = ob.modifiers.new('WeightedNormal', 'WEIGHTED_NORMAL')
        wn.keep_sharp = True
    return ob


def box(name, size, center, mat=None, taper_top=1.0):
    """Axis-aligned box; taper_top < 1 shrinks the top face (x and y) for wedge/cartoon shapes."""
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        if v.co.z > 0 and taper_top != 1.0:
            v.co.x *= taper_top
            v.co.y *= taper_top
        v.co = Vector((v.co.x * size[0], v.co.y * size[1], v.co.z * size[2])) + Vector(center)
    return _new_obj(name, bm, mat)


def half_cylinder(name, length, radius, center, mat=None, segments=12, squash=1.0):
    """Barrel-lid shape: half cylinder along X, flat side down, closed caps."""
    bm = bmesh.new()
    ring = []
    for i in range(segments + 1):
        a = math.pi * i / segments
        ring.append((math.cos(a) * radius, math.sin(a) * radius * squash))
    left = [bm.verts.new((-length / 2, y, z)) for y, z in ring]
    right = [bm.verts.new((length / 2, y, z)) for y, z in ring]
    for i in range(segments):
        bm.faces.new((left[i], right[i], right[i + 1], left[i + 1]))
    # Caps as triangle fans from the middle of the flat edge: a single semicircle face would be an
    # n-gon, which Roblox's specification asks to avoid (and which can shade unpredictably).
    mids = []
    for ring_verts, x in ((left, -length / 2), (right, length / 2)):
        mid = bm.verts.new((x, 0, 0))
        mids.append(mid)
        for i in range(segments):
            bm.faces.new((mid, ring_verts[i + 1], ring_verts[i]))
    # The bottom must share the fan's centre vertices, otherwise their edges form T-junctions
    # (non-manifold, not watertight). Two quads instead of one.
    bm.faces.new((left[0], mids[0], mids[1], right[0]))
    bm.faces.new((mids[0], left[-1], right[-1], mids[1]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector(center))
    return _new_obj(name, bm, mat)


def cylinder(name, radius, depth, center, mat=None, segments=16, axis='Z', tilt=(0, 0, 0)):
    """`tilt` (radians, XYZ) is applied around the cylinder's own centre before it is moved into place.
    Rotating the object afterwards would pivot around the world origin, because builders put the
    object origin at (0,0,0)."""
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=True, segments=segments, radius1=radius, radius2=radius, depth=depth)
    if axis == 'Y':
        bmesh.ops.rotate(bm, verts=bm.verts, cent=(0, 0, 0), matrix=Matrix.Rotation(math.pi / 2, 3, 'X'))
    elif axis == 'X':
        bmesh.ops.rotate(bm, verts=bm.verts, cent=(0, 0, 0), matrix=Matrix.Rotation(math.pi / 2, 3, 'Y'))
    if any(tilt):
        bmesh.ops.rotate(bm, verts=bm.verts, cent=(0, 0, 0), matrix=Euler(tilt).to_matrix())
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector(center))
    return _new_obj(name, bm, mat)


def rock(name, radius=1.0, seed=1, detail=2, flatten=0.7, chunk=0.35, mat=None):
    """Stylised rock: subdivided icosphere -> low-frequency noise displacement -> planar cuts.
    `chunk` controls how faceted the result is (planar dissolve angle). Origin at bottom-centre."""
    rnd = random.Random(seed)
    bm = bmesh.new()
    bmesh.ops.create_icosphere(bm, subdivisions=detail + 1, radius=radius)
    off = Vector((rnd.uniform(-50, 50), rnd.uniform(-50, 50), rnd.uniform(-50, 50)))
    stretch = Vector((rnd.uniform(0.9, 1.4), rnd.uniform(0.8, 1.2), flatten))
    for v in bm.verts:
        n = noise.noise(v.co * 0.9 + off)                     # broad shape
        n2 = noise.noise(v.co * 2.3 + off * 1.7) * 0.35        # secondary forms
        v.co = v.co * (1 + 0.28 * n + 0.12 * n2)
        v.co = Vector((v.co.x * stretch.x, v.co.y * stretch.y, v.co.z * stretch.z))
    bmesh.ops.dissolve_limit(bm, angle_limit=chunk, verts=bm.verts, edges=bm.edges)
    bmesh.ops.triangulate(bm, faces=[f for f in bm.faces if len(f.verts) > 4])
    zmin = min(v.co.z for v in bm.verts)
    # sink 12% into the ground so it reads as embedded, then put the origin at the new base
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector((0, 0, -zmin - radius * flatten * 0.12)))
    bisect = bmesh.ops.bisect_plane(bm, geom=bm.verts[:] + bm.edges[:] + bm.faces[:], plane_co=(0, 0, 0), plane_no=(0, 0, 1), clear_inner=True)
    edges = [e for e in bisect['geom_cut'] if isinstance(e, bmesh.types.BMEdge)]
    if edges:
        bmesh.ops.holes_fill(bm, edges=edges)
        bmesh.ops.triangulate(bm, faces=[f for f in bm.faces if len(f.verts) > 4])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return _new_obj(name, bm, mat)


def crystal(name, radius, height, center, tilt=(0, 0), sides=6, mat=None, point=0.35):
    """Hexagonal prism with a pointed tip; `tilt` in degrees around X and Y. Base at center."""
    bm = bmesh.new()
    base = [bm.verts.new((math.cos(2 * math.pi * i / sides) * radius, math.sin(2 * math.pi * i / sides) * radius, 0)) for i in range(sides)]
    top = [bm.verts.new((v.co.x * 0.92, v.co.y * 0.92, height * (1 - point))) for v in base]
    tip = bm.verts.new((0, 0, height))
    for i in range(sides):
        j = (i + 1) % sides
        bm.faces.new((base[i], base[j], top[j], top[i]))
        bm.faces.new((top[i], top[j], tip))
    centre = bm.verts.new((0, 0, 0))          # fan the base: a single hexagon face would be an n-gon
    for i in range(sides):
        bm.faces.new((base[(i + 1) % sides], base[i], centre))
    rot = Euler((math.radians(tilt[0]), math.radians(tilt[1]), 0)).to_matrix()
    bmesh.ops.rotate(bm, verts=bm.verts, cent=(0, 0, 0), matrix=rot)
    bmesh.ops.translate(bm, verts=bm.verts, vec=Vector(center))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return _new_obj(name, bm, mat)


def join(objs, name):
    bpy.ops.object.select_all(action='DESELECT')
    for o in objs:
        o.select_set(True)
    bpy.context.view_layer.objects.active = objs[0]
    bpy.ops.object.join()
    objs[0].name = name
    objs[0].data.name = name
    return objs[0]
