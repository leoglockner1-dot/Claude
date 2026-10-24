---
title: "UI-23 — User-themeable editor UI built with the Style Editor (DevForum)"
tags: [reference, ui, technical]
reference_type: "DevForum UI screenshots + critique (Mixed-positive)"
date_accessed: "2026-10-24"
---

# UI-23 — User-themeable editor UI built with the Style Editor (DevForum)

## Identity
- **Name:** UI-23 — User-themeable editor UI built with the Style Editor (DevForum)
- **Reference type:** DevForum UI screenshots + critique (Mixed-positive)
- **Source URL:** <https://devforum.roblox.com/t/customizable-ui-showcase/4853181>
- **Creator/publisher:** DevForum user Nocturnalyse
- **Date posted / accessed:** 2026-09-05 / 2026-10-24
- **Access limitations:** Screenshots posted by the author; the live game was not played.

![df-4853181-00.jpg](../../Assets/UI/devforum/df-4853181-00.jpg)
![df-4853181-01.jpg](../../Assets/UI/devforum/df-4853181-01.jpg)
![df-4853181-07.jpg](../../Assets/UI/devforum/df-4853181-07.jpg)

## What is observable
An accessory editor: right panels "Adjust" (X/Y/Z, grid snap) and "Accessory Type" list, left vertical icon toolbar, top "Publish" + "?" buttons. The same layout shown in purple/pink, dark navy and gold themes — the player chooses primary/secondary colours ("thanks to the Roblox UI Styler").

## Community critique (quoted/paraphrased from the thread)
- "use consistent padding everywhere … look at your whole UI … the distance between edge and what's inside, it's different everywhere" (koeqaife)
- "if you're using icons from different packs, … find a good pack with all icons you need so you have same style and same size of icons" (koeqaife)

## What works
- Theme tokens make the whole UI recolourable — a real use of Roblox's Style Editor.
- Tool layout follows creative-software conventions (toolbar left, properties right).

## Why it might work
Tokens enforce consistency automatically.

## What does not work
- Inconsistent padding between panels (reply).
- Icons from multiple packs → different stroke weights/sizes (reply).
- "Secondary colour changes the UI way more than primary" — token roles mis-assigned (reply).

## Reusable principles
- **UI-004** One padding scale everywhere; **UI-006** one icon family; **TECH-004** use Style Editor tokens for colour roles.

## Roblox implementation
Style Editor: tokens (`$Primary`, `$Surface`, `$Accent`), `StyleRule`s per component class, and `StyleQuery` per `ViewportDisplaySize`.

## Original application
A music-maker game offering three themes (Day, Night, Neon) built on the same tokens; accessibility theme with higher contrast.

## Confidence
High.

## Related
[UI Layout and Scaling](../../11-Roblox-Technical-Reference/UI-Layout-and-Scaling.md) · [Typography Color and Spacing](../Typography-Color-and-Spacing.md)
