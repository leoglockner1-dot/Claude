---
title: "BL-EX-08, 10, 13 — Furniture, mechanical object, stylized character (specs, NOT executed)"
tags: [blender, exercise, spec, not-executed]
note_type: "exercise"
status: "specified only — not executed in this session"
---

# Exercise specs that were not executed

These exercises are fully specified so a later agent can run them, but **no work or results exist for them yet**. Each follows the same loop as the executed exercises: criteria → v1 → inspection set + QC → ranked defects → v2 → result.

## BL-EX-08 — Furniture set (table, chair, shelf) for one interior style
- **Brief:** a cosy-cabin interior, classic avatar scale (seat height ~1.5–2 studs relative to a 5-stud avatar; check with an avatar reference).
- **Criteria:** a consistent bevel scale and colour palette across the 3 pieces; a chair silhouette readable from the gameplay camera; ≤ 800 tris per piece; pivot bottom-centre; the chair seat as a `_Att` point for sitting (`Chair_Seat_Att`); QC 0 FAIL.
- **Focus:** a *set* reads as one family through shared shape language (all edges rounded the same, the same leg profile).
- **Tools:** `rbx_shapes.box` + `bevel`; `rbx_exercise.inspect_asset`.

## BL-EX-10 — Mechanical object: lever with base (an interactable)
- **Brief:** a wall lever that players pull (ProximityPrompt).
- **Criteria:** two meshes, base and handle. The handle's origin sits **on the hinge axis**, so "pulled" is a single 45–60° rotation (tween in Studio). The on and off states are distinguishable by silhouette, plus a colour accent (green/red knob) for non-colour-blind and colour-blind readability (shape + colour). ≤ 600 tris. A `Lever_Prompt_Att` attachment for the prompt.
- **Test:** render both states, run the silhouette test on each, and verify the hinge pivot by rotating in Blender and checking that the base does not intersect.

## BL-EX-13 — Stylized character (blockout level)
- **Brief:** a non-avatar NPC (shopkeeper) for a stylized game. **Not** an avatar body (avatar items have separate specs: R15, cages and budgets in the avatar docs).
- **Criteria:** a clear silhouette and readable "role" (props like an apron or scale help); proportions chosen deliberately (head-to-body ratio documented); edge loops at the shoulders, elbows, hips and knees for deformation; ≤ 4 bone influences per vertex; root bone at the origin; idle animation exported as a single FBX track ([BL-13](../BL-13-Rigging-and-Animation-Export.md)).
- **Risk:** character art is where "generic AI look" shows most ([AI and Template Look Detection](../../15-Anti-Patterns-and-Failure-Cases/AI-and-Template-Look-Detection.md)). Build from reference and a written shape-language plan.
