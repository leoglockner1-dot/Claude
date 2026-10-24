---
title: "LU-12 — Upgrade pricing and pacing"
tags: [luau, economy, progression, incremental]
note_type: "procedure"
evidence: "tested (CLI); pacing guidance is design interpretation"
code: "_tools/luau/src/CostCurve.luau"
---

# LU-12 — Upgrade pricing and pacing

## Purpose
Price upgrades so that each purchase takes a deliberate amount of play time, and so that buy-x10 and buy-max buttons agree with single purchases.

## Curves
| Curve | Formula (level 0 = first purchase) | Feel |
|---|---|---|
| Linear | `base + step·level` | Calm; works when rewards are not multiplicative |
| Exponential | `base·growth^level` | Classic incremental. 1.07–1.15 is typical (interpretation, not a platform rule) |
| Polynomial | `base·(level+1)^power` | Gentler late game than exponential |

## The metric that matters: seconds to afford
`secondsToAfford(curve, level, income)` = price ÷ income per second. Plot it for levels 0–100 with your *actual* income curve. Prices alone tell you nothing about pacing.
- If seconds-to-afford grows without limit, players hit a wall. Plan a prestige/rebirth or a new income source before that point.
- If it stays flat, upgrades stop feeling earned.

## Implementation notes
- `total(from, to)` sums single prices, so "buy x10" charges the same as ten single buys. Tested.
- `maxAffordable(level, money)` never overspends; the next level is provably unaffordable. Tested.
- Prices clamp at 2^53 and report `clamped = true` instead of silently losing precision. Tested.
- Validate on the server: a client asking for "buy max" sends the *intent*; the server computes the count.

## Common mistakes
- Closed-form geometric sums with float drift that disagree with per-level prices by 1. Summing is cheap at these sizes.
- Showing "1.00M" for 999,999 because of rounding up. See [LU-27](LU-27-HUD-Number-Formatting.md).

## Exercise
Income starts at 1 coin/s and each upgrade adds +1 coin/s. With `exponential(base=10, growth=1.15)`, find the first level where seconds-to-afford exceeds 60 s. Propose a change that keeps the first 10 minutes under 30 s per purchase.

**Acceptance:** the answer is computed with the module (show the code) and the change is justified by the seconds-to-afford numbers.
