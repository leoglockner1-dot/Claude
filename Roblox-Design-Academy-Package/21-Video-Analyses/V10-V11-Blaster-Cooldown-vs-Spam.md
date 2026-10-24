---
title: "V10/V11 — Blaster with state cooldown vs no cooldown"
tags: [video, reference, game-feel, vfx, combat]
reference_type: "video"
date_accessed: "2026-10-24"
---

# V10/V11 — Blaster with state cooldown vs no cooldown

## Identity
- **Name:** V10/V11 — Blaster with state cooldown vs no cooldown
- **Reference type:** Video (official Roblox Creator Docs recording)
- **Source page:** https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/implement-blasters
- Local clip: [V10-blaster-with-cooldown.mp4](../Assets/Animation-VFX/clips/V10-blaster-with-cooldown.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/tutorials/gameplay-scripting/Blaster-Behavior/Normal-BlastState.mp4>
- Local clip: [V11-blaster-no-cooldown.mp4](../Assets/Animation-VFX/clips/V11-blaster-no-cooldown.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/tutorials/gameplay-scripting/Blaster-Behavior/Custom-BlastState.mp4>
- **Creator/publisher:** Roblox Corporation (CC BY 4.0)
- **Date accessed:** 2026-10-24
- **How it was analysed:** 12 sampled frames + per-frame motion energy (20 fps) + audio RMS envelope, onset detection and spectral centroid (16 kHz mono), plus targeted frame crops where noted. **Audio was measured as waveform data, not listened to.**

![V10-blaster-with-cooldown analysis sheet](../Assets/Animation-VFX/video-sheets/V10-blaster-with-cooldown-sheet.jpg)
![V11-blaster-no-cooldown analysis sheet](../Assets/Animation-VFX/video-sheets/V11-blaster-no-cooldown-sheet.jpg)

*Sheet legend: blue = motion energy over time, orange = audio RMS, white lines = detected audio onsets, numbers = seconds.*

## What is observable
First-person laser blaster in the Laser Tag reference game; objective banner on top ("Tag opposing players to score points! First team to 3 points wins"), team score top-right.
- **V10 (Ready/Blasting/Disabled states):** discrete muzzle flashes at ≈0.15, 0.70, 1.40, 1.95, 2.55 s → **~0.6 s cadence** while clicking; red beam to the wall each time.
- **V11 (state check always true):** muzzle ring glow is **continuous**; motion energy stays high throughout — individual shots are no longer distinguishable.

## What works
The cooldown gives each shot a beginning and end, so flash, beam and sound read as one event each.

## Why it might work
Docs: "This slight pause prevents you from being able to blast as quickly as you can click." Readability of feedback depends on spacing events in time (general game-feel knowledge).

## What does not work / trade-offs
A fixed 0.6 s cadence may feel slow for some weapon fantasies; the right value is weapon-specific.

## Reusable principles
- **FEEL-004** Space repeated feedback so each instance is readable; rate limits are part of game feel, not just balance.

## Roblox implementation
Model weapon state as an enum (Ready → Blasting → Ready / Disabled); gate input client-side for feel and re-check server-side for fairness.

## Original application
A snowball fight where throwing has a 0.4 s wind-up arc and a visible "reload" puff, so spam is impossible and each hit lands as a moment.

## Confidence
High (measured).

## Limitations
Very short clips; recoil, sound design not isolated.

## Related
[Feedback Arc and Impact](../08-Animation-and-Game-Feel/Feedback-Arc-and-Impact.md)
