# Reference IMP-07 — Winds of Fortune: Colour-Coded Stat Icon System

## Metadata
- Category: UI / Visual language / Iconography
- Source: Roblox Creator Docs, "UI and UX design" > Visual language > Icons. Game: https://www.roblox.com/games/7714627632/
- Asset: `../Assets/UI/IMP-07_winds-of-fortune-stats.png`
- Date added: 2026-10-24
- Rating: 4.5/5
- Confidence: High
- Reference type: Positive

## Context
A stats screen. On the left is a list of derived stats (attack types, health, mana, stamina, regen rates). On the right, five attributes (Strength, Dexterity, Constitution, Intellect, Wisdom) each show "Increases:" followed by the icons of the stats they raise.

## What Works
- **Icon families share colour and shape.** Orange is melee and ranged attack, which Strength raises. Yellow-orange is stamina and dexterity. Green hearts are health and Constitution. Blue is magic and Intellect. Purple is mana and Wisdom.
- **Each attribute name is coloured like the icons it affects.** The cause→effect relationship is visible without reading a tooltip.
- **Modifier glyphs are reused**: "+" means max or regen and "↑" means increase, applied consistently across every family.
- One serif display font in cream, a hand-drawn icon style and a dark translucent panel give it a coherent fantasy identity.

## What Does Not Work
- The helper text "You gain stat points every time you level up." is small grey on dark, with low contrast.
- "Available Points: 0" in red reads like an error rather than a neutral zero.
- Many numbers have identical weight, so nothing guides the eye inside the left list.

## Reusable Design Rules
1. Build an **icon grammar**: base shape = resource, colour = family, modifier glyph = variation (+ regen, ↑ boost).
2. Colour labels with the same hue as the icons they control, so relationships become visible.
3. Red means bad or blocked. Don't use it for neutral values.

## Anti-Patterns
- Colour-only distinctions. This screen is safe because shape also differs (heart vs boot vs flame), so keep that property when copying the idea.

## Application to Roblox Development
Define a palette module (`Theme.Health = Color3...`) and reuse it in icons, bars, text (`RichText` `<font color>`) and VFX. Draw icons as one sprite sheet (`ImageRectOffset`) to save memory.

## Limitations
Static image, so interaction (spending points) and feedback weren't seen.

## Related Notes
[UI Design Principles](../02_UI_UX/UI_Design_Principles.md) · [01 Visual Design Principles](../01_Visual_Design_Principles.md) · [Typography and Spacing](../02_UI_UX/Typography_and_Spacing.md)
