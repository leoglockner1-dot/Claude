---
title: "LU-06 — Rate limiting with a token bucket"
tags: [luau, security, rate-limit]
note_type: "procedure"
evidence: "tested (CLI) + official docs"
code: "_tools/luau/src/TokenBucket.luau"
---

# LU-06 — Rate limiting with a token bucket

## Purpose
Stop spam of anything a client can trigger: remotes, `Touched`, prompts, clicks. Allow short natural bursts.

## Approach
A **token bucket** per player, which is the algorithm Roblox's security docs use. The bucket holds `capacity` tokens; each action spends one; tokens refill at `capacity / windowSeconds` per second.

```lua
local TokenBucket = require(script.Parent.TokenBucket)
local limiter = TokenBucket.new(5, 10, time)        -- burst 5, then 1 every 2 s
remote.OnServerEvent:Connect(function(player, ...)
    if not limiter:allow(player.UserId) then return end
    -- validate, then act
end)
Players.PlayerRemoving:Connect(function(p) limiter:forget(p.UserId) end)   -- avoid leaks
```

Differences from the docs' version: the clock is injected (so tests control time), `forget()` is built in, and an optional `cost` lets expensive actions spend more.

## Choosing numbers
| Action | Suggested start | Reasoning |
|---|---|---|
| Shop purchase | 5 / 10 s | People rarely buy more than a few things in a burst |
| Chat-like custom message | 5 / 10 s | Same as the docs' chat example |
| Weapon fire | slightly above the weapon's real fire rate | Server truth = weapon cooldown; the bucket is a backstop |
| Cosmetic emote | 3 / 5 s | Low value, high spam potential |
Tune from playtests and analytics. These are starting points, not facts.

## Common mistakes
- Client-side cooldown only. It is good for UX and useless for security.
- One global bucket for all players. One spammer then blocks everyone.
- Never clearing buckets for players who left (a slow memory leak on long-running servers).
- Dropping a request silently when the player needs feedback. Return a reason (`"slow down"`) on RemoteFunctions.

## Test cases (passing)
- A burst of 5 is allowed and the 6th is refused.
- After 1.9 s there is no token (0.95); at 2.0 s one token exists.
- Players are independent; `forget` clears state.
- Integration: 50 rapid purchases → exactly 5 accepted (`ShopServer` test).

## Acceptance criteria
Every client-triggerable server action has a limiter with a documented rate; buckets are cleared on `PlayerRemoving`.

## References
- https://create.roblox.com/docs/scripting/security/client-server-boundary#rate-limiting
