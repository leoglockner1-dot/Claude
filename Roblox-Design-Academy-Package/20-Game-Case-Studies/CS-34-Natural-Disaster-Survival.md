---
title: "CS-34 — Natural Disaster Survival (one rule, random events, 18 years later)"
tags: [case-study, survival, party, rounds, randomness]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-34 — Natural Disaster Survival (one rule, random events, 18 years later)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [Natural Disaster Survival](https://www.roblox.com/games/189707/) · universe 65241 · by Stickmasterluke |
| Genre (Roblox) | Survival / – · max 30 players per server |
| Concurrent players at capture | 9,034 |
| Visits · favourites | 4,524,090,234 · 11,919,460 (2.63 per 1k visits) |
| Like ratio | 91% (4,422,336 up / 449,783 down) |
| Created / updated | 2008-03-28 / 2026-09-17 |
| Game passes for sale | 3 · 60–95 R$ (median 80) · e.g. Green Balloon (95), Red Apple (80), Yellow Compass (60) |

**Developer description (excerpt):** "Quickly, run around in circles! Your life depends on it!"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] "Quickly, run around in circles! Your life depends on it!" |
| Main action | [INF] Move to safe spots as a random disaster hits a random map. |
| Immediate feedback | [INF] Environmental destruction, deaths, survival announcement. |
| Reward → new possibility | [INF] Survival (wins); [DATA] 3 cheap passes (60–95 R$) for small tools (Balloon, Apple, Compass). |
| Micro loop (seconds) | [INF] Positioning decisions under threat. |
| Core loop (minutes) | [INF] round: map + disaster revealed → survive → results → next round. |
| Meta loop (days) | [INF] Social play and variety from map × disaster combinations; minimal progression. |

## First-time experience
[INF] Zero learning required: run from danger. The 7-word description shows how little is needed.

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | **Combinatorial variety** (maps × disasters) from a tiny ruleset; instantly understood; [DATA] created 2008, 91% likes, 11.9M favourites. |
| Weakest part / quit risks | [INF] Little long-term progression; fits a casual, social niche. |
| Essential features | Random disaster, random map, short rounds. |
| Possibly unnecessary | Most systems: the game shows how little is needed. |
| Minimal prototype to test the idea | 2 maps × 2 disasters, 90-second rounds; test round-to-round retention. |

## Reusable lessons
- Variety through **combinations** of a few contents beats a long list of unique content.
- Short rounds with an instantly legible threat need almost no onboarding.

## Original application (do not copy the game)
Weather Roulette on floating islands: each round, a random weather (fog, gusts, lightning) changes how islands behave.

## Confidence
Medium (classic, well-known structure; inference).

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
