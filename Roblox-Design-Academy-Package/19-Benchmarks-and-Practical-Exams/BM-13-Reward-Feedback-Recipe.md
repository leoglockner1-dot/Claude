---
title: "BM-13 — Reward feedback that reads at small size"
tags: [benchmark, animation,-vfx]
note_type: "benchmark"
level: "Intermediate"
status: "executed"
---

# BM-13 — Reward feedback that reads at small size

| Field | Value |
|---|---|
| Area | Animation / VFX |
| Level | Intermediate |
| Time box | 60 min |
| Status | ✅ Executed by the academy |

## Task
Design a collect/reward feedback (motion + particles + sound) with stated timings; preview it and check it reads at small size and doesn't fatigue on repetition.

## Inputs
- [AV recipe template](../08-Animation-and-Game-Feel/Recipes/AV-Recipe-Index.md)
- `_tools/av/make_av_previews.py` for previews.

## Deliverables
- Recipe note with timings, a GIF preview, a WAV and its measurements.

## Acceptance criteria (pass/fail)
- [ ] Timings stated (anticipation/impact/settle).
- [ ] The preview reads at 25% size.
- [ ] Sound duration within the recipe's target.

## Scoring rubric (0 / 1–2 / 3)
| Dimension | 0 | 1–2 | 3 |
|---|---|---|---|
| Readability | Busy noise | Reads large | Reads small |
| Timing | Unstated | Stated | Stated and measured |
| Iteration | One try | Revised | Revised with the defect named |

## Common failure modes
- More particles instead of clearer ones.

## Self-critique before submitting
Run the [Self-Critique Loop](../18-Skill-Training/Self-Critique-Loop.md): state the criteria **before** looking at the result, inspect the output (not your intention), and log every failed version.

## Academy run and evidence
[AV-03 Collecting](../08-Animation-and-Game-Feel/Recipes/AV-03-Collecting.md): the coin burst v1 did not read and needed a v2. [Measured Audio Observations](../10-Sound-Design/Measured-Audio-Observations.md): heavy impact was corrected from 0.43 s to 0.35 s and victory from 0.9 s to 1.46 s. Previews are synthesized, not in-engine.

## Related
- [AV-03](../08-Animation-and-Game-Feel/Recipes/AV-03-Collecting.md)
- [AV-18 Repetition Fatigue](../08-Animation-and-Game-Feel/Recipes/AV-18-Repetition-Fatigue.md)
