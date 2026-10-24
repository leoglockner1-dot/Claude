# Reference IMP-20 — Squishmallows: Contextual (Just-in-Time) Tutorials

## Metadata
- Category: Gameplay / Onboarding
- Source: Roblox Creator Docs, "Onboarding techniques" > Contextual tutorials. Game: https://www.roblox.com/games/7941853407/
- Asset: `../Assets/Gameplay/IMP-20_squishmallows-contextual-1.png`, `../Assets/Gameplay/IMP-20_squishmallows-contextual-2.png`, `../Assets/Gameplay/IMP-20_squishmallows-market-1.png`, `../Assets/Gameplay/IMP-20_squishmallows-market-2.png`
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

## Related Notes
[Retention and Replayability](../05_Game_Design/Retention_and_Replayability.md) · [Core Loops](../05_Game_Design/Core_Loops.md) · [Menus and Navigation](../02_UI_UX/Menus_and_Navigation.md)
