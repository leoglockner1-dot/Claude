---
title: "Technical Principles (TECH-001 – TECH-006)"
tags: [principles, technical]
note_type: "principles"
---

# Technical Principles (TECH-001 – TECH-006)

Roblox-specific implementation principles (all verified against Creator Docs, 2026-10-24).

| ID | Principle | Confidence |
|---|---|---|
| TECH-001 | Interactive UI inside CoreUISafeInsets | High |
| TECH-002 | Scale + constraints, not raw pixels or raw scale | High |
| TECH-003 | Respect player accessibility settings | High |
| TECH-004 | Tokens via the Style Editor | High |
| TECH-005 | Server-authoritative purchases, client-side feedback | High |
| TECH-006 | Budget effects for mobile | High |

## TECH-001 — Interactive UI inside CoreUISafeInsets
**Rule:** Use `ScreenInsets = CoreUISafeInsets` for interactive ScreenGuis.

- **Reasoning:** Avoids top-bar and notch occlusion (docs).
- **Evidence:** [UI Layout and Scaling](../11-Roblox-Technical-Reference/UI-Layout-and-Scaling.md)
- **Good application:** —
- **Failure mode:** Buttons under the notch.
- **Conditions & exceptions:** Backgrounds may use `None`.
- **Roblox implementation:** Property on each ScreenGui.
- **Confidence:** High
- **Tags:** #technical #ui

## TECH-002 — Scale + constraints, not raw pixels or raw scale
**Rule:** Combine Scale sizing with `UISizeConstraint`/`UIAspectRatioConstraint` and `ViewportDisplaySize` adaptation.

- **Reasoning:** Pure scale balloons on TVs; pixels break on phones (docs).
- **Evidence:** [UI Layout and Scaling](../11-Roblox-Technical-Reference/UI-Layout-and-Scaling.md)
- **Good application:** —
- **Failure mode:** 75 % width panel on a 4K TV.
- **Conditions & exceptions:** —
- **Roblox implementation:** Style queries `@ViewportDisplaySizeSmall/Large`.
- **Confidence:** High
- **Tags:** #technical #ui

## TECH-003 — Respect player accessibility settings
**Rule:** Support `PreferredTextSize` (avoid relying on `TextScaled`), `PreferredTransparency`, `ReducedMotionEnabled`.

- **Reasoning:** Docs: TextScaled ignores PreferredTextSize.
- **Evidence:** [Accessibility Settings](../11-Roblox-Technical-Reference/Accessibility-Settings.md)
- **Good application:** —
- **Failure mode:** TextScaled everywhere.
- **Conditions & exceptions:** —
- **Roblox implementation:** AutomaticSize + TextWrapped containers.
- **Confidence:** High
- **Tags:** #technical #accessibility

## TECH-004 — Tokens via the Style Editor
**Rule:** Centralise colours, fonts and sizes as Style Editor tokens and rules.

- **Reasoning:** Consistency and themeability (DevForum example).
- **Evidence:** [UI 23 DevForum Themeable Avatar Editor](../01-UI-UX/Analyses/UI-23-DevForum-Themeable-Avatar-Editor.md), [UI Layout and Scaling](../11-Roblox-Technical-Reference/UI-Layout-and-Scaling.md)
- **Good application:** Player-selectable themes.
- **Failure mode:** Hard-coded colours in 200 objects.
- **Conditions & exceptions:** —
- **Roblox implementation:** StyleSheet + StyleRules + tokens.
- **Confidence:** High
- **Tags:** #technical

## TECH-005 — Server-authoritative purchases, client-side feedback
**Rule:** Grant purchases in `ProcessReceipt`/server; show feedback immediately on the client.

- **Reasoning:** Docs: use ProcessReceipt, not PromptProductPurchaseFinished.
- **Evidence:** [Client Server and Purchases](../11-Roblox-Technical-Reference/Client-Server-and-Purchases.md)
- **Good application:** —
- **Failure mode:** Granting items from a LocalScript.
- **Conditions & exceptions:** —
- **Roblox implementation:** `MarketplaceService.ProcessReceipt` returning `Enum.ProductPurchaseDecision`.
- **Confidence:** High
- **Tags:** #technical #economy

## TECH-006 — Budget effects for mobile
**Rule:** Particles ≤100/s per emitter on mobile, few overlapping transparent layers, ≤255 Highlights, test on a baseline phone.

- **Reasoning:** Docs limits; fill-rate and overdraw cost.
- **Evidence:** [Particles Lighting and Effects](../11-Roblox-Technical-Reference/Particles-Lighting-and-Effects.md), [Performance and Mobile](../11-Roblox-Technical-Reference/Performance-and-Mobile.md)
- **Good application:** Short `Emit()` bursts.
- **Failure mode:** Continuous 400/s emitters on mobile.
- **Conditions & exceptions:** —
- **Roblox implementation:** Device-tier settings; MicroProfiler.
- **Confidence:** High
- **Tags:** #technical #performance
