---
title: "FC-BL-04 — Coins flew into the air: rotation applied around the world origin"
tags: [failure-case, blender, python, transforms]
note_type: "failure-case"
evidence: "real failure observed in this session (2026-10-24)"
---

# Coins flew into the air: rotation applied around the world origin

| Field | Record |
|---|---|
| **Problem** | Coins flew into the air: rotation applied around the world origin |
| **Context** | Cartoon chest v2: 22 coin discs created at their positions, then given random tilts with `object.rotation_euler` and `transform_apply`. |
| **Observable symptoms** | In the render, coins were scattered high above the chest. |
| **Cause (established)** | Builders create meshes in place with the **object origin at (0,0,0)**. Rotating the object rotates around the world origin, which swings the coins (whose geometry sits away from the origin) along large arcs. |
| **Correction** | Added a `tilt` parameter to `rbx_shapes.cylinder` that rotates the bmesh around its own centre **before** translating it into place. |
| **How the correction was tested** | Re-rendered v3; coins sit in a heap in the chest. |
| **Final result** | Fixed. |
| **Reusable lesson** | Know where the origin is before rotating. Rotate in mesh space around the part centre, or set the origin first. |
| **Related** | [BL-EX-04](../../06-Blender-and-3D-Assets/Exercises/BL-EX-04-Treasure-Chests.md), [BL-18](../../06-Blender-and-3D-Assets/BL-18-Technical-Troubleshooting.md) |
