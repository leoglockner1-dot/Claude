---
title: "CS-37 — Dead Rails (co-op train journey through a zombie desert)"
tags: [case-study, survival, co-op, journey, horror]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-37 — Dead Rails (co-op train journey through a zombie desert)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [[👻EVENT] Dead Rails ](https://www.roblox.com/games/116495829188952/) · universe 7018190066 · by RCM Games |
| Genre (Roblox) | Adventure / Exploration · max 16 players per server |
| Concurrent players at capture | 33,148 |
| Visits · favourites | 6,616,933,561 · 6,153,337 (0.93 per 1k visits) |
| Like ratio | 93% (3,353,012 up / 269,517 down) |
| Created / updated | 2025-01-01 / 2026-10-24 |
| Game passes for sale | 4 · 95–175 R$ (median 148) · e.g. Tommy Gun (175), +5 Storage (95), Mauser C96 (148), Sawed-Off Shotgun (148) |

**Developer description (excerpt):** "In 1899, a mysterious virus swept the American continent. Dubbed the ‘Zombie Plague’, a cure was discovered in Mexico. Gather your friends and board your trains to fight through the zombie-infested desert."

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] In 1899, a zombie plague; a cure in Mexico. Gather friends and fight through the desert on trains. |
| Main action | [INF] Fuel and drive the train, scavenge stops, fight zombies. |
| Immediate feedback | [INF] Train progress, combat, resource gains. |
| Reward → new possibility | [INF] Distance → closer to the cure (the ending); [DATA] weapon/storage passes (Tommy Gun 175, +5 Storage 95). |
| Micro loop (seconds) | [INF] Combat and resource choices at stops. |
| Core loop (minutes) | [INF] travel → stop → scavenge/fight → refuel → travel (run-based). |
| Meta loop (days) | [INF] Run completion, weapons/classes; events. |

## First-time experience
[DEV] The premise gives a clear destination (cure in Mexico) from the first line.

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | A **journey with a destination** frames every action; co-op roles on a shared vehicle; [DATA] 93% likes. |
| Weakest part / quit risks | [INF] Run failure late in a journey can sting; weapon passes may imbalance. |
| Essential features | Moving base (train), stops, threat. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | A train on a short track, 2 stops, zombies, fuel; test whether groups divide roles. |

## Reusable lessons
- A **moving base** creates constant forward pressure and a natural run structure.
- A destination in the premise answers "what am I doing" instantly.

## Original application (do not copy the game)
A riverboat delivering medicine down a haunted river; each town stop offers fuel, crew or danger.

## Confidence
Medium-low.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
