---
title: "R10 — Short onboarding sequence"
tags: [recipe, onboarding]
note_type: "recipe"
---

# R10 — Short onboarding sequence

## 1. Goal
Get new players to the core verb within ~60 s and keep them through the first reward.

## 2. When to use
Every new game.

## 3. Required inputs
Core verb; first reward; first upgrade; secondary systems list.

## 4. Recommended structure
Spawn → picture sign/arrow → core verb → reward flies to counter → first upgrade → social moment → celebration + goals. Secondary systems via contextual tutorials; timed hints for stuck players.

## 5. Step-by-step implementation
1. Map the first minute with the timeline template.
2. Implement each step as a funnel step (`LogOnboardingFunnelStepEvent`).
3. Visual guidance only (sign/arrow/trail); no blur, no paragraph popups.
4. Timed hints at ~typical completion time +1 s, once.
5. Trigger table for secondary systems.
6. Run Experiments on the weakest step.

## 6. Animation guidance
Arrow bob 0.6 s loop; outline pulse; trail fade after completion.

## 7. Sound guidance
Positive chime per completed step; no narration required.

## 8. Mobile considerations
Arrows large; targets in thumb reach; text ≥ readable minimum.

## 9. Performance considerations
Trails as Beams; remove guidance objects after completion.

## 10. Common mistakes
Forced shop tutorial (ONB-06); tiny step chips (UI-25); teaching everything upfront.

## 11. QA checklist
Use CL-06.

## 12. References & confidence
[First Minute Timeline](../../03-Core-Gameplay-Loops/First-Minute-Timeline.md) · [First Session Design](../../13-Onboarding-and-Multiplayer/Onboarding/First-Session-Design.md) · [CL 06 First Session Onboarding](../../23-Quality-Checklists/CL-06-First-Session-Onboarding.md)

**Confidence:** High.
