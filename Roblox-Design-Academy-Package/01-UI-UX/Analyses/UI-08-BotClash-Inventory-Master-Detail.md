---
title: "BotClash Simulator: Inventory Master-Detail"
tags: [reference, ui]
reference_type: "image-analysis"
source_ref: "IMP-08 (earlier import package)"
date_accessed: "2026-10-24"
---

# BotClash Simulator: Inventory Master-Detail

## Metadata
- Category: UI / Inventory / Buttons
- Source: Roblox Creator Docs, "UI and UX design" > Visual language > Buttons. Game: https://www.roblox.com/games/9300407930/
- Asset: see images below

![IMP-08_botclash-inventory](../../Assets/UI/docs/IMP-08_botclash-inventory.jpg)

- Date added: 2026-10-24
- Rating: 4.5/5
- Confidence: High
- Reference type: Positive

## Context
A collection inventory with Bots, Mounts and Items tabs. A grid of hexagonal bot cards sits on the left with a scrollbar. A detail panel for the selected bot is on the right. An action bar runs along the bottom.

## What Works
- **A distinctive, consistent shape language.** Chamfered (cut-corner) tabs, a chamfered close-button corner and chamfered action buttons, plus hexagon item cards. You'd recognise this UI from a crop, which is what *identity* means.
- **Master-detail layout.** Browse on the left, inspect and act on the right. No popups.
- **Rarity is shown by hexagon colour** (blue, purple, gold, teal), and the detail panel repeats it with the "Epic" label in purple.
- **One warm accent equals the primary action.** "DEPLOY BEST" is the only orange element in a blue and cyan UI, so the eye goes there first.
- The selected tab is bright cyan with dark text, and unselected tabs are dark with cyan text. That's a clear inversion.
- Small status badges show locked (padlock) and equipped (check).
- The capacity readout "28/200" and "Squad Power: 375,728" summarise the whole collection.

## What Does Not Work
- The white bottom bar breaks the dark-panel scheme and feels pasted on.
- The badges (lock and check) are small for touch inspection.

## Reusable Design Rules
1. Choose **one geometric motif** (chamfer, rounded pill, hexagon, ink brush…) and apply it to tabs, buttons, cards and the close button. That's cheap and strong identity.
2. Keep exactly one accent colour for the single most valuable action on a screen.
3. Use master-detail for collections over about 12 items instead of modal detail popups.
4. Selected tab = inverted colours, not just a thin underline.

## Anti-Patterns
- Copying this exact motif (chamfer + cyan) produces a clone. Take the *principle* of one motif and choose your own.

## Roblox implementation
Use 9-slice (`ScaleType.Slice`) chamfer images so one texture serves every size. Build the grid with `UIGridLayout` inside a `ScrollingFrame` with `AutomaticCanvasSize`. Selecting a card updates the detail panel and doesn't open a new window.

## Original application
A robot-racing garage using one rounded-hexagon motif for every card, tab and button, with only "RACE" in the accent colour.

## Limitations
No motion or sound seen. Gamepad navigation order wasn't checked.

## Related
[Shops and Inventory](../Shops-and-Monetization-UI.md) · [UI Design Principles](../../17-Design-Principles/UI-Principles.md) · [01 Visual Design Principles](../../11-Visual-Identity/Visual-Identity-Framework.md)
