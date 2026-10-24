---
title: "CS-32 — Be My Camera (asymmetric 2-player obby — great hook, mixed reception)"
tags: [case-study, obby, co-op, asymmetric, communication]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-32 — Be My Camera (asymmetric 2-player obby — great hook, mixed reception)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [Be My Camera [2 Player Obby]](https://www.roblox.com/games/95205997597502/) · universe 7145230420 · by Obby Republic |
| Genre (Roblox) | Obby & Platformer / – · max 15 players per server |
| Concurrent players at capture | 389 |
| Visits · favourites | 53,077,097 · 1,060,353 (19.98 per 1k visits) |
| Like ratio | 58% (6,284 up / 4,555 down) |
| Created / updated | 2025-01-25 / 2026-09-21 |
| Game passes for sale | 9 · 29–349 R$ (median 129) · e.g. Falcon  (99), Ultimate Coil (199), VIP (349), Gravity Coil (129), Starter Pack (29), One Shot (199), Speed Coil (89), Enemy Drones Skin Pack (279) |

**Developer description (excerpt):** "🎥 Be your friend's eyes 👀 One of you jumps through the obby while the other controls the camera and protects them with lasers! 👀 work together to make it to the end. 📷 One player sees everything and fights evil drones, and the other does the jumping. 🧠 Talk, guide each other, you need real teamwork for this obby! FREE VIP …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] One player jumps through the obby while the other controls the camera and protects them with lasers. |
| Main action | [DEV] Runner: jump. Camera: aim the view and shoot drones. |
| Immediate feedback | [INF] Runner's success depends on the camera's view; drones destroyed. |
| Reward → new possibility | [INF] Stage progress; [DATA] passes: VIP 349, Gravity Coil 129, Ultimate Coil 199. |
| Micro loop (seconds) | [DEV] **Asymmetric roles**: one sees everything, the other moves; "Talk, guide each other". |
| Core loop (minutes) | [INF] navigate a stage together → survive drones → checkpoint. |
| Meta loop (days) | [DEV] Skins; "FREE VIP SERVERS" for playing with friends. |

## First-time experience
[DEV] The role split is explained in the description; [INF] works best with a friend and voice/text chat.

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | A genuinely **new interaction** (control is split between two people) that is explainable in one image ([TI-22](../02-Thumbnails-and-Icons/Analyses/TI-22-Asymmetric-CoOp-Explained-In-One-Image.md)). [DATA] Very high favourites per 1k visits (19.98). |
| Weakest part / quit risks | [DATA] 58% like ratio. [INF] Asymmetric co-op with random partners can be frustrating (bad camera partner = unplayable for the runner). [INF] Favourites may be inflated by in-game prompts; no evidence either way. |
| Essential features | Role split, communication, drone threat. |
| Possibly unnecessary | [INF] Movement-aid passes in a co-op skill game. |
| Minimal prototype to test the idea | A 3-stage course with split roles; test with friend pairs vs stranger pairs and compare completion and fun ratings. |

## Reusable lessons
- Asymmetric roles create unique moments **with friends**; design the stranger experience explicitly (role swap, partner rating, solo mode).
- High favourites with low likes = an exciting idea that disappoints in some sessions [INF].

## Original application (do not copy the game)
One player drives a mine cart blind; the other reads a map and pulls switches; roles swap at each station.

## Confidence
Medium for the hook; low for reception causes.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
