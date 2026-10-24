---
title: "Squishmallows: Contextual (Just-in-Time) Tutorials"
tags: [reference, onboarding]
reference_type: "image-analysis"
source_ref: "IMP-20 (earlier import package)"
date_accessed: "2026-10-24"
---

# Squishmallows: Contextual (Just-in-Time) Tutorials

## Metadata
- Category: Gameplay / Onboarding
- Source: Roblox Creator Docs, "Onboarding techniques" > Contextual tutorials. Game: https://www.roblox.com/games/7941853407/
- Asset: see images below

![IMP-20_squishmallows-contextual-1](../../Assets/Gameplay/docs/IMP-20_squishmallows-contextual-1.jpg)
![IMP-20_squishmallows-contextual-2](../../Assets/Gameplay/docs/IMP-20_squishmallows-contextual-2.jpg)
![IMP-20_squishmallows-market-1](../../Assets/Gameplay/docs/IMP-20_squishmallows-market-1.jpg)
![IMP-20_squishmallows-market-2](../../Assets/Gameplay/docs/IMP-20_squishmallows-market-2.jpg)

- Date added: 2026-10-24
- Rating: 4/5 (technique), 3/5 (presentation)
- Confidence: High for the technique, Medium for visuals
- Reference type: Mixed

## Context
When the player first holds two identical Squishmallows, NPC Jenny explains combining three of them at the combination machine. When the player first reaches the market, Mayor Mike says "Let me show you how it works!".

## What Works
- **The trigger is the player's state, not a timeline.** The tutorial appears exactly when it becomes useful, which Roblox ties to better retention of the lesson and shorter onboarding.
- Mid- and late-game systems (the player market) are **not** in the first-session tutorial at all.
- Named NPCs (name tag above the bubble) make instructions feel social.

## What Does Not Work
- The speech bubbles are large white rounded boxes covering the lower half of the screen, with plain bold black text. Functional but generic. The bubble style doesn't express the plush-toy identity.
- Multi-line text per bubble. It could be shorter.

## Reusable Design Rules
1. Make a **trigger table**: feature → first-relevant condition → 1–2 line tutorial. Teach nothing before its trigger.
2. Keep the first session to the core loop only.
3. Style dialogue bubbles to the game's identity (shape, colour, font).

## Original application
A pet-fusion tutorial that triggers only when the player owns two identical pets, delivered by the fusion machine itself lighting up.

## Related
[Retention and Replayability](../First-Session-Design.md) · [Core Loops](../../03-Core-Gameplay-Loops/Core-Loop-Framework.md) · [Menus and Navigation](../../01-UI-UX/Menus-and-Navigation.md)
