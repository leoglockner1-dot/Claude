---
title: "TUT-15 — Use particles for explosions (burst with Emit)"
tags: [tutorial, vfx, particles, explosion]
note_type: "tutorial-procedure"
source: "https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/use-particles-for-explosions"
source_author: "Roblox Creator Documentation"
licence: "Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution."
accessed: "2026-10-24"
evidence: "[SRC] = what the tutorial says; [ANALYSIS] = our reading; [SIM-TESTED] = reproduced in a Luau simulation; [HYP] = untested"
---

# TUT-15 — Use particles for explosions (burst with Emit)

**Skill:** Make a one-shot burst effect with a ParticleEmitter and trigger it from a script.

## Source and access
- Source: [https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/use-particles-for-explosions](https://create.roblox.com/docs/tutorials/use-case-tutorials/vfx/use-particles-for-explosions)
- Author: Roblox (official documentation). Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution.
- Access: Read the Markdown source of the page from the public Roblox/creator-docs repository (commit 4e795e6), accessed 2026-10-24. Images, videos and the linked sample places (.rbxl) were **not** opened, and no step was performed in Roblox Studio.

## Workflow in the tutorial [SRC]
1. Insert a `ParticleEmitter` named Explosion; set it up for a burst (rate 0 so it doesn't emit continuously, speed/lifetime/spread tuned).
2. Test bursts in edit mode with the Emit() plugin (type 100, press Emit).
3. Shape colour and transparency over lifetime with sequences.
4. A server Script on the trap part: on touch by a Humanoid, set `Health = 0` and call `particleEmitter:Emit(EMIT_AMOUNT)`.

## Decisions and the reasons the tutorial gives [SRC]
| Decision | Reason |
|---|---|
| `Emit(n)` instead of enabling the emitter. | Gives an exact one-time burst. |
| Colour and transparency sequences. | Particles fade naturally instead of popping out. |

## Our analysis
- **[ANALYSIS]** Emitting from a server script replicates the burst to all clients — fine for a shared event; for purely local feedback emit on the client to save bandwidth.
- **[OBS — our exercise]** Our [coin burst v1](../08-Animation-and-Game-Feel/Recipes/AV-03-Collecting.md) did not read at small size and needed a v2 with fewer, larger particles; count is not the same as readability.
- **[ANALYSIS]** The trap kills instantly with no telegraph; see [AV-22](../08-Animation-and-Game-Feel/Recipes/AV-22-Hazard-Telegraph.md).

## Common mistakes
- Leaving `Rate` > 0 → constant stream.
- Hundreds of overlapping translucent particles → overdraw.
- No sound layer.

## Troubleshooting
| Symptom | Likely cause / fix |
|---|---|
| Nothing appears | Emitter disabled? Lifetime 0? Part transparency doesn't affect particles, but `Enabled` and `Rate` do. |
| Burst looks thin | Raise size and lower count; add a flash and a shockwave layer. |

## Reusable procedure (ours)
1. Design the burst in layers: flash → core → debris → smoke.
2. One emitter per layer, Rate 0, tuned lifetime/speed/size sequences.
3. Trigger with `Emit(n)` from the correct side (server for shared events, client for local).
4. Add sound and a small camera shake for the player involved.
5. Check performance with many simultaneous bursts.

## Exercise
Build a 3-layer explosion for the 'Obsidian Rush' eruption and compare with AV-09.

### Acceptance criteria
- [ ] Reads at 25% screen size (screenshot).
- [ ] 10 simultaneous bursts keep the frame time within budget on the emulated low-end device.
- [ ] Has a sound layer.

## Related
- [AV-20 Particle System Setup](../08-Animation-and-Game-Feel/Recipes/AV-20-Particle-System-Setup.md)
- [VFX Principles and Performance](../09-VFX/VFX-Principles-and-Performance.md)
- [LU-19 VFX System](../07-Roblox-Studio-and-Luau/LU-19-VFX-System.md)
