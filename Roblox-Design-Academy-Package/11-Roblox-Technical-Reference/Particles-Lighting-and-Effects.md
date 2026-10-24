---
title: "Particles, Lighting and Post-Processing"
tags: [technical, vfx, lighting]
note_type: "technical-reference"
---

# Particles, Lighting and Post-Processing

> **Verified** against the Roblox Creator Docs (GitHub mirror commit 4e795e6 and create.roblox.com, accessed 2026-10-24). Re-check yearly. Items marked *(recommendation)* are design advice, not engine facts.

## ParticleEmitter
- `Rate` ≤ **400/s per emitter (100/s on mobile)**; `Lifetime` capped at 20 s; flipbook framerate ≤30 fps; `:Emit(n)` for bursts. Cost from **fill-rate** and **overdraw**. [particle emitters](https://create.roblox.com/docs/effects/particle-emitters)
## Other effects
`Beam`, `Trail`, `Highlight` (max **255** displayed simultaneously; extras silently ignored), light sources (`PointLight`, `SpotLight`, `SurfaceLight`). [effects](https://create.roblox.com/docs/effects)
## Post-processing (Lighting or Camera)
`BloomEffect`, `BlurEffect`, `ColorCorrectionEffect` (Brightness, Contrast, Saturation, TintColor), `DepthOfFieldEffect`, `SunRaysEffect`, `ColorGradingEffect` (TonemapperPreset). In `Lighting` they apply to all players. [post-processing](https://create.roblox.com/docs/environment/post-processing-effects)
*(recommendation)* Use local (client) effects for personal feedback (damage flash) and keep post-processing subtle on mobile.
