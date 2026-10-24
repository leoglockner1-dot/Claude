---
title: "CS-13 — Roblox Laser Tag reference game (gameplay-scripting curriculum)"
tags: [case-study, competitive, reference-project]
note_type: "case-study"
date_accessed: "2026-10-24"
---

# CS-13 — Roblox Laser Tag reference game (gameplay-scripting curriculum)

> Source: Roblox Creator Docs gameplay-scripting curriculum (https://create.roblox.com/docs/tutorials/curriculums/gameplay-scripting) — official reference project; analysed via its videos.

## Observed
- First-person blaster with **Ready / Blasting / Disabled** states → shot cadence ≈0.6 s ([V10/V11](../16-Video-Analyses/V10-V11-Blaster-Cooldown-vs-Spam.md)).
- Objective banner: "Tag opposing players to score points! First team to 3 points wins."
- Round end: "Victory!" / "Defeat…" with bright vs dark stingers ([V08/V09](../16-Video-Analyses/V08-V09-Victory-and-Defeat-Screens.md)).

![Blaster with cooldown](../Assets/Animation-VFX/video-sheets/V10-blaster-with-cooldown-sheet.jpg)

## Loop
Spawn → tag opponents → team reaches 3 → round end screen → next round. (Documented by Roblox.)

## Lessons
- Weapon states are a game-feel tool (FEEL-004).
- Round end screens need motion and a next step (FEEL-008).

## Original application
A water-balloon team game: balloons refill at fountains (state: Empty/Ready), first team to soak 5 rivals wins, splash-screen victory with rising tones.

## Confidence
High (official project, observed videos).

## Related
[Game Feel Principles](../14-Design-Principles/Game-Feel-Principles.md)
