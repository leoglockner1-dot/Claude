# Reference IMP-17 — Hello Kitty Cafe: Spotlight Highlight and Floor Trail

## Metadata
- Category: Gameplay / Onboarding / UI highlight
- Source: Roblox Creator Docs, "Onboarding techniques" > Highlights; Enhance immersion
- Asset: `../Assets/Gameplay/IMP-17_hello-kitty-cafe-highlight.png`, `../Assets/Gameplay/IMP-17_hello-kitty-cafe-trail.png`
- Date added: 2026-10-24
- Rating: 4.5/5
- Confidence: Medium. The "dim the rest" effect is described by Roblox; the screenshot shows the arrow and outline.
- Reference type: Positive

## Context
1. In the build menu, a pink arrow points at the Counters button, the button is outlined, and Hello Kitty says "Select counter type."
2. In the café, a trail of pink dots runs along the floor from the player to Hello Kitty.

## What Works
- **Pointing beats describing.** No "find the counter button in the furniture menu".
- **The guide character speaks the instruction**, which keeps the brand voice. The text is three words.
- **A brand-coloured floor trail** suggests a path without forcing it. Roblox notes this keeps choice and immersion.

## Reusable Design Rules
1. Tutorial UI highlight = **arrow + outline + (optional) dim everything else**. Only the target stays interactive.
2. Floor trails use the brand accent colour, are spaced dots or chevrons, and **fade once the goal is reached**.
3. Put instructions in a character's mouth with the shortest possible imperative.

## Application to Roblox Development
- UI spotlight: a full-screen dark `Frame` (BackgroundTransparency about 0.5) with the target cloned above it, or 4 frames around the target's AbsolutePosition.
- Floor trail: a `Beam` with a dot texture, or spaced parts with `Highlight` (mind the 255 limit).

## Related Notes
[Retention and Replayability](../05_Game_Design/Retention_and_Replayability.md) · [Menus and Navigation](../02_UI_UX/Menus_and_Navigation.md) · [VFX Principles](../04_Animation_And_Game_Feel/VFX_Principles.md)
