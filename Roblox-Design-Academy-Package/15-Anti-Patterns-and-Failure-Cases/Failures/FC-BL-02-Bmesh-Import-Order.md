---
title: "FC-BL-02 — pip bpy: `import bmesh` failed before `import bpy`"
tags: [failure-case, blender, python]
note_type: "failure-case"
evidence: "real failure observed in this session (2026-10-24)"
---

# pip bpy: `import bmesh` failed before `import bpy`

| Field | Record |
|---|---|
| **Problem** | pip bpy: `import bmesh` failed before `import bpy` |
| **Context** | `ex_props.py` imported `bmesh` on the line before `bpy`. |
| **Observable symptoms** | `ModuleNotFoundError: No module named 'bmesh'`. |
| **Cause (established)** | With the PyPI `bpy` module, `bmesh` (and `mathutils`) become importable only after `bpy` is imported. |
| **Correction** | Import `bpy` first in every module, with a comment explaining why. |
| **How the correction was tested** | Re-ran the props exercise. |
| **Final result** | All scripts run. |
| **Reusable lesson** | With pip `bpy`, `import bpy` must be the first Blender import. |
| **Related** | [BL-19](../../06-Blender-and-3D-Assets/BL-19-Blender-Python-Automation.md) |
