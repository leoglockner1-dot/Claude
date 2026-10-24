---
title: "BL-00 — Blender-to-Roblox pipeline (facts and defaults)"
tags: [blender, roblox, pipeline, export, import, reference]
note_type: "reference"
evidence: "official docs (Roblox creator-docs 4e795e6; Blender 5.2.3 bpy introspection)"
---

# BL-00 — Blender-to-Roblox pipeline (facts and defaults)

The facts every Roblox asset depends on, each with its source. **[RBX]** = Roblox Creator Docs. **[BPY]** = verified by running Blender 5.2.3 (`bpy` module) in this session. **[HOUSE]** = academy convention.

## Units, axes, scale
| Fact | Source |
|---|---|
| 1 stud = 28 cm (Roblox units table) | [RBX] physics/units |
| Set Blender Scene > Units > **Unit System = None** (and Rotation = Degrees) so that 1 Blender unit = 1 stud | [RBX] art/blender |
| Blender is Z-up; Studio is Y-up | [RBX] art/blender |
| Classic avatars ≈ **5 studs** tall; humanoid-proportion avatars ≈ **6–6.5 studs** | [RBX] studio/avatar-settings |
| Default jump height: 5 studs; the environment-art sample keeps doorways/halls ≥ 10 studs wide and walls ≥ 10 studs tall | [RBX] tutorials/curriculums/environmental-art/greybox-your-environment |

## Mesh specifications (general, non-avatar)
| Spec | Source |
|---|---|
| ≤ **20,000 triangles** per mesh | [RBX] art/modeling/specifications |
| **Watertight** (no holes or exposed backfaces); must have **volume** (no zero thickness) | [RBX] same |
| **No n-gons**; quads where possible | [RBX] same |
| **One material per mesh**; a single UV set; UVs within 0–1; overlapping UVs allowed | [RBX] art/modeling/texture-specifications |
| Textures up to 4096×4096; guidance 256² for ~5×5 stud objects, 512² for ~10×10, 1024² for ~20×20 | [RBX] same |
| Normal maps: **OpenGL tangent-space** only | [RBX] same |
| Rigs: bones scale (1,1,1), rotation 0, root at 0,0,0, ≤ 4 influences per vertex, no root influences; a single animation track per FBX | [RBX] art/modeling/specifications |

## Export (Blender side)
| Setting | Value | Source |
|---|---|---|
| Format | FBX for rigs/animation; glTF needs no scaling workaround; OBJ is also supported | [RBX] art/blender, export-requirements |
| FBX Path Mode / Embed Textures | **Copy** + Embed on | [RBX] export-requirements |
| FBX Apply Scalings | **FBX Unit Scale** (recommended). Alternatives: Scale 0.01 on export, or Unit Scale 0.01 in the scene; the docs warn about side effects of the latter | [RBX] art/blender "Adjust scale (FBX)" |
| Forward / Up | **Z Forward / Y Up** (Blender→Studio section) | [RBX] art/blender |
| Add Leaf Bones | Off | [RBX] export-requirements |
| Bake Animation | Off unless exporting animation | [RBX] export-requirements |
| Python equivalents | `export_scene.fbx(apply_scale_options='FBX_SCALE_UNITS', axis_forward='Z', axis_up='Y', add_leaf_bones=False, bake_anim=False, path_mode='COPY', embed_textures=True)`; `export_scene.gltf(export_format='GLB', export_yup=True)` | [BPY] operator properties introspected in 5.2.3 |

## Import (Studio side)
| Setting | Value | Source |
|---|---|---|
| Insert Using Scene Position | On if positions were authored in Blender | [RBX] art/blender |
| World Forward / World Up | **Front / Top** | [RBX] art/blender |
| Scale Unit | **Stud** | [RBX] art/blender |
| Name suffixes | `_Att` → Attachment; `_OuterCage` → WrapTarget; `_InnerCage`+`_OuterCage` → WrapLayer | [RBX] parts/meshes |

## Engine-side properties to set after import
| Property | Guidance | Source |
|---|---|---|
| `CollisionFidelity` | Box / Hull / Default / PreciseConvexDecomposition / Tunable; precise is the most expensive | [RBX] parts/meshes; see [BL-17](BL-17-Collision-Fidelity.md) |
| `RenderFidelity` | Automatic: highest under 250 studs, medium 250–500, lowest beyond 500 | [RBX] parts/meshes |
| Instancing | Copies of one mesh asset with identical texture/SurfaceAppearance share draw calls. Import once, duplicate in Studio | [RBX] performance-optimization/improve |

## Version-sensitive Blender facts (verified in 5.2.3)
- Auto Smooth (mesh property) was removed in Blender 4.1. The 5.2 operators are `object.shade_smooth_by_angle` and `object.shade_auto_smooth`, which add a "Smooth by Angle" modifier. **[BPY]** Tutorials made before 4.1 that say "enable Auto Smooth in Object Data" are outdated.
- With the pip `bpy` module, `import bmesh` fails unless `bpy` is imported first ([FC-BL-02](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-BL-02-Bmesh-Import-Order.md)). **[BPY]**
- Headless EEVEE and Workbench need an EGL library; Cycles CPU works without it ([FC-BL-01](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-BL-01-Headless-EEVEE-Needs-EGL.md)). **[BPY]**

## Not verified here (do this in Studio)
- How Studio imports **material base colours without textures** from FBX/GLB. This session's exercise assets use flat Principled colours. Verify in the Importer preview, and expect to set `MeshPart.Color` or use a palette texture ([BL-08](BL-08-Materials-and-Color.md)).
- Final scale in Studio for the exported files. Round trips were checked only in Blender ([BL-15](BL-15-Export-Settings.md)).

## Sources
Accessed 2026-10-24. Roblox pages from the creator-docs repository (commit 4e795e6); Blender pages from the 5.2 LTS manual (the URLs use `latest`, which served 5.2 on that date).
- [Use Blender with Roblox](https://create.roblox.com/docs/art/blender)
- [Export requirements](https://create.roblox.com/docs/art/modeling/export-requirements)
- [Mesh specifications](https://create.roblox.com/docs/art/modeling/specifications)
- [Meshes (MeshPart, fidelity, name suffixes)](https://create.roblox.com/docs/parts/meshes)
- [bpy 5.2.3 on PyPI](https://pypi.org/project/bpy/) — operator and property names confirmed by introspection in this environment
