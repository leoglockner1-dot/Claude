# LIVE-00 — Roblox Chart Snapshot, 2026-10-24 (Halloween season)

## Method
- **Data:** official Roblox web APIs, fetched 2026-10-24:
  - `apis.roblox.com/explore-api/v1/get-sorts` (device = all, country = all), which supplies the charts
  - `games.roblox.com/v1/games` for details
  - `thumbnails.roblox.com` for the current icon (512×512) and every detail-page thumbnail (768×432)
- **Sample:** 46 games: the top 22 of *Top Playing Now*, 12 of *Up-and-Coming*, 8 of *Top Trending* and 4 of *Top Revisited*, with duplicates removed. 46 icons and 222 thumbnails, all downloaded.
- **Viewing:**
  - icons at **150 px and 64 px** in a dark grid (the home-page context)
  - lead thumbnails at 320×180
  - the full 10-thumbnail sets of Dress To Impress and RIVALS
- **Not seen:** personalized home-page thumbnails (each viewer may get a different one), video thumbnails, in-game UI, gameplay, audio.
- **Snapshot bias:** this is **Halloween week**. Seasonal tags and pumpkins are temporary, and *The Hollow* is a Roblox-run crossover event. Re-take the snapshot in another season before generalizing seasonal findings.
- **Images:** delivered privately as `LIVE_2026-10-24_assets.zip`, not in the public repo. Unzip it into the academy root and it adds `Assets/Icons/LIVE/`, `Assets/Thumbnails/LIVE/` and `Assets/Thumbnails/LIVE/_sheets/`. Files are named `<universeId>.jpg` for icons and `<universeId>_<nn>.jpg` for thumbnails, where `_00` is the first thumbnail.
- **Stats** are a single moment in time (CCU = concurrent players; Like% = up ÷ (up + down)). They describe the sample, **not** cause and effect. Nothing here proves a thumbnail *caused* success.

