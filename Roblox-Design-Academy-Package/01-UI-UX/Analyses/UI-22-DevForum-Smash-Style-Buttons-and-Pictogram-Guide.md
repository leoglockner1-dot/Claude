---
title: "UI-22 — Tilted-card buttons and a 3-panel pictogram rule guide (DevForum)"
tags: [reference, ui, onboarding, identity]
reference_type: "DevForum UI screenshots + critique (Positive)"
date_accessed: "2026-10-24"
---

# UI-22 — Tilted-card buttons and a 3-panel pictogram rule guide (DevForum)

## Identity
- **Name:** UI-22 — Tilted-card buttons and a 3-panel pictogram rule guide (DevForum)
- **Reference type:** DevForum UI screenshots + critique (Positive)
- **Source URL:** <https://devforum.roblox.com/t/my-ui-showoff-feedbacks-please/4823740>
- **Creator/publisher:** DevForum user Scrin_bs (same author as UI-15)
- **Date posted / accessed:** 2026-08-21 / 2026-10-24
- **Access limitations:** Screenshots posted by the author; the live game was not played.

![df-4823740-00.jpg](../../Assets/UI/devforum/df-4823740-00.jpg)
![df-4823740-03.jpg](../../Assets/UI/devforum/df-4823740-03.jpg)
![df-4823740-06.jpg](../../Assets/UI/devforum/df-4823740-06.jpg)

## What is observable
Right-edge buttons are **tilted cards** (red "Modes" with a cube icon, yellow "Build" with a hammer) — the author cites Smash Bros-style inspiration. A "TIMER" guide modal explains a mechanic in **three numbered pictogram panels**: (1) stopwatch "05:00 – Timer gives you a time limit…", (2) "05:00 → 04:50" with streak badges "the longer your streak, the more seconds are stolen", (3) red skull "00:00 … you will be DEAD". A "BUILD" modal: big orange "Main Game" card + a locked hazard-striped "???" card.

## Community critique (quoted/paraphrased from the thread)
- "the side buttons, the timer window, and the loading screen are close to perfect" (checcerr). Note: the same designer's earlier shop (UI-15) was criticised as harsh — a visible learning arc.

## What works
- **Mechanic explained with pictures and numbers**, minimal text (same principle as Color or Die, [ONB-02](../../13-Onboarding-and-Multiplayer/Onboarding/Analyses/ONB-02-Color-or-Die-Rules-Sign.md)).
- Distinct, ownable shape motif (tilted cards) applied to multiple buttons.
- Locked content teased with hazard stripes + "???" (curiosity).

## Why it might work
Pictograms survive localisation and young readers (Roblox design-for-roblox: keep UI visual).

## What does not work
Grey panel bodies are dull vs the colourful buttons; body text still small.

## Reusable principles
- **ONB-002** Teach rules as 2–3 picture panels; **ID-002** one geometric motif = identity.

## Roblox implementation
Guide modal as `UIGridLayout` of 3 cards with `ImageLabel` + 1–2 lines; open contextually on first timer start.

## Original application
A cooking-race game explaining "burnt food" with three panels: pan + timer → smoke → black pancake with a frowning face.

## Confidence
High.

## Related
[First Session Design](../../13-Onboarding-and-Multiplayer/Onboarding/First-Session-Design.md) · [Visual Identity Framework](../../11-Visual-Identity/Visual-Identity-Framework.md)
