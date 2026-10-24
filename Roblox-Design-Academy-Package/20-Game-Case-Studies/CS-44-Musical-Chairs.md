---
title: "CS-44 — Musical Chairs (simple childhood rule, mixed reception)"
tags: [case-study, party, childhood-game, elimination, weak-reception]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-44 — Musical Chairs (simple childhood rule, mixed reception)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [Musical Chairs 🎵🪑](https://www.roblox.com/games/113323927469374/) · universe 6688157118 · by Infinity Forge Interactive |
| Genre (Roblox) | Party & Casual / Childhood Game · max 14 players per server |
| Concurrent players at capture | 4,475 |
| Visits · favourites | 541,847,789 · 1,718,274 (3.17 per 1k visits) |
| Like ratio | 66% (61,366 up / 31,125 down) |
| Created / updated | 2024-10-18 / 2026-10-14 |
| Game passes for sale | 13 · 9–199 R$ (median 39) · e.g. Glitch Pack (39), Rainbow Pack (19), +25% Speed Boost (199), Space Pack (9), Galaxy Pack (19), Squid Pack (39), VIP! (149), Snow Pack (19) |

**Developer description (excerpt):** "🎵 Welcome to Musical Chairs! 🪑 Don't be the last one to find a seat! How to play: - Run around the chairs and find one when the music stops! If you don't, you're out! - The last person alive wins! 🪙 Earn coins to buy pets, trails, and chair skins! Premium users get extra coins every win! LIKE AND FAVORITE FOR NEW UPDATES AND …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Run around chairs; when the music stops, find a seat or you are out; last alive wins. |
| Main action | [DEV] Run and sit at the right moment. |
| Immediate feedback | [INF] Music stop, scramble, elimination. |
| Reward → new possibility | [DEV] Coins → pets, trails, chair skins; premium users get extra coins. |
| Micro loop (seconds) | [INF] Reaction timing + positioning. |
| Core loop (minutes) | [DEV] round: circle → music stops → sit → eliminate → repeat. |
| Meta loop (days) | [DEV] Cosmetics; [DATA] 13 passes from 9 R$, incl. "+25% Speed Boost" (199). |

## First-time experience
[DEV] Rules fully explained in the description.

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | Instantly understood rule; short rounds. |
| Weakest part / quit risks | [DATA] **66% like ratio**. [INF] Likely causes: a **speed boost pass in a speed-decided game** (pay-to-win in the core skill), early elimination means long waiting/spectating, little depth. *Not verified.* |
| Essential features | Music cue, chairs, elimination. |
| Possibly unnecessary | [INF] Speed boost pass. |
| Minimal prototype to test the idea | Compare two versions: with a speed pass vs none; and eliminated players play a side minigame while waiting. |

## Reusable lessons
- **Never sell an advantage in the exact skill that decides the round** ([CL-08](../23-Quality-Checklists/CL-08-Shop-and-Monetization-Ethics.md)).
- Elimination games need something for eliminated players to do.

## Original application (do not copy the game)
Musical umbrellas in a rainstorm: when thunder cracks, grab an umbrella; eliminated players control the wind.

## Confidence
Medium for the data; low for causes.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
