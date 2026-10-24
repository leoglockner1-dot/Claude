---
title: "Game Case Study Index and cross-case patterns"
tags: [index, case-study, game-design, core-loop]
note_type: "index"
---

# Game Case Study Index

**54 case-study notes covering about 62 distinct Roblox experiences**, plus 6 documented developer failure cases ([Failures-Documented](../15-Anti-Patterns-and-Failure-Cases/Failures-Documented/FC-GD-01-Troll-Outfit-Tower-Retention-Collapse.md)).

**Evidence level, stated honestly:** no game was played (no Roblox client here; video sites blocked). Each note uses Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue, and developer DevForum posts where available. Loops marked [DEV] come from the developer's words; [INF] marks inference. **First-10/30-second claims are inferences** unless the note says otherwise. The highest-value next step for any later agent with a Roblox client: play the top 10 here for 15 minutes each and replace [INF] with [OBS].

## By genre
| Genre | Case studies |
|---|---|
| Simulator / incremental | [CS-19 Bee Swarm](CS-19-Bee-Swarm-Simulator.md) · [CS-20 Pet Simulator 99](CS-20-Pet-Simulator-99.md) · [CS-21 Grow a Garden](CS-21-Grow-a-Garden.md) · [CS-22 Fisch](CS-22-Fisch.md) · [CS-23 Mining Simulator 2 (decline)](CS-23-Mining-Simulator-2.md) · [CS-12 "+1" games](CS-12-Plus-One-Incremental-Games.md) · [CS-04 Steal-loop games](CS-04-Steal-Loop-Games.md) |
| Tycoon / management / building | [CS-25 Restaurant Tycoon 3](CS-25-Restaurant-Tycoon-3.md) · [CS-26 Theme Park Tycoon 2](CS-26-Theme-Park-Tycoon-2.md) · [CS-27 Lumber Tycoon 2](CS-27-Lumber-Tycoon-2.md) · [CS-28 Chicken Farm](CS-28-Chicken-Farm.md) · [CS-11 Tycoon group](CS-11-Tycoon-Group.md) · [CS-24 Build A Boat](CS-24-Build-A-Boat-For-Treasure.md) · [CS-18 Plant (reference)](CS-18-Plant-Reference-Project.md) |
| Obby / platformer | [CS-05 Tower of Hell](CS-05-Tower-of-Hell.md) · [CS-29 Speed Run 4](CS-29-Speed-Run-4.md) · [CS-30 Obby on a Bike](CS-30-Obby-But-Youre-On-A-Bike.md) · [CS-16 Troll-tower funnel](CS-16-Troll-Tower-Obby-Funnel.md) |
| Co-op | [CS-31 Teamwork Puzzles](CS-31-Teamwork-Puzzles.md) · [CS-32 Be My Camera](CS-32-Be-My-Camera.md) · [CS-33 Webbed!](CS-33-Webbed.md) · group view: [CS-09](CS-09-Small-CoOp-Games.md) · [CS-37 Dead Rails](CS-37-Dead-Rails.md) · [CS-01 99 Nights](CS-01-99-Nights-in-the-Forest.md) |
| Survival / horror / escape | [CS-07 DOORS](CS-07-DOORS.md) · [CS-34 Natural Disaster Survival](CS-34-Natural-Disaster-Survival.md) · [CS-35 Piggy](CS-35-Piggy.md) · [CS-36 Flee the Facility](CS-36-Flee-the-Facility.md) · [CS-38 Evade](CS-38-Evade.md) · [CS-53 Sell Fries (anomaly trend)](CS-53-Sell-Fries-Anomaly.md) · [CS-54 Dig to Escape](CS-54-Dig-to-Escape.md) · [CS-14 Duvall Drive](CS-14-Mystery-of-Duvall-Drive.md) |
| Competitive / combat | [CS-02 RIVALS](CS-02-RIVALS.md) · [CS-39 BedWars](CS-39-BedWars.md) · [CS-40 Arsenal](CS-40-Arsenal.md) · [CS-41 Strongest Battlegrounds](CS-41-The-Strongest-Battlegrounds.md) · [CS-13 Laser Tag (reference)](CS-13-Laser-Tag-Reference-Game.md) · [CS-15 TURBOSTORM](CS-15-TURBOSTORM-Racing.md) |
| Party / minigames | [CS-42 Epic Minigames](CS-42-Epic-Minigames.md) · [CS-43 Hide and Seek Extreme](CS-43-Hide-and-Seek-Extreme.md) · [CS-44 Musical Chairs](CS-44-Musical-Chairs.md) · group view: [CS-10](CS-10-Party-Round-Games.md) |
| Social / roleplay / life | [CS-06 Adopt Me](CS-06-Adopt-Me.md) · [CS-08 Brookhaven](CS-08-Brookhaven.md) · [CS-03 Dress To Impress](CS-03-Dress-To-Impress.md) · [CS-45 Work at a Pizza Place](CS-45-Work-at-a-Pizza-Place.md) · [CS-46 PLS DONATE](CS-46-PLS-DONATE.md) · [CS-47 Bloxburg](CS-47-Welcome-to-Bloxburg.md) |
| Sports / rhythm | [CS-48 Volleyball Legends](CS-48-Volleyball-Legends.md) · [CS-49 Super Golf](CS-49-Super-Golf.md) · [CS-52 Funky Friday](CS-52-Funky-Friday.md) |
| Strategy / RPG | [CS-50 Tower Defense Simulator](CS-50-Tower-Defense-Simulator.md) · [CS-51 Blox Fruits](CS-51-Blox-Fruits.md) |
| Documented struggling games | [CS-17 Outbreak Mayhem](CS-17-Outbreak-Mayhem.md) · [FC-GD-01…06](../15-Anti-Patterns-and-Failure-Cases/Failure-and-Correction-Index.md) |

