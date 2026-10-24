---
title: "UI-21 — Over-decorated inventory and genre-template stock panel (DevForum portfolio)"
tags: [reference, ui, anti-pattern]
reference_type: "DevForum UI screenshots + critique (Mixed/Negative)"
date_accessed: "2026-10-24"
---

# UI-21 — Over-decorated inventory and genre-template stock panel (DevForum portfolio)

## Identity
- **Name:** UI-21 — Over-decorated inventory and genre-template stock panel (DevForum portfolio)
- **Reference type:** DevForum UI screenshots + critique (Mixed/Negative)
- **Source URL:** <https://devforum.roblox.com/t/rate-feedback-on-my-ui/4702783>
- **Creator/publisher:** DevForum user (GFX artist moving to UI)
- **Date posted / accessed:** 2026-06-25 / 2026-10-24
- **Access limitations:** Screenshots posted by the author; the live game was not played.

![df-4702783-00.jpg](../../Assets/UI/devforum/df-4702783-00.jpg)
![df-4702783-03.jpg](../../Assets/UI/devforum/df-4702783-03.jpg)
![df-4702783-06.jpg](../../Assets/UI/devforum/df-4702783-06.jpg)

## What is observable
(1) "Anime HUD": dark, small roleplay nameplates, five dark hotbar slots — text unreadable at full HD. (2) "Grow a Garden type UI": wood-texture stock panel "New Stock in 15s / RESTOCK", top tabs SHOP (orange) / BASE (wood) / SELL (blue), left buttons SHOP / GUIDE / Storage in red/green/yellow. (3) Inventory framed by **ornate red dragon sculptures**. Heavy diagonal watermark across all images.

## Community critique (quoted/paraphrased from the thread)
- "the amount of watermarking is insane" (JAC_kko)
- "The layout in the first image looks good, but the style is rather too complicated … The dragons in the third image are a bit too…" (mechclash)

## What works
- The garden-style panel is readable and matches its genre's expectations.

## Why it might work
Genre familiarity reduces learning (Roblox: match genre conventions).

## What does not work
- Dragon ornament frame dominates the content (decoration > information).
- (2) is a recognisable copy of a genre leader's look — usable, but no identity.
- Dark tiny text in (1).

## Reusable principles
- **UI-008** Decoration must never outweigh content; **ID-005** borrow genre grammar, not a competitor's skin.

## Roblox implementation
Use 9-slice frames with thin borders; put ornament only on the header; test legibility at 1280×720 and phone size.

## Original application
A dragon-themed inventory where the theme lives in icon style and a small scale-pattern header, not in a full sculpted frame.

## Confidence
Medium (portfolio mock-ups, not shipped game).

## Related
[Anti Pattern Catalog](../../15-Anti-Patterns-and-Failure-Cases/Anti-Pattern-Catalog.md)
