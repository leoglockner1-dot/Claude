---
title: "CS-54 — Dig to Escape (prison dig with night patrols; states its playtime)"
tags: [case-study, survival, escape, digging, trend]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-54 — Dig to Escape (prison dig with night patrols; states its playtime)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [⛏️Dig to Escape](https://www.roblox.com/games/92122513197996/) · universe 9145063979 · by Breakout Funs |
| Genre (Roblox) | Survival / Escape · max 14 players per server |
| Concurrent players at capture | 5,739 |
| Visits · favourites | 606,422,702 · 636,442 (1.05 per 1k visits) |
| Like ratio | 98% (1,139,846 up / 26,021 down) |
| Created / updated | 2025-11-10 / 2026-10-10 |
| Game passes for sale | 2 · 395–695 R$ (median 695) · e.g. OP DRILL [PERMANENT] (695), X-RAY GOGGLES [PERMANENT] (395) |

**Developer description (excerpt):** "😨 Oh no, you got arrested! Now you’re stuck in a prison with no way out... or is there? ⛏️Rumor says there's a secret tunnel under the prison. Dig down to find it and escape. 👮‍♂️ But be careful, the Guard patrols at night... ⏰ AVERAGE Playtime is 30-60m+ 🎵 CHASE MUSIC by PENACORE"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] You are arrested; dig down to a secret tunnel and escape, but the guard patrols at night. |
| Main action | [INF] Dig, hide the tunnel, avoid the guard. |
| Immediate feedback | [INF] Depth progress, guard proximity. |
| Reward → new possibility | [INF] Escape; [DATA] passes: OP Drill (695), X-Ray Goggles (395) - permanent tools. |
| Micro loop (seconds) | [INF] Dig vs risk timing. |
| Core loop (minutes) | [INF] dig → hide/avoid patrol → dig deeper → escape. |
| Meta loop (days) | [DEV] "AVERAGE Playtime is 30-60m+" - a finite experience. |

## First-time experience
[DEV] Premise and goal in 3 lines.

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | **A concrete goal + risk** (patrol) + a finite promise ("30–60 min") sets expectations; [DATA] **98% likes**. |
| Weakest part / quit risks | [INF] Finite story = low long-term retention by design; tool passes shorten the experience. |
| Essential features | Dig progress, patrol threat, hiding. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | One cell, one patrol bot with a schedule, a 20-block dig; test tension and completion. |

## Reusable lessons
- Stating the session length is a promise that can raise satisfaction for finite games.
- Risk/reward timing (dig while unseen) makes a simple verb tense.

## Original application (do not copy the game)
Escape a museum by night: move exhibits to build a path to a skylight while the night guard makes rounds.

## Confidence
Medium.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
