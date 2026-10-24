---
title: "R13 — Readable mobile interface"
tags: [recipe, ui, mobile]
note_type: "recipe"
---

# R13 — Readable mobile interface

## 1. Goal
UI that works at phone size first and scales up.

## 2. When to use
All games (most Roblox users are on mobile).

## 3. Required inputs
Device list (baseline phone), safe-area settings, text-size tokens.

## 4. Recommended structure
Thumb zones, CoreUISafeInsets, Small/Medium/Large viewport style queries, ≥44 pt targets, ≤5 HUD buttons visible, progressive disclosure.

## 5. Step-by-step implementation
1. Design at 844×390 (example phone landscape) first.
2. Style queries for `@ViewportDisplaySizeSmall` with larger relative text and fewer columns.
3. `UITextSizeConstraint` minimums; avoid `TextScaled` for body text.
4. Test PreferredTextSize Largest and PreferredTransparency 0.
5. Real-device test (emulator not accurate for memory).

## 6. Animation guidance
Same as desktop but no hover; bigger press feedback.

## 7. Sound guidance
Many players mute — visual twins required.

## 8. Mobile considerations
This is the mobile recipe.

## 9. Performance considerations
Fewer transparent layers; low particle rates.

## 10. Common mistakes
Half-screen panels with tiny tiles (V01); tiny chips (UI-25); keyboard hints on touch.

## 11. QA checklist
Use CL-07.

## 12. References & confidence
[Mobile Controller and Accessibility](../../01-UI-UX/Mobile-Controller-and-Accessibility.md) · [UI Layout and Scaling](../../14-Technical-Reference/UI-Layout-and-Scaling.md) · [CL 07 Mobile and Accessibility](../../23-Quality-Checklists/CL-07-Mobile-and-Accessibility.md)

**Confidence:** High.
