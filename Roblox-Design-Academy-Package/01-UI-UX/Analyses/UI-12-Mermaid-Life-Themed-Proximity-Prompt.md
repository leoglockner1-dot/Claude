---
title: "Mermaid Life: Themed Proximity Prompt"
tags: [reference, ui]
reference_type: "image-analysis"
source_ref: "IMP-12 (earlier import package)"
date_accessed: "2026-10-24"
---

# Mermaid Life: Themed Proximity Prompt

## Metadata
- Category: UI / World-space prompts / Conventions
- Source: Roblox Creator Docs, "UI and UX design" > Design interactions > Conventions. Game: https://www.roblox.com/games/4377254026/
- Asset: see images below

![IMP-12_mermaid-life-proximity-prompt](../../Assets/UI/docs/IMP-12_mermaid-life-proximity-prompt.jpg)

- Date added: 2026-10-24
- Rating: 4.5/5
- Confidence: High
- Reference type: Positive

## Context
A player stands next to a shell-shaped chair. A world-space prompt shows a glossy pink bubble with "E" and the label "Sit".

## What Works
- **The convention is kept** (key glyph + verb) and **restyled** to match the game's palette: a pink-violet pearly bubble with an underwater feel.
- **A one-word verb label** ("Sit") instead of "Press E to sit on the chair".
- A small ring above marks the anchor point on the object.

## Reusable Design Rules
1. Customise `ProximityPrompt` visuals (`Style = Custom`) to the game's identity, but keep "key glyph + short verb".
2. Use a single verb as the label, plus an optional object name.
3. Show the platform glyph per input (E on keyboard, a button icon on gamepad, a tap target on touch).

## Roblox implementation
`ProximityPrompt.Style = Enum.ProximityPromptStyle.Custom` and build the billboard UI from `ProximityPromptService.PromptShown`. Use `UserInputService:GetImageForKeyCode` for gamepad glyphs. Keep `MaxActivationDistance` tight so prompts don't stack in crowded rooms.

## Original application
A haunted-house prompt rendered as a flickering candle with key glyph + "Light".

## Related
[UI Design Principles](../../17-Design-Principles/UI-Principles.md) · [Mobile UI](../Mobile-Controller-and-Accessibility.md)
