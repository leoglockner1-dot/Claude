---
title: "FC-QA-01 — QA: my own checks produced false results (bounding-box coverage, exact-seam rays, open-mesh normals)"
tags: [failure-case, qa, tooling, method]
note_type: "failure-case"
evidence: "real failure observed in this session (2026-10-24)"
---

# QA: my own checks produced false results (bounding-box coverage, exact-seam rays, open-mesh normals)

| Field | Record |
|---|---|
| **Problem** | QA: my own checks produced false results (bounding-box coverage, exact-seam rays, open-mesh normals) |
| **Context** | Writing automated checks for the modular kit (BL-EX-09) and the VFX cards (BL-EX-12). |
| **Observable symptoms** | (a) A bounding-box coverage check would have reported the doorway as solid (the joined mesh's bbox spans the hole). (b) Ray samples placed exactly on a seam reported a false gap at y=10.0. (c) The 'faces pointing inward' heuristic reported 48 false WARNs on open VFX cards. |
| **Cause (established)** | Each check assumed something untrue: (a) that bboxes match the geometry, (b) that rays never hit exact shared edges, (c) that 'outside' is defined for open meshes. |
| **Correction** | (a) Ray casts against geometry. (b) Samples offset by 0.25 studs off the seams. (c) QC skips the inward check on non-manifold meshes, and `card=True` turns open-mesh checks into INFO. |
| **How the correction was tested** | A probe at 9.99 / 9.999 / 10.0 / 10.001 / 10.01 proved the artifact; the reruns show the expected results (door opening found; 0 false gaps; 0 false WARNs). |
| **Final result** | Fixed. |
| **Reusable lesson** | Validate the validator: probe edge cases of every automated check before trusting its pass or fail. |
| **Related** | [BL-EX-09](../../06-Blender-and-3D-Assets/Exercises/BL-EX-09-Modular-Building-Kit.md), [BL-EX-12](../../06-Blender-and-3D-Assets/Exercises/BL-EX-12-VFX-Geometry.md) |
