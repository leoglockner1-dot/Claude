---
title: "UI-18 — Industrial terminal main menu with one dominant action (Package Inspector, DevForum)"
tags: [reference, ui, menus]
reference_type: "DevForum UI screenshot + critique (Mostly positive)"
date_accessed: "2026-10-24"
---

# UI-18 — Industrial terminal main menu with one dominant action (Package Inspector, DevForum)

## Identity
- **Name:** UI-18 — Industrial terminal main menu with one dominant action (Package Inspector, DevForum)
- **Reference type:** DevForum UI screenshot + critique (Mostly positive)
- **Source URL:** <https://devforum.roblox.com/t/pre-alpha-package-inspector-main-menu-ui-feedback/4672756>
- **Creator/publisher:** DevForum user ImmuneJar
- **Date posted / accessed:** 2026-06-07 / 2026-10-24
- **Access limitations:** Screenshots posted by the author; the live game was not played.

![df-4672756-00.jpg](../../Assets/UI/devforum/df-4672756-00.jpg)

## What is observable
A dark panel top-left: blue square logo + "PACKAGE INSPECTOR", then a **highlighted blue "▶ START SOLO"** button, then dark rows STATS / SHOP / HOW TO PLAY / SETTINGS with glyph icons, and a footer "Cash: $634 · Level: 16 · Highest Shift: 5". The right ~80 % is intentionally empty (for a lobby background). Tiny version text bottom-right.

## Community critique (quoted/paraphrased from the thread)
- "use images rather than emojis/symbols" (foxiegamerr13)
- "the font size for the text in the buttons are too large … so it looks different from 'PACKAGE INSPECTOR' … the stats below settings are a little cluttered" (ROBBEROX8)

## What works
- Exactly **one** saturated element = the primary action.
- Theme (warehouse terminal) is consistent: monospace-like caps, dark industrial palette.
- Progress summary on the menu gives a reason to continue.

## Why it might work
Decision speed improves when one action dominates (NN/g visual hierarchy: colour/contrast + scale).

## What does not work
- Button text same size/weight as the title (reply) → title loses hierarchy.
- Footer stats cramped; emoji/symbol icons instead of designed icons (reply).
- Text is small for phones.

## Reusable principles
- **UI-001** One primary action per screen; **UI-002** at most 4–5 type sizes with clear steps.

## Roblox implementation
Left-anchored `Frame` with `UIListLayout` (Padding 8 px), primary button with accent fill, others `BackgroundTransparency` 0.6; `UITextSizeConstraint` minimums for phones.

## Original application
A lighthouse-keeper game menu: one lit "Start Night Shift" lamp-button; other options are unlit brass plaques.

## Confidence
High.

## Related
[Menus and Navigation](../Menus-and-Navigation.md) · [R01 Polished Main Menu](../../18-Skill-Training/Design-Recipes/R01-Polished-Main-Menu.md)
