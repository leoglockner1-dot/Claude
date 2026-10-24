---
title: "CS-38 — Evade (movement-mastery survival vs Nextbots)"
tags: [case-study, survival, movement, parkour, rounds]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-38 — Evade (movement-mastery survival vs Nextbots)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [[1.5x 🎃HLWN] Evade ](https://www.roblox.com/games/9872472334/) · universe 3647333358 · by Hexagon Development Community |
| Genre (Roblox) | Survival / – · max 15 players per server |
| Concurrent players at capture | 56,695 |
| Visits · favourites | 9,371,779,501 · 8,601,786 (0.92 per 1k visits) |
| Like ratio | 94% (3,272,995 up / 212,612 down) |
| Created / updated | 2022-06-10 / 2026-10-24 |
| Game passes for sale | 26 · 100–1200 R$ (median 500) · e.g. [❗LIMITED RETURN❗] Eclipse Set (500), 🐱 Glorp Cat Set 👽 (500), 🎵💪 Music Carry Pack 2 (350), 🎵 Music Emotes Pack 2 (500), 🎵 Music Emotes Pack 1 (500), RELICS Boombox (300), 🎵💪 Music Carry Pack 1 (350), +6 Emote Slots (300) |

**Developer description (excerpt):** "🎃 The Halloween Event is out! Collect Wisps and Spellbooks to purchase exclusive themed items! 📜 New Weekly missions that grant exotic items and currencies! 🎟️New Voucher currency, use it for quick revives and respawns 🖥️ Newly Revamped Shop, Battlepass, Settings, and Community UI 🛠️New Deployable and Utility upgrades, enhance …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] An action parkour game where movement is the key to surviving the Nextbots. |
| Main action | [DEV] Move/parkour, interact, use items, emote; revive teammates. |
| Immediate feedback | [INF] Chase intensity, near misses. |
| Reward → new possibility | [DEV] Event currencies, weekly missions, battlepass, item upgrades with tokens/XP. |
| Micro loop (seconds) | [DEV] **Movement skill** under pressure. |
| Core loop (minutes) | [INF] round: survive pursuers → revive others → extract/round end. |
| Meta loop (days) | [DEV] Weekly missions, battlepass, collectables with lore, deployable upgrades; [DATA] 26 passes (cosmetic sets/emotes). |

## First-time experience
[DEV] Clear: press Play; controls listed. [DEV] Warning for flashing lights and loud sounds.

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | A skill ceiling in movement gives mastery for veterans while rounds stay readable for newcomers; [DATA] 94% likes. |
| Weakest part / quit risks | [INF] New players vs movement experts in the same round; cosmetics-heavy pass list. |
| Essential features | Movement tech, pursuers, revives. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | One arena, 2 pursuers with simple pathing, slide+jump movement; test survival time progression over 5 rounds. |

## Reusable lessons
- Movement mastery is a deep, content-cheap progression (players get better, not numbers).
- Revives add a co-op layer to a survival loop.

## Original application (do not copy the game)
A rooftop chase where umbrellas glide and wall-runs chain; pursuers are paper lanterns that speed up in darkness.

## Confidence
Medium.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
