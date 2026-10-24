---
title: "UI-25 — UI judged 'AI-generated looking' by players (Roll a Cupcake, DevForum)"
tags: [reference, ui, anti-pattern, ai-look]
reference_type: "DevForum in-game screenshots + critique (Negative)"
date_accessed: "2026-10-24"
---

# UI-25 — UI judged "AI-generated looking" by players (Roll a Cupcake, DevForum)

## Identity
- **Name:** UI-25 — UI judged "AI-generated looking" by players (Roll a Cupcake, DevForum)
- **Reference type:** DevForum in-game screenshots + critique (Negative)
- **Source URL:** <https://devforum.roblox.com/t/how-can-i-get-players-to-understand-my-game/4761565>
- **Creator/publisher:** Developer UsePoison; screenshots by reviewers
- **Date posted / accessed:** 2026-07-28 / 2026-10-24
- **Access limitations:** Screenshots posted by the author; the live game was not played.

![df-4761565-r2-982e2de8906878453fe05.jpg](../../Assets/UI/devforum/df-4761565-r2-982e2de8906878453fe05.jpg)
![df-4761565-r2-60a672f9c62ebc24697de.jpg](../../Assets/UI/devforum/df-4761565-r2-60a672f9c62ebc24697de.jpg)
![df-4761565-r3-f4feca052a1d966-2-378.jpg](../../Assets/UI/devforum/df-4761565-r3-f4feca052a1d966-2-378.jpg)

## What is observable
A huge orange "SPIN" button with a thick dark stroke; "69 coins" in yellow outlined text on a dark pill; an item row "Silver Cupcake · Lv1 · Epic | +25 c/tick | EQUIPPED | Slot 10" with green SLOT 10 and purple MOVE buttons; an inventory panel with tiny rarity filter chips; a tutorial chip "Tutorial – Step 1/4 · Click the SPIN button" small in the top-left.

## Community critique (quoted/paraphrased from the thread)
- "the text mixing with the strokes hurts my head … I would make the arrows during the tutorial a bit bigger, because it took me a second to find them." (asher_dz)
- "it looks a bit ai generated … it 100% is, no doubt." (INBOUNDNUKE)
- Developer: "I really do agree with the GUIs looking sort of AI-like … I will edit [the] cluttered UI strokes" (UsePoison)

## What works
- The primary action (SPIN) is huge and unmistakable.

## Why it might work
—

## What does not work
- **Uniform heavy strokes on every text** ("the text mixing with the strokes hurts my head").
- Generic saturated buttons with identical glossy treatment; tiny metadata line with pipes; tutorial chip too small; inventory showed outdated coins-per-tick (data mismatch).
- Players described it as AI-generated looking — the developer agreed and planned a full overhaul. Gameplay context: players "walk around aimlessly and leave despite the tutorial".

## Reusable principles
- **UI-007** Strokes are for legibility over busy backgrounds, not a default on every text; **UI-017** tutorial prompts must be as prominent as the action they teach. See [AI/template look detection](../../15-Anti-Patterns-and-Failure-Cases/AI-and-Template-Look-Detection.md).

## Roblox implementation
`UIStroke` only on text over the 3D world; panel text without stroke; tutorial step as a large callout anchored to the target with an arrow.

## Original application
A dessert-shop UI with cream panels and chocolate-brown text without strokes; only the floating "+coins" world text gets an outline.

## Confidence
High (community + developer agreement).

## Related
[AI and Template Look Detection](../../15-Anti-Patterns-and-Failure-Cases/AI-and-Template-Look-Detection.md) · [First Session Design](../../13-Onboarding-and-Multiplayer/Onboarding/First-Session-Design.md)
