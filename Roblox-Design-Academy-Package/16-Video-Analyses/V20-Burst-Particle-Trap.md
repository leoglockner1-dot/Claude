---
title: "V20 — Telegraphed trap with a burst effect"
tags: [video, reference, vfx, level-design, game-feel]
reference_type: "video"
date_accessed: "2026-10-24"
---

# V20 — Telegraphed trap with a burst effect

## Identity
- **Name:** V20 — Telegraphed trap with a burst effect
- **Reference type:** Video (official Roblox Creator Docs recording)
- **Source page:** https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/use-particles-for-explosions
- Local clip: [V20-burst-particle-trap.mp4](../Assets/Animation-VFX/clips/V20-burst-particle-trap.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/tutorials/using-particles-for-explosions/burstParticle_finalInContext.mp4>
- **Creator/publisher:** Roblox Corporation (CC BY 4.0)
- **Date accessed:** 2026-10-24
- **How it was analysed:** 12 sampled frames + per-frame motion energy (20 fps) + audio RMS envelope, onset detection and spectral centroid (16 kHz mono), plus targeted frame crops where noted. **Audio was measured as waveform data, not listened to.**

![V20-burst-particle-trap analysis sheet](../Assets/Animation-VFX/video-sheets/V20-burst-particle-trap-sheet.jpg)

*Sheet legend: blue = motion energy over time, orange = audio RMS, white lines = detected audio onsets, numbers = seconds.*

## What is observable
3 s, muted. A stone tile with a glowing cyan glyph emits **small idle sparks** (the warning). The avatar walks onto it; **burst window ≈1.25–1.65 s** (measured motion peak): full-frame cyan lightning tendrils for ~0.4 s, the avatar breaks apart; debris and sparks settle by ≈2.0 s, then the idle sparks resume (trap re-armed).

## What works
- Anticipation is built into the level (idle sparks) — fair warning.
- The payoff is short (~0.4 s) and huge; then the scene returns to readable.

## Why it might work
Telegraphing makes failure feel fair; brief extreme intensity marks a rare, important event (fail state).

## What does not work / trade-offs
Full-screen coverage would hide the play space if it happened often; acceptable for death, not for every hit.

## Reusable principles
- **FEEL-001** Telegraph hazards (anticipation) before payoff; **FEEL-006** reserve full-screen intensity for rare events.

## Roblox implementation
Continuous low `Rate` emitter for the idle state + a second emitter with `Rate=0` fired via `:Emit(n)` on `Touched`; keep `Lifetime` short.

## Original application
Mushroom traps in a forest that puff tiny spores while idle and release one big spore cloud that briefly tints the screen green when stepped on.

## Confidence
High.

## Limitations
No audio.

## Related
[VFX Principles and Performance](../05-Animation-and-Game-Feel/VFX-Principles-and-Performance.md) · [Environmental Communication](../08-Level-Design/Environmental-Communication.md)
