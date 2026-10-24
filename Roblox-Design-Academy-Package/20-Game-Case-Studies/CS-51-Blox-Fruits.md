---
title: "CS-51 — Blox Fruits (long RPG progression with collectible powers)"
tags: [case-study, rpg, progression, collection, combat]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-51 — Blox Fruits (long RPG progression with collectible powers)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [Blox Fruits](https://www.roblox.com/games/2753915549/) · universe 994732206 · by Gamer Robot Inc |
| Genre (Roblox) | RPG / Action RPG · max 12 players per server |
| Concurrent players at capture | 149,752 |
| Visits · favourites | 65,087,508,922 · 20,122,519 (0.31 per 1k visits) |
| Like ratio | 92% (12,788,762 up / 1,068,372 down) |
| Created / updated | 2019-01-16 / 2026-10-22 |
| Game passes for sale | 6 · 350–2700 R$ (median 450) · e.g. Dark Blade (1200), 2x Money (450), 2x Mastery (450), Fruit Notifier (2700), Fast Boats (350), 2x Boss Drops (350) |

**Developer description (excerpt):** "OUT NOW: 🧲 Magnet + 🏝️ Sea 1 + MORE Welcome to Blox Fruits! Become a master swordsman or a powerful blox fruit user as you train to become the strongest player to ever live. You can choose to fight against tough enemies or have powerful boss battles while sailing across the ocean to find hidden secrets. Current level cap: 3000 …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Become a master swordsman or a blox-fruit user; train to become the strongest; fight bosses; sail to find secrets. |
| Main action | [INF] Fight NPCs/bosses, quest, sail. |
| Immediate feedback | [INF] Combat VFX, level-ups. |
| Reward → new possibility | [DEV] Levels (cap 3000), fruits with distinct powers (long list in the description). |
| Micro loop (seconds) | [INF] Combat skills of the equipped fruit/style. |
| Core loop (minutes) | [INF] quest → fight → level → stronger area/sea. |
| Meta loop (days) | [DEV] Fruit collection (each a different moveset), seas, level cap 3000; [DATA] passes: Fruit Notifier (2,700), 2x Money/Mastery (450), Dark Blade (1,200). |

## First-time experience
[INF] Pick a style/fruit; start questing. *Not observed.*

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | **Collectible powers that change the moveset** (not just stats) plus a very long level ladder; [DATA] 65B visits, 92% likes. |
| Weakest part / quit risks | [INF] Very long grind; powerful paid items. |
| Essential features | Combat, quests, fruits as movesets, seas. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | 2 fruits with different movesets, 1 island of NPCs, 5 levels; test which fruit players prefer and why. |

## Reusable lessons
- Unlocks that **change how you play** sustain a long ladder better than stat increases.

## Original application (do not copy the game)
Weather mages: each collected cloud gives a new spell set (fog step, lightning dash); islands require specific weather.

## Confidence
Medium-low.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
