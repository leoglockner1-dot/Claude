# Reference IMP-21 — Plant (Roblox Reference Project): Timed Hints

## Metadata
- Category: Gameplay / Onboarding
- Source: Roblox Creator Docs, "Onboarding techniques" > Timed hints. Project: https://create.roblox.com/docs/resources/plant-reference-project
- Asset: `../Assets/Gameplay/IMP-21_plant-timed-hint-before.png`, `../Assets/Gameplay/IMP-21_plant-timed-hint-after.png`, `../Assets/Gameplay/IMP-21_plant-stall-hint-before.png`, `../Assets/Gameplay/IMP-21_plant-stall-hint-after.png`
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

## Application to Roblox Development
Use `task.delay(hintDelay, showHintIfNotDone)` per step. Put the delay in a Config so it can be tuned live (Roblox suggests A/B testing delays with Experiments).

## Related Notes
[Retention and Replayability](../05_Game_Design/Retention_and_Replayability.md) · [Core Loop Review](../09_Quality_Checklists/Core_Loop_Review.md)
