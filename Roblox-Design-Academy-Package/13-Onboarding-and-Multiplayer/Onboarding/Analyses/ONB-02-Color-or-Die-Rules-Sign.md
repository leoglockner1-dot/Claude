---
title: "Color or Die: In-World 'How to Play' Sign"
tags: [reference, onboarding]
reference_type: "image-analysis"
source_ref: "IMP-16 (earlier import package)"
date_accessed: "2026-10-24"
---

# Color or Die: In-World "How to Play" Sign

## Metadata
- Category: Gameplay / Onboarding
- Source: Roblox Creator Docs, "Onboarding techniques" > Visual elements > Prominence
- Asset: see images below

![IMP-16_color-or-die-rules-sign](../../../Assets/Gameplay/docs/IMP-16_color-or-die-rules-sign.jpg)

- Date added: 2026-10-24
- Rating: 5/5 for the technique
- Confidence: High
- Reference type: Positive

## Context
The player collects their first paint bucket. Straight ahead is a wall poster titled "How to Play!" with three stick-figure panels:
- a red figure on a red wall: "Hidden!"
- a red figure on a blue wall: "Dead!"
- a third mismatch: "Dead!"

The floor says "Pick up the first color" with an arrow.

## What Works
- **The core rule is taught in three pictures.** Roblox contrasts it with the 50-word paragraph it replaces.
- **It's in the line of sight, but it doesn't block anything.** The player can't miss it and doesn't have to dismiss it.
- **Good vs bad outcomes are shown side by side.** Players learn the rule from the contrast.
- Hand-drawn style is cheap to make and charming, and it reads like a note left by a previous survivor.

## Reusable Design Rules
1. Explain the core mechanic as **2–3 picture panels with one-word captions**, placed in the world on the first path.
2. Show the **failure state** next to the success state.
3. Pair the sign with a **first concrete action** ("Pick up the first color").

## Anti-Patterns
- Text-only popups at spawn. Players skip them (Roblox: "Players generally don't like to read instructions").

## Roblox implementation
Use a `SurfaceGui` or decal on a wall part next to the spawn exit. Make sure it's readable at the default camera distance on a phone.

## Original application
A floor-is-lava game whose first room shows three pictograms: on carpet = safe, on tiles = burn, jump = cross.

## Related
[Core Loops](../../../03-Core-Gameplay-Loops/Core-Loop-Framework.md) · [Retention and Replayability](../First-Session-Design.md) · [01 Visual Design Principles](../../../11-Visual-Identity/Visual-Identity-Framework.md)
