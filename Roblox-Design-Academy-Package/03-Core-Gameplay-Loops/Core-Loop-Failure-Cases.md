---
title: "Core Loop Failure Cases (documented) and their patterns"
tags: [core-loop, failure-case, retention, documented]
note_type: "index"
evidence: "developer self-reports on the Roblox DevForum + community diagnosis; Roblox official discovery posts"
---

# Core Loop Failure Cases

Real games whose developers reported weak retention or reception, with the diagnosis people offered. **The corrections were not tested by us.** Treat each diagnosis as a hypothesis with community support.

| Case | Reported symptom | Diagnosed cause (pattern) | Framework field that would have caught it |
|---|---|---|---|
| [FC-GD-01 TROLL Outfit Tower](../15-Anti-Patterns-and-Failure-Cases/Failures-Documented/FC-GD-01-Troll-Outfit-Tower-Retention-Collapse.md) | Spike to 230 CCU, then collapse; 1.7k R$ lifetime | No reason to return; free fun exhausted in minutes; features cut at launch | 8 Meta loop, 15 Failure criteria |
| [FC-GD-02 Battle Cars](../15-Anti-Patterns-and-Failure-Cases/Failures-Documented/FC-GD-02-Battle-Cars-Repetitive-Loop.md) | High dislikes; no organic traffic | Loop "seen it all after 5 minutes"; bugs; mixed art/UI styles; content production too slow | 5 New possibility, 11 Boredom points |
| [FC-GD-03 Be A Photographer](../15-Anti-Patterns-and-Failure-Cases/Failures-Documented/FC-GD-03-Photography-Game-Feature-Sprawl.md) | Players join and leave | Core activity hollowed out; UI clutter; economy exploits; too many systems | 2 Main action, 6 Micro loop, red flag "5+ systems" |
| [FC-GD-04 Rising Empires](../15-Anti-Patterns-and-Failure-Cases/Failures-Documented/FC-GD-04-Rising-Empires-Generic-First-Impression.md) | New players leave almost immediately | Looks like "just another TD"; slow to the main action | 1 Premise (no visible twist), 9 First session |
| [FC-GD-05 Dig to 999M](../15-Anti-Patterns-and-Failure-Cases/Failures-Documented/FC-GD-05-Dig-To-999M-Tutorial-Money-Gap.md) | Low D1 | Tutorial asks for an unaffordable purchase; content ends in ~1 hour | 9 First session, 10 Progression pacing |
| [FC-GD-06 No One Leaves the Woods](../15-Anti-Patterns-and-Failure-Cases/Failures-Documented/FC-GD-06-Asymmetric-Survival-Engaged-Core-Low-D1.md) | Engaged core, 3–4% D1 | New players don't reach the fun; averages hide distributions; ad traffic differs | 9 First session, 13 Playtest plan (fresh players) |
| [CS-17 Outbreak Mayhem](../20-Game-Case-Studies/CS-17-Outbreak-Mayhem.md) (v1) | Feature-rich but unclear | Unclear objectives | 1 Premise |
| [CS-15 TURBOSTORM](../20-Game-Case-Studies/CS-15-TURBOSTORM-Racing.md) (v1) | Good sessions, no organic traffic | Onboarding friction (thread details in the note) | 9 First session |
| [ONB-06 Forced blur tutorial](../13-Onboarding-and-Multiplayer/Onboarding/Analyses/ONB-06-DevForum-Forced-Blur-Tutorial-Funnel.md) (v1) | ~30% onboarding rate | Forced, blocking tutorial | 9 First session |

## Patterns across cases
1. **"Fun for 5 minutes" is the most common verdict.** The micro loop works; the core loop doesn't change and the meta loop is missing (FC-GD-01, 02, 05).
2. **First-minute failures look like retention failures.** If new players never reach the fun, the average numbers fall even when veterans love the game (FC-GD-04, 06, ONB-06).
3. **Feature count is not depth.** Systems that don't feed the core verb add clutter (FC-GD-03, CS-17).
4. **Visible quality issues hit the like ratio and play-through rate first.** Bugs, mismatched UI and AI-looking UI were named in FC-GD-02 and FC-GD-03.
5. **The platform measures retention windows.** Since June 2026, Home recommendations use D1, D2–7 and D8–28 signals plus play-through and first-play bounce rates (official). A weak D1 is no longer hidden by a good launch week.

## Use
Before launch, run every concept through fields 8, 9, 11 and 15 of the [framework](Core-Loop-Evaluation-Framework.md), and playtest with *fresh* players, not friends who already know the game.
