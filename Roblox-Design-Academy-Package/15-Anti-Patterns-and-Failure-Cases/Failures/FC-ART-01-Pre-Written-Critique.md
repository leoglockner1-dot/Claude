---
title: "FC-ART-01 — Process: v2 'fixes' written before looking at v1"
tags: [failure-case, process, self-critique, honesty]
note_type: "failure-case"
evidence: "real failure observed in this session (2026-10-24)"
---

# Process: v2 'fixes' written before looking at v1

| Field | Record |
|---|---|
| **Problem** | Process: v2 'fixes' written before looking at v1 |
| **Context** | Props exercise: v2 code branches with comments describing v1 defects were written before the v1 render existed. |
| **Observable symptoms** | On inspection, some pre-written 'defects' did not exist: the gem and the tree passed, and 'potato rocks' was only partly true. The real v1 defects included ones I had not predicted (ground cutting the coin and pickaxe renders, a hidden pebble in the cluster). |
| **Cause (established)** | Writing predicted critique saves time but fabricates evidence. It would have shipped notes that claimed defects nobody observed. |
| **Correction** | Rewrote the v2 branches after viewing v1: removed the unjustified changes (gem colour, tree canopy) and rewrote the comments to describe what the renders actually showed. |
| **How the correction was tested** | Each v2 change now maps to a defect visible in the v1 inspection sheet. |
| **Final result** | Notes describe observed defects only. |
| **Reusable lesson** | Critique follows evidence. Plan options in advance if useful, but label them as hypotheses until the render confirms them. |
| **Related** | [BL-EX-06](../../06-Blender-and-3D-Assets/Exercises/BL-EX-06-Stylized-Tree.md), [Self-Critique Loop](../../18-Skill-Training/Self-Critique-Loop.md) |
