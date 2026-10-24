---
title: "LU-10 — Inventory, stacking and crafting costs"
tags: [luau, inventory, crafting]
note_type: "procedure"
evidence: "tested (CLI)"
code: "_tools/luau/src/Inventory.luau"
---

# LU-10 — Inventory, stacking and crafting costs

## Purpose
A server-side inventory model that never loses rewards silently and never takes half a crafting cost.

## Design rules encoded
- Item definitions (stack size) live on the server.
- `add()` tops up existing stacks, then opens slots, and **returns how many fit**. The caller decides what to do with the rest: mail it, drop it, or show "Inventory full". Silent deletion is a top source of angry bug reports.
- `remove()` is all-or-nothing.
- `consume({ore = 5, wood = 2})` checks every cost before removing any.

## UI mirror
The client shows a copy. After every server change, send a small diff (`{slot, id, count}`) or the full list if it is short. Do not let the client move items locally without server confirmation, except as an optimistic preview that can roll back.

## Common mistakes
- Checking costs one at a time while removing, which leaves partial removal when the second item is missing.
- Using `#inventory` as "item count" when slots hold stacks.
- Trusting a client "move slot 3 to slot 7" request without validating both indices and ownership.

## Test cases (passing)
Stacks to 50, opens slots up to capacity, reports 30 of 40 fitting; remove is all-or-nothing and removes emptied stacks; `consume` with one missing cost changes nothing.

## Acceptance criteria
Tests pass; no reward path calls `add()` without handling the overflow return value.
