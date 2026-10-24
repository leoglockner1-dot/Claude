---
title: "FC-LU-01 — Luau: a bare tuple type alias broke parsing, and require hid it"
tags: [failure-case, luau, tooling]
note_type: "failure-case"
evidence: "real failure observed in this session (2026-10-24)"
---

# Luau: a bare tuple type alias broke parsing, and require hid it

| Field | Record |
|---|---|
| **Problem** | Luau: a bare tuple type alias broke parsing, and require hid it |
| **Context** | Writing `Validate.luau` for the academy's tested Luau library (standalone Luau CLI, commit 32c2808). |
| **Observable symptoms** | Running the test suite failed in a *different* file: `ShopServer.luau:51: attempt to call a nil value` on `Validate.Str(...)`. Printing the module's keys showed every field was nil; `type(require(...))` was `"string"`. |
| **Cause (established)** | `export type Result = (boolean, string?)` is not valid Luau. A parenthesised type list is parsed as the start of a function type, so the parser expected `->`. The module failed to parse, and the CLI's `require` returned the error message string instead of raising, so the failure surfaced later as a nil call. |
| **Correction** | Removed the alias (functions return `(boolean, string?)` directly). Added a rule and the `run_tests.sh` script: run `luau-analyze` on **every** file before running tests. |
| **How the correction was tested** | `luau-analyze` printed the parse errors immediately; after the fix the suite ran. |
| **Final result** | 54/54 tests pass; 0 type errors. |
| **Reusable lesson** | Type-check before you run. When a symptom appears in module B, check that module A even parsed. A required module that is a string is a parse failure. |
| **Related** | [LU-00](../../07-Roblox-Studio-and-Luau/LU-00-Working-Method.md), [LU-01](../../07-Roblox-Studio-and-Luau/LU-01-Luau-Essentials.md), [LU-22](../../07-Roblox-Studio-and-Luau/LU-22-Debugging-Workflow.md) |
