---
title: "BM-07 — Modular kit that snaps on a 5-stud grid"
tags: [benchmark, blender,-level-art]
note_type: "benchmark"
level: "Advanced"
status: "executed"
---

# BM-07 — Modular kit that snaps on a 5-stud grid

| Field | Value |
|---|---|
| Area | Blender / level art |
| Level | Advanced |
| Time box | 3 h |
| Status | ✅ Executed by the academy |

## Task
Build a 4-piece wall kit (wall, doorway, corner, floor) whose pieces snap on a 5-stud grid with consistent pivots, proven with automated ray checks.

## Inputs
- [TUT-09](../16-Tutorials-and-Workflows/TUT-09-Polished-Assets-Trim-Sheets-Modular-Kits.md) pivot and divisibility rules.
- `ex_modular_kit.py` as reference.

## Deliverables
- Kit meshes plus an assembly render.
- Automated checks: pivot, grid lengths/heights, gap/overlap rays, opening found in the doorway.

## Acceptance criteria (pass/fail)
- [ ] All pieces watertight and on the grid for length and height.
- [ ] Doorway opening detected by ray, not by bounding box.
- [ ] No gaps at seams (rays offset from exact seams).

## Scoring rubric (0 / 1–2 / 3)
| Dimension | 0 | 1–2 | 3 |
|---|---|---|---|
| Snap correctness | Gaps/overlaps | Minor | None |
| Check validity | Checks unvalidated | Some probing | Each check probed for false results |
| Criteria honesty | Criteria changed silently | — | Any changed criterion explained |

## Common failure modes
- Bounding-box checks that call a doorway solid.
- Joined boxes that are non-manifold.
- Requiring every footprint edge on the grid (impossible for 1-stud walls).

## Self-critique before submitting
Run the [Self-Critique Loop](../18-Skill-Training/Self-Critique-Loop.md): state the criteria **before** looking at the result, inspect the output (not your intention), and log every failed version.

## Academy run and evidence
[BL-EX-09](../06-Blender-and-3D-Assets/Exercises/BL-EX-09-Modular-Building-Kit.md): v1 doorway made of joined boxes was non-manifold → rebuilt as a U-profile extrude (28 tris). Criterion K2 was mis-specified and revised openly. Two validator blind spots found (FC-QA-01).

## Related
- [BL-EX-09](../06-Blender-and-3D-Assets/Exercises/BL-EX-09-Modular-Building-Kit.md)
- [FC-QA-01](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-QA-01-Validator-Blind-Spots.md)
