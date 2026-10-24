---
title: "R06 — Progression or milestone celebration"
tags: [recipe, rewards]
note_type: "recipe"
---

# R06 — Progression or milestone celebration

## 1. Goal
Mark level-ups and milestones as moments of joy, then point to the next goal.

## 2. When to use
Level-ups, onboarding completion, first rare item, season tier.

## 3. Required inputs
What unlocked, next goal.

## 4. Recommended structure
Brief title pop ("LEVEL 5!") → unlocked items shown as icons → "Next: …" with progress bar → auto-dismiss (or tap) within ~2 s.

## 5. Step-by-step implementation
1. Queue celebrations (never stack modals).
2. Title scale 0.8→1.0 Back Out 0.25 s; particles from title edges.
3. Unlock icons slide in 0.1 s apart.
4. Show next goal bar.
5. Return control quickly; keep a small toast if the player is in combat.

## 6. Animation guidance
Total ≤2 s; respect ReducedMotion (fade only).

## 7. Sound guidance
Ascending arpeggio + soft whoosh; distinct from purchase sound.

## 8. Mobile considerations
Center modal acceptable briefly; never during an active hazard — fall back to a toast.

## 9. Performance considerations
One-shot particles only.

## 10. Common mistakes
Silent level-ups; long modals mid-combat; no next goal.

## 11. QA checklist
- [ ] Next goal shown
- [ ] Doesn't interrupt danger
- [ ] Queue works with simultaneous events

## 12. References & confidence
[V08 V09 Victory and Defeat Screens](../16-Video-Analyses/V08-V09-Victory-and-Defeat-Screens.md) · [Onboarding Principles](../14-Design-Principles/Onboarding-Principles.md)

**Confidence:** Medium.
