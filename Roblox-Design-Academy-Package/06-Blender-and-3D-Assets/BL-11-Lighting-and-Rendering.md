---
title: "BL-11 — Lighting and rendering: inspection vs presentation"
tags: [blender, rendering, lighting, presentation, evidence]
note_type: "procedure"
evidence: "implemented and used (rbx_scene.py)"
---

# BL-11 — Lighting and rendering: inspection vs presentation

## Two kinds of render
| | Inspection render | Presentation render |
|---|---|---|
| Purpose | Find defects; prove quality | Communicate the asset (thumbnail, portfolio, review) |
| Camera | Orthographic front/side/top + perspective 3/4 at fixed distance | Chosen hero angle, lens, crop |
| Light | Neutral 3-point, identical for all assets | Mood lighting allowed |
| Extras | Wire over clay, silhouette, downscaled sizes | Background, props, depth |
| Rule | **Always made** | Optional, never a replacement |

## The academy's standard set (`rbx_exercise.inspect_asset`)
`_front`, `_side`, `_top`, `_threequarter`, `_wire` (wire over neutral clay), `_silhouette` (front), `_silhouette_gameplay` (elevated 3/4), `_sizes` (512/150/64/32 px), plus QC JSON and exports.

## Lighting recipe (implemented in `three_point_lights`)
- Key: warm sun, 50° elevation from the upper left.
- Fill: cool, 35% of the key, from the right.
- Rim: from behind, 80% of the key, to separate the silhouette from the background.
- Background: neutral mid-grey that does not match the asset's main hue.
- View transform **Standard** rather than AgX for predictable stylized colours. (AgX is a filmic transform that desaturates highlights; useful for realism, misleading for flat palette checks.)

## Engines (verified headless, Blender 5.2.3)
- **EEVEE**: fast; it needs an EGL/OpenGL context. Headless Linux needed `libegl1` + Mesa (software llvmpipe) installed. It is slow in software: about 12 renders per asset took ~1.5–2 min.
- **Workbench**: flat/solid preview; same EGL requirement.
- **Cycles (CPU)**: works with no GPU or EGL; slower per sample, physically based.
See [FC-BL-01](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-BL-01-Headless-EEVEE-Needs-EGL.md).

## Presentation pitfalls
- A dramatic low angle and heavy depth of field hide proportion problems.
- Coloured rim lights hide flat albedo.
- Cropping hides the base (pivot and ground contact problems).
- **Ground cuts through assets whose pivot is not at the base** (coins, tools). Lift them for renders. This was a real defect in BL-EX-02/05 v1.

## Acceptance criteria
Every asset note contains the inspection set; presentation renders are labelled as such.
