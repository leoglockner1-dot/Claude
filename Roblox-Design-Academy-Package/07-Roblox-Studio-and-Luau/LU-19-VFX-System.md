---
title: "LU-19 — VFX system: emit, pool, budget"
tags: [luau, vfx, particles, performance]
note_type: "procedure"
evidence: "official docs; not executed"
---

# LU-19 — VFX system: emit, pool, budget

## Purpose
Play effects from code consistently and cheaply: bursts on events, loops while states last, with a budget that protects mobile frame rate.

## Facts (effects docs)
- `ParticleEmitter.Rate` is particles per second; one emitter can create **up to 400/s (100/s on mobile)**. The docs advise keeping the rate as low as possible and using size and other properties for the look.
- For one-shot bursts, set `Enabled = false` and call `emitter:Emit(count)` (the explosion tutorial uses this pattern).
- Particles, decals and textures don't batch well and add draw calls. **Property changes on ParticleEmitters can dramatically affect performance** (performance-optimization/improve).
- Beams and Trails exist for lasers, slashes and motion trails.

## Procedure
1. Author each effect as a template (Attachment + emitters) in `ReplicatedStorage/VFX`.
2. A client `VfxController.play(name, cframe or attachment, scale)` clones from a **pool** (pre-created, reused), positions it, calls `:Emit(n)` per emitter and returns it to the pool after the longest particle lifetime.
3. The server tells clients *what happened* (`HitAt(position, type)`) through one RemoteEvent, or an UnreliableRemoteEvent for purely cosmetic cues. Clients render it. The server never spawns particles for everyone at its own cost.
4. **Budget:** count active effects; above the cap, skip low-priority ones (ambient sparkles) before high-priority ones (hit confirmation). Lower emission counts on `ViewportDisplaySize.Small` or when the frame time is high.
5. Respect the readability hierarchy: gameplay-critical effects (telegraphs, hits) get contrast and timing priority over decorative ones ([VFX Principles](../09-VFX/VFX-Principles-and-Performance.md)).

## Common mistakes
- `Instance.new("ParticleEmitter")` per hit with no cleanup.
- Leaving emitters `Enabled = true` and toggling them for bursts (timing becomes rate-dependent).
- Animating emitter properties every frame from script (expensive per the docs).
- Huge, bright, long-lived particles that hide enemies and telegraphs.

## Test cases
- Trigger the effect 100 times quickly: the instance count stays flat (the pool works); no frame-time spike beyond the target in the MicroProfiler.
- Device Emulator on a phone profile: the effect still reads, and the reduced counts apply.

## Acceptance criteria
Pooled playback; per-effect particle counts documented; a frame-budget fallback exists; the server sends events, not particles.

## References
- https://create.roblox.com/docs/effects/particle-emitters · https://create.roblox.com/docs/performance-optimization/improve · https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/use-particles-for-explosions
