---
title: "GM-03 — Charging and releasing"
tags: [mechanic, game-design]
note_type: "mechanic"
evidence: "academy synthesis; Roblox-specific constraints from official docs; examples from case studies (see Evidence row)"
---

# GM-03 — Charging and releasing

| Aspect | Notes |
|---|---|
| **What the player does** | Holds to build power, releases to act: golf shot, bow draw, jump charge, wind-up punch. |
| **Skill or decision involved** | Estimating the right amount of power; committing under uncertainty. |
| **Feedback needed** | A filling meter with a readable sweet spot, audio pitch rising with charge, a release impact sized to power. |
| **Why it can be satisfying** | Commitment plus estimation creates a mini-gamble every action; the moment of release is punchy. |
| **Design conditions under which it works** | Must map to all inputs: mouse drag, touch slider (Super Golf uses a slider on mobile), gamepad trigger. Server validates power range. |
| **How difficulty can scale** | Oscillating meters, moving targets, wind, overcharge penalty. |
| **How progression can change it** | New clubs/bows changing curve shape or max power; trajectory preview as an upgrade. |
| **What causes repetition fatigue** | Same distance every time (solved); no variation in targets. |
| **Exploits and edge cases (Roblox-specific where relevant)** | Client sending max power (clamp server-side); NaN power values ([LU-05](../07-Roblox-Studio-and-Luau/LU-05-Server-Validation.md)). |
| **Genres it fits** | Sports (golf, bowling), archery, launch games, fighting wind-ups. |
| **Genres it does not fit (or fits badly)** | Fast twitch shooters where holding slows the pace. |
| **Original variations** | Charge drains a shared resource; releasing at perfect charge triggers a bonus effect. |
| **Prototype and testing guidance** | Charge meter + one target at 3 distances; track how many shots until players hit consistently. |
| **Examples in this academy (evidence)** | [CS-49 Super Golf](../20-Game-Case-Studies/CS-49-Super-Golf.md) [DEV] click-drag-release, mobile slider · [CS-48 Volleyball Legends](../20-Game-Case-Studies/CS-48-Volleyball-Legends.md) serve power |

**Use with:** [Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Mechanics Index](Mechanics-Index.md)
