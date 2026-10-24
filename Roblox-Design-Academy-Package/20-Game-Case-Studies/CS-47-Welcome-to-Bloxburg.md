---
title: "CS-47 — Welcome to Bloxburg (build + life sim + jobs)"
tags: [case-study, roleplay, life-sim, building, jobs]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-47 — Welcome to Bloxburg (build + life sim + jobs)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [[🏚️] Welcome to Bloxburg ](https://www.roblox.com/games/185655149/) · universe 88070565 · by Bloxburg Development |
| Genre (Roblox) | Roleplay & Avatar Sim / Life · max 12 players per server |
| Concurrent players at capture | 25,583 |
| Visits · favourites | 10,143,698,948 · 14,027,015 (1.38 per 1k visits) |
| Like ratio | 88% (5,645,758 up / 733,953 down) |
| Created / updated | 2014-11-04 / 2026-10-22 |
| Game passes for sale | 8 · 100–600 R$ (median 300) · e.g. Multiple Floors (360), Transform Plus (600), Advanced Placing (250), Large Plot (250), Premium (300), Excellent Employee (300), Basements (100), Marvelous Mood (180) |

**Developer description (excerpt):** "👋 Welcome to the town of Bloxburg, where you can be anything you want to be! 🏡 Build and decorate, or buy the house or creation of your dreams! 👕 Customize your character with outfits and roles! 🎭 Roleplay with friends using interactive items and emotes! 💼 Choose a job and earn money + rewards as you work! 🚗 Select one of many …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Build and decorate your house, choose a job, level skills, roleplay. |
| Main action | [DEV] Build, work jobs, drive, roleplay with items/emotes. |
| Immediate feedback | [INF] Earnings, skill level ups, house changes. |
| Reward → new possibility | [DEV] Money and skill levels unlock content; [DATA] passes extend building (Multiple Floors 360, Advanced Placing 250, Large Plot 250). |
| Micro loop (seconds) | [INF] Building/placement decisions; job tasks. |
| Core loop (minutes) | [DEV] work → earn → build → (roleplay in the result). |
| Meta loop (days) | [DEV] Skills (e.g. cooking), creations, roleplay. |

## First-time experience
[INF] Building tools need teaching. *Not observed.*

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | **Players create the venue for their own roleplay**; building passes monetize creative scope. |
| Weakest part / quit risks | [INF] Building is time-intensive; mobile complexity. |
| Essential features | Build mode, jobs, skills. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | Small plot build mode + one job; test whether players invite others to see their house. |

## Reusable lessons
- Build tools + a reason to show the result (visitors, roleplay) = a self-sustaining social loop.

## Original application (do not copy the game)
Treehouse village: build platforms in giant trees; neighbours connect rope bridges.

## Confidence
Medium.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
