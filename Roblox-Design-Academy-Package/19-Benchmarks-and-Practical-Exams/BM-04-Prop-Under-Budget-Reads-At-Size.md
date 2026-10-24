---
title: "BM-04 — Model a collectible that reads at 32–64 px under budget"
tags: [benchmark, blender]
note_type: "benchmark"
level: "Beginner"
status: "executed"
---

# BM-04 — Model a collectible that reads at 32–64 px under budget

| Field | Value |
|---|---|
| Area | Blender |
| Level | Beginner |
| Time box | 60 min |
| Status | ✅ Executed by the academy |

## Task
Model a gem and a coin with centred pivots, ≤ 200 tris for the gem, that are recognisable at 32–64 px. Use `rbx_qc.check_object` and `render_at_size`.

## Inputs
- `_tools/blender/` toolkit.
- [BL-02 Shape Language](../06-Blender-and-3D-Assets/BL-02-Shape-Language-Silhouette-Proportion.md).

## Deliverables
- Renders at 256/64/32 px.
- QC JSON with 0 FAIL.
- FBX/GLB export and a round-trip dimension check.

## Acceptance criteria (pass/fail)
- [ ] Gem ≤ 200 tris; one material each.
- [ ] Both read at 32 px in a blind check (name the object from the 32 px image).
- [ ] Pivot at the centre (they spin).

## Scoring rubric (0 / 1–2 / 3)
| Dimension | 0 | 1–2 | 3 |
|---|---|---|---|
| Readability | Unreadable at 64 px | Reads at 64 | Reads at 32 |
| Budget | Over | At budget | Well under with no loss |
| Process | One version | Revised once | Revised with each defect named |

## Common failure modes
- Detail that disappears at small sizes (embossing).
- Pivot at the base for a spinning pickup.

## Self-critique before submitting
Run the [Self-Critique Loop](../18-Skill-Training/Self-Critique-Loop.md): state the criteria **before** looking at the result, inspect the output (not your intention), and log every failed version.

## Academy run and evidence
[BL-EX-02](../06-Blender-and-3D-Assets/Exercises/BL-EX-02-Collectible-Gem-and-Coin.md): the gem passed at 32 tris and read at 32 px; the coin's emboss was invisible at small sizes and needed revisions. A stale `matrix_world` put the pivot 1.5 studs off until fixed (FC-BL-06).

## Related
- [BL-EX-02](../06-Blender-and-3D-Assets/Exercises/BL-EX-02-Collectible-Gem-and-Coin.md)
- [BL-16 Performance Budgets](../06-Blender-and-3D-Assets/BL-16-Performance-Budgets.md)
