---
title: "Accessibility Settings to Support"
tags: [technical, accessibility]
note_type: "technical-reference"
---

# Accessibility Settings to Support

> **Verified** against the Roblox Creator Docs (GitHub mirror commit 4e795e6 and create.roblox.com, accessed 2026-10-24). Re-check yearly. Items marked *(recommendation)* are design advice, not engine facts.

[accessibility guidelines](https://create.roblox.com/docs/production/publishing/accessibility)
- `GuiService.PreferredTransparency` (1 default → 0 opaque): multiply backgrounds' transparency.
- `GuiService.PreferredTextSize` (Medium/Large/Larger/Largest): **`TextScaled` text ignores it**; `UITextSizeConstraint` caps it; `AutomaticSize` grows to fit; `TextWrapped` wraps.
- `GuiService.ReducedMotionEnabled`: remove/reduce motion tweens (snap or fade).
- Colour non-reliance (>5 % colour blindness), sound non-reliance, separate volume controls, sufficient text size and contrast.
- External defaults (labelled): Apple HIG contrast ≥4.5:1 for text ≤17 pt; hit regions ≥44×44 pt.
