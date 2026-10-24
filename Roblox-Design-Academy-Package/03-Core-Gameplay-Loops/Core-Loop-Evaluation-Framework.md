---
title: "Core Loop Evaluation Framework (use before adding systems)"
tags: [core-loop, framework, game-design, prototype, playtest]
note_type: "framework"
evidence: "Roblox docs (core loops) + official 2026 discovery/experiment posts + documented developer failures"
---

# Core Loop Evaluation Framework

**Use this before building anything beyond a prototype.** A concept is not good because it sounds creative. It is promising when you can say *why the repeated action is engaging*, *what makes the next repetition different*, and *how a playtest could prove you wrong*.

## Why this matters on Roblox now (sourced)
- Roblox's Home recommendations (2026) weigh **long-term retention**: D1, D2–7 and D8–28 windows of playtime, play days, qualified sessions, co-play days and spend days, plus **play-through rate** and **first-play bounce rate**. Official guidance: *"If retention is low, focus first on making the core gameplay experience more fun, clear, and rewarding"*: a great first session, a satisfying core loop, reasons to come back. ([DevForum, Roblox Chief Growth Officer, 2026-08-06](https://devforum.roblox.com/t/boost-your-discovery-by-building-games-people-want-to-play/4779042); [RFY signals, 2026-06-15](https://devforum.roblox.com/t/recommended-for-you-algorithm-improvements-that-better-value-long-term-retention/4684575))
- Roblox's own core-loop page: minute-to-minute interaction → most repeated action → progression engine; without progression a game becomes "repetitive, boring, and shallow" ([docs](https://create.roblox.com/docs/production/game-design/core-loops)).
- Documented failures show the pattern: games that are "fun for a few minutes" but whose "main loop is very repetitive" with "no real reason to come back tomorrow" lose recommendation traffic ([Core Loop Failure Cases](Core-Loop-Failure-Cases.md)).

## The evaluation sheet (fill every field)
| # | Field | What a good answer looks like |
|---|---|---|
| 1 | **One-sentence premise** | "You \<verb\> \<object\> to \<goal\>, but \<tension\>." The verb and the tension are visible in the sentence. |
| 2 | **Main player action** | A concrete input: hold to cast and track a bar; place a tower; jump a gap. Not "explore" or "have fun". |
| 3 | **Immediate feedback** (≤ 0.1–0.3 s) | What the player sees and hears right after acting: number pop, sound, animation, camera. |
| 4 | **Reward** | What is gained, how big, how often, and how it is shown (travels to a counter, reveal). |
| 5 | **New possibility or decision** | What the reward *unlocks or changes*: a new area, tool, option, risk. If the answer is "a bigger number", flag it. |
| 6 | **Micro loop** (seconds) | Action → feedback → small gain. Name the skill/decision in it: timing, aim, route, risk, social, or none (automatic). |
| 7 | **Core loop** (minutes) | The repeated sequence, e.g. *collect → sell → upgrade → reach new zone*. What changes each cycle? |
| 8 | **Meta loop** (sessions/days) | Why return tomorrow: collection, mastery, status, social commitments, live events, building something persistent. |
| 9 | **First-session experience** | 0–10 s (what am I, where do I go), 10–30 s (first action), 30–90 s (first reward), 3–5 min (first upgrade that changes something visible), session end (next goal visible). |
| 10 | **Progression** | What grows (power, options, territory, cosmetics, knowledge) and the pacing metric (e.g. seconds-to-afford next upgrade, [LU-12](../07-Roblox-Studio-and-Luau/LU-12-Upgrade-Pricing.md)). |
| 11 | **Potential boredom points** | Where repetition stops changing: the same zone too long, an upgrade that changes only numbers, waiting with nothing to do, a solved strategy. |
| 12 | **Minimal prototype** | The smallest playable build that tests the core claim (usually 1 verb, 1 reward, 1 upgrade, 1 obstacle; graybox; no shop). |
| 13 | **Playtest plan** | Who (5+ fresh players from the target audience), what to watch (first action time, first confusion, quit moment), what to ask afterwards (would you play again tomorrow? why?). |
| 14 | **Success criteria** | Measurable: "7/10 testers perform the core action within 30 s without help"; "median prototype session ≥ 8 min"; "≥ 5/10 say they'd come back". |
| 15 | **Failure criteria** | What result would make you change or drop the concept: "median session < 3 min", "players stop after the first upgrade", "nobody can explain the goal". |

## Red flags (stop and fix before adding systems)
- Field 5 is "+X% more" for every reward → **number-only progression**. Add new options, places or rules.
- Field 6 has no skill or decision → the micro loop is automatic. Fine for idle or social games *only* if the meta or social layer carries the session.
- The first meaningful reward comes later than ~2 minutes, or needs reading.
- The concept needs 5+ systems to be fun ("unnecessary systems", AP-25). Documented case: a photography game where reviewers said to *cut the fluff and focus on the core* ([FC-GD-03](../15-Anti-Patterns-and-Failure-Cases/Failures-Documented/FC-GD-03-Photography-Game-Feature-Sprawl.md)).
- Retention depends on content you cannot produce fast enough (documented case: a solo dev's car combat game, [FC-GD-02](../15-Anti-Patterns-and-Failure-Cases/Failures-Documented/FC-GD-02-Battle-Cars-Repetitive-Loop.md)).

## Evidence quality for each field
Mark every answer as **[OBS]** observed in a playtest or recording, **[DEV]** stated by the developer or official docs, **[INF]** inferred, or **[HYP]** a hypothesis to test. A concept sheet full of [HYP] is normal; a *case study* full of [INF] must say so.

## Using it with data (Roblox Experiments)
Roblox's Experiments feature lets you A/B test loop variables. The official 2026 summary reports that about 1 in 4 of 1,000+ experiments produced a statistically significant playtime lift (average ~5%). Examples from creators: a difficulty "sweet spot" (+50% payer conversion, +10% session time), a free end-of-level reward (+12.5% playtime, +5.3% D1), and a level-based progression replacing a plain shop (+10% D1) ([DevForum, 2026-03-31](https://devforum.roblox.com/t/running-successful-experiments-insights-from-top-creators/4549276)). Use the framework to choose *what* to test; use experiments to decide.

## Worked examples
- Concept sheets: [Core Loop Library](Core-Loop-Library.md) (three loops for one theme, evaluated).
- Real games through the same lens: [Game Case Studies](../20-Game-Case-Studies/Case-Study-Index.md).
- Mechanics with their design conditions: [Game Mechanics Library](../04-Game-Mechanics/Mechanics-Index.md).
