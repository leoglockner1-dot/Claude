---
title: "The Survival Game: Minimal Survival HUD"
tags: [reference, ui]
reference_type: "image-analysis"
source_ref: "IMP-03 (earlier import package)"
date_accessed: "2026-10-24"
---

# The Survival Game: Minimal Survival HUD

## Metadata
- Category: UI / HUD
- Source: Roblox Creator Docs, "UI and UX design" > Prioritization. Game: https://www.roblox.com/games/11156779721/
- Asset: see images below

![IMP-03_the-survival-game-hud](../../Assets/UI/docs/IMP-03_the-survival-game-hud.jpg)

- Date added: 2026-10-24
- Rating: 4/5
- Confidence: Medium (one desktop screenshot)
- Reference type: Positive

## Context
An open-world survival HUD. The player needs to monitor health and hunger and reach the map, inventory and tools quickly.

## What Works
- **The centre is empty.** All UI sits on the edges, and the avatar and horizon own the middle of the screen.
- **The two survival stats are top-right**: health (red bar, 100/100, red "+" icon) and hunger (orange bar, 423/1300, orange food icon). Each bar's colour matches its icon.
- **One button family.** Every menu button is the same dark-teal circle with a light ring: Q quests and T shop on the left, V avatar, E inventory and C crafting on the right.
- **Keybind letters are printed on each button** (Q, T, V, E, C). The hotbar shows 1, 2, 3.
- **Tool hotbar bottom-centre, only three slots.** It follows the Roblox convention, so it's instantly familiar.

## What Does Not Work
- The keybind letters are tiny, and they're meaningless on touch. They should hide when `PreferredInput` is touch (unknown whether they do).
- Six side buttons are pure icons with no labels, so first-time players have to guess (backpack vs avatar).

## Visual Analysis
- Hierarchy: survival stats get colour; navigation is neutral teal. Information that changes is coloured, static navigation is muted. A good split.
- Spacing: buttons are evenly stacked with generous gaps, and the margins look consistent.

## Reusable Design Rules
1. Keep the centre third of the screen free of persistent UI.
2. **Colour = live state, neutral = navigation.** Only bars and alerts get saturated colour.
3. Show input hints that match the active device, and hide keyboard letters on touch.
4. Use few hotbar slots early and unlock more with progression.

## Anti-Patterns
- Icon-only buttons for non-conventional features. Add a label on first view, or a long-press tooltip.

## Roblox implementation
Two `ScreenGui`s with `ScreenInsets = CoreUISafeInsets`. Edge stacks use `UIListLayout` with fixed `Padding`. Hint labels come from `InputActionLabel`. Bars are a `Frame` with a fill child whose `Size.X.Scale` is tweened (Quad Out, about 0.2 s).

## Original application
A space-survival HUD where oxygen and power gauges live top-right, the centre stays empty, and three suit-module buttons hug the right edge.

## Limitations
Desktop only. The mobile layout, animations and audio weren't seen.

## Related
[HUD Design](../HUD-Layouts.md) · [Mobile UI](../Mobile-Controller-and-Accessibility.md) · [UI Design Principles](../../17-Design-Principles/UI-Principles.md)
