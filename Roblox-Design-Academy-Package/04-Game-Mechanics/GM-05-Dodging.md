---
title: "GM-05 — Dodging"
tags: [mechanic, game-design]
note_type: "mechanic"
evidence: "academy synthesis; Roblox-specific constraints from official docs; examples from case studies (see Evidence row)"
---

# GM-05 — Dodging

| Aspect | Notes |
|---|---|
| **What the player does** | Avoids threats by moving, rolling, ducking or timing i-frames. |
| **Skill or decision involved** | Reading telegraphs, spatial awareness, timing. |
| **Feedback needed** | Clear telegraphs (wind-up, ground markers), satisfying near-miss cue, readable hitboxes. |
| **Why it can be satisfying** | Survival through skill; near-misses spike excitement. |
| **Design conditions under which it works** | Telegraphs must be readable at mobile size and through VFX clutter ([VFX Principles](../09-VFX/VFX-Principles-and-Performance.md)); hit detection must be consistent (decide authority: server-validated hits with latency tolerance). |
| **How difficulty can scale** | Faster projectiles, more simultaneous threats, less telegraph time, smaller arenas. |
| **How progression can change it** | New threat types with new patterns; dodge upgrades (dash charges). |
| **What causes repetition fatigue** | Unreadable patterns; random damage; dodging with no counter-play. |
| **Exploits and edge cases (Roblox-specific where relevant)** | Client-side position manipulation; lag-switching. Validate movement plausibility. |
| **Genres it fits** | Survival (Nextbots), bullet-hell, boss fights, obbies with moving hazards. |
| **Genres it does not fit (or fits badly)** | Slow strategy and idle games. |
| **Original variations** | Dodging that charges an ability (graze meter); cooperative dodging where one player shields. |
| **Prototype and testing guidance** | Arena + one threat with a 0.5 s telegraph; test whether players attribute hits to themselves. |
| **Examples in this academy (evidence)** | [CS-38 Evade](../20-Game-Case-Studies/CS-38-Evade.md) · [CS-34 Natural Disaster Survival](../20-Game-Case-Studies/CS-34-Natural-Disaster-Survival.md) · [V20 burst trap](../21-Video-Analyses/V20-Burst-Particle-Trap.md) |

**Use with:** [Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Mechanics Index](Mechanics-Index.md)
