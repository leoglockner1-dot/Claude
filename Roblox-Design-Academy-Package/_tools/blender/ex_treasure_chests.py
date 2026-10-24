"""Exercise BL-EX-04: one treasure chest, three art directions (toy / premium / cartoon).

Acceptance criteria (set before building):
  A1  Each chest reads as "treasure chest" from its silhouette alone (front ortho, flat colour).
  A2  The three directions are distinguishable at 64 px.
  A3  Every mesh passes rbx_qc FAILs (<=20k tris, watertight, <=1 material, volume).
  A4  Pivot of each assembly is bottom-centre at (0,0,0); size fits a 5-stud-tall character
      (chest roughly 2-3.5 studs wide).
  A5  FBX + GLB export succeed and re-import with the same dimensions (in Blender).

Run:  python3 ex_treasure_chests.py <out_dir> [version]
"""
import json
import math
import os
import tempfile
import random
import sys

import bpy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rbx_export
import rbx_qc
import rbx_scene as S
import rbx_shapes as G

OUT = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('-') else os.path.join(tempfile.gettempdir(), 'rbx_chests')
VERSION = sys.argv[2] if len(sys.argv) > 2 else 'v1'


def chest_toy(x):
    """Chunky, toy-like: squat, very soft bevels, saturated primaries, few big parts."""
    wood = S.material('Toy_Wood', (0.62, 0.22, 0.10), roughness=0.55)
    gold = S.material('Toy_Gold', (1.0, 0.72, 0.12), roughness=0.35, metallic=0.2)
    w, d, h = 3.0, 2.2, 1.5
    body = G.bevel(G.box('Toy_Body', (w, d, h), (x, 0, h / 2), wood), 0.28, 4, harden=False)
    lid = G.bevel(G.half_cylinder('Toy_Lid', w, d / 2, (x, 0, h), wood, segments=14), 0.12, 3, harden=False)
    bands = [G.bevel(G.box(f'Toy_Band{i}', (0.42, d + 0.16, h + 0.06), (x + sx * 0.85, 0, h / 2 + 0.01), gold), 0.12, 3, harden=False)
             for i, sx in enumerate((-1, 1))]
    lid_bands = [G.bevel(G.half_cylinder(f'Toy_LidBand{i}', 0.42, d / 2 + 0.08, (x + sx * 0.85, 0, h), gold, segments=14), 0.08, 2, harden=False)
                 for i, sx in enumerate((-1, 1))]
    lock = G.bevel(G.box('Toy_Lock', (0.75, 0.3, 0.8), (x, -d / 2 - 0.1, h - 0.05), gold), 0.14, 3, harden=False)
    parts = [body, lid, lock] + bands + lid_bands
    for p in parts:
        G.apply_modifiers(p)
        for f in p.data.polygons:
            f.use_smooth = True
    gold_parts = G.join([lock] + bands + lid_bands, 'Toy_GoldTrim')
    return [body, lid, gold_parts]


def chest_premium(x):
    """Premium, restrained: taller, slim crisp bevels, dark walnut + thin brass edge trim, small lock."""
    wood = S.material('Prem_Walnut', (0.16, 0.085, 0.05), roughness=0.45)
    brass = S.material('Prem_Brass', (0.78, 0.6, 0.32), roughness=0.3, metallic=0.9)
    w, d, h = 2.6, 1.6, 1.25
    lh = 0.55
    body = G.bevel(G.box('Prem_Body', (w, d, h), (x, 0, h / 2), wood), 0.03, 2)
    lid = G.bevel(G.box('Prem_Lid', (w + 0.04, d + 0.04, lh), (x, 0, h + lh / 2), wood, taper_top=0.94), 0.03, 2)
    t = 0.07
    trims = []
    for sx in (-1, 1):
        for sy in (-1, 1):   # vertical corner trims
            trims.append(G.box(f'Prem_Corner{sx}{sy}', (t, t, h + lh), (x + sx * (w / 2), sy * (d / 2), (h + lh) / 2), brass))
    for z in (0.04, h, h + lh - 0.02):   # horizontal rings: base, lid seam, lid top
        trims.append(G.box(f'Prem_RingF{z}', (w + t, t, t), (x, -d / 2, z), brass))
        trims.append(G.box(f'Prem_RingB{z}', (w + t, t, t), (x, d / 2, z), brass))
        trims.append(G.box(f'Prem_RingL{z}', (t, d + t, t), (x - w / 2, 0, z), brass))
        trims.append(G.box(f'Prem_RingR{z}', (t, d + t, t), (x + w / 2, 0, z), brass))
    lock = G.box('Prem_Lock', (0.3, 0.06, 0.38), (x, -d / 2 - 0.04, h - 0.02), brass)
    trims.append(lock)
    for p in [body, lid] + trims:
        G.apply_modifiers(p)
    trim = G.join(trims, 'Prem_BrassTrim')
    G.bevel(trim, 0.012, 1, harden=False)
    G.apply_modifiers(trim)
    return [body, lid, trim]


