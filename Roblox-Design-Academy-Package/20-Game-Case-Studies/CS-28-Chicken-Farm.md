---
title: "CS-28 — Chicken Farm (merge + offline idle; very high like ratio)"
tags: [case-study, tycoon, merge, idle, offline-progress]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-28 — Chicken Farm (merge + offline idle; very high like ratio)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [Chicken Farm 🐣](https://www.roblox.com/games/137233438285284/) · universe 10209534490 · by Skandi Studios |
| Genre (Roblox) | Simulation / Tycoon · max 6 players per server |
| Concurrent players at capture | 2,440 |
| Visits · favourites | 129,611,808 · 410,740 (3.17 per 1k visits) |
| Like ratio | 99% (1,164,833 up / 12,367 down) |
| Created / updated | 2026-05-23 / 2026-10-24 |
| Game passes for sale | 4 · 29–799 R$ (median 499) · e.g. Auto Collect Eggs (79), Double Eggs (499), Auto Collect Money (29), Double Gems (799) |

**Developer description (excerpt):** "🐔 Welcome to Chicken Farm! 🥚 🐣 Buy Chickens and start farming! 💵 Convert Eggs into Cash 🔀 Merge Chickens to unlock rarer ones! 🥚 Build the ultimate Chicken Nest! 🌙 Your Chickens keep laying Eggs even while you're away! 💰 UPDATE 10: 🚀 Events 💎New Gem Upgrades 🍀New Lucky Block 🐓 Gold Chickens 🦵 Obby 🔄New Rebirth 📈2 new Buy Tiers …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Buy chickens, convert eggs to cash, merge chickens into rarer ones, build the ultimate nest; chickens keep laying offline. |
| Main action | [DEV] Buy chickens, collect eggs, merge chickens. |
| Immediate feedback | [INF] Merge results (new rarer chicken), egg piles. |
| Reward → new possibility | [DEV] Merging unlocks rarer chickens → higher egg value; [DEV] rebirth, gems, lucky blocks, events (Update 10). |
| Micro loop (seconds) | [DEV] Collect + merge decisions (which to merge, when). |
| Core loop (minutes) | [DEV] buy → lay eggs → sell → buy more → merge up. |
| Meta loop (days) | [DEV] Offline laying, rebirths, events. |

## First-time experience
[INF] Merge mechanics are self-explanatory once seen. *Not observed.*

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | [DATA] 99% like ratio (small sample relative to giants: 130M visits). Merge gives a tactile decision in an idle frame. |
| Weakest part / quit risks | [DATA] Passes automate collection (Auto Collect Eggs 79, Auto Collect Money 29), which removes the micro loop for payers. |
| Essential features | Merge, offline production, rebirth. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | 5 chicken tiers, merge, offline eggs; test if players return within 24 h. |

## Reusable lessons
- Merge is a cheap way to add a satisfying decision and visible upgrade to an idle loop.
- Cheap automation passes (29–79 R$) monetize impatience; be sure the remaining play still has decisions.

## Original application (do not copy the game)
Merge lanterns on a night market street; brighter lanterns attract more visitors overnight.

## Confidence
Medium (developer description explicit).

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
