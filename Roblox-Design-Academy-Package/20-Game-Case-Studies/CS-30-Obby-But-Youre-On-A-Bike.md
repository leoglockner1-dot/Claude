---
title: "CS-30 — Obby But You're On a Bike (one twist on a saturated genre)"
tags: [case-study, obby, twist, vehicle, speedrun]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-30 — Obby But You're On a Bike (one twist on a saturated genre)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [[🎃PARK] Obby But You’re On a Bike](https://www.roblox.com/games/14184086618/) · universe 4908792642 · by FORTUNE 777 |
| Genre (Roblox) | Obby & Platformer / – · max 20 players per server |
| Concurrent players at capture | 1,129 |
| Visits · favourites | 1,949,377,419 · 8,528,880 (4.38 per 1k visits) |
| Like ratio | 76% (948,631 up / 293,950 down) |
| Created / updated | 2023-07-25 / 2026-10-24 |
| Game passes for sale | 9 · 99–399 R$ (median 199) · e.g. Fly On Any Bike (299), Motorcycle (399), Gravity Coil (139), Teleport Gun (149), World Pass (399), Double Trophies (199), Neon Paint (99), SnowRacer X (399) |

**Developer description (excerpt):** "🚴 Beat the Obby on Your Trusty Bike! 🏁 Explore 111 unique worlds with 100 challenging stages! ⏰ Compete on Speedrun Leaderboards and prove you’re the ultimate rider. 💖 Thank you to all our amazing players for your continued support! Tags: Obby, Bike Trail, Biking, Obstacle Course, Fun, Bike Obby, Parkour, Race This game may …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Beat the obby on a bike: 111 worlds, 100 stages, speedrun leaderboards. |
| Main action | [INF] Ride a bike through obstacle stages (momentum control instead of jumping). |
| Immediate feedback | [INF] Bike physics, falls, checkpoints. |
| Reward → new possibility | [DEV] Stage progress, speedrun leaderboard placement; [DATA] passes: Fly On Any Bike 299, Motorcycle 399, Gravity Coil 139, Teleport Gun 149. |
| Micro loop (seconds) | [INF] Momentum and balance skill. |
| Core loop (minutes) | [INF] ride stage → fail/retry → checkpoint → next stage. |
| Meta loop (days) | [DEV] Leaderboards; large stage count; [DATA] high favourites per 1k visits (4.38). |

## First-time experience
[DEV] The title is the tutorial: "obby, but on a bike" tells you everything before you join.

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | **A one-line twist** that changes the core verb (jump → ride) and is fully explained by the name; highest favourites/visit ratio among the obbies here. |
| Weakest part / quit risks | [DATA] 76% likes; [INF] skip passes (Teleport Gun, Fly) undercut the challenge; physics frustration. |
| Essential features | Bike controller, stage set, checkpoints. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | Bike controller + 5 stages; compare completion vs the same stages on foot. |

## Reusable lessons
- In a saturated genre, **change the verb**, not the theme, and put the change in the title.
- Leaderboards add mastery to finite content.

## Original application (do not copy the game)
Obby on a pogo stick: constant bouncing makes timing the core skill; stages reward rhythm.

## Confidence
Medium.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
