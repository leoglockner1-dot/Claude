---
title: "FC-BL-06 — Pivot off by 1.5 studs: matrix_world read before Blender updated it"
tags: [failure-case, blender, python, pivot]
note_type: "failure-case"
evidence: "real failure observed in this session (2026-10-24)"
---

# Pivot off by 1.5 studs: matrix_world read before Blender updated it

| Field | Record |
|---|---|
| **Problem** | Pivot off by 1.5 studs: matrix_world read before Blender updated it |
| **Context** | `rbx_exercise.center_on_origin()` moved assets so that their pivot lands on the origin, using `matrix_world`-based bounds. |
| **Observable symptoms** | QC (with pivot checks enabled in v2) reported the gem's pivot 1.5 studs from its centre. |
| **Cause (established)** | The gem builder set `ob.location.z = 1.5` immediately before centring. `matrix_world` is not recomputed until the depsgraph updates, so the bounds were stale and the correction was wrong. |
| **Correction** | Call `bpy.context.view_layer.update()` before reading bounds (also after lifting assets for renders). |
| **How the correction was tested** | Re-ran the gem (v3): pivot check PASS. |
| **Final result** | Fixed. The bug also existed in v1, unnoticed because the pivot check was off. |
| **Reusable lesson** | After changing transforms in a script, update the view layer before reading `matrix_world`. Turn on every check that applies; an unchecked property is an unknown, not a pass. |
| **Related** | [BL-EX-02](../../06-Blender-and-3D-Assets/Exercises/BL-EX-02-Collectible-Gem-and-Coin.md), [BL-19](../../06-Blender-and-3D-Assets/BL-19-Blender-Python-Automation.md) |
