---
title: "V28 — Linear vs Cubic easing on the same animation (measured)"
tags: [video, reference, animation, game-feel]
reference_type: "video"
date_accessed: "2026-10-24"
---

# V28 — Linear vs Cubic easing on the same animation (measured)

## Identity
- **Name:** V28 — Linear vs Cubic easing on the same animation (measured)
- **Reference type:** Video (official Roblox Creator Docs recording)
- **Source page:** https://create.roblox.com/docs/animation/editor (easing)
- Local clip: [V28a-easing-linear.mp4](../Assets/Animation-VFX/clips/V28a-easing-linear.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/animation/animation-editor/Easing-Linear.mp4>
- Local clip: [V28b-easing-cubic.mp4](../Assets/Animation-VFX/clips/V28b-easing-cubic.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/animation/animation-editor/Easing-Cubic.mp4>
- **Creator/publisher:** Roblox Corporation (CC BY 4.0)
- **Date accessed:** 2026-10-24
- **How it was analysed:** 12 sampled frames + per-frame motion energy (20 fps) + audio RMS envelope, onset detection and spectral centroid (16 kHz mono), plus targeted frame crops where noted. **Audio was measured as waveform data, not listened to.**

![V28a-easing-linear analysis sheet](../Assets/Animation-VFX/video-sheets/V28a-easing-linear-sheet.jpg)
![V28b-easing-cubic analysis sheet](../Assets/Animation-VFX/video-sheets/V28b-easing-cubic-sheet.jpg)

*Sheet legend: blue = motion energy over time, orange = audio RMS, white lines = detected audio onsets, numbers = seconds.*

## What is observable
Same golem rig animation in the Animation Editor, 12 s each. Motion-energy profile of one move (10 bins, normalized):
- **Linear:** 0.12, 0.45, 0.54, 0.50, 0.55, 0.59, 0.41, 0.30, … — a **flat plateau** (constant speed, abrupt start/stop).
- **Cubic:** 0.22, 0.39, 0.63, 0.77, **0.94**, 0.82, 0.81, 0.48, 0.32, 0.20 — a **bell curve** (accelerate, peak, decelerate). Bursts repeat about every 1.3 s with holds between.

## What works
Cubic motion reads as weighted and organic; linear reads mechanical.

## Why it might work
Slow-in/slow-out is one of the classic animation principles (Thomas & Johnston); real objects accelerate and decelerate.

## What does not work / trade-offs
Linear is still right for constant mechanical motion (conveyors, spinners) — see V18.

## Reusable principles
- **FEEL-003** Default to eased curves for characters and UI; reserve Linear for continuous mechanical motion.

## Roblox implementation
Animation Editor keyframe easing (Cubic/Elastic/Bounce…); for UI `TweenInfo` EasingStyle (`Quad` default, `Cubic`, `Back`…).

## Original application
A door that swings with Cubic Out on open and a tiny Back overshoot on close to feel heavy.

## Confidence
High (measured).

## Limitations
Animation Editor demo, not gameplay.

## Related
[Timing Reference](../05-Animation-and-Game-Feel/Timing-Reference.md) · [Tweening and Animation](../11-Roblox-Technical-Reference/Tweening-and-Animation.md)
