---
title: "V01 — Berry Avenue avatar customization flow"
tags: [video, reference, ui, menus]
reference_type: "video"
date_accessed: "2026-10-24"
---

# V01 — Berry Avenue avatar customization flow

## Identity
- **Name:** V01 — Berry Avenue avatar customization flow
- **Reference type:** Video (official Roblox Creator Docs recording)
- **Source page:** https://create.roblox.com/docs/production/game-design/ui-ux-design (Design flows)
- Local clip: [V01-berry-avenue-avatar-flow.mp4](../Assets/Animation-VFX/clips/V01-berry-avenue-avatar-flow.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/game-design/ui-ux-design/ui-ux-design-18-video.mp4>
- **Creator/publisher:** Roblox Corporation (CC BY 4.0)
- **Date accessed:** 2026-10-24
- **How it was analysed:** 12 sampled frames + per-frame motion energy (20 fps) + audio RMS envelope, onset detection and spectral centroid (16 kHz mono), plus targeted frame crops where noted. **Audio was measured as waveform data, not listened to.**

![V01-berry-avenue-avatar-flow analysis sheet](../Assets/Animation-VFX/video-sheets/V01-berry-avenue-avatar-flow-sheet.jpg)

*Sheet legend: blue = motion energy over time, orange = audio RMS, white lines = detected audio onsets, numbers = seconds.*

## What is observable
| Time | Event |
|---|---|
| 0.0–0.3 s | Avatar editor already open: ~half-screen right panel (lavender with yellow frame), icon tabs + search field on top, category row (ALL / HEAD / FACE / NECK / SHOULDER / FRONT) |
| 0.3 s | Grid area shows a 3-dot loading indicator |
| ≈0.9 s | Item grid (5 columns) populated — ~0.6 s load |
| 1.4–1.95 s | Category switch (motion spikes) — grid content swaps |
| ≈2.7 s | Tapped item (glasses) appears on the avatar on the left immediately |
| ≈3.9 s | Panel closes (largest motion spike) — back to world; right-edge vertical stack of small yellow HUD buttons |
The audio track is silent (−180 dBFS).

## What works
- **Live preview on the avatar** next to the grid: selecting = seeing, no confirm step.
- **Two parallel entry paths** (category tabs and search) visible in the same header.
- Closing returns directly to play; HUD reappears in the same place.

## Why it might work
- Roblox's own analysis: low friction comes from few steps and instant preview (see docs text in [UI-14](../01-UI-UX/Analyses/UI-14-Berry-Avenue-Avatar-Flow-Chart.md)). Observed timing supports it: from tap to visible result there is no measurable delay at 20 fps sampling.

## What does not work / trade-offs
- Item tiles are small (5 columns inside half the screen) — on a phone each tile would be roughly thumb-sized at best (inference from proportions; not tested on device).
- Loading the grid takes ~0.6 s with only a dot indicator.
- The DONE button is small and low-contrast relative to the panel (green on lavender).

## Reusable principles
- Preview changes in place, instantly (see **UI-010** in [UI Principles](../17-Design-Principles/UI-Principles.md)).
- Count taps to the goal; offer browse **and** search for large catalogs (**UI-009**).

## Roblox implementation
- Keep the avatar visible in a `ViewportFrame` or the real camera framed left; panel in a `Frame` anchored right with `UIGridLayout`.
- Equip on `Activated` immediately (client-side visual), validate ownership on the server via `RemoteFunction`.
- Pre-load thumbnails for the first category (`ContentProvider:PreloadAsync`) to hide the 0.6 s grid fill.

## Original application
A pet-customization screen where tapping a hat instantly puts it on the pet standing in the world, with a single "Done" thumb button that is the only saturated element on the panel.

## Confidence
High for the sequence and timing (directly measured); Medium for the mobile-size critique (inferred).

## Limitations
Short 7 s clip; the full flow (search, removal) is described by Roblox but not all shown.

## Related
[Menus and Navigation](../01-UI-UX/Menus-and-Navigation.md) · [UI 14 Berry Avenue Avatar Flow Chart](../01-UI-UX/Analyses/UI-14-Berry-Avenue-Avatar-Flow-Chart.md) · [R13 Readable Mobile Interface](../18-Skill-Training/Design-Recipes/R13-Readable-Mobile-Interface.md)
