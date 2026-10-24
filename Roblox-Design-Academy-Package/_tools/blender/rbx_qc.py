"""Technical quality check for Roblox-bound meshes (Blender 5.2, bpy + bmesh).

Checks map to Roblox's published requirements (create.roblox.com/docs/art/modeling/specifications,
.../texture-specifications) plus academy house rules. Each check reports value, limit, status and
the source of the rule so an agent can tell an official requirement from a house preference.

Run inside Blender:   import rbx_qc; report = rbx_qc.check_objects(objs); rbx_qc.print_report(report)
Run from a shell:     python3 -c "import bpy, sys; sys.path.insert(0,'_tools/blender'); ..."
What this cannot see: how Studio's Importer will treat the file, real collision shape, in-game
lighting, or whether the asset *looks* good. Those need Studio and a human/visual review.
"""
import json
import math

import bpy  # must come first: with the pip 'bpy' module, bmesh only exists after bpy is imported
import bmesh

OFFICIAL = 'Roblox specifications'
TEXTURE_SPEC = 'Roblox texture specifications'
HOUSE = 'academy house rule'


def _tri_count(bm):
    return sum(len(f.verts) - 2 for f in bm.faces)


def _evaluated_bmesh(obj):
    dg = bpy.context.evaluated_depsgraph_get()
    eo = obj.evaluated_get(dg)
    me = eo.to_mesh()
    bm = bmesh.new()
    bm.from_mesh(me)
    eo.to_mesh_clear()
    return bm