def chest_cartoon(x):
    """Exaggerated cartoon: tapered body, bulging lid tipped open, oversized lock, glowing gold inside."""
    wood = S.material('Cart_Wood', (0.36, 0.16, 0.45), roughness=0.6)
    metal = S.material('Cart_Metal', (0.15, 0.75, 0.7), roughness=0.4, metallic=0.3)
    glow = S.material('Cart_Glow', (1.0, 0.8, 0.2), roughness=0.3, emission=(1.0, 0.75, 0.15), emission_strength=4.0)
    w, d, h = 2.6, 2.0, 1.6
    body = G.bevel(G.box('Cart_Body', (w * 0.85, d * 0.85, h), (x, 0, h / 2), wood, taper_top=1.22), 0.16, 3, harden=False)
    treasure = G.bevel(G.box('Cart_Treasure', (w * 0.92, d * 0.9, 0.5), (x, 0, h + 0.05), glow, taper_top=0.6), 0.2, 2, harden=False)
    lid = G.half_cylinder('Cart_Lid', w * 1.08, d * 0.55, (0, 0, 0), wood, segments=16, squash=1.35)
    G.bevel(lid, 0.12, 2, harden=False)
    G.apply_modifiers(lid)
    lid.location = (x, d * 0.52, h + 0.02)
    lid.rotation_euler = (-1.05, 0, 0)          # tipped open ~60 degrees around the hinge
    bpy.context.view_layer.objects.active = lid
    lid.select_set(True)
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    lock = G.bevel(G.box('Cart_Lock', (0.95, 0.35, 1.0), (x, -d * 0.62, h * 0.55), metal, taper_top=0.8), 0.2, 3, harden=False)
    band = G.bevel(G.box('Cart_Band', (w * 1.1, d * 1.12, 0.32), (x, 0, 0.3), metal, taper_top=1.06), 0.1, 2, harden=False)
    for p in (body, treasure, lock, band):
        G.apply_modifiers(p)
    for p in (body, treasure, lock, band, lid):
        for f in p.data.polygons:
            f.use_smooth = True
    metal_parts = G.join([lock, band], 'Cart_Metal')
    return [body, lid, metal_parts, treasure]


def chest_premium_v2(x):
    """v2 fix for 'reads as a crate': arched lid gives the chest silhouette, corner brackets replace
    the thin uniform frame, and a larger lock plate gives the front a focal point."""
    wood = S.material('Prem_Walnut', (0.20, 0.10, 0.055), roughness=0.45)
    brass = S.material('Prem_Brass', (0.85, 0.66, 0.34), roughness=0.28, metallic=0.9)
    w, d, h = 2.6, 1.6, 1.2
    body = G.bevel(G.box('Prem_Body', (w, d, h), (x, 0, h / 2), wood), 0.03, 2)
    lid = G.bevel(G.half_cylinder('Prem_Lid', w + 0.02, d / 2 + 0.01, (x, 0, h), wood, segments=16, squash=0.55), 0.02, 1)
    t, arm = 0.08, 0.34
    parts = []
    for sx in (-1, 1):            # L-shaped corner brackets on the four front/back vertical edges
        for sy in (-1, 1):
            cx, cy = x + sx * (w / 2), sy * (d / 2)
            for z0 in (0.0, h - arm):
                parts.append(G.box(f'Prem_BrV{sx}{sy}{z0}', (t, t, arm), (cx, cy, z0 + arm / 2), brass))
                parts.append(G.box(f'Prem_BrH{sx}{sy}{z0}', (arm, t * 0.6, t), (cx - sx * arm / 2, cy, z0 + (t / 2 if z0 == 0 else arm - t / 2)), brass))
    parts.append(G.box('Prem_Seam', (w + 0.06, d + 0.06, 0.06), (x, 0, h), brass))      # lid seam band
    plate = G.box('Prem_LockPlate', (0.46, 0.06, 0.56), (x, -d / 2 - 0.035, h - 0.08), brass)
    parts.append(plate)
    for p in [body, lid] + parts:
        G.apply_modifiers(p)
    trim = G.join(parts, 'Prem_BrassTrim')
    G.bevel(trim, 0.012, 1, harden=False)
    G.apply_modifiers(trim)
    keyhole = S.material('Prem_Keyhole', (0.03, 0.02, 0.02), roughness=0.9)
    hole = G.box('Prem_Keyhole', (0.08, 0.03, 0.18), (x, -d / 2 - 0.07, h - 0.12), keyhole)
    return [body, lid, trim, hole]


