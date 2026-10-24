---
title: "BL-21 — Procedural variation without sameness"
tags: [blender, procedural, variation, art-direction]
note_type: "procedure"
evidence: "rock exercise (seeds, parameters) + Roblox instancing facts"
---

# BL-21 — Procedural variation without sameness

## The trap
Seeds give infinite *different* rocks that all look *the same kind of generic*. Variation in noise is not variation in design.

## What creates meaningful variation
| Lever | Example from BL-EX-01 |
|---|---|
| **Archetype** (different silhouette families) | boulder (tall-ish mass), slab (flat, wide), cluster (group of 3 sizes) |
| **Proportion ranges** per archetype | slab `flatten=0.35` vs boulder `0.8` |
| **Facet scale** = style | `chunk` (dissolve angle) 0.35 → many small facets; 0.6 → big planes |
| **Composition** | cluster: big/medium/small in a triangle; v1's line layout hid a pebble |
| **Colour role** | cool grey vs warm grey stone for zone identity |
Seed noise comes *last*, as micro-variation inside a designed archetype.

## Roblox constraint: instancing
Every unique mesh is a separate asset and loses instancing with its siblings ([BL-16](BL-16-Performance-Budgets.md)). A good set is **3–5 archetype meshes**, varied in Studio by rotation, uniform scale and colour, not 50 unique rocks.

## Procedure
1. Design archetypes by hand or with parameters; critique each one (silhouette, 64 px read).
2. Generate 3–6 seeds per archetype and **pick** the best one. Do not ship all of them.
3. Place copies in Studio with rotation/scale variation; check the repetition from the player's height.

## Acceptance criteria
At most ~5 meshes per prop family; each archetype passes [BL-20](BL-20-Modeling-Quality-Framework.md); the scene shows no obvious repetition from normal camera positions.

## Sources
Accessed 2026-10-24. Roblox pages from the creator-docs repository (commit 4e795e6); Blender pages from the 5.2 LTS manual (the URLs use `latest`, which served 5.2 on that date).
- [Meshes (MeshPart, fidelity, name suffixes)](https://create.roblox.com/docs/parts/meshes)
- [Improve performance](https://create.roblox.com/docs/performance-optimization/improve)
