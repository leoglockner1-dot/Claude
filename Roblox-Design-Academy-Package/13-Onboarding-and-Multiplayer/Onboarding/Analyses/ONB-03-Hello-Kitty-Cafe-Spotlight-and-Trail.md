---
title: "Hello Kitty Cafe: Spotlight Highlight and Floor Trail"
tags: [reference, onboarding]
reference_type: "image-analysis"
source_ref: "IMP-17 (earlier import package)"
date_accessed: "2026-10-24"
---

# Hello Kitty Cafe: Spotlight Highlight and Floor Trail

## Metadata
- Category: Gameplay / Onboarding / UI highlight
- Source: Roblox Creator Docs, "Onboarding techniques" > Highlights; Enhance immersion
- Asset: see images below

![IMP-17_hello-kitty-cafe-highlight](../../../Assets/Gameplay/docs/IMP-17_hello-kitty-cafe-highlight.jpg)
![IMP-17_hello-kitty-cafe-trail](../../../Assets/Gameplay/docs/IMP-17_hello-kitty-cafe-trail.jpg)

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

## Roblox implementation
- UI spotlight: a full-screen dark `Frame` (BackgroundTransparency about 0.5) with the target cloned above it, or 4 frames around the target's AbsolutePosition.
- Floor trail: a `Beam` with a dot texture, or spaced parts with `Highlight` (mind the 255 limit).

## Original application
A first-time pizza order: the dough station glows and a dotted flour trail leads to it; the chef mascot says "Knead!".

## Related
[Retention and Replayability](../First-Session-Design.md) · [Menus and Navigation](../../../01-UI-UX/Menus-and-Navigation.md) · [VFX Principles](../../../09-VFX/VFX-Principles-and-Performance.md)
