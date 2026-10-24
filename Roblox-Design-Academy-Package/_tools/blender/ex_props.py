"""Exercises BL-EX-01 rocks, BL-EX-02 collectible gem + coin, BL-EX-03 crystal cluster,
BL-EX-05 pickaxe tool, BL-EX-06 stylised tree. One script so the props share light and scale.

Acceptance criteria (written before the first build; see each note for the full list):
  rocks    - three distinct silhouettes (boulder / slab / cluster), visibly faceted planes, flat base
             that sits on the ground, <= 600 tris each, one material each.
  gem/coin - readable at 64 px; pivot at the CENTRE (they spin/bob in place); gem <= 200 tris.
  crystal  - spiky radial silhouette that cannot be mistaken for a rock; <= 600 tris.
  pickaxe  - side silhouette reads as a pickaxe; origin at the grip (where the hand holds it);
             about 4 studs long; head clearly contrasts with the handle.
  tree     - reads as a tree at 64 px; trunk + canopy as separate meshes (one material each);
             <= 1500 tris total; pivot at the trunk base.
Run:  python3 ex_props.py <out_dir> <version>
"""
import math
import os
import tempfile
import random
import sys

import bpy  # must come first: with the pip 'bpy' module, bmesh only exists after bpy is imported
import bmesh
from mathutils import Vector, noise

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rbx_exercise as X
import rbx_scene as S
import rbx_shapes as G

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(tempfile.gettempdir(), 'rbx_props')
V = sys.argv[2] if len(sys.argv) > 2 else 'v1'


def flat(ob):
    for f in ob.data.polygons:
        f.use_smooth = False
    return ob


def rocks():
    stone = S.material('Stone', (0.42, 0.44, 0.48), roughness=0.85)
    stone2 = S.material('StoneWarm', (0.50, 0.45, 0.40), roughness=0.85)
    if V == 'v1':
        boulder = flat(G.rock('Rock_Boulder', 1.4, seed=3, detail=2, flatten=0.8, chunk=0.35, mat=stone))
        slab = flat(G.rock('Rock_Slab', 1.6, seed=11, detail=2, flatten=0.35, chunk=0.35, mat=stone2))
        parts = [G.rock(f'Rock_Pebble{i}', r, seed=20 + i, detail=1, flatten=0.7, chunk=0.4, mat=stone) for i, r in enumerate((0.7, 0.5, 0.4))]
    else:
        # v2: v1 boulder silhouette was an even egg/oval made of many small facets. Fewer subdivisions
        # + a larger dissolve angle give fewer, bigger planes and a more angular outline.
        boulder = flat(G.rock('Rock_Boulder', 1.4, seed=3, detail=1, flatten=0.8, chunk=0.6, mat=stone))
        slab = flat(G.rock('Rock_Slab', 1.6, seed=11, detail=1, flatten=0.35, chunk=0.6, mat=stone2))
        parts = [G.rock(f'Rock_Pebble{i}', r, seed=20 + i, detail=1, flatten=0.7, chunk=0.7, mat=stone) for i, r in enumerate((0.7, 0.5, 0.4))]
    offsets = ((0, 0, 0), (0.85, 0.35, 0), (-0.55, 0.6, 0))
    if V != 'v1':
        # v2: in v1 the third pebble was hidden behind the first and the two visible ones sat in a line.
        # Triangle layout with clearly different sizes (big / medium / small) reads as a deliberate group.
        offsets = ((0, 0, 0), (1.0, -0.45, 0), (0.25, -0.95, 0))
    for p, off in zip(parts, offsets):
        p.location = off
        flat(p)
    bpy.ops.object.select_all(action='DESELECT')
    for p in parts:
        p.select_set(True)
    bpy.context.view_layer.objects.active = parts[0]
    bpy.ops.object.transform_apply(location=True)
    cluster = G.join(parts, 'Rock_Cluster')
    G.cleanup(cluster)
    return {'rock_boulder': [boulder], 'rock_slab': [slab], 'rock_cluster': [cluster]}


def gem():
    """Low-poly brilliant: crown ring + table + pavilion point. Centre pivot."""
    col = (0.15, 0.55, 1.0)
    m = S.material('Gem', col, roughness=0.15, metallic=0.0, emission=col, emission_strength=0.4)   # v1 passed review: unchanged
    bm = bmesh.new()
    n = 8
    girdle = [bm.verts.new((math.cos(2 * math.pi * i / n) * 0.5, math.sin(2 * math.pi * i / n) * 0.5, 0)) for i in range(n)]
    table = [bm.verts.new((math.cos(2 * math.pi * (i + 0.5) / n) * 0.28, math.sin(2 * math.pi * (i + 0.5) / n) * 0.28, 0.22)) for i in range(n)]
    tip = bm.verts.new((0, 0, -0.55))
    for i in range(n):
        j = (i + 1) % n
        bm.faces.new((girdle[i], girdle[j], table[i]))
        bm.faces.new((girdle[j], table[j], table[i]))
        bm.faces.new((girdle[j], girdle[i], tip))
    c = bm.verts.new((0, 0, 0.22))
    for i in range(n):
        bm.faces.new((table[i], table[(i + 1) % n], c))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    ob = flat(G._new_obj('Gem', bm, m))
    ob.location.z = 1.5
    return {'gem': [ob]}


