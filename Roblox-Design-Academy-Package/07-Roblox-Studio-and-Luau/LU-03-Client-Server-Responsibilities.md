---
title: "LU-03 — Client–server responsibilities"
tags: [luau, security, networking, architecture]
note_type: "procedure"
evidence: "official docs"
---

# LU-03 — Client–server responsibilities

## The principle (Roblox security docs)
"Never trust the client." An exploiter controls their own client. They can decompile replicated scripts, take network ownership of their character and any unanchored parts, fire remotes at any rate with any arguments, and trigger `Touched`, `ProximityPrompt` and `ClickDetector` events from any range. **The server is the source of truth** for game state, rules, progression and decisions. The client renders and sends input.

## Responsibility table
| Concern | Client | Server |
|---|---|---|
| Input capture, camera, UI, local VFX/SFX | ✅ owns | — |
| "I pressed Buy on item X" | sends an *intent* | validates and decides |
| Prices, rewards, drop odds, cooldown timers that matter | never trusted | ✅ owns |
| Character movement | simulates (network owner) | validates plausibility if it matters (speed, teleport) |
| Hit detection in combat | may *propose* (origin + target) | checks distance from shooter, distance from target, line of sight to static geometry, fire rate, ammo, team, alive state |
| Saving data | — | ✅ only the server can access DataStores |
| Cosmetic feedback (button press, coin pop) | ✅ immediately, for responsiveness | confirms or corrects |

## Responsive *and* safe: optimistic feedback
1. The client plays the feedback right away: button press animation, a "pending" state.
2. The server validates, then applies the change.
3. The server replies with the authoritative result (RemoteFunction return value, or a RemoteEvent to that client).
4. The client reconciles: show the success celebration, or roll back with a short error message ("Too far from shop").

Never celebrate a purchase (confetti, sound) before the server confirms. A rollback after a celebration feels worse than a 100 ms wait.

## Threat-model questions for every feature (from Roblox "Security by design")
- If a client sent any value for each parameter, what is the worst outcome?
- What if this ran 1,000+ times per second? What rate should it allow?
- Could it be used to ruin another player's experience?
- What is the minimum state the client needs to see?

## Common mistakes
- Granting rewards on `Touched` without checking that the toucher's character exists, is alive and is near the object, and without rate limiting.
- Trusting `ProximityPrompt` properties for security. The docs say only `Triggered` has a server distance check, and `HoldDuration` can be altered by the client.
- Letting the client send *prices*, *damage values* or *reward amounts*.

## Acceptance criteria
- Every remote handler checks, in order: rate limit, type/shape, values, context (distance, ownership, state). Only then does it change state. [LU-05](LU-05-Server-Validation.md), [LU-06](LU-06-Rate-Limiting.md)
- No reward, currency or item change is decided on the client.

## References
- https://create.roblox.com/docs/scripting/security/security-tactics
- https://create.roblox.com/docs/scripting/security/client-server-boundary
- https://create.roblox.com/docs/scripting/security/network-ownership
