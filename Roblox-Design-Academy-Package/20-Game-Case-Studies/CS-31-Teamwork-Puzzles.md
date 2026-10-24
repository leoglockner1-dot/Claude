---
title: "CS-31 — Teamwork Puzzles (award-winning puzzles, but the weakest like ratio in the sample)"
tags: [case-study, obby, co-op, puzzle, dependency]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-31 — Teamwork Puzzles (award-winning puzzles, but the weakest like ratio in the sample)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [Teamwork Puzzles (Obby)](https://www.roblox.com/games/13184713709/) · universe 4599924264 · by LemonBread Studios |
| Genre (Roblox) | Obby & Platformer / – · max 16 players per server |
| Concurrent players at capture | 1,855 |
| Visits · favourites | 739,197,166 · 302,181 (0.41 per 1k visits) |
| Like ratio | 49% (37,235 up / 38,423 down) |
| Created / updated | 2023-04-19 / 2026-10-13 |
| Game passes for sale | 5 · 199–799 R$ (median 399) · e.g. Magic Carpet (799), Gravity Coil (199), Portable Noob (499), Checkpoints (399), Double Coins (399) |

**Developer description (excerpt):** "🧩 Team up with up to 3 players to solve puzzles and beat obstacle courses! Don't leave anybody behind because you will need them later. Earn coins to unlock special trails or replay stages for a faster time. Play with friends for the best experience! 🏆 RIA 2025 Best Puzzle Experience"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Team up with up to 3 players to solve puzzles and beat obstacle courses; "Don't leave anybody behind because you will need them later." |
| Main action | [INF] Cooperative platforming and puzzle solving (pressing switches, carrying, timing together). |
| Immediate feedback | [INF] Doors opening when teammates coordinate. |
| Reward → new possibility | [DEV] Coins → trails; replay for faster times; [DEV] "RIA 2025 Best Puzzle Experience". |
| Micro loop (seconds) | [INF] Coordination and communication with teammates. |
| Core loop (minutes) | [INF] reach puzzle → coordinate → solve → next stage. |
| Meta loop (days) | [DEV] Cosmetics, faster replays; [DATA] passes include "Checkpoints" (399), "Portable Noob" (499), "Magic Carpet" (799). |

## First-time experience
[INF] The experience depends on finding cooperative teammates; with strangers or alone it may stall.

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | [DEV] Recognized puzzle design (award). Forced interdependence creates memorable social moments with friends. |
| Weakest part / quit risks | [DATA] **49% like ratio**, the lowest of 113 games pulled. [INF] Likely causes: dependency on strangers (one AFK or troll blocks progress), solo players unable to progress, pay-to-skip passes in a puzzle game. *Cause not verified.* |
| Essential features | Puzzles requiring 2+ players, team matchmaking. |
| Possibly unnecessary | [INF] Skip passes conflict with puzzle satisfaction. |
| Minimal prototype to test the idea | Two puzzles that need 2 players + a solo fallback (bot or alternate path); compare completion and like rate with/without fallback. |

## Reusable lessons
- **Hard dependency on strangers is a quit risk**: plan for AFK/trolls/solo (fallbacks, kicking, bots).
- Awards and good design do not guarantee player satisfaction when matchmaking fails.
- See [Low-Population Design](../13-Onboarding-and-Multiplayer/Multiplayer/Low-Population-Design.md).

## Original application (do not copy the game)
A two-key vault heist where either player can carry both keys at a slower speed, so a partner helps but is never required.

## Confidence
Low for causes; high for the data anomaly.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
