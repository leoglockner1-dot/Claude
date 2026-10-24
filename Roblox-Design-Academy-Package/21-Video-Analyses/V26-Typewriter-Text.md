---
title: "V26 — Typewriter dialogue with rich-text keywords"
tags: [video, reference, ui, animation, narrative]
reference_type: "video"
date_accessed: "2026-10-24"
---

# V26 — Typewriter dialogue with rich-text keywords

## Identity
- **Name:** V26 — Typewriter dialogue with rich-text keywords
- **Reference type:** Video (official Roblox Creator Docs recording)
- **Source page:** https://create.roblox.com/docs/ui/animation (Typewriter effect on text)
- Local clip: [V26-typewriter-text.mp4](../Assets/Animation-VFX/clips/V26-typewriter-text.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/ui/ui-animation/Text-Typewriter.mp4>
- **Creator/publisher:** Roblox Corporation (CC BY 4.0)
- **Date accessed:** 2026-10-24
- **How it was analysed:** 12 sampled frames + per-frame motion energy (20 fps) + audio RMS envelope, onset detection and spectral centroid (16 kHz mono), plus targeted frame crops where noted. **Audio was measured as waveform data, not listened to.**

![V26-typewriter-text analysis sheet](../Assets/Animation-VFX/video-sheets/V26-typewriter-text-sheet.jpg)

*Sheet legend: blue = motion energy over time, orange = audio RMS, white lines = detected audio onsets, numbers = seconds.*

## What is observable
20 s, silent. Dungeon door; a dark caption box near the top reveals text character by character: "Beyond this door is the **Great Zorgoth**… [dagger icon]" (name in red) then "…who rules this dungeon **unchallenged!** [devil icon]" (keyword yellow). From sampled frames, "Beyond this door" appears between ≈4.2 and 5.8 s and the two lines are complete by ≈7.5 s → roughly **10–15 characters/second** (approximate).

## What works
- Keywords coloured + small inline icons → scannable even if the player skips reading.
- Box grows with the text.

## Why it might work
Gradual reveal paces narrative; colour highlights carry the key information (Roblox UI/UX doc: highlight items/abilities with colour/bold).

## What does not work / trade-offs
Slow reveal annoys repeat players unless tapping completes the line (not shown).

## Reusable principles
- **UI-014** Narrative text: reveal ≈ 10–20 chars/s (hypothesis range), tap to complete, highlight keywords.

## Roblox implementation
`TextLabel.MaxVisibleGraphemes` incremented over time + `RichText` `<font color>`; skip on input.

## Original application
A detective game where clues in dialogue are highlighted and automatically added to a notebook icon that pulses once.

## Confidence
Medium (reveal speed estimated from sparse frames).

## Limitations
Speed approximate.

## Related
[Typography Color and Spacing](../01-UI-UX/Typography-Color-and-Spacing.md)
