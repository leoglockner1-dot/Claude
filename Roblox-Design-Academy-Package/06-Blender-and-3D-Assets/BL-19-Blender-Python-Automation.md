---
title: "BL-19 — Blender Python automation (tested toolkit)"
tags: [blender, python, bpy, automation, tooling]
note_type: "procedure"
evidence: "tested in this session with bpy 5.2.3 (pip) on Linux, headless"
code: "_tools/blender/"
---

# BL-19 — Blender Python automation

## Environment that was verified
- `bpy` **5.2.3** from PyPI (`pip install bpy==5.2.3`). It needs **Python 3.13** for this version (the wheel is cp313). Installed in a venv with `uv`.
- Linux container, no GPU. Cycles CPU works out of the box; EEVEE/Workbench need `libegl1 libegl-mesa0 libgl1-mesa-dri` (software rendering) and print harmless `EGL_BAD_MATCH` warnings.
- In the Blender application you can run the same scripts with `blender -b -P script.py -- args` (not tested here; the Blender download servers timed out from this environment).

## Toolkit modules ([`_tools/blender/`](../_tools/blender/))
| Module | What it does |
|---|---|
| `rbx_scene.py` | Reset a scene to Roblox conventions (units None), materials, 3-point lights, cameras framed from bounds, **inspection renders** (ortho + 3/4 + wire-over-clay), silhouettes (front and gameplay angle), downscale sheets, contact sheets |
| `rbx_qc.py` | Technical QC against Roblox specs and house rules: triangles, n-gons, non-manifold, loose verts, zero-area faces, inward faces, volume, scale/rotation applied, pivot, material slots, UV sets, UV range. Each check reports its **source** (Roblox spec vs house rule) |
| `rbx_export.py` | FBX/GLB/OBJ export with the documented settings; round-trip dimension check |
| `rbx_shapes.py` | Small builders: box (with taper), half-cylinder lid (fan caps), cylinder, rock, crystal, bevel helper, cleanup, join |
| `rbx_exercise.py` | Harness: centre on pivot → inspection set → QC → export |
| `ex_treasure_chests.py`, `ex_props.py`, `ex_extra.py` (palette, animated pickup, VFX), `ex_modular_kit.py` | Exercises (see the exercise notes) |

## Run
```bash
python3 -m venv .venv && .venv/bin/pip install bpy==5.2.3 pillow numpy    # Python 3.13
cd _tools/blender
../../.venv/bin/python ex_treasure_chests.py out/chests v4
../../.venv/bin/python ex_props.py out/props v2
../../.venv/bin/python ex_extra.py out/extra          # ONLY=ex07,ex11,ex12 to pick
../../.venv/bin/python ex_modular_kit.py out/kit v2
```
Runtime here (software EEVEE, 4 cores): ~6–8 min for the chest exercise, ~12 min for props.

## Writing your own automation: rules learned
1. `import bpy` before `bmesh` (pip module).
2. Builders put object origins at the world origin, so **rotate geometry in bmesh around its own centre**, not via `object.rotation_euler` plus apply.
3. Call `bpy.context.view_layer.update()` after moving objects and before reading `matrix_world`/bounds.
4. Evaluate meshes through the depsgraph for QC (`obj.evaluated_get(depsgraph).to_mesh()`), because that is what gets exported.
5. Keep generated helper objects prefixed `_`, and exclude them from exports and QC.
6. Make every script take an output directory and a version label, so v1/v2 evidence sits side by side.
7. Do not kill background renders with `pkill -f <script name>` from a command line that contains the same name; it kills the launching shell too ([FC-WF-01](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-WF-01-Pkill-Matched-Own-Shell.md)).

## Procedural generation, used well
See [BL-21](BL-21-Procedural-Variation.md). Automate the **repetitive** work (camera rigs, exports, QC, batch renders, variations of one designed asset). Leave the design decisions to a person or a critiqued loop.

## Sources
Accessed 2026-10-24. Roblox pages from the creator-docs repository (commit 4e795e6); Blender pages from the 5.2 LTS manual (the URLs use `latest`, which served 5.2 on that date).
- [bpy 5.2.3 on PyPI](https://pypi.org/project/bpy/) — operator and property names confirmed by introspection in this environment
- Tested code: `_tools/blender/` in this package.
