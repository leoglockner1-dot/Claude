---
title: "Roblox Studio and Luau — Training Index"
tags: [luau, studio, index, technical]
note_type: "index"
---

# Roblox Studio and Luau — Training Index

Practical procedures for building Roblox systems that are **correct, secure, testable and maintainable**. Every procedure uses the same template: purpose, preconditions, dependencies, approach, APIs, common mistakes, security, performance, test cases, acceptance criteria, official references.

## How this section is different from a snippet collection
- The core logic lives in **tested, strict-typed modules** in [`_tools/luau/src/`](../_tools/luau/src/). They have no engine dependencies, so they run in the standalone Luau CLI. [`run_tests.sh`](../_tools/luau/run_tests.sh) type-checks every file with `luau-analyze` and runs the suite.
- **Last verified run (2026-10-24):** Luau CLI built from `luau-lang/luau` commit `32c2808`. `luau-analyze`: 0 type errors. Tests: **54 passed, 0 failed** (module specs) + **6 passed, 0 failed** (`tests/tutorial_repros.luau`, reproductions of two official-tutorial defects, see [TUT-01](../16-Tutorials-and-Workflows/TUT-01-Upgrade-Button-Server-Purchase.md) and [TUT-13](../16-Tutorials-and-Workflows/TUT-13-Save-Player-Data-Safely.md)).
- Engine wiring stays thin and is shown in each note. It was **not executed**, because Roblox Studio is not available in this environment. Treat it as reviewed code that you still have to playtest in Studio.
- Facts about Roblox come from the Roblox Creator Docs source (`Roblox/creator-docs`, commit `4e795e6`, read 2026-10-24). Links point to create.roblox.com.

## Start here
1. [LU-00 — Working method: pure modules, thin wiring](LU-00-Working-Method.md)
2. [LU-01 — Luau essentials for game code](LU-01-Luau-Essentials.md)
3. [LU-02 — Project architecture and script locations](LU-02-Project-Architecture.md)
4. [LU-03 — Client–server responsibilities](LU-03-Client-Server-Responsibilities.md)

## Procedures
| # | Procedure | Code | Tested? |
|---|---|---|---|
| LU-04 | [Remote events, functions and unreliable remotes](LU-04-Remotes.md) | — | docs-based |
| LU-05 | [Server-side validation of client input](LU-05-Server-Validation.md) | `Validate.luau` | ✅ CLI |
| LU-06 | [Rate limiting with a token bucket](LU-06-Rate-Limiting.md) | `TokenBucket.luau` | ✅ CLI |
| LU-07 | [Server-authoritative currency and shop purchase](LU-07-Currency-and-Shop.md) | `Currency.luau`, `ShopServer.luau` | ✅ CLI + mocks |
| LU-08 | [Player data persistence](LU-08-Player-Data-Persistence.md) | `PlayerData.luau`, `Retry.luau` | ✅ CLI (store calls not run) |
| LU-09 | [Developer product receipts](LU-09-Developer-Product-Receipts.md) | `Receipts.luau` | ✅ CLI |
| LU-10 | [Inventory, stacking and crafting costs](LU-10-Inventory.md) | `Inventory.luau` | ✅ CLI |
| LU-11 | [Round-based game loop](LU-11-Round-Loop.md) | `RoundMachine.luau` | ✅ CLI |
| LU-12 | [Upgrade pricing and pacing](LU-12-Upgrade-Pricing.md) | `CostCurve.luau` | ✅ CLI |
| LU-13 | [Random rewards, odds disclosure and pity](LU-13-Random-Rewards.md) | `WeightedLoot.luau` | ✅ CLI |
| LU-14 | [UI implementation and scaling](LU-14-UI-Implementation.md) | — | docs-based |
| LU-15 | [Input handling (keyboard, gamepad, touch)](LU-15-Input-Handling.md) | — | docs-based |
| LU-16 | [TweenService, springs and UI motion](LU-16-Tweens-and-Springs.md) | `Feel.luau` | ✅ CLI (math only) |
| LU-17 | [Character and object animation](LU-17-Animation-Playback.md) | — | docs-based |
| LU-18 | [Sound system: groups, mixing, ducking](LU-18-Sound-System.md) | — | docs-based |
| LU-19 | [VFX system: emit, pool, budget](LU-19-VFX-System.md) | — | docs-based |
| LU-20 | [Signals, cleanup and memory leaks](LU-20-Signals-and-Cleanup.md) | `Signal.luau` | ✅ CLI |
| LU-21 | [Error handling](LU-21-Error-Handling.md) | `Retry.luau` | ✅ CLI |
| LU-22 | [Debugging workflow](LU-22-Debugging-Workflow.md) | — | method |
| LU-23 | [Performance profiling](LU-23-Performance-Profiling.md) | — | docs-based |
| LU-24 | [Mobile support](LU-24-Mobile-Support.md) | — | docs-based |
| LU-25 | [Testing strategy](LU-25-Testing-Strategy.md) | `tests/`, `mocks/` | ✅ CLI |
| LU-26 | [Asset import and organization in Studio](LU-26-Asset-Import-and-Organization.md) | — | docs-based |
| LU-27 | [HUD number formatting](LU-27-HUD-Number-Formatting.md) | `Feel.luau` | ✅ CLI (found a real bug) |

## Related
- Earlier technical references (kept from v1): [14-Technical-Reference](../14-Technical-Reference/Roblox-Platform-Facts.md)
- Failures found while building this section: [Failure Library](../15-Anti-Patterns-and-Failure-Cases/Failure-and-Correction-Index.md)
- Benchmarks that use this code: [Benchmark Index](../19-Benchmarks-and-Practical-Exams/Benchmark-Index.md)