def coin():
    gold = S.material('CoinGold', (1.0, 0.72, 0.15), roughness=0.3, metallic=0.85)
    face = G.cylinder('Coin', 0.6, 0.14, (0, 0, 1.5), gold, segments=24, axis='Y')
    G.bevel(face, 0.04, 2, angle_deg=30, harden=True)
    G.apply_modifiers(face)
    if V != 'v1':
        # v2: v1 coin face was blank - at 64/32 px it read as a plain yellow disc. A raised star emboss
        # gives it an identity and an extra highlight edge. (Same mesh, so still one material.)
        bm = bmesh.new()
        pts = []
        for i in range(10):
            r = 0.38 if i % 2 == 0 else 0.17
            a = math.pi / 2 + i * math.pi / 5
            pts.append((math.cos(a) * r, math.sin(a) * r))
        front = [bm.verts.new((x, -0.07, z + 1.5)) for x, z in pts]
        back = [bm.verts.new((x, -0.12, z + 1.5)) for x, z in pts]
        cf = bm.verts.new((0, -0.12, 1.5))
        cb = bm.verts.new((0, -0.07, 1.5))
        for i in range(10):
            j = (i + 1) % 10
            bm.faces.new((front[i], front[j], back[j], back[i]))
            bm.faces.new((cf, back[i], back[j]))
            bm.faces.new((cb, front[j], front[i]))
        bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
        star = G._new_obj('CoinStar', bm, gold)
        face = G.join([face, star], 'Coin')
        G.cleanup(face)
    return {'coin': [face]}


def crystals():
    m = S.material('Crystal', (0.45, 0.85, 1.0), roughness=0.2, emission=(0.3, 0.75, 1.0), emission_strength=0.6)
    base_m = S.material('CrystalBase', (0.30, 0.30, 0.36), roughness=0.9)
    base = flat(G.rock('Crystal_Base', 0.9, seed=5, detail=1, flatten=0.4, chunk=0.6, mat=base_m))
    spec = [(0.28, 2.2, (0, 0, 0.2), (0, 0)), (0.2, 1.5, (0.35, 0.15, 0.15), (0, 28)), (0.18, 1.2, (-0.35, 0.1, 0.15), (5, -30)),
            (0.15, 0.9, (0.1, -0.35, 0.12), (-30, 8)), (0.14, 0.8, (-0.05, 0.4, 0.12), (30, -5))]
    if V != 'v1':
        # v2: v1 side shards were similar in size and the hexagonal prisms read a little like pencils.
        # Stronger size hierarchy (one hero, two mids, small accents) and a wider fan of tilts.
        spec = [(0.34, 2.6, (0, 0, 0.15), (0, -6)), (0.22, 1.6, (0.38, 0.12, 0.12), (6, 34)), (0.2, 1.3, (-0.4, 0.05, 0.12), (4, -38)),
                (0.13, 0.75, (0.12, -0.38, 0.1), (-38, 12)), (0.12, 0.6, (-0.12, 0.42, 0.1), (36, -10)), (0.1, 0.5, (0.45, -0.25, 0.08), (-20, 50))]
    shards = [flat(G.crystal(f'Crystal_{i}', r, h, c, tilt=t, mat=m)) for i, (r, h, c, t) in enumerate(spec)]
    # (v1 QC FAIL: each shard's hexagonal base was a 6-sided n-gon; rbx_shapes.crystal now fans it.)
    cluster = G.join(shards, 'Crystal_Shards')
    G.cleanup(cluster)
    return {'crystal_cluster': [base, cluster]}


