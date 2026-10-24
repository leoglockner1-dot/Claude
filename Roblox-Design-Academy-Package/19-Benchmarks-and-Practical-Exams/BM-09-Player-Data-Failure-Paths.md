---
title: "BM-09 — Player data that survives failure paths"
tags: [benchmark, luau,-data]
note_type: "benchmark"
level: "Advanced"
status: "executed"
---

# BM-09 — Player data that survives failure paths

| Field | Value |
|---|---|
| Area | Luau / data |
| Level | Advanced |
| Time box | 2 h |
| Status | ✅ Executed by the academy |

## Task
Write load/save logic that never overwrites real data after a failed load, retries with backoff, saves on leave and shutdown, and is tested with injected DataStore failures.

## Inputs
- `src/PlayerData`, `src/Retry` (reference).
- The TUT-13 repro as a known-bad example.

## Deliverables
- Module plus tests with injected read/write failures.

## Acceptance criteria (pass/fail)
- [ ] Failed load → no write, ever (test).
- [ ] Transient failure → retried, then succeeds (test).
- [ ] Shutdown path saves dirty sessions (test or documented Studio check).

## Scoring rubric (0 / 1–2 / 3)
| Dimension | 0 | 1–2 | 3 |
|---|---|---|---|
| Failure safety | Saves defaults over data | Blocks save only | Blocks save and earning, tells the player |
| Retries | None | Fixed delay | Backoff with cap |
| Evidence | Untested | Happy path | Injected failures |

## Common failure modes
- The TUT-13 pattern (earning after a failed load creates a value that autosave writes).

## Self-critique before submitting
Run the [Self-Critique Loop](../18-Skill-Training/Self-Critique-Loop.md): state the criteria **before** looking at the result, inspect the output (not your intention), and log every failed version.

## Academy run and evidence
`PlayerData` and `Retry` specs (in the 54 passing) plus the GoldManager repro (500 → 10 with the tutorial logic, 500 kept with the fix). Studio shutdown behaviour **not** verified.

## Related
- [LU-08 Player Data Persistence](../07-Roblox-Studio-and-Luau/LU-08-Player-Data-Persistence.md)
- [TUT-13](../16-Tutorials-and-Workflows/TUT-13-Save-Player-Data-Safely.md)
