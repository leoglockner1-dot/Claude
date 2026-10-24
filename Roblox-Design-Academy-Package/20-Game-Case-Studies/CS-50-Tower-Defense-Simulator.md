---
title: "CS-50 — Tower Defense Simulator (co-op TD with unit collection and live events)"
tags: [case-study, strategy, tower-defense, co-op, collection, live-ops]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-50 — Tower Defense Simulator (co-op TD with unit collection and live events)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [[🌙 NIGHT 3] Tower Defense Simulator](https://www.roblox.com/games/3260590327/) · universe 1176784616 · by Paradoxum Games |
| Genre (Roblox) | Strategy / Tower Defense · max 50 players per server |
| Concurrent players at capture | 17,540 |
| Visits · favourites | 5,038,139,590 · 3,530,680 (0.7 per 1k visits) |
| Like ratio | 94% (2,084,564 up / 129,588 down) |
| Created / updated | 2019-06-05 / 2026-10-23 |
| Game passes for sale | 21 · 55–7999 R$ (median 449) · e.g. 🌽🍂 Harvester [LIMITED TIME] (799), [LIMITED TIME] Slasher (499), 👑 VIP 👑 (375), ## [LIMITED] Executioner (799), 🔧 Engineer (1690), 💻 Hacker 💻 (2249), ⚙️ Sandbox Plus+ ⚙️ (7999), 🎯[FPS MODE] Gatling Gun! (1949) |

**Developer description (excerpt):** "💜 Thank you for 2 MILLION likes! Use code 2MILLION for a free Mercenary Pursuit skin! Place units to defend against hordes of zombies! Team up with friends and face against even stronger bosses to unlock new units! 👥💵 Join the Paradoxum Games group for +$100 starting cash! 👍 Thumbs up and favorite for more quality updates! 🌟 …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Place units to defend against hordes of zombies; team up and face stronger bosses to unlock new units. |
| Main action | [DEV] Place and upgrade units along a path. |
| Immediate feedback | [INF] Waves, enemy deaths, base HP. |
| Reward → new possibility | [DEV] Unlock new units; [DATA] 21 passes incl. limited-time units (Harvester, Slasher, Executioner 499–799). |
| Micro loop (seconds) | [INF] Placement and upgrade timing decisions. |
| Core loop (minutes) | [INF] match: waves → earn → place/upgrade → boss → win/lose. |
| Meta loop (days) | [DEV] Unit collection, battlepass, story chapters ("Solar Requiem Night I–III"), crates; versioned releases. |

## First-time experience
[DEV] Group join gives +$100 starting cash (incentive).

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | **Strategic placement decisions** each wave; co-op against bosses; unit roster as long-term goal; [DATA] 94% likes. |
| Weakest part / quit risks | [INF] Limited-time paid units can create pay-to-win perception and FOMO. |
| Essential features | Path, placement, upgrades, waves. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | One path, 3 unit types, 5 waves; test whether players change strategy after a loss. |

## Reusable lessons
- TD is a **decision** game: each wave should ask a new placement question.
- Episodic events ("Night I–III") create anticipation across weeks.

## Original application (do not copy the game)
Garden defense against snails using sprinklers, salt lines and ladybugs; weather changes snail behaviour.

## Confidence
Medium.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
