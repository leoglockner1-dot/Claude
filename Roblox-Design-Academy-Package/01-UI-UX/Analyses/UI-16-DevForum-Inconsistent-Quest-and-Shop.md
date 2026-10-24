---
title: "UI-16 — Quest panel and shop that look like two different games (DevForum)"
tags: [reference, ui, consistency]
reference_type: "DevForum UI screenshots + critique (Mixed)"
date_accessed: "2026-10-24"
---

# UI-16 — Quest panel and shop that look like two different games (DevForum)

## Identity
- **Name:** UI-16 — Quest panel and shop that look like two different games (DevForum)
- **Reference type:** DevForum UI screenshots + critique (Mixed)
- **Source URL:** <https://devforum.roblox.com/t/what-makes-a-gui-high-quality-looking-for-feedback/4700580>
- **Creator/publisher:** DevForum user Count_Doggo
- **Date posted / accessed:** 2026-06-24 / 2026-10-24
- **Access limitations:** Screenshots posted by the author; the live game was not played.

![df-4700580-00.jpg](../../Assets/UI/devforum/df-4700580-00.jpg)
![df-4700580-03.jpg](../../Assets/UI/devforum/df-4700580-03.jpg)
![df-4700580-06.jpg](../../Assets/UI/devforum/df-4700580-06.jpg)

## What is observable
Old version: flat blue quest panel with green progress bars; currency "2,130 G" in a serif font bottom-left. New quest panel: white card with navy header, red X, green progress bar ("Collect 5 normal chicken eggs 2/5"). New "Chicken Shop": orange wooden header, blue body, white item cards, a green "Buy: 25G" and a blue "Buy: 7 R$" button per item.

## Community critique (quoted/paraphrased from the thread)
- "The shop and quest UIs are very different from each other, and don't really look like they're from the same game … get a consistent look going for the entire game (same fonts, colors…)" (supernovasalmon)
- "maintaining consistency throughout the styling … if it actually fits the theme … 'less is more'" (adrriannm)
- "use the same structure everywhere (as long as it makes sense)" (mechclash)

## What works
- Shop items: picture + name + flavour line + stats + two clearly separated buy paths (soft vs Robux colours).
- Quest card is clean and readable.

## Why it might work
Separate colours for soft and premium currency prevent mistakes.

## What does not work
- Quest UI (flat modern card) and shop UI (wood/cartoon) share **no fonts, colours or shapes** → the game feels assembled from parts.
- Old version's currency font differs from everything else.

## Reusable principles
- **UI-005** One visual system across all screens; decide style before building screens ([UI Principles](../../14-Design-Principles/UI-Principles.md)).

## Roblox implementation
Create a single `StyleSheet` with tokens and derive every panel from one panel component (header, body, close button) — change it once, update everywhere.

## Original application
A farm game: decide "hand-painted wooden signage" once; quests become pinned notes on the same wood board style as the shop.

## Confidence
High.

## Related
[UI UX Overview](../UI-UX-Overview.md) · [Visual Identity Framework](../../07-Visual-Identity/Visual-Identity-Framework.md)
