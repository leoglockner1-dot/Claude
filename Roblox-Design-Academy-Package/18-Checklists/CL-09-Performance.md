---
title: "CL-09 — Performance"
tags: [checklist, performance]
note_type: "checklist"
---

# CL-09 — Performance

Mark each item ✅ verified (write how), ❌ failed (write what), ⬜ not checked. **Never tick an item you did not check.** Distinguish verified results from assumptions in the report.

- [ ] Baseline device chosen and tested weekly
- [ ] 60 FPS budget (16.67 ms) held in heaviest scene
- [ ] Event-driven scripts; no heavy per-frame loops
- [ ] Streaming enabled; join time measured
- [ ] Particles within limits; few transparent overlaps
- [ ] Highlight count < 255 at peak
- [ ] Textures/meshes reused; materials preferred
- [ ] No server-only assets in ReplicatedStorage
- [ ] MicroProfiler capture saved for worst scene

## Based on
[Performance and Mobile](../11-Roblox-Technical-Reference/Performance-and-Mobile.md) · [Particles Lighting and Effects](../11-Roblox-Technical-Reference/Particles-Lighting-and-Effects.md)
