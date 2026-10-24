---
title: "BL-18 — Technical troubleshooting (Blender → Roblox)"
tags: [blender, troubleshooting, roblox]
note_type: "reference"
evidence: "mix: real failures from this session (marked ✅) and documented issues (marked 📄)"
---

# BL-18 — Technical troubleshooting

| Symptom | Likely cause | Fix | Evidence |
|---|---|---|---|
| Model imports far too big in Studio | Default FBX scaling | Apply Scalings = FBX Unit Scale, or use glTF | 📄 Roblox art/blender "Adjust scale (FBX)" |
| Model lies on its side | Axis settings | Export Z Forward / Y Up; Studio World Forward Front / Up Top | 📄 art/blender |
| Importer rejects the mesh / errors | Over 20k tris, non-manifold, n-gons, zero-thickness | Run `rbx_qc`; fix FAIL items | 📄 specifications |
| Black or inside-out faces | Normals inverted | Shift+N; QC "faces pointing inward" | ✅ check implemented |
| Shading gradients on flat faces | Smooth shading without weighted normals | Bevel (harden) + Weighted Normal | 📄 Blender manual |
| N-gon FAIL on caps | Single cap face | Triangle fan | ✅ FC-BL-03 |
| Non-manifold after fixing n-gons | T-junction (fan centre on an edge not shared) | Split the adjoining face to use the new vertex | ✅ FC-BL-03 |
| Parts float with small gaps | Exact contact + bevels | Overlap parts slightly | ✅ FC-BL-05 |
| Rotated parts end up far away | Rotation around the world origin (object origin at 0,0,0) | Rotate in mesh space around the part centre, or set the origin first | ✅ FC-BL-04 |
| Asset half-hidden in renders | Ground plane cuts a centre/grip pivot | Lift for inspection renders | ✅ BL-EX-02/05 |
| `ModuleNotFoundError: bmesh` (pip bpy) | `import bmesh` before `import bpy` | Import bpy first | ✅ FC-BL-02 |
| EEVEE crash headless: `libEGL.so.1` missing | No EGL in container | Install libegl1 + Mesa, or use Cycles | ✅ FC-BL-01 |
| Many identical props, many draw calls | Each copy imported separately (different asset ids) | Import once, duplicate in Studio | 📄 performance-optimization/improve |
| Textures missing after import | Not embedded | Path Mode Copy + Embed Textures | 📄 export-requirements |
| Two materials on one mesh | Roblox allows one per mesh | Split by material or use a palette texture | 📄 texture-specifications; ✅ BL-EX-07 |
| Old tutorial says "Auto Smooth checkbox" | Removed in Blender 4.1 | Shade Auto Smooth (Smooth by Angle modifier) | ✅ bpy 5.2.3 introspection |

## Sources
Accessed 2026-10-24. Roblox pages from the creator-docs repository (commit 4e795e6); Blender pages from the 5.2 LTS manual (the URLs use `latest`, which served 5.2 on that date).
- [Export requirements](https://create.roblox.com/docs/art/modeling/export-requirements)
- [Mesh specifications](https://create.roblox.com/docs/art/modeling/specifications)
- Blender manual: [Editing Normals](https://docs.blender.org/manual/en/latest/modeling/meshes/editing/mesh/normals.html)
- [bpy 5.2.3 on PyPI](https://pypi.org/project/bpy/) — operator and property names confirmed by introspection in this environment
