---
title: "BM-16 — Convert a tutorial into a procedure and find its weak point"
tags: [benchmark, process,-luau]
note_type: "benchmark"
level: "Advanced"
status: "executed"
---

# BM-16 — Convert a tutorial into a procedure and find its weak point

| Field | Value |
|---|---|
| Area | Process / Luau |
| Level | Advanced |
| Time box | 90 min |
| Status | ✅ Executed by the academy |

## Task
Pick an official tutorial; write it up in the TUT template, separating [SRC] from your analysis; find at least one failure path the tutorial does not handle and demonstrate it (test or simulation).

## Inputs
- [Tutorial-Workflow Index](../16-Tutorials-and-Workflows/Tutorial-Workflow-Index.md) template.

## Deliverables
- TUT note plus a reproduction.

## Acceptance criteria (pass/fail)
- [ ] Source, licence and access recorded (what was and wasn't opened).
- [ ] Claims about engine behaviour are checked against the docs (see FC-RES-01).
- [ ] The reproduction fails with the tutorial logic and passes with the fix.

## Scoring rubric (0 / 1–2 / 3)
| Dimension | 0 | 1–2 | 3 |
|---|---|---|---|
| Separation | Mixed | Partly | Clean |
| Defect evidence | Asserted | Argued | Reproduced |
| Source checks | None | Some | Every engine claim checked |

## Common failure modes
- Claiming a guarantee the engine doesn't give (our own FC-RES-01).

## Self-critique before submitting
Run the [Self-Critique Loop](../18-Skill-Training/Self-Critique-Loop.md): state the criteria **before** looking at the result, inspect the output (not your intention), and log every failed version.

## Academy run and evidence
TUT-01 and TUT-13 with `tests/tutorial_repros.luau` (6/6 passing; simulation, not Studio).

## Related
- [TUT-01](../16-Tutorials-and-Workflows/TUT-01-Upgrade-Button-Server-Purchase.md)
- [TUT-13](../16-Tutorials-and-Workflows/TUT-13-Save-Player-Data-Safely.md)
- [FC-RES-01](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-RES-01-Assumed-Engine-Guarantee.md)
