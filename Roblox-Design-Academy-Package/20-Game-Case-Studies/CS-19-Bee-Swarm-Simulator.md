---
title: "CS-19 — Bee Swarm Simulator (collection + territory incremental)"
tags: [case-study, simulator, incremental, collection, quests]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-19 — Bee Swarm Simulator (collection + territory incremental)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [Bee Swarm Simulator](https://www.roblox.com/games/1537690962/) · universe 601130232 · by Onett |
| Genre (Roblox) | Simulation / Incremental Simulator · max 6 players per server |
| Concurrent players at capture | 32,375 |
| Visits · favourites | 4,624,717,686 · 6,560,329 (1.42 per 1k visits) |
| Like ratio | 96% (3,042,572 up / 139,984 down) |
| Created / updated | 2018-03-21 / 2026-08-22 |
| Game passes for sale | 0 · e.g. none listed for sale (developer products are not visible through this API) |

**Developer description (excerpt):** "Grow your own swarm of bees, collect pollen, and make honey in Bee Swarm Simulator! Meet friendly bears, complete their quests and get rewards! As your hive grows larger and larger, you can explore further up the mountain. Use your bees to defeat dangerous bugs and monsters. Look for treasures hidden around the map. Discover …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Grow a swarm of bees, collect pollen and make honey, then use the hive to climb further up the mountain and fight bugs. |
| Main action | [INF] Walk through flower fields while bees gather pollen; convert pollen to honey at the hive. |
| Immediate feedback | [INF] Pollen counter filling; bees visibly flying to flowers; a backpack-full state that forces a return trip. |
| Reward → new possibility | [DEV] Honey buys bees and gear → **new fields higher up the mountain** (territory unlock, not just bigger numbers); quests from bears give rewards. |
| Micro loop (seconds) | [INF] Choose where to stand (field choice), when to return to convert. Low dexterity skill, moderate route/timing decisions. |
| Core loop (minutes) | [INF] gather → convert → buy bees/equipment → unlock a higher field → repeat with new flower types. |
| Meta loop (days) | [DEV] Bear quest chains, new bee types "with their own traits and personalities", treasures hidden around the map, monster fights. |

## First-time experience
[INF] The description gives a clear first verb ("collect pollen") and a visible destination ("explore further up the mountain"). The first-session reward is likely the first new bee or field. *Not observed: actual timings of the first 10/30 s.* [HYP] The mountain is a strong diegetic progress map: players can see where they are going.

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | Progress is **spatial** (higher fields) and **collectible** (bee types with personalities), so upgrades change *where* you play and *what* you own, not only rates. |
| Weakest part / quit risks | [INF] Long-term grind for higher fields; idle-ish micro loop can feel passive. [DATA] **0 game passes for sale** (monetization, if any, is via developer products, which are invisible here). |
| Essential features | Swarm growth visible on screen; field-gated mountain; quest giver structure. |
| Possibly unnecessary | Cannot judge without play. |
| Minimal prototype to test the idea | One field, 3 bee types, a hive conversion point, one gated second field; test whether players want to see the second field. |

## Reusable lessons
- Make progression **visible in the world**: a mountain you climb tells players their goal without UI.
- Collectibles with personality (traits, names) carry more attachment than stat items.
- Quest givers (characters) give direction and pacing to an otherwise open grind.

## Original application (do not copy the game)
A coral reef where your fish school cleans algae fields; deeper reef zones unlock as the school grows, and each fish species changes how the school moves.

## Confidence
Medium for structure ([DEV] description is explicit about the loop); low for pacing and first-session details.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
