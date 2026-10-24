---
title: "BL-13 — Rigging and animation export for Roblox"
tags: [blender, rigging, animation, export]
note_type: "procedure"
evidence: "Roblox specs/export docs + a tested keyframe export (BL-EX-11)"
---

# BL-13 — Rigging and animation export for Roblox

## Roblox rules (art/modeling/specifications, export-requirements)
- Bones frozen: scale (1,1,1), rotation (0,0,0); **root bone at 0,0,0**; no influences on the root.
- **≤ 4 bone influences per vertex.** Keep symmetry where possible.
- **One animation track per FBX** export; export separate files for separate animations.
- FBX: **Add Leaf Bones off**; **Bake Animation on** only when exporting animation.
- Characters and avatar items have extra specs (R15 naming, cages). Follow the avatar pages, not this note.

## Simple mechanical rigs (doors, chests, levers, spinners)
Often you need **no armature**: export separate parts with pivots at their hinge, then animate in Studio with TweenService or the Animation Editor via Motor6Ds/joints. That is cheaper and easier to adjust.
- Put the lid's origin **on the hinge line**. In [BL-EX-04](Exercises/BL-EX-04-Treasure-Chests.md) the cartoon lid's vertices were shifted so the hinge is at the local origin, which makes "open" a single rotation.

## Rigged procedure (when deformation is needed)
1. Model in rest pose with edge loops at joints ([BL-05](BL-05-Mesh-Structure-and-Topology.md)).
2. Add an armature; root bone at the origin; apply all transforms.
3. Parent with automatic weights, then fix the weights. Limit the total to 4 per vertex (*Weights > Limit Total*).
4. Animate; one action per export.
5. Export FBX (Bake Animation on, leaf bones off); import; verify in the Animation Editor.

## Tested here
[BL-EX-11 Animated pickup](Exercises/BL-EX-11-Animated-Pickup.md) exports a keyframed spin+bob as FBX and checks that the animation survives a re-import in Blender. Studio import of that animation was **not** tested.
