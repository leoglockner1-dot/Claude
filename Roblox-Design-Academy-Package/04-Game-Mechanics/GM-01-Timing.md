---
title: "GM-01 — Timing"
tags: [mechanic, game-design]
note_type: "mechanic"
evidence: "academy synthesis; Roblox-specific constraints from official docs; examples from case studies (see Evidence row)"
---

# GM-01 — Timing

| Aspect | Notes |
|---|---|
| **What the player does** | Acts at the right moment: jump at a gap edge, hit a note, sit when music stops, parry a swing. |
| **Skill or decision involved** | Perception and motor timing; anticipation of patterns. |
| **Feedback needed** | Instant (<100 ms) confirmation with graded quality (Perfect/Good/Miss), sound on hit, visible windows or tells before the moment. |
| **Why it can be satisfying** | Mastery is felt directly: the player improves and *knows* it. Near-misses invite retries. |
| **Design conditions under which it works** | The cue must be readable (visual + audio, never audio-only, [V04](../21-Video-Analyses/V04-Sound-Reliance-Phone.md)). Timing windows must survive network latency: judge timing on the **client** for feel, validate plausibility on the server (rate, sequence), never trust the client for rewards ([LU-03](../07-Roblox-Studio-and-Luau/LU-03-Client-Server-Responsibilities.md)). |
| **How difficulty can scale** | Narrower windows, faster tempo, overlapping cues, fake-outs, combining with movement. |
| **How progression can change it** | Unlock new patterns, longer combos, modifiers (double time), forgiving windows as a purchasable *accessibility* option (not power). |
| **What causes repetition fatigue** | Same pattern repeated; windows so wide that skill does not matter; so narrow that it feels random on mobile. |
| **Exploits and edge cases (Roblox-specific where relevant)** | Autoclickers/macros; latency abuse in PvP; frame-rate-dependent windows (use time, not frames). |
| **Genres it fits** | Rhythm, platformers, fishing/reeling, combat parries, party elimination games. |
| **Genres it does not fit (or fits badly)** | Idle/management games where players expect to look away; very high-latency multiplayer interactions. |
| **Original variations** | Timing to a *visual* rhythm (lighthouse flashes); cooperative timing (two players must press within 0.2 s). |
| **Prototype and testing guidance** | One cue, three window sizes; measure hit rate per device (PC vs phone) and adjust until mobile Good-rate ≥ 70% at the easiest tier. |
| **Examples in this academy (evidence)** | [CS-52 Funky Friday](../20-Game-Case-Studies/CS-52-Funky-Friday.md) · [CS-44 Musical Chairs](../20-Game-Case-Studies/CS-44-Musical-Chairs.md) · [CS-22 Fisch](../20-Game-Case-Studies/CS-22-Fisch.md) (reeling) · [V19 hold duration](../21-Video-Analyses/V19-Proximity-Hold-Duration.md) |

**Use with:** [Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Mechanics Index](Mechanics-Index.md)
