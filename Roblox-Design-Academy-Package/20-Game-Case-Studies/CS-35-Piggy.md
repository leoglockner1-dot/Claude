---
title: "CS-35 — Piggy (episodic horror escape with user maps)"
tags: [case-study, survival, horror, escape, story, ugc]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-35 — Piggy (episodic horror escape with user maps)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [Piggy [FRIGHTFUL CARNIVAL]](https://www.roblox.com/games/4623386862/) · universe 1516533665 · by Piggy Dev Team |
| Genre (Roblox) | Survival / – · max 6 players per server |
| Concurrent players at capture | 27,267 |
| Visits · favourites | 14,431,930,020 · 12,283,258 (0.85 per 1k visits) |
| Like ratio | 90% (4,072,903 up / 435,963 down) |
| Created / updated | 2020-01-23 / 2026-10-24 |
| Game passes for sale | 8 · 100–300 R$ (median 100) · e.g. x2 Piggy Tokens (300), x2 Piggy Chance (150), Build Map Slot 3 (100), Build Map Slot 11 (100), Build Map Slot 12 (100), Build Map Slot 4 (100), Build Map Slot 6 (100), Build Map Slot 5 (100) |

**Developer description (excerpt):** "Do you have what it takes to escape Piggy and uncover the mysteries surrounding the beast? Controls: Pick up items / Use items - Click (Computer), Tap (Mobile) or Right Trigger (Controller) Crouch / Place trap - CTRL (Computer), Tap (Mobile) or B (Controller) Credits: IK3As - Building Optikk & Epic_Tank - Build Mode For You to …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Escape Piggy and uncover the mysteries surrounding the beast. |
| Main action | [DEV] Pick up/use items, crouch, place traps; [INF] solve the map's escape puzzle while one player or bot hunts. |
| Immediate feedback | [INF] Chase tension, item use opening paths. |
| Reward → new possibility | [INF] Escape → story progress; [DATA] passes: x2 Piggy Tokens (300), x2 Piggy Chance (150), Build Map slots (100). |
| Micro loop (seconds) | [INF] Item routing + evasion. |
| Core loop (minutes) | [INF] round: find items → open exits → avoid Piggy → escape. |
| Meta loop (days) | [DEV] Mysteries/story chapters; [DATA] **user map building** (Build Map slots) extends content. |

## First-time experience
[DEV] Controls for PC, mobile and controller listed in the description.

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | **Story + escape puzzle + chase**; user-built maps (passes) extend content at low dev cost. |
| Weakest part / quit risks | [INF] Puzzle solutions become known; replay depends on new chapters/maps. |
| Essential features | Hunter vs escapers, item puzzles, chapters. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | One house, 3 key items, one hunter bot; test escape rate and tension. |

## Reusable lessons
- Episodic story drops create appointment returns.
- Letting players **build maps** turns your community into a content pipeline.

## Original application (do not copy the game)
A lighthouse keeper escape: collect lamp parts to signal a ship while a fog creature listens for footsteps.

## Confidence
Medium-low.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
