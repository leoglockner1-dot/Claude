# Reference IMP-26 — Icon Theme Set (Roblox Examples)

## Metadata
- Category: Icons
- Source: Roblox Creator Docs, "Icons" (https://create.roblox.com/docs/production/publishing/experience-icons): "Urban action", "Camping simulation", "Peaceful ocean theme", "fun theme park setting"
- Asset: `../Assets/Icons/IMP-26_icon-action.jpg`, `../Assets/Icons/IMP-26_icon-camping.jpg`, `../Assets/Icons/IMP-26_icon-ocean.jpg`, `../Assets/Icons/IMP-26_icon-theme-park.jpg`
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

## Related Notes
[Game Icon Principles](../03_Thumbnails_And_Icons/Game_Icon_Principles.md) · [Composition and Focal Points](../03_Thumbnails_And_Icons/Composition_and_Focal_Points.md) · [Thumbnail Review](../09_Quality_Checklists/Thumbnail_Review.md)
