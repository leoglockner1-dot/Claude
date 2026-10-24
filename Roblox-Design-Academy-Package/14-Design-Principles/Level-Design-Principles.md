---
title: "Level Design Principles (LEVEL-001 – LEVEL-005)"
tags: [principles, level-design]
note_type: "principles"
---

# Level Design Principles (LEVEL-001 – LEVEL-005)

Environmental communication principles. Evidence here is thinner (no gameplay video access) — mostly Roblox docs examples.

| ID | Principle | Confidence |
|---|---|---|
| LEVEL-001 | The world teaches | High |
| LEVEL-002 | Landmarks visible from spawn | Medium |
| LEVEL-003 | Telegraph hazards in the geometry | High |
| LEVEL-004 | Mask discontinuities | High |
| LEVEL-005 | Respawn close to the failure | Medium |

## LEVEL-001 — The world teaches
**Rule:** Signs, trails, footprints and light guide players better than text.

- **Reasoning:** Roblox onboarding techniques.
- **Evidence:** [LVL 01 Jailbreak Footprint Hint](../08-Level-Design/Analyses/LVL-01-Jailbreak-Footprint-Hint.md), [ONB 01 Creatures of Sonaria Guided Trail](../09-Onboarding/Analyses/ONB-01-Creatures-of-Sonaria-Guided-Trail.md)
- **Good application:** Footprints to a vent.
- **Failure mode:** Floating text instructions everywhere.
- **Conditions & exceptions:** —
- **Roblox implementation:** Decals, `Beam`, lights.
- **Confidence:** High
- **Tags:** #level-design

## LEVEL-002 — Landmarks visible from spawn
**Rule:** Key destinations have a beacon/silhouette visible from spawn.

- **Reasoning:** Orientation at a glance.
- **Evidence:** [V13 Health Pickup](../16-Video-Analyses/V13-Health-Pickup.md)
- **Good application:** Light column over the pickup.
- **Failure mode:** Flat uniform spawn with no destination.
- **Conditions & exceptions:** —
- **Roblox implementation:** Tall light beams, unique silhouettes.
- **Confidence:** Medium
- **Tags:** #level-design

## LEVEL-003 — Telegraph hazards in the geometry
**Rule:** Hazards show their danger state before contact.

- **Reasoning:** Fair failure.
- **Evidence:** [V20 Burst Particle Trap](../16-Video-Analyses/V20-Burst-Particle-Trap.md)
- **Good application:** Sparking trap tile.
- **Failure mode:** Invisible kill bricks.
- **Conditions & exceptions:** Troll games subvert this intentionally — still teach the rule first.
- **Roblox implementation:** Idle VFX + colour coding.
- **Confidence:** High
- **Tags:** #level-design

## LEVEL-004 — Mask discontinuities
**Rule:** Hide teleports and room transitions with short fades.

- **Reasoning:** Prevents disorientation.
- **Evidence:** [V21 V22 Duvall Cutscene and Respawn](../16-Video-Analyses/V21-V22-Duvall-Cutscene-and-Respawn.md)
- **Good application:** Duvall 0.7 s respawn black.
- **Failure mode:** Pop teleports.
- **Conditions & exceptions:** —
- **Roblox implementation:** Fade frame + `PivotTo`.
- **Confidence:** High
- **Tags:** #level-design

## LEVEL-005 — Respawn close to the failure
**Rule:** Return players near where they failed unless difficulty design requires otherwise.

- **Reasoning:** Short loss keeps flow.
- **Evidence:** [V21 V22 Duvall Cutscene and Respawn](../16-Video-Analyses/V21-V22-Duvall-Cutscene-and-Respawn.md), [CS 05 Tower of Hell](../15-Game-Case-Studies/CS-05-Tower-of-Hell.md)
- **Good application:** Duvall walkway respawn.
- **Failure mode:** Long walk back after each fall in a casual game.
- **Conditions & exceptions:** Tower of Hell intentionally has "absolutely no checkpoints" — difficulty is the product.
- **Roblox implementation:** `SpawnLocation` per section / checkpoint system.
- **Confidence:** Medium
- **Tags:** #level-design
