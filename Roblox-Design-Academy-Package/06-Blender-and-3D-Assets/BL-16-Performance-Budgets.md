---
title: "BL-16 — Performance budgets for 3D assets"
tags: [blender, performance, budgets, roblox]
note_type: "procedure"
evidence: "Roblox docs + exercise measurements"
---

# BL-16 — Performance budgets for 3D assets

## Hard limits (Roblox)
20,000 triangles per mesh; textures ≤ 4096². Avatar items have their own budgets.

## What actually costs frame time (performance-optimization/improve)
1. **Draw calls**, not triangles, usually dominate. Identical meshes (same asset id) with identical textures/SurfaceAppearance are **instanced**, i.e. batched.
2. Dense clusters of objects, decals, textures and particles (which batch poorly).
3. `RenderFidelity = Precise` on many meshes.
4. Shadow casting from many small parts or lights; transparency overdraw.
5. Precise collision on many meshes (physics).

## Budget guidance (house, calibrated by the exercises)
| Asset class | Measured in this academy | Suggested ceiling |
|---|---|---|
| Small pickup (gem, coin) | 32 tris (gem), 288 (coin v1) | ≤ 500 |
| Ground prop (rock) | 56–250 tris (v2: 56–164) | ≤ 800 |
| Hero prop (chest) | 1,060–1,856 tris total | ≤ 3,000 |
| Tree | 348 tris | ≤ 2,000 |
| Tool | 288 tris | ≤ 1,500 |
These ceilings are design guidance for a mobile-friendly stylized game, not platform numbers. A dense scene of 500 rocks matters more than one rock's count, and instancing matters more than either.

## Procedure
1. Set per-class budgets in the art brief.
2. QC reports triangles per mesh and per assembly.
3. Reuse meshes: build variation by rotation, scale and colour on the *same* mesh asset where possible, so it stays instanced.
4. For many small details, prefer a texture/trim sheet over geometry.
5. Measure in the target scene with Render Stats and the MicroProfiler ([LU-23](../07-Roblox-Studio-and-Luau/LU-23-Performance-Profiling.md)).

## Acceptance criteria
Each asset's triangle count is within its class budget; repeated props reuse one asset id; scene draw calls are measured on a phone profile.

## Sources
Accessed 2026-10-24. Roblox pages from the creator-docs repository (commit 4e795e6); Blender pages from the 5.2 LTS manual (the URLs use `latest`, which served 5.2 on that date).
- [Mesh specifications](https://create.roblox.com/docs/art/modeling/specifications)
- [Meshes (MeshPart, fidelity, name suffixes)](https://create.roblox.com/docs/parts/meshes)
- [Improve performance](https://create.roblox.com/docs/performance-optimization/improve)
- Blender manual: [Decimate Modifier](https://docs.blender.org/manual/en/latest/modeling/modifiers/generate/decimate.html)
