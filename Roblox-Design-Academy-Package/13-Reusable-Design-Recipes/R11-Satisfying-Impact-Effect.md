---
title: "R11 — Satisfying impact effect"
tags: [recipe, game-feel, vfx]
note_type: "recipe"
---

# R11 — Satisfying impact effect

## 1. Goal
Make hits feel weighty and readable without visual noise.

## 2. When to use
Melee/ranged combat, mining, breaking objects.

## 3. Required inputs
Hit event data (target, strength), tier table.

## 4. Recommended structure
Anticipation (wind-up) → hit frame: target flash + particles (semantic) + sound + (heavy only) hit-stop and small camera kick → numbers → follow-through.

## 5. Step-by-step implementation
1. Classify hit strength into tiers S/M/L.
2. Target `Highlight` fill 0→0.6→0 over 0.1 s.
3. `Emit()` 5–20 particles by tier along hit normal.
4. Heavy: pause attacker/target `AnimationTrack:AdjustSpeed(0)` for 0.05 s locally, then resume.
5. Camera kick: offset 0.1–0.2 studs decaying over 0.15 s (heavy only, ReducedMotion → off).
6. Damage number pooled BillboardGui.

## 6. Animation guidance
Hit-stop 0.03–0.08 s; shake ≤0.3 s decaying.

## 7. Sound guidance
Transient + material texture; heavier = lower + longer tail; rotate 3–4 samples.

## 8. Mobile considerations
Effects scaled for small screens; don't cover the reticle.

## 9. Performance considerations
Particle caps (100/s mobile per emitter); Highlight limit 255.

## 10. Common mistakes
Shake on every hit; full-screen flashes for light hits; same sample each hit.

## 11. QA checklist
- [ ] Each tier distinguishable blind (audio only) and muted (visual only)
- [ ] ReducedMotion respected
- [ ] 10 hits/s keeps 60 FPS on baseline

## 12. References & confidence
[Feedback Arc and Impact](../05-Animation-and-Game-Feel/Feedback-Arc-and-Impact.md) · [V10 V11 Blaster Cooldown vs Spam](../16-Video-Analyses/V10-V11-Blaster-Cooldown-vs-Spam.md) · [VFX Principles and Performance](../05-Animation-and-Game-Feel/VFX-Principles-and-Performance.md)

**Confidence:** Medium (values are hypotheses).
