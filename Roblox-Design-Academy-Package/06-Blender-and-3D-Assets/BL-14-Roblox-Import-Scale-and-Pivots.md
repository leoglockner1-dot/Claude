---
title: "BL-14 — Roblox import, scale and pivots"
tags: [blender, roblox, import, scale, pivot]
note_type: "procedure"
evidence: "Roblox docs + QC/round-trip results"
---

# BL-14 — Roblox import, scale and pivots

## Scale
- Model in studs (Unit System None). Keep a 5-stud classic avatar reference in the scene; 6–6.5 studs for humanoid-proportion games ([RBX] avatar-settings).
- Typical sizes used in the exercises: chest 2.7–3.0 studs wide; pickaxe ~3.7 studs long; tree ~5 studs tall; collectible gem 1 stud.
- Apply scale (Ctrl+A) so object scale = 1. `rbx_qc` warns otherwise.
- Export FBX with **FBX Unit Scale**, or use glTF (no scale workaround needed per Roblox docs). In Studio set **Scale Unit = Stud**.

## Pivots (origin) by role
| Role | Pivot | Why |
|---|---|---|
| Ground prop (chest, rock, tree) | bottom-centre of its footprint | Places flush on the ground; rotates in place |
| Assembly with a moving part | bottom-centre of the **base**, not of the bounding box | An open lid overhangs; bounding-box centring shifts the base (a real case in BL-EX-04: pivot offset 0.54 studs until measured on the body) |
| Hinged part | on the hinge line | Opening = a single rotation |
| Spinning/bobbing pickup | geometric centre | Spins around itself |
| Tool | the **grip** point | Roblox `Tool` grip offsets become simple |
| Modular kit piece | a consistent corner/edge on a 5-stud grid | The environmental-art curriculum snaps kit pieces in 5-stud increments |

## Round-trip check (what was verified)
`rbx_export.round_trip_dimensions` re-imports the FBX/GLB into an empty Blender scene and compares sizes. For the chests: FBX and GLB both re-imported at **2.67×1.705×1.815** (premium) etc., identical to the source assemblies. **This proves file integrity and Blender-side scale only.** Studio's Importer may still differ; check the Importer preview.

## Studio import steps (Roblox Blender guide)
Import > choose the file > *Insert Using Scene Position* as needed > World Forward **Front**, World Up **Top** > Scale Unit **Stud** > *Import Only as a Model* for multi-part assets.

## Acceptance criteria
QC pivot check passes (or the assembly pivot is reported); round trip matches; the Studio preview shows the right size next to an avatar.
