---
title: "V12 — Upgrade button with no feedback (baseline to improve on)"
tags: [video, reference, ui, progression, anti-pattern]
reference_type: "video"
date_accessed: "2026-10-24"
---

# V12 — Upgrade button with no feedback (baseline to improve on)

## Identity
- **Name:** V12 — Upgrade button with no feedback (baseline to improve on)
- **Reference type:** Video (official Roblox Creator Docs recording)
- **Source page:** https://create.roblox.com/docs/tutorials/curriculums/core/scripting/script-an-upgrade-button
- Local clip: [V12-upgrade-button-baseline.mp4](../Assets/Animation-VFX/clips/V12-upgrade-button-baseline.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/tutorials/script-an-upgrade-button/script-an-upgrade-button-example.mp4>
- **Creator/publisher:** Roblox Corporation (CC BY 4.0)
- **Date accessed:** 2026-10-24
- **How it was analysed:** 12 sampled frames + per-frame motion energy (20 fps) + audio RMS envelope, onset detection and spectral centroid (16 kHz mono), plus targeted frame crops where noted. **Audio was measured as waveform data, not listened to.**

![V12-upgrade-button-baseline analysis sheet](../Assets/Animation-VFX/video-sheets/V12-upgrade-button-baseline-sheet.jpg)

*Sheet legend: blue = motion energy over time, orange = audio RMS, white lines = detected audio onsets, numbers = seconds.*

## What is observable
8.7 s, silent. Leaderboard (People / Coins / Jump) top-right: 10 coins, Jump 0. Clicking a **small white "Upgrade" button** bottom-right (turns grey while pressed) → Coins 10→5, Jump 0→30 (≈1.8–2.5 s); again 5→0, Jump 30→60 (≈3.3–4.0 s). From 5.4 s the character jumps visibly higher.

## What works
It works functionally and shows the full purchase→stat→effect chain.

## Why it might work
It is a scripting tutorial; feedback is intentionally out of scope.

## What does not work / trade-offs
- The only feedback is a number change in the leaderboard, far from the button.
- No sound, no animation, no "+30 Jump" popup, no preview of the next cost.
- The payoff (higher jump) is only discovered later.

## Reusable principles
- **PROG-003** Every purchase needs immediate, local confirmation + preview of the effect; see recipe [R04 Upgrade purchase](../13-Reusable-Design-Recipes/R04-Upgrade-Purchase-Interaction.md).

## Roblox implementation
Add: button press scale 0.95 (0.06 s), cost flies from currency counter into the button, stat label pops "+30" near the button, short rising sound, and a camera-free demo (character auto-jumps once).

## Original application
A gardening upgrade "Bigger watering can": on purchase the can in the player's hand visibly grows with a squash-stretch and the next watering shows the larger splash radius.

## Confidence
High.

## Limitations
Tutorial context, not a shipped game.

## Related
[Reward Presentation](../04-Progression-and-Economy/Reward-Presentation.md) · [R04 Upgrade Purchase Interaction](../13-Reusable-Design-Recipes/R04-Upgrade-Purchase-Interaction.md)
