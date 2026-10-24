---
title: "LU-05 — Server-side validation of client input"
tags: [luau, security, validation, remotes]
note_type: "procedure"
evidence: "tested (CLI) + official docs"
code: "_tools/luau/src/Validate.luau"
---

# LU-05 — Server-side validation of client input

## Purpose
Reject malformed, oversized or impossible requests before they touch game state.

## Preconditions
A remote (or `Touched`/`ProximityPrompt` handler) that changes state, grants rewards or affects other players.

## Dependencies
[`Validate.luau`](../_tools/luau/src/Validate.luau). No engine dependencies.

## Approach: four layers, in this order
1. **Rate limit**, cheapest first: [LU-06](LU-06-Rate-Limiting.md).
2. **Type and structure:** exact table shape, bounded strings and arrays, no metatables, no extra keys. In Roblox, instance arguments also need `typeof(x) == "Instance"`, `x:IsA("…")` and `x:IsDescendantOf(expectedFolder)`. The docs' example shows an exploiter sending a *table that imitates an Instance* with `Price = 0`.
3. **Values:** finite, integer where expected, within range, an id that exists in the **server's** catalog.
4. **Context/permission:** close enough, owns the key, character alive, not on cooldown, round in the right state.

```lua
local Validate = require(script.Parent.Validate)
local schema = {
    itemId = Validate.Str({ maxLen = 32, pattern = "^[%w_]+$" }),
    qty    = Validate.Number({ min = 1, max = 10, integer = true }),
}
local ok, err = Validate.shape(payload, schema)   -- rejects extra keys such as `price`
if not ok then return false, "bad request: " .. err end
```

## The NaN trap (verified)
`NaN` has type `"number"` but fails every comparison. A naive check like `if offered < 0 or offered > max then reject end` **accepts** NaN. The test suite asserts exactly this (`documents why: NaN passes naive range checks`). Then NaN poisons balances and trades. Roblox docs recommend `math.isfinite(x)`. `Validate.number` uses `v ~= v or v == ±math.huge`, which also works in the standalone CLI.

## Common mistakes
- Checking only `type(x) == "number"`.
- Letting `Validate.shape` pass tables with extra keys. This module rejects them on purpose.
- Validating on the client only. Client validation is for UX; server validation is for security.
- Doing expensive work (string operations, searches) *before* the size checks.

## Security notes
- Unbounded strings and arrays are a server-cost attack. `Validate.str` caps at 200 bytes by default, and `array` requires a `maxLen`.
- Never `require`, load assets or index the DataModel by a path the client sent.

## Performance
Validation is O(payload size), and the caps bound that size. It is negligible next to the work it protects.

## Test cases (all in `tests/run_all.luau`, passing)
- NaN, `+inf`, `-inf` rejected; integer/range enforced.
- 201-byte string rejected; invalid UTF-8 (`"\255\254"`) rejected; pattern mismatch rejected.
- Shape rejects an extra key `price = 0`, a metatable, NaN inside the shape, and a string instead of a table.
- Array rejects holes, non-index keys and oversize.

## Acceptance criteria
- Each remote handler validates every argument with an explicit schema before using it.
- Fuzzing a handler with random types (nil, string, table, NaN, huge numbers) never errors and never changes state.

## References
- https://create.roblox.com/docs/scripting/security/client-server-boundary (Validating remote inputs, The danger of NaN)
