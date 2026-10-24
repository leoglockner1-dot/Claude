---
title: "BM-06 — Fix a tool whose silhouette misreads"
tags: [benchmark, blender]
note_type: "benchmark"
level: "Intermediate"
status: "executed"
---

# BM-06 — Fix a tool whose silhouette misreads

| Field | Value |
|---|---|
| Area | Blender |
| Level | Intermediate |
| Time box | 45 min |
| Status | ✅ Executed by the academy |

## Task
A pickaxe reads as an umbrella at gameplay distance. Diagnose *why* (which shape feature causes it) before changing anything, then fix it in at most two revisions.

## Inputs
- The v1 contact sheet from BL-EX-05.

## Deliverables
- A written diagnosis before the fix.
- Before/after silhouettes.

## Acceptance criteria (pass/fail)
- [ ] The diagnosis names a shape feature (profile, not size).
- [ ] The final version reads as a pick in silhouette.
- [ ] ≤ 400 tris.

## Scoring rubric (0 / 1–2 / 3)
| Dimension | 0 | 1–2 | 3 |
|---|---|---|---|
| Diagnosis | "Make it thicker" | Partly right | Names the profile cause |
| Result | Still misreads | Reads with hint | Reads blind |
| Economy | > 2 revisions | 2 | 1 |

## Common failure modes
- Treating a shape problem as a size problem (what our v2 did).

## Self-critique before submitting
Run the [Self-Critique Loop](../18-Skill-Training/Self-Critique-Loop.md): state the criteria **before** looking at the result, inspect the output (not your intention), and log every failed version.

## Academy run and evidence
[BL-EX-05](../06-Blender-and-3D-Assets/Exercises/BL-EX-05-Pickaxe-Tool.md): v2 thickened the head and **failed**; v3 changed the crescent profile to a constant-thickness bar with the handle visible through the eye and passed (320 tris). The academy run took 2 revisions, so it scores 2 on economy.

## Related
- [BL-EX-05](../06-Blender-and-3D-Assets/Exercises/BL-EX-05-Pickaxe-Tool.md)
- [BL-02 Shape Language](../06-Blender-and-3D-Assets/BL-02-Shape-Language-Silhouette-Proportion.md)
