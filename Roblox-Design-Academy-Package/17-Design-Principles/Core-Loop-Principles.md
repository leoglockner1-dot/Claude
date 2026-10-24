---
title: "Core Loop Principles (LOOP-001 – LOOP-016)"
tags: [principles, core-loop]
note_type: "principles"
---

# Core Loop Principles (LOOP-001 – LOOP-016)

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
| LOOP-009 | Build return triggers into the loop | Medium |
| LOOP-010 | Unlocks should change how you play | Medium |
| LOOP-011 | Design the stranger and solo experience | Medium |
| LOOP-012 | Change the verb and say it in the name | Medium |
| LOOP-013 | Read current health next to historic success | Medium |
| LOOP-014 | Variety through combinations | Medium |
| LOOP-015 | Measure new players separately | Medium |
| LOOP-016 | Test loop variables with experiments | Medium |

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
- **Evidence:** [ONB 06 DevForum Forced Blur Tutorial Funnel](../13-Onboarding-and-Multiplayer/Onboarding/Analyses/ONB-06-DevForum-Forced-Blur-Tutorial-Funnel.md), [CS 16 Troll Tower Obby Funnel](../20-Game-Case-Studies/CS-16-Troll-Tower-Obby-Funnel.md)
- **Good application:** Party games start a round immediately.
- **Failure mode:** Shop tutorial before climbing in a tower obby.
- **Conditions & exceptions:** —
- **Roblox implementation:** Spawn facing the first interaction; funnel step "first core action".
- **Confidence:** Medium
- **Tags:** #core-loop #onboarding

## LOOP-003 — One verb, many contexts
**Rule:** Depth comes from new contexts for the same verb (targets, hazards, combos), not new systems.

- **Reasoning:** Simple mechanics with depth retain; feature bloat confuses.
- **Evidence:** [CS 05 Tower of Hell](../20-Game-Case-Studies/CS-05-Tower-of-Hell.md), [CS 02 RIVALS](../20-Game-Case-Studies/CS-02-RIVALS.md)
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
- **Evidence:** [CS 10 Party Round Games](../20-Game-Case-Studies/CS-10-Party-Round-Games.md), [CS 04 Steal Loop Games](../20-Game-Case-Studies/CS-04-Steal-Loop-Games.md)
- **Good application:** Hot potato countdown; others can steal your items.
- **Failure mode:** Pure grind with no risk or comparison.
- **Conditions & exceptions:** Cozy games use aspiration instead of risk.
- **Roblox implementation:** Round timers, PvP steal windows, leaderboards.
- **Confidence:** Medium
- **Tags:** #core-loop

## LOOP-006 — Short rounds for tourists, depth for locals
**Rule:** Offer complete sessions in minutes while keeping long-term goals for returning players.

- **Reasoning:** Roblox: sessions hop between games; tourists vs locals.
- **Evidence:** [Low Population Design](../13-Onboarding-and-Multiplayer/Multiplayer/Low-Population-Design.md), [CS 10 Party Round Games](../20-Game-Case-Studies/CS-10-Party-Round-Games.md)
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
- **Evidence:** [Onboarding Evidence From Developers](../13-Onboarding-and-Multiplayer/Onboarding/Onboarding-Evidence-From-Developers.md), [Analytics and Experiments](../14-Technical-Reference/Analytics-and-Experiments.md)
- **Good application:** Funnel identified the 48 % churn step.
- **Failure mode:** Changing five things after a bad day of ads.
- **Conditions & exceptions:** —
- **Roblox implementation:** `AnalyticsService:LogOnboardingFunnelStepEvent`, `LogFunnelStepEvent`, Experiments.
- **Confidence:** High
- **Tags:** #analytics

# Added in Academy 2.0

## LOOP-009 — Build return triggers into the loop
**Rule:** Give the core loop at least one built-in reason to come back tomorrow (offline growth, restocks, appointments, episodes, a persistent creation).

