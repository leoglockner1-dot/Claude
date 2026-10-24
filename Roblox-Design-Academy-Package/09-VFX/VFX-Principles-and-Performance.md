---
title: "VFX Principles and Performance"
tags: [vfx, performance]
note_type: "topic"
---

# VFX Principles and Performance

## Principles
FEEL-005 semantic shapes/colours · FEEL-006 intensity tiers · FEEL-009 ambient fades · FEEL-001 telegraphs → [Game Feel Principles](../17-Design-Principles/Game-Feel-Principles.md)

## Evidence
[V13 Health Pickup](../21-Video-Analyses/V13-Health-Pickup.md) · [V20 Burst Particle Trap](../21-Video-Analyses/V20-Burst-Particle-Trap.md) · [V27 Fading Particles Volcano](../21-Video-Analyses/V27-Fading-Particles-Volcano.md) · [GF 01 Winds of Fortune Combat Feedback](../08-Animation-and-Game-Feel/Analyses/GF-01-Winds-of-Fortune-Combat-Feedback.md)

## Verified engine limits (Roblox docs)
- ParticleEmitter: up to **400 particles/s per emitter (100/s on mobile)**; lifetime capped at 20 s; flipbook ≤30 fps.
- Cost drivers: **fill-rate** (screen area) and **overdraw** (overlapping transparent layers).
- `Highlight`: only **255** shown at once on the client.
- Avoid partial transparency where possible (overdraw).
→ [Particles Lighting and Effects](../14-Technical-Reference/Particles-Lighting-and-Effects.md)

## Effect tier table (template)
| Tier | Events | Budget |
|---|---|---|
| S (subtle) | footsteps, small pickups, hover | ≤10 particles, ≤0.3 s, no shake |
| M | hits, purchases, quest step | ≤30 particles, ≤0.6 s, flash allowed |
| L | kills, level-up, rare drop | burst + light + sound stinger, ≤1.5 s |
| XL | boss, legendary, fail state | full-screen allowed briefly, camera move, ≤3 s, skippable |

## Multiplayer readability
Other players' effects should be dimmer/smaller than your own; never hide enemies or hazards.
