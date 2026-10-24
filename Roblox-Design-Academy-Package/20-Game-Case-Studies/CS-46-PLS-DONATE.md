---
title: "CS-46 — PLS DONATE (social economy where the "game" is other players)"
tags: [case-study, social, economy, booths, robux]
note_type: "case-study"
date_accessed: "2026-10-24"
evidence_level: "public data + developer description; gameplay NOT observed"
---

# CS-46 — PLS DONATE (social economy where the "game" is other players)

> **Method.** Built from Roblox API data (2026-10-24), the developer's own description, the game-pass catalogue and, where cited, developer posts. **The game was not played** (no Studio or client in this environment; video sites blocked). Tags: **[DEV]** stated by the developer or the page, **[DATA]** API data, **[INF]** inference, **[HYP]** hypothesis to test. Popularity is context, not proof of good design.

## Data (2026-10-24)
| Field | Value |
|---|---|
| Game | [PLS DONATE 💸](https://www.roblox.com/games/8737602449/) · universe 3317679266 · by Quataun |
| Genre (Roblox) | Social / – · max 28 players per server |
| Concurrent players at capture | 2,725 |
| Visits · favourites | 5,255,420,733 · 4,448,929 (0.85 per 1k visits) |
| Like ratio | 93% (3,701,654 up / 280,031 down) |
| Created / updated | 2022-02-05 / 2026-08-16 |
| Game passes for sale | 7 · 49–100000 R$ (median 399) · e.g. Donation Sign (99), Cloaking Device (399), Golf Cart (499), Booth Painter (699), Disguise Mask (299), Boombox Control (49), Gigantic Donation Sign (100000) |

**Developer description (excerpt):** "💸 PLS DONATE is a game where you can raise Robux or donate Robux to others! How to Play: 🎪 Claim a booth 📝 Customize your booth text 💰 Receive Robux from other players! 💸 Donate Robux to other players! ⚠️ Notes: • Roblox Plus subscription is required to donate Robux. • Robux transfers are limited to 500/day and 1,000/month. …"

## Loop analysis
| Layer | Analysis |
|---|---|
| One-sentence premise | [DEV] Claim a booth, customize the text, receive or donate Robux. |
| Main action | [DEV] Claim booth, edit sign, interact with others. |
| Immediate feedback | [INF] Donation announcements and effects. |
| Reward → new possibility | [DEV] Robux from other players; [DATA] passes for booth customization (Donation Sign 99, Booth Painter 699) and status items. |
| Micro loop (seconds) | [INF] Social persuasion, presentation of your booth. |
| Core loop (minutes) | [INF] claim booth → attract attention → receive/donate. |
| Meta loop (days) | [INF] Status, leaderboards (not verified); [DEV] notes Roblox transfer limits and age requirements. |

## First-time experience
[DEV] 3-step How to Play.

## Critical analysis
| Question | Answer |
|---|---|
| Strongest part | A **social space with one clear purpose** and minimal UI (see [UI-26](../01-UI-UX/Analyses/UI-26-DevForum-Pls-Donate-and-Color-Place-Minimal-UI.md)). |
| Weakest part / quit risks | [DEV] Depends on platform transfer rules (limits, Roblox Plus subscription to donate, parental approval for under-18s) - external constraints shape the loop. |
| Essential features | Booths, sign customization, donation flow. |
| Possibly unnecessary | Cannot judge. |
| Minimal prototype to test the idea | Not a recommended template; study it for social presentation design. |

## Reusable lessons
- Social games can be built around one interaction if presentation tools are rich.
- When a loop depends on platform policy, document the rules in-game.

## Original application (do not copy the game)
A street-performer plaza: players perform emotes/music on stages and earn in-game tips for cosmetics (no Robux transfer).

## Confidence
Medium.

## Related
[Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) · [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md)
