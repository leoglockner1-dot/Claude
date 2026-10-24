---
title: "FC-BL-01 — Blender headless: EEVEE crashed without libEGL"
tags: [failure-case, blender, environment]
note_type: "failure-case"
evidence: "real failure observed in this session (2026-10-24)"
---

# Blender headless: EEVEE crashed without libEGL

| Field | Record |
|---|---|
| **Problem** | Blender headless: EEVEE crashed without libEGL |
| **Context** | Rendering inspection images with `bpy` 5.2.3 in a Linux container without a GPU. |
| **Observable symptoms** | Cycles rendered; switching to EEVEE killed the process after `Couldn't open libEGL.so.1`. |
| **Cause (established)** | EEVEE and Workbench need an OpenGL/EGL context; the container had no EGL library. |
| **Correction** | Installed `libegl1 libegl-mesa0 libgl1-mesa-dri` (software llvmpipe). EEVEE and Workbench then rendered (with harmless `EGL_BAD_MATCH` warnings). |
| **How the correction was tested** | Rendered the same test scene in all three engines and compared images. |
| **Final result** | All academy renders use EEVEE (software); ~1.5–2 min per 12-render asset set. |
| **Reusable lesson** | Probe the render engines first in a new environment; Cycles CPU is the dependency-free fallback. |
| **Related** | [BL-11](../../06-Blender-and-3D-Assets/BL-11-Lighting-and-Rendering.md), [BL-19](../../06-Blender-and-3D-Assets/BL-19-Blender-Python-Automation.md) |
