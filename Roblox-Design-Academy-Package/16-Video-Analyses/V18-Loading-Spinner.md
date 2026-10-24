---
title: "V18 — Minimal loading spinner"
tags: [video, reference, ui, loading]
reference_type: "video"
date_accessed: "2026-10-24"
---

# V18 — Minimal loading spinner

## Identity
- **Name:** V18 — Minimal loading spinner
- **Reference type:** Video (official Roblox Creator Docs recording)
- **Source page:** https://create.roblox.com/docs/players/loading-screens (Add animations)
- Local clip: [V18-loading-spinner.mp4](../Assets/Animation-VFX/clips/V18-loading-spinner.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/ui/misc/Loading-Animation.mp4>
- **Creator/publisher:** Roblox Corporation (CC BY 4.0)
- **Date accessed:** 2026-10-24
- **How it was analysed:** 12 sampled frames + per-frame motion energy (20 fps) + audio RMS envelope, onset detection and spectral centroid (16 kHz mono), plus targeted frame crops where noted. **Audio was measured as waveform data, not listened to.**

![V18-loading-spinner analysis sheet](../Assets/Animation-VFX/video-sheets/V18-loading-spinner-sheet.jpg)

*Sheet legend: blue = motion energy over time, orange = audio RMS, white lines = detected audio onsets, numbers = seconds.*

## What is observable
12 s, silent. Navy screen; after ≈0.7 s a thin ring fades in with a lighter arc rotating around a dim track (~1 revolution per ~4 s) and the word "Loading" centred inside. Nothing else changes.

## What works
Calm, cheap, clearly "working"; uses `TweenService` per the docs.

## Why it might work
Indeterminate indicators reassure that the system is alive (NN/g: feedback needed for delays > 1 s; percent-done for > ~10 s).

## What does not work / trade-offs
No progress, no tip, no game identity — for multi-second loads it wastes the most attentive moment of a session.

## Reusable principles
- **UI-015** Loading screens should show identity + progress or a useful tip when waits exceed a few seconds.

## Roblox implementation
`ReplicatedFirst` LocalScript + `ContentProvider:PreloadAsync` with a callback to drive a determinate bar; `RemoveDefaultLoadingScreen()` once your UI is up.

## Original application
A heist game whose loading screen is a safe dial turning per asset batch loaded, with a rotating one-line tip about the current map.

## Confidence
High.

## Limitations
Only the animation was shown, no real load.

## Related
[Loading Death and Round Transitions](../01-UI-UX/Loading-Death-and-Round-Transitions.md)
