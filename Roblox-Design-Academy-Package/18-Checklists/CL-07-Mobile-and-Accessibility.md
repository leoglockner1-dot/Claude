---
title: "CL-07 — Mobile & Accessibility"
tags: [checklist, mobile, accessibility]
note_type: "checklist"
---

# CL-07 — Mobile & Accessibility

Mark each item ✅ verified (write how), ❌ failed (write what), ⬜ not checked. **Never tick an item you did not check.** Distinguish verified results from assumptions in the report.

- [ ] Designed and tested at phone size first
- [ ] Touch targets ≥44×44 pt equivalent (external standard)
- [ ] Primary actions in thumb zone; nothing under the thumbstick
- [ ] CoreUISafeInsets for interactive UI
- [ ] PreferredTextSize Largest: no clipping; body text not TextScaled
- [ ] PreferredTransparency 0: backgrounds opaque
- [ ] ReducedMotion honoured
- [ ] Colour non-reliance verified in greyscale
- [ ] Sound non-reliance verified muted
- [ ] Contrast of body text ≈4.5:1 or better (external standard)
- [ ] Real low-end device tested (FPS/memory noted)
- [ ] Console: D-pad reachability, TV-safe area, chat window disabled

## Based on
[Mobile Controller and Accessibility](../01-UI-UX/Mobile-Controller-and-Accessibility.md) · [Accessibility Settings](../11-Roblox-Technical-Reference/Accessibility-Settings.md)
