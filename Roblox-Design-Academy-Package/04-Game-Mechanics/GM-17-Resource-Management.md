---
title: "GM-17 — Resource management"
tags: [mechanic, game-design]
note_type: "mechanic"
evidence: "academy synthesis; Roblox-specific constraints from official docs; examples from case studies (see Evidence row)"
---

# GM-17 — Resource management

| Aspect | Notes |
|---|---|
| **What the player does** | Allocates limited resources (money, fuel, time, slots) among competing uses. |
| **Skill or decision involved** | Planning, prioritization, forecasting. |
| **Feedback needed** | Clear stocks and flows (income/s, fuel left), projections, warnings before depletion. |
| **Why it can be satisfying** | Smart decisions compound; players feel clever. |
| **Design conditions under which it works** | Few, clearly different resources (a reviewer criticized an economy with too many inputs and one sink, [FC-GD-03](../15-Anti-Patterns-and-Failure-Cases/Failures-Documented/FC-GD-03-Photography-Game-Feature-Sprawl.md)); sinks that matter; server-authoritative values ([LU-07](../07-Roblox-Studio-and-Luau/LU-07-Currency-and-Shop.md)). |
| **How difficulty can scale** | Scarcity, competing demands, events that drain resources. |
| **How progression can change it** | New resource types, conversion buildings, automation. |
| **What causes repetition fatigue** | One correct allocation (solved); bookkeeping without decisions. |
| **Exploits and edge cases (Roblox-specific where relevant)** | Infinite loops in conversion chains; offline exploits; NaN values. |
| **Genres it fits** | Tycoons, survival, TD (cash per wave), management. |
| **Genres it does not fit (or fits badly)** | Party games for very young players. |
| **Original variations** | Shared resource pool across the server (tragedy of the commons); resources that decay. |
| **Prototype and testing guidance** | Two resources, one conversion, one sink; test whether testers form different strategies. |
| **Examples in this academy (evidence)** | [CS-50 TDS](../20-Game-Case-Studies/CS-50-Tower-Defense-Simulator.md) · [CS-37 Dead Rails](../20-Game-Case-Studies/CS-37-Dead-Rails.md) · [CS-25 RT3](../20-Game-Case-Studies/CS-25-Restaurant-Tycoon-3.md) · [LU-12 pacing](../07-Roblox-Studio-and-Luau/LU-12-Upgrade-Pricing.md) |

**Use with:** [Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Mechanics Index](Mechanics-Index.md)
