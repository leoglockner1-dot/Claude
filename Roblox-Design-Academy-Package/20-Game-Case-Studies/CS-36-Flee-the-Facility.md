---
title: "CS-36 — Flee the Facility (1 vs 4 asymmetric rounds, one pass, long life)"
tags: [case-study, survival, asymmetric, 1v4, rounds, live-ops]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-36 — Flee the Facility (1 vs 4 asymmetric rounds, one pass, long life)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [Flee the Facility](https://www.roblox.com/games/893973440/) · universe 372226183 · by A.W. Apps |
| Genre (Roblox) | Survival / 1 vs All · max 5 players per server |
| Concurrent players at capture | 49,799 |
| Visits · favourites | 6,102,888,976 · 9,751,571 (1.6 per 1k visits) |
| Like ratio | 92% (2,811,818 up / 241,220 down) |
| Created / updated | 2017-07-01 / 2026-10-24 |
| Game passes for sale | 1 · 420–420 R$ (median 420) · e.g. VIP (420) |

**Developer description (excerpt):** "RUN, HIDE, ESCAPE! Run from the beast, unlock the exits, and flee the facility! This game runs well on phones, tablets, PC, Xbox, and PlayStation. 📋GAME RULES📋 https://devforum.roblox.com/t/flee-the-facility-game-rules/3941301 ⭐CREDITS⭐ https://devforum.roblox.com/t/flee-the-facility-credits/2026108 📄 Latest Update [10/01/26] …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Run, hide, escape: run from the beast, unlock the exits and flee. |
| Main action | [INF] Survivors hack computers and avoid the Beast; the Beast hunts and captures. |
| Immediate feedback | [INF] Hacking progress, capture freezes, exits opening. |
| Reward → new possibility | [INF] Escapes/captures → currency → cosmetics; [DATA] **only 1 pass** (VIP, 420 R$). |
| Micro loop (seconds) | [INF] Stealth/route decisions; hacking task attention. |
| Core loop (minutes) | [INF] round: hack → evade → open exits → escape (or Beast captures all). |
| Meta loop (days) | [DEV] Events (9th Anniversary), trading post, maps; [DEV] change logs posted on DevForum. |

## First-time experience
[DEV] Runs well on phones/tablets/PC/console; rules linked on DevForum.

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | A tight **asymmetric** ruleset (5-player servers) with clear roles; long life (created 2017, 92% likes) with a light monetization surface. |
| Weakest part / quit risks | [INF] Role balance (Beast vs survivors) and new-player skill gaps. |
| Essential features | Asymmetric roles, objective tasks, short rounds. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | One map, 3 computers, Beast vs 3 survivors; test which side wins how often. |

## Reusable lessons
- Asymmetric 1vN rounds create natural tension with small servers.
- Public change logs + events sustain a classic without heavy monetization.

## Original application (do not copy the game)
Museum night: three thieves swap paintings while one guard with a flashlight patrols; light reveals, darkness hides.

## Confidence
Medium.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
