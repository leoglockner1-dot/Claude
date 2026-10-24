---
title: "GM-09 — Melting (transforming material with heat/time)"
tags: [mechanic, game-design]
note_type: "mechanic"
evidence: "academy synthesis; Roblox-specific constraints from official docs; examples from case studies (see Evidence row)"
---

# GM-09 — Melting (transforming material with heat/time)

| Aspect | Notes |
|---|---|
| **What the player does** | Applies heat or a process to change a material: melt ice, smelt ore, cook, forge. |
| **Skill or decision involved** | Managing time and temperature; avoiding over/under-processing. |
| **Feedback needed** | Visible state change (colour, glow, shape), progress bar or visual threshold, a warning before ruin (smoke). |
| **Why it can be satisfying** | Transformation is satisfying to watch; mastery of "just right" timing. |
| **Design conditions under which it works** | States must be readable at a glance (raw → ready → burnt). Works best as a *step* in a production chain, not a standalone loop. |
| **How difficulty can scale** | Multiple items at once, faster burn, recipes needing precise states. |
| **How progression can change it** | Better furnaces, automation, new materials with different curves. |
| **What causes repetition fatigue** | Waiting with nothing else to do; identical curves for every material. |
| **Exploits and edge cases (Roblox-specific where relevant)** | Leaving items processing while offline if timers are client-side; compute from server timestamps. |
| **Genres it fits** | Crafting, cooking/restaurant, forging, survival. |
| **Genres it does not fit (or fits badly)** | Action games with no downtime. |
| **Original variations** | Melting ice to reveal frozen treasure (risk: too hot destroys it); a glacier that melts as the world map. |
| **Prototype and testing guidance** | One furnace, 2 materials, 3 states; test whether players multitask several furnaces. |
| **Examples in this academy (evidence)** | [CS-25 Restaurant Tycoon 3](../20-Game-Case-Studies/CS-25-Restaurant-Tycoon-3.md) [DEV] fires and burned food when unattended · [CS-53 Sell Fries](../20-Game-Case-Studies/CS-53-Sell-Fries-Anomaly.md) |

**Use with:** [Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Mechanics Index](Mechanics-Index.md)
