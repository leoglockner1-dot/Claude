---
title: "CS-27 — Lumber Tycoon 2 (physical logistics as the core skill)"
tags: [case-study, tycoon, sandbox, physics, logistics]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-27 — Lumber Tycoon 2 (physical logistics as the core skill)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [🌳 Lumber Tycoon 2](https://www.roblox.com/games/13822889/) · universe 2471084 · by Defaultio |
| Genre (Roblox) | Simulation / Tycoon · max 6 players per server |
| Concurrent players at capture | 2,354 |
| Visits · favourites | 1,338,606,431 · 4,657,839 (3.48 per 1k visits) |
| Like ratio | 88% (2,037,710 up / 285,895 down) |
| Created / updated | 2009-07-30 / 2026-10-24 |
| Game passes for sale | 3 · 220–720 R$ (median 390) · e.g. Super Blueprints (720), Super Hoove (390), Super Bridge (220) |

**Developer description (excerpt):** "Welcome to Lumberland! Deforest your surroundings and build your dreams! Check the changelog to keep up with the most recent updates. You can find it in the game menu. Thanks for playing!"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Deforest your surroundings and build your dreams. |
| Main action | [INF] Chop trees with axes, transport logs physically, process at a sawmill, build structures. |
| Immediate feedback | [INF] Physical logs falling and needing transport; money on sale. |
| Reward → new possibility | [INF] Money → better axes, vehicles, land, blueprints; [DATA] passes: Super Blueprints 720, Super Hoove 390, Super Bridge 220. |
| Micro loop (seconds) | [INF] Physical handling/transport skill (logs are objects, not counters). |
| Core loop (minutes) | [INF] find wood → chop → haul → mill/sell → buy tools/land → build. |
| Meta loop (days) | [INF] Rare woods in distant biomes; building a personal base; very long history (created 2009). |

## First-time experience
[DEV] Description gives almost no onboarding; [INF] relies on community knowledge. *Not observed.*

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | Turning resources into **physical objects** makes logistics the gameplay (loading a truck is a puzzle). |
| Weakest part / quit risks | [INF] Opaque onboarding; physics frustration. |
| Essential features | Physical resource objects, transport, sawmill, land. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | One forest, axe, a truck, a mill; test whether hauling feels like play or chore. |

## Reusable lessons
- Physicalizing a resource changes the genre: a counter becomes a logistics puzzle.
- Long-tail games can survive on depth even with minimal descriptions, but new-player clarity likely suffers.

## Original application (do not copy the game)
A ice-harvesting game on a frozen lake: cut blocks, slide them to the icehouse before they melt.

## Confidence
Low–medium.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
