---
title: "LU-27 — HUD number formatting"
tags: [luau, ui, hud, formatting]
note_type: "procedure"
evidence: "tested (CLI); found and fixed a real bug"
code: "_tools/luau/src/Feel.luau"
---

# LU-27 — HUD number formatting

## Purpose
Numbers players read at a glance: stable width, never lying, consistent across the game.

## Functions (tested)
| Function | Example | Use |
|---|---|---|
| `Feel.abbreviate(n)` | 1234 → `1.23K`, 9,870,000 → `9.87M`, 12,345,678 → `12.3M`, 999,999 → `999K` | Currency counters, damage numbers |
| `Feel.commas(n)` | 1234567 → `1,234,567` | Prices where the exact value matters |
| `Feel.clock(s)` | 75 → `1:15` | Round timers |

## Rules
- **Three significant digits** keep the width stable as numbers grow.
- **Truncate, never round up.** Showing `1.00M` for 999,999 tells players they can afford something they cannot.
- **Add an epsilon before truncating.** 9,870,000 / 1e6 is 9.869999… in binary floating point, and plain `floor` gives `9.86M`. The test suite caught exactly this bug ([FC-LU-02](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-LU-02-Float-Truncation-HUD-Numbers.md)).
- Use the same formatter everywhere, so the shop price and the wallet agree.
- Display formatting is client-side; the server keeps exact integers.

## Acceptance criteria
All formatting goes through one module; tests include float-boundary values (9.87M, 999,999, negatives).
