---
title: "Performance and Mobile Constraints"
tags: [technical, performance, mobile]
note_type: "technical-reference"
---

# Performance and Mobile Constraints

> **Verified** against the Roblox Creator Docs (GitHub mirror commit 4e795e6 and create.roblox.com, accessed 2026-10-24). Re-check yearly. Items marked *(recommendation)* are design advice, not engine facts.

- 60 FPS = **16.67 ms** per frame; prefer event-driven code; split long work across frames; `Parallel Luau` for heavy work. [design for performance](https://create.roblox.com/docs/performance-optimization/design)
- Choose a **baseline low-end device**, test throughout; Studio emulator is not accurate for memory.
- Illustrative budget from docs: <1,000 draw calls and <1,000,000 triangles on the baseline device (device-specific).
- Built-in materials use far less memory than custom textures; reuse meshes/textures; packages avoid duplicate assets.
- Avoid partial transparency (overdraw); instance streaming (`StreamingEnabled`, default on); SLIM avatars/LOD for crowds.
- Don't store server-only assets in `ReplicatedStorage`.
- Most users are on mobile; audience sensitive to load times. [design for Roblox](https://create.roblox.com/docs/production/game-design/design-for-roblox)
