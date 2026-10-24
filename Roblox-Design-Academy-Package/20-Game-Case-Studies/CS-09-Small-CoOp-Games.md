---
title: "CS-09 — Small co-op obbies: Be My Camera, Webbed!, Teamwork Puzzles"
tags: [case-study, co-op, obby]
note_type: "case-study"
date_accessed: "2026-10-24"
---

# CS-09 — Small co-op obbies: Be My Camera, Webbed!, Teamwork Puzzles

> **Method:** built from the game's public page data, its own description, its current icon/thumbnails and its game-pass catalogue (Roblox APIs, 2026-10-24). **The games were not played.** Loop descriptions are **inferences** from these sources unless marked otherwise. Popularity is context, not proof of good design.

## Observable data
| Field | Value (2026-10-24) |
|---|---|
| Game | [Be My Camera \[2 Player Obby\]](https://www.roblox.com/games/95205997597502/) · universe 7145230420 |
| Creator | Obby Republic |
| Genre (Roblox) | Obby & Platformer / – |
| Concurrent players at capture | 604 |
| Total visits | 53,056,916 |
| Like ratio | 58 % |
| Created / last updated | 2025-01-25 / 2026-09-21 |
| Game passes for sale | 9: Starter Pack (29 R$); Lava Protection (59 R$); Speed Coil (89 R$); Falcon (99 R$); Gravity Coil (129 R$); Ultimate Coil (199 R$); One Shot (199 R$); Enemy Drones Skin Pack (279 R$); VIP (349 R$) |

**Description excerpt (developer's own words):** "🎥 Be your friend's eyes 👀 / One of you jumps through the obby while the other controls the camera and protects them with lasers! /  / 👀 work together to make it to the end. / 📷 One player sees everything and fights evil drones, and the other does the jumping. / 🧠 Talk, guide each other, you need real teamwork for this obby! /  / FREE VIP SERVERS! / 🛠 UPDATE 1 /  - Skins /  - Camera sensitivity slider! /  / tags: 2 player obby, teamwork, car…"

![be-my-camera__u7145230420.jpg](../Assets/Icons/live-2026-10-24/be-my-camera__u7145230420.jpg)
![be-my-camera__u7145230420__00.jpg](../Assets/Thumbnails/live-2026-10-24/be-my-camera__u7145230420__00.jpg)

| Field | Value (2026-10-24) |
|---|---|
| Game | [Webbed! ❄️ \[2 Player Obby\]](https://www.roblox.com/games/132586479415502/) · universe 7364297396 |
| Creator | studio arsenic |
| Genre (Roblox) | Obby & Platformer / – |
| Concurrent players at capture | 5,246 |
| Total visits | 472,411,389 |
| Like ratio | 87 % |
| Created / last updated | 2025-03-11 / 2026-07-04 |
| Game passes for sale | 0 |

**Description excerpt (developer's own words):** "⚠️THIS GAME IS MADE FOR 2 PLAYERS⚠️ /  / The two spiders 🕷️ have become webbed together 🕸️,  and only through teamwork  can they overcome the tricky terrains ahead. In this 2-player obby, each spider can cling to walls and swing across gaps by shooting their web. /  / 🎁 LIKE AND JOIN THE GROUP FOR A FREE REVIVE 🎁 /  / 🛠 If you experience lag, it is recommended you switch to a private server (free).…"

![webbed__u7364297396.jpg](../Assets/Icons/live-2026-10-24/webbed__u7364297396.jpg)
![webbed__u7364297396__00.jpg](../Assets/Thumbnails/live-2026-10-24/webbed__u7364297396__00.jpg)

| Field | Value (2026-10-24) |
|---|---|
| Game | [Teamwork Puzzles (Obby)](https://www.roblox.com/games/13184713709/) · universe 4599924264 |
| Creator | LemonBread Studios |
| Genre (Roblox) | Obby & Platformer / – |
| Concurrent players at capture | 3,002 |
| Total visits | 739,130,481 |
| Like ratio | 49 % |
| Created / last updated | 2023-04-19 / 2026-10-13 |
| Game passes for sale | 5: Gravity Coil (199 R$); Checkpoints (399 R$); Double Coins (399 R$); Portable Noob (499 R$); Magic Carpet (799 R$) |

**Description excerpt (developer's own words):** "🧩 Team up with up to 3 players to solve puzzles and beat obstacle courses! /  / Don't leave anybody behind because you will need them later. Earn coins to unlock special trails or replay stages for a faster time. Play with friends for the best experience! /  / 🏆 RIA 2025 Best Puzzle Experience…"

![teamwork-puzzles__u4599924264.jpg](../Assets/Icons/live-2026-10-24/teamwork-puzzles__u4599924264.jpg)
![teamwork-puzzles__u4599924264__00.jpg](../Assets/Thumbnails/live-2026-10-24/teamwork-puzzles__u4599924264__00.jpg)


## Loop breakdown (inferred)
| Game | Inferred loop |
|---|---|
| Be My Camera | Asymmetric: one jumps blind, the other controls the camera and shoots drones (description) |
| Webbed! | Two spiders tethered; cling and swing via webs; "made for 2 players" |
| Teamwork Puzzles | Up to 3 players solve puzzle obstacles; coins for trails; replay for time |

## What appears to work
- Each states its co-op rule in title + thumbnail ([TI-22](../02-Thumbnails-and-Icons/Analyses/TI-22-Asymmetric-CoOp-Explained-In-One-Image.md)).
- Several offer free private servers — supports playing with a friend.

## Risks, weaknesses or open questions
- Like ratios vary widely: Webbed! 87 %, Be My Camera 58 %, Teamwork Puzzles 49 % — a clear premise does not guarantee satisfaction; solo arrivals in a 2-player game is a likely pain point (hypothesis, SOCIAL-003).

## Lessons for our games
- Strict co-op needs effortless partner matching or a solo fallback.

## Original application
A two-player "Bridge Builders": one carries planks, the other places them; solo mode gives an NPC helper with simple commands.

## Confidence
Medium.

## Related
[Low Population Design](../13-Onboarding-and-Multiplayer/Multiplayer/Low-Population-Design.md) · [Social Principles](../17-Design-Principles/Social-Principles.md)
