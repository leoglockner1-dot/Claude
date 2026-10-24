---
title: "Spellbound RPG: Contextual Radial Menu"
tags: [reference, ui]
reference_type: "image-analysis"
source_ref: "IMP-01 (earlier import package)"
date_accessed: "2026-10-24"
---

# Spellbound RPG: Contextual Radial Menu

## Metadata
- Category: UI / HUD / Menus and navigation
- Source: Roblox Creator Docs, "UI and UX design" > Prioritization (https://create.roblox.com/docs/production/game-design/ui-ux-design). Game: https://www.roblox.com/games/6468323505/
- Asset: see images below

![IMP-01_spellbound-radial-menu](../../Assets/UI/docs/IMP-01_spellbound-radial-menu.jpg)
![IMP-01_spellbound-radial-menu-closed](../../Assets/UI/docs/IMP-01_spellbound-radial-menu-closed.jpg)

- Date added: 2026-10-24
- Rating: 4/5 (subjective: "clear lesson worth reusing, minor flaws")
- Confidence: Medium. Two still frames only, so the transition animation was not seen.
- Reference type: Positive

## Context
A mobile-friendly HUD. One circular **Items** button sits alone on screen. When it's selected, three sibling buttons (Skills, Equipment, Deck) appear next to it. Roblox cites it as a "clean, minimalist UI" that keeps a small screen from being overwhelmed.

## What Works
- **Progressive disclosure.** Four destinations cost the screen space of one until the player asks for them.
- **Selected vs unselected is unmistakable.** The selected button gets a full-colour illustrated icon (brown book) and a larger label. Unselected ones are flat white glyphs.
- **The dark circular ring reads on busy terrain.** The ring and dark fill separate the icon from the brown and white snowy ground.
- **Chunky outlined labels** stay legible over the 3D world.

## What Does Not Work
- Two icon styles (illustrated vs flat glyph) are used at once. It works as a state signal here, but copied carelessly it looks inconsistent.
- All-caps display font everywhere means there's no typographic hierarchy inside the labels.

## Visual Analysis
- Hierarchy: the selected state wins on size, colour and detail at once (three cues stacked).
- Shape language: perfect circles with bevelled dark rims. Soft and toy-like, which fits a fantasy RPG.
- Usability: large round targets suit thumbs. Labels sit above the buttons, so a finger doesn't cover them.

## Reusable Design Rules
1. Hide secondary navigation behind one parent button on mobile. Reveal it on tap and collapse it on outside-tap.
2. Signal the selected state with **at least two** cues (size and colour, or colour and detail), never colour alone.
3. Put a solid ring or plate behind HUD icons that sit over the 3D world.

## Anti-Patterns
- Don't nest more than one level of radial reveal, because players lose track.
- Don't mix illustrated and flat icons **unless** the difference carries meaning, such as state.

## Roblox implementation
Build a `Frame` with `UIListLayout` (horizontal) for the children. Tween their `GroupTransparency` (CanvasGroup) and `Size` from 0 with `Back`/`Out` at about 0.15–0.2 s, and snap instantly if `GuiService.ReducedMotionEnabled`. Use your own icon set and shape language rather than circles and books.

## Original application
A crafting game: one "Workbench" button that fans out Recipes / Materials / Upgrades as tilted paper tags pinned to it, matching a workshop theme.

## Limitations
The opening animation, sound and the gamepad/keyboard equivalents were not observable. "Selected" is inferred from the cursor and the doc alt text.

## Related
[HUD Design](../HUD-Layouts.md) · [Menus and Navigation](../Menus-and-Navigation.md) · [Mobile UI](../Mobile-Controller-and-Accessibility.md) · [UI Design Principles](../../14-Design-Principles/UI-Principles.md)
