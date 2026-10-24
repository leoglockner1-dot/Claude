---
title: "UI-26 — 'Core-like' minimal UI: Pls Donate shop and Color Place palette (DevForum)"
tags: [reference, ui, minimal]
reference_type: "DevForum screenshots of two live games + technique explanation (Positive)"
date_accessed: "2026-10-24"
---

# UI-26 — "Core-like" minimal UI: Pls Donate shop and Color Place palette (DevForum)

## Identity
- **Name:** UI-26 — "Core-like" minimal UI: Pls Donate shop and Color Place palette (DevForum)
- **Reference type:** DevForum screenshots of two live games + technique explanation (Positive)
- **Source URL:** <https://devforum.roblox.com/t/how-would-i-make-ui-like-in-pls-donate-or-color-place-simple-modern-core-like-ui/2852902>
- **Creator/publisher:** Thread by Danielhoteaale; explanation and captures by Reditect
- **Date posted / accessed:** 2024-02-25 / 2026-10-24
- **Access limitations:** Screenshots posted by the author; the live game was not played.

![df-2852902-r2-1dc42d620e7e102-2-345.jpg](../../Assets/UI/devforum/df-2852902-r2-1dc42d620e7e102-2-345.jpg)
![df-2852902-r4-27df482b29124008-2-30.jpg](../../Assets/UI/devforum/df-2852902-r4-27df482b29124008-2-30.jpg)

## What is observable
**Pls Donate (video frames posted by Reditect):** red-header "GAME SHOP" with a VIP subscription card (orange gradient, "SUBSCRIBE $2.99", benefit list) and a grid of item cards with price chips. **Color Place:** dark-grey pill UI — coordinates "(26, 35)", author name and "4 hours" top-left; "get more +" green pill and "2 places / next place in 0:03" timer on the right; a 2-column grid of colour circles; small icon column; a large blue "place" button bottom-left.

## Community critique (quoted/paraphrased from the thread)
- "Pls Donate does a great job of using MouseEnter and MouseLeave events in combination with TweenService. The Color3, Size, and Position of buttons, images, and text change based on those events." (Reditect)
- "Color Place … uses gray often … Text is a light gray and backgrounds are dark gray. More important/eye-catching elements … closer to white" (Reditect)

## What works
- Color Place: **the content is the colour palette**; UI chrome recedes into greys; the only saturated elements are the colours themselves and the action.
- Pls Donate: hover tweens on Size/Color/Position give responsiveness (explained in thread).

## Why it might work
Neutral chrome lets content carry colour (NN/g hierarchy via colour contrast). Hover/press motion confirms interactivity.

## What does not work
Pls Donate's shop mixes many saturated cards — busy, though typical for monetization screens.

## Reusable principles
- **UI-003** Neutral chrome, saturated content; **FEEL-007** every interactive element responds to hover/press within 0.1 s.

## Roblox implementation
Per the thread: `MouseEnter`/`MouseLeave` + `TweenService` on `Size`, `BackgroundColor3`; `UICorner`; text light grey on dark grey, important items closer to white.

## Original application
A photo-mode tool whose UI is entirely dark grey pills, so the player's screenshot is the only colourful thing on screen.

## Confidence
Medium (screenshots via the thread; games not played).

## Related
[Typography Color and Spacing](../Typography-Color-and-Spacing.md) · [R12 Reusable Button Animation System](../../13-Reusable-Design-Recipes/R12-Reusable-Button-Animation-System.md)
