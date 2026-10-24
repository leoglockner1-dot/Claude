---
title: "CS-42 — Epic Minigames (142 minigames + board-game meta mode)"
tags: [case-study, party, minigames, variety, social]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-42 — Epic Minigames (142 minigames + board-game meta mode)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [[🎃] Epic Minigames](https://www.roblox.com/games/277751860/) · universe 110181652 · by Typical Games |
| Genre (Roblox) | Party & Casual / Minigame · max 12 players per server |
| Concurrent players at capture | 1,883 |
| Visits · favourites | 2,360,779,050 · 8,625,023 (3.65 per 1k visits) |
| Like ratio | 91% (2,273,733 up / 236,211 down) |
| Created / updated | 2015-07-29 / 2026-10-23 |
| Game passes for sale | 10 · 99–899 R$ (median 299) · e.g. VIP (499), Private Server Powers (899), Double Coins (299), Play Rewards Plus (299), Second Pet (99), Second Effect (99), Illumina (149), x4 Controller Chance (249) |

**Developer description (excerpt):** "Welcome to Epic Minigames, the game where you can enjoy a collection of 142 unique and exciting minigames! 🕹️ Level up and earn coins by winning rounds, and spend your coins on gear, pets, effects, and other fun stuff for your character. 🌟 As well as the main minigame mode, there's also Epic Party 🎲, a board game where you can …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] A collection of 142 unique minigames; win rounds for coins; Epic Party is a board game with friends or strangers. |
| Main action | [INF] Varies per minigame. |
| Immediate feedback | [INF] Round winner announcements. |
| Reward → new possibility | [DEV] Levels and coins → gear, pets, effects. |
| Micro loop (seconds) | [INF] Changes every round. |
| Core loop (minutes) | [INF] minigame → results → next minigame. |
| Meta loop (days) | [DEV] Levels, cosmetics, a **board-game mode** that wraps minigames in a longer arc. |

## First-time experience
[INF] Each minigame must teach itself in seconds.

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | **Variety as the core** (142 minigames) plus a board-game wrapper that gives a session-long goal; [DATA] created 2015, 91% likes, high favourites/1k (3.65). |
| Weakest part / quit risks | [DATA] Low current CCU (1,883); [INF] uneven quality across many minigames. |
| Essential features | Fast minigame rotation, self-explaining rules. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | 5 minigames with 10-second rule cards, rotating; test if players stay for 10 rounds. |

## Reusable lessons
- A **meta-structure** (board game, tournament) turns a playlist into a story.
- Every minigame needs a 1-line rule + visual demo.

## Original application (do not copy the game)
Minigame road trip: each stop on a map is a minigame; the winner chooses the next route.

## Confidence
Medium.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
