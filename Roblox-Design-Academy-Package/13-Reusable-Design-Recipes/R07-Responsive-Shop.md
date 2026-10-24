---
title: "R07 — Responsive, honest shop"
tags: [recipe, ui, shop]
note_type: "recipe"
---

# R07 — Responsive, honest shop

## 1. Goal
A shop that is fast to scan, clear about value and currencies, and fair.

## 2. When to use
Any soft- or premium-currency shop.

## 3. Required inputs
Offer list with prices and categories; currency icons; odds tables for random items.

## 4. Recommended structure
Header (title, balance, close) → category tabs (selected = most prominent) → grid with value ladder (one hero offer isolated) → detail/preview on select → buy button with currency icon; Robux buttons visually distinct.

## 5. Step-by-step implementation
1. Group product types into containers (UI-06).
2. Art scales with quantity (UI-05).
3. Balance visible in header with "+" shortcut.
4. Unaffordable: price red + "need N more" + lock icon.
5. Pending state on `PromptProductPurchase`; grant via ProcessReceipt.
6. Paid random items: "Odds" labelled button on the card.
7. Gamepad: grid navigation, B closes.

## 6. Animation guidance
Tab switch: content cross-fade 0.15 s; card hover 1.03 scale; purchase success pop.

## 7. Sound guidance
Press click; success chime; avoid sounds on hover for grids.

## 8. Mobile considerations
2-column grid on Small screens; tabs scrollable; buy buttons ≥44 pt.

## 9. Performance considerations
Lazy-load thumbnails; reuse cards.

## 10. Common mistakes
Harsh four-hue palettes (UI-15); look-alike currency icons (UI-17); badges everywhere; selected tab darker than others (UI-05).

## 11. QA checklist
- [ ] Value order obvious in 2 s
- [ ] Robux vs soft currency distinguishable without colour
- [ ] Odds disclosure compliant
- [ ] No stacked offer modals
- [ ] Ethics checklist CL-08 passed

## 12. References & confidence
[Shops and Monetization UI](../01-UI-UX/Shops-and-Monetization-UI.md) · [CL 08 Shop and Monetization Ethics](../18-Checklists/CL-08-Shop-and-Monetization-Ethics.md) · [UI 05 Dragon Adventures Premium Shop](../01-UI-UX/Analyses/UI-05-Dragon-Adventures-Premium-Shop.md)

**Confidence:** High.
