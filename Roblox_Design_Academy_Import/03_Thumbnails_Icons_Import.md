# Thumbnails and Icons — Import Content

**Merge into:** the `03_Thumbnails_And_Icons/` notes. The labels are the same as in [02_UI_UX_Import.md](02_UI_UX_Import.md). Specs are in [Roblox_Platform_Facts.md](Roblox_Platform_Facts.md).

---

## → Thumbnail_Principles.md

### What a thumbnail must do
A thumbnail has two jobs: get the click *and* set a truthful expectation. Roblox measures **qualified** play-through (plays that last a significant time ÷ impressions), so a misleading thumbnail that gets clicks but loses players fails by Roblox's own metric [FACT].

### Core rules
1. **One idea, one focal point.** The viewer should be able to say "it's a game where you ___" in under a second [RBX "relevant content"; OBS IMP-22, IMP-25].
2. **Show a verb or a relationship**: chase, versus, escape, reward, danger, build. Not just an object or a mood [OBS IMP-22 positive, IMP-24 negative].
3. **Theme and colour communicate genre and tone** before anything is read [RBX; OBS IMP-25, IMP-28].
4. **Nothing essential at the bottom.** Player count and other metadata can cover it [FACT].
5. **16:9 at 1920×1080.** Other ratios are stretched [FACT].
6. **Use real in-engine renders** (Freecam: Shift+P). Stock photos or vector cut-outs, as in IMP-22, set false expectations, and in *video* thumbnails they're rejected [FACT video rules].
7. **Upload 2–5 variants and keep them active.** Personalization picks per audience segment. Refresh with each major update, then leave them [FACT].

### Composition toolbox [GEN; OBS]
- **Diagonals for motion and energy**; horizontals and verticals for calm and stability [IMP-22].
- **Rim light or silhouette** separates the subject from a busy background [IMP-22].
- **Dark foreground framing** adds depth and focus [IMP-25].
- **One accent hue + muted rest.** The accent marks the focal point [IMP-25].
- **A low camera** makes subjects imposing; a high camera makes them cute or vulnerable [GEN].
- **Subject large.** It should fill roughly a third or more of the frame [HYP].
- **Faces and avatars** sell a player fantasy (who you are in this game). Most Roblox examples without a character, like IMP-22 and IMP-25, are weaker on this [OBS].

### Text on thumbnails [RBX + HYP]
- Roblox's still-image rules don't ban text, but the video rules limit overlays to gameplay context, with no ads or claims ("50% off", "Free UGC!").
- Hypothesis: 0–3 words at most, large, high contrast, never at the bottom. A logo works better on the icon than on every thumbnail.

---

## → Game_Icon_Principles.md

- **512×512 or larger, square.** It shows as small as about **150×150**, so preview it small [FACT].
- **One subject, big. Two dominant hues. Flat shapes survive downscaling best** [OBS IMP-26 small-size test: the flat camping icon was most legible and the detailed 3D theme-park render least].
- **Crop closer than feels natural.** One hero element (a character's face, one item, one vehicle), not a whole scene [OBS IMP-26].
- **The icon is the brand; thumbnails are the content.** Keep the icon stable over time so players recognise it; rotate thumbnails [GEN/HYP].
- **Never ship the default icon** [FACT + IMP-27].
- **No stickers or unexplained symbols.** If an event matters, re-theme the art [OBS IMP-27].
- **Colour grade decides genre perception** [OBS IMP-28].
- **Test in context:** put your icon in a mock grid between 10 popular icons in your genre at 150 px and 64 px. Does it stand out? Can you name the game's verb? [HYP method]

---

## → Composition_and_Focal_Points.md

A focal-point checklist that can be run on any image:
1. Squint test or blur at 10 px: what is the brightest, most saturated, highest-contrast area? It must be the subject.
2. Count the competing focal points. More than one main subject plus one secondary means it's cluttered.
3. Check the silhouette: fill the subject solid black. Is it still recognisable?
4. Edge check: nothing important touches the frame edges or the bottom strip.
5. Eye path: where does the eye go first and second? Diagonals and gaze lines should lead to the subject.
6. Value structure: does it read in greyscale? Separation should come from light and dark, not only hue.

---

## → Thumbnail_Anti_Patterns.md

| Anti-pattern | Example | Correction |
|---|---|---|
| No subject, only a mood | [IMP-23](07_Bad_Examples/IMP-23_Unclear_Thumbnail.md) | Choose one in-game moment with a verb |
| Unexplained stickers or symbols | IMP-23, [IMP-27](07_Bad_Examples/IMP-27_Icon_Failures.md) | Remove them, or integrate the event into the scene |
| Prop clutter / everything-in-frame | [IMP-24](06_Reference_Analyses/IMP-24_Comical_Theme_Thumbnail.md) | Cut every prop that doesn't support the idea |
| Generic AI illustration look | IMP-24 (my judgement) | Use in-engine renders with game-specific details and avatars |
| Not 16:9, low-res, compression artefacts | IMP-23 | Export a 1920×1080 PNG or high-quality JPG |
| Non-gameplay imagery (stock photos, other-game art) | IMP-22 | Use Freecam renders of your real game |
| Essential info at the bottom | — | Keep the bottom roughly 15% free [HYP size] |
| Default icon | IMP-27 | Custom icon before launch |

### Signs of the "AI look" (hypotheses to evaluate, not rules)
- Random symmetric prop scatter
- A background unrelated to the subject
- Over-smooth painterly lighting on everything
- Uncanny faces and hands
- Text-like gibberish
- No game-specific UI, avatar or world detail
- A generic fantasy landscape

Each one points to an image that wasn't composed with intent.
