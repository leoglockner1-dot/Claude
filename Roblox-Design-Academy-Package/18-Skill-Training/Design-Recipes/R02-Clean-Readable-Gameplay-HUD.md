---
title: "R02 — Clean, readable gameplay HUD"
tags: [recipe, ui, hud]
note_type: "recipe"
---

# R02 — Clean, readable gameplay HUD

## 1. Goal
A HUD that shows the minimum needed for decisions, never covers the action, and adapts to device.

## 2. When to use
Any real-time game.

## 3. Required inputs
List of player decisions and the info each needs; frequency of each action; semantic colour map.

## 4. Recommended structure
Zones: top-left (below Roblox top bar) objectives; top-centre timers/banners; top-right vitals & currency; centre empty; bottom-centre hotbar (≤5 early); bottom-right touch actions; bottom-left reserved for thumbstick on touch.

## 5. Step-by-step implementation
1. For each piece of info ask Roblox's prioritization questions (what is the player doing, what do they need now).
2. Assign zones; use `ScreenInsets = CoreUISafeInsets`.
3. Build meters as Frame + fill; tween with `TweenInfo.new(0.5, Exponential, Out)`; colour by fraction (V06).
4. Context-swap action buttons by state (UI-02) instead of adding buttons.
5. Show input hints via `InputActionLabel` per device.
6. Add a peripheral damage tint (ColorCorrection) for player damage.
7. Add a "hide HUD" toggle for creators.

## 6. Animation guidance
Meters ≈0.25 s visible change; damage flash attack 1 frame, decay ~0.3 s; banners slide in 0.2 s, stay 2–3 s.

## 7. Sound guidance
Low-health heartbeat loop only below ~25 % (with visual twin); avoid HUD sounds for frequent passive updates.

## 8. Mobile considerations
Thumb zone for primary actions; minimum 44 pt targets; no tiny keybind letters on touch; test with PreferredTextSize Largest.

## 9. Performance considerations
Update text only on change (events), not every frame; avoid many transparent stacked frames.

## 10. Common mistakes
Two button languages (UI-02); centre overlays during action (UI-24); translucent buttons over bright terrain; keyboard letters on touch (UI-03).

## 11. QA checklist
- [ ] Centre third empty
- [ ] Every element passes the "decision it supports" test
- [ ] Squint test: vitals readable
- [ ] Greyscale test passes
- [ ] Works on phone emulator + real phone

## 12. References & confidence
[HUD Layouts](../../01-UI-UX/HUD-Layouts.md) · [V06 V07 HUD Meter Tween and Damage Flash](../../21-Video-Analyses/V06-V07-HUD-Meter-Tween-and-Damage-Flash.md) · [UI 03 The Survival Game Minimal HUD](../../01-UI-UX/Analyses/UI-03-The-Survival-Game-Minimal-HUD.md)

**Confidence:** High.
