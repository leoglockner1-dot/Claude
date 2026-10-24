---
title: "Engineering Principles (ENG-001 – ENG-008)"
tags: [principles, eng]
note_type: "principles"
---

# Engineering Principles (ENG-001 – ENG-008)

Principles for Roblox/Luau systems, backed by the tested module library and official docs.

| ID | Principle | Confidence |
|---|---|---|
| ENG-001 | Pure modules, thin wiring | Medium-high |
| ENG-002 | Validate in four layers | Medium-high |
| ENG-003 | Treat NaN as hostile | Medium-high |
| ENG-004 | Fail closed on data loads | Medium-high |
| ENG-005 | Grant once, confirm after save | Medium-high |
| ENG-006 | Type-check before running | Medium-high |
| ENG-007 | Boundary-test display math | Medium-high |
| ENG-008 | Show effective odds when modifiers apply | Medium-high |

## ENG-001 — Pure modules, thin wiring
**Rule:** Put rules in engine-free modules with injected time/randomness/IO; keep engine wiring short.

- **Reasoning:** Logic bugs are what damage players, and CLI tests catch them.
- **Evidence:** [LU-00](../07-Roblox-Studio-and-Luau/LU-00-Working-Method.md); 54 passing tests.
- **Good application:** ShopServer with MockRoblox.
- **Failure mode:** Rules buried in LocalScripts and Touched handlers.
- **Conditions & exceptions:** One-off visual scripts.
- **Roblox implementation:** ModuleScripts with `start()` ([LU-02](../07-Roblox-Studio-and-Luau/LU-02-Project-Architecture.md)).

## ENG-002 — Validate in four layers
**Rule:** Rate limit → type/shape → values → context, before any state change.

- **Reasoning:** Exploiters control all client data (Roblox security docs).
- **Evidence:** [LU-05](../07-Roblox-Studio-and-Luau/LU-05-Server-Validation.md), [LU-06](../07-Roblox-Studio-and-Luau/LU-06-Rate-Limiting.md).
- **Good application:** BuyItem handler.
- **Failure mode:** Trusting a client-sent price.
- **Conditions & exceptions:** —
- **Roblox implementation:** Validate.luau + TokenBucket.luau.

## ENG-003 — Treat NaN as hostile
**Rule:** Reject non-finite numbers explicitly; range checks alone do not stop NaN.

- **Reasoning:** NaN fails every comparison (Roblox docs; asserted in tests).
- **Evidence:** [LU-05](../07-Roblox-Studio-and-Luau/LU-05-Server-Validation.md).
- **Good application:** `Validate.number`.
- **Failure mode:** Trade offers with NaN gold.
- **Conditions & exceptions:** —
- **Roblox implementation:** `math.isfinite` in Roblox.

## ENG-004 — Fail closed on data loads
**Rule:** If player data fails to load, never let the player progress on defaults that will overwrite real data.

- **Reasoning:** The most destructive persistence bug.
- **Evidence:** [LU-08](../07-Roblox-Studio-and-Luau/LU-08-Player-Data-Persistence.md).
- **Good application:** Kick with a retry message after Retry fails.
- **Failure mode:** Silent defaults saved on leave.
- **Conditions & exceptions:** —
- **Roblox implementation:** Retry.call + session locking.

## ENG-005 — Grant once, confirm after save
**Rule:** For developer products, record PurchaseIds and return PurchaseGranted only after a successful save.

- **Reasoning:** Official purchasing sample.
- **Evidence:** [LU-09](../07-Roblox-Studio-and-Luau/LU-09-Developer-Product-Receipts.md) tests.
- **Good application:** `Receipts.process`.
- **Failure mode:** Double grants on retries; lost purchases on crash.
- **Conditions & exceptions:** —
- **Roblox implementation:** ProcessReceipt adapter.

## ENG-006 — Type-check before running
**Rule:** Run luau-analyze (strict) on every file before running tests.

- **Reasoning:** A module that does not parse can make require return a string.
- **Evidence:** [FC-LU-01](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-LU-01-Luau-Type-Alias-Parse-Error-Silent-Require.md).
- **Good application:** run_tests.sh.
- **Failure mode:** Debugging symptoms in the wrong file.
- **Conditions & exceptions:** —
- **Roblox implementation:** Studio Script Analysis / `--!strict`.

## ENG-007 — Boundary-test display math
**Rule:** Test number formatting and rounding at non-representable values (9.87M, 999,999).

- **Reasoning:** Floating-point truncation produced 9.86M.
- **Evidence:** [FC-LU-02](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-LU-02-Float-Truncation-HUD-Numbers.md).
- **Good application:** Feel.abbreviate tests.
- **Failure mode:** Prices that disagree between shop and wallet.
- **Conditions & exceptions:** —
- **Roblox implementation:** One shared formatter module.

## ENG-008 — Show effective odds when modifiers apply
**Rule:** When pity or luck boosts apply to a paid random roll, display the effective odds, not the base odds.

- **Reasoning:** Roblox's paid random items policy lists pity systems and luck boosts as probability modifiers that must be explained numerically.
- **Evidence:** [LU-13](../07-Roblox-Studio-and-Luau/LU-13-Random-Rewards.md).
- **Good application:** `WeightedLoot.effectiveOdds`.
- **Failure mode:** Showing base odds during a forced pity roll.
- **Conditions & exceptions:** Free (non-paid) rolls are outside that policy, but transparency still builds trust.
- **Roblox implementation:** Odds UI behind a labelled 'Details' button.
