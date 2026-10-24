---
title: "V21/V22 — Mystery of Duvall Drive: cutscene text and respawn fades"
tags: [video, reference, animation, level-design, transitions, narrative]
reference_type: "video"
date_accessed: "2026-10-24"
---

# V21/V22 — Mystery of Duvall Drive: cutscene text and respawn fades

## Identity
- **Name:** V21/V22 — Mystery of Duvall Drive: cutscene text and respawn fades
- **Reference type:** Video (official Roblox Creator Docs recording)
- **Source page:** https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/main-design-requirements
- Local clip: [V21-duvall-cutscene.mp4](../Assets/Animation-VFX/clips/V21-duvall-cutscene.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/resources/mystery-of-duvall-drive/technical-overview/cutscene.mp4>
- Local clip: [V22-duvall-respawn.mp4](../Assets/Animation-VFX/clips/V22-duvall-respawn.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/resources/mystery-of-duvall-drive/technical-overview/respawning-players.mp4>
- **Creator/publisher:** Roblox Corporation (CC BY 4.0)
- **Date accessed:** 2026-10-24
- **How it was analysed:** 12 sampled frames + per-frame motion energy (20 fps) + audio RMS envelope, onset detection and spectral centroid (16 kHz mono), plus targeted frame crops where noted. **Audio was measured as waveform data, not listened to.**

![V21-duvall-cutscene analysis sheet](../Assets/Animation-VFX/video-sheets/V21-duvall-cutscene-sheet.jpg)
![V22-duvall-respawn analysis sheet](../Assets/Animation-VFX/video-sheets/V22-duvall-respawn-sheet.jpg)

*Sheet legend: blue = motion energy over time, orange = audio RMS, white lines = detected audio onsets, numbers = seconds.*

## What is observable
**V21 (14.6 s):** interacting with a photo album shows a handwritten-font memory note (≈3.0 s). Then the antagonist speaks in large, spaced, distorted typewriter text at the bottom ("Someone…attempts to restore…seal / Can't…let you do that…", 4.3–5.5 s; "…come to us…", 6.7–9.1 s) while the room darkens → **full black 9.1–10.3 s (~1.2 s)** → new location fades in, pink-tinted, **blurred then focused** (11.5 → 12.8 s).

**V22 (8.2 s):** the player falls off a treehouse walkway through foliage (≈1–4.5 s), sees a purple glyph void (5.1 s), **black for ≈0.7 s** (5.8–6.5 s), and reappears on the walkway at 7.2 s.

## What works
- Typography distinguishes voices: handwriting = memory, spaced typewriter = threat.
- Black holds hide teleports; blur→focus gives the arrival a beat.
- Respawn returns the player close to where they fell (short loss of progress).

## Why it might work
Roblox's write-up: the EventManager transports players after tasks; respawn is a short CFrame teleport. Fades mask discontinuities that would otherwise confuse orientation.

## What does not work / trade-offs
The threat text over a dark scene has low contrast at times; tracks were silent in these recordings so audio role cannot be judged.

## Reusable principles
- **LEVEL-004** Mask spatial discontinuities with short fades (~0.7–1.2 s observed); **ID-004** typography is part of narrative identity.

## Roblox implementation
`Lighting.ColorCorrection` or a full-screen `Frame` tween to black; teleport with `PivotTo` during black; `DepthOfFieldEffect` FocusDistance tween for blur→focus.

## Original application
A dream-world obby where falling off fades to white (not black) with a soft chime, and the checkpoint statue glows on arrival.

## Confidence
High for visuals; audio absent.

## Limitations
Tracks silent; showcase project, not a commercial game.

## Related
[Environmental Communication](../12-Level-Design/Environmental-Communication.md) · [Loading Death and Round Transitions](../01-UI-UX/Loading-Death-and-Round-Transitions.md)
