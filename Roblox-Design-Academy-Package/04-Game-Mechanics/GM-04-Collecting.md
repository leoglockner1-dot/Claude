---
title: "GM-04 — Collecting"
tags: [mechanic, game-design]
note_type: "mechanic"
evidence: "academy synthesis; Roblox-specific constraints from official docs; examples from case studies (see Evidence row)"
---

# GM-04 — Collecting

| Aspect | Notes |
|---|---|
| **What the player does** | Picks up items (coins, pollen, fish, pets) or completes sets. |
| **Skill or decision involved** | Route efficiency (micro); set completion planning (meta). Often low skill. |
| **Feedback needed** | Pickup pop, sound with slight pitch variation, item flying to a counter, set progress. |
| **Why it can be satisfying** | Constant small rewards; completion drive; collections express identity (rare pets, outfits). |
| **Design conditions under which it works** | Works when items have **meaning beyond count**: rarity, personality, sets, display. Collection target must be visible (index/collection book). |
| **How difficulty can scale** | Rarer items in harder places; timed or conditional spawns. |
| **How progression can change it** | Magnet radius, auto-collect, new zones with new item families. |
| **What causes repetition fatigue** | Collecting numbers only; auto-collect removing the only action; enormous collections where nothing feels special (a reviewer's point in [FC-GD-03](../15-Anti-Patterns-and-Failure-Cases/Failures-Documented/FC-GD-03-Photography-Game-Feature-Sprawl.md)). |
| **Exploits and edge cases (Roblox-specific where relevant)** | Remote "I collected X" spam: validate distance, existence and rate server-side ([LU-05](../07-Roblox-Studio-and-Luau/LU-05-Server-Validation.md), [LU-06](../07-Roblox-Studio-and-Luau/LU-06-Rate-Limiting.md)). |
| **Genres it fits** | Simulators, platformers, exploration, pet games. |
| **Genres it does not fit (or fits badly)** | Tense competitive games (collecting distracts from the duel) unless collecting *is* the competition. |
| **Original variations** | Collectibles that change behaviour (bees with traits); collections that unlock new abilities. |
| **Prototype and testing guidance** | Field of pickups + counter + one rare variant; measure if players chase the rare one. |
| **Examples in this academy (evidence)** | [CS-19 Bee Swarm](../20-Game-Case-Studies/CS-19-Bee-Swarm-Simulator.md) · [CS-20 PS99](../20-Game-Case-Studies/CS-20-Pet-Simulator-99.md) · [R03 Currency Collection](../18-Skill-Training/Design-Recipes/R03-Currency-Collection-Interaction.md) · [BL-EX-02](../06-Blender-and-3D-Assets/Exercises/BL-EX-02-Collectible-Gem-and-Coin.md) |

**Use with:** [Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Mechanics Index](Mechanics-Index.md)
