---
title: "Mobile, Controller and Accessibility"
tags: [ui, mobile, accessibility]
note_type: "topic"
---

# Mobile, Controller and Accessibility

## Verified facts (Roblox docs)
- Most users play on mobile; design UI mobile-first (design-for-roblox).
- `ScreenInsets`: CoreUISafeInsets (interactive), DeviceSafeInsets, TopbarSafeInsets, None.
- `ViewportDisplaySize` Small/Medium/Large; `PreferredInput`; `InputActionLabel` for device-correct glyphs.
- Player settings to respect: `PreferredTransparency`, `PreferredTextSize` (**TextScaled ignores it**), `ReducedMotionEnabled`.
- Console: 10-ft UI, TV-safe area, D-pad reachability, disable chat window.
→ details: [UI Layout and Scaling](../14-Technical-Reference/UI-Layout-and-Scaling.md), [Accessibility Settings](../14-Technical-Reference/Accessibility-Settings.md)

## External standards (labelled)
- Apple HIG: hit region at least **44×44 pt**; accessibility table lists 44×44 pt default and 28×28 pt minimum on iOS.
- Apple HIG contrast table: **4.5:1** minimum for text up to 17 pt.
These are not Roblox rules; use them as defensible defaults.

## Mobile checklist
[CL 07 Mobile and Accessibility](../23-Quality-Checklists/CL-07-Mobile-and-Accessibility.md) · recipe [R13 Readable Mobile Interface](../18-Skill-Training/Design-Recipes/R13-Readable-Mobile-Interface.md)

## Evidence of failure
Tiny chips and text (UI-25, UI-13), keyboard hints on touch (UI-03), translucent buttons on bright scenes (UI-02), low-graphics world appearance ignored (CS-15).
