---
title: "Progression Systems"
tags: [progression]
note_type: "topic"
---

# Progression Systems

## Meaningful vs arbitrary progression
| Meaningful | Arbitrary number inflation |
|---|---|
| Upgrade changes behaviour/visuals (bigger throw, new zone, new ability) | "+5 %" with no visible effect |
| Next goal visible with preview | Unknown next step |
| Player chooses between options | Single linear grind |
| Numbers grow **and** world reflects it | Numbers grow, world identical |

Evidence: upgrade baseline with no feedback ([V12](../21-Video-Analyses/V12-Upgrade-Button-Baseline.md)); incremental genre makes numbers the fantasy but ties them to a physical verb ([TI-30](../02-Thumbnails-and-Icons/Analyses/TI-30-Incremental-Genre-Grammar.md)).

## Common Roblox structures (observed in descriptions)
Levels/XP, rebirth/prestige ("Rebirth to grow stronger" — Stone Skipping; Raft Tycoon; Steal a Brainrot), collections with rarity and mutations (Steal An Egg, Fish It!), season/battle passes (Jailbreak UI-04; Fish It! "LIMITED BATTLEPASS"), events with temporary currencies (Adopt Me candy, Brookhaven Candy Corn).

## Rebirth/prestige guidance (hypotheses)
- Rebirth must give a **permanent, visible** advantage (multiplier shown as a badge/aura) and **faster early re-progress**, otherwise it reads as punishment.
- Show "time to recover" estimate before confirming (UI-011 destructive pattern).

## Economy health
Track sources and sinks per currency (Roblox "Balance virtual economies" doc); log with `AnalyticsService:LogEconomyEvent` (verified API name).

## Related
[Progression and Economy Principles](../17-Design-Principles/Progression-and-Economy-Principles.md) · [Reward Presentation](Reward-Presentation.md) · [Game Pass Economy Study](Game-Pass-Economy-Study.md)
