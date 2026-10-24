---
title: "FC-BL-05 — Parts placed exactly edge-to-edge showed a gap after bevels"
tags: [failure-case, blender, modeling]
note_type: "failure-case"
evidence: "real failure observed in this session (2026-10-24)"
---

# Parts placed exactly edge-to-edge showed a gap after bevels

| Field | Record |
|---|---|
| **Problem** | Parts placed exactly edge-to-edge showed a gap after bevels |
| **Context** | Cartoon chest v3: the lid hinge placed exactly on the body's back-top edge. |
| **Observable symptoms** | Side view showed the lid hovering with a visible gap behind the body. |
| **Cause (established)** | Bevels round off both touching edges, so 'exact contact' becomes two rounded edges with space between them. |
| **Correction** | Tucked the hinge 0.12 studs into the body (overlap). |
| **How the correction was tested** | v4 side render. |
| **Final result** | The lid reads as attached. |
| **Reusable lesson** | Overlap parts slightly where they meet; never rely on exact contact between bevelled parts. |
| **Related** | [BL-04](../../06-Blender-and-3D-Assets/BL-04-Hard-Surface-Modeling.md) |
