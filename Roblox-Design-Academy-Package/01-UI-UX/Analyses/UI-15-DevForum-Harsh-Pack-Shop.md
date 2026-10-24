---
title: "UI-15 — 'Packs' shop with clashing colours (Dodge The Bullets, DevForum)"
tags: [reference, ui, shop, anti-pattern]
reference_type: "DevForum UI screenshot + critique (Negative)"
date_accessed: "2026-10-24"
---

# UI-15 — "Packs" shop with clashing colours (Dodge The Bullets, DevForum)

## Identity
- **Name:** UI-15 — "Packs" shop with clashing colours (Dodge The Bullets, DevForum)
- **Reference type:** DevForum UI screenshot + critique (Negative)
- **Source URL:** <https://devforum.roblox.com/t/my-new-shop-gui-feedbacks/4859702>
- **Creator/publisher:** DevForum user Scrin_bs
- **Date posted / accessed:** 2026-09-08 / 2026-10-24
- **Access limitations:** Screenshots posted by the author; the live game was not played.

![df-4859702-00.jpg](../../Assets/UI/devforum/df-4859702-00.jpg)
![df-4859702-03.jpg](../../Assets/UI/devforum/df-4859702-03.jpg)

## What is observable
A "PACKS" window: red title bar, black body, rows per pack (Speed Pack, Jump Pack, Heal Pack, Destroyer Pack). Each row: a striped icon tile, "Contains:" with two item cards (red and yellow, with very small descriptive text), and **two stacked price buttons** (cyan diamond currency, grey coin currency). A flame "Top!" badge. Chevron rank icons per row. Saturated red + yellow + cyan + black, all at similar intensity.

## Community critique (quoted/paraphrased from the thread)
- "the color scheme is quite harsh and unpleasant … combined with all the sharp corners everywhere it makes for a hostile viewing experience" (0_devT)
- "Style clashing — the buttons to purchase items are high quality compared to … the X button (looks pixelated)" (verva1_n)
- "Padding is bad … Buttons don't fit at all … the robux icon blends" (ParadoxSoftwork)

## What works
- Clear row structure (what → contains → buy).
- The two currencies are given different button colours.

## Why it might work
The row grammar is easy to scan left-to-right.

## What does not work
- **Four saturated hues at equal intensity** → no focal point; red is used for both frame and content.
- Item descriptions inside cards are unreadable at screenshot size.
- Mixed rendering quality: crisp buy buttons next to a pixelated X (reply).
- Inconsistent padding; buttons not fitting their slots (reply with crops).

## Reusable principles
- **UI-003** One accent; **UI-004** consistent padding scale; **UI-007** every element rendered at the same fidelity ([UI Principles](../../17-Design-Principles/UI-Principles.md)).

## Roblox implementation
Define tokens in the Style Editor (background, surface, accent, currency colours) and apply via `StyleRule`s; use one `UIPadding` value set; 9-slice frames rendered at 2× to avoid pixelation.

## Original application
A sci-fi ammo shop on a dark neutral panel where only the "Buy" buttons carry colour (currency-coded), and pack contents are icons with one-word labels.

## Confidence
High that the issues are visible; community critique corroborates.

## Related
[Shops and Monetization UI](../Shops-and-Monetization-UI.md) · [Anti Pattern Catalog](../../15-Anti-Patterns-and-Failure-Cases/Anti-Pattern-Catalog.md) · [UI 22 DevForum Smash Style Buttons and Pictogram Guide](UI-22-DevForum-Smash-Style-Buttons-and-Pictogram-Guide.md)
