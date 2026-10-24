---
title: "Plant (Roblox Reference Project): Timed Hints"
tags: [reference, onboarding]
reference_type: "image-analysis"
source_ref: "IMP-21 (earlier import package)"
date_accessed: "2026-10-24"
---

# Plant (Roblox Reference Project): Timed Hints

## Metadata
- Category: Gameplay / Onboarding
- Source: Roblox Creator Docs, "Onboarding techniques" > Timed hints. Project: https://create.roblox.com/docs/resources/plant-reference-project
- Asset: see images below

![IMP-21_plant-timed-hint-before](../../../Assets/Gameplay/docs/IMP-21_plant-timed-hint-before.jpg)
![IMP-21_plant-timed-hint-after](../../../Assets/Gameplay/docs/IMP-21_plant-timed-hint-after.jpg)
![IMP-21_plant-stall-hint-before](../../../Assets/Gameplay/docs/IMP-21_plant-stall-hint-before.jpg)
![IMP-21_plant-stall-hint-after](../../../Assets/Gameplay/docs/IMP-21_plant-stall-hint-after.jpg)

- Date added: 2026-10-24
- Rating: 4.5/5
- Confidence: High. Roblox made the example, though its 10/11-second numbers are described as hypothetical.
- Reference type: Positive

## Context
1. The "PLANT CABBAGE SEED" button gains a glowing yellow outline if the player hasn't pressed it after a while.
2. After harvesting, a cyan arrow appears above the correct market stall if the player hasn't found it.

## What Works
- **Help only for players who need it.** Experienced players never see the hint. Roblox's hypothetical: if most players press within 10 s, show the hint at 11 s.
- **Shown once**, the first time the task appears.
- The hint is an **outline glow / arrow**, not a popup. It adds information without interrupting.

## Reusable Design Rules
1. For every onboarding step, measure the typical completion time in playtests, then show a visual hint just after it.
2. Hint = highlight or arrow on the target. Escalate to text only if the player is still stuck.
3. Show it once, and remove it on completion.

## Roblox implementation
Use `task.delay(hintDelay, showHintIfNotDone)` per step. Put the delay in a Config so it can be tuned live (Roblox suggests A/B testing delays with Experiments).

## Original application
A parkour tutorial that highlights the wall-run glyph only if the player has not wall-run within 15 s of reaching the first wall.

## Related
[Retention and Replayability](../First-Session-Design.md) · [Core Loop Review](../../../23-Quality-Checklists/CL-04-Core-Loop-Review.md)
