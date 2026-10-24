---
title: "CS-40 — Arsenal (gun-game progression inside every match)"
tags: [case-study, competitive, shooter, arcade, progression-per-match]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-40 — Arsenal (gun-game progression inside every match)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [Arsenal](https://www.roblox.com/games/286090429/) · universe 111958650 · by ROLVe |
| Genre (Roblox) | Shooter / Deathmatch Shooter · max 16 players per server |
| Concurrent players at capture | 3,431 |
| Visits · favourites | 6,321,209,086 · 11,525,820 (1.82 per 1k visits) |
| Like ratio | 89% (5,126,988 up / 665,971 down) |
| Created / updated | 2015-08-18 / 2026-10-22 |
| Game passes for sale | 5 · 245–725 R$ (median 395) · e.g. Day of the Dead Bundle (395), VIP (395), Nexus Bundle (725), Primus the Knight Bundle (245), Bugs & Beasts Bundle (495) |

**Developer description (excerpt):** "Race to the top through a massive Arsenal of weapons! Conquer the day in fast paced arcade gameplay, from bazookas to spell books, each weapon will keep you guessing on what's next! Earn BattleBucks and trick out your game with a huge cast of characters, melees, kill effects, skins and more! Join the ROLVe group for an in-game …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Race to the top through a massive arsenal of weapons; each weapon keeps you guessing. |
| Main action | [INF] Shoot; each kill advances you to the next weapon. |
| Immediate feedback | [INF] Kill effects, weapon swap. |
| Reward → new possibility | [DEV] Next weapon (in-match progression), BattleBucks → cosmetics (characters, melees, kill effects, skins). |
| Micro loop (seconds) | [INF] Aim and adapt to each new weapon. |
| Core loop (minutes) | [INF] match: kill → weapon changes → race to the final weapon. |
| Meta loop (days) | [DEV] Cosmetics; group perk +25% BattleBucks/XP. |

## First-time experience
[INF] Instantly legible: shoot, progress, win.

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | **Progression happens within the match** (weapon ladder), so every kill changes your situation; cosmetics-only meta keeps fairness. |
| Weakest part / quit risks | [DATA] 3,431 CCU now (vs historic reach 6.3B visits): [INF] aging; the genre now has newer competitors (e.g. RIVALS, [CS-02](CS-02-RIVALS.md)). |
| Essential features | Weapon ladder, fast respawns. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | 5-weapon ladder in a small arena; test if players stay for 3 matches. |

## Reusable lessons
- In-match progression (ladders, upgrades) makes short sessions feel like a full arc.
- Cosmetic-only monetization preserves competitive trust.

## Original application (do not copy the game)
A water-balloon ladder: each splash upgrades your launcher; final tier is a single giant balloon.

## Confidence
Medium-low.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
