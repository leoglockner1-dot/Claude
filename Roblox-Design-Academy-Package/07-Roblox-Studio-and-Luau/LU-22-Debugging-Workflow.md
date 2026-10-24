---
title: "LU-22 — Debugging workflow"
tags: [luau, debugging, method]
note_type: "procedure"
evidence: "method + official docs; examples from this session's real failures"
---

# LU-22 — Debugging workflow

## Purpose
Find the actual cause of a bug quickly and prove the fix. Do not stop at the first change that seems to help.

## The loop
1. **Reproduce** with the smallest steps. Write them down. If it is intermittent, find what varies: timing, player count, device, data.
2. **Observe, don't guess.** Read the full error and stack trace in Output. Breakpoints, Watch and the Call Stack (Studio debugger) show the actual values. The Developer Console (F9) shows client/server logs and memory in live servers.
3. **Locate the boundary:** which module first holds a wrong value? Bisect by logging inputs and outputs at module boundaries.
4. **Explain** the cause in one sentence before changing code ("`abbreviate` truncates 9.869999… because floats cannot represent 9.87").
5. **Write a failing test** for that cause (pure modules: CLI test; engine behaviour: a Studio reproduction checklist).
6. **Fix** the cause, not the symptom.
7. **Verify:** the new test passes, the old tests still pass, and the original reproduction no longer fails.
8. **Record** it in the [Failure Library](../15-Anti-Patterns-and-Failure-Cases/Failure-and-Correction-Index.md) if the lesson is reusable.

## Studio tools (studio/debugging, developer-console docs)
- Breakpoints (including conditional breakpoints and logpoints), step in/over/out, Watch, Call Stack.
- Command Bar for quick inspection during play.
- Developer Console sections: Log, Memory, Network, **Script Profiler**.
- Log files are kept on disk for later inspection.

## Real examples from building this academy
| Symptom | Wrong first guess | Actual cause | Fix |
|---|---|---|---|
| `attempt to call a nil value` in `ShopServer` at `Validate.Str` | `require` path wrong | `Validate.luau` failed to **parse** (a bare tuple type alias); `require` returned the error *string*, so every field was nil | Removed the alias; run `luau-analyze` before tests ([FC-LU-01](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-LU-01-Luau-Type-Alias-Parse-Error-Silent-Require.md)) |
| HUD showed "9.86M" for 9,870,000 | formatting pattern wrong | float truncation | epsilon before `floor` ([FC-LU-02](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-LU-02-Float-Truncation-HUD-Numbers.md)) |
| Coins flew above the chest in a Blender script | coin positions wrong | rotation applied around the world origin, because the object origin was at (0,0,0) | rotate in mesh space before translating ([FC-BL-04](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-BL-04-Rotation-Around-World-Origin.md)) |

## Common mistakes
- Changing several things at once, then not knowing which one fixed it.
- "Fixing" by adding `task.wait()` until a race seems to disappear.
- Deleting the reproduction steps after the fix (no regression test).

## Acceptance criteria
Each fixed bug has a one-sentence cause, a test or reproduction checklist, and evidence the test failed before and passes after.

## References
- https://create.roblox.com/docs/studio/debugging · https://create.roblox.com/docs/studio/developer-console
