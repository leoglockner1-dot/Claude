"""Exercises BL-EX-07 (palette texture: many colours -> one mesh, one material), BL-EX-11 (animated
pickup export) and BL-EX-12 (VFX geometry: shockwave ring + slash ribbon with gradient UVs).

Acceptance criteria (set before building):
  BL-EX-07  the toy chest (3 meshes, 3 flat materials) becomes ONE mesh with ONE material and ONE UV set,
            UVs inside 0-1, colours preserved: mean render difference vs the 3-material original < 3/255
            per channel inside the object mask; FBX with embedded palette PNG exports and re-imports.
  BL-EX-11  a coin with a looping spin (360 deg / 2 s) + bob exports to FBX with baked animation, and the
            re-imported file still contains an action whose frame range matches (Blender-side check).
  BL-EX-12  ring and slash meshes are watertight-free *cards* (VFX meshes are allowed to be open; QC
            non-manifold FAIL is expected and documented), UVs run 0->1 along the effect so one gradient
            texture fades them; tris <= 200 each.
Run:  python3 ex_extra.py <out_dir>
"""
import json
import math
import os
import sys

import bpy
import bmesh

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rbx_export
import rbx_qc
import rbx_scene as S
import rbx_shapes as G

OUT = sys.argv[1] if len(sys.argv) > 1 else '/tmp/extra'
os.makedirs(OUT, exist_ok=True)


