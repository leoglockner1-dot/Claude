---
title: "Close-Button Convention Across Four Games"
tags: [reference, ui]
reference_type: "image-analysis"
source_ref: "IMP-10 (earlier import package)"
date_accessed: "2026-10-24"
---

# Close-Button Convention Across Four Games

## Metadata
- Category: UI / Conventions / Visual identity
- Source: Roblox Creator Docs, "UI and UX design" > Conventions. Games: Winds of Fortune, Dragon Adventures, BotClash Simulator, DOORS
- Asset: see images below

![IMP-10_close-button-convention](../../Assets/UI/docs/IMP-10_close-button-convention.jpg)

- Date added: 2026-10-24
- Rating: 5/5 as a teaching example
- Confidence: High
- Reference type: Positive (comparison)

## Context
Four close buttons are shown side by side. Visually they have nothing in common:
- Winds of Fortune: a thin cream serif "X" on dark red.
- Dragon Adventures: a red bevelled square with a dark "X".
- BotClash: a cyan chamfered corner with a dark-blue "X".
- DOORS: a big flat cream "X" next to a code-entry field.

## What Works
- **Placement and symbol stay fixed (top-right "X"). Style changes completely.** Every one is recognisable as "close" in under a second, and every one belongs to its own game.

## Reusable Design Rules
1. **Follow conventions in *placement and meaning*. Express identity in *styling*.** This is the central answer to "how do I avoid generic UI without confusing players".
2. Conventions worth keeping: X = close (top-right), grey = unusable, padlock = locked, "E" proximity prompt = interact, number keys = hotbar, ground circle = queue.
3. Before you break a convention, write down why and test it with new players.

## Anti-Patterns
- **Generic** isn't the same as **conventional**. Generic is copying another game's *styling*. Conventional is using the shared *grammar*.

## Roblox implementation
Make one `CloseButton` component and use it in every panel. Bind it to Escape and gamepad B (`ButtonB`), and make it a large enough touch target even if the visible glyph is small (put an invisible bigger hitbox around it).

## Original application
A cozy-farm game using a wooden peg "X" — top-right, same meaning, wholly different style.

## Related
[UI Design Principles](../../14-Design-Principles/UI-Principles.md) · [UI Anti Patterns](../../12-Anti-Patterns-and-Design-Critique/Anti-Pattern-Catalog.md) · [01 Visual Design Principles](../../07-Visual-Identity/Visual-Identity-Framework.md)
