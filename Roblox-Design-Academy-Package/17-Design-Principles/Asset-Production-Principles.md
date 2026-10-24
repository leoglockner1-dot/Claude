---
title: "Asset Production Principles (ASSET-001 – ASSET-010)"
tags: [principles, asset]
note_type: "principles"
---

# Asset Production Principles (ASSET-001 – ASSET-010)

Principles for 3D assets, derived from the executed Blender exercises (evidence linked) and Roblox docs.

| ID | Principle | Confidence |
|---|---|---|
| ASSET-001 | Judge four categories separately | Medium-high |
| ASSET-002 | Silhouette at the gameplay angle | Medium-high |
| ASSET-003 | Identity comes from 2–3 features | Medium-high |
| ASSET-004 | Facet scale defines stylization | Medium-high |
| ASSET-005 | Overlap, don't touch | Medium-high |
| ASSET-006 | Pivot by role | Medium-high |
| ASSET-007 | Few archetypes, instanced | Medium-high |
| ASSET-008 | One material per mesh: split or palette | Medium-high |
| ASSET-009 | Inspect what you'd see in game | Medium-high |
| ASSET-010 | Treat cards as a documented exception | Medium-high |

## ASSET-001 — Judge four categories separately
**Rule:** Rate visual, geometry, presentation and Roblox integration quality separately; the overall result is the lowest one.

- **Reasoning:** A beautiful render can hide broken geometry or a wrong pivot.
- **Evidence:** [BL-20](../06-Blender-and-3D-Assets/BL-20-Modeling-Quality-Framework.md); exercise logs.
- **Good application:** Chest v4: visual pass at the gameplay angle, QC 0 FAIL, Studio unverified (stated).
- **Failure mode:** Approving an asset from a hero render.
- **Conditions & exceptions:** —
- **Roblox implementation:** Inspection set + rbx_qc + Studio import check.

## ASSET-002 — Silhouette at the gameplay angle
**Rule:** Test silhouettes from the elevated 3/4 camera players actually use, not only in front orthographic view.

- **Reasoning:** The front view is the worst case and misjudges some designs.
- **Evidence:** [BL-EX-04](../06-Blender-and-3D-Assets/Exercises/BL-EX-04-Treasure-Chests.md) front vs gameplay silhouettes.
- **Good application:** Premium chest reads at 3/4.
- **Failure mode:** Redesigning a chest that already reads in play.
- **Conditions & exceptions:** First-person or top-down games use their own camera.
- **Roblox implementation:** `render_silhouette(view='gameplay')`.

## ASSET-003 — Identity comes from 2–3 features
**Rule:** Name the 2–3 features that make an object recognizable and protect them through every iteration.

- **Reasoning:** Removing one feature breaks the read faster than detail can restore it.
- **Evidence:** Premium chest v1 (flat lid) read as a crate.
- **Good application:** Arched lid + brackets + lock.
- **Failure mode:** Adding rivets to fix an ambiguous silhouette.
- **Conditions & exceptions:** —
- **Roblox implementation:** Write them in the asset brief ([BL-01](../06-Blender-and-3D-Assets/BL-01-Reference-Gathering.md)).

## ASSET-004 — Facet scale defines stylization
**Rule:** Control facet size deliberately; fewer, larger planes often read as more stylized than more polygons.

- **Reasoning:** Rock v1 (204 tris, small facets) read worse than v2 (56 tris, big planes).
- **Evidence:** [BL-EX-01](../06-Blender-and-3D-Assets/Exercises/BL-EX-01-Stylized-Rocks.md).
- **Good application:** Planar decimate / limited dissolve.
- **Failure mode:** Uniform tiny facets (low-poly sphere look).
- **Conditions & exceptions:** Realistic styles use smooth shading instead.
- **Roblox implementation:** `rbx_shapes.rock(chunk=...)`.

## ASSET-005 — Overlap, don't touch
**Rule:** Where bevelled parts meet, overlap them slightly instead of placing them in exact contact.

