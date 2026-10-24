---
title: "Arcane Odyssey: Health Colour Consistency (and Font Noise)"
tags: [reference, ui]
reference_type: "image-analysis"
source_ref: "IMP-11 (earlier import package)"
date_accessed: "2026-10-24"
---

# Arcane Odyssey: Health Colour Consistency (and Font Noise)

## Metadata
- Category: UI / Consistency / Typography
- Source: Roblox Creator Docs, "UI and UX design" > Conventions/Consistency. Game: https://www.roblox.com/games/3272915504/
- Asset: see images below

![IMP-11_arcane-odyssey-character](../../Assets/UI/docs/IMP-11_arcane-odyssey-character.jpg)

- Date added: 2026-10-24
- Rating: 3/5
- Confidence: High
- Reference type: Mixed

## Context
A character sheet. On the left are the avatar, name, age, playtime, a Max Health bar and fame. On the right are the level, XP bar and four attributes (Vitality, Magic, Strength, Weapons), each with a colour, a bar, a "+1" button and a description.

## What Works
- **Green always means health or vitality.** That includes the Max Health bar, the Vitality label, its bar and its number. Roblox cites this as the consistency example.
- **Each attribute owns a colour** (green, blue, red, yellow) that's applied to the label, the bar and the value.
- A "???" tab teases locked content, a cheap curiosity hook.
- The XP bar shows "63 / 103", which is a concrete next goal.

## What Does Not Work
- **Four or more typefaces**: a fantasy serif (headers), an italic sans (descriptions), all-caps sans (tabs, renown) and a numeric face. It feels noisy and unplanned.
- **Long italic grey descriptions** on a translucent background are hard to read on a phone.
- A large empty box bottom-right has no purpose.

## Reusable Design Rules
1. Lock a **semantic colour map** early (health, mana, stamina, XP, currency, rarity tiers) and never reuse those colours decoratively.
2. **Limit fonts: at most two families**, with roles set by weight and size.
3. Put descriptions behind a tap or hover on mobile, and show one line by default.

## Original application
A colour map fixed in a ModuleScript (health, stamina, gold, rarity tiers) and enforced by a lint check on UI colours.

## Related
[Typography and Spacing](../Typography-Color-and-Spacing.md) · [UI Design Principles](../../14-Design-Principles/UI-Principles.md) · [UI Anti Patterns](../../12-Anti-Patterns-and-Design-Critique/Anti-Pattern-Catalog.md)
