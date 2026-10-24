---
title: "Unclear Thumbnail and Non-16:9 Upload (Roblox Negative Examples)"
tags: [reference, thumbnail, icon, anti-pattern]
reference_type: "image-analysis"
source_ref: "IMP-23 (earlier import package)"
date_accessed: "2026-10-24"
---

# Unclear Thumbnail and Non-16:9 Upload (Roblox Negative Examples)

## Metadata
- Category: Thumbnails / Bad example
- Source: Roblox Creator Docs, "Thumbnails" > Best practices (marked ❌ "Unclear imagery and ambiguous graphic in top-right corner" and ❌ "not in 16:9; displayed thumbnail stretched")
- Asset: see images below

![IMP-23_unclear-thumbnail](../../Assets/Thumbnails/docs/IMP-23_unclear-thumbnail.jpg)
![IMP-23_not-16-9-stretched](../../Assets/Thumbnails/docs/IMP-23_not-16-9-stretched.jpg)

- Date added: 2026-10-24
- Rating: 1/5
- Confidence: High
- Reference type: Negative

## Context
A low-angle photo of a skyscraper in fog, with heavy radial motion blur and visible posterization and compression artefacts. Grey-blue monochrome. A white square in the top-right holds a pink-purple snowflake.


## Observation of the second image (non-16:9 upload, viewed 2026-10-24)
"Elemental Academy" title in a white serif font with a dark outline, over an abstract kaleidoscope of orange fire and blue lightning. The letterforms are visibly **stretched horizontally**: Roblox displays uploads at 16:9 and distorts other ratios. The image is also **text-only key art over an abstract pattern**: it shows no game world, no character and no verb. It fails THUMB-002 even before the distortion.

## What Does Not Work
- **No subject.** A building with no story, no character, no action.
- **No genre signal.** Racing? Horror? City sim? The viewer can't tell.
- **An unexplained graphic.** The snowflake in a white box doesn't relate to anything. Is it a logo? A winter event? It also breaks the colour scheme.
- **Technical artefacts**: banding and blockiness, which read as low effort.
- Second asset: a non-16:9 upload gets **stretched** by Roblox. Distorted proportions also read as amateur.

## Why it fails, and when it's harmful
Thumbnails compete in a grid of dozens. Without a focal point and genre cue, the image adds nothing to the title, so it's skipped. It hurts most for new games with no brand recognition.

## Correction
Pick one in-game moment that shows the verb (escape, race, build…). Render it in-engine at 1920×1080 with one focal point and one accent colour. If you need a badge for an event, integrate it into the scene (snow, decorations) rather than pasting a sticker.

## Better approach
[TI-04](TI-04-Duvall-Drive-Horror-Thumbnail.md) (one focal point, framing) · [TI-01](TI-01-Urban-Rush-Action-Thumbnail.md) (clear action)

## Original application
Replace a vague skyline with one in-game moment showing the core verb and one accent colour.

## Related
[Thumbnail Anti Patterns](../../12-Anti-Patterns-and-Design-Critique/Anti-Pattern-Catalog.md) · [Thumbnail Review](../../18-Checklists/CL-02-Thumbnail-and-Icon-Review.md)
