---
title: "GM-18 — Skill-based movement"
tags: [mechanic, game-design]
note_type: "mechanic"
evidence: "academy synthesis; Roblox-specific constraints from official docs; examples from case studies (see Evidence row)"
---

# GM-18 — Skill-based movement

| Aspect | Notes |
|---|---|
| **What the player does** | Moves with techniques that reward practice: wall-runs, slides, momentum jumps, bike control. |
| **Skill or decision involved** | Execution, route optimization, chaining techniques. |
| **Feedback needed** | Speed lines, FOV changes, sound rising with speed, readable momentum. |
| **Why it can be satisfying** | Movement mastery feels good every second; skill shows visibly to others. |
| **Design conditions under which it works** | Responsive controls (character physics tuning), consistent collision, mobile input support (context buttons), anti-cheat speed validation. |
| **How difficulty can scale** | Tighter routes, longer chains, speedrun timers. |
| **How progression can change it** | Movement upgrades (with care: they change the challenge), new techniques taught in stages. |
| **What causes repetition fatigue** | Inconsistent physics; techniques too hard to discover. |
| **Exploits and edge cases (Roblox-specific where relevant)** | Speed hacks (validate distance over time server-side); physics glitches. |
| **Genres it fits** | Obbies, Nextbot survival, racing, parkour. |
| **Genres it does not fit (or fits badly)** | Strategy/idle. |
| **Original variations** | Movement through a different body (bike, spider web, pogo) as the twist. |
| **Prototype and testing guidance** | One technique (slide-jump) + one course; measure time improvement across 5 runs. |
| **Examples in this academy (evidence)** | [CS-38 Evade](../20-Game-Case-Studies/CS-38-Evade.md) · [CS-30 Obby on a Bike](../20-Game-Case-Studies/CS-30-Obby-But-Youre-On-A-Bike.md) · [CS-33 Webbed!](../20-Game-Case-Studies/CS-33-Webbed.md) |

**Use with:** [Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Mechanics Index](Mechanics-Index.md)
