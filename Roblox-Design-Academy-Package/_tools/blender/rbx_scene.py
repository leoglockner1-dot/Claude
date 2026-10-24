"""Scene, camera, lighting and render helpers for Roblox-bound assets (Blender 5.2, bpy).

Conventions used by every academy script:
- 1 Blender unit = 1 stud (Scene > Units > Unit System = None, as Roblox's Blender guide says).
- Assets sit on the ground plane with the pivot (origin) at bottom-centre unless noted.
- Presentation renders and inspection renders are different things: `render_views` makes the
  honest inspection set (front/side/top orthographic + 3/4 + wire-over-clay), `render_hero`
  makes the flattering one. Never judge an asset from the hero render alone.
"""
import math
import os

import bpy
from mathutils import Vector


def reset_scene(engine='BLENDER_EEVEE', res=(800, 800)):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    s = bpy.context.scene
    s.unit_settings.system = 'NONE'
    s.unit_settings.system_rotation = 'DEGREES'
    s.render.engine = engine
    s.render.resolution_x, s.render.resolution_y = res
    s.render.film_transparent = False
    s.view_settings.view_transform = 'Standard'   # predictable colours; AgX desaturates stylised palettes
    if engine == 'CYCLES':
        s.cycles.samples = 48
        s.cycles.device = 'CPU'
    world = bpy.data.worlds.new('World')
    world.use_nodes = True
    s.world = world
    set_background((0.18, 0.19, 0.22))
    return s


def set_background(rgb, strength=1.0):
    bg = bpy.context.scene.world.node_tree.nodes['Background']
    bg.inputs['Color'].default_value = (*rgb, 1)
    bg.inputs['Strength'].default_value = strength


def material(name, rgb, roughness=0.6, metallic=0.0, emission=None, emission_strength=0.0):
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes = True
    p = m.node_tree.nodes['Principled BSDF']
    p.inputs['Base Color'].default_value = (*rgb, 1)
    p.inputs['Roughness'].default_value = roughness
    p.inputs['Metallic'].default_value = metallic
    if emission:
        p.inputs['Emission Color'].default_value = (*emission, 1)
        p.inputs['Emission Strength'].default_value = emission_strength
    return m


def bounds(objs):
    pts = [o.matrix_world @ Vector(c) for o in objs if o.type == 'MESH' for c in o.bound_box]
    lo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    hi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    return lo, hi


def add_camera(name, loc, target, ortho_scale=None, lens=50):
    cam = bpy.data.objects.new(name, bpy.data.cameras.new(name))
    bpy.context.scene.collection.objects.link(cam)
    cam.location = loc
    direction = Vector(target) - Vector(loc)
    cam.rotation_euler = direction.to_track_quat('-Z', 'Y').to_euler()
    if ortho_scale:
        cam.data.type = 'ORTHO'
        cam.data.ortho_scale = ortho_scale
    else:
        cam.data.lens = lens
    return cam


def three_point_lights(center, size, key_energy=3.0):
    """Key (warm, upper left), fill (cool, right), rim (behind). Sun lights keep it scale-independent."""
    out = []
    for name, rot, energy, col in (
        ('Key', (math.radians(50), 0, math.radians(-40)), key_energy, (1.0, 0.95, 0.88)),
        ('Fill', (math.radians(65), 0, math.radians(60)), key_energy * 0.35, (0.85, 0.9, 1.0)),
        ('Rim', (math.radians(120), 0, math.radians(170)), key_energy * 0.8, (1, 1, 1)),
    ):
        light = bpy.data.objects.new(name, bpy.data.lights.new(name, 'SUN'))
        light.data.energy = energy
        light.data.color = col
        light.rotation_euler = rot
        bpy.context.scene.collection.objects.link(light)
        out.append(light)
    return out


def ground(size=40, rgb=(0.32, 0.33, 0.36)):
    bpy.ops.mesh.primitive_plane_add(size=size, location=(0, 0, 0))
    g = bpy.context.active_object
    g.name = '_Ground'
    g.data.materials.append(material('_GroundMat', rgb, roughness=0.9))
    return g


def render(path, camera):
    s = bpy.context.scene
    s.camera = camera
    s.render.filepath = path
    os.makedirs(os.path.dirname(path), exist_ok=True)
    bpy.ops.render.render(write_still=True)
    return path


def _clay_override(objs, on):
    """Swap every asset material for neutral clay (on=True) or restore (on=False)."""
    clay = material('_Clay', (0.7, 0.7, 0.7), roughness=0.8)
    for o in objs:
        if o.type != 'MESH':
            continue
        if on:
            o['_mats'] = [m.name if m else '' for m in o.data.materials]
            for i in range(len(o.data.materials)):
                o.data.materials[i] = clay
            if not o.data.materials:
                o.data.materials.append(clay)
                o['_mats'] = ['']
        else:
            names = list(o.get('_mats', []))
            for i, n in enumerate(names):
                o.data.materials[i] = bpy.data.materials.get(n) if n else None
            if names == ['']:
                o.data.materials.clear()


