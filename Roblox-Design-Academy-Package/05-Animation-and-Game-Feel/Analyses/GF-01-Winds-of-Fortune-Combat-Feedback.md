---
title: "Winds of Fortune: Layered Combat Feedback and Quest Waypoint"
tags: [reference, game-feel, vfx]
reference_type: "image-analysis"
source_ref: "IMP-19 (earlier import package)"
date_accessed: "2026-10-24"
---

# Winds of Fortune: Layered Combat Feedback and Quest Waypoint

## Metadata
- Category: Game feel / VFX / HUD
- Source: Roblox Creator Docs, "Onboarding techniques" > Facilitate feedback; Directional arrows
- Asset: see images below

![IMP-19_winds-of-fortune-combat-feedback](../../Assets/Animation-VFX/docs/IMP-19_winds-of-fortune-combat-feedback.jpg)
![IMP-19_winds-of-fortune-waypoint](../../Assets/Gameplay/docs/IMP-19_winds-of-fortune-waypoint.jpg)

- Date added: 2026-10-24
- Rating: 4/5
- Confidence: Medium. Still frames, plus Roblox's own description of the effects. No audio.
- Reference type: Positive

## Context
- Waypoint: a quest tracker top-left ("Marooned – Talk to Captain Edwards") and a green X marker in the world above the NPC.
- Combat: skeletons are being hit at night.

Roblox lists six simultaneous feedback channels:
1. VFX flash on hit
2. red damage numbers
3. a pulsing red screen effect at low HP
4. health bars that update
5. coins flying out on a kill
6. a quest counter that updates ("Kill 15 skeletons (4/15)")

## What Works
- **Each feedback channel answers a different question**: did I hit? (flash), how much? (numbers), am I in danger? (red vignette), what did I get? (coins), am I progressing? (counter). That's layered feedback without duplication.
- The quest tracker and the world marker share the objective, so the HUD and the world agree.

## Reusable Design Rules
1. List the player's questions after an action and give **one feedback channel per question**.
2. Danger feedback (low-HP vignette) must be peripheral, never obscuring the centre.
3. Rewards should **travel** from the source to the HUD counter (coins flying to the balance). That shows where value went.

## Roblox implementation
- Hit flash: `Highlight` with a short FillTransparency tween, or a brief emissive part flash.
- Damage numbers: `BillboardGui`s pooled and recycled.
- Vignette: a full-screen `ImageLabel` whose transparency is driven by HP.
- Coin fly: tween screen-space icons from `Camera:WorldToViewportPoint(enemyPos)` to the counter.

## Original application
A mining game: pickaxe hit sparks (did I hit?), ore chunk counter popping (how much?), cracks spreading (progress?), ore flying to the bag (where did it go?).

## Limitations
No audio heard. Sequence timing and VFX scale weren't measurable.

## Related
[VFX Principles](../VFX-Principles-and-Performance.md) · [Camera and Impact](../Feedback-Arc-and-Impact.md) · [SFX and Audio Feedback](../../06-Sound-Design/Sound-Design-Principles.md) · [HUD Design](../../01-UI-UX/HUD-Layouts.md)
