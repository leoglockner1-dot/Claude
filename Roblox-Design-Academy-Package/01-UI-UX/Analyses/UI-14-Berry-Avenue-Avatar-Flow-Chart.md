---
title: "Berry Avenue: Low-Friction Avatar Flow (Process Reference)"
tags: [reference, ui]
reference_type: "image-analysis"
source_ref: "IMP-14 (earlier import package)"
date_accessed: "2026-10-24"
---

# Berry Avenue: Low-Friction Avatar Flow (Process Reference)

## Metadata
- Category: UX / Flows
- Source: Roblox Creator Docs, "UI and UX design" > Design flows. Game: https://www.roblox.com/games/8481844229/
- Asset: see images below

![IMP-14_berry-avenue-avatar-flow](../../Assets/UI/docs/IMP-14_berry-avenue-avatar-flow.jpg)
![IMP-14_berry-avenue-avatar-flow](../../Assets/UI/docs/IMP-14_berry-avenue-avatar-flow.jpg)

- Date added: 2026-10-24
- Rating: 4/5 as a method
- Confidence: High for the method, none for the visuals (video not watched)
- Reference type: Positive (process)

## Context
The flow is: Tap Avatar → (Body-part tab **or** Search) → Select item ⇄ Remove item → Done. Roblox presents it as a low-friction flow, derived from player goals: modify quickly, find items easily, preview instantly, remove easily.

## Reusable Design Rules
1. Write the **player goals** for a feature first, then design the flow, then the screens.
2. **Draw the flow chart and count the taps** to the core goal. Every extra step is friction.
3. Give two ways in (browse by category **and** search) for any collection over about 30 items.
4. **Preview instantly on the avatar or object**, without a confirm step.
5. Make "undo" equal to "tap again".

## Roblox implementation
Before building any menu in Studio, add a Mermaid flow chart to the project note in Obsidian. Use it as an acceptance criterion: "equip in ≤ 4 taps".

## Original application
Before building a pet shop, write the goals (browse fast, preview pet, compare, buy) and count taps (≤3 to buy).

## Limitations
The video still needs to be watched to judge animation and feedback. Add a sequence analysis later.

## Related
[Menus and Navigation](../Menus-and-Navigation.md) · [Shops and Inventory](../Shops-and-Monetization-UI.md) · [UI Review](../../18-Checklists/CL-01-UI-Review.md)
