---
title: "V13 — Health pickup with semantic particles"
tags: [video, reference, vfx, pickups]
reference_type: "video"
date_accessed: "2026-10-24"
---

# V13 — Health pickup with semantic particles

## Identity
- **Name:** V13 — Health pickup with semantic particles
- **Reference type:** Video (official Roblox Creator Docs recording)
- **Source page:** https://create.roblox.com/docs/tutorials/use-case-tutorials/scripting/intermediate-scripting/create-a-health-pickup
- Local clip: [V13-health-pickup.mp4](../Assets/Animation-VFX/clips/V13-health-pickup.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/tutorials/creating-a-health-pickup/fullHealthPickupEffect.mp4>
- **Creator/publisher:** Roblox Corporation (CC BY 4.0)
- **Date accessed:** 2026-10-24
- **How it was analysed:** 12 sampled frames + per-frame motion energy (20 fps) + audio RMS envelope, onset detection and spectral centroid (16 kHz mono), plus targeted frame crops where noted. **Audio was measured as waveform data, not listened to.**

![V13-health-pickup analysis sheet](../Assets/Animation-VFX/video-sheets/V13-health-pickup-sheet.jpg)

*Sheet legend: blue = motion energy over time, orange = audio RMS, white lines = detected audio onsets, numbers = seconds.*

## What is observable
16.6 s, silent track. A soft white light column marks the pickup pad from a distance. Walking in (≈4.5–5.2 s) triggers **green "+" shaped particles** rising around the avatar (≈6.2–9.0 s); the pad's glow dims afterwards (cooldown state). Health bar (top-right) fills. At 11.8 s a red full-screen tint signals damage taken elsewhere.

## What works
- The particle **shape carries meaning** (plus = health) instead of generic sparkles.
- The beacon is readable from across the street (landmark function).
- The pad shows its cooldown by dimming — state visible in the world.

## Why it might work
Semantic shapes are understood without text; consistent colour (green = health) matches HUD conventions (see [UI-11 Arcane Odyssey](../01-UI-UX/Analyses/UI-11-Arcane-Odyssey-Health-Colour.md)).

## What does not work / trade-offs
No pickup sound in this recording; particles last ~3 s, which would be long for a frequent pickup.

## Reusable principles
- **FEEL-005** Particle shapes and colours should encode the effect's meaning ([Game-feel principles](../17-Design-Principles/Game-Feel-Principles.md)).

## Roblox implementation
`ParticleEmitter` with a "+" texture, `Emit(15)` on touch, `Lifetime` 0.6–1.0, `LightEmission` low; `PointLight` on pad tweened to 0 during cooldown.

## Original application
A mana fountain that emits small blue droplet-shaped particles toward the player and visibly lowers its water level until it refills.

## Confidence
High for visuals; no audio present.

## Limitations
Silent recording.

## Related
[VFX Principles and Performance](../09-VFX/VFX-Principles-and-Performance.md)
