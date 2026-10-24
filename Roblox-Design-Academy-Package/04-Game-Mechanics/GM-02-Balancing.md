---
title: "GM-02 — Balancing"
tags: [mechanic, game-design]
note_type: "mechanic"
evidence: "academy synthesis; Roblox-specific constraints from official docs; examples from case studies (see Evidence row)"
---

# GM-02 — Balancing

| Aspect | Notes |
|---|---|
| **What the player does** | Keeps something stable: a tower of blocks, a tray of drinks, a character on a beam, a needle in a band. |
| **Skill or decision involved** | Continuous fine control and correction; planning ahead of drift. |
| **Feedback needed** | Clear stability indicator (wobble, tilt meter), escalating warnings before failure, satisfying collapse. |
| **Why it can be satisfying** | Tension rises continuously; recovering from a wobble feels heroic; failure is often funny. |
| **Design conditions under which it works** | Physics must be deterministic enough to feel fair; on Roblox physics, client-owned parts simulate locally (network ownership), so validate outcomes server-side if they grant rewards. |
| **How difficulty can scale** | More weight, wind, moving platforms, longer duration, adding a second task. |
| **How progression can change it** | Better tools (wider tray, stabilizers) that change how much attention balancing needs. |
| **What causes repetition fatigue** | Long uneventful stretches; failure from physics jitter rather than player error. |
| **Exploits and edge cases (Roblox-specific where relevant)** | Network-ownership manipulation of unanchored parts; physics glitches at low frame rates. |
| **Genres it fits** | Party games, physics sims, delivery/serving, precision obbies. |
| **Genres it does not fit (or fits badly)** | Competitive ranked play (physics variance feels unfair). |
| **Original variations** | Balance shared between two players (each controls one side); balance that changes the world (keeping a ship level floods one side). |
| **Prototype and testing guidance** | One tray, 3 objects, a tilt meter; test whether failures are blamed on self (good) or on the game (bad). |
| **Examples in this academy (evidence)** | [CS-24 Build A Boat](../20-Game-Case-Studies/CS-24-Build-A-Boat-For-Treasure.md) (structural survival) · Experiments post: block-pool difficulty "sweet spot" in Build a Crazy Tower ([Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md)) |

**Use with:** [Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Mechanics Index](Mechanics-Index.md)
