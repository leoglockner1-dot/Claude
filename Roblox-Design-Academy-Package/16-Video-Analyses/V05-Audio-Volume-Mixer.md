---
title: "V05 — Separate SFX and music sliders in a noisy hazard game"
tags: [video, reference, audio, accessibility, ui]
reference_type: "video"
date_accessed: "2026-10-24"
---

# V05 — Separate SFX and music sliders in a noisy hazard game

## Identity
- **Name:** V05 — Separate SFX and music sliders in a noisy hazard game
- **Reference type:** Video (official Roblox Creator Docs recording)
- **Source page:** https://create.roblox.com/docs/production/publishing/accessibility (Volume controls)
- Local clip: [V05-audio-volume-mixer.mp4](../Assets/Animation-VFX/clips/V05-audio-volume-mixer.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/publishing/accessibility/Audio-Volume.mp4>
- **Creator/publisher:** Roblox Corporation (CC BY 4.0)
- **Date accessed:** 2026-10-24
- **How it was analysed:** 12 sampled frames + per-frame motion energy (20 fps) + audio RMS envelope, onset detection and spectral centroid (16 kHz mono), plus targeted frame crops where noted. **Audio was measured as waveform data, not listened to.**

![V05-audio-volume-mixer analysis sheet](../Assets/Animation-VFX/video-sheets/V05-audio-volume-mixer-sheet.jpg)

*Sheet legend: blue = motion energy over time, orange = audio RMS, white lines = detected audio onsets, numbers = seconds.*

## What is observable
41 s. A grid of red tiles; falling fireballs with particle trails crack tiles (white glow) which then turn black and drop. Audio RMS spikes with every impact (onsets cluster 8–21 s). At ≈22 s a compact mixer appears: **red explosion icon + slider (SFX)** above **blue music-note icon + slider (music)**. At ≈25 s the SFX slider is lowered, at ≈29 s the music slider; the RMS envelope drops correspondingly (late section near silent).

## What works
- Two channels, each identified by **icon and colour**, no text needed.
- The panel is small and overlays a corner of the action (game remains visible).

## Why it might work
Different players want different balances; separating channels lets them silence repetitive impacts without losing music (or vice versa). Roblox lists this under accessibility.

## What does not work / trade-offs
The slider thumbs are diamond shapes without numeric values; precise settings are hard to repeat.

## Reusable principles
- **AUDIO-005** Provide at least separate SFX / Music volume groups exposed in settings.

## Roblox implementation
Route sounds through separate mixing groups (Roblox now recommends the audio-objects API — `AudioFader`/bus style mixing — over the discouraged `SoundGroup`; verify current API in [Audio API notes](../11-Roblox-Technical-Reference/Audio-and-Sound-APIs.md)). Persist values with `DataStoreService` or player attributes.

## Original application
A rhythm-obby where the settings gear opens a 3-row mixer (Music / Effects / Voice) with large icons and percentage labels.

## Confidence
High.

## Limitations
Waveform-only audio analysis.

## Related
[Sound Design Principles](../06-Sound-Design/Sound-Design-Principles.md) · [Audio and Sound APIs](../11-Roblox-Technical-Reference/Audio-and-Sound-APIs.md)
