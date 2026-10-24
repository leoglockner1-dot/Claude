---
title: "LU-23 — Performance profiling"
tags: [luau, performance, profiling, mobile]
note_type: "procedure"
evidence: "official docs"
---

# LU-23 — Performance profiling

## Purpose
Find what is actually slow (script, physics, rendering, network, memory) before optimizing, and confirm that the change helped.

## Tools (performance-optimization docs)
- **MicroProfiler** (Ctrl+F6 in Studio and client): per-frame timeline of engine and script work. Add your own labels with `debug.profilebegin("Label")` / `debug.profileend()`.
- **Developer Console** (F9): Memory (LuaHeap, InstanceCount, PlaceScriptMemory), Network, Script Profiler.
- **Render Stats** (Shift+F2 on the client): draw calls and timing.
- Test on real low-end hardware where possible; the docs have a "Test on hardware" page.

## Where time goes, and the documented fixes
| Area | Common problem (docs) | Fix (docs) |
|---|---|---|
| Script compute | Expensive work on per-frame `RunService` events; deep clones or serialization of big tables | Run frame events only when needed; split work with `task.wait()`; multithreading for data-model-free work; native code generation for some server scripts |
| Script memory | Connections never disconnected; per-player tables never cleared; Player/character objects not destroyed | [LU-20](LU-20-Signals-and-Cleanup.md) |
| Rendering | Too many **draw calls**; dense objects; decals/particles don't batch; missed **instancing** (same-looking meshes with different asset ids); `RenderFidelity = Precise` everywhere; shadows; transparency overdraw | Reuse one mesh asset id and duplicate it in Studio (import assets individually, then duplicate; do not import whole scenes); lower fidelity; fewer shadow casters; avoid layered transparency |
| Physics | Unanchored clutter; precise collision on many meshes | Anchor static parts; Box/Hull collision for props ([BL-17](../06-Blender-and-3D-Assets/BL-17-Collision-Fidelity.md)) |
| Network | Frequent large remote payloads; replicating unneeded instances | Send ids and deltas; UnreliableRemoteEvent for cosmetic streams; streaming |

## Procedure
1. Set a target (for example a stable 60 FPS on a mid-range phone, and server heartbeat stable at full player count). Measure a baseline on the target device.
2. Reproduce the slow situation (the worst-case area, the full server).
3. MicroProfiler: find the frame spikes and identify the scope (your label or an engine label).
4. Change **one** thing, then measure again under the same conditions.
5. Keep the change only if the measurement improved; write down before/after numbers.

## Common mistakes
- Optimizing Luau micro-patterns while the real cost is draw calls from a scene import.
- Measuring in Studio on a powerful PC and assuming phones behave the same.
- Removing the visuals that carry gameplay information to "save performance". Cut decorative effects first.

## Acceptance criteria
Each optimization has before/after measurements from the same device and scenario.

## References
- https://create.roblox.com/docs/performance-optimization/identify · https://create.roblox.com/docs/performance-optimization/improve · https://create.roblox.com/docs/performance-optimization/microprofiler
