---
title: "TUT-09 — Develop polished assets: art style, textures, trim sheets, modular kits, props"
tags: [tutorial, environment-art, trim-sheets, modular-kit, blender]
note_type: "tutorial-procedure"
source: "https://create.roblox.com/docs/tutorials/curriculums/environmental-art/develop-polished-assets"
source_author: "Roblox Creator Documentation"
licence: "Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution."
accessed: "2026-10-24"
evidence: "[SRC] = what the tutorial says; [ANALYSIS] = our reading; [SIM-TESTED] = reproduced in a Luau simulation; [HYP] = untested"
---

# TUT-09 — Develop polished assets: art style, textures, trim sheets, modular kits, props

**Skill:** Plan the asset set that replaces a greybox: style board, tileable textures, trim sheets, a modular kit with consistent pivots, and props.

## Source and access
- Source: [https://create.roblox.com/docs/tutorials/curriculums/environmental-art/develop-polished-assets](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/develop-polished-assets) · [https://create.roblox.com/docs/tutorials/use-case-tutorials/modeling/assemble-modular-environments](https://create.roblox.com/docs/tutorials/use-case-tutorials/modeling/assemble-modular-environments)
- Author: Roblox (official documentation). Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution.
- Access: Read the Markdown source of the page from the public Roblox/creator-docs repository (commit 4e795e6), accessed 2026-10-24. Images, videos and the linked sample places (.rbxl) were **not** opened, and no step was performed in Roblox Studio.

## Workflow in the tutorial [SRC]
1. Choose an art style with a mood board as the source of truth.
2. Tileable textures tile on X **and** Y, must have no seam and no standout element (a distinctive patch reveals repetition); up to 1024×1024, with cost rising near the maximum.
3. Trim sheets tile on X **or** Y; each row is a reusable surface treatment; avoid object-specific details; square dimensions.
4. Modular kit pieces share a **consistent pivot** (e.g. forward-most lower corner) and sizes that divide by the smallest piece (5×5 → 15×5) so they snap at 5-stud increments; larger pieces can be split into named child meshes (UpperTrim, LowerTrim, Wall).
5. Props need logical pivots for placement (e.g. back of a fire extinguisher for wall mounting) and only enough geometry to read by silhouette.
6. Assemble-modular-environments page: move one mesh at a time, because selecting several averages their pivots.

## Decisions and the reasons the tutorial gives [SRC]
| Decision | Reason |
|---|---|
| Trim sheets over unique textures. | More visual variety from one texture set, saving memory. |
| Consistent pivots. | Pieces snap together at predictable offsets; inconsistent pivots cause clashing geometry. |
| Silhouette-level prop detail. | Players see props from many angles; extra geometry costs performance. |

## Our analysis
- **[OBS — our exercise]** In our [modular kit exercise](../06-Blender-and-3D-Assets/Exercises/BL-EX-09-Modular-Building-Kit.md) the kit criterion K2 had to be revised openly; the pivot rule from this tutorial is what the kit QC checks (`rbx_qc.check_object(pivot=...)`).
- **[ANALYSIS]** "Move one mesh at a time" is easy to miss and causes misalignment that looks like a modelling error.

## Common mistakes
- A standout element in a tileable texture.
- Pivots in the centre for modular pieces.
- Sizes that don't divide by the smallest module.
- Trim sheet rows with object-specific details.

## Troubleshooting
| Symptom | Likely cause / fix |
|---|---|
| Pieces overlap or leave gaps | Check pivot location and size divisibility. |
| Texture repetition obvious | Remove the standout element; use organic tiling or decal overlays. |

## Reusable procedure (ours)
1. Mood board → 5 style rules.
2. List surfaces: tileable (large areas) vs trim (edges, panels).
3. Define the module (e.g. 5 studs) and pivot convention before modelling.
4. Model kit pieces; QC pivot, size divisibility, tri budget.
5. Model props to silhouette; set logical pivots.

## Exercise
Run `_tools/blender/ex_modular_kit.py` and extend the kit with a corner piece that follows the same pivot convention.

### Acceptance criteria
- [ ] New piece passes `rbx_qc.check_object` with the kit's pivot rule.
- [ ] It snaps to existing pieces at 5-stud steps in a contact-sheet render with no gaps or overlaps.

## Related
- [BL-09 UV Mapping and Texture Budgets](../06-Blender-and-3D-Assets/BL-09-UV-Mapping-and-Texture-Budgets.md)
- [BL-14 Import Scale and Pivots](../06-Blender-and-3D-Assets/BL-14-Roblox-Import-Scale-and-Pivots.md)
- [BL-12 Asset Organization](../06-Blender-and-3D-Assets/BL-12-Asset-Organization-and-Naming.md)
