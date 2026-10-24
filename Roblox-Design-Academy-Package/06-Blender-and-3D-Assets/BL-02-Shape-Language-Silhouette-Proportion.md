---
title: "BL-02 — Shape language, silhouette and proportion"
tags: [blender, shape-language, silhouette, proportion, art-direction]
note_type: "procedure"
evidence: "academy method + real silhouette tests (BL-EX-04, BL-EX-01..06)"
---

# BL-02 — Shape language, silhouette and proportion

## Concepts
- **Shape language:** circles and soft forms read as friendly, safe or playful; squares and boxes as stable, sturdy or dependable; triangles and points as dangerous, dynamic or sharp. This is a widely taught convention in character and prop design, not a law. Use it to support the object's *gameplay role*: a hazard should look sharp, a pickup inviting.
- **Silhouette:** the outline alone should identify the object. Players see many props at a distance, in motion and partly hidden.
- **Primary / secondary / tertiary:** big mass (60–70% of the visual weight), medium features (lid, handle, bands), small details (rivets, keyhole). Remove tertiary details first when reducing.
- **Proportion:** the relationships between parts (lid-to-body height, handle-to-head length). Stylization is a deliberate change of proportions.

## Procedure
1. Block out the primary shape only, then render a **silhouette** from the front and from the **gameplay camera** ([`rbx_scene.render_silhouette`](../_tools/blender/rbx_scene.py)).
2. If the silhouette is ambiguous, change **shape** (not detail): add a lid arch, taper the body, bend the head.
3. Add secondary shapes that break up the outline at 1–2 points (bands sticking out, a lock protruding).
4. Downscale test: 64 px and 32 px. If the object becomes a blob, increase contrast between primary masses or simplify.
5. Compare against other assets in the same game: the same bevel scale, the same exaggeration level.

## Evidence from this academy (real renders)
| Asset | Front silhouette | Gameplay-angle silhouette | Lesson |
|---|---|---|---|
| Premium chest v2–v4 | Rectangle (fails) | Clear arched-lid chest | **Judge at the gameplay angle**; a front orthographic view is the worst case |
| Open cartoon chest v4 | Reads as a bin/cup | Clear open chest | Open states change the silhouette a lot; test each state |
| Crystal cluster v1 | Spiky radial shape | Spiky radial | Pointed shapes = "crystal/danger" immediately; passed |
| Boulder v1 | Even oval/egg | Oval | Too smooth an outline → reads as a potato; needs bigger planes |
See [BL-EX-04](Exercises/BL-EX-04-Treasure-Chests.md) and [BL-EX-01](Exercises/BL-EX-01-Stylized-Rocks.md).

## Common mistakes
- Fixing an ambiguous read with detail (rivets, textures) instead of shape.
- Making everything the same size of detail, which reads as noise.
- Copying a famous game's silhouette for an "instant read".

## Acceptance criteria
The silhouette at the gameplay angle identifies the object to someone who was not told what it is; the 64 px version is still distinct from the neighbouring assets in the same set.
