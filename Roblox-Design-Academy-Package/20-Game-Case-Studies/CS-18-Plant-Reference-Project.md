---
title: "CS-18 — Plant (Roblox reference project): simple farming loop with timed hints"
tags: [case-study, simulator, reference-project]
note_type: "case-study"
date_accessed: "2026-10-24"
---

# CS-18 — Plant (Roblox reference project): simple farming loop with timed hints

> Source: <https://create.roblox.com/docs/resources/plant-reference-project> and Onboarding techniques doc.

## Observed (docs)
- Loop: plant seeds → sell produce → invest in larger pots and more valuable plants.
- Timed hints: glow the "PLANT CABBAGE SEED" button after the typical completion time; arrow over the correct market stall ([ONB-05](../13-Onboarding-and-Multiplayer/Onboarding/Analyses/ONB-05-Plant-Timed-Hints.md)).
- Economy UI: "Grow 1 cabbage, 1 s/stage. Sell cabbages for 1c." + "2 Owned" + coin counter.

![Plant timed hint](../Assets/Gameplay/docs/IMP-21_plant-timed-hint-after.jpg)

## Lessons
- State the economy plainly on the action button panel (input → time → output).
- Help only the stuck (ONB-006).

## Confidence
High (official).

## Related
[First Session Design](../13-Onboarding-and-Multiplayer/Onboarding/First-Session-Design.md) · [Onboarding Principles](../17-Design-Principles/Onboarding-Principles.md)
