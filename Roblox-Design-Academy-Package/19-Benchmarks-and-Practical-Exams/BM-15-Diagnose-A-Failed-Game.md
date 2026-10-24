---
title: "BM-15 — Diagnose a failed game from a developer's post-mortem"
tags: [benchmark, game-design]
note_type: "benchmark"
level: "Intermediate"
status: "executed"
---

# BM-15 — Diagnose a failed game from a developer's post-mortem

| Field | Value |
|---|---|
| Area | Game design |
| Level | Intermediate |
| Time box | 45 min |
| Status | ✅ Executed by the academy |

## Task
Read one developer self-report (FC-GD-01…06 sources). Map the symptoms to framework fields and propose the smallest test that would confirm the diagnosis.

## Inputs
- [Core Loop Failure Cases](../03-Core-Gameplay-Loops/Core-Loop-Failure-Cases.md)

## Deliverables
- Symptom → field → proposed test table.

## Acceptance criteria (pass/fail)
- [ ] Separates the developer's claims, the community diagnosis and your own hypothesis.
- [ ] The proposed test is cheap (≤ 1 day) and has a pass/fail threshold.

## Scoring rubric (0 / 1–2 / 3)
| Dimension | 0 | 1–2 | 3 |
|---|---|---|---|
| Evidence separation | Mixed | Partly | Clear |
| Test quality | Vague | Testable | Cheap with threshold |

## Common failure modes
- Treating community diagnosis as proven.

## Self-critique before submitting
Run the [Self-Critique Loop](../18-Skill-Training/Self-Critique-Loop.md): state the criteria **before** looking at the result, inspect the output (not your intention), and log every failed version.

## Academy run and evidence
The FC-GD notes in [Core Loop Failure Cases](../03-Core-Gameplay-Loops/Core-Loop-Failure-Cases.md) do this mapping; the tests they propose were **not** run.

## Related
- [Failure and Correction Index](../15-Anti-Patterns-and-Failure-Cases/Failure-and-Correction-Index.md)
