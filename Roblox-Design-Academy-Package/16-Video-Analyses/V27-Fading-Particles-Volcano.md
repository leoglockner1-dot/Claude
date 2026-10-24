---
title: "V27 — Particles that fade over lifetime"
tags: [video, reference, vfx, environment]
reference_type: "video"
date_accessed: "2026-10-24"
---

# V27 — Particles that fade over lifetime

## Identity
- **Name:** V27 — Particles that fade over lifetime
- **Reference type:** Video (official Roblox Creator Docs recording)
- **Source page:** https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/custom-particle-effects
- Local clip: [V27-fading-particles-volcano.mp4](../Assets/Animation-VFX/clips/V27-fading-particles-volcano.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/tutorials/custom-particle-effects/fadingParticles.mp4>
- **Creator/publisher:** Roblox Corporation (CC BY 4.0)
- **Date accessed:** 2026-10-24
- **How it was analysed:** 12 sampled frames + per-frame motion energy (20 fps) + audio RMS envelope, onset detection and spectral centroid (16 kHz mono), plus targeted frame crops where noted. **Audio was measured as waveform data, not listened to.**

![V27-fading-particles-volcano analysis sheet](../Assets/Animation-VFX/video-sheets/V27-fading-particles-volcano-sheet.jpg)

*Sheet legend: blue = motion energy over time, orange = audio RMS, white lines = detected audio onsets, numbers = seconds.*

## What is observable
6.7 s. Continuous white smoke puffs rise from an orange lava vent and fade out as they rise (transparency over lifetime); emission is steady (periodic motion energy).

## What works
No particle pops out abruptly; warm lava vs white smoke gives clear figure-ground.

## Why it might work
Gradual fade avoids distracting pop-in/out; ambient effects should not demand attention.

## What does not work / trade-offs
Many overlapping semi-transparent puffs = overdraw cost (Roblox performance docs); keep counts low on mobile.

## Reusable principles
- **FEEL-009** Ambient effects fade in/out over lifetime and stay low-contrast so gameplay effects remain dominant.

## Roblox implementation
`ParticleEmitter.Transparency` NumberSequence 0.3→1, `Size` growing, `Rate` minimal (mobile cap 100/s per emitter).

## Original application
Pollen drifting in a meadow level that fades in near the player and out at distance.

## Confidence
High.

## Limitations
No audio.

## Related
[VFX Principles and Performance](../05-Animation-and-Game-Feel/VFX-Principles-and-Performance.md)
