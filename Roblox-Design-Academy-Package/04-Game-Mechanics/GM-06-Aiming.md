---
title: "GM-06 — Aiming"
tags: [mechanic, game-design]
note_type: "mechanic"
evidence: "academy synthesis; Roblox-specific constraints from official docs; examples from case studies (see Evidence row)"
---

# GM-06 — Aiming

| Aspect | Notes |
|---|---|
| **What the player does** | Points at a target: shooting, throwing, casting, pointing a camera. |
| **Skill or decision involved** | Hand-eye coordination; leading moving targets; choosing targets. |
| **Feedback needed** | Crosshair response, hit markers, hit sounds, damage numbers, kill confirmation. |
| **Why it can be satisfying** | Precise, immediate skill expression; hits feel earned. |
| **Design conditions under which it works** | Must work on touch (aim assist, larger hitboxes) and gamepad. Server validates shots: origin near the shooter, target near the reported hit, no static obstruction, fire rate, ammo ([Roblox security docs](../07-Roblox-Studio-and-Luau/LU-03-Client-Server-Responsibilities.md)). |
| **How difficulty can scale** | Smaller/faster targets, recoil, projectile travel time, cover. |
| **How progression can change it** | Weapons with different handling (not only damage); scopes; loadouts. |
| **What causes repetition fatigue** | Identical weapons; time-to-kill extremes (too fast = no counter-play, too slow = spongy). |
| **Exploits and edge cases (Roblox-specific where relevant)** | Aimbots, silent aim, remote spoofing of hits. Validate server-side; rate limit. |
| **Genres it fits** | Shooters, sports throws, photography/camera games, tower targeting. |
| **Genres it does not fit (or fits badly)** | Games for very young players on touch without assist. |
| **Original variations** | Aim to *paint* territory; aim with a delayed projectile you steer. |
| **Prototype and testing guidance** | One weapon, 3 target distances, server hit validation; measure hit rate by device. |
| **Examples in this academy (evidence)** | [CS-02 RIVALS](../20-Game-Case-Studies/CS-02-RIVALS.md) · [CS-40 Arsenal](../20-Game-Case-Studies/CS-40-Arsenal.md) · [V10/V11 blaster cooldown](../21-Video-Analyses/V10-V11-Blaster-Cooldown-vs-Spam.md) · [CS-13 Laser Tag](../20-Game-Case-Studies/CS-13-Laser-Tag-Reference-Game.md) |

**Use with:** [Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Mechanics Index](Mechanics-Index.md)
