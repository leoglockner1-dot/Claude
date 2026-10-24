---
title: "LU-17 — Character and object animation"
tags: [luau, animation]
note_type: "procedure"
evidence: "official docs; not executed"
---

# LU-17 — Character and object animation

## Purpose
Play authored animations reliably on characters and rigs, sync gameplay to animation moments, and avoid the common replication and priority bugs.

## Facts (animation/using docs)
- Pattern for Humanoid rigs: get the `Animator` under the `Humanoid` → create an `Animation` with an `AnimationId` → `Animator:LoadAnimation(anim)` → `AnimationTrack:Play()`.
- Non-humanoid rigs use an `AnimationController` with an `Animator`.
- Animation **events** (markers) fire through `AnimationTrack:GetMarkerReachedSignal("Name")`. Use them to time hit frames, footstep sounds and VFX bursts.
- Default character animations can be replaced (the docs show how) and animation weights can be blended.

## Procedure
1. Author in the Animation Editor (or Blender, then import; see [BL-13](../06-Blender-and-3D-Assets/BL-13-Rigging-and-Animation-Export.md)). Add markers at gameplay moments (`Hit`, `Release`, `Footstep`).
2. Set the track priority to fit its role (Core < Idle < Movement < Action levels). Actions must outrank movement, or they get overridden.
3. Load each track **once** per character and cache it. Loading inside every input handler leaks tracks.
4. Play cosmetic animations on the client that owns the character. Animations played by a client on its own character's Animator replicate to others.
5. Gameplay effects (damage) come from the **server** on a validated request; the animation marker only times the client's request and visuals.

## Common mistakes
- Calling `LoadAnimation` on every key press.
- Using marker timing as authority for damage on the server.
- Animations not playing for others because they were played on a cloned or non-replicated rig.
- An asset permission/ownership mismatch: the animation must be owned by the experience owner or group.

## Test cases
- 2-client playtest: client A's action animation is visible on client B.
- Spam the action: the animation restarts cleanly, no stacking or leaks (watch the Developer Console memory).

## Acceptance criteria
Tracks cached per character; markers drive SFX/VFX timing; the action animation outranks movement.

## References
- https://create.roblox.com/docs/animation/using · https://create.roblox.com/docs/animation/events · [Character Animation recipes](../08-Animation-and-Game-Feel/Timing-Reference.md)