def check_object(obj, tri_budget=20000, pivot='bottom-center'):
    """Return a list of check dicts for one mesh object, evaluated with its modifiers applied."""
    bm = _evaluated_bmesh(obj)
    bm.verts.ensure_lookup_table()
    res = []

    def add(name, value, limit, ok, source, fix=''):
        res.append({'check': name, 'value': value, 'limit': limit,
                    'status': 'PASS' if ok else ('WARN' if source == HOUSE else 'FAIL'),
                    'source': source, 'fix': '' if ok else fix})

    tris = _tri_count(bm)
    add('triangles', tris, f'<= {tri_budget}', tris <= tri_budget, OFFICIAL,
        'Decimate, remove hidden faces, or split into several meshes.')
    ngons = sum(1 for f in bm.faces if len(f.verts) > 4)
    add('ngons (faces > 4 verts)', ngons, '0 where possible', ngons == 0, OFFICIAL,
        'Triangulate or re-cut with loop cuts; check for shading artifacts after.')
    non_manifold = sum(1 for e in bm.edges if not e.is_manifold)
    add('non-manifold edges (watertight)', non_manifold, '0', non_manifold == 0, OFFICIAL,
        'Select > All by Trait > Non Manifold, then fill holes / merge by distance.')
    loose = sum(1 for v in bm.verts if not v.link_edges)
    add('loose vertices', loose, '0', loose == 0, HOUSE, 'Mesh > Clean Up > Delete Loose.')
    degenerate = sum(1 for f in bm.faces if f.calc_area() < 1e-8)
    add('zero-area faces', degenerate, '0', degenerate == 0, HOUSE, 'Mesh > Clean Up > Degenerate Dissolve.')
    # Normals: compare with a copy whose normals were recalculated outside.
    before = [f.normal.copy() for f in bm.faces]
    bm2 = bm.copy()
    bmesh.ops.recalc_face_normals(bm2, faces=bm2.faces)
    flipped = sum(1 for a, f in zip(before, bm2.faces) if a.dot(f.normal) < 0)
    bm2.free()
    add('faces pointing inward', flipped, '0', flipped == 0, HOUSE,
        'Mesh > Normals > Recalculate Outside (Shift+N).')
    # Volume: zero-thickness check via bounding box.
    dims = obj.dimensions
    thin = min(dims) < 1e-4
    add('has volume (not a flat plane)', [round(d, 3) for d in dims], 'min dim > 0', not thin, OFFICIAL,
        'Add thickness (Solidify) - Roblox meshes cannot be 0 thickness.')
    # Transforms.
    scale_ok = all(abs(s - 1) < 1e-4 for s in obj.scale)
    add('object scale applied', [round(s, 4) for s in obj.scale], '(1,1,1)', scale_ok, HOUSE,
        'Object > Apply > Scale (Ctrl+A) so exported size equals modelled size.')
    rot_ok = all(abs(r) < 1e-4 for r in obj.rotation_euler)
    add('object rotation applied', [round(math.degrees(r), 2) for r in obj.rotation_euler], '(0,0,0)', rot_ok, HOUSE,
        'Object > Apply > Rotation.')
    # Pivot.
    lo = [min((obj.matrix_world @ v.co)[i] for v in bm.verts) for i in range(3)] if bm.verts else [0, 0, 0]
    hi = [max((obj.matrix_world @ v.co)[i] for v in bm.verts) for i in range(3)] if bm.verts else [0, 0, 0]
    o = obj.matrix_world.translation
    if pivot is None:
        target = None
    elif pivot == 'bottom-center':
        target = ((lo[0] + hi[0]) / 2, (lo[1] + hi[1]) / 2, lo[2])
    else:
        target = tuple((lo[i] + hi[i]) / 2 for i in range(3))
    if target is not None:   # pivot=None: part of an assembly whose pivot is checked as a whole
        off = math.dist(tuple(o), target)
        size = max(hi[i] - lo[i] for i in range(3)) or 1
        add(f'pivot at {pivot}', round(off, 4), f'<= {round(size * 0.02, 4)} (2% of size)', off <= size * 0.02, HOUSE,
            'Set origin: snap 3D cursor to the intended pivot, Object > Set Origin > Origin to 3D Cursor.')
    # Materials and UVs.
    mats = len([m for m in obj.data.materials if m])
    add('material slots', mats, '<= 1 per mesh', mats <= 1, TEXTURE_SPEC,
        'Roblox meshes take one material: bake/atlas, use vertex colour, or split the mesh.')
    uvs = len(obj.data.uv_layers)
    add('UV sets', uvs, '<= 1', uvs <= 1, TEXTURE_SPEC, 'Delete extra UV maps.')
    if uvs:
        layer = bm.loops.layers.uv.active
        out = sum(1 for f in bm.faces for l in f.loops
                  if not (-1e-4 <= l[layer].uv.x <= 1.0001 and -1e-4 <= l[layer].uv.y <= 1.0001))
        add('UVs inside 0-1', out, '0 loops outside', out == 0, TEXTURE_SPEC, 'Pack islands (UV > Pack Islands).')
    smooth = sum(1 for f in bm.faces if f.smooth)
    res.append({'check': 'smooth-shaded faces (info)', 'value': f'{smooth}/{len(bm.faces)}', 'limit': 'intentional',
                'status': 'INFO', 'source': HOUSE, 'fix': ''})
    res.append({'check': 'size in studs (info)', 'value': [round(hi[i] - lo[i], 3) for i in range(3)],
                'limit': 'matches intended in-game size', 'status': 'INFO', 'source': HOUSE, 'fix': ''})
    bm.free()
    return res


def check_objects(objs, **kw):
    report = {o.name: check_object(o, **kw) for o in objs if o.type == 'MESH'}
    total = sum(r['value'] for checks in report.values() for r in checks if r['check'] == 'triangles')
    report['_summary'] = {
        'meshes': len(report),
        'total_triangles': total,
        'fails': sum(1 for k, v in report.items() if k != '_summary' for r in v if r['status'] == 'FAIL'),
        'warns': sum(1 for k, v in report.items() if k != '_summary' for r in v if r['status'] == 'WARN'),
    }
    return report


def print_report(report):
    for name, checks in report.items():
        if name == '_summary':
            continue
        print(f'== {name}')
        for r in checks:
            print(f"  [{r['status']:4}] {r['check']}: {r['value']} (limit {r['limit']}; {r['source']})"
                  + (f"  -> {r['fix']}" if r['fix'] else ''))
    print('SUMMARY', json.dumps(report['_summary']))


def save_report(report, path):
    with open(path, 'w') as f:
        json.dump(report, f, indent=1)