def chest_cartoon_v2(x):
    """v2 fixes: lid hinged ON the back top edge and opened ~40 deg so its dome reads as a lid (v1 floated
    and read as a sofa back); treasure is a pile of coin discs with mild emission instead of a white slab;
    base band flush and thin so it no longer reads as a tray."""
    wood = S.material('Cart_Wood', (0.40, 0.17, 0.50), roughness=0.6)
    metal = S.material('Cart_Metal', (0.12, 0.70, 0.66), roughness=0.4, metallic=0.3)
    gold = S.material('Cart_Gold', (1.0, 0.70, 0.12), roughness=0.3, metallic=0.6, emission=(1.0, 0.6, 0.1), emission_strength=0.6)
    w, d, h = 2.2, 1.7, 1.6
    top_scale = 1.22
    body = G.bevel(G.box('Cart_Body', (w, d, h), (x, 0, h / 2), wood, taper_top=top_scale), 0.16, 3, harden=False)
    tw, td = w * top_scale, d * top_scale
    coins = []
    rnd = random.Random(7)
    for i in range(22):           # heap of coins poking above the rim
        r = rnd.uniform(0, 0.75)
        a = rnd.uniform(0, 6.283)
        cx, cy = x + r * 1.2 * math.cos(a), r * 0.75 * math.sin(a)
        cz = h + 0.1 + (0.75 - r) * 0.45
        tilt = (rnd.uniform(-0.6, 0.6), rnd.uniform(-0.6, 0.6), 0)
        coins.append(G.cylinder(f'Cart_Coin{i}', 0.2, 0.05, (cx, cy, cz), gold, segments=12, tilt=tilt))
    heap = G.bevel(G.box('Cart_Heap', (tw * 0.82, td * 0.78, 0.35), (x, 0, h + 0.02), gold, taper_top=0.55), 0.15, 2, harden=False)
    R = td / 2 + 0.04
    lid = G.half_cylinder('Cart_Lid', tw + 0.08, R, (0, 0, 0), wood, segments=16, squash=1.15)
    G.bevel(lid, 0.12, 2, harden=False)
    G.apply_modifiers(lid)
    for v in lid.data.vertices:                    # move the hinge (back edge, y=+R) to the local origin
        v.co.y -= R
    lid.location = (x, td / 2 - 0.12, h - 0.06)    # hinge tucked slightly INTO the body's back-top edge:
    # placing it exactly on the edge (v3) left a visible gap after bevels; a small overlap hides the seam
    lid.rotation_euler = (math.radians(-105), 0, 0)  # leaning back past vertical; at -40 (v2a) it read as a floating slab
    lock = G.bevel(G.box('Cart_Lock', (0.7, 0.3, 0.75), (x, -d * top_scale / 2 - 0.05, h * 0.78), metal, taper_top=0.8), 0.18, 3, harden=False)
    band = G.bevel(G.box('Cart_Band', (w * 1.03, d * 1.03, 0.18), (x, 0, 0.15), metal, taper_top=1.03), 0.06, 2, harden=False)
    bpy.ops.object.select_all(action='DESELECT')
    for p in coins + [lid]:
        p.select_set(True)
    bpy.context.view_layer.objects.active = lid
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    for p in (body, heap, lock, band):
        G.apply_modifiers(p)
    treasure = G.join([heap] + coins, 'Cart_Treasure')
    G.cleanup(treasure)
    metal_parts = G.join([lock, band], 'Cart_Metal')
    G.cleanup(metal_parts)
    for p in (body, treasure, metal_parts, lid):
        for f in p.data.polygons:
            f.use_smooth = True
    return [body, lid, metal_parts, treasure]


