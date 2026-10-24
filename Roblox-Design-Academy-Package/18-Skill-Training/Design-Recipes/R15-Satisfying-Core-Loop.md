---
title: "R15 — Designing a satisfying core loop"
tags: [recipe, core-loop]
note_type: "recipe"
---

# R15 — Designing a satisfying core loop

## 1. Goal
A loop that is clear in 60 s, satisfying every cycle and deep enough to return to.

## 2. When to use
Pre-production and whenever retention is weak.

## 3. Required inputs
Premise sentence; target audience (tourists/locals mix); session length goal.

## 4. Recommended structure
Three layers (Roblox) + five loop types (main, supporting, meta, social, monetization) + first-session timeline.

## 5. Step-by-step implementation
1. Write: "A game where you ___ to ___, while ___ (stakes)."
2. Define the verb; prototype it greybox until it is fun alone (no rewards).
3. Add feedback stack (R03/R11) and one progression engine.
4. Map every feature to a loop step; cut orphans.
5. Add one social interaction that changes outcomes.
6. Add solo fallback (bots) if multiplayer-dependent.
7. Instrument funnels; run 5 blind playtests of the first minute; iterate one variable at a time.

## 6. Animation guidance
Feedback per cycle ≤0.3 s for frequent actions; bigger celebration per milestone.

## 7. Sound guidance
Cycle-completion sound distinct from per-action sound.

## 8. Mobile considerations
Cycle must be playable with touch only.

## 9. Performance considerations
Loop must hold 60 FPS on the baseline device at max players.

## 10. Common mistakes
Adding systems instead of depth (CS-17); teaching shop before verb (CS-16); progression with no visible change (V12).

## 11. QA checklist
Use CL-04 and CL-06.

## 12. References & confidence
[Core Loop Framework](../../03-Core-Gameplay-Loops/Core-Loop-Framework.md) · [Core Loop Principles](../../17-Design-Principles/Core-Loop-Principles.md) · [CL 04 Core Loop Review](../../23-Quality-Checklists/CL-04-Core-Loop-Review.md)

**Confidence:** Medium (synthesis).
