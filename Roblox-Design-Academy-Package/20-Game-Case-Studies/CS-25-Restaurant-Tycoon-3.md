---
title: "CS-25 — Restaurant Tycoon 3 (weekly live ops on a management tycoon)"
tags: [case-study, tycoon, management, live-ops, building]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description + two developer DevForum posts; gameplay NOT observed"
---

# CS-25 — Restaurant Tycoon 3 (weekly live ops on a management tycoon)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [Restaurant Tycoon 3](https://www.roblox.com/games/119048529960596/) · universe 7094518649 · by Ultraw |
| Genre (Roblox) | Simulation / Tycoon · max 6 players per server |
| Concurrent players at capture | 8,342 |
| Visits · favourites | 384,305,386 · 920,340 (2.39 per 1k visits) |
| Like ratio | 95% (398,575 up / 19,680 down) |
| Created / updated | 2025-01-16 / 2026-10-24 |
| Game passes for sale | 9 · 249–1499 R$ (median 349) · e.g. Sandbox Mode (1499), Auto Money Collection (299), Allow Build Collisions (349), Glass Animals Bundle (399), Chip Shop Diva Bundle (349), Precision Build (599), 3x Customer Luck (399), 2x Item Limits (299) |

**Developer description (excerpt):** "🧑‍🍳Welcome to Restaurant Tycoon 3 [HOW TO PLAY] 👨Click to serve customers! 🍔Cook dishes for the customers! 🍝Build and upgrade your restaurant! 💵Your restaurant can literally make money while you're offline! 📂 Updates & Credits https://devforum.roblox.com/t/restaurant-tycoon-3/3670704 ⭐ What's changed since Restaurant Tycoon 2? …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Serve customers, cook dishes, build and upgrade your restaurant; it earns money while you are offline. |
| Main action | [DEV] Click to serve customers; cook dishes; place furniture and kitchen items. |
| Immediate feedback | [DEV] Customers show **emoji sentiments**; [DEV] eating and cooking animations; fires/burned food when unattended. |
| Reward → new possibility | [DEV] Money → kitchen tiers, more dishes (200+ dishes, 50+ cuisines), floors, workers. |
| Micro loop (seconds) | [DEV] Serving/cooking actions; [DEV] attention management (burning food). |
| Core loop (minutes) | [DEV] serve/cook → earn → expand/upgrade restaurant → unlock dishes via on-screen objectives. |
| Meta loop (days) | [DEV] **Weekly updates**: the developer's DevForum log lists dated updates almost every week from May 2025 to 2026-10-23 (≈70 entries): new dishes, events, customer types, franchising, offline earning. [DEV] Trophies, milestones, gifts between restaurants. |

## First-time experience
[DEV] RT3 added "community-designed starter restaurants" and on-screen **objectives** to unlock dishes, which suggests a structured first session. *Timings not observed.*

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | A **sustained weekly content cadence** documented by the developer; customization depth (walls, doors, windows, roofs, 3 colours per item) makes each restaurant personal. |
| Weakest part / quit risks | [INF] Complexity of building tools for new/mobile players; many systems (franchising, farming, drive-thru) may overwhelm. |
| Essential features | Customer service loop with readable sentiment, build mode, dish unlocks. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | One counter, 3 dishes, customers with patience + emoji, one upgrade; test whether players redesign the layout to serve faster. |

## Reusable lessons
- Readable NPC emotion (emoji sentiment) turns a spreadsheet into a story.
- A predictable update cadence is itself a meta loop: players return for "this week's thing".
- Starter templates reduce blank-canvas paralysis in building games.

## Original application (do not copy the game)
A bakery on a moving train: serve passengers at each station stop; redesign the carriage between stations.

## Confidence
Medium-high for systems (developer lists them); low for feel.

## Related
Developer posts: [Restaurant Tycoon 3 updates log](https://devforum.roblox.com/t/restaurant-tycoon-3/3670704) · [50 new features](https://devforum.roblox.com/t/50-new-features-in-restaurant-tycoon-3%E2%AD%90/3636102) · [Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md)
