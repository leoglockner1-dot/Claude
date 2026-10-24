---
title: "Core Loop Principles (LOOP-001 – LOOP-008)"
tags: [principles, core-loop]
note_type: "principles"
---

# Core Loop Principles (LOOP-001 – LOOP-008)

Principles for the gameplay loop. Loops of live games are **inferred** from descriptions/thumbnails unless stated; see case studies.

| ID | Principle | Confidence |
|---|---|---|
| LOOP-001 | Name the three layers | High |
| LOOP-002 | Core verb within the first minute | Medium |
| LOOP-003 | One verb, many contexts | Medium |
| LOOP-004 | Every system feeds the loop | Medium |
| LOOP-005 | Visible stakes in each cycle | Medium |
| LOOP-006 | Short rounds for tourists, depth for locals | Medium |
| LOOP-007 | Variety through generation or rotation | Medium |
| LOOP-008 | Measure, then iterate the loop | High |

## LOOP-001 — Name the three layers
**Rule:** Write down minute-to-minute action, most repeated action set and progression engine before building anything else.

- **Reasoning:** Roblox core-loop framework.
- **Evidence:** [Core Loop Framework](../03-Core-Gameplay-Loops/Core-Loop-Framework.md)
- **Good application:** 99 Nights description: "Build a camp with friends. Something is watching you." — survive nights → build camp.
- **Failure mode:** Systems added without a loop map.
- **Conditions & exceptions:** —
- **Roblox implementation:** Loop diagram in project note; every feature mapped to a layer.
- **Confidence:** High
- **Tags:** #core-loop

## LOOP-002 — Core verb within the first minute
**Rule:** New players perform the core verb within ~60 s without reading.

- **Reasoning:** DevForum funnels: 48 % leave at a forced shop step; 97 % never reach floor 2 when the core is not engaging.
- **Evidence:** [ONB 06 DevForum Forced Blur Tutorial Funnel](../09-Onboarding/Analyses/ONB-06-DevForum-Forced-Blur-Tutorial-Funnel.md), [CS 16 Troll Tower Obby Funnel](../15-Game-Case-Studies/CS-16-Troll-Tower-Obby-Funnel.md)
- **Good application:** Party games start a round immediately.
- **Failure mode:** Shop tutorial before climbing in a tower obby.
- **Conditions & exceptions:** —
- **Roblox implementation:** Spawn facing the first interaction; funnel step "first core action".
- **Confidence:** Medium
- **Tags:** #core-loop #onboarding

## LOOP-003 — One verb, many contexts
**Rule:** Depth comes from new contexts for the same verb (targets, hazards, combos), not new systems.

- **Reasoning:** Simple mechanics with depth retain; feature bloat confuses.
- **Evidence:** [CS 05 Tower of Hell](../15-Game-Case-Studies/CS-05-Tower-of-Hell.md), [CS 02 RIVALS](../15-Game-Case-Studies/CS-02-RIVALS.md)
- **Good application:** Tower of Hell: climb, randomized sections.
- **Failure mode:** Five unrelated mini-systems in session one.
- **Conditions & exceptions:** Social sandboxes are tool-driven rather than verb-driven.
- **Roblox implementation:** Content pipeline producing variants of the verb.
- **Confidence:** Medium
- **Tags:** #core-loop

## LOOP-004 — Every system feeds the loop
**Rule:** Each feature answers which loop step it strengthens; orphan systems are cut.

- **Reasoning:** Prevents bloat.
- **Evidence:** [Core Loop Framework](../03-Core-Gameplay-Loops/Core-Loop-Framework.md)
- **Good application:** Steal-a-Brainrot description lists buy → steal → generate money → rebirth.
- **Failure mode:** Daily spin unrelated to anything.
- **Conditions & exceptions:** Social/cosmetic systems feed the "show off" social loop.
- **Roblox implementation:** Feature table: system → loop step → metric.
- **Confidence:** Medium
- **Tags:** #core-loop

## LOOP-005 — Visible stakes in each cycle
**Rule:** Each cycle should have something to lose or gain visibly (timer, rival, threat).

- **Reasoning:** Tension sustains repetition.
- **Evidence:** [CS 10 Party Round Games](../15-Game-Case-Studies/CS-10-Party-Round-Games.md), [CS 04 Steal Loop Games](../15-Game-Case-Studies/CS-04-Steal-Loop-Games.md)
- **Good application:** Hot potato countdown; others can steal your items.
- **Failure mode:** Pure grind with no risk or comparison.
- **Conditions & exceptions:** Cozy games use aspiration instead of risk.
- **Roblox implementation:** Round timers, PvP steal windows, leaderboards.
- **Confidence:** Medium
- **Tags:** #core-loop

## LOOP-006 — Short rounds for tourists, depth for locals
**Rule:** Offer complete sessions in minutes while keeping long-term goals for returning players.

- **Reasoning:** Roblox: sessions hop between games; tourists vs locals.
- **Evidence:** [Low Population Design](../10-Multiplayer-Design/Low-Population-Design.md), [CS 10 Party Round Games](../15-Game-Case-Studies/CS-10-Party-Round-Games.md)
- **Good application:** Round-based party games + unlockables.
- **Failure mode:** 30-minute mandatory intro.
- **Conditions & exceptions:** —
- **Roblox implementation:** Round length config; persistent unlocks.
- **Confidence:** Medium
- **Tags:** #core-loop #retention

## LOOP-007 — Variety through generation or rotation
**Rule:** Replayability comes from randomised/rotating content within the same verb.

- **Reasoning:** Tower of Hell markets randomised towers.
- **Evidence:** [TI 26 Tower of Hell Feature Caption](../02-Thumbnails-and-Icons/Analyses/TI-26-Tower-of-Hell-Feature-Caption.md)
- **Good application:** Random sections, rotating maps.
- **Failure mode:** One fixed level.
- **Conditions & exceptions:** Handcrafted story games trade replay for narrative.
- **Roblox implementation:** Modular section library + seeded generation.
- **Confidence:** Medium
- **Tags:** #core-loop

## LOOP-008 — Measure, then iterate the loop
**Rule:** Instrument funnels per step and iterate one change at a time.

- **Reasoning:** Roblox recommends funnels and Experiments; DevForum data shows how leaks locate problems.
- **Evidence:** [Onboarding Evidence From Developers](../09-Onboarding/Onboarding-Evidence-From-Developers.md), [Analytics and Experiments](../11-Roblox-Technical-Reference/Analytics-and-Experiments.md)
- **Good application:** Funnel identified the 48 % churn step.
- **Failure mode:** Changing five things after a bad day of ads.
- **Conditions & exceptions:** —
- **Roblox implementation:** `AnalyticsService:LogOnboardingFunnelStepEvent`, `LogFunnelStepEvent`, Experiments.
- **Confidence:** High
- **Tags:** #analytics
