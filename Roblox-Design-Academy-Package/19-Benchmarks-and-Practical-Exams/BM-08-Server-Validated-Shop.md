---
title: "BM-08 — Server-validated shop with rate limit"
tags: [benchmark, luau,-security]
note_type: "benchmark"
level: "Intermediate"
status: "executed"
---

# BM-08 — Server-validated shop with rate limit

| Field | Value |
|---|---|
| Area | Luau / security |
| Level | Intermediate |
| Time box | 90 min |
| Status | ✅ Executed by the academy |

## Task
Implement a purchase handler that validates input, rate-limits, reads prices server-side, deducts before any yield and returns a result; prove it with tests against hostile input.

## Inputs
- `src/Validate`, `src/TokenBucket`, `src/Currency` (or write your own).
- `mocks/MockRoblox.luau` for remotes and players.

## Deliverables
- Module plus tests: wrong types, NaN, negative quantity, unknown item, spam, insufficient funds.

## Acceptance criteria (pass/fail)
- [ ] All hostile-input tests refused without errors.
- [ ] Spam: only budgeted requests succeed.
- [ ] No path deducts twice or credits without deducting.

## Scoring rubric (0 / 1–2 / 3)
| Dimension | 0 | 1–2 | 3 |
|---|---|---|---|
| Validation | Types only | Types and ranges | Types, ranges, NaN/inf, unknown ids |
| Ordering | Yield before deduct | — | Deduct before any yield |
| Tests | Happy path | Some hostile | Every rule has a failing-input test |

## Common failure modes
- Trusting a client-sent price.
- Check-then-yield-then-deduct (see TUT-01 repro).

## Self-critique before submitting
Run the [Self-Critique Loop](../18-Skill-Training/Self-Critique-Loop.md): state the criteria **before** looking at the result, inspect the output (not your intention), and log every failed version.

## Academy run and evidence
`ShopServer` specs in `_tools/luau/tests/run_all.luau` (part of 54 passing). The TUT-01 race reproduction (`tests/tutorial_repros.luau`) shows the ordering defect and its fix.

## Related
- [LU-07 Currency and Shop](../07-Roblox-Studio-and-Luau/LU-07-Currency-and-Shop.md)
- [TUT-01](../16-Tutorials-and-Workflows/TUT-01-Upgrade-Button-Server-Purchase.md)
