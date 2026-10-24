---
title: "Icon Theme Set (Roblox Examples)"
tags: [reference, thumbnail, icon]
reference_type: "image-analysis"
source_ref: "IMP-26 (earlier import package)"
date_accessed: "2026-10-24"
---

# Icon Theme Set (Roblox Examples)

## Metadata
- Category: Icons
- Source: Roblox Creator Docs, "Icons" (https://create.roblox.com/docs/production/publishing/experience-icons): "Urban action", "Camping simulation", "Peaceful ocean theme", "fun theme park setting"
- Asset: see images below

![IMP-26_icon-action](../../Assets/Icons/docs/IMP-26_icon-action.jpg)
![IMP-26_icon-camping](../../Assets/Icons/docs/IMP-26_icon-camping.jpg)
![IMP-26_icon-ocean](../../Assets/Icons/docs/IMP-26_icon-ocean.jpg)
![IMP-26_icon-theme-park](../../Assets/Icons/docs/IMP-26_icon-theme-park.jpg)

- Date added: 2026-10-24
- Rating: see each entry below
- Confidence: High. Each was viewed at about 250 px and at 150 px (the documented small size).
- Reference type: Positive (comparison)

## Small-size test (150×150) — observed
| Icon | Holds up at 150 px? | Why |
|---|---|---|
| Action (red-glow helicopter silhouette over light trails) | ✅ Yes | One silhouette, high contrast, glow halo |
| Camping (flat vector orange tent, teal mountains) | ✅✅ Best | Three flat shapes, complementary orange and teal, no fine detail |
| Ocean (flat dolphins, waves, rainbow) | ✅ Mostly | Dolphins get small, but the colour story ("calm sea") survives |
| Theme park (3D Roblox render of a rollercoaster) | ⚠️ Partly | Loops survive, the riders become specks. Busy |

## Reusable Design Rules
1. **One subject, large, centred or on a strong diagonal.** Icons are viewed at 150 px or less.
2. **Flat shapes and two dominant hues** survive downscaling better than detailed renders.
3. A 3D render icon needs a **cropped, close camera** on one hero element (one cart and its riders, not the whole park).
4. Always test icons at 150 px and about 64 px next to other icons. Distinctiveness is judged *in the grid*, not alone.

## Original application
Design the icon as a single bold subject that survives at 64 px; test it in a grid of genre competitors.

## Related
[Game Icon Principles](../Icon-Principles.md) · [Composition and Focal Points](../Composition-Checklist.md) · [Thumbnail Review](../../18-Checklists/CL-02-Thumbnail-and-Icon-Review.md)
