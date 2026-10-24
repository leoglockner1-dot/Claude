---
title: "CL-01 — UI Review"
tags: [checklist, ui]
note_type: "checklist"
---

# CL-01 — UI Review

Mark each item ✅ verified (write how), ❌ failed (write what), ⬜ not checked. **Never tick an item you did not check.** Distinguish verified results from assumptions in the report.

- [ ] Screenshot taken on a phone (or phone emulator at smallest supported size); all text readable without zoom
- [ ] Squint/blur test: the primary action is the most visible element (UI-001)
- [ ] Exactly one accent-coloured element per screen
- [ ] ≤2 font families, ≤5 type sizes; no sentences in all caps (UI-002)
- [ ] Padding/gaps use only the spacing scale (check 3 random gaps) (UI-004)
- [ ] All states exist: normal, hover, pressed, selected (gamepad), disabled, pending (FEEL-007)
- [ ] Selected tab is more prominent than unselected
- [ ] Strokes/glows/gradients each have a stated job (UI-007)
- [ ] Decoration lighter than content (UI-008)
- [ ] No overlap with Roblox top bar/chat/leaderboard; `ScreenInsets` checked (TECH-001)
- [ ] Greyscale screenshot still communicates states (UI-012)
- [ ] Works with PreferredTextSize = Largest, PreferredTransparency = 0, ReducedMotion = on (TECH-003)
- [ ] Gamepad: all controls reachable; key actions ≤3 moves
- [ ] Input hints match device (no keyboard letters on touch)
- [ ] Longest localized string fits
- [ ] Destructive actions distinct + confirmed (UI-011)
- [ ] Modals never stack (open two triggers at once)
- [ ] Same panel/button components as other screens (UI-005)
- [ ] Flow chart exists; tap count recorded (UI-009)

## Based on
[UI Principles](../17-Design-Principles/UI-Principles.md) · [UI UX Overview](../01-UI-UX/UI-UX-Overview.md)
