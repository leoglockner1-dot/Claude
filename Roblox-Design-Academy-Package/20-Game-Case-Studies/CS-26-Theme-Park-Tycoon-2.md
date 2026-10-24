---
title: "CS-26 — Theme Park Tycoon 2 (creative management with friends)"
tags: [case-study, tycoon, building, creativity, co-op]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-26 — Theme Park Tycoon 2 (creative management with friends)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [Theme Park Tycoon 2](https://www.roblox.com/games/69184822/) · universe 31970568 · by Den_S |
| Genre (Roblox) | Simulation / Tycoon · max 6 players per server |
| Concurrent players at capture | 3,645 |
| Visits · favourites | 1,625,415,025 · 6,107,413 (3.76 per 1k visits) |
| Like ratio | 89% (2,085,502 up / 256,983 down) |
| Created / updated | 2012-01-02 / 2026-08-31 |
| Game passes for sale | 5 · 74–374 R$ (median 90) · e.g. Disable collisions (270), 24 extra expansion plots (374), Enable Ride operations (90), Increased height limit (74), Extra colors (90) |

**Developer description (excerpt):** "In Theme Park Tycoon 2 you get your own plot of land to build your own theme park on, together with your friends! Construct a range of rides the way you want and design your own roller coasters to truly make your park your own! Select from hundreds of scenery pieces to decorate your park further!"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Build your own theme park on your own plot with friends; design roller coasters; decorate with hundreds of scenery pieces. |
| Main action | [INF] Place rides, paths, scenery; design coaster tracks. |
| Immediate feedback | [INF] Guests visiting rides; coaster test runs. |
| Reward → new possibility | [INF] Park income → more rides and space; [DATA] passes extend space/height ("24 extra expansion plots" 374, "Increased height limit" 74). |
| Micro loop (seconds) | [INF] Placement and track-design decisions. |
| Core loop (minutes) | [INF] build attraction → guests pay → expand → build bigger/more creative attractions. |
| Meta loop (days) | [INF] Personal creative project that persists; co-building with friends. |

## First-time experience
[INF] Building games need a guided first ride placement. *Not observed.*

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | **Longevity**: created 2012, updated 2026; the highest favourites per 1k visits in this batch (3.76) suggests strong commitment. Creative expression with a management frame. |
| Weakest part / quit risks | [INF] Steep learning curve of coaster design on mobile. |
| Essential features | Plot, ride placement, coaster editor, guest economy. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | A plot, 3 flat rides, paths, guests who pay; test if players decorate without being asked. |

## Reusable lessons
- When players invest creativity, favouriting/returning follows: the park is *theirs*.
- Passes that **extend the canvas** (space, height) monetize creativity without pay-to-win.

## Original application (do not copy the game)
Design a mini-golf course on floating islands; visitors rate holes; expand with new island biomes.

## Confidence
Medium for structure; low for details.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
