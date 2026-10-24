---
title: "CS-33 — Webbed! (physical tether co-op)"
tags: [case-study, obby, co-op, physics, tether]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-33 — Webbed! (physical tether co-op)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [Webbed! ❄️ [2 Player Obby]](https://www.roblox.com/games/132586479415502/) · universe 7364297396 · by studio arsenic |
| Genre (Roblox) | Obby & Platformer / – · max 12 players per server |
| Concurrent players at capture | 3,487 |
| Visits · favourites | 472,556,829 · 694,072 (1.47 per 1k visits) |
| Like ratio | 87% (109,264 up / 16,817 down) |
| Created / updated | 2025-03-11 / 2026-07-04 |
| Game passes for sale | 0 · e.g. none listed for sale (developer products are not visible through this API) |

**Developer description (excerpt):** "⚠️THIS GAME IS MADE FOR 2 PLAYERS⚠️ The two spiders 🕷️ have become webbed together 🕸️, and only through teamwork can they overcome the tricky terrains ahead. In this 2-player obby, each spider can cling to walls and swing across gaps by shooting their web. 🎁 LIKE AND JOIN THE GROUP FOR A FREE REVIVE 🎁 🛠 If you experience lag, …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Two spiders webbed together overcome tricky terrain; each can cling to walls and swing by shooting webs. |
| Main action | [DEV] Cling, shoot web, swing; [INF] coordinate the tether. |
| Immediate feedback | [INF] Physical pull between partners; swings. |
| Reward → new possibility | [INF] Stage progress; [DEV] free revive for liking/joining the group. |
| Micro loop (seconds) | [DEV] Physics movement + coordination. |
| Core loop (minutes) | [INF] traverse stage together → checkpoint → next. |
| Meta loop (days) | [INF] Completion, playing with a friend. |

## First-time experience
[DEV] "THIS GAME IS MADE FOR 2 PLAYERS" up front; [DEV] recommends free private servers if laggy.

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | The **tether makes cooperation physical**: you feel your partner's mistakes, which is funny rather than blocking. 87% likes vs Be My Camera's 58% [DATA] in the same co-op obby niche. |
| Weakest part / quit risks | [INF] Physics latency in public servers (developer acknowledges lag, suggests private servers). |
| Essential features | Tether physics, web swing, 2-player stages. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | Two tethered capsules, one swing mechanic, 3 gaps; test laughter/retry rate in pairs. |

## Reusable lessons
- Shared physical constraints make co-op failure **funny** instead of frustrating; compare with role dependency in [CS-31](CS-31-Teamwork-Puzzles.md)/[CS-32](CS-32-Be-My-Camera.md).
- Be honest about requirements ("made for 2 players") to filter the audience.

## Original application (do not copy the game)
Two balloons tied by a string drifting through a windy canyon; each can inflate/deflate to steer.

## Confidence
Medium.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
