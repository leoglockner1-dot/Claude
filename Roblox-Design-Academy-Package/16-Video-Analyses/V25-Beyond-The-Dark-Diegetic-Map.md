---
title: "V25 — Beyond the Dark: diegetic holographic UI"
tags: [video, reference, ui, visual-identity, diegetic]
reference_type: "video"
date_accessed: "2026-10-24"
---

# V25 — Beyond the Dark: diegetic holographic UI

## Identity
- **Name:** V25 — Beyond the Dark: diegetic holographic UI
- **Reference type:** Video (official Roblox Creator Docs recording)
- **Source page:** https://create.roblox.com/docs/resources/beyond-the-dark/user-interface
- Local clip: [V25-beyond-the-dark-diegetic-map.mp4](../Assets/Animation-VFX/clips/V25-beyond-the-dark-diegetic-map.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/resources/beyond-the-dark/user-interface/Final-UI.mp4>
- **Creator/publisher:** Roblox Corporation (CC BY 4.0)
- **Date accessed:** 2026-10-24
- **How it was analysed:** 12 sampled frames + per-frame motion energy (20 fps) + audio RMS envelope, onset detection and spectral centroid (16 kHz mono), plus targeted frame crops where noted. **Audio was measured as waveform data, not listened to.**

![V25-beyond-the-dark-diegetic-map analysis sheet](../Assets/Animation-VFX/video-sheets/V25-beyond-the-dark-diegetic-map-sheet.jpg)

*Sheet legend: blue = motion energy over time, orange = audio RMS, white lines = detected audio onsets, numbers = seconds.*

## What is observable
16 s, portrait capture, silent. A curved cyan holographic panel in the world reads "CONDITIONS NEAR KN-22 / WELCOME TO KERR-NEWMAN / DEPARTURES/ARRIVALS" next to a lavender 3D station model; an "[E] Interact" prompt; the panel shifts with camera parallax.

## What works
The interface is part of the world's fiction (signage of a space station) — styling, glow and curvature match the setting.

## Why it might work
Diegetic UI strengthens world-to-UI consistency and avoids screen clutter.

## What does not work / trade-offs
Curved, glowing, small text is harder to read than flat screen UI; works for ambient information, not for time-critical decisions.

## Reusable principles
- **ID-003** World-to-UI consistency; use diegetic UI for flavour/navigation, screen UI for critical state.

## Roblox implementation
`SurfaceGui` on curved/angled parts, `LightInfluence` low, `Brightness` up; keep critical info duplicated on screen.

## Original application
A pirate game whose quest board is a physical notice board with pinned parchment notes; the screen HUD only shows the active quest.

## Confidence
High.

## Limitations
Silent; portrait crop.

## Related
[Visual Identity Framework](../07-Visual-Identity/Visual-Identity-Framework.md)
