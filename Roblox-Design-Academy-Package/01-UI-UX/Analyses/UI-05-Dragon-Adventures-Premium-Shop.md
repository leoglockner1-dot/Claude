---
title: "Dragon Adventures: Premium Coin Shop"
tags: [reference, ui]
reference_type: "image-analysis"
source_ref: "IMP-05 (earlier import package)"
date_accessed: "2026-10-24"
---

# Dragon Adventures: Premium Coin Shop

## Metadata
- Category: UI / Shops
- Source: Roblox Creator Docs, "UI and UX design" > Attention. Game: https://www.roblox.com/games/3475397644/
- Asset: see images below

![IMP-05_dragon-adventures-premium-shop](../../Assets/UI/docs/IMP-05_dragon-adventures-premium-shop.jpg)

- Date added: 2026-10-24
- Rating: 4/5
- Confidence: High (clean full-panel screenshot)
- Reference type: Mixed (mostly positive)

## Context
A Robux shop for coin bundles. Four category tabs sit on top (Gamepasses, Boosts, Coins, Bundles). Six bundles fill a 2×3 grid, and a separate tall "BEST VALUE!" card stands on the right.

## What Works
- **Value is shown by illustration scale.** The art grows with the amount: coin stack → coin pile → bag → barrel → chest → cauldron → vault. You can rank the bundles without reading a number.
- **The top-value bundle is isolated.** It gets its own tall card, more padding, a red ribbon, a light-ray glow and "70% Off!". Roblox calls this out explicitly ("increasing its size and separating it with more padding").
- **Every price button looks the same**: green, Robux glyph, number. Once learned, a player can scan them instantly.
- **The close button follows convention**: red, top-right, white X.
- "Most Popular!" is a small star badge, a secondary emphasis that stays below "Best value".

## What Does Not Work
- **The tabs are four saturated colours** (green, purple, orange, blue). The green tab matches the green price buttons, so tabs and buttons compete.
- **The selected tab (Coins) is darker and recessed**, which can read as disabled. Selected states should look *more* active, not less.
- Decorative frame, ribbon and texture are heavy. It fits the cartoon-fantasy identity, but it's the upper limit.

## Visual Analysis
- Hierarchy: Best value > Most popular > the rest. A clear three-step ladder.
- Colour: gold coins on a purple panel (complementary pair) make the products pop.
- Spacing: an even grid with consistent card padding.

## Reusable Design Rules
1. Scale **product art** with value, so the quantity can be understood without text.
2. Give one hero offer **space**, not just a badge. Padding and size beat stickers.
3. A selected tab must be the most saturated or brightest, never the darkest.
4. Reserve one colour for "buy" (here green) and use it nowhere else in the panel.

## Anti-Patterns
- Multiple "best/popular/hot/limited" badges on one screen cancel each other out. Use one hero and at most one secondary badge.
- Fake or permanent discounts. "70% off" must be true relative to the base rate, or you lose trust (an ethical and policy risk, not verified for this game).

## Roblox implementation
Build a 2×3 `UIGridLayout` and a sibling hero `Frame`. Use `UIStroke` and `UICorner` on cards, and one 9-slice frame texture for the panel to keep memory low. Tie price buttons to `MarketplaceService:PromptProductPurchase` with a pending or disabled state while the prompt is open.

## Original application
A bakery shop whose bundles grow from a single cupcake to a full cake tower; the best-value tower stands alone on a pedestal card.

## Limitations
Hover and press states, purchase feedback and the mobile layout weren't seen.

## Related
[Shops and Inventory](../Shops-and-Monetization-UI.md) · [UI Design Principles](../../14-Design-Principles/UI-Principles.md) · [UI Anti Patterns](../../12-Anti-Patterns-and-Design-Critique/Anti-Pattern-Catalog.md)