## Cross-case patterns (synthesis; each with its evidence)
| # | Pattern | Evidence | Confidence |
|---|---|---|---|
| P1 | **Return triggers built into the loop** (offline growth, restocks, weekly updates, episodic chapters) | Grow a Garden [DEV] offline growth + restocks; Restaurant Tycoon 3 ≈70 weekly updates [DEV]; BedWars fixed Friday slot [DEV]; TDS "Night I–III" [DEV]; Piggy chapters | Medium-high |
| P2 | **Progress you can see in the world** beats progress in a menu | Bee Swarm's mountain [DEV]; Theme Park/Bloxburg plots; Speed Run 4's per-level music + look [DEV] | Medium |
| P3 | **Unlocks that change how you play** sustain long ladders better than stat increases | Blox Fruits movesets [DEV]; Fisch rods/locations; Arsenal weapon ladder; contrast Mining Simulator 2's decline [DATA] | Medium |
| P4 | **Change the verb, put it in the title** in saturated genres | Obby But You're On a Bike (4.38 favourites per 1k visits, highest of the obbies here) [DATA]; Rising Empires' "just another TD" problem ([FC-GD-04](../15-Anti-Patterns-and-Failure-Cases/Failures-Documented/FC-GD-04-Rising-Empires-Generic-First-Impression.md)) | Medium |
| P5 | **Dependency on strangers is a satisfaction risk** | Teamwork Puzzles 49%, Be My Camera 58% [DATA] vs Webbed 87%, where the shared constraint is physical and funny [DATA]; [FC-GD-06](../15-Anti-Patterns-and-Failure-Cases/Failures-Documented/FC-GD-06-Asymmetric-Survival-Engaged-Core-Low-D1.md) | Medium (cause inferred) |
| P6 | **Never sell an advantage in the skill that decides the round** | Musical Chairs sells +25% speed; 66% likes [DATA]; movement-aid passes common in obbies, the lowest-liked genre | Low-medium (correlation) |
| P7 | **Obbies and party games have the lowest like ratios** in this sample: median 75% and 79% vs 92.5% for simulation (112 games with >1,000 votes) | [DATA] computed from the API pull | Medium for the data; causes are hypotheses (difficulty frustration, elimination waiting, stranger dependency) |
| P8 | **Pass count does not track like ratio**: medians 89–92% whether a game sells 0, 1–5, 6–15 or 16+ passes | [DATA] same pull | Medium; what is sold matters more than how much (see P6) |
| P9 | **Combinatorial variety** (maps × events) beats lists of unique content | Natural Disaster Survival (2008, 91% likes); Tower of Hell (randomized towers) | Medium |
| P10 | **State honest expectations** (player count, session length, warnings) | Webbed "MADE FOR 2 PLAYERS"; Dig to Escape "30–60m+" and 98% likes; DOORS warnings | Low-medium |
| P11 | **Current health ≠ historic success**: read CCU and update dates next to visits and likes | Mining Simulator 2: 210M visits, 93% likes, 25 CCU [DATA] | High (data) |
| P12 | **Tone contrast** (calm job → sudden threat) is a 2026 trend format | Sell Fries! [Anomaly], Clone Baby Care (Anomaly), Dig to Escape | Medium (trend observed in chart data) |

These patterns feed [Core Loop Principles](../17-Design-Principles/Core-Loop-Principles.md) and the [Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md).

## How to write a new case study
Use `CS-19`…`CS-54` as the template: data table → developer description excerpt → loop table (premise, action, feedback, reward → new possibility, micro/core/meta) → first-time experience → critical analysis (strongest, weakest/quit risks, essential, unnecessary, minimal prototype) → lessons → original application → confidence. Tag every claim. If you can play the game, add an **[OBS] first-session log** with timestamps (0:00 spawn, first action, first reward, first upgrade, first confusion, quit or continue).
