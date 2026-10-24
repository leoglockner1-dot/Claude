---
title: "V14–V17 — Pickup, chomp, button and coin sounds (timing measured)"
tags: [video, reference, audio, game-feel, pickups]
reference_type: "video"
date_accessed: "2026-10-24"
---

# V14–V17 — Pickup, chomp, button and coin sounds (timing measured)

## Identity
- **Name:** V14–V17 — Pickup, chomp, button and coin sounds (timing measured)
- **Reference type:** Video (official Roblox Creator Docs recording)
- **Source page:** https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio · https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/in-game-sounds
- Local clip: [V14-collectable-gems-sound.mp4](../Assets/Animation-VFX/clips/V14-collectable-gems-sound.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/tutorials/in-game-sounds/ingameSounds-collectables.mp4>
- Local clip: [V15-gumdrop-chomp-sound.mp4](../Assets/Animation-VFX/clips/V15-gumdrop-chomp-sound.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/tutorials/add-2D-audio/Feedback-Final.mp4>
- Local clip: [V16-ui-button-jingle.mp4](../Assets/Animation-VFX/clips/V16-ui-button-jingle.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/tutorials/add-2D-audio/UI-Final.mp4>
- Local clip: [V17-platformer-jump-coin-sounds.mp4](../Assets/Animation-VFX/clips/V17-platformer-jump-coin-sounds.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/tutorials/add-2D-audio/game-state-example.mp4>
- **Creator/publisher:** Roblox Corporation (CC BY 4.0)
- **Date accessed:** 2026-10-24
- **How it was analysed:** 12 sampled frames + per-frame motion energy (20 fps) + audio RMS envelope, onset detection and spectral centroid (16 kHz mono), plus targeted frame crops where noted. **Audio was measured as waveform data, not listened to.**

![V14-collectable-gems-sound analysis sheet](../Assets/Animation-VFX/video-sheets/V14-collectable-gems-sound-sheet.jpg)
![V15-gumdrop-chomp-sound analysis sheet](../Assets/Animation-VFX/video-sheets/V15-gumdrop-chomp-sound-sheet.jpg)
![V16-ui-button-jingle analysis sheet](../Assets/Animation-VFX/video-sheets/V16-ui-button-jingle-sheet.jpg)
![V17-platformer-jump-coin-sounds analysis sheet](../Assets/Animation-VFX/video-sheets/V17-platformer-jump-coin-sounds-sheet.jpg)

*Sheet legend: blue = motion energy over time, orange = audio RMS, white lines = detected audio onsets, numbers = seconds.*

## What is observable
**V14 gems (3.6 s):** gem disappearance (green-pixel drop) at **0.93 / 1.60 / 2.37 s** vs sound onsets at **1.05 / 1.65 / 2.35 s** → offsets **+120 ms, +50 ms, −20 ms**. Dominant pitch **466 Hz, 466 Hz, 623 Hz** (third pickup higher); level steady ≈ −23.6 dB RMS.

**V15 gumdrop (3.8 s):** gumdrop vanishes ≈1.7–1.8 s, "chomp" onset 2.05 s, bright (centroid ≈3.4 kHz), peak −18.9 dBFS. No particle burst — the sound carries the event.

**V16 UI button (10.1 s):** a round peppermint button bottom-left toggles red↔cyan on each press (1.7 / 5.0 / 7.85 s); a jingle starts on **the same frame** as the visual toggle (centroid ≈1.4–1.6 kHz, ~0.6–0.8 s decay).

**V17 platformer (3.9 s):** docs: "airy whoosh as soon as the player presses jump" and "high-pitched ding and coins jostling … as soon as the character touches a coin"; measured onsets 0.25, 0.60 s (centroid ≈2.7 kHz), 2.05 s (1.3 kHz), 2.35 s (2.3 kHz).

## What works
- UI sound + visual state change synchronized to the frame (V16).
- Pitch change on the third gem (V14) hints at streak/variation.
- Short, bright one-shots for positive events (V15, V17).

## Why it might work
Roblox docs state one-shot 2D audio gives "an instant, clear response to crucial gameplay functions". Synchronization below ~0.1 s reads as one event (NN/g 0.1 s limit for instantaneous feel — UI context, applied here as a heuristic).

## What does not work / trade-offs
- V14's first sound lags the visual by ~120 ms and V15's chomp follows the disappearance by roughly 0.2–0.3 s — perceptible lag risk (hypothesis; sampling resolution 33–50 ms).
- Repeating an identical sample (466 Hz twice) invites fatigue in high-frequency pickups.

## Reusable principles
- **AUDIO-001** Trigger feedback sounds client-side on the same frame as the visual; **AUDIO-003** vary pitch/sample for frequent sounds; **AUDIO-002** bright timbres for rewards.

## Roblox implementation
Play pickup sounds from a `LocalScript` on the client when the touch is detected locally (then confirm on server); randomize `PlaybackSpeed` 0.95–1.08 or step it up with a combo counter.

## Original application
A berry-picking loop where each berry in a 5-berry bush plays the next note of a pentatonic scale, completing a tiny melody when the bush is cleared.

## Confidence
High for timings/pitches (measured); Medium for perceptual thresholds.

## Limitations
Waveform/spectrum only; no listening; small samples.

## Related
[Sound Recipes](../10-Sound-Design/Sound-Recipes.md) · [Measured Audio Observations](../10-Sound-Design/Measured-Audio-Observations.md)