- **Reasoning:** Roblox Home recommendations (2026) weigh D1, D2–7 and D8–28 retention.
- **Evidence:** [Case-Study-Index P1](../20-Game-Case-Studies/Case-Study-Index.md); [RFY post](https://devforum.roblox.com/t/recommended-for-you-algorithm-improvements-that-better-value-long-term-retention/4684575)
- **Good application:** Grow a Garden offline growth + restocks ([CS-21](../20-Game-Case-Studies/CS-21-Grow-a-Garden.md)).
- **Failure mode:** [FC-GD-01](../15-Anti-Patterns-and-Failure-Cases/Failures-Documented/FC-GD-01-Troll-Outfit-Tower-Retention-Collapse.md): fun exhausted in one session.
- **Conditions & exceptions:** Finite story games may accept low long-term retention by design (Dig to Escape states 30–60 min).
- **Roblox implementation:** Server timestamps for offline progress ([LU-08](../07-Roblox-Studio-and-Luau/LU-08-Player-Data-Persistence.md)); a fixed weekly update slot.

## LOOP-010 — Unlocks should change how you play
**Rule:** Prefer rewards that add options, rules or places over rewards that only raise numbers.

- **Reasoning:** Number-only progression stops feeling different; rule changes renew decisions.
- **Evidence:** Blox Fruits movesets, Fisch locations, Bee Swarm fields vs the decline of Mining Simulator 2 (P3).
- **Good application:** Species that change pool rules in [Core Loop Library A](../03-Core-Gameplay-Loops/Core-Loop-Library.md).
- **Failure mode:** Upgrade screens full of +10%.
- **Conditions & exceptions:** Incremental genres can use numbers as the *pace*, as long as milestones add new mechanics.
- **Roblox implementation:** Framework field 5 "new possibility" must not read "bigger number".

## LOOP-011 — Design the stranger and solo experience
**Rule:** Any cooperative mechanic must have a plan for AFK, trolls, mismatched skill and solo players.

- **Reasoning:** Hard dependency on random partners correlates with the lowest like ratios in the sample.
- **Evidence:** Teamwork Puzzles 49%, Be My Camera 58% vs Webbed 87% ([P5](../20-Game-Case-Studies/Case-Study-Index.md)).
- **Good application:** Solo fallback with bots carrying heavy parts slowly ([Concept B](../03-Core-Gameplay-Loops/Core-Loop-Library.md)).
- **Failure mode:** A run that cannot progress because one partner left.
- **Conditions & exceptions:** Friends-only experiences can state the requirement clearly (Webbed: "MADE FOR 2 PLAYERS").
- **Roblox implementation:** Vote-kick/partner swap; bot fill; optional rather than mandatory dependencies.

## LOOP-012 — Change the verb and say it in the name
**Rule:** In a crowded genre, differentiate through a changed core action, and make the name/thumbnail state it.

- **Reasoning:** Players decide in seconds; "just another X" loses them.
- **Evidence:** Obby But You're On a Bike (highest favourites per visit of the obbies); [FC-GD-04](../15-Anti-Patterns-and-Failure-Cases/Failures-Documented/FC-GD-04-Rising-Empires-Generic-First-Impression.md).
- **Good application:** "Obsidian Rush": mining where the ground melts under you.
- **Failure mode:** A theme swap on an unchanged genre loop.
- **Conditions & exceptions:** Brand-led sequels can rely on recognition instead.
- **Roblox implementation:** Title + thumbnail brief states the twist ([Thumbnail Brief Template](../02-Thumbnails-and-Icons/Thumbnail-Brief-Template.md)).

## LOOP-013 — Read current health next to historic success
**Rule:** When studying a reference game, read CCU and the last update date next to visits and likes.

- **Reasoning:** Visits and likes accumulate; they describe the past.
- **Evidence:** Mining Simulator 2: 210M visits, 93% likes, 25 CCU (P11).
- **Good application:** Case studies record CCU at capture and update dates.
- **Failure mode:** Copying a design that worked in 2022 and no longer retains.
- **Conditions & exceptions:** —
- **Roblox implementation:** Use the games API fields `playing` and `updated` ([Game Data Sources](../22-Source-Library/Game-Data-Sources.md)).

## LOOP-014 — Variety through combinations
**Rule:** Get variety by combining a few contents (maps × events × modifiers) rather than authoring long lists.

- **Reasoning:** Combinations multiply cheaply and stay learnable.
- **Evidence:** Natural Disaster Survival, Tower of Hell (P9).
- **Good application:** Volcano vents randomized per run (Concept B).
- **Failure mode:** 50 unique levels nobody replays.
- **Conditions & exceptions:** Story games need authored content.
- **Roblox implementation:** Seeded generation; modifiers as data tables.

## LOOP-015 — Measure new players separately
**Rule:** Evaluate the first-session funnel of new players separately from veteran engagement and from paid traffic.

- **Reasoning:** Averages hide distributions; ad traffic behaves differently (developer measurement).
- **Evidence:** [FC-GD-06](../15-Anti-Patterns-and-Failure-Cases/Failures-Documented/FC-GD-06-Asymmetric-Survival-Engaged-Core-Low-D1.md) and the linked ads report.
- **Good application:** Funnel events: joined → first action → first reward → first upgrade.
- **Failure mode:** "My friends love it" while D1 is 3%.
- **Conditions & exceptions:** —
- **Roblox implementation:** Creator Analytics funnels and acquisition sources; custom analytics events ([Analytics and Experiments](../14-Technical-Reference/Analytics-and-Experiments.md)).

## LOOP-016 — Test loop variables with experiments
**Rule:** Choose a loop variable (difficulty, reward timing, progression structure) and A/B test it instead of debating it.

- **Reasoning:** Roblox reports ~1 in 4 of 1,000+ experiments gave a significant playtime lift (avg ~5%).
- **Evidence:** [Experiments post](https://devforum.roblox.com/t/running-successful-experiments-insights-from-top-creators/4549276): end-of-level free reward +12.5% playtime, +5.3% D1; level-based progression +10% D1.
- **Good application:** Test Concept C's banking reward curve.
- **Failure mode:** Shipping big redesigns on intuition only.
- **Conditions & exceptions:** Needs enough traffic for significance.
- **Roblox implementation:** Configs + Experiments in Creator Hub.
