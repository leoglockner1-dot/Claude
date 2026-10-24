---
title: "BM-11 — Weighted loot with honest odds disclosure"
tags: [benchmark, luau,-economy-ethics]
note_type: "benchmark"
level: "Intermediate"
status: "executed"
---

# BM-11 — Weighted loot with honest odds disclosure

| Field | Value |
|---|---|
| Area | Luau / economy ethics |
| Level | Intermediate |
| Time box | 45 min |
| Status | ✅ Executed by the academy |

## Task
Implement weighted random rewards with pity, and compute the *effective* odds a player should be shown (including pity), verified by simulation.

## Inputs
- `src/WeightedLoot` (reference, incl. `effectiveOdds`).

## Deliverables
- Module, displayed-odds table, simulation result.

## Acceptance criteria (pass/fail)
- [ ] Displayed odds match a 100k-roll simulation within ±0.5 percentage points.
- [ ] Pity is included in the displayed odds.
- [ ] Weights of 0 and negative weights are rejected.

## Scoring rubric (0 / 1–2 / 3)
| Dimension | 0 | 1–2 | 3 |
|---|---|---|---|
| Correctness | Wrong odds | Base odds only | Effective odds incl. pity |
| Verification | None | Small sample | Large simulation with tolerance |
| Ethics | Hidden odds | Odds shown | Odds shown in the shop flow |

## Common failure modes
- Showing base weights while pity changes the real rates.

## Self-critique before submitting
Run the [Self-Critique Loop](../18-Skill-Training/Self-Critique-Loop.md): state the criteria **before** looking at the result, inspect the output (not your intention), and log every failed version.

## Academy run and evidence
`WeightedLoot` specs in `run_all.luau` (part of 54 passing).

## Related
- [LU-13 Random Rewards](../07-Roblox-Studio-and-Luau/LU-13-Random-Rewards.md)
- [CL-08 Shop and Monetization Ethics](../23-Quality-Checklists/CL-08-Shop-and-Monetization-Ethics.md)
