---
title: "LU-11 — Round-based game loop"
tags: [luau, rounds, multiplayer, state-machine]
note_type: "procedure"
evidence: "tested (CLI)"
code: "_tools/luau/src/RoundMachine.luau"
---

# LU-11 — Round-based game loop

## Purpose
A predictable Waiting → Intermission → Playing → Results cycle that cannot freeze, and that handles players leaving.

## Approach
`RoundMachine` is driven by `step(dt)` and `setPlayers(n)`; game code reacts in `onEnter(state)`.
```lua
local m = RoundMachine.new({ minPlayers = 2, intermission = 15, roundLength = 120, results = 8 })
RoundMachine.onEnter(m, function(state, machine)
    if state == "Playing" then spawnMap(); teleportPlayers()
    elseif state == "Results" then showWinner(machine.winner); cleanupMap() end
    statusRemote:FireAllClients(state, machine.timeLeft)      -- clients run their own countdown display
end)
Players.PlayerAdded:Connect(function() RoundMachine.setPlayers(m, #Players:GetPlayers()) end)
Players.PlayerRemoving:Connect(function() task.defer(function() RoundMachine.setPlayers(m, #Players:GetPlayers()) end) end)
RunService.Heartbeat:Connect(function(dt) RoundMachine.step(m, dt) end)
```
Send the state and remaining time once per transition. Clients count down locally; do not send the timer every frame.

## Rules encoded and why
- Every timed state has a limit, so a missed win condition cannot freeze the server loop.
- Dropping below `minPlayers` during a round goes to Results (no zombie rounds with one player left). During intermission it goes back to Waiting.
- `finish(winner)` works only while Playing, so a late win event cannot overwrite Results.

## Common mistakes
- `while true do wait(1) … end` with nested waits. Timings drift and the code is hard to test.
- Reading `#Players:GetPlayers()` inside `PlayerRemoving`, where the leaving player may still be counted. Defer one step.
- Low-population servers where a round can never start. Combine this with the guidance in [Low-Population Design](../13-Onboarding-and-Multiplayer/Multiplayer/Low-Population-Design.md): bots, solo mode or a lower minimum.

## Test cases (passing)
Full cycle with ordered transition events; mid-round drop → Results → Waiting; timeout → Results with no winner.

## Acceptance criteria
Tests pass; a 2-client Studio test cycles twice without errors; a client leaving mid-round ends it.
