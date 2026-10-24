---
title: "V08/V09 — Laser Tag victory vs defeat screen (audio timbre measured)"
tags: [video, reference, ui, audio, round-transitions]
reference_type: "video"
date_accessed: "2026-10-24"
---

# V08/V09 — Laser Tag victory vs defeat screen (audio timbre measured)

## Identity
- **Name:** V08/V09 — Laser Tag victory vs defeat screen (audio timbre measured)
- **Reference type:** Video (official Roblox Creator Docs recording)
- **Source page:** https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting/add-rounds
- Local clip: [V08-laser-tag-victory.mp4](../Assets/Animation-VFX/clips/V08-laser-tag-victory.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/tutorials/gameplay-scripting/Adding-Rounds/Victory-UI.mp4>
- Local clip: [V09-laser-tag-defeat.mp4](../Assets/Animation-VFX/clips/V09-laser-tag-defeat.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/tutorials/gameplay-scripting/Adding-Rounds/Defeat-UI.mp4>
- **Creator/publisher:** Roblox Corporation (CC BY 4.0)
- **Date accessed:** 2026-10-24
- **How it was analysed:** 12 sampled frames + per-frame motion energy (20 fps) + audio RMS envelope, onset detection and spectral centroid (16 kHz mono), plus targeted frame crops where noted. **Audio was measured as waveform data, not listened to.**

![V08-laser-tag-victory analysis sheet](../Assets/Animation-VFX/video-sheets/V08-laser-tag-victory-sheet.jpg)
![V09-laser-tag-defeat analysis sheet](../Assets/Animation-VFX/video-sheets/V09-laser-tag-defeat-sheet.jpg)

*Sheet legend: blue = motion energy over time, orange = audio RMS, white lines = detected audio onsets, numbers = seconds.*

## What is observable
Both 5 s. Identical layout: centred italic bold word over the sky/arena, small subtitle "Green wins" below. Text: **"Victory!"** vs **"Defeat…"**. No animation visible in sampled frames (motion energy ≈ 0 after the first frame).
Audio stinger at t≈0 in both. **Measured:** Victory spectral centroid **1,655 Hz** with strongest energy near 1.7 kHz; Defeat centroid **1,150 Hz** with dominant energy at **170–180 Hz** and a longer tail (~2.3 s to −20 dB).

## What works
- One reusable layout; the state is carried by word, punctuation ("!" vs "…") and **sound brightness**.
- Text is centred and large; nothing else competes.

## Why it might work
Brighter, higher-frequency sounds read as positive and lower, darker sounds as negative in common game-audio practice (general knowledge, consistent with the measurement; not a Roblox rule).

## What does not work / trade-offs
- No motion, no celebration, no score breakdown — a functional minimum. Victory feels as heavy as defeat visually.
- The subtitle is tiny.

## Reusable principles
- **AUDIO-002** Encode outcome valence in timbre/pitch; **FEEL-008** wins deserve a short celebration with clear next step ([Audio principles](../17-Design-Principles/Audio-Principles.md)).

## Roblox implementation
Show a `ScreenGui` on `RoundEnded`; tween the title `TextSize`/scale from 0.8→1.0 (Back Out, ~0.25 s) for victory only; play different `Sound`s; add a "Next round in N" countdown.

## Original application
A racing game's finish screen that keeps one layout but changes the accent colour (gold vs grey), the stinger (rising vs falling interval) and shows "+XP" counting up only on podium finishes.

## Confidence
High for measurements; Medium for the perceptual interpretation.

## Limitations
Audio not listened to.

## Related
[Reward Reveals and Celebrations](../08-Animation-and-Game-Feel/Reward-Reveals-and-Celebrations.md) · [Sound Recipes](../10-Sound-Design/Sound-Recipes.md)
