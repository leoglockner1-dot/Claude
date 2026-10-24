---
title: "TUT-16 — In-game sounds and 3D audio (positional, feedback, roll-off)"
tags: [tutorial, audio, sound, 3d-audio]
note_type: "tutorial-procedure"
source: "https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/in-game-sounds"
source_author: "Roblox Creator Documentation"
licence: "Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution."
accessed: "2026-10-24"
evidence: "[SRC] = what the tutorial says; [ANALYSIS] = our reading; [SIM-TESTED] = reproduced in a Luau simulation; [HYP] = untested"
---

# TUT-16 — In-game sounds and 3D audio (positional, feedback, roll-off)

**Skill:** Place positional ambience in the world and trigger feedback sounds from scripts.

## Source and access
- Source: [https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/in-game-sounds](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/in-game-sounds) · [https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio)
- Author: Roblox (official documentation). Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution.
- Access: Read the Markdown source of the page from the public Roblox/creator-docs repository (commit 4e795e6), accessed 2026-10-24. Images, videos and the linked sample places (.rbxl) were **not** opened, and no step was performed in Roblox Studio.

## Workflow in the tutorial [SRC]
1. Positional: a `Sound` parented to a part plays from that location; set Playing + Looped; `RollOffMaxDistance = 30` and `RollOffMode = InverseTapered` for a smooth fade; `SoundGroup`s balance categories.
2. Feedback: a `Sound` in SoundService played from a LocalScript when the player touches a collectable.
3. Newer audio API (add-3D-audio page): `AudioPlayer` → `Wire` → `AudioEmitter`, heard by an `AudioListener` on the character; `DistanceAttenuation` curve `{0: 1}, {20: 0.8}, {40: 0.4}, {80: 0}`; seamless loops require matching start/end points in an audio editor.

## Decisions and the reasons the tutorial gives [SRC]
| Decision | Reason |
|---|---|
| Roll-off limits. | Without them ambience is audible across the map. |
| Feedback sound on the client. | Instant and only for the player who collected. |
| Seamless loops. | An audible loop point breaks immersion. |

## Our analysis
- **[OBS — our measurements]** Our synthesized sound set ([Measured Audio Observations](../10-Sound-Design/Measured-Audio-Observations.md)) uses the same categories; two sounds had to be corrected to their duration targets.
- **[ANALYSIS]** Repeating the same chime for every pickup causes fatigue; vary pitch slightly ([AV-18 Repetition Fatigue](../08-Animation-and-Game-Feel/Recipes/AV-18-Repetition-Fatigue.md)).
- **[ANALYSIS]** The tutorial uses specific asset IDs; we did not listen to them.

## Common mistakes
- Ambience with no roll-off.
- All sounds in one group (can't offer separate volume settings).
- Loop with a click at the seam.

## Troubleshooting
| Symptom | Likely cause / fix |
|---|---|
| Sound plays everywhere | Parented to SoundService/workspace root instead of a part; or roll-off too large. |
| Sound doesn't play | Asset not permitted for your experience, or `Playing` not set / `Play()` not called. |

## Reusable procedure (ours)
1. Classify sounds: ambience (positional loop), feedback (local one-shot), event (shared one-shot), music.
2. Put each class in its own SoundGroup.
3. Set roll-off for positional sounds; test by walking away.
4. Trigger feedback client-side; events server-side or via replication.
5. Vary pitch/volume slightly for frequent sounds.

## Exercise
Add volcano ambience (positional), a pickup chime with ±5% pitch variation, and an eruption event sound to a test place.

### Acceptance criteria
- [ ] Ambience inaudible beyond the chosen distance.
- [ ] Separate SoundGroups for music and SFX with a working volume slider.
- [ ] Ten rapid pickups don't sound identical.

## Related
- [Sound Design Principles](../10-Sound-Design/Sound-Design-Principles.md)
- [LU-18 Sound System](../07-Roblox-Studio-and-Luau/LU-18-Sound-System.md)
- [AV-16 Sound Layering](../08-Animation-and-Game-Feel/Recipes/AV-16-Sound-Layering.md)
