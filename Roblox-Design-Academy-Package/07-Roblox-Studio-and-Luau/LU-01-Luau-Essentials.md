---
title: "LU-01 — Luau essentials for game code"
tags: [luau, fundamentals]
note_type: "procedure"
evidence: "official docs + CLI checks"
---

# LU-01 — Luau essentials for game code

Not a language tutorial. These are the Luau facts that most often decide whether game code is correct.

| Topic | What to know | Why it matters in games |
|---|---|---|
| `--!strict` | Enables full type checking for the file. Run `luau-analyze`, or watch Script Analysis in Studio. | Catches nil access and wrong argument types before a playtest. In this session it caught real problems; see [FC-LU-01](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-LU-01-Luau-Type-Alias-Parse-Error-Silent-Require.md). |
| Optional option tables | `local o: Opts = opts or {}`, then read `o.field` into locals before comparing. | Under strict mode, `opts or {}` without an annotation has type `{} \| Opts`, and field access fails to type-check. |
| Numbers | All numbers are doubles. Integers are exact up to 2^53. `0/0` is NaN and `1/0` is `math.huge`. | Prices past 2^53 lose precision; `CostCurve` clamps. NaN fails every comparison, so `NaN < 0` and `NaN > max` are both false. Range checks alone let it through. See [LU-05](LU-05-Server-Validation.md). |
| Float display | `9870000 / 1e6` is `9.869999…` | Truncating for display gives "9.86M" instead of "9.87M". Add a small epsilon; see [LU-27](LU-27-HUD-Number-Formatting.md). |
| Integer division and compound ops | `//`, `+=`, `-=`, `..=` | Readable counters and grid math. |
| Generalized iteration | `for k, v in t do` works on tables without `pairs`/`ipairs`. | Concise. For arrays it visits 1..n in order. |
| `table.clone` / `table.freeze` | Shallow copy / read-only table. | Clone saves before migrating them. Freeze config so a bug cannot mutate shared constants. |
| `table.create(n, v)`, `table.find(t, v)` | Preallocate / linear search. | Use `find` on short lists only; a large set wants a map `{[id]=true}`. |
| Strings | `#s` counts bytes; `utf8.len(s)` returns nil for invalid UTF-8. | Validate client strings by byte length (cost) *and* UTF-8 validity. |
| `pcall` / `error` | `pcall(fn)` returns `false, err` instead of throwing. | Every yielding web call (DataStore, MessagingService, HttpService) goes inside `pcall`. See [LU-21](LU-21-Error-Handling.md). |
| `if … then … else` expressions | `local s = if n > 0 then "+" else ""` | Avoids the `a and b or c` bug when `b` can be false/nil. |
| Roblox-only globals | `game`, `workspace`, `Instance`, `Vector3`, `CFrame`, `task`, `typeof`, `Random`, `time`, `tick` | They do **not** exist in the standalone CLI. Keep pure modules free of them, or inject them. |

## Common mistakes
- `local x = cond and false or y` always gives `y`. Use an `if` expression.
- Using `#t` on dictionaries. It is only meaningful for arrays without holes.
- Comparing floats with `==` after arithmetic. Use a tolerance or integers (store currency as integers).
- Writing `type Result = (boolean, string?)`. A bare tuple is not a valid type alias, and the result is a parse error. Return `(boolean, string?)` directly.

## Exercise
Write `safeAdd(a: unknown, b: unknown): number?` that returns nil for non-numbers, NaN or infinities, and for a result above 2^53. Test it with `0/0`, `math.huge`, `"5"`, `2^53` and `1`.

**Acceptance:** `luau-analyze` is clean; all five cases behave as specified.

## References
- https://create.roblox.com/docs/luau/numbers · https://create.roblox.com/docs/luau/type-checking · https://create.roblox.com/docs/luau/tables · https://luau.org
