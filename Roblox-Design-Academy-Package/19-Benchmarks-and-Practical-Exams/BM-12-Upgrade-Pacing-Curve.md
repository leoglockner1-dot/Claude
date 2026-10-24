---
title: "BM-12 — Upgrade pacing curve to a target"
tags: [benchmark, economy]
note_type: "benchmark"
level: "Intermediate"
status: "partial"
---

# BM-12 — Upgrade pacing curve to a target

| Field | Value |
|---|---|
| Area | Economy |
| Level | Intermediate |
| Time box | 60 min |
| Status | ◐ Partly executed |

## Task
Choose cost-curve parameters so the next purchase takes ≤ 45 s in the first 10 minutes and 2–4 minutes after 30 minutes, for a given income model; show the table.

## Inputs
- `src/CostCurve` (reference).
- An income model (state yours).

## Deliverables
- Parameter choice, a time-to-next-purchase table at 1/5/10/30/60 min, overflow behaviour.

## Acceptance criteria (pass/fail)
- [ ] Targets met in the table.
- [ ] Large values clamp instead of losing precision.
- [ ] The assumptions are stated, with [HYP] where untested.

## Scoring rubric (0 / 1–2 / 3)
| Dimension | 0 | 1–2 | 3 |
|---|---|---|---|
| Targets | Missed | Partly | Met |
| Robustness | Overflows | — | Clamps and reports |
| Honesty | Presented as fact | — | Labelled as a model |

## Common failure modes
- Pure exponential curves that wall players at 20 minutes.

## Self-critique before submitting
Run the [Self-Critique Loop](../18-Skill-Training/Self-Critique-Loop.md): state the criteria **before** looking at the result, inspect the output (not your intention), and log every failed version.

## Academy run and evidence
`CostCurve` behaviour is tested (in the 54 passing, incl. clamping at 2^53). A full pacing table against an income model is **not** yet worked out in the package; [LU-12](../07-Roblox-Studio-and-Luau/LU-12-Upgrade-Pricing.md) gives the method.

## Related
- [LU-12 Upgrade Pricing](../07-Roblox-Studio-and-Luau/LU-12-Upgrade-Pricing.md)
- [Progression Systems](../05-Progression-and-Economy/Progression-Systems.md)
