---
title: "R03 — Satisfying currency collection"
tags: [recipe, game-feel, economy]
note_type: "recipe"
---

# R03 — Satisfying currency collection

## 1. Goal
Make picking up currency feel rewarding without slowing the loop.

## 2. When to use
Coins, gems, resources collected many times per minute.

## 3. Required inputs
Currency icon, counter location, pickup frequency estimate.

## 4. Recommended structure
World pickup → instant local vanish + small burst → icon flies to the HUD counter → counter pops and counts up → optional "+N" floater.

## 5. Step-by-step implementation
1. Detect touch on client for feedback; send claim to server; server validates (distance, rate) and grants.
2. On local detect: hide pickup, `Emit(6–10)` sparkle in currency colour, play pickup sound (same frame).
3. Spawn a screen `ImageLabel` at `Camera:WorldToViewportPoint(pos)` and tween to the counter's `AbsolutePosition` (0.35–0.5 s, Quad In then pop).
4. On arrival: counter scale 1.15→1.0 (Back Out 0.15 s); number tween/count-up.
5. Batch: if many pickups within 0.2 s, merge into one flight with "+N".

## 6. Animation guidance
Flight 0.35–0.5 s; counter pop 0.15 s; floaters rise 0.6 s and fade.

## 7. Sound guidance
Bright short ding; pitch steps up for streaks within 1.5 s (reset after); cap concurrent plays to 3.

## 8. Mobile considerations
Counter must be visible (top-right); flight path must not cross primary buttons.

## 9. Performance considerations
Pool UI flyers and particles; never create per-coin `BillboardGui`s endlessly.

## 10. Common mistakes
Sound lagging the visual (V14 +120 ms); identical sample every time; counter far from where players look; server round-trip before any feedback.

## 11. QA checklist
- [ ] Feedback starts same frame
- [ ] Server validates
- [ ] Streak pitch resets
- [ ] 20 pickups/s doesn't drop FPS on baseline phone

## 12. References & confidence
[V14 V17 Pickup and UI Sounds](../../21-Video-Analyses/V14-V17-Pickup-and-UI-Sounds.md) · [GF 01 Winds of Fortune Combat Feedback](../../08-Animation-and-Game-Feel/Analyses/GF-01-Winds-of-Fortune-Combat-Feedback.md) · [Audio Principles](../../17-Design-Principles/Audio-Principles.md)

**Confidence:** Medium (timings are starting values).
