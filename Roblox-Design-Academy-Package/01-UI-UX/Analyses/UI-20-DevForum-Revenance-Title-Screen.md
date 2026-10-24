---
title: "UI-20 — Minimal title screen with tone mismatch (Revenance, DevForum)"
tags: [reference, ui, menus]
reference_type: "DevForum UI screenshots + critique (Mixed)"
date_accessed: "2026-10-24"
---

# UI-20 — Minimal title screen with tone mismatch (Revenance, DevForum)

## Identity
- **Name:** UI-20 — Minimal title screen with tone mismatch (Revenance, DevForum)
- **Reference type:** DevForum UI screenshots + critique (Mixed)
- **Source URL:** <https://devforum.roblox.com/t/feedback-on-my-ui-design-for-my-friends-game-title-screen/4684927>
- **Creator/publisher:** DevForum user (author of thread 4684927)
- **Date posted / accessed:** 2026-06-16 / 2026-10-24
- **Access limitations:** Screenshots posted by the author; the live game was not played.

![df-4684927-00.jpg](../../Assets/UI/devforum/df-4684927-00.jpg)
![df-4684927-03.jpg](../../Assets/UI/devforum/df-4684927-03.jpg)
![df-4684927-06.jpg](../../Assets/UI/devforum/df-4684927-06.jpg)

## What is observable
Title screen: left-aligned "REVENANCE" wordmark with bracket corners, menu items (Singleplayer, Settings, Collection, Credits) each with a thin slanted underline; dark night street behind. Save-file modal: glassy teal sci-fi panels, three identical "Start a New Save" buttons. Save details: many fields showing "NULL", bottom row "< Back · Delete · Start >".

## Community critique (quoted/paraphrased from the thread)
- "the main menu background is a bit too dark … idk what genre your game is, it looks like horror…? The UI in the other screenshots look a bit sci-fi, also the font can be a bit better" (Ashlee_IsTyping)

## What works
- Restrained, consistent teal system in the modals.
- Left-aligned menu leaves the scene visible (mood).

## Why it might work
Minimal menus keep atmosphere and reduce noise.

## What does not work
- Tone mismatch: dark horror street vs bright teal sci-fi panels (reply: "genre unclear").
- **Delete sits next to Start with equal weight** — destructive action not differentiated.
- Placeholder "NULL" values visible; low-contrast small text.

## Reusable principles
- **UI-011** Destructive actions must look different and ask for confirmation; **ID-003** UI style should come from the world's genre.

## Roblox implementation
Confirm dialog for Delete; red/outlined style; keep destructive buttons apart from the primary; hide empty fields.

## Original application
A post-apocalyptic save screen using worn paper ID cards; deleting a save means "tearing" a card with a hold-to-confirm.

## Confidence
High for observations.

## Related
[Menus and Navigation](../Menus-and-Navigation.md) · [Visual Identity Framework](../../07-Visual-Identity/Visual-Identity-Framework.md)
