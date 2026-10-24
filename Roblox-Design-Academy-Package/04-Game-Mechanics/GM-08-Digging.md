---
title: "GM-08 — Digging"
tags: [mechanic, game-design]
note_type: "mechanic"
evidence: "academy synthesis; Roblox-specific constraints from official docs; examples from case studies (see Evidence row)"
---

# GM-08 — Digging

| Aspect | Notes |
|---|---|
| **What the player does** | Removes material to go down or through: blocks, sand, ore veins, tunnels. |
| **Skill or decision involved** | Route choice, risk (cave-ins, patrols), resource prioritization. |
| **Feedback needed** | Material breaking with weight (particles + crunch sound), depth meter, rarity flashes in walls. |
| **Why it can be satisfying** | Visible progress downward; discovery of what lies beneath; tactile breaking. |
| **Design conditions under which it works** | Depth must **change something** (new materials, hazards, darkness); terrain/voxel cost must fit performance budgets (part counts, streaming). |
| **How difficulty can scale** | Harder layers, hazards (gas, lava), limited oxygen, patrols (Dig to Escape [DEV]). |
| **How progression can change it** | Better tools change speed and what can be dug; detection tools (X-ray goggles sold as a pass in Dig to Escape [DATA]). |
| **What causes repetition fatigue** | Uniform layers; depth that only raises numbers (contrast with Mining Simulator 2's decline, [CS-23](../20-Game-Case-Studies/CS-23-Mining-Simulator-2.md)). |
| **Exploits and edge cases (Roblox-specific where relevant)** | Digging through world bounds; remote spoofing of mined blocks; server cost of many destroyed parts. |
| **Genres it fits** | Mining sims, escape games, survival, treasure hunts. |
| **Genres it does not fit (or fits badly)** | Precision platformers. |
| **Original variations** | Dig upward to escape a flood; digging reveals a buried story in fossils. |
| **Prototype and testing guidance** | 20×20 block column with 3 layer types and one hazard; test how deep players go before returning. |
| **Examples in this academy (evidence)** | [CS-54 Dig to Escape](../20-Game-Case-Studies/CS-54-Dig-to-Escape.md) · [CS-23 Mining Simulator 2](../20-Game-Case-Studies/CS-23-Mining-Simulator-2.md) · [FC-GD-05 Dig to 999M](../15-Anti-Patterns-and-Failure-Cases/Failures-Documented/FC-GD-05-Dig-To-999M-Tutorial-Money-Gap.md) |

**Use with:** [Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Mechanics Index](Mechanics-Index.md)
