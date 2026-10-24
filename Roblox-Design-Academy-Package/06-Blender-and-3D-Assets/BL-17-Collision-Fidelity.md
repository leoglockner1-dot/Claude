---
title: "BL-17 — Collision fidelity"
tags: [roblox, collision, physics, performance]
note_type: "procedure"
evidence: "Roblox docs (parts/meshes)"
---

# BL-17 — Collision fidelity

## Options (`MeshPart.CollisionFidelity`, parts/meshes docs)
| Option | Shape | Use |
|---|---|---|
| **Box** | bounding box | small or non-interactive objects; cheapest |
| **Hull** | convex hull | objects with few indentations |
| **Default** | approximate, supports concavity | complex objects with semi-detailed interaction |
| **PreciseConvexDecomposition** | most precise, still not 1:1 | when exact contact matters; **most expensive**, slowest to compute |
| **Tunable** | `CollisionPrecision` slider | balance precision against cost without switching type |
Visualize with Studio's *Visualization Options > Collision fidelity*.

## Decision rules (house)
- Decoration the player never touches → set `CanCollide = false` and maybe `CanQuery = false`; fidelity is then irrelevant.
- Pickups → Box (they are triggered by touch/overlap, not walked on).
- Rocks and props you walk around → Hull.
- Rocks you walk *on* → Default (concavity matters), or simple invisible proxy parts.
- Buildings/interiors → walls as simple parts or Box meshes; avoid Precise on whole buildings.
- Chests with an opening lid → body Box/Hull, lid Hull; the treasure inside non-collidable.

## Common mistakes
- Leaving every imported mesh on Default or Precise ("it looks right"), so physics cost grows with prop count.
- Gaps between the visible mesh and Box collision that make players float or snag. Check with the visualization.

## Acceptance criteria
Every imported mesh has a deliberate fidelity (documented per asset class); visualization checked on walkable areas.

## Sources
Accessed 2026-10-24. Roblox pages from the creator-docs repository (commit 4e795e6); Blender pages from the 5.2 LTS manual (the URLs use `latest`, which served 5.2 on that date).
- [Meshes (MeshPart, fidelity, name suffixes)](https://create.roblox.com/docs/parts/meshes)
