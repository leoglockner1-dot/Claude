---
title: "CS-22 — Fisch (skill-based fishing micro loop + exploration)"
tags: [case-study, simulator, fishing, skill, exploration, collection]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-22 — Fisch (skill-based fishing micro loop + exploration)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [Fisch 👻 [HORSEMAN]](https://www.roblox.com/games/16732694052/) · universe 5750914919 · by Fisching |
| Genre (Roblox) | Simulation / – · max 20 players per server |
| Concurrent players at capture | 85,071 |
| Visits · favourites | 5,061,189,162 · 3,700,822 (0.73 per 1k visits) |
| Like ratio | 91% (3,070,443 up / 310,728 down) |
| Created / updated | 2024-03-13 / 2026-10-24 |
| Game passes for sale | 9 · 99–499 R$ (median 239) · e.g. Enchant Anywhere (239), Double XP (239), Sell Anywhere (399), Spawn Boat Anywhere (299), Supporter (169), Appraise Anywhere (499), Appraisers Luck (299), Emote Pack (99) |

**Developer description (excerpt):** "🦈 Welcome to Fisch 🦈 Dive into Fisch, the ultimate fishing adventure where exploration and progression are yours to control. Cast your line to catch rare and unique fish, each with 400,000+ possible variations. Explore a growing world with your trusty rod, and maybe even reel in some new friends along the way! [How To Fish] • …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Cast your line, catch rare fish (400,000+ variations), explore a growing world with your rod. |
| Main action | [DEV] Hold to cast → wait for a bite (optionally "shake" to attract) → hold/click to keep a white bar on the moving blue line until the progress bar fills. |
| Immediate feedback | [DEV] Progress bar filling; [INF] tension when the line drifts; catch reveal. |
| Reward → new possibility | [DEV] Rare/unique fish → [INF] money for rods/boats → new waters. |
| Micro loop (seconds) | [DEV] A **tracking skill game** (keep the bar on the line); "it's okay to mess up a few times" - forgiving. |
| Core loop (minutes) | [INF] travel to a spot → cast → reel minigame → sell/keep → upgrade rod/boat → new locations. |
| Meta loop (days) | [DEV] Huge variation space (collection), exploration of a growing world; [DATA] passes sell convenience (Sell Anywhere 399, Spawn Boat Anywhere 299, Enchant Anywhere 239, Double XP 239). |

## First-time experience
[DEV] The description teaches the exact controls in 4 steps. [INF] The first catch is likely within the first minute. *Not observed.*

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | The **micro loop has skill** (tracking) with forgiveness; collection + exploration give long goals. Convenience passes remove travel friction rather than gating content. |
| Weakest part / quit risks | [INF] The same minigame repeated hundreds of times; depth must come from rods/conditions/locations changing the minigame. Cannot verify. |
| Essential features | Reel minigame, rarity, locations, rod upgrades. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | One pond, one rod, the reel minigame with 3 fish difficulties; test if players do 20 casts voluntarily. |

## Reusable lessons
- A simple, readable skill micro loop with forgiveness keeps grinding active instead of idle.
- Sell **convenience** (anywhere-actions) rather than power to keep the core fair.
- Variation (sizes, mutations) multiplies a modest content list into a huge collection.

## Original application (do not copy the game)
A beekeeper smoker game: calm a swarm by matching breath rhythm on a bar; calmer swarms give rarer honey; travel to new meadows.

## Confidence
Medium-high for the micro loop (developer documents controls); medium otherwise.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
