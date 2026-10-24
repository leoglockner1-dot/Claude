---
title: "Research Methodology"
tags: [start-here, meta]
note_type: "start-here"
---

# Research Methodology

## Sources and how they were used
1. **Official Roblox docs** (technical facts, official design guidance, 29 videos, ~60 example images) — GitHub mirror + live site.
2. **Roblox APIs** — charts (Top Playing Now, Up-and-Coming, Top Trending, Top Revisited, genre sorts), genre searches, game metadata, votes, icons, thumbnails, game passes for 85 games.
3. **DevForum** — 30 threads where developers posted UI, thumbnails or analytics and received critique.
4. **External UX sources** — NN/g (3 articles), Apple HIG (2 pages).

## Analysis methods
- **Images:** viewed at full size and at display size (icons 150/64 px; thumbnails 320×180) in grids next to competitors. Observations written before interpretations.
- **Videos:** 12 timestamped frames per video; per-frame motion energy (mean absolute frame difference at 20–60 fps) to time events; targeted crops (e.g., health bar every 50 ms); audio RMS envelope (50 ms windows), onset detection and spectral centroid. **Audio was measured, never listened to.**
- **Economy:** pass names/prices aggregated; keyword categories; descriptive statistics only.
- **Case studies:** built from developer descriptions + marketing + passes; loops are labelled as inferred.

## Evidence labels
- **Confidence High:** directly observed or officially documented.
- **Medium:** plausible interpretation with supporting evidence.
- **Low/Hypothesis:** requires testing (e.g., recommended durations).

## Reference template
Identity → What is observable → What works → Why it might work → What does not work → Reusable principles → Roblox implementation → Original application → Confidence → Related. (Adapted per reference type.)

## Originality rule
Every analysis contains an **original application** that does not copy the reference. Never copy interfaces, compositions, characters or branding.

## Intake of new references
[CL 12 Reference Intake](../18-Checklists/CL-12-Reference-Intake.md)
