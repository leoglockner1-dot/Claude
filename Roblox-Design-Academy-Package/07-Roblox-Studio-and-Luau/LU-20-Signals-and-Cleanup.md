---
title: "LU-20 — Signals, cleanup and memory leaks"
tags: [luau, memory, events, architecture]
note_type: "procedure"
evidence: "tested (CLI) + official docs"
code: "_tools/luau/src/Signal.luau"
---

# LU-20 — Signals, cleanup and memory leaks

## Purpose
Let modules communicate without tight coupling, and release everything a player or round created when it ends.

## Facts (performance-optimization/improve docs)
- The engine never garbage-collects **connected** event callbacks or the values they reference while the connection lives.
- A common wrong assumption: when a user leaves, their `Player` object and character are **not automatically destroyed** unless `Workspace.PlayerCharacterDestroyBehavior` is enabled. Connections on them keep consuming memory.
- Tables keyed by player that are never cleared grow forever on long-running servers.
- Developer Console memory values that point to leaks: **LuaHeap** growing, **InstanceCount** growing, **PlaceScriptMemory** per script.

## Tools here
- `Signal.new()`: `connect`, `fire`, `count`. Handlers connected or disconnected during a fire take effect next time, so there is no skipped-listener bug. Tested: a handler that disconnects another during the same fire.
- `Signal.janitor()`: `add(item)` accepts functions, Luau connections, `RBXScriptConnection`s (`Disconnect`) and Instances (`Destroy`); `clean()` runs in **reverse order**. Tested.

## Procedure
1. Per player: create a janitor in `PlayerAdded`. Add every connection, spawned instance and per-player table cleanup to it.
2. In `PlayerRemoving`: `janitor:clean()`, then clear all `[player]`/`[userId]` table entries (limiters, sessions, inventories).
3. Per round: one janitor for map, NPCs and round connections, cleaned on Results.
4. Enable `PlayerCharacterDestroyBehavior`, or destroy `Player`/character in `PlayerRemoving`/`CharacterRemoving` with `task.defer`, as the docs show.

## Common mistakes
- Connecting to `player.CharacterAdded` inside `PlayerAdded` and never disconnecting.
- `RunService.Heartbeat:Connect` for a short effect and forgetting to disconnect.
- Holding Instances in module-level tables after they are destroyed.

## Test cases
- CLI: the janitor cleans in reverse order and disconnects signals (passing).
- Studio: join/leave 8 clients repeatedly (Multi-client simulation, or `StudioTestService` for scripted runs). Server LuaHeap and InstanceCount return to baseline.

## Acceptance criteria
Every `Connect` in server code is either on an instance that is destroyed with its owner or added to a janitor; per-player tables are cleared on leave.

## References
- https://create.roblox.com/docs/performance-optimization/improve#script-memory-usage · https://create.roblox.com/docs/studio/testing-modes
