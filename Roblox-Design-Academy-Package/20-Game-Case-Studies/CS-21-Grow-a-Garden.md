---
title: "CS-21 — Grow a Garden (offline growth, restock shop, social flexing)"
tags: [case-study, simulator, tycoon, idle, social, offline-progress]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-21 — Grow a Garden (offline growth, restock shop, social flexing)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [[🎃] Grow a Garden 🌶️](https://www.roblox.com/games/126884695634066/) · universe 7436755782 · by The Garden Game |
| Genre (Roblox) | Simulation / Tycoon · max 4 players per server |
| Concurrent players at capture | 22,997 |
| Visits · favourites | 35,988,664,699 · 11,456,418 (0.32 per 1k visits) |
| Like ratio | 90% (9,439,967 up / 1,055,432 down) |
| Created / updated | 2025-03-25 / 2026-10-24 |
| Game passes for sale | 0 · e.g. none listed for sale (developer products are not visible through this API) |

**Developer description (excerpt):** "🍅Welcome to Grow a Garden🍅 Are you ready to grow your very own garden? Buy seeds from the shop when they restock, plant them, wait for them to grow, and collect the profits! Flex fruits and finds on friends, and have fun! [How To Plant] • Equip your seed you want to plant! • Click in your farm on the brown plots to plant! • …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Buy seeds when the shop restocks, plant, wait, harvest and sell; "your garden literally grows while you are offline". |
| Main action | [DEV] Equip seed → click a brown plot → wait → harvest. |
| Immediate feedback | [INF] Plants visibly growing on your own plot; harvest yields. |
| Reward → new possibility | [DEV] Profits → more/better seeds; [DEV] "flex fruits and finds on friends". |
| Micro loop (seconds) | [DEV] Plant/harvest clicks; [INF] timing around shop restocks. |
| Core loop (minutes) | [DEV] buy seeds (on restock) → plant → wait → harvest → sell → buy better seeds. |
| Meta loop (days) | [DEV] Offline growth gives a reason to come back; restock timing creates appointment play; social flexing of rare finds. |

## First-time experience
[DEV] The description includes a 4-step **How To Plant** guide, so the first action is explicit. [INF] The first reward requires waiting for growth; the shop restock adds scarcity. *Timings not observed.*

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | **Return triggers are built into the loop**: offline growth + restocks + something to show friends. Small server (max 4) keeps the social space intimate. [DATA] 36 billion visits; 90% likes. |
| Weakest part / quit risks | [INF] Waiting is the core pacing tool; without enough to do while waiting, sessions can be short (which may be acceptable if return visits are frequent). [DATA] Very low favourites per 1k visits (0.32) relative to other games here [INF: a proxy of commitment per visit; may reflect huge casual traffic]. |
| Essential features | Own plot, visible growth, restock shop, offline progress. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | One plot, 3 seed types, a restock timer, offline growth (save timestamp, compute growth on join); test whether players return after 1 hour. |

## Reusable lessons
- Offline progress converts *time away* into a reason to return; compute it from saved timestamps on join (server-side).
- Shop restocks create scarcity and appointment play without punishing absence too hard.
- Make rare outcomes **showable** to friends: flexing is a free social loop.

## Original application (do not copy the game)
A potion cellar: brew in cauldrons that keep bubbling while offline; the ingredient market restocks on a timer; rare brews glow on your shelf for visitors.

## Confidence
Medium-high for the loop ([DEV] explicit how-to); low for pacing.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
