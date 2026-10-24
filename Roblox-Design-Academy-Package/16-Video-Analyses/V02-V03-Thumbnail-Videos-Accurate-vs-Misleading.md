---
title: "V02/V03 — Thumbnail video: accurate vs misleading (Roblox example pair)"
tags: [video, reference, thumbnail, marketing]
reference_type: "video"
date_accessed: "2026-10-24"
---

# V02/V03 — Thumbnail video: accurate vs misleading (Roblox example pair)

## Identity
- **Name:** V02/V03 — Thumbnail video: accurate vs misleading (Roblox example pair)
- **Reference type:** Video (official Roblox Creator Docs recording)
- **Source page:** https://create.roblox.com/docs/production/publishing/thumbnails (Video accuracy)
- Local clip: [V02-thumbnail-video-accurate.mp4](../Assets/Animation-VFX/clips/V02-thumbnail-video-accurate.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/publishing/experience-metadata/Thumbnail-Video-Accurate.mp4>
- Local clip: [V03-thumbnail-video-inaccurate.mp4](../Assets/Animation-VFX/clips/V03-thumbnail-video-inaccurate.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/publishing/experience-metadata/Thumbnail-Video-Inaccurate.mp4>
- **Creator/publisher:** Roblox Corporation (CC BY 4.0)
- **Date accessed:** 2026-10-24
- **How it was analysed:** 12 sampled frames + per-frame motion energy (20 fps) + audio RMS envelope, onset detection and spectral centroid (16 kHz mono), plus targeted frame crops where noted. **Audio was measured as waveform data, not listened to.**

![V02-thumbnail-video-accurate analysis sheet](../Assets/Animation-VFX/video-sheets/V02-thumbnail-video-accurate-sheet.jpg)
![V03-thumbnail-video-inaccurate analysis sheet](../Assets/Animation-VFX/video-sheets/V03-thumbnail-video-inaccurate-sheet.jpg)

*Sheet legend: blue = motion energy over time, orange = audio RMS, white lines = detected audio onsets, numbers = seconds.*

## What is observable
**V02 (accurate, 15.3 s, no audio):** continuous third-person gameplay on tropical floating rocks: spawn on a pink pad (0.6 s), sparkle burst on jump (1.9 s), the player follows a line of golden coins across rocks, a second sparkle double-jump (7.0 s), lands on grass in ruins (14.6 s). Motion energy is continuous with no single dominant spike → **no hard cuts**. The touch-thumbstick ring is visible (real client UI).

**V03 (misleading, 15.6 s, no audio):** cinematic character close-ups with a glowing gold card behind the heroine (0.7–4.5 s), a nuclear-style mushroom explosion (5.8–7.1 s), a **single large motion spike at ≈8.4 s (hard cut)** to a gameplay-like platform, then flying with a sword slash ring, more explosions, and a "LEGENDS ARISE" logo end card (14.9 s).

## What works
- V02 shows the actual verb (jump between rocks, collect coins) in one unbroken take; a viewer knows what they will do.
- V02 uses sparkles only at jump moments — effects mark actions rather than decorate.

## Why it might work
Roblox's video rules reject "Misrepresented gameplay", "Artificial visuals" and advertisement-like content; V03 combines cinematic close-ups, effects beyond normal play and a logo card. Thumbnail videos are reviewed and a rejection still costs one of 3 monthly uploads (see [Platform facts](../11-Roblox-Technical-Reference/Publishing-Thumbnails-and-Icons.md)).

## What does not work / trade-offs
- V02 is visually calm; it relies on the environment's beauty. For a competitive game it would undersell intensity.
- V03 is far more "exciting" in isolation — which is exactly the temptation the rule exists to prevent.

## Reusable principles
- **THUMB-010** Marketing must depict the real loop ([Thumbnail principles](../14-Design-Principles/Thumbnail-and-Icon-Principles.md)).
- Show the verb within the first seconds; avoid cuts that hide what the player controls.

## Roblox implementation
Record with Studio's Freecam (Shift+P) or a smooth follow camera during a real playtest; trim to 15–30 s; no voice-over, no lyrics, no "50% off" overlays (Roblox rules).

## Original application
For a mining game: one continuous 20 s take of a player mining a vein, the ore flying to the backpack counter, and the first upgrade being bought — no title cards.

## Confidence
High — both clips are Roblox-labelled examples and their content was directly observed.

## Limitations
Roblox produced both for illustration; real submitted videos may be judged differently in moderation.

## Related
[Thumbnail Principles](../02-Thumbnails-and-Icons/Thumbnail-Principles.md) · [Publishing Thumbnails and Icons](../11-Roblox-Technical-Reference/Publishing-Thumbnails-and-Icons.md)
