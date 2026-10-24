---
title: "R04 — Upgrade purchase interaction"
tags: [recipe, progression, ui]
note_type: "recipe"
---

# R04 — Upgrade purchase interaction

## 1. Goal
Make buying an upgrade clear before, satisfying during and visible after.

## 2. When to use
Stat/ability/tool upgrades bought with soft currency.

## 3. Required inputs
Current and next values, cost, visual hook of the upgrade.

## 4. Recommended structure
Card: icon + name → "current → next" (delta highlighted) → cost on the button (red if unaffordable, with "get more" path) → after purchase: button pop, cost flies out of the counter, stat label "+N", and an immediate in-world demonstration.

## 5. Step-by-step implementation
1. Server-side upgrade definitions (cost, value, visual hook).
2. Card shows `current → next` and delta in accent colour.
3. Press: 0.06 s down state; client sets pending state; RemoteFunction to server.
4. Server validates currency, applies, returns new state.
5. Client: currency counter count-down, card pop, "+30 Jump" floater near the button, sound; demonstrate (e.g., auto-jump once) or highlight the changed object.
6. Update next tier preview immediately.

## 6. Animation guidance
Press 0.06 s; pop 0.15 s Back Out; floater 0.6 s.

## 7. Sound guidance
Purchase: rising two-note + coin shimmer; denied: soft low thud + shake 4 px (0.15 s).

## 8. Mobile considerations
Cards ≥44 pt buttons; don't put buy buttons where a scroll gesture starts.

## 9. Performance considerations
Avoid re-building the whole list on each purchase; update one card.

## 10. Common mistakes
Silent number change elsewhere (V12); no next preview; identical look for affordable/unaffordable.

## 11. QA checklist
- [ ] Before: current→next visible
- [ ] During: pending state prevents double-buy
- [ ] After: effect visible within 1 s
- [ ] Unaffordable state readable without colour

## 12. References & confidence
[V12 Upgrade Button Baseline](../16-Video-Analyses/V12-Upgrade-Button-Baseline.md) · [Progression and Economy Principles](../14-Design-Principles/Progression-and-Economy-Principles.md) · [Client Server and Purchases](../11-Roblox-Technical-Reference/Client-Server-and-Purchases.md)

**Confidence:** High (structure), Medium (timings).
