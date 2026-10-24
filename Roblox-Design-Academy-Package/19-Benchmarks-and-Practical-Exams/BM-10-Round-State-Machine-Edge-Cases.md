---
title: "BM-10 — Round state machine edge cases"
tags: [benchmark, luau,-multiplayer]
note_type: "benchmark"
level: "Intermediate"
status: "executed"
---

# BM-10 — Round state machine edge cases

| Field | Value |
|---|---|
| Area | Luau / multiplayer |
| Level | Intermediate |
| Time box | 60 min |
| Status | ✅ Executed by the academy |

## Task
Implement Intermission → Active → Results with explicit transitions and test: everyone leaves mid-round, a player joins mid-round, a timer expires during Results.

## Inputs
- `src/RoundMachine` (reference).

## Deliverables
- Module plus tests for each edge case.

## Acceptance criteria (pass/fail)
- [ ] No transition from an invalid state is possible.
- [ ] Edge cases each have a test.
- [ ] Each transition fires its signal exactly once.

## Scoring rubric (0 / 1–2 / 3)
| Dimension | 0 | 1–2 | 3 |
|---|---|---|---|
| States explicit | Implicit loop | Enum but unchecked | Transition table enforced |
| Edge cases | None | Some | All listed |
| Observability | No events | Some | Every transition signalled |

## Common failure modes
- `while true do wait()` loops with hidden state.
- No handling for an empty server.

## Self-critique before submitting
Run the [Self-Critique Loop](../18-Skill-Training/Self-Critique-Loop.md): state the criteria **before** looking at the result, inspect the output (not your intention), and log every failed version.

## Academy run and evidence
`RoundMachine` specs in `run_all.luau` (part of 54 passing).

## Related
- [LU-11 Round Loop](../07-Roblox-Studio-and-Luau/LU-11-Round-Loop.md)
- [TUT-04](../16-Tutorials-and-Workflows/TUT-04-Round-Loop-and-Team-Points.md)