## Sample
| # | Game | Chart | Genre | Subgenre | Playing | Visits | Like% | Thumbs |
|---|---|---|---|---|---|---|---|---|
| 1 | Murder Mystery 2 | top-trending | Survival | 1 vs All | 1,535,981 | 31,700,820,335 | 91% | 3 |
| 2 | [NEW STAGES]  DONT SPLASH 🎃 | top-trending | Obby & Platformer | Runner | 88,213 | 21,905,250 | 89% | 3 |
| 3 | [🎃 NEW QUEST] Dress To Impress | top-trending | Roleplay & Avatar Sim | Dress Up | 207,547 | 11,227,664,379 | 91% | 10 |
| 4 | DOORS 🍬🍭 | top-trending | Survival | Escape | 119,319 | 7,941,275,569 | 93% | 9 |
| 5 | The Hollow | top-trending | Entertainment | Showcase & Hub | 36,508 | 50,111,577 | 84% | 2 |
| 6 | Cat Battles 🐾 | top-trending | Action | Battlegrounds & Fighting | 68,383 | 63,183,796 | 73% | 4 |
| 7 | 🎃 Sell Fries! [Anomaly] 🍟 | top-trending | Survival | – | 75,326 | 64,193,448 | 84% | 1 |
| 8 | [🎃] Bike Universe | top-trending | Simulation | Vehicle Sim | 63,825 | 20,327,788 | 85% | 2 |
| 9 | [NOW] Ragdoll Reality 🩸 | up-and-coming | Simulation | Physics Sim | 58,458 | 6,222,809 | 82% | 1 |
| 10 | Backseat Rally | up-and-coming | – | – | 50,418 | 23,999,717 | 92% | 4 |
| 11 | +1 Dance Battle Evolution | up-and-coming | Simulation | Incremental Simulator | 23,901 | 6,277,363 | 88% | 6 |
| 12 | [🌍WORLD 2] +1 Venom Evolution | up-and-coming | Simulation | Incremental Simulator | 31,313 | 10,795,332 | 97% | 2 |
| 13 | Adopt Your Animal! | up-and-coming | – | – | 18,385 | 2,314,876 | 87% | 5 |
| 14 | Steel Fighters | up-and-coming | Simulation | Tycoon | 32,812 | 7,618,125 | 91% | 3 |
| 15 | DIVINE HATCHERS 0.0001% [NEW!] | up-and-coming | Simulation | Tycoon | 21,638 | 20,315,010 | 92% | 1 |
| 16 | Clone Baby Care (Anomaly) | up-and-coming | Survival | – | 29,986 | 12,914,303 | 88% | 4 |
| 17 | [🎃] Bike For Egg! | up-and-coming | Simulation | Tycoon | 26,751 | 18,440,538 | 95% | 5 |
| 18 | [UPD] Something is Wrong With My Dog... | up-and-coming | Adventure | Story | 23,502 | 4,647,918 | 76% | 5 |
| 19 | [🎃EVENT] Solve The Cube | up-and-coming | Puzzle | – | 2,040 | 9,043,596 | 82% | 4 |
| 20 | +1 Slinky Escape | up-and-coming | Simulation | Incremental Simulator | 13,987 | 4,203,203 | 80% | 1 |
| 21 | Steal An Egg | top-playing-now | Simulation | Tycoon | 1,343,038 | 9,329,214,875 | 92% | 4 |
| 22 | [🎵] +1 Speed Keyboard Escape / Candy & Chocolate | top-playing-now | Simulation | Incremental Simulator | 1,322,226 | 6,569,956,397 | 97% | 3 |
| 23 | Brookhaven 🏡RP | top-playing-now | Roleplay & Avatar Sim | Life | 641,277 | 88,854,634,783 | 86% | 9 |
| 24 | 99 Nights in the Forest 🔦 | top-playing-now | Survival | – | 457,487 | 30,230,571,754 | 90% | 3 |
| 25 | [💀] Steal a Brainrot | top-playing-now | Simulation | Tycoon | 334,375 | 74,123,197,115 | 85% | 4 |
| 26 | [HIRED KILLER] Jujutsu Shenanigans | top-playing-now | Action | Battlegrounds & Fighting | 326,691 | 7,742,229,395 | 86% | 4 |
| 27 | [🎃] Adopt Me! | top-playing-now | Roleplay & Avatar Sim | Pet Care | 279,332 | 45,198,800,546 | 86% | 6 |
| 28 | [🎃] RIVALS | top-playing-now | Shooter | Deathmatch Shooter | 255,533 | 18,932,197,643 | 94% | 10 |
| 29 | Blox Fruits | top-playing-now | RPG | Action RPG | 203,877 | 65,085,038,163 | 92% | 8 |
| 30 | 🎃 Dandy's World [ALPHA] | top-playing-now | Survival | Escape | 157,863 | 7,769,641,390 | 88% | 10 |
| 31 | Fisch 👻 [HORSEMAN] | top-playing-now | Simulation | – | 116,857 | 5,060,151,499 | 91% | 10 |
| 32 | [BUTCHER x 🎃] Violence District | top-playing-now | Survival | 1 vs All | 115,827 | 1,618,036,673 | 93% | 5 |
| 33 | Catalog Avatar Creator | top-playing-now | Shopping | Avatar Shopping | 94,342 | 8,171,291,957 | 94% | 8 |
| 34 | [X2🎃DUELS] Murderers VS Sheriffs | top-playing-now | Action | Battlegrounds & Fighting | 91,076 | 1,985,193,281 | 87% | 2 |
| 35 | 🎉 [PSX] Pet Simulator 99! 🐾 | top-playing-now | Simulation | Incremental Simulator | 89,523 | 2,679,754,192 | 95% | 4 |
| 36 | Berry Avenue 🏠 RP | top-playing-now | Roleplay & Avatar Sim | Life | 81,570 | 8,893,551,464 | 86% | 10 |
| 37 | [UPD] Volleyball Legends | top-playing-now | Sports & Racing | Sports | 80,691 | 4,031,303,498 | 95% | 10 |
| 38 | [🎃] Anime Dice | top-playing-now | Simulation | Incremental Simulator | 77,813 | 130,991,268 | 99% | 2 |
| 39 | [6 HRS] Fish It! 🐟 | top-playing-now | Simulation | Incremental Simulator | 77,131 | 4,797,505,590 | 83% | 9 |
| 40 | [🎃] Huss Valley | top-playing-now | Action | Battlegrounds & Fighting | 72,078 | 189,358,605 | 88% | 1 |
| 41 | [1.5x 🎃HLWN] Evade | top-playing-now | Survival | – | 72,071 | 9,370,628,228 | 94% | 9 |
| 42 | [UPDATE!] Illegal Soccer | top-playing-now | Sports & Racing | Sports | 67,296 | 230,386,684 | 86% | 7 |
| 43 | [⌛] Bloodlines | top-revisited | RPG | Action RPG | 9,285 | 66,921,492 | 82% | 2 |
| 44 | TYPER TOWN - [ OFFICIAL ] | top-revisited | – | – | 1,011 | 486,988 | 97% | 1 |
| 45 | [🤹APRIL FOOL'S🤡] Anime Adventures | top-revisited | Strategy | Tower Defense | 29,587 | 2,520,163,804 | 92% | 1 |
| 46 | Forest Market | top-revisited | Simulation | – | 3,560 | 10,635,413 | 95% | 5 |

## Key findings (details in LIVE-01…LIVE-13)

### Icons
1. **Countdown icons are a dominant live-ops convention right now.** 12 of 46 icons (26%) show a white hourglass or a big word ("NOW", "NOW!", "24 HOUR", "6 HOURS", "30 MINS") over darkened art. That includes giants like Steal a Brainrot and Fish It! At 64 px they look nearly identical. → [LIVE-04](LIVE-04_Countdown_Icon_Convention.md)
2. **The icons that read best at 64 px** are one face or object filling the frame with high contrast: RIVALS (red hand on white), 99 Nights (red-eyed creature on red), Pet Simulator 99 (flat cat face), Adopt Me! (dragon face plus wordmark), MM2 (abstract logo on black). → [LIVE-10](LIVE-10_Small_Size_Champions.md)
3. **The weakest at 64 px** are dark, busy or low-contrast: Fisch, Violence District, Bloodlines, Clone Baby Care. → [LIVE-12](LIVE-12_Weak_At_Small_Size.md)
4. **The dominant art style** is a close-up 3D render of a Roblox avatar or character, with an exaggerated expression, saturated colour and strong rim light. Distinct exceptions: RIVALS (minimal red mannequin), MM2 (logo), Jujutsu Shenanigans (pencil sketch thumbnail), Bloodlines (sepia anime).

### Thumbnails
5. **Number and odds bait:** "$997,151,167/s", "0.00001%", "1 in 9,342,584", "+7M", "$676767p/s". Big numbers act as a promise of escalation in incremental and gacha genres. → [LIVE-08](LIVE-08_Number_and_Odds_Bait.md)
6. **Template cloning is visible.** *Bike For Egg!* (created 2026-09-15) reuses the *Steal An Egg* (created 2026-07-25) thumbnail formula almost exactly. → [LIVE-05](LIVE-05_Template_Clone_Steal_An_Egg.md)
7. **Before/after splits** show the progression fantasy in one image (+1 Venom Evolution, +1 Dance Battle). → [LIVE-09](LIVE-09_Before_After_Split.md)
8. **First-person framing** puts the viewer in the role (Backseat Rally, Adopt Your Animal!, Anime Dice). → [LIVE-13](LIVE-13_First_Person_Framing.md)
9. **The strongest brand system:** RIVALS. Icon and all 10 thumbnails share one visual rule (red faceless mannequin + one weapon + white or grey arena). → [LIVE-01](LIVE-01_RIVALS_Brand_System.md)
10. **Storytelling in one frame:** 99 Nights in the Forest (sleeping avatar, campfire, monster behind). → [LIVE-02](LIVE-02_99_Nights_Story_Thumbnail.md)
11. **Event framing:** *The Hollow* crossover puts a red frame and logo on participating games. That's shared visibility, and it shows that brand overlays are accepted when they mean something. → [LIVE-07](LIVE-07_The_Hollow_Event_Frame.md)
12. **Maintenance failures exist even at the top:**
    - Dress To Impress has its Halloween thumbnail **twice** and still keeps summer and Christmas images active → [LIVE-06](LIVE-06_Dress_To_Impress_Thumbnail_Set.md)
    - Typer Town's thumbnail is a **grey placeholder** → [LIVE-11](LIVE-11_Placeholder_Thumbnail.md)
    - Divine Hatchers' icon says "0.0001%" while its thumbnail says "0.00001%" → [LIVE-08](LIVE-08_Number_and_Odds_Bait.md)

### Names (observation; not a design rule)
13. **29 of 46 names carry a bracket tag** ([🎃], [UPD], [NEW STAGES], [6 HRS], [X2 DUELS]…) to signal freshness or events. The game name has become a live-ops channel. Treat this as a platform convention to *consider*, not proof that it works.

## What this changes in the academy
- Add **"design the icon so it survives a temporary countdown overlay"** to [Game Icon Principles](../03_Thumbnails_And_Icons/Game_Icon_Principles.md) (LIVE-04).
- Add **"thumbnail-set hygiene"** (no duplicates, retire out-of-season art) to the [Thumbnail Review](../09_Quality_Checklists/Thumbnail_Review.md) (LIVE-06, LIVE-11).
- Add **"one visual rule across icon + all thumbnails"** to [Thumbnail Principles](../03_Thumbnails_And_Icons/Thumbnail_Principles.md) (LIVE-01).
- Update [Thumbnail Anti-Patterns](../03_Thumbnails_And_Icons/Thumbnail_Anti_Patterns.md) with template cloning (LIVE-05) and the numeric-claims caution (LIVE-08).
