---
title: "LU-25 — Testing strategy"
tags: [luau, testing, qa]
note_type: "procedure"
evidence: "tested (CLI suite) + official docs"
code: "_tools/luau/tests/, _tools/luau/mocks/"
---

# LU-25 — Testing strategy

## Purpose
Know which kind of test proves what, and use the cheapest one that can actually fail for the bug you care about.

## Test layers
| Layer | Proves | Doesn't prove | Tool |
|---|---|---|---|
| Type check | No nil access or wrong types in the checked paths | Logic correctness | `luau-analyze` (strict), Studio Script Analysis |
| Unit (pure modules) | Rules: prices, validation, migrations, odds, state machine | Engine behaviour | Luau CLI + `TestKit` (this academy: 54 tests) |
| Integration with mocks | Modules work together through the documented contract (player arg first, client data arbitrary) | Replication, latency, real yields | `MockRoblox` + `ShopServer` tests |
| Studio playtest | Engine behaviour, UI, feel | Many players, real devices | Play / Play Here / Run |
| Multi-client simulation | Replication, per-player isolation, join/leave | Real network conditions | *Start* with several clients; Network simulator |
| Scripted Studio tests | Repeatable multi-client, device and input flows | Production scale | `StudioTestService` (up to 8 simulated clients), `StudioDeviceSimulatorService`, `VirtualInput` (Studio-only, per testing-modes docs) |
| Device test | Performance, touch ergonomics | — | Real phones |

## Procedure for a new system
1. Acceptance criteria → test names.
2. Pure module + unit tests (red → green).
3. Integration test with mocks for the remote/handler contract, including exploit payloads.
4. Studio playtest checklist (visual and feel checks).
5. Multi-client run for anything shared or saved.
6. Record results honestly: "CLI 54/54 pass; Studio not run" is a valid, useful result.

## Writing good tests
- Test behaviour that matters to players: "grants once", "never overspends", "refuses NaN".
- Make time and randomness injectable; use seeds.
- Include at least one **adversarial** case per remote.
- Keep tests fast (the whole suite here runs in about a second).

## Real value demonstrated here
The suite found a real display bug (`9.86M`, [FC-LU-02](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-LU-02-Float-Truncation-HUD-Numbers.md)). The analyzer exposed a parse error that `require` had hidden ([FC-LU-01](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-LU-01-Luau-Type-Alias-Parse-Error-Silent-Require.md)).

## Acceptance criteria
Every system ships with unit tests for its rules, at least one adversarial integration test per remote, and a written Studio playtest checklist with results.

## References
- https://create.roblox.com/docs/studio/testing-modes · [`tests/run_all.luau`](../_tools/luau/tests/run_all.luau)
