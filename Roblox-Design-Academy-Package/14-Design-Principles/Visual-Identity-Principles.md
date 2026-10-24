---
title: "Visual Identity Principles (ID-001 – ID-006)"
tags: [principles, identity]
note_type: "principles"
---

# Visual Identity Principles (ID-001 – ID-006)

Art-direction principles for coherent, original games.

| ID | Principle | Confidence |
|---|---|---|
| ID-001 | Write an identity statement first | High |
| ID-002 | One geometric motif | High |
| ID-003 | World-to-UI consistency | High |
| ID-004 | Typography is part of identity | Medium |
| ID-005 | Borrow grammar, not skins | High |
| ID-006 | Colour grade sets genre | High |

## ID-001 — Write an identity statement first
**Rule:** Define emotional target, shape motif, palette roles, type pairing and 3–5 references before producing assets.

- **Reasoning:** Unmade decisions produce template/AI-looking results.
- **Evidence:** [Visual Identity Framework](../07-Visual-Identity/Visual-Identity-Framework.md), [UI 19 DevForum Default Template HUD](../01-UI-UX/Analyses/UI-19-DevForum-Default-Template-HUD.md)
- **Good application:** RIVALS: red mannequin + white arenas everywhere.
- **Failure mode:** Default fonts and per-element colours.
- **Conditions & exceptions:** —
- **Roblox implementation:** Identity note + Style Editor tokens + palette module.
- **Confidence:** High
- **Tags:** #identity

## ID-002 — One geometric motif
**Rule:** Choose one shape motif (chamfer, pill, hexagon, brush, stitched…) and apply it to UI and props.

- **Reasoning:** Cheapest strong identity signal.
- **Evidence:** [UI 08 BotClash Inventory Master Detail](../01-UI-UX/Analyses/UI-08-BotClash-Inventory-Master-Detail.md), [UI 22 DevForum Smash Style Buttons and Pictogram Guide](../01-UI-UX/Analyses/UI-22-DevForum-Smash-Style-Buttons-and-Pictogram-Guide.md)
- **Good application:** Chamfered tabs and buttons.
- **Failure mode:** Mixed rounded, sharp and ornamental shapes.
- **Conditions & exceptions:** —
- **Roblox implementation:** 9-slice motif images reused.
- **Confidence:** High
- **Tags:** #identity

## ID-003 — World-to-UI consistency
**Rule:** UI style derives from the world's genre and materials.

- **Reasoning:** Mismatch confuses genre (community critique).
- **Evidence:** [UI 20 DevForum Revenance Title Screen](../01-UI-UX/Analyses/UI-20-DevForum-Revenance-Title-Screen.md), [V25 Beyond The Dark Diegetic Map](../16-Video-Analyses/V25-Beyond-The-Dark-Diegetic-Map.md)
- **Good application:** Sci-fi hologram signage in a space station.
- **Failure mode:** Teal sci-fi panels over a horror street.
- **Conditions & exceptions:** —
- **Roblox implementation:** Material/texture references shared by UI and environment artists.
- **Confidence:** High
- **Tags:** #identity

## ID-004 — Typography is part of identity
**Rule:** Choose type that matches tone; vary voice via typography deliberately.

- **Reasoning:** Duvall uses handwriting vs typewriter for different voices.
- **Evidence:** [V21 V22 Duvall Cutscene and Respawn](../16-Video-Analyses/V21-V22-Duvall-Cutscene-and-Respawn.md), [TI 24 Horror Icon Cluster](../02-Thumbnails-and-Icons/Analyses/TI-24-Horror-Icon-Cluster.md)
- **Good application:** "He ate them." serif horror.
- **Failure mode:** Default font everywhere.
- **Conditions & exceptions:** Legibility first for gameplay text.
- **Roblox implementation:** `FontFace` tokens; Builder fonts are free to use.
- **Confidence:** Medium
- **Tags:** #identity #typography

## ID-005 — Borrow grammar, not skins
**Rule:** Use genre conventions (placement, symbols, mechanics) but never copy a competitor's visual style or composition.

- **Reasoning:** Conventions aid learning; copies lose identity.
- **Evidence:** [UI 10 Close Button Convention](../01-UI-UX/Analyses/UI-10-Close-Button-Convention.md), [TI 12 Template Clone Steal An Egg](../02-Thumbnails-and-Icons/Analyses/TI-12-Template-Clone-Steal-An-Egg.md), [UI 21 DevForum Overdecorated Portfolio UI](../01-UI-UX/Analyses/UI-21-DevForum-Overdecorated-Portfolio-UI.md)
- **Good application:** Four different close buttons, same meaning.
- **Failure mode:** Grow-a-Garden-lookalike stock panel.
- **Conditions & exceptions:** —
- **Roblox implementation:** Reference board notes "principle taken" per reference.
- **Confidence:** High
- **Tags:** #identity #originality

## ID-006 — Colour grade sets genre
**Rule:** Decide saturation/hue/contrast from the emotional target; keep marketing grade consistent with in-game lighting.

- **Reasoning:** Same image, three grades → three genres.
- **Evidence:** [TI 07 Colour Grade Changes Genre](../02-Thumbnails-and-Icons/Analyses/TI-07-Colour-Grade-Changes-Genre.md), [TI 04 Duvall Drive Horror Thumbnail](../02-Thumbnails-and-Icons/Analyses/TI-04-Duvall-Drive-Horror-Thumbnail.md)
- **Good application:** Horror: narrow hue, one glowing accent.
- **Failure mode:** Saturated cartoon grade on a horror game.
- **Conditions & exceptions:** —
- **Roblox implementation:** `ColorCorrectionEffect`/`ColorGradingEffect` presets per area.
- **Confidence:** High
- **Tags:** #identity #color
