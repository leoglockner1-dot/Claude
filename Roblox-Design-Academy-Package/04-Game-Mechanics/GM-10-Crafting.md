---
title: "GM-10 — Crafting"
tags: [mechanic, game-design]
note_type: "mechanic"
evidence: "academy synthesis; Roblox-specific constraints from official docs; examples from case studies (see Evidence row)"
---

# GM-10 — Crafting

| Aspect | Notes |
|---|---|
| **What the player does** | Combines inputs into outputs by recipe. |
| **Skill or decision involved** | Planning, resource allocation, discovering recipes. |
| **Feedback needed** | Recipe preview, missing-ingredient highlights, satisfying craft animation and result reveal. |
| **Why it can be satisfying** | Agency over progression; converts collected junk into meaningful items. |
| **Design conditions under which it works** | Recipes must be discoverable (book, hints); costs consumed atomically on the server ([LU-10 Inventory.consume](../07-Roblox-Studio-and-Luau/LU-10-Inventory.md)); outputs should open new options, not just bigger stats. |
| **How difficulty can scale** | Deeper recipe trees, rare inputs, time-gated crafts. |
| **How progression can change it** | New stations, recipe unlocks, quality tiers. |
| **What causes repetition fatigue** | Long linear recipe chains with no choices; inventory management chores. |
| **Exploits and edge cases (Roblox-specific where relevant)** | Partial consumption bugs; duplicate crafting via double remote calls (rate limit + atomic consume). |
| **Genres it fits** | Survival, RPG, simulators, life sims. |
| **Genres it does not fit (or fits badly)** | Short party rounds. |
| **Original variations** | Crafting with physical assembly (place parts on a bench); recipes discovered by experimentation. |
| **Prototype and testing guidance** | 4 inputs, 3 recipes, a recipe book; test whether players experiment. |
| **Examples in this academy (evidence)** | [LU-10](../07-Roblox-Studio-and-Luau/LU-10-Inventory.md) (atomic costs, tested) · [FC-GD-05](../15-Anti-Patterns-and-Failure-Cases/Failures-Documented/FC-GD-05-Dig-To-999M-Tutorial-Money-Gap.md) (crafting planned as the next retention layer) |

**Use with:** [Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Mechanics Index](Mechanics-Index.md)