def linear_to_srgb(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def palette_convert(objs, name, png_path, swatch=8):
    """Join objects into one mesh whose faces sample swatches of a generated palette image."""
    from PIL import Image
    mats = []
    for o in objs:
        for m in o.data.materials:
            if m and m not in mats:
                mats.append(m)
    n = len(mats)
    cols = math.ceil(math.sqrt(n))
    size = cols * swatch
    img = Image.new('RGB', (size, size), (255, 0, 255))
    centres = {}
    for i, m in enumerate(mats):
        rgb = m.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value[:3]
        px = tuple(int(round(linear_to_srgb(c) * 255)) for c in rgb)   # Base Color is linear; PNG is sRGB
        cx, cy = (i % cols), (i // cols)
        for x in range(cx * swatch, (cx + 1) * swatch):
            for y in range(cy * swatch, (cy + 1) * swatch):
                img.putpixel((x, y), px)
        # UV v axis points up, image rows go down
        centres[m.name] = ((cx + 0.5) / cols, 1 - (cy + 0.5) / cols)
    img.save(png_path)
    # record each face's material before joining
    for o in objs:
        me = o.data
        if not me.uv_layers:
            me.uv_layers.new(name='UVMap')
        uv = me.uv_layers.active.data
        for poly in me.polygons:
            m = me.materials[poly.material_index]
            u, v = centres[m.name]
            for li in poly.loop_indices:
                uv[li].uv = (u, v)
    joined = G.join(objs, name)
    joined.data.materials.clear()
    mat = bpy.data.materials.new(name + '_Palette')
    mat.use_nodes = True
    nt = mat.node_tree
    tex = nt.nodes.new('ShaderNodeTexImage')
    tex.image = bpy.data.images.load(png_path)
    tex.interpolation = 'Closest'                # crisp swatches, no bleeding between colours
    nt.links.new(tex.outputs['Color'], nt.nodes['Principled BSDF'].inputs['Base Color'])
    nt.nodes['Principled BSDF'].inputs['Roughness'].default_value = 0.5
    joined.data.materials.append(mat)
    for poly in joined.data.polygons:
        poly.material_index = 0
    return joined, {'materials_in': n, 'palette_px': size, 'colours': {m.name: centres[m.name] for m in mats}}


def render_mask_diff(a_png, b_png):
    import numpy as np
    from PIL import Image
    a = np.asarray(Image.open(a_png).convert('RGB')).astype(float)
    b = np.asarray(Image.open(b_png).convert('RGB')).astype(float)
    bg = a[0, 0]
    mask = np.abs(a - bg).sum(axis=2) > 6
    d = np.abs(a - b)[mask]
    return {'mask_pixels': int(mask.sum()), 'mean_abs_diff_per_channel': [round(float(x), 2) for x in d.mean(axis=0)],
            'p99_abs_diff': round(float(np.percentile(d, 99)), 2)}


def ex07():
    S.reset_scene('BLENDER_EEVEE', (600, 600))
    S.three_point_lights((0, 0, 1), 4)
    S.ground(30)
    import ex_treasure_chests as chests          # builders only; its main() is guarded
    parts = chests.chest_toy(0.0)
    cam = S.add_camera('Cam', (4.2, -5.6, 4.0), (0, 0, 1.0), lens=50)
    before = S.render(os.path.join(OUT, 'ex07_before_3materials.png'), cam)
    qc_before = rbx_qc.check_objects(parts, pivot=None)
    joined, info = palette_convert(parts, 'Toy_Chest', os.path.join(OUT, 'ex07_palette.png'))
    after = S.render(os.path.join(OUT, 'ex07_after_palette.png'), cam)
    qc_after = rbx_qc.check_objects([joined], pivot='bottom-center')
    diff = render_mask_diff(before, after)
    fbx = rbx_export.export_fbx([joined], os.path.join(OUT, 'export', 'toy_chest_palette.fbx'))
    glb = rbx_export.export_gltf([joined], os.path.join(OUT, 'export', 'toy_chest_palette.glb'))
    res = {'info': info, 'diff': diff, 'qc_before_summary': qc_before['_summary'],
           'qc_after': {k: v for k, v in qc_after.items()}, 'exports': [fbx, glb]}
    rt = [rbx_export.round_trip_dimensions(p) for p in (fbx, glb)]
    # check that the re-imported GLB still references an image texture
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=glb)
    imgs = [i.name for i in bpy.data.images]
    res['roundtrip'] = rt
    res['glb_reimport_images'] = imgs
    return res


def ex11():
    S.reset_scene('BLENDER_EEVEE', (400, 400))
    gold = S.material('CoinGold', (1.0, 0.72, 0.15), roughness=0.3, metallic=0.85)
    coin = G.cylinder('Coin_Anim', 0.6, 0.14, (0, 0, 0), gold, segments=24, axis='Y')
    G.bevel(coin, 0.04, 2, angle_deg=30)
    G.apply_modifiers(coin)
    scene = bpy.context.scene
    scene.render.fps = 30
    scene.frame_start, scene.frame_end = 1, 61
    for f, rot, z in ((1, 0, 1.5), (31, math.pi, 1.75), (61, 2 * math.pi, 1.5)):
        coin.rotation_euler = (0, 0, rot)
        coin.location = (0, 0, z)
        coin.keyframe_insert('rotation_euler', index=2, frame=f)
        coin.keyframe_insert('location', index=2, frame=f)
    # linear spin so the loop has no ease-in/ease-out hitch at the seam (Blender 5.x layered actions:
    # walk every F-curve the action exposes, through channelbags when present)
    act = coin.animation_data.action
    fcurves = []
    try:
        for layer in act.layers:
            for strip in layer.strips:
                for bag in strip.channelbags:
                    fcurves += list(bag.fcurves)
    except AttributeError:
        fcurves = list(act.fcurves)
    for fc in fcurves:
        if fc.data_path == 'rotation_euler':
            for kp in fc.keyframe_points:
                kp.interpolation = 'LINEAR'
    path = os.path.join(OUT, 'export', 'coin_spin_bob.fbx')
    rbx_export.export_fbx([coin], path, animated=True)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.fbx(filepath=path)
    actions = [(a.name, list(a.frame_range)) for a in bpy.data.actions]
    return {'export': path, 'bytes': os.path.getsize(path), 'reimported_actions': actions, 'fcurves_set_linear': len(fcurves)}


def gradient_png(path, w=64, h=8):
    """Horizontal ramp: transparent/dark at u=0 (tail) -> bright opaque at u=0.85 -> fades at u=1 (head)."""
    from PIL import Image
    img = Image.new('RGBA', (w, h))
    for x in range(w):
        u = x / (w - 1)
        a = min(1.0, u / 0.85) if u <= 0.85 else max(0.0, 1 - (u - 0.85) / 0.15)
        for y in range(h):
            v = y / (h - 1)
            edge = 1 - abs(2 * v - 1) ** 3          # soft across the width too
            img.putpixel((x, y), (int(160 + 95 * a), int(220 * a + 30), 255, int(255 * a * edge)))
    img.save(path)
    return path


def ex12():
    """v2: v1 rendered both meshes as flat white shapes (emission 3.0 blew out; no texture, so the UV
    gradient - the point of the exercise - was invisible; slash cropped). v2 drives colour AND alpha from
    a generated gradient through the UVs, lowers emission, and frames both meshes."""
    S.reset_scene('BLENDER_EEVEE', (900, 500))
    S.set_background((0.06, 0.06, 0.08))
    grad = gradient_png(os.path.join(OUT, 'ex12_gradient.png'))
    mat = bpy.data.materials.new('VfxGradient')
    mat.use_nodes = True
    nt = mat.node_tree
    p = nt.nodes['Principled BSDF']
    tex = nt.nodes.new('ShaderNodeTexImage')
    tex.image = bpy.data.images.load(grad)
    nt.links.new(tex.outputs['Color'], p.inputs['Emission Color'])
    nt.links.new(tex.outputs['Color'], p.inputs['Base Color'])
    nt.links.new(tex.outputs['Alpha'], p.inputs['Alpha'])
    p.inputs['Emission Strength'].default_value = 1.2
    try:
        mat.surface_render_method = 'BLENDED'     # EEVEE Next alpha blending
    except AttributeError:
        pass
    # Shockwave ring: flat annulus; U around, V inner(0) -> outer(1). For a ring we want the fade across
    # the width, so map V (not U) to the gradient: rotate the UVs 90 degrees.
    bm = bmesh.new()
    uv = bm.loops.layers.uv.new('UVMap')
    seg, r0, r1 = 32, 1.4, 2.0
    inner = [bm.verts.new((math.cos(2 * math.pi * i / seg) * r0, math.sin(2 * math.pi * i / seg) * r0, 0.05)) for i in range(seg)]
    outer = [bm.verts.new((math.cos(2 * math.pi * i / seg) * r1, math.sin(2 * math.pi * i / seg) * r1, 0.05)) for i in range(seg)]
    for i in range(seg):
        j = (i + 1) % seg
        f = bm.faces.new((inner[i], inner[j], outer[j], outer[i]))
        for loop, (u, v) in zip(f.loops, ((0.0, 0.5), (0.0, 0.5), (0.85, 0.5), (0.85, 0.5))):
            loop[uv].uv = (u, v)                  # inner edge transparent -> outer edge bright
    ring = G._new_obj('Vfx_Shockwave', bm, mat)
    # Slash ribbon: U along the arc (0 tail -> 1 head), V across the width
    bm = bmesh.new()
    uv = bm.loops.layers.uv.new('UVMap')
    seg = 16
    rows = []
    for i in range(seg + 1):
        t = i / seg
        a = math.radians(-60 + 150 * t)
        width = 0.05 + 0.45 * math.sin(math.pi * t)
        rr = 2.0
        rows.append((bm.verts.new((math.cos(a) * (rr - width) + 5, math.sin(a) * (rr - width), 0.05)),
                     bm.verts.new((math.cos(a) * (rr + width) + 5, math.sin(a) * (rr + width), 0.05)), t))
    for (a0, b0, t0), (a1, b1, t1) in zip(rows, rows[1:]):
        f = bm.faces.new((a0, a1, b1, b0))
        for loop, (u, v) in zip(f.loops, ((t0, 0), (t1, 0), (t1, 1), (t0, 1))):
            loop[uv].uv = (u, v)
    slash = G._new_obj('Vfx_Slash', bm, mat)
    bpy.context.view_layer.update()
    cam = S.add_camera('Cam', (2.6, -0.001, 11.0), (2.6, 0, 0), ortho_scale=10.5)
    png = S.render(os.path.join(OUT, 'ex12_vfx_meshes_v2.png'), cam)
    qc = rbx_qc.check_objects([ring, slash], pivot=None, card=True)
    exports = [rbx_export.export_fbx([ring], os.path.join(OUT, 'export', 'vfx_shockwave.fbx')),
               rbx_export.export_fbx([slash], os.path.join(OUT, 'export', 'vfx_slash.fbx'))]
    return {'render': png, 'qc': qc, 'exports': exports}


if __name__ == '__main__':
    only = (os.environ.get('ONLY') or 'ex07,ex11,ex12').split(',')
    results = {name: fn() for name, fn in (('ex07', ex07), ('ex11', ex11), ('ex12', ex12)) if name in only}
    out = os.path.join(OUT, 'extra_results_%s.json' % '_'.join(sorted(results)))
    with open(out, 'w') as f:
        json.dump(results, f, indent=1, default=str)
    for name, r in results.items():
        summary = {k: v for k, v in r.items() if k in ('diff', 'glb_reimport_images', 'reimported_actions', 'bytes')}
        if 'qc' in r:
            summary['qc'] = r['qc']['_summary']
        if 'qc_after' in r:
            summary['qc_after'] = r['qc_after']['_summary']
        print(name, json.dumps(summary, default=str))
