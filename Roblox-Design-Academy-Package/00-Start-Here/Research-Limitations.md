---
title: "Research Limitations (read before trusting anything)"
tags: [start-here, limitations]
note_type: "start-here"
---

# Research Limitations (read before trusting anything)

## Academy 2.0 limitations (2026-10-24)
1. **Roblox Studio was not available.** No Blender import into Studio, no script, UI or effect was run in Studio. Every such step is marked *not verified*. Luau was tested with the open-source Luau CLI and mocks; engine behaviour (replication, physics, DataStore timing) was **not** exercised.
2. **Blender work is real but headless.** Exercises ran in bpy 5.2.3 with renders inspected as images. No human artist reviewed them, and "reads as a chest" judgements are the academy's own.
3. **Audio and motion previews are synthesized** (Python), measured and inspected, but not produced in-engine, and not reviewed by players.
4. **No video tutorial was watched.** YouTube is blocked; the tutorials converted are official text tutorials. Video analyses remain the v1 set of official Roblox videos.
5. **Game case studies use public data only.** Description, votes, passes and thumbnails were used, but **no game was played**. Wikipedia, Fandom and games-press sites are blocked.
6. **Two tutorial defects were reproduced in simulation,** not in a live game. They show that the logic allows the failure, not how often it happens.
7. **The BM-03 reserved zones are approximate.** They were measured by eye from one official illustration and extrapolated to tablets.
8. **Benchmarks were run by the academy itself.** No independent grader was involved; two benchmarks (thumbnail, playtest) are specifications only.
9. **Core-loop concepts are unplaytested** and labelled [HYP].

## v1 limitations (still apply)

1. **No YouTube or other gameplay video** could be analysed (bot check). Animation/VFX/audio evidence comes from **29 official Roblox docs videos** (tutorials and showcases), not from commercial games' gameplay.
2. **No game was played.** Loops of live games are inferred from descriptions, marketing and pass catalogues.
3. **Audio was not listened to** — only measured (levels, timing, spectral centroid).
4. **In-game UI of top commercial games** is represented by Roblox-docs screenshots (some 2023–2024 era) and DevForum indie projects; current in-game UI of the top 85 games was not captured.
5. **Snapshot bias:** charts captured during Halloween week 2026; popularity ≠ quality; stats are not causal evidence.
6. **DevForum metrics** are developer-reported and unverified.
7. **Level design** coverage is thin (8 references).
8. **External sources** limited to NN/g and Apple HIG; Material, FMOD, GDC Vault, Game Developer, ArtStation were inaccessible.
9. **Recommended durations** in recipes are hypotheses unless marked as measured.
10. **Images of third-party games** are included for private study; do not republish.

Full access log: [Access Log](../22-Source-Library/Access-Log.md)

## Highest-value next research (for whoever continues)
- Capture current in-game UI of 20 top games (screenshots + 10 s clips with sound) — the main gap.
- Record and measure reward reveals (eggs/crates) in 5 top simulators.
- Level-design walkthrough captures (spawn → first goal) of 10 games.
