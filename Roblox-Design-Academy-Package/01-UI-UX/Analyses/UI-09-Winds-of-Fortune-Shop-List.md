---
title: "Winds of Fortune: Clothing Shop List Typography"
tags: [reference, ui]
reference_type: "image-analysis"
source_ref: "IMP-09 (earlier import package)"
date_accessed: "2026-10-24"
---

# Winds of Fortune: Clothing Shop List Typography

## Metadata
- Category: UI / Typography / Shops
- Source: Roblox Creator Docs, "UI and UX design" > Visual language > Text. Game: https://www.roblox.com/games/7714627632/
- Asset: see images below

![IMP-09_winds-of-fortune-clothing-list](../../Assets/UI/docs/IMP-09_winds-of-fortune-clothing-list.jpg)

- Date added: 2026-10-24
- Rating: 3.5/5
- Confidence: High
- Reference type: Mixed

## Context
A vertical shop list. The coin balance is at the top. Each row has an item icon, a name, the category and a coin price.

## What Works
- **Clear two-level type hierarchy**: a large cream serif name, then smaller grey category and price.
- **The price colour is yellow and matches the coin icon**, so the currency is recognisable instantly.
- **The selected or hovered row gets a soft radial glow**, a subtle state change that needs no border.
- **The balance sits at the top of the list**, so the player can compare it with prices without leaving the screen.

## What Does Not Work
- **"Clothing" repeats on every row.** That's redundant information taking space, and it should be a header.
- **Dark clothing icons on a dark background** have low contrast, and the icons are small.

## Reusable Design Rules
1. Per row: **name (primary) → price (secondary, currency-coloured) → meta (tertiary, muted)**.
2. Information shared by all rows belongs in a header, not in each row.
3. Item icons need a light plate or rim when the item itself is dark.

## Roblox implementation
Use `UIListLayout` + `AutomaticSize.Y` rows and `TextService` checks for long names. If the price is unaffordable, turn it red (Roblox's consistency example) plus a lock icon.

## Original application
A potion shop list: potion name large, price in gem colour, category as a section header instead of per row.

## Related
[Typography and Spacing](../Typography-Color-and-Spacing.md) · [Shops and Inventory](../Shops-and-Monetization-UI.md)
