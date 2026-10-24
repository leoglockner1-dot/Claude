---
title: "V23/V24 — Same visuals with and without audio (stretching pantry)"
tags: [video, reference, audio, level-design, horror]
reference_type: "video"
date_accessed: "2026-10-24"
---

# V23/V24 — Same visuals with and without audio (stretching pantry)

## Identity
- **Name:** V23/V24 — Same visuals with and without audio (stretching pantry)
- **Reference type:** Video (official Roblox Creator Docs recording)
- **Source page:** https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/develop-a-moving-world
- Local clip: [V23-duvall-pantry-with-sound.mp4](../Assets/Animation-VFX/clips/V23-duvall-pantry-with-sound.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/resources/mystery-of-duvall-drive/developing-a-moving-world/pantry-movement.mp4>
- Local clip: [V24-duvall-pantry-silent.mp4](../Assets/Animation-VFX/clips/V24-duvall-pantry-silent.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/resources/mystery-of-duvall-drive/developing-a-moving-world/pantry-movement-silent.mp4>
- **Creator/publisher:** Roblox Corporation (CC BY 4.0)
- **Date accessed:** 2026-10-24
- **How it was analysed:** 12 sampled frames + per-frame motion energy (20 fps) + audio RMS envelope, onset detection and spectral centroid (16 kHz mono), plus targeted frame crops where noted. **Audio was measured as waveform data, not listened to.**

![V23-duvall-pantry-with-sound analysis sheet](../Assets/Animation-VFX/video-sheets/V23-duvall-pantry-with-sound-sheet.jpg)
![V24-duvall-pantry-silent analysis sheet](../Assets/Animation-VFX/video-sheets/V24-duvall-pantry-silent-sheet.jpg)

*Sheet legend: blue = motion energy over time, orange = audio RMS, white lines = detected audio onsets, numbers = seconds.*

## What is observable
11.6 s each, identical visuals: the player walks toward a lit pantry end while the corridor stretches away (motion 2.4–7.8 s); objective text "Items Restored 0/4" bottom-centre. Docs: a nightmare where "no matter how fast you run, the room feels like it keeps getting longer".
**With sound (measured):** level rises from ≈2.9 s, onsets 3.55/3.70 s (centroid ≈1.3–1.5 kHz), then a **sustained bed (median −19.8 dBFS)** to the end. Silent version: no track.

## What works
A controlled A/B: the audio layer starts as the space begins to move and persists, turning a slow visual into sustained tension.

## Why it might work
Continuous low-level sound beds sustain mood where visuals change slowly (general horror sound-design practice).

## What does not work / trade-offs
Cannot judge the actual sound content (not listened).

## Reusable principles
- **AUDIO-006** Use sustained beds for mood, one-shots for events; start the bed with the first visual change.

## Roblox implementation
`Sound` with `Looped=true`, volume tween 0→target over ~0.5 s triggered with the room animation; stop with a fade on completion.

## Original application
An ice cave where a low creaking bed rises as cracks spread on the floor, then drops to silence the instant the player reaches safety.

## Confidence
Medium (audio role inferred from levels and timing).

## Limitations
No listening; one scene.

## Related
[Measured Audio Observations](../06-Sound-Design/Measured-Audio-Observations.md) · [Environmental Communication](../08-Level-Design/Environmental-Communication.md)
