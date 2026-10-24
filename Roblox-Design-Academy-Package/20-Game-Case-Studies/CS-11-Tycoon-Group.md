---
title: "CS-11 — Tycoons: Mansion Tycoon, Raft Tycoon, Museum Tycoon"
tags: [case-study, tycoon]
note_type: "case-study"
date_accessed: "2026-10-24"
---

# CS-11 — Tycoons: Mansion Tycoon, Raft Tycoon, Museum Tycoon

> **Method:** built from the game's public page data, its own description, its current icon/thumbnails and its game-pass catalogue (Roblox APIs, 2026-10-24). **The games were not played.** Loop descriptions are **inferences** from these sources unless marked otherwise. Popularity is context, not proof of good design.

## Observable data
| Field | Value (2026-10-24) |
|---|---|
| Game | [Mansion Tycoon 🌴🏠](https://www.roblox.com/games/12912731475/) · universe 4518160318 |
| Creator | Capybara's Productions |
| Genre (Roblox) | Simulation / Tycoon |
| Concurrent players at capture | 5,501 |
| Total visits | 663,851,553 |
| Like ratio | 97 % |
| Created / last updated | 2023-03-26 / 2026-09-29 |
| Game passes for sale | 11: Extra Speed (10 R$); Starter Pack (80 R$); Audio System (80 R$); Auto Collect (200 R$); Jetpack (200 R$); VIP (400 R$); Race Cars Pack (400 R$); Luxury Cars Pack (400 R$); Exotic Cars Pack (550 R$); Auto Purchase (600 R$); Double Cash (650 R$) |

**Description excerpt (developer's own words):** "👍 Like and favorite the game to show us you want more mansions! 👍 /  / Build a mansion, penthouse, or yacht, drive cool cars, race your cars at the race track, roleplay with other players, and so much more in this epic mansion tycoon!  /  / 🔔 Press the follow button so you don't miss out when new updates drop! /  / 🌟 Premium users earn 20% more money! 🌟 / 🌟 Join the Capybara's Productions group and verify in the game to receive a…"

![mansion-tycoon__u4518160318.jpg](../Assets/Icons/live-2026-10-24/mansion-tycoon__u4518160318.jpg)
![mansion-tycoon__u4518160318__00.jpg](../Assets/Thumbnails/live-2026-10-24/mansion-tycoon__u4518160318__00.jpg)

| Field | Value (2026-10-24) |
|---|---|
| Game | [🌊 Raft Tycoon](https://www.roblox.com/games/76137189788863/) · universe 7082423811 |
| Creator | Flappy Bit Games |
| Genre (Roblox) | Simulation / Tycoon |
| Concurrent players at capture | 1,430 |
| Total visits | 305,405,376 |
| Like ratio | 95 % |
| Created / last updated | 2025-01-13 / 2026-10-24 |
| Game passes for sale | 15: Run Boost (1 R$); Jump Boost (2 R$); Double Cash (3 R$); Kayak (19 R$); Golden Sword (24 R$); Starter Pack (49 R$); Auto Collect (99 R$); AH-64 Helicopter (149 R$); Race Boat (149 R$); Sleigh (149 R$); Titanic (199 R$); Aircraft Carrier (345 R$) … |

**Description excerpt (developer's own words):** "Welcome to Raft Tycoon!🌊 / Start small and build the ultimate floating empire! Expand your raft, collect resources, and upgrade your setup while surviving the open sea. But beware—sharks are always nearby! /  / 💾 Auto-saving progress. / 🔁 Rebirth system to progress faster. / 🤗 Playing with friends gives everyone bonuses! (10% per friend) / 🎟️ Special passes with exclusive perks. /  / 🔓 Redeem codes to get rewards: / FLAPPY, SEASIDE, C…"

![raft-tycoon__u7082423811.jpg](../Assets/Icons/live-2026-10-24/raft-tycoon__u7082423811.jpg)
![raft-tycoon__u7082423811__00.jpg](../Assets/Thumbnails/live-2026-10-24/raft-tycoon__u7082423811__00.jpg)

| Field | Value (2026-10-24) |
|---|---|
| Game | [Museum Tycoon🏛️](https://www.roblox.com/games/9802068147/) · universe 3627275994 |
| Creator | Zoomy Studios |
| Genre (Roblox) | Simulation / Tycoon |
| Concurrent players at capture | 45 |
| Total visits | 34,612,760 |
| Like ratio | 90 % |
| Created / last updated | 2022-06-03 / 2026-10-21 |
| Game passes for sale | 7: Super Speed (49 R$); Fly (199 R$); Auto Collect Cash (299 R$); VIP (399 R$); x2 Cash (399 R$); Super Cars (499 R$); T-Rex Exhibit (699 R$) |

**Description excerpt (developer's own words):** "✨Check out the new William and Charlotte Bloomberg Public Science Common! /  / 👋Welcome to Museum Tycoon with the Museum of Science! You’ve visited museums. Now you get to build one. 🏛️ / Explore two full floors of the real-life Museum of Science's Blue Wing and shape your own museum — filled with exhibits that spark curiosity and reward discovery.  /  / 🦖Unlock new exhibits to increase your income!  / 🤑Collect money from kiosks…"

![museum-tycoon__u3627275994.jpg](../Assets/Icons/live-2026-10-24/museum-tycoon__u3627275994.jpg)
![museum-tycoon__u3627275994__00.jpg](../Assets/Thumbnails/live-2026-10-24/museum-tycoon__u3627275994__00.jpg)


## Loop breakdown (inferred)
| Layer | Inference |
|---|---|
| Minute-to-minute | Collect income, walk onto buy pads |
| Most repeated action | Buy the next part (green pad + price) |
| Progression engine | Bigger build → more income; rebirths (Raft) |
| Social loop | Raft Tycoon: "Playing with friends gives everyone bonuses! (10 % per friend)"; Mansion Tycoon: race track, roleplay |
| Monetization | Auto Collect, Auto Build/Purchase, Double Cash, vehicles; **Raft Tycoon lists passes at 1–3 R$** (Run Boost 1, Jump Boost 2, Double Cash 3) — unusual; may be regional pricing or a promotion, cause unknown |

## What appears to work
- Mechanic + aspiration in thumbnails ([TI-21](../02-Thumbnails-and-Icons/Analyses/TI-21-Tycoon-Buy-Pad-Grammar.md)).
- Very high like ratios (Mansion 97 %, Raft 95 %, Museum 90 %).
- Museum Tycoon partners with a real museum (Museum of Science) — educational theme.

## Risks, weaknesses or open questions
- Automation passes (Auto Collect/Build) monetize skipping the loop itself — watch that the loop remains fun without them (opinion).

## Lessons for our games
- Friend bonuses are a clean social incentive (SOCIAL-001).

## Original application
A lighthouse-network tycoon: each lighthouse you build lights a new sea lane for ships that pay tolls; friends' lighthouses connect lanes for shared bonuses.

## Confidence
Medium.

## Related
[TI 21 Tycoon Buy Pad Grammar](../02-Thumbnails-and-Icons/Analyses/TI-21-Tycoon-Buy-Pad-Grammar.md) · [Social Principles](../17-Design-Principles/Social-Principles.md)
