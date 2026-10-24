---
title: "V19 — Hold-to-interact prompt with progress ring"
tags: [video, reference, ui, interaction, audio]
reference_type: "video"
date_accessed: "2026-10-24"
---

# V19 — Hold-to-interact prompt with progress ring

## Identity
- **Name:** V19 — Hold-to-interact prompt with progress ring
- **Reference type:** Video (official Roblox Creator Docs recording)
- **Source page:** https://create.roblox.com/docs/ui/proximity-prompts (HoldDuration)
- Local clip: [V19-proximity-hold-duration.mp4](../Assets/Animation-VFX/clips/V19-proximity-hold-duration.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/ui/proximity-prompt/HoldDuration.mp4>
- **Creator/publisher:** Roblox Corporation (CC BY 4.0)
- **Date accessed:** 2026-10-24
- **How it was analysed:** 12 sampled frames + per-frame motion energy (20 fps) + audio RMS envelope, onset detection and spectral centroid (16 kHz mono), plus targeted frame crops where noted. **Audio was measured as waveform data, not listened to.**

![V19-proximity-hold-duration analysis sheet](../Assets/Animation-VFX/video-sheets/V19-proximity-hold-duration-sheet.jpg)

*Sheet legend: blue = motion energy over time, orange = audio RMS, white lines = detected audio onsets, numbers = seconds.*

## What is observable
8 s. Torch-lit dungeon door with a prompt panel "[E] Door / Pick Lock". When the hold starts (≈1.6 s) the panel collapses to the key icon with a **circular gauge filling clockwise** until ≈5.0 s (**≈3.3 s hold**). Audio onsets at 2.65 s and 4.1 s (centroid ≈2.0–2.5 kHz, click-like), the door swings open ≈5.4–6.4 s with an onset at 5.4 s.

## What works
- Object name + verb before the hold; during the hold the text disappears and only progress remains.
- Intermittent clicks during the hold make waiting active; completion has its own sound + door motion.

## Why it might work
Holds prevent accidental triggers for consequential actions; progress feedback keeps the 3 s wait tolerable (NN/g: feedback for >1 s waits).

## What does not work / trade-offs
3.3 s is long for a frequent action; no cancel affordance shown.

## Reusable principles
- **UI-013** Long or consequential actions use hold-with-progress; quick, reversible ones fire instantly.

## Roblox implementation
`ProximityPrompt.HoldDuration`, `ObjectText`, `ActionText`; custom styles via `Style = Custom` and `PromptButtonHoldBegan/Ended`.

## Original application
A "Defuse" interaction where each 1 s segment of the ring lights a different wire, with a click per segment.

## Confidence
High.

## Limitations
Audio not listened to.

## Related
[UI 12 Mermaid Life Themed Proximity Prompt](../01-UI-UX/Analyses/UI-12-Mermaid-Life-Themed-Proximity-Prompt.md) · [UI Layout and Scaling](../11-Roblox-Technical-Reference/UI-Layout-and-Scaling.md)
