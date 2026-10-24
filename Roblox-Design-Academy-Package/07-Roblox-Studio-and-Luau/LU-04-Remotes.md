---
title: "LU-04 — Remote events, functions and unreliable remotes"
tags: [luau, networking, remotes]
note_type: "procedure"
evidence: "official docs"
---

# LU-04 — Remote events, functions and unreliable remotes

## Purpose
Pick the right remote type and avoid the argument-passing traps.

## Choosing
| Type | Delivery | Use for | Avoid for |
|---|---|---|---|
| `RemoteEvent` | Reliable and **ordered**, including across different RemoteEvent instances, in one direction per connection | Intents (buy, equip), state pushes (round started) | Per-frame streams |
| `RemoteFunction` | Reliable; the caller **yields** until the reply arrives | Requests that need an answer (purchase result) | Server→client invokes (a client that never answers makes the server thread wait) |
| `UnreliableRemoteEvent` | No delivery guarantee, no ordering; dropped if the payload is over **1,000 bytes**, if the client exceeds the throttle, or if no handler is connected | Frequent cosmetic updates (aim direction, VFX cues) where only the latest matters | Anything that must arrive |

## Facts from the docs that cause real bugs
- The server handler's first parameter is always the `Player` who fired it. The client cannot spoof it, but every other argument can be anything.
- **Ordering applies to when handlers *start*.** If a handler yields (`task.wait`, `WaitForChild`), the next message can begin before it resumes. Do not assume handler A finishes before handler B.
- If no handler is connected, RemoteEvent messages are **queued**, and the queue is limited. Once it is full, messages are dropped with a "Remote event invocation" error. Connect handlers at start-up, before clients can fire.
- RemoteFunction calls and RemoteEvent messages have **no guaranteed relative order**. If order matters, use one remote type or add sequence numbers.
- Only the last `OnServerInvoke` assignment takes effect.
- Argument limitations: tables with non-string keys get their keys **converted to strings**; functions arrive as `nil`; metatables are not kept; mixed tables and table identity are not preserved; instances that do not replicate to the receiver arrive as `nil`.
- Client→server messages share a throttle per remote type. See the Throttling section of the `RemoteEvent` API page for current numbers. They change, so do not hard-code numbers from memory.

## Implementation pattern
```lua
-- ServerMain (RunContext = Server). Create remotes on the server so they exist before clients look.
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local folder = Instance.new("Folder"); folder.Name = "Remotes"; folder.Parent = ReplicatedStorage
local buy = Instance.new("RemoteFunction"); buy.Name = "BuyItem"; buy.Parent = folder
buy.OnServerInvoke = function(player, payload)
    return shop:buy(player, payload)          -- see LU-07; validation happens inside
end
```
```lua
-- Client: never assume success
local result = { ReplicatedStorage.Remotes.BuyItem:InvokeServer({ itemId = "sword", qty = 1 }) }
if result[1] then showPurchased(result[2]) else showError(result[2]) end
```

## Common mistakes
- Sending whole Instances or large tables every frame. Send ids and small numbers.
- Expecting a table with `[player] = score` keys to arrive intact. The keys become strings.
- Using `InvokeClient` on the server without a timeout strategy.

## Test cases
- Fire the remote with `nil`, a string, a huge table, NaN and a table with extra keys. The server must reject each without erroring. The pattern is shown in [`tests/run_all.luau`](../_tools/luau/tests/run_all.luau) ("rejects exploit payloads").
- Fire 50 times in one second. Accepted requests must be at most the burst capacity ([LU-06](LU-06-Rate-Limiting.md)).

## References
- https://create.roblox.com/docs/scripting/events/remote (Delivery guarantees, Argument limitations)
- https://create.roblox.com/docs/reference/engine/classes/RemoteEvent (Throttling)
