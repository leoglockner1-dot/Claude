---
title: "CS-07 — DOORS (procedural horror co-op)"
tags: [case-study, horror, co-op]
note_type: "case-study"
date_accessed: "2026-10-24"
---

# CS-07 — DOORS (procedural horror co-op)

> **Method:** built from the game's public page data, its own description, its current icon/thumbnails and its game-pass catalogue (Roblox APIs, 2026-10-24). **The games were not played.** Loop descriptions are **inferences** from these sources unless marked otherwise. Popularity is context, not proof of good design.

## Observable data
| Field | Value (2026-10-24) |
|---|---|
| Game | [DOORS 🍬🍭](https://www.roblox.com/games/6516141723/) · universe 2440500124 |
| Creator | LSPLASH |
| Genre (Roblox) | Survival / Escape |
| Concurrent players at capture | 119,319 |
| Total visits | 7,941,275,569 |
| Like ratio | 93 % |
| Created / last updated | 2021-03-14 / 2026-10-24 |
| Game passes for sale | 3: BUSTER PASS (HALLOWEEN '26) (99 R$); KITTY BUNDLE (299 R$); ADMIN PANEL (499 R$) |

**Description excerpt (developer's own words):** "YOU'RE INVITED TO THE ESTATE! 🍬🍭🎃 / Part of THE HOLLOW Event! /  / A horror game involving doors. /  / We recommend entering without a guide; use each death as a lesson. / ⚠️ Loud sounds, flashing lights ahead! / 🎧 📷 Headphones & max graphics recommended /  / ❤️ Join the LSPLASH group for a free Revive! / ⭐ Buy (and we…"

![doors__u2440500124.jpg](../Assets/Icons/live-2026-10-24/doors__u2440500124.jpg)
![doors__u2440500124__00.jpg](../Assets/Thumbnails/live-2026-10-24/doors__u2440500124__00.jpg)


## Loop breakdown (inferred)
| Layer | Inference |
|---|---|
| Minute-to-minute | Walk door to door through a mansion, react to entities |
| Most repeated action | Survive rooms; "use each death as a lesson" (description) |
| Progression engine | Knobs currency spent in the **pre-run shop** (Roblox docs case), unlocks |
| Social loop | Group runs (elevator), event crossover (The Hollow) |
| Monetization | 3 passes: Buster Pass (Halloween '26) 99, Kitty Bundle 299, Admin Panel 499 |

## What appears to work
- Description sets expectations honestly: "Loud sounds, flashing lights ahead", "Headphones & max graphics recommended".
- Pre-run shop is Roblox's example of a well-placed contextual purchase (PROG-008).
- Event crossover framing in marketing ([TI-14](../02-Thumbnails-and-Icons/Analyses/TI-14-The-Hollow-Event-Frame.md)).

## Risks, weaknesses or open questions
- Audio-dependent horror needs visual cues for muted players (AUDIO-004) — not verified.

## Lessons for our games
- Teach through failure explicitly ("each death as a lesson") — learning is the loop.

## Original application
A submarine horror run where each failed dive reveals one new creature entry in a logbook, making death informative.

## Confidence
Medium.

## Related
[Shops and Monetization UI](../01-UI-UX/Shops-and-Monetization-UI.md) · [Audio Principles](../14-Design-Principles/Audio-Principles.md)
