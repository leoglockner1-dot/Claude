---
title: "Spellbound RPG: Spells-as-Cards Metaphor"
tags: [reference, ui]
reference_type: "image-analysis"
source_ref: "IMP-13 (earlier import package)"
date_accessed: "2026-10-24"
---

# Spellbound RPG: Spells-as-Cards Metaphor

## Metadata
- Category: UI / Game design / Metaphor
- Source: Roblox Creator Docs, "UI and UX design" > Design interactions > Metaphors. Game: https://www.roblox.com/games/6468323505/
- Asset: see images below

![IMP-13_spellbound-card-combat](../../Assets/UI/docs/IMP-13_spellbound-card-combat.jpg)

- Date added: 2026-10-24
- Rating: 3.5/5
- Confidence: Medium. One frame of an animation.
- Reference type: Mixed

## Context
Turn-based combat inside a glowing summoning circle. The player's spells appear as a fanned hand of cards. The card under the cursor is enlarged. PASS and FLEE buttons sit below, a turn timer (21) above, and HP and gold bottom-left.

## What Works
- **Metaphor.** Casting abstract spells is mapped onto drawing and playing cards, which players already understand. Roblox's point is that the metaphor removes a tutorial.
- **Hover enlarge** isolates the card being considered.
- **The cost badge** (orange circle with a number) sits in the same corner on every card.
- The combat stage is **diegetic**: an arena circle on the ground with participant slots.

## What Does Not Work
- **Card text is unreadable at this size** ("120-160 … One target"). On a phone it's illegible.
- The arena rings, glow, cards, badges and floating names all compete. There's no calm zone around the decision.

## Reusable Design Rules
1. Find a **real-world metaphor** for abstract systems (cards = spells, backpack = inventory, recipe = crafting).
2. Make cards readable through **icon + one number**, and leave detailed text to an inspect state.
3. During decisions, dim or blur the world to give the choice a calm background.

## Original application
Abstract enchantments represented as gemstones socketed into a sword — familiar "socket" metaphor.

## Limitations
The animation, sounds and the effects that play when a card is used weren't observed.

## Related
[Core Loops](../../03-Core-Gameplay-Loops/Core-Loop-Framework.md) · [UI Design Principles](../../17-Design-Principles/UI-Principles.md) · [Typography and Spacing](../Typography-Color-and-Spacing.md)