def _wire_overlay(objs, on, thickness):
    wires = []
    if not on:
        for o in [o for o in bpy.data.objects if o.name.startswith('_Wire_')]:
            bpy.data.objects.remove(o)
        return wires
    wm = material('_WireMat', (0.05, 0.05, 0.06), roughness=1.0)
    for o in objs:
        if o.type != 'MESH':
            continue
        w = o.copy()
        w.data = o.data.copy()
        w.name = '_Wire_' + o.name
        bpy.context.scene.collection.objects.link(w)
        w.data.materials.clear()
        w.data.materials.append(wm)
        mod = w.modifiers.new('Wire', 'WIREFRAME')
        mod.thickness = thickness
        mod.use_replace = True
        mod.use_even_offset = True
        wires.append(w)
    return wires


def render_views(objs, out_dir, stem, res=600):
    """Inspection set: front, side, top (orthographic), 3/4 perspective, and wire-over-clay 3/4.
    Returns the list of written files. Camera framing comes from the assets' world bounds."""
    s = bpy.context.scene
    s.render.resolution_x = s.render.resolution_y = res
    lo, hi = bounds(objs)
    c = (lo + hi) / 2
    size = max((hi - lo).x, (hi - lo).y, (hi - lo).z)
    d = size * 3
    ortho = size * 1.35
    files = []
    views = {
        'front': add_camera('CamFront', (c.x, c.y - d, c.z), c, ortho),
        'side': add_camera('CamSide', (c.x + d, c.y, c.z), c, ortho),
        'top': add_camera('CamTop', (c.x, c.y - 0.001, c.z + d), c, ortho),
        'threequarter': add_camera('Cam34', (c.x + d * 0.62, c.y - d * 0.78, c.z + d * 0.48), c, lens=60),
    }
    for name, cam in views.items():
        files.append(render(os.path.join(out_dir, f'{stem}_{name}.png'), cam))
    _clay_override(objs, True)
    _wire_overlay(objs, True, thickness=size * 0.004)
    files.append(render(os.path.join(out_dir, f'{stem}_wire.png'), views['threequarter']))
    _wire_overlay(objs, False, 0)
    _clay_override(objs, False)
    for cam in views.values():
        bpy.data.objects.remove(cam)
    return files


def render_at_size(src_png, out_png, sizes=(512, 150, 64, 32)):
    """Readability check: the same image downscaled to typical on-screen sizes, side by side."""
    from PIL import Image
    im = Image.open(src_png).convert('RGB')
    w = sum(sizes) + 10 * (len(sizes) + 1)
    sheet = Image.new('RGB', (w, max(sizes) + 20), (24, 24, 28))
    x = 10
    for sz in sizes:
        sheet.paste(im.resize((sz, sz), Image.LANCZOS), (x, 10))
        x += sz + 10
    sheet.save(out_png)
    return out_png


def contact_sheet(files, out_png, cols=3, cell=360, labels=True):
    from PIL import Image, ImageDraw
    rows = (len(files) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * cell, rows * (cell + (18 if labels else 0))), (20, 20, 24))
    d = ImageDraw.Draw(sheet)
    for i, f in enumerate(files):
        im = Image.open(f).convert('RGB')
        im.thumbnail((cell, cell))
        x, y = (i % cols) * cell, (i // cols) * (cell + (18 if labels else 0))
        sheet.paste(im, (x, y))
        if labels:
            d.text((x + 4, y + cell + 2), os.path.basename(f), fill=(220, 220, 220))
    sheet.save(out_png)
    return out_png


def render_silhouette(objs, out_png, res=400, view='front'):
    """Flat black silhouette on white (alpha of a transparent-film render). Use it to judge shape
    language without colour, lighting or detail helping."""
    from PIL import Image
    s = bpy.context.scene
    hidden = [o for o in s.objects if o.type == 'MESH' and o not in objs and not o.hide_render]
    for o in hidden:
        o.hide_render = True
    s.render.film_transparent = True
    s.render.resolution_x = s.render.resolution_y = res
    lo, hi = bounds(objs)
    c = (lo + hi) / 2
    size = max((hi - lo).x, (hi - lo).y, (hi - lo).z)
    loc = {'front': (c.x, c.y - size * 3, c.z), 'side': (c.x + size * 3, c.y, c.z),
           # 'gameplay': elevated 3/4 like a default third-person Roblox camera looking down at a prop
           'gameplay': (c.x + size * 1.6, c.y - size * 2.4, c.z + size * 1.8)}[view]
    cam = add_camera('CamSil', loc, c, size * 1.5)
    tmp = out_png + '.rgba.png'
    render(tmp, cam)
    bpy.data.objects.remove(cam)
    s.render.film_transparent = False
    for o in hidden:
        o.hide_render = False
    a = Image.open(tmp).split()[-1].point(lambda v: 0 if v > 128 else 255)
    a.convert('RGB').save(out_png)
    os.remove(tmp)
    return out_png
