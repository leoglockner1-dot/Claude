---
title: "BM-02 — Debug a buggy Luau module against a spec"
tags: [benchmark, luau]
note_type: "benchmark"
level: "Intermediate"
status: "executed"
---

# BM-02 — Debug a buggy Luau module against a spec

| Field | Value |
|---|---|
| Area | Luau |
| Level | Intermediate |
| Time box | 45 min |
| Status | ✅ Executed by the academy |

## Task
`_tools/luau/benchmarks/DailyReward_buggy.luau` has planted defects. Using `benchmarks/bm02_spec.luau`, find every defect, fix a copy, and write one sentence per defect explaining the cause.

## Inputs
- `DailyReward_buggy.luau` (rules in its header comment).
- `bm02_spec.luau` (one test per defect plus controls).
- Luau CLI (`luau`, `luau-analyze`).

## Deliverables
- A fixed module that passes every test.
- A defect list: test name → cause → fix.

## Acceptance criteria (pass/fail)
- [ ] `luau-analyze` reports 0 errors on the fix.
- [ ] All 9 tests pass on the fixed module.
- [ ] The fix does not mutate the input state.
- [ ] Each defect explanation names the root cause, not the symptom (e.g. "NaN fails every comparison, so `now - last < COOLDOWN` is false and the claim is allowed").

## Scoring rubric (0 / 1–2 / 3)
| Dimension | 0 | 1–2 | 3 |
|---|---|---|---|
| Coverage | < 4 defects fixed | 4–5 | All 5 (6 failing tests) |
| Root cause | Symptoms only | Some causes | Every cause stated |
| Regression safety | Controls break | Controls pass | Controls pass and an extra test added |

## Common failure modes
- Patching the test instead of the module.
- Fixing the cap by clamping the streak (it should keep counting; only the reward is capped).
- Missing infinity while fixing NaN.

## Self-critique before submitting
Run the [Self-Critique Loop](../18-Skill-Training/Self-Critique-Loop.md): state the criteria **before** looking at the result, inspect the output (not your intention), and log every failed version.

## Academy run and evidence
Run on 2026-10-24: buggy module fails exactly the 6 defect tests (D1a NaN, D1b infinity, D2 window boundary `>` vs `>=`, D3 reward uses the old streak, D4 no cap, D5 mutates input) and passes the 3 controls; the fixed module passes 9/9 ([run log](../Assets/Original/Luau/test-runs-2026-10-24.txt)). **Self-critique:** v1 of the spec reused one state across sub-cases, so the mutation defect masked the boundary defect (the boundary test failed for the wrong reason); I also listed "clock earlier than last claim" as a defect, but the cooldown check already refuses it. Spec v2 isolates each test and keeps that case as a control.

## Related
- [LU-05 Server Validation](../07-Roblox-Studio-and-Luau/LU-05-Server-Validation.md)
- [LU-22 Debugging Workflow](../07-Roblox-Studio-and-Luau/LU-22-Debugging-Workflow.md)
- [LU-25 Testing Strategy](../07-Roblox-Studio-and-Luau/LU-25-Testing-Strategy.md)
