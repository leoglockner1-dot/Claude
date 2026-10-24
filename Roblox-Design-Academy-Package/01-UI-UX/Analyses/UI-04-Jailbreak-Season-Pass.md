---
title: "Jailbreak: Season Pass Free vs Premium Track"
tags: [reference, ui]
reference_type: "image-analysis"
source_ref: "IMP-04 (earlier import package)"
date_accessed: "2026-10-24"
---

# Jailbreak: Season Pass Free vs Premium Track

## Metadata
- Category: UI / Progression and rewards / Shops
- Source: Roblox Creator Docs, "UI and UX design" > Attention. Game: https://www.roblox.com/games/606849621/
- Asset: see images below

![IMP-04_jailbreak-season-pass](../../Assets/UI/docs/IMP-04_jailbreak-season-pass.jpg)

- Date added: 2026-10-24
- Rating: 3.5/5. The structure is excellent and the typography is weak.
- Confidence: Medium. The screenshot was taken at season end ("0s", "Coming soon").
- Reference type: Mixed

## Context
A ten-tier season track. Free rewards hang **above** a black numbered timeline. Premium "Season pass exclusives!" sit **below** it on a gold-orange stripe. Purchase and gift actions are at the bottom.

## What Works
- **A colour band splits free and paid.** Roblox's own reading is that "a stripe of golden yellow lies beneath the season pass-exclusive icons". You can tell which rewards are premium without reading anything.
- **The numbered timeline as a spine** makes progress spatial (left = earned, right = upcoming).
- **The timer is in a fixed corner** (top-right, "Season ends in"), which creates urgency without a popup.
- **Gifting is built in.** This is a social purchase path, which suits Roblox's friend-driven audience.

## What Does Not Work
- **Everything is the same heavy, outlined, all-caps display font**: title, subtitle, CTA, gift row, tier numbers. With every label shouting, nothing stands out. Hierarchy here comes only from size.
- **Reward icons are small, and every one carries a tiny corner badge.** At phone size the badges become noise.
- A contradictory state is visible: "Season ends in 0s" next to "Coming soon".
- An orphan red dot sits top-left.

## Visual Analysis
- Colour: sky-blue panel, orange for premium and calls to action, magenta item backgrounds. Orange does double duty (premium stripe and CTA). That's consistent, but it weakens the CTA.
- Typography: a single display face for all roles. See the anti-pattern below.

## Reusable Design Rules
1. Separate free and paid tracks **spatially** (above and below) **and** with colour.
2. Draw progress as a physical line that fills. Players read where they are faster than a "Tier 6/10" label.
3. Use at most two type roles: display for titles and numbers, a readable sans for everything else.
4. Every reward cell must survive a 50% downscale. Test it on a phone.

## Anti-Patterns
- **All-caps display font everywhere.** It works for 1–3 words of title. For sentences ("THANKS FOR PLAYING! THE NEXT SEASON IS COMING SOON!") it slows reading and flattens hierarchy.
- Don't show stale or impossible states (0 s + coming soon). Hide or replace the section.

## Roblox implementation
Build a horizontal `ScrollingFrame` with `UIListLayout`. Each tier is a fixed-width column with free cell, number node and premium cell. Tween the progress line's `Size.X.Scale`. For the premium stripe, use a single tinted `Frame` behind the row, not per-item gradients.

## Original application
A fishing season track drawn as a river with free rewards on the bank and premium rewards on a golden boat lane.

## Limitations
The claim/unlock animation, sound and the in-season state were not visible.

## Related
[Progression and Rewards](../../04-Progression-and-Economy/Progression-Systems.md) · [Shops and Inventory](../Shops-and-Monetization-UI.md) · [Typography and Spacing](../Typography-Color-and-Spacing.md) · [UI Anti Patterns](../../12-Anti-Patterns-and-Design-Critique/Anti-Pattern-Catalog.md)
