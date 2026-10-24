---
title: "LU-21 — Error handling"
tags: [luau, errors, reliability]
note_type: "procedure"
evidence: "tested (Retry) + official docs"
code: "_tools/luau/src/Retry.luau"
---

# LU-21 — Error handling

## Purpose
Failures (web calls, bad data, bugs) degrade one feature instead of breaking the server loop or losing player progress.

## Rules
1. **Every yielding web API call goes in `pcall`**: DataStore, MessagingService, HttpService, MarketplaceService info queries, TeleportService.
2. **Retry only transient failures**, with capped exponential backoff and jitter (`Retry.call`). Do not retry invalid requests, as the docs advise. Tested: success after 2 failures with delays 1 s then 2 s; stop on a non-retryable error; the cap holds.
3. **Fail closed for player data.** If a load fails, do not let the player progress on defaults that will overwrite real data ([LU-08](LU-08-Player-Data-Persistence.md)).
4. **Isolate handlers.** An error inside one `Connect` callback does not stop other connections, but it does abort that handler mid-way. Validate before mutating, so a half-run handler leaves no half-changed state.
5. **Report errors with context.** `error("save failed for " .. key .. ": " .. tostring(err))`. Errors without the key or player are hard to trace.
6. `assert` for programmer mistakes (wrong config), `return false, reason` for expected runtime outcomes (insufficient funds). Do not error on normal gameplay outcomes.

## Pattern
```lua
local ok, result = Retry.call(function()
    return store:UpdateAsync(key, transform)
end, {
    attempts = 5, baseDelay = 1, maxDelay = 16, wait = task.wait,
    isRetryable = function(err) return not string.find(tostring(err), "invalid") end,  -- adapt to documented error codes
})
if not ok then warn("[Save] ", key, result) end
```
Look up the actual retryable error codes on the data store error-code page. The `"invalid"` match above is a placeholder.

## Common mistakes
- `pcall(store:GetAsync(key))`: that calls the function *before* `pcall`. Use `pcall(store.GetAsync, store, key)` or a closure.
- Swallowing errors silently (`pcall(fn)` without checking the result).
- Infinite retry loops without a cap, which burn the request budget for everyone.

## Acceptance criteria
No unprotected web call in the codebase (searchable: `GetAsync|SetAsync|UpdateAsync|PublishAsync|RequestAsync` each inside `pcall`/`Retry.call`); load failures fail closed; tests for the retry policy pass.

## References
- https://create.roblox.com/docs/cloud-services/data-stores/best-practices#retry-transient-failures · https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits
