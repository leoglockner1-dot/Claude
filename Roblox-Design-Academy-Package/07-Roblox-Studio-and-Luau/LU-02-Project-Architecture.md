---
title: "LU-02 — Project architecture and script locations"
tags: [luau, architecture, studio]
note_type: "procedure"
evidence: "official docs"
---

# LU-02 — Project architecture and script locations

## Purpose
A layout where every script has an obvious home, server secrets never replicate, and one entry point per side makes start-up order predictable.

## What Roblox recommends (scripting/locations, read 2026-10-24)
- A single `Script` with `RunContext = Client` in `ReplicatedStorage`, and a single `Script` with `RunContext = Server` in `ServerScriptService`.
- Put as much code as possible in `ModuleScript`s that those two scripts require. Give each module a `start()` function, so that **all modules load before any starts**.
- Shared code goes in ModuleScripts in `ReplicatedStorage`.
- Use `LocalScript`s sparingly; if you must, put them in the Starter containers. Scripts there are cloned per player, which makes Output links point at ephemeral copies.
- Avoid scripts inside Workspace instances. **Tag** instances and handle them from one module with `CollectionService`. Exception: distributable models/packages, which should set an explicit `RunContext`.
- A default `Script` has `RunContext = Legacy`: server-side, and it runs only in server containers.

## Recommended tree
```
ReplicatedStorage
  Shared/            ModuleScripts used by both sides (Feel, Signal, item definitions WITHOUT secrets)
  Remotes/           RemoteEvent / RemoteFunction instances (created by the server at start-up, or placed in Studio)
  ClientMain         Script, RunContext = Client  -> requires Client/* modules, calls start()
  Client/            client-only ModuleScripts (UI controllers, input, camera, VFX playback)
ServerScriptService
  ServerMain         Script, RunContext = Server  -> requires Server/* modules, calls start()
  Server/            server-only ModuleScripts (Validate, TokenBucket, Currency, PlayerData, ShopServer...)
ServerStorage        assets the client must not see until the server clones them (maps, loot models)
ReplicatedFirst      loading screen only (minimal)
```

## Decisions and their reasons
| Decision | Reason |
|---|---|
| Prices, drop tables and reward amounts live in `ServerScriptService` | Anything in ReplicatedStorage can be read by exploiters; the docs note that even ModuleScripts that never run on the client can be decompiled if they replicate. |
| Remotes in one folder, named after intents (`BuyItem`, `RequestRespawn`) | Easy to audit: each remote = one validated server handler. |
| Modules expose `start()` and do not connect events at require time | Avoids order bugs where module A fires before module B has connected. |
| CollectionService tags instead of per-part scripts | One place to fix a bug; fewer scripts; instances can be added at runtime. |

## Common mistakes
- Putting server-only modules in ReplicatedStorage "because both sides need the item list". Split public data (names, icons) from private data (drop weights, server-only prices).
- `while true do … wait() end` loops in many scripts. Use events, or one scheduler.
- Requiring client modules from the server (they may reference `Players.LocalPlayer`, which is nil on the server).

## Acceptance criteria
- Exactly one server entry script and one client entry script (plus an optional ReplicatedFirst loader).
- No secrets (prices used for validation, loot weights, admin lists) in replicated containers.
- Every tagged behaviour is handled by a module that also handles instances added later (`GetInstanceAddedSignal`).

## References
- https://create.roblox.com/docs/scripting/locations · https://create.roblox.com/docs/scripting/security/access-control · https://create.roblox.com/docs/scripting/module
