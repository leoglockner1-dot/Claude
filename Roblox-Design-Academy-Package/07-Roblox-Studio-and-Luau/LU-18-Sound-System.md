---
title: "LU-18 — Sound system: groups, mixing, ducking"
tags: [luau, audio, sound]
note_type: "procedure"
evidence: "official docs; not executed"
---

# LU-18 — Sound system: groups, mixing, ducking

## Purpose
A mix that players can control (music vs effects), where important sounds cut through, and where code plays sounds through one service instead of scattered `Sound:Play()` calls.

## Facts (sound/groups docs)
- `SoundGroup.Volume` is a **multiplier from 0 to 10** applied to child audio while relative volumes are kept. A 0.5 Sound in a 0.5 group plays at 0.25 effective.
- Groups can nest (Master → Music / SFX / UI / Voice).
- **Ducking:** a `CompressorSoundEffect` on a low-priority group, side-chained to a high-priority group, lowers the low-priority audio while important sounds play. The docs' example ducks music under GUI notifications.
- Roblox also documents a newer audio object API (`AudioPlayer`, `AudioEmitter`, `AudioListener`, wires). See the [Audio and Sound APIs reference](../14-Technical-Reference/Audio-and-Sound-APIs.md). Pick one stack per project.

## Procedure
1. Build the mix tree in `SoundService`: `Master` → `Music`, `SFX`, `UI`, `Ambience`, `Voice`.
2. A client `SoundController` module exposes `play(name, opts)`. It picks from variation pools, randomizes pitch by ±3–5% (house guidance against repetition fatigue), and caps concurrent instances per sound.
3. Settings sliders write to the group volumes and save them in player settings ([LU-08](LU-08-Player-Data-Persistence.md), `settings.music/sfx`).
4. Duck music under rewards and important UI with a compressor side-chain.
5. 3D sounds go on parts or attachments in the world; UI sounds play without position.

## Common mistakes
- Every sound at Volume 1, so collect sounds drown out warnings.
- The same sample replayed with no variation (fatigue in loops that fire hundreds of times).
- Critical information conveyed only by sound. The docs' accessibility page ("sound reliance") warns against this; always pair it with a visual ([V04](../21-Video-Analyses/V04-Sound-Reliance-Phone.md)).
- Creating new `Sound` instances per play without cleanup.

## Test cases
- Music slider at 0 → no music; SFX unaffected.
- 50 rapid pickups: no clipping wall of sound (the concurrency cap works); pitch variation audible.
- A reward plays while music runs: music dips and recovers.

## Acceptance criteria
All audio routed through groups; user volume settings persist; at least one ducking rule for important cues; no gameplay-critical info is audio-only.

## References
- https://create.roblox.com/docs/sound/groups · https://create.roblox.com/docs/audio · [Sound Design Principles](../10-Sound-Design/Sound-Design-Principles.md)
