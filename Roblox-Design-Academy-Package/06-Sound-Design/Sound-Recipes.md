---
title: "Sound Recipes for Common Roblox Interactions"
tags: [audio, recipes]
note_type: "topic"
---

# Sound Recipes for Common Roblox Interactions

Describe desired sonic characteristics (no copyrighted references). Values are starting points.

| Interaction | Character | Length | Variation | Sync | Notes |
|---|---|---|---|---|---|
| Button hover | very soft tick, high | <60 ms | none | on enter | optional on mobile (no hover) |
| Button press | soft click/pop, mid-high | 60–120 ms | ±3 % pitch | press frame | UI group |
| Confirm/purchase | bright two-note rise + coin shimmer | 300–600 ms | none | on server confirm (+ instant soft click on press) | "cha-ching" per Roblox UX doc example |
| Error/denied | short low muted thud | 150 ms | none | instant | never harsh/loud |
| Coin pickup | bright ding | 80–200 ms | pitch steps up in streaks | touch frame (client) | cap simultaneous plays |
| Rare item reveal | rising riser during anticipation → sparkle burst at reveal | 1–2 s | per rarity tier | aligned to reveal frame | rarity-specific motif |
| Level-up | ascending arpeggio + soft whoosh | 0.8–1.5 s | none | with visual pop | duck music ~30 % briefly |
| Hit (light) | short transient + material texture | 80–150 ms | 3–4 samples rotate | hit frame | louder for heavier hits |
| Hit (heavy) | low thump + crack + tail | 200–400 ms | 2–3 samples | hit frame + hit-stop | tie to camera kick |
| Damage taken | muffled low thud + quick red flash | 150–300 ms | rotate | instant | combine with V06 flash |
| Victory stinger | bright, major, rising | 1–2 s | none | screen appear | — |
| Defeat stinger | low, falling, darker | 1–2.5 s | none | screen appear | — |
| Ambient bed | low continuous texture | loop | slow modulation | starts with first visual change | fade in/out ~0.5 s |
| Hazard warning | rhythmic pulse increasing in rate | loop | rate = danger | with visual telegraph | must have visual twin |

Implementation: client-side `Sound`/audio objects for UI and local feedback; positional emitters for world events; group by Music / SFX / UI / Ambient with player sliders.
