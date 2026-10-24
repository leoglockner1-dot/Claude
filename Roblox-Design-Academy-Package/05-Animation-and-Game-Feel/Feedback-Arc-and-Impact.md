---
title: "Feedback Arc and Impact"
tags: [game-feel, animation]
note_type: "topic"
---

# Feedback Arc and Impact

## The arc
**Anticipation → Action → Impact → Follow-through/Recovery → Reward/Settle.** Classic animation principles (Thomas & Johnston, *The Illusion of Life*) applied to interaction; Roblox docs examples show each stage:
| Stage | Observed example | Measured |
|---|---|---|
| Anticipation | Idle sparks on a trap tile ([V20](../16-Video-Analyses/V20-Burst-Particle-Trap.md)) | continuous before contact |
| Action/Impact | Burst lightning | ≈0.4 s full-frame peak |
| Follow-through | Debris settles, sparks resume | ≈0.35 s |
| Reward | Coins fly to counter (GF-01) | — |

## Impact toolkit (use the smallest that works)
1. **Flash** on the hit target (`Highlight` fill tween 0.05–0.1 s).
2. **Numbers** (pooled `BillboardGui`).
3. **Screen tint** for damage to the player — measured docs flash: one-frame attack, decays to ~15 % by ≈200 ms ([V06](../16-Video-Analyses/V06-V07-HUD-Meter-Tween-and-Damage-Flash.md)).
4. **Particles** shaped by meaning (FEEL-005).
5. **Camera** — small, decaying shake/FOV kick only for heavy events; scale to zero with `ReducedMotionEnabled` (hypothesis values in [Timing reference](Timing-Reference.md)).
6. **Sound** on the same frame (AUDIO-001).

## Readability under intensity
Space repeated events (FEEL-004, blaster cadence ≈0.6 s), keep the centre readable, and reserve full-screen effects for rare events (FEEL-006).

## Recipes
[R11 Satisfying Impact Effect](../13-Reusable-Design-Recipes/R11-Satisfying-Impact-Effect.md) · [R12 Reusable Button Animation System](../13-Reusable-Design-Recipes/R12-Reusable-Button-Animation-System.md)
