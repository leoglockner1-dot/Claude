---
title: "Icon Failures: Default, Ambiguous Symbol, Low-Res, Not Square"
tags: [reference, thumbnail, icon, anti-pattern]
reference_type: "image-analysis"
source_ref: "IMP-27 (earlier import package)"
date_accessed: "2026-10-24"
---

# Icon Failures: Default, Ambiguous Symbol, Low-Res, Not Square

## Metadata
- Category: Icons / Bad example
- Source: Roblox Creator Docs, "Icons" > Best practices (all marked ❌)
- Asset: see images below

![IMP-27_icon-default](../../Assets/Icons/docs/IMP-27_icon-default.jpg)
![IMP-27_icon-ambiguous-symbol](../../Assets/Icons/docs/IMP-27_icon-ambiguous-symbol.jpg)
![IMP-27_icon-low-res](../../Assets/Icons/docs/IMP-27_icon-low-res.jpg)
![IMP-27_icon-not-square](../../Assets/Icons/docs/IMP-27_icon-not-square.jpg)

- Date added: 2026-10-24
- Rating: 1/5
- Confidence: High
- Reference type: Negative

## The four failures (observed)
| Failure | What it looks like | Consequence | Fix |
|---|---|---|---|
| **Default icon** | A generic castle-and-bridge landscape with a white ROBLOX wordmark | Says nothing about *this* game. Signals "unfinished" | Always upload a custom 512×512 icon before any promotion |
| **Ambiguous symbol** | A good theme-park render with a random pink snowflake in a white box top-right | Confuses the message and covers part of the subject | Remove stickers. If an event matters, theme the scene itself |
| **Low resolution** | Blurry, JPEG-blocky helicopter icon | Looks low-effort next to sharp icons | Export at 512 px or more from a larger master |
| **Not square** | The icon letterboxed with grey bars | Wasted space, unprofessional | Compose for a 1:1 square from the start |

## Better approach
[TI-05](TI-05-Icon-Theme-Set-Small-Size-Test.md) · [TI-07](TI-07-Colour-Grade-Changes-Genre.md)

## Original application
Checklist item: never ship default icon, no stickers, ≥512 px, square.

## Related
[Game Icon Principles](../Icon-Principles.md) · [Thumbnail Anti Patterns](../../12-Anti-Patterns-and-Design-Critique/Anti-Pattern-Catalog.md) · [Thumbnail Review](../../18-Checklists/CL-02-Thumbnail-and-Icon-Review.md)
