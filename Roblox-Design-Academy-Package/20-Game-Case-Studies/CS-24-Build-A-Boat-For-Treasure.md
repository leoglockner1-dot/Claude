---
title: "CS-24 — Build A Boat For Treasure (sandbox building tested by a gauntlet)"
tags: [case-study, sandbox, building, physics, creativity]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-24 — Build A Boat For Treasure (sandbox building tested by a gauntlet)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [Build A Boat For Treasure](https://www.roblox.com/games/537413528/) · universe 210851291 · by Chillz Studios |
| Genre (Roblox) | Simulation / Sandbox · max 7 players per server |
| Concurrent players at capture | 13,641 |
| Visits · favourites | 5,237,858,368 · 8,555,325 (1.63 per 1k visits) |
| Like ratio | 93% (3,667,135 up / 259,704 down) |
| Created / updated | 2016-11-02 / 2026-10-09 |
| Game passes for sale | 4 · 250–500 R$ (median 250) · e.g. Gold Multiplier (500), Penguin Character (250), Fox Character (250), Chicken Character (250) |

**Developer description (excerpt):** "Build your ship and set sail for your adventure! Liked the game? Don't forget to leave a Thumbs Up(👍) and Favorite(🌟) . Thank you! Don't forget to check out our group! https://www.roblox.com/My/Groups.aspx?gid=2782840 Group Perks: ✨Member✨ --- 25% more gold! 💫Mega Member💫 --- 300% more health! --- 25% more gold! 🌟Royal Member🌟 …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Build your ship and set sail for your adventure. |
| Main action | [INF] Place blocks to build a boat; launch it down a river of obstacles. |
| Immediate feedback | [INF] Physics: the boat survives, breaks or sinks; distance reached. |
| Reward → new possibility | [INF] Gold by distance/treasure → more and better blocks; [DEV] group perks give more gold/health/TNT. |
| Micro loop (seconds) | [INF] Placement decisions (building) and steering/surviving (voyage). |
| Core loop (minutes) | [INF] build → launch → see how far you get → earn gold → buy blocks → rebuild better. |
| Meta loop (days) | [INF] Creative expression, sharing builds, completing the course; characters sold as passes (250 R$ each). |

## First-time experience
[INF] Building tools need teaching; first voyage likely fails fast, which is part of the fun. *Not observed.*

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | **Player creativity is the content**, and the voyage gives creativity a concrete test (does my design survive?). Long-lived: created 2016, 93% likes. |
| Weakest part / quit risks | [INF] Building UI complexity for new/mobile players; physics edge cases. |
| Essential features | Free-form build, physics test course, block economy. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | 10 block types, a 3-obstacle course, gold by distance; test whether players rebuild after the first failure. |

## Reusable lessons
- Give creative tools a **test** with stakes; expression plus evaluation beats either alone.
- Failure that is funny (sinking, breaking) invites retries.

## Original application (do not copy the game)
Build a balloon basket from parts and drift across a stormy canyon; wind gusts test balance and lift.

## Confidence
Low–medium: description is minimal; loop inferred from title and passes.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
