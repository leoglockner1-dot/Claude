---
title: "LU-08 — Player data persistence"
tags: [luau, datastore, persistence]
note_type: "procedure"
evidence: "tested (CLI, pure parts) + official docs; DataStore calls not executed"
code: "_tools/luau/src/PlayerData.luau, _tools/luau/src/Retry.luau"
---

# LU-08 — Player data persistence

## Purpose
Load, migrate and save player progress without losing or duplicating it.

## Official guidance this follows (data-stores/best-practices, read 2026-10-24)
- Use **few data stores**, and **one key per player** (e.g. `User_123456`) while the data fits the **4 MB per-key** limit (4,194,304 bytes in the limits table).
- Use **static key patterns**, never display names.
- **Buffer in memory.** Load at session start, then save periodically, on leave, on shutdown, and at critical checkpoints such as purchases. The official sample uses a 180 s save interval, shorter than the session-lock expiry.
- **Stagger** recurring requests with a random offset and jitter.
- **Retry transient failures** with capped exponential backoff plus jitter, keep retries for one key in order, and remember that a failed write may still have succeeded.
- **Prefer `UpdateAsync`** when the write depends on the current value or several servers may write the key.
- Request budgets scale with players. Standard read and write budgets are `60 + numPlayers × 40` per minute; check the limits page for the current table.
- **Session locking** (official sample): lock the key in metadata during the first `UpdateAsync`, refresh it during autosaves, release it on the final save. This stops two servers from overwriting each other, which is the root of "item duplication" exploits.

## What the module does (pure, tested)
`PlayerData.fromSave(raw)` turns anything loaded from the store into a valid current-version table:
- `nil` → defaults (new player)
- old versions → run migrations in order (v1 `gold` → v2 `coins`; v2 flat `musicVolume` → v3 `settings`)
- wrong types/NaN → replaced with defaults; map entries filtered
- a **newer** version than this server knows → **refuse to load**. During a rolling update, an old server must not downgrade-overwrite data saved by a new server.

`PlayerData.toSave(d)` estimates the size, errors above 4 MB and warns above 256 KB (a house rule, so growth gets noticed early).

## Wiring sketch (not executed here)
```lua
local store = DataStoreService:GetDataStore("PlayerData")
local function load(player)
    local ok, raw = Retry.call(function() return store:GetAsync(PlayerData.key(player.UserId)) end,
        { wait = task.wait, rng = math.random })
    if not ok then player:Kick("Could not load your data, please rejoin") return end   -- never play on defaults after a failed load
    local data = PlayerData.fromSave(raw)
    sessions[player] = data
end
local function save(player)
    local data = sessions[player]; if not data then return end
    Retry.call(function()
        store:UpdateAsync(PlayerData.key(player.UserId), function(old) return (PlayerData.toSave(data)) end)
    end, { wait = task.wait })
end
Players.PlayerRemoving:Connect(function(p) save(p); sessions[p] = nil end)
game:BindToClose(function() for _, p in Players:GetPlayers() do task.spawn(save, p) end task.wait(3) end)
```
For production, add session locking (see the official sample) or use a well-maintained module, after reviewing its maintenance status as the docs advise.

## Common mistakes
- **Saving defaults over real data after a failed load.** This is the most destructive bug. If a load fails, do not let the player progress on defaults that will later be saved.
- `SetAsync` from several places for the same key (lost updates).
- Saving on every coin pickup, which exhausts the request budget.
- Editing an old migration after release. Add a new step instead.
- Using `player.Name` in keys (names can change).

## Test cases (passing)
New player defaults; v1→v3 migration with defaults filled in; wrong types and NaN dropped; newer-version save refused; size guard warns at 20k inventory entries; static key format.

## Acceptance criteria
- Pure tests pass.
- Studio test with API access enabled: join, earn, leave, rejoin → data restored.
- Simulated load failure (wrap `GetAsync` to error) → the player is not allowed to play on unsaved defaults.

## References
- https://create.roblox.com/docs/cloud-services/data-stores/best-practices
- https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits
- https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing
