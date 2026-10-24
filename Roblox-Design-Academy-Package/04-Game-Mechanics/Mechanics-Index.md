---
title: "Game Mechanics Library — Index"
tags: [index, mechanic, game-design]
note_type: "index"
---

# Game Mechanics Library

Each mechanic note gives: what the player does, the skill/decision, the feedback needed, why it satisfies, **the design conditions under which it works**, difficulty scaling, how progression changes it, repetition fatigue, exploits (Roblox-specific), genres it fits and doesn't, original variations, prototype/testing guidance, and examples from the case studies.

**Evidence level:** the mechanic descriptions are academy synthesis (design knowledge, labelled as such). Roblox-specific constraints (server validation, network ownership, prompts firing from any distance) come from official docs. Examples link to case studies, which are themselves based on public data, not play.

| # | Mechanic | Core skill | Strong fits |
|---|---|---|---|
| GM-01 | [Timing](GM-01-Timing.md) | Perception and motor timing | Rhythm, platformers, fishing/reeling, combat parries, party elimination games. |
| GM-02 | [Balancing](GM-02-Balancing.md) | Continuous fine control and correction | Party games, physics sims, delivery/serving, precision obbies. |
| GM-03 | [Charging and releasing](GM-03-Charge-and-Release.md) | Estimating the right amount of power | Sports (golf, bowling), archery, launch games, fighting wind-ups. |
| GM-04 | [Collecting](GM-04-Collecting.md) | Route efficiency (micro) | Simulators, platformers, exploration, pet games. |
| GM-05 | [Dodging](GM-05-Dodging.md) | Reading telegraphs, spatial awareness, timing. | Survival (Nextbots), bullet-hell, boss fights, obbies with moving hazards. |
| GM-06 | [Aiming](GM-06-Aiming.md) | Hand-eye coordination | Shooters, sports throws, photography/camera games, tower targeting. |
| GM-07 | [Building](GM-07-Building.md) | Spatial planning, creativity, engineering trade-offs (cost, strength, layout efficiency). | Tycoons, sandboxes, survival bases, life sims. |
| GM-08 | [Digging](GM-08-Digging.md) | Route choice, risk (cave-ins, patrols), resource prioritization. | Mining sims, escape games, survival, treasure hunts. |
| GM-09 | [Melting (transforming material with heat/time)](GM-09-Melting.md) | Managing time and temperature | Crafting, cooking/restaurant, forging, survival. |
| GM-10 | [Crafting](GM-10-Crafting.md) | Planning, resource allocation, discovering recipes. | Survival, RPG, simulators, life sims. |
| GM-11 | [Risk and reward](GM-11-Risk-and-Reward.md) | Judgement under uncertainty | Steal loops, roguelites, extraction games, gambling-free push-your-luck. |
| GM-12 | [Escaping](GM-12-Escaping.md) | Navigation, puzzle-solving, evasion. | Horror, escape rooms, obby finales, asymmetric 1vN. |
| GM-13 | [Cooperation](GM-13-Cooperation.md) | Communication, role execution, trust. | Co-op obbies, survival, jobs (Pizza Place), raids. |
| GM-14 | [Competition](GM-14-Competition.md) | Depends: execution, strategy, reading opponents. | Shooters, fighting, sports, party elimination. |
| GM-15 | [Exploration](GM-15-Exploration.md) | Curiosity, navigation, reading environmental cues. | Adventure, RPG, simulators with zones, horror. |
| GM-16 | [Discovery (learning hidden rules and content)](GM-16-Discovery.md) | Experimentation, deduction, memory. | Horror (DOORS "use each death as a lesson" [DEV]), puzzle, crafting, RPG. |
| GM-17 | [Resource management](GM-17-Resource-Management.md) | Planning, prioritization, forecasting. | Tycoons, survival, TD (cash per wave), management. |
| GM-18 | [Skill-based movement](GM-18-Skill-Based-Movement.md) | Execution, route optimization, chaining techniques. | Obbies, Nextbot survival, racing, parkour. |
| GM-19 | [Environmental interaction](GM-19-Environmental-Interaction.md) | Observation, cause-and-effect reasoning. | Puzzle, horror, adventure, roleplay. |

## Combining mechanics
Most successful loops combine **one skill mechanic** (timing, aiming, movement) with **one decision mechanic** (risk/reward, resource management) and **one long-term mechanic** (collecting, building, discovery). Example: Fisch = timing (reel) + exploration (zones) + collecting (fish variants) [CS-22]. Check new concepts against this triangle in the [Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md).
