---
title: "CS-23 — Mining Simulator 2 (a declining incremental — what is left when updates stop)"
tags: [case-study, simulator, incremental, decline, live-ops]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-23 — Mining Simulator 2 (a declining incremental — what is left when updates stop)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [Mining Simulator 2](https://www.roblox.com/games/9551640993/) · universe 3558292888 · by Rumble Studios |
| Genre (Roblox) | Simulation / Incremental Simulator · max 12 players per server |
| Concurrent players at capture | 25 |
| Visits · favourites | 210,827,910 · 517,277 (2.45 per 1k visits) |
| Like ratio | 93% (352,195 up / 25,727 down) |
| Created / updated | 2022-05-05 / 2026-08-26 |
| Game passes for sale | 15 · 79–3499 R$ (median 499) · e.g. More Teams! (229), Fast Hatch (749), Triple Hatch (749), Teleporter (174), Stronger Pickaxe (399), Small Storage (79), Omega Scythe (3499), Omega Nuke (549) |

**Developer description (excerpt):** "The Cleanup Update for Mining Simulator 2 is here! ⚙️ Removed Christmas Event + Decorations! 🥚 Added Magma Mystery Egg! 🍀 Added Season 20 Mining Pass! Welcome to Mining Simulator 2! ⛏️ 💎 Explore the depths of the mines to discover rare materials and ores to sell! Upgrade your backpack and tools to gather more resources. A game …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Explore the depths, mine rare ores, sell them, upgrade backpack and tools. |
| Main action | [INF] Click/hold to mine blocks; return to sell. |
| Immediate feedback | [INF] Ore counter, backpack capacity fill. |
| Reward → new possibility | [DEV] Money → bigger backpack/better tools → deeper ores; [DATA] eggs/pets ("Magma Mystery Egg") and a season pass. |
| Micro loop (seconds) | [INF] Mine adjacent blocks; low skill. |
| Core loop (minutes) | [DEV] mine → sell → upgrade backpack/tool → go deeper. |
| Meta loop (days) | [DEV] Season pass ("Season 20 Mining Pass"), eggs; [DATA] 15 passes 79–3,499 R$ (Fast Hatch, Triple Hatch, Teleporter, More Teams). |

## First-time experience
[INF] Classic mine→sell loop is instantly legible. *Not observed.*

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | [DATA] Historic reach (210M visits, 517k favourites, 93% likes) shows the classic mine-sell-upgrade loop works for a time. |
| Weakest part / quit risks | [DATA] **Only 25 concurrent players at capture**; last update 2026-08-26 is described as a "Cleanup Update" that *removed* a Christmas event. [INF] When live content stops, a pure number-growth loop has little to hold players; 2.45 favourites per 1k visits shows players once committed. |
| Essential features | Backpack-limit return trips, depth-gated ores. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | (For learning) Compare: one mine with depth gates vs the same mine plus a weekly rotating "event ore": which retains a test group longer? |

## Reusable lessons
- Favourites and like ratio record **past** satisfaction; CCU and update dates show **current** health. Always read both.
- Incremental loops whose novelty comes from events need a sustainable update cadence (contrast Restaurant Tycoon 3, [CS-25](CS-25-Restaurant-Tycoon-3.md)).

## Original application (do not copy the game)
(Lesson-oriented) Design any depth-based incremental so that deeper layers change *rules* (darkness, gas, collapsing floors), not only ore value.

## Confidence
High for the decline data; low for causes (inference).

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
