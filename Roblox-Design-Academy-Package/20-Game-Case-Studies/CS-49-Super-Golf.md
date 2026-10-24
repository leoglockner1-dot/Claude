---
title: "CS-49 — Super Golf! (charge-and-release with a map builder)"
tags: [case-study, sports, charge-release, ugc, party]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-49 — Super Golf! (charge-and-release with a map builder)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [Super Golf!](https://www.roblox.com/games/4468711919/) · universe 1424449565 · by Nosniy Games |
| Genre (Roblox) | Sports & Racing / Sports · max 20 players per server |
| Concurrent players at capture | 430 |
| Visits · favourites | 257,434,242 · 990,805 (3.85 per 1k visits) |
| Like ratio | 80% (318,133 up / 80,490 down) |
| Created / updated | 2019-11-29 / 2026-09-21 |
| Game passes for sale | 9 · 299–699 R$ (median 399) · e.g. More Cheers! (399), Custom Hats! (699), More Hats! (399), More Colors! (299), Invisible! (399), Gem Rewards! (399), More Effects! (399), VIP! (499) |

**Developer description (excerpt):** "🚨 NEW CODE AT 350K LIKES! 👍 Use code "wow_300k_likes" for a special reward! ⛳ Welcome to Super Golf! Play against others on a variety of exciting courses, unlock cool rewards, customize your ball, and compete to be the best player! 🔨 Use the Map Builder to create your very own golf courses and play them with your friends! ⭐️ …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Play golf against others on varied courses; build your own courses with the Map Builder. |
| Main action | [DEV] Click and drag to charge, release to shoot; mobile slider. |
| Immediate feedback | [INF] Ball flight, strokes counter. |
| Reward → new possibility | [DEV] Least strokes wins; unlock cosmetics; vote for next map/mode. |
| Micro loop (seconds) | [DEV] **Charge-and-release** aim/power skill. |
| Core loop (minutes) | [DEV] play hole → strokes → next hole → vote next map. |
| Meta loop (days) | [DEV] Map Builder (UGC), customization; [DATA] cosmetic passes (hats, colours, cheers). |

## First-time experience
[DEV] 4-step how-to-play with per-device controls.

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | A classic **charge-release** mechanic with UGC maps and voting (players choose content). |
| Weakest part / quit risks | [DATA] 80% likes, 430 CCU (small now). |
| Essential features | Charge-release shot, courses, turn order. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | One hole, drag-to-charge, stroke counter; test if players try "one more shot". |

## Reusable lessons
- Charge-and-release maps naturally to mouse, touch (slider) and gamepad.
- Map voting gives players agency and surfaces the best UGC.

## Original application (do not copy the game)
Paper-plane golf through a city of skyscrapers; wind shifts per hole.

## Confidence
Medium.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
