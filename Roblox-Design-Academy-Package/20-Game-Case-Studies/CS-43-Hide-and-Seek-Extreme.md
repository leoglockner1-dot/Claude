---
title: "CS-43 — Hide and Seek Extreme (childhood game + asymmetric abilities)"
tags: [case-study, party, hide-and-seek, asymmetric, childhood-game]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-43 — Hide and Seek Extreme (childhood game + asymmetric abilities)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [Hide and Seek Extreme](https://www.roblox.com/games/205224386/) · universe 93740418 · by Tim7775 |
| Genre (Roblox) | Party & Casual / Childhood Game · max 14 players per server |
| Concurrent players at capture | 1,912 |
| Visits · favourites | 3,427,155,266 · 6,962,610 (2.03 per 1k visits) |
| Like ratio | 91% (989,601 up / 96,363 down) |
| Created / updated | 2015-01-18 / 2026-08-28 |
| Game passes for sale | 5 · 10–300 R$ (median 50) · e.g. The Yeti (50), Boombox (300), Seeker chance multiplier (100), Triple Coin Value (30), Donation (10) |

**Developer description (excerpt):** "Welcome to Hide and Seek Extreme. At the start of the game, one player gets chosen to be 'It'. 'It' has to try and find the other players. 'It' will not spawn with their default character, instead they will spawn with their equipped 'It' character. Every 'It' character has a special ability that can be used to help catch the …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] One player is "It" and must find the others; "It" characters have special abilities. |
| Main action | [DEV] Hide (hiders) or seek with an ability (press 1); taunt (T). |
| Immediate feedback | [INF] Found/caught moments. |
| Reward → new possibility | [DEV] "It" characters purchasable in the shop; [DATA] passes include a seeker chance multiplier (100) and boombox. |
| Micro loop (seconds) | [INF] Hiding spot choice vs seeking routes; abilities. |
| Core loop (minutes) | [INF] round: hide/seek → found or survive → next round. |
| Meta loop (days) | [DEV] Collect "It" characters. |

## First-time experience
[DEV] The rules are known from childhood; no tutorial needed.

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | **Known rules** + giant-scale maps (inferred from the "Extreme" framing) + ability variety; created 2015, 91% likes. |
| Weakest part / quit risks | [INF] Seeker chance multiplier pass affects role distribution. |
| Essential features | Hide/seek roles, big maps, abilities. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | One oversized room, 4 hiders, 1 seeker with one ability; test round tension. |

## Reusable lessons
- Childhood games are instant onboarding; add a twist (scale, abilities) for identity.

## Original application (do not copy the game)
Hide-and-seek in a toy box at mouse scale; the seeker is a cat with a "pounce" ability.

## Confidence
Medium.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