def main():
    S.reset_scene('BLENDER_EEVEE', (900, 900))
    S.three_point_lights((0, 0, 1), 4)
    S.ground(60)
    if VERSION == 'v1':
        chests = {'toy': chest_toy(-4.2), 'premium': chest_premium(0), 'cartoon': chest_cartoon(4.2)}
    else:
        chests = {'toy': chest_toy(-4.2), 'premium': chest_premium_v2(0), 'cartoon': chest_cartoon_v2(4.2)}
    os.makedirs(OUT, exist_ok=True)
    results = {'version': VERSION, 'qc': {}, 'exports': {}}
    # Line-up render (presentation-ish, same light for all three)
    lo, hi = S.bounds([o for v in chests.values() for o in v])
    c = (lo + hi) / 2
    dist = 13.5 if VERSION == 'v1' else 19.0    # v1 framing cropped both outer chests
    cam = S.add_camera('LineUp', (c.x + 2.5, c.y - dist, c.z + dist * 0.36), (c.x, c.y, c.z - 0.3), lens=50)
    bpy.context.scene.render.resolution_x, bpy.context.scene.render.resolution_y = 1500, 700
    S.render(os.path.join(OUT, f'chests_lineup_{VERSION}.png'), cam)
    bpy.data.objects.remove(cam)
    # Hide the other chests while inspecting one, so framing and silhouettes are honest
    for name, objs in chests.items():
        for other, oo in chests.items():
            for o in oo:
                o.hide_render = other != name
        # move to origin for pivot check and export, then back
        blo, bhi = S.bounds(objs[:1])       # centre on the body, not on an overhanging lid
        dx = -(blo.x + bhi.x) / 2
        for o in objs:
            o.location.x += dx
            bpy.context.view_layer.objects.active = o
        bpy.ops.object.select_all(action='DESELECT')
        for o in objs:
            o.select_set(True)
        bpy.ops.object.transform_apply(location=True)
        for o in objs:   # origin to assembly bottom-centre = world origin
            bpy.context.scene.cursor.location = (0, 0, 0)
            bpy.ops.object.select_all(action='DESELECT')
            o.select_set(True)
            bpy.context.view_layer.objects.active = o
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        S.render_views(objs, OUT, f'chest_{name}_{VERSION}', res=520)
        S.render_silhouette(objs, os.path.join(OUT, f'chest_{name}_{VERSION}_silhouette.png'))
        S.render_silhouette(objs, os.path.join(OUT, f'chest_{name}_{VERSION}_silhouette_gameplay.png'), view='gameplay')
        rep = rbx_qc.check_objects(objs, pivot=None)
        lo, hi = S.bounds(objs[:1])        # pivot is judged on the body footprint (an open lid overhangs)
        rep['_summary']['assembly_pivot_offset'] = round(((lo.x + hi.x) / 2) ** 2 + ((lo.y + hi.y) / 2) ** 2 + lo.z ** 2, 4) ** 0.5
        lo, hi = S.bounds(objs)
        rep['_summary']['assembly_size_studs'] = [round(v, 2) for v in (hi - lo)]
        results['qc'][name] = rep
        results['exports'][name] = [rbx_export.export_fbx(objs, os.path.join(OUT, 'export', f'chest_{name}.fbx')),
                                    rbx_export.export_gltf(objs, os.path.join(OUT, 'export', f'chest_{name}.glb'))]
        for o in objs:
            o.location.x -= dx
        bpy.ops.object.select_all(action='DESELECT')
        for o in objs:
            o.select_set(True)
        bpy.ops.object.transform_apply(location=True)
        for o in objs:
            o.hide_render = False
    with open(os.path.join(OUT, f'chests_report_{VERSION}.json'), 'w') as f:
        json.dump(results, f, indent=1, default=str)
    # Round trips run last because they reset the scene
    rt = {n: [rbx_export.round_trip_dimensions(p) for p in paths] for n, paths in results['exports'].items()}
    with open(os.path.join(OUT, f'chests_roundtrip_{VERSION}.json'), 'w') as f:
        json.dump(rt, f, indent=1)
    for n, rep in results['qc'].items():
        print(n, rep['_summary'])
    print(json.dumps(rt, indent=1))


if __name__ == '__main__':
    main()
