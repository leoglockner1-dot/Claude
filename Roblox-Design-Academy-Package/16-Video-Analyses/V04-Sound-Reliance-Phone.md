---
title: "V04 — Sound-only vs sound + visual cue (ringing phone)"
tags: [video, reference, audio, accessibility]
reference_type: "video"
date_accessed: "2026-10-24"
---

# V04 — Sound-only vs sound + visual cue (ringing phone)

## Identity
- **Name:** V04 — Sound-only vs sound + visual cue (ringing phone)
- **Reference type:** Video (official Roblox Creator Docs recording)
- **Source page:** https://create.roblox.com/docs/production/publishing/accessibility (Sound non-reliance)
- Local clip: [V04-sound-reliance-phone.mp4](../Assets/Animation-VFX/clips/V04-sound-reliance-phone.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/publishing/accessibility/Sound-Reliance.mp4>
- **Creator/publisher:** Roblox Corporation (CC BY 4.0)
- **Date accessed:** 2026-10-24
- **How it was analysed:** 12 sampled frames + per-frame motion energy (20 fps) + audio RMS envelope, onset detection and spectral centroid (16 kHz mono), plus targeted frame crops where noted. **Audio was measured as waveform data, not listened to.**

![V04-sound-reliance-phone analysis sheet](../Assets/Animation-VFX/video-sheets/V04-sound-reliance-phone-sheet.jpg)

*Sheet legend: blue = motion energy over time, orange = audio RMS, white lines = detected audio onsets, numbers = seconds.*

## What is observable
Same scene twice (45 s). Label "Sound Only" (0–28 s), then "Sound + Visual Aids" (28–45 s).
- Measured audio onsets: **12.4, 15.2, 18.0 s** (first half) and **31.0, 33.8, 36.55 s** (second half) — identical ring bursts (~0.7 s each, spectral centroid ≈1.06 kHz, peak −20.7 dBFS), ~2.8 s apart. Silence between rings (no ambient bed).
- First half: **no visual change at all** (motion energy flat) and the character does not react.
- Second half: a green light pulses on the ringing payphone (31.9 s); the character walks to it (motion burst 35.2–36.05 s); a higher-centroid click at 38.75 s (≈2.9 kHz) when it is answered; the booth light turns pink.

## What works
- The visual cue sits **on the source object** (the phone), not in a HUD popup — it tells *where* as well as *that*.
- The audio is unchanged, so the video isolates the value of the visual aid.

## Why it might work
Players with sound off (common on mobile — inference) or hearing impairment otherwise get no information. Roblox's guidance: never convey events only with sound.

## What does not work / trade-offs
The pulsing light is subtle in a dark blue scene; a brighter or animated cue might be needed in busier scenes.

## Reusable principles
- **AUDIO-004** Every meaningful sound event needs a visual counterpart at the source ([Audio principles](../14-Design-Principles/Audio-Principles.md)).

## Roblox implementation
Pair `Sound:Play()` with a `PointLight`/`Highlight` pulse tween on the emitting part; drive both from the same function so they cannot drift apart.

## Original application
A cooking game: when a dish is done the oven *dings* and its door light blinks and steam puffs — so muted players still notice.

## Confidence
High (measured audio + observed visuals).

## Limitations
Audio not listened to; tone character inferred only from spectral centroid.

## Related
[Sound Design Principles](../06-Sound-Design/Sound-Design-Principles.md) · [Mobile Controller and Accessibility](../01-UI-UX/Mobile-Controller-and-Accessibility.md)
