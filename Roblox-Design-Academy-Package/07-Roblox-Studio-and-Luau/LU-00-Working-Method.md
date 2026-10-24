---
title: "LU-00 — Working method: pure modules, thin wiring"
tags: [luau, method, testing, architecture]
note_type: "procedure"
evidence: "tested (CLI) + official docs"
---

# LU-00 — Working method: pure modules, thin wiring

## Purpose
To make Roblox code that an agent can **verify without Studio** and that stays maintainable once the game grows.

## The rule
Split every system into two parts:
1. **Pure logic module.** Rules, numbers and state transitions. It takes plain values and returns plain values. It never calls `game:GetService`, never touches an `Instance` and never yields. If it needs time, randomness or saving, those come in as **injected functions** (`now`, `rng`, `save`).
2. **Thin wiring script.** Connects the module to the engine: remotes, Players events, DataStores, UI. It should be short enough to review by eye.

Example: `ShopServer.luau` receives `deps.setInvokeHandler`, `deps.characterPosition` and `deps.save`. In Roblox those wrap a `RemoteFunction`, the character's root part and a DataStore. In tests, [`mocks/MockRoblox.luau`](../_tools/luau/mocks/MockRoblox.luau) supplies fakes.

## Why it works
- Most game bugs that damage players are **logic bugs**: double grants, NaN bypasses, lost saves, wrong prices. Logic bugs are exactly what CLI tests catch.
- Engine behaviour (replication, physics, rendering) needs a Studio playtest anyway. Keeping it in the wiring keeps that surface small.
- Injected time and randomness make tests deterministic. A token bucket test controls the clock, and a loot test uses a seeded generator.

## Procedure
1. Write acceptance criteria as test names before writing code, for example "grants once even if Roblox calls again".
2. Write the module with `--!strict` at the top.
3. Run `luau-analyze` and fix every type error before running anything. See [FC-LU-01](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-LU-01-Luau-Type-Alias-Parse-Error-Silent-Require.md): a module that does not parse can make `require` return the error string instead of raising.
4. Run the tests: `bash _tools/luau/run_tests.sh <path-to-luau-bin>`.
5. Write the wiring. Review it against the security checklist in [LU-05](LU-05-Server-Validation.md).
6. Playtest in Studio. Use *Start* with several clients for anything multiplayer. See [LU-25](LU-25-Testing-Strategy.md).

## When not to use it
- One-off visual scripts (a door that tweens open). Writing them directly is fine, as long as they hold no rules worth testing.
- Do not invent abstractions "for testability" around code that has no logic. Keep it simple.

## Getting the Luau CLI
- Releases: https://github.com/luau-lang/luau/releases. Or build from source: `cmake -S . -B build -DCMAKE_BUILD_TYPE=RelWithDebInfo && cmake --build build --target Luau.Repl.CLI Luau.Analyze.CLI`. That build path was used here, because the GitHub releases page returned HTTP 403 from this environment.
- The standalone CLI has no Roblox globals (`game`, `Instance`, `Vector3`, `task`, `Random`, `time`, `typeof`). The modules here avoid them on purpose.

## Acceptance criteria
- `luau-analyze` reports 0 errors on every module.
- Every rule a player could exploit or lose progress to has a named test.
- The wiring script contains no rule logic beyond calling module functions.

## References
- Script locations and the "modules with `start()`" pattern: https://create.roblox.com/docs/scripting/locations
- Luau type checking: https://create.roblox.com/docs/luau/type-checking
