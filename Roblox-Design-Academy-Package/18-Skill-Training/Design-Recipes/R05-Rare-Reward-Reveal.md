---
title: "R05 — Rare reward reveal"
tags: [recipe, rewards, vfx]
note_type: "recipe"
---

# R05 — Rare reward reveal

## 1. Goal
Make rare outcomes feel rare and exciting, honestly.

## 2. When to use
Eggs, crates, chests, rare drops.

## 3. Required inputs
Rarity ladder (colours, sounds), item 3D model, odds table if paid.

## 4. Recommended structure
Anticipation (object wobbles, glow builds in rarity colour, rising riser) → burst → item reveal in `ViewportFrame` with name + rarity tag → collect/equip/continue buttons. Multi-open → summary grid.

## 5. Step-by-step implementation
1. Server rolls outcome (never client).
2. Client receives result, chooses anticipation length by rarity tier.
3. Dim background (`ColorCorrection` brightness down or a dark frame 0.6 alpha).
4. Wobble the object 2–3 times (rotation tween, accelerating); glow `PointLight` brightness up in rarity colour.
5. Burst: `Emit()` rarity-coloured particles + flash 0.1 s.
6. Reveal model spinning slowly; name pops after 0.2 s.
7. Offer Skip after first view; remember preference.

## 6. Animation guidance
Common ≤0.6 s total; rare 1.5–2.5 s; legendary ≤4 s; all skippable after the first time.

## 7. Sound guidance
Riser during anticipation; burst sparkle at reveal; unique motif per top tier; duck music briefly.

## 8. Mobile considerations
Text sizes large; reveal fits portrait and landscape; buttons in thumb reach.

## 9. Performance considerations
Few, large particles; dispose ViewportFrame models after.

## 10. Common mistakes
Same animation for all rarities; unskippable long reveals; marketing odds ≠ real odds (TI-15); hidden odds.

## 11. QA checklist
- [ ] Odds visible pre-purchase with labelled button (if paid)
- [ ] Rarity readable without colour
- [ ] Skip works
- [ ] Server-authoritative roll

## 12. References & confidence
[Reward Reveals and Celebrations](../../08-Animation-and-Game-Feel/Reward-Reveals-and-Celebrations.md) · [Random Rewards and Fairness](../../05-Progression-and-Economy/Random-Rewards-and-Fairness.md) · [V20 Burst Particle Trap](../../21-Video-Analyses/V20-Burst-Particle-Trap.md)

**Confidence:** Medium (durations are hypotheses; policy facts High).
