---
title: "Tower Defense Simulator: Daily Skins and Crates Shop"
tags: [reference, ui]
reference_type: "image-analysis"
source_ref: "IMP-06 (earlier import package)"
date_accessed: "2026-10-24"
---

# Tower Defense Simulator: Daily Skins and Crates Shop

## Metadata
- Category: UI / Shops
- Source: Roblox Creator Docs, "UI and UX design" > Attention. Game: https://www.roblox.com/games/3260590327/
- Asset: see images below

![IMP-06_tower-defense-simulator-daily-shop](../../Assets/UI/docs/IMP-06_tower-defense-simulator-daily-shop.jpg)

- Date added: 2026-10-24
- Rating: 3.5/5
- Confidence: Medium
- Reference type: Mixed

## Context
A daily rotating shop. On the left are three tall "Daily tower skins" cards. On the right is a dark panel of "Daily crates" (2×2) with a restock timer. Six category tabs with 3D icons run across the top.

## What Works
- **Two groups are separated by size and proximity.** Skins are tall portrait cards, crates are small squares inside their own dark container. Roblox cites exactly this.
- **Rarity is encoded in the card background colour**: green for Uncommon, grey for Common. A text tag ("✨ Uncommon") repeats it, so colour isn't the only signal.
- **Locked state follows convention**: grey button plus padlock plus "Locked".
- **Currency is distinguished by icon**: gold coin vs R$ glyph on the same green button shape.
- The restock timer is placed **in the section header** ("Restock in 23:26:00"), where the question "when does this change?" comes up.

## What Does Not Work
- A "[NEW]" tag clips behind the tab bar. That's an unpolished layering bug.
- Tab labels overlap their 3D icons, and the strip feels cramped.
- Robux and coin purchases share the same green button. Only the small icon tells them apart, which is risky for accidental Robux spending. A distinct treatment for real-money buttons is safer.

## Reusable Design Rules
1. Group by **container**: different product types get different card shapes and their own panel.
2. Rarity = background colour **plus** a text tag (colour non-reliance).
3. Put countdowns in the header of the thing that changes.
4. Give real-money (Robux) buttons a visual treatment that is distinct from soft-currency buttons.

## Anti-Patterns
- Overlapping tags and clipped labels. Test with the longest localized strings.

## Roblox implementation
Use `ZIndex` / `ZIndexBehavior.Sibling` to prevent tag clipping, and `TextService:GetTextSize` to test label fit. Drive the server-time countdown from a `workspace:GetServerTimeNow()`-based restock timestamp.

## Original application
A garden store with tall seed-packet cards for daily seeds and a separate crate panel for random packs (with labelled odds).

## Limitations
No interaction states and no mobile view. Crate purchases are paid random items, so odds disclosure must be visible before purchase ([Verified facts](../../14-Technical-Reference/Roblox-Platform-Facts.md)). Whether this screen complies wasn't checked.

## Related
[Shops and Inventory](../Shops-and-Monetization-UI.md) · [UI Design Principles](../../17-Design-Principles/UI-Principles.md) · [Reward Reveal Sequences](../../08-Animation-and-Game-Feel/Reward-Reveals-and-Celebrations.md)
