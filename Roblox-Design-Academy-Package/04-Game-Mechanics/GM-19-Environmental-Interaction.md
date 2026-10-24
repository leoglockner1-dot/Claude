---
title: "GM-19 — Environmental interaction"
tags: [mechanic, game-design]
note_type: "mechanic"
evidence: "academy synthesis; Roblox-specific constraints from official docs; examples from case studies (see Evidence row)"
---

# GM-19 — Environmental interaction

| Aspect | Notes |
|---|---|
| **What the player does** | Changes or uses the world: opens doors, pulls levers, breaks walls, moves objects, triggers events. |
| **Skill or decision involved** | Observation, cause-and-effect reasoning. |
| **Feedback needed** | Affordances (glow, prompts, highlights), visible consequences, sound on interaction. |
| **Why it can be satisfying** | The world feels responsive; agency is visible. |
| **Design conditions under which it works** | Interactables must be readable (consistent affordance language, [ONB-03 highlight](../13-Onboarding-and-Multiplayer/Onboarding/Analyses/ONB-03-Hello-Kitty-Cafe-Spotlight-and-Trail.md)); server validates every trigger (ProximityPrompt and ClickDetector events can be fired by exploiters from any distance, per Roblox docs, [LU-03](../07-Roblox-Studio-and-Luau/LU-03-Client-Server-Responsibilities.md)). |
| **How difficulty can scale** | Chains of interactions, timed sequences, hidden interactables. |
| **How progression can change it** | Tools that unlock new interactions (keys, abilities). |
| **What causes repetition fatigue** | Interactions with no consequence; inconsistent affordances. |
| **Exploits and edge cases (Roblox-specific where relevant)** | Remote triggering of prompts; physics props used to grief. |
| **Genres it fits** | Puzzle, horror, adventure, roleplay. |
| **Genres it does not fit (or fits badly)** | Pure arena combat. |
| **Original variations** | Interactions that are permanent for the whole server; interactions that need two players. |
| **Prototype and testing guidance** | 3 interactables with clear affordances + 1 hidden; test discovery rate. |
| **Examples in this academy (evidence)** | [UI-12 themed prompt](../01-UI-UX/Analyses/UI-12-Mermaid-Life-Themed-Proximity-Prompt.md) · [V19](../21-Video-Analyses/V19-Proximity-Hold-Duration.md) · [CS-14 Duvall Drive](../20-Game-Case-Studies/CS-14-Mystery-of-Duvall-Drive.md) |

**Use with:** [Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Mechanics Index](Mechanics-Index.md)
