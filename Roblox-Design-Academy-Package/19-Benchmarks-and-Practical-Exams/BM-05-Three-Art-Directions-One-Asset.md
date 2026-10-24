---
title: "BM-05 — One asset, three art directions (treasure chest)"
tags: [benchmark, blender,-visual-identity]
note_type: "benchmark"
level: "Intermediate"
status: "executed"
---

# BM-05 — One asset, three art directions (treasure chest)

| Field | Value |
|---|---|
| Area | Blender / visual identity |
| Level | Intermediate |
| Time box | 3 h |
| Status | ✅ Executed by the academy |

## Task
Model a treasure chest in three directions (e.g. premium, cartoon, rugged), each readable as a *treasure chest* in silhouette and passing QC.

## Inputs
- `_tools/blender/ex_treasure_chests.py` as the reference implementation (do the task before reading it).

## Deliverables
- A line-up render, gameplay-distance silhouettes and QC JSON for each version.
- A version log naming each defect and its fix.

## Acceptance criteria (pass/fail)
- [ ] Each passes all FAIL-level QC checks.
- [ ] In silhouette, each is identified as a chest (not a crate, sofa or slab).
- [ ] The three differ in shape language, not only colour.

## Scoring rubric (0 / 1–2 / 3)
| Dimension | 0 | 1–2 | 3 |
|---|---|---|---|
| Read | Any misread | Reads after a hint | Reads blind |
| Differentiation | Colour swaps | Proportion changes | Distinct shape language |
| Iteration honesty | Only final shown | Some history | Every failed version shown |

## Common failure modes
- The premium chest reads as a crate (no lid curve, no trim).
- Exact contact plus bevels leaves a hinge gap.

## Self-critique before submitting
Run the [Self-Critique Loop](../18-Skill-Training/Self-Critique-Loop.md): state the criteria **before** looking at the result, inspect the output (not your intention), and log every failed version.

## Academy run and evidence
[BL-EX-04](../06-Blender-and-3D-Assets/Exercises/BL-EX-04-Treasure-Chests.md): four versions. Defects: premium read as a crate; cartoon read as a sofa, then as a floating slab; n-gon coin caps; hinge gap. All fixed by v4.

## Related
- [BL-EX-04](../06-Blender-and-3D-Assets/Exercises/BL-EX-04-Treasure-Chests.md)
- [R14 Visual Identity System](../18-Skill-Training/Design-Recipes/R14-Coherent-Visual-Identity-System.md)