- **Reasoning:** Bevels round both edges and open a visible gap.
- **Evidence:** [FC-BL-05](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-BL-05-Exact-Contact-Leaves-Gap.md).
- **Good application:** Hinge tucked 0.12 studs into the body.
- **Failure mode:** Floating lids and trims.
- **Conditions & exceptions:** Watertight single meshes: build as one profile instead ([BL-EX-09](../06-Blender-and-3D-Assets/Exercises/BL-EX-09-Modular-Building-Kit.md)).
- **Roblox implementation:** —

## ASSET-006 — Pivot by role
**Rule:** Set the origin where the object is used: base for props, centre for spinners, grip for tools, hinge line for moving parts.

- **Reasoning:** Correct pivots make placement and animation single operations.
- **Evidence:** [BL-14](../06-Blender-and-3D-Assets/BL-14-Roblox-Import-Scale-and-Pivots.md).
- **Good application:** Cartoon lid opens with one rotation.
- **Failure mode:** Pivot at the bounding-box centre of an open-lid chest.
- **Conditions & exceptions:** —
- **Roblox implementation:** QC pivot check; assembly pivot on the body footprint.

## ASSET-007 — Few archetypes, instanced
**Rule:** Ship 3–5 well-designed archetype meshes per prop family and vary them in Studio, instead of dozens of unique meshes.

- **Reasoning:** Identical meshes with identical textures are instanced into fewer draw calls (Roblox docs).
- **Evidence:** [BL-21](../06-Blender-and-3D-Assets/BL-21-Procedural-Variation.md); performance-optimization/improve.
- **Good application:** Kit room = 16 objects, 4 meshes.
- **Failure mode:** 50 unique rocks from seeds.
- **Conditions & exceptions:** Hero props can be unique.
- **Roblox implementation:** Import once, duplicate in Studio ([LU-26](../07-Roblox-Studio-and-Luau/LU-26-Asset-Import-and-Organization.md)).

## ASSET-008 — One material per mesh: split or palette
**Rule:** Respect Roblox's one-material rule by splitting meshes by material role, or by using a palette texture; choose by whether surface response matters.

- **Reasoning:** Palette keeps colours (Δ1.8/255) but loses per-part metal/roughness.
- **Evidence:** [BL-EX-07](../06-Blender-and-3D-Assets/Exercises/BL-EX-07-Palette-Single-Material.md).
- **Good application:** Palette for small props; split for hero chests.
- **Failure mode:** Exporting a multi-material mesh.
- **Conditions & exceptions:** —
- **Roblox implementation:** `palette_convert`; QC material slots.

## ASSET-009 — Inspect what you'd see in game
**Rule:** Inspection renders must not hide defects: lift non-base pivots off the ground, use neutral light, include wireframe and small-size views.

- **Reasoning:** The ground hid half the coin; dramatic lighting hides flat albedo.
- **Evidence:** [BL-11](../06-Blender-and-3D-Assets/BL-11-Lighting-and-Rendering.md).
- **Good application:** Standard inspection set per asset.
- **Failure mode:** Judging from a cropped hero shot.
- **Conditions & exceptions:** —
- **Roblox implementation:** `rbx_exercise.inspect_asset`.

## ASSET-010 — Treat cards as a documented exception
**Rule:** Solid props follow the watertight/volume spec; planar cards (VFX, foliage) are an intentional exception with DoubleSided where needed.

- **Reasoning:** Roblox's own environment-art sample uses planar foliage with DoubleSided.
- **Evidence:** [BL-EX-12](../06-Blender-and-3D-Assets/Exercises/BL-EX-12-VFX-Geometry.md); assemble-an-asset-library docs.
- **Good application:** QC `card=True`.
- **Failure mode:** Forcing thickness onto VFX ribbons, or ignoring the spec for solid props.
- **Conditions & exceptions:** —
- **Roblox implementation:** MeshPart.DoubleSided (renders twice; use sparingly).
