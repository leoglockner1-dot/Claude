---
title: "FC-BL-03 — Fixing n-gons created non-manifold T-junctions"
tags: [failure-case, blender, topology, qc]
note_type: "failure-case"
evidence: "real failure observed in this session (2026-10-24)"
---

# Fixing n-gons created non-manifold T-junctions

| Field | Record |
|---|---|
| **Problem** | Fixing n-gons created non-manifold T-junctions |
| **Context** | Treasure chest lids built as half-cylinders. QC v1 reported n-gons on the semicircular caps. |
| **Observable symptoms** | v2 replaced each cap with a triangle fan from a centre vertex on the flat bottom edge. QC then FAILed *watertight* on every lid (6–12 non-manifold edges each). |
| **Cause (established)** | The fan's centre vertex lay on the edge shared with the bottom quad, but the bottom quad still used only the corner vertices, so a **T-junction** split one edge on one side only. |
| **Correction** | The bottom face was split into two quads that both use the fan centre vertices. The crystal base got the same fan fix, with no shared edge issue. |
| **How the correction was tested** | Full QC re-run. |
| **Final result** | All lids: 0 n-gons, 0 non-manifold edges. |
| **Reusable lesson** | A fix for one QC rule can break another. Always re-run the whole QC, and when adding a vertex on an edge, update **every** face that uses that edge. |
| **Related** | [BL-05](../../06-Blender-and-3D-Assets/BL-05-Mesh-Structure-and-Topology.md), [BL-EX-04](../../06-Blender-and-3D-Assets/Exercises/BL-EX-04-Treasure-Chests.md) |
