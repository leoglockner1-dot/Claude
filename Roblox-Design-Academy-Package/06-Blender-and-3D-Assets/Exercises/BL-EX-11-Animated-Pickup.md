---
title: "BL-EX-11 — Animated pickup: spin + bob FBX export (executed)"
tags: [blender, exercise, animation, export, executed]
note_type: "exercise"
status: "executed (Blender side only)"
code: "_tools/blender/ex_extra.py (ex11)"
---

# BL-EX-11 — Animated pickup export

## Acceptance criteria
A coin with a looping spin (360° over 2 s at 30 fps) and a bob exports to FBX with baked animation; the re-imported file still contains an action with the same frame range.

## Method
Keyframes at frames 1/31/61: rotation Z 0 → π → 2π, location Z 1.5 → 1.75 → 1.5. Rotation keys set to **linear** interpolation, so the loop has no ease-in/ease-out hitch at the seam. Export via `rbx_export.export_fbx(..., animated=True)` (`bake_anim=True`, leaf bones off).

## Result
- FBX exported (27 KB): [coin_spin_bob.fbx](../../Assets/Original/Blender/BL-EX-11-Animated-Pickup/export/coin_spin_bob.fbx).
- Re-import in a fresh Blender scene: **one action, frame range 1–61**: Pass ([results](../../Assets/Original/Blender/BL-EX-11-Animated-Pickup/anim-results.json)).
- Blender 5.x stores keyframes in **layered actions** (layers → strips → channelbags → F-curves). Scripts written for 4.x that use `action.fcurves` need a fallback, as the exercise code shows. This is version-sensitive.

## Design note
For a Roblox pickup, a looping spin/bob is usually cheaper and more flexible as **TweenService or code** on the client ([LU-16](../../07-Roblox-Studio-and-Luau/LU-16-Tweens-and-Springs.md)) than as an imported animation. Use authored animation when the motion is complex (a chest opening with squash and stretch).

## Not verified
Studio import of the animation (Animation Editor / AnimationController). Studio expects one animation per FBX ([BL-13](../BL-13-Rigging-and-Animation-Export.md)).