def pickaxe():
    wood = S.material('Handle', (0.45, 0.28, 0.14), roughness=0.7)
    steel = S.material('PickSteel', (0.62, 0.66, 0.72), roughness=0.35, metallic=0.9)
    handle_len = 3.6 if V in ('v1', 'v2') else 3.75     # v3: handle end shows above the head
    handle = G.cylinder('Pick_Handle', 0.11, handle_len, (0, 0, handle_len / 2), wood, segments=8)
    G.bevel(handle, 0.03, 1, harden=False)
    G.apply_modifiers(handle)
    # Head: a curved bar built from segments along an arc, tapering to points at both ends.
    # v1/v2 profile grew tall in the middle (crescent cross-section), so the 3/4 view read as an umbrella
    # canopy over a shaft. v3: near-constant bar thickness, sharper points, less sag, and the handle
    # pokes through the top of the head (the "eye"), which is what makes a tool read as a tool.
    bm = bmesh.new()
    segs, span = 10, 2.6
    sag = {'v1': 0.45, 'v2': 0.6}.get(V, 0.35)
    rings = []
    for i in range(segs + 1):
        t = i / segs
        x = (t - 0.5) * span
        z = 3.35 - sag * (2 * (t - 0.5)) ** 2
        if V in ('v1', 'v2'):
            w = 0.2 * (1 - abs(2 * t - 1) ** 1.5) + 0.02
            hgt = (0.28 if V == 'v1' else 0.34) * (1 - abs(2 * t - 1) ** 2) + 0.03
        else:
            edge = abs(2 * t - 1)
            w = 0.13 * (1 - edge ** 4) + 0.01             # stays thick until close to the tips
            hgt = 0.15 * (1 - edge ** 4) + 0.01
        rings.append([bm.verts.new((x, sy * w, z + sz * hgt)) for sy, sz in ((-1, -1), (1, -1), (1, 1), (-1, 1))])
    for a, b in zip(rings, rings[1:]):
        for k in range(4):
            bm.faces.new((a[k], a[(k + 1) % 4], b[(k + 1) % 4], b[k]))
    bm.faces.new(rings[0][::-1])
    bm.faces.new(rings[-1])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    head = G._new_obj('Pick_Head', bm, steel)
    collar = G.box('Pick_Collar', (0.34, 0.34, 0.5) if V in ('v1', 'v2') else (0.36, 0.36, 0.42), (0, 0, 3.3), steel)
    G.bevel(collar, 0.05, 2)
    G.apply_modifiers(collar)
    head = G.join([head, collar], 'Pick_Head')
    G.cleanup(head)
    for o in (handle, head):
        flat(o)
    if V != 'v1':
        grip = S.material('Grip', (0.75, 0.15, 0.12), roughness=0.8)
        wrap = G.cylinder('Pick_Grip', 0.135, 0.9, (0, 0, 0.6), grip, segments=8)
        flat(wrap)
        return {'pickaxe': [handle, head, wrap]}
    return {'pickaxe': [handle, head]}


def tree():
    bark = S.material('Bark', (0.38, 0.24, 0.14), roughness=0.9)
    leaf = S.material('Leaves', (0.30, 0.62, 0.25), roughness=0.8)
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=True, segments=7, radius1=0.45, radius2=0.22, depth=3.2)
    bmesh.ops.translate(bm, verts=bm.verts, vec=(0, 0, 1.6))
    trunk = flat(G._new_obj('Tree_Trunk', bm, bark))
    blobs = []
    spec = [((0, 0, 3.6), 1.5), ((0.9, 0.3, 3.1), 1.0), ((-0.8, -0.2, 3.2), 1.1), ((0.1, -0.6, 4.4), 0.9)]
    # v1 passed review (reads as a tree at 64 px, 348 tris): unchanged in v2
    for i, (c, r) in enumerate(spec):
        b = bmesh.new()
        bmesh.ops.create_icosphere(b, subdivisions=2, radius=r)
        for v in b.verts:
            v.co *= 1 + 0.12 * noise.noise(v.co * 1.7 + Vector((i * 3.1, 0, 0)))
            v.co.z *= 0.8
        bmesh.ops.translate(b, verts=b.verts, vec=c)
        blobs.append(flat(G._new_obj(f'Tree_Leaf{i}', b, leaf)))
    canopy = G.join(blobs, 'Tree_Canopy')
    G.cleanup(canopy)
    flat(canopy)
    return {'tree': [trunk, canopy]}


def main():
    S.reset_scene('BLENDER_EEVEE', (900, 900))
    S.three_point_lights((0, 0, 1), 4)
    S.ground(80)
    builders = [rocks, gem, coin, crystals, pickaxe, tree]
    only = os.environ.get('ONLY')            # e.g. ONLY=gem to rebuild one asset
    if only:
        builders = [b for b in builders if b.__name__ in only.split(',')]
    os.makedirs(OUT, exist_ok=True)
    summary, exports = {}, []
    for b in builders:
        for name, objs in b().items():
            pivot = 'center' if name in ('gem', 'coin') else 'bottom-center'
            pivot_obj = None
            if name == 'pickaxe':
                pivot_obj = objs[0]
            X.center_on_origin(objs, pivot_obj, pivot)
            if name == 'pickaxe':
                # Tool grip: put the origin a quarter of the way up the handle, where the hand holds it.
                for o in objs:
                    o.location.z -= 3.6 * 0.18
                bpy.ops.object.select_all(action='DESELECT')
                for o in objs:
                    o.select_set(True)
                bpy.ops.object.transform_apply(location=True)
            rep, ex, _ = X.inspect_asset(objs, OUT, f'{name}_{V}', qc_pivot=pivot if len(objs) == 1 else None)
            exports += ex
            summary[name] = {'summary': rep['_summary'], 'issues': X.fails(rep)}
            for o in objs:      # park inspected assets out of the way of the next one
                o.hide_render = True
                o.hide_viewport = True
    import json
    with open(os.path.join(OUT, f'props_summary_{V}.json'), 'w') as f:
        json.dump(summary, f, indent=1)
    X.round_trips(exports, os.path.join(OUT, f'props_roundtrip_{V}.json'))
    for k, v in summary.items():
        print(k, v['summary'], v['issues'])


if __name__ == '__main__':
    main()
