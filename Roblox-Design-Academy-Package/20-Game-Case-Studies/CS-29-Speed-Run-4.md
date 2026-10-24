---
title: "CS-29 — Speed Run 4 (skill platformer with per-level identity and time pressure)"
tags: [case-study, obby, platformer, skill, speedrun]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-29 — Speed Run 4 (skill platformer with per-level identity and time pressure)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [[🎃] Speed Run 4](https://www.roblox.com/games/183364845/) · universe 83858907 · by Vurse |
| Genre (Roblox) | Obby & Platformer / – · max 30 players per server |
| Concurrent players at capture | 1,140 |
| Visits · favourites | 1,755,057,036 · 4,572,640 (2.61 per 1k visits) |
| Like ratio | 74% (1,040,223 up / 369,861 down) |
| Created / updated | 2014-10-20 / 2026-10-22 |
| Game passes for sale | 12 · 50–999 R$ (median 499) · e.g. 8x Egg Hatches (599), FINAL DESTINY (999), Gravity Coil (530), 3x Egg Hatches (279), Speed Coil (170), Anime World (499), Fly on a Cloud (800), 2x Luck (99) |

**Developer description (excerpt):** "Join in the fast paced fun and test your skill with this challenging platformer! There are dozens of unique levels to run and parkour through to victory. Each level has a unique song and appearance.. Can you reach all the final levels? Race your friends, or race against the clock and keep an eye on the timer, good luck! …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Run and parkour through dozens of unique levels; race friends or the clock; unlock forbidden levels with stars and dimensions by beating the game. |
| Main action | [INF] Run, jump, precise platforming at speed. |
| Immediate feedback | [DEV] A timer; [DEV] each level has a unique song and appearance. |
| Reward → new possibility | [DEV] Level completion → next level; stars → forbidden levels; beating the game → dimensions. |
| Micro loop (seconds) | [INF] Execution skill (jumps, timing); [DEV] racing against time/friends. |
| Core loop (minutes) | [INF] attempt level → fail/retry → finish → improve time or move on. |
| Meta loop (days) | [DEV] Hidden/locked content (forbidden levels, dimensions), [INF] personal bests; [DATA] 12 passes incl. "Gravity Coil" (530) - a movement aid that changes the challenge. |

## First-time experience
[INF] Instant clarity (run to the end); difficulty likely ramps. *Not observed.*

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | **Each level has its own song and look**: identity per stage makes progress memorable, not a list of numbers. Speedrun timer adds mastery replay. |
| Weakest part / quit risks | [DATA] 74% like ratio in a 1.75B-visit game; [INF] difficulty walls and movement-aid passes can frustrate or feel like paying to skip skill. |
| Essential features | Tight controls, readable level identity, timer. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | 3 short levels with distinct colour/music; a timer; test if players replay level 1 to beat their time. |

## Reusable lessons
- Give stages **identity** (palette + music), so progress feels like travelling.
- A timer converts a finished level into a mastery loop at near-zero content cost.
- Selling movement aids in a skill game is a trade-off: it monetizes frustration and changes the game.

## Original application (do not copy the game)
A rooftop courier run where each district has its own soundtrack; deliveries are timed; secret shortcuts unlock with collected stamps.

## Confidence
Medium for structure (developer explicit).

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
