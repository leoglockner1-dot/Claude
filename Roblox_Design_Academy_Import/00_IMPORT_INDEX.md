# Roblox Design Academy — Import Package Index

- **Prepared:** 2026-10-24, in a separate cloud Claude session, for the Claude that maintains the Obsidian vault.
- **Purpose:** add researched, source-backed knowledge and 28 analyzed visual references to the existing `Roblox Design Academy` folder.
- **Rule:** merge into existing notes, **never overwrite** them. Where this package conflicts with an existing rule, keep both and record the conflict in `08_Lessons_Learned/` for the user to decide.

## What's inside

| Package file | Merge target in the vault | Content |
|---|---|---|
| [Sources.md](Sources.md) | `Sources.md` at the academy root (create it or append) | Every source with URL, access date and license; what could **not** be accessed |
| [Roblox_Platform_Facts.md](Roblox_Platform_Facts.md) | Copy as `Roblox_Platform_Facts.md` at the academy root and link it from `00_START_HERE.md` | Verified specs: thumbnail and icon sizes, safe areas, accessibility settings, particle limits, odds policy… |
| [01_Visual_Design_Import.md](01_Visual_Design_Import.md) | `01_Visual_Design_Principles.md` | Identity statement method, colour, shape, silhouette |
| [02_UI_UX_Import.md](02_UI_UX_Import.md) | `02_UI_UX/*.md` (sections are labelled per file) | Roblox's five UI principles, HUD, menus, shops, mobile, typography, anti-patterns |
| [03_Thumbnails_Icons_Import.md](03_Thumbnails_Icons_Import.md) | `03_Thumbnails_And_Icons/*.md` | Thumbnail and icon rules, composition checklist, anti-patterns, "AI-look" signs |
| [04_Game_Feel_Import.md](04_Game_Feel_Import.md) | `04_Animation_And_Game_Feel/*.md` | Action arc, timing starting points, easing, VFX tiers and limits, SFX, camera, reward reveals |
| [05_Game_Design_Import.md](05_Game_Design_Import.md) | `05_Game_Design/*.md` | Core-loop model, genre loops, progression, FTUE, social/solo, anti-pattern table |
| [06_Reference_Analyses/](06_Reference_Analyses/) (26 files) | `06_Reference_Analyses/` | Full template analyses IMP-01…IMP-28 (except 23, 27) |
| [07_Bad_Examples/](07_Bad_Examples/) (3 files) | `07_Bad_Examples/` | IMP-23, IMP-27 and the **Anti-Pattern Catalog** (AP-01…AP-15) |
| [09_Checklist_Additions.md](09_Checklist_Additions.md) | `09_Quality_Checklists/*.md` | Observable checklist items to add |
| [10_Reference_Wishlist_and_Capture_Guide.md](10_Reference_Wishlist_and_Capture_Guide.md) | Merge into `00_START_HERE.md` ("How to contribute references") or keep as a note | What to capture next and how the user supplies references |
| [11_Live_Snapshot_2026-10/](11_Live_Snapshot_2026-10/) (14 files) | Keep as its own folder `11_Live_Snapshot_2026-10/` (or move into `06_Reference_Analyses/`) | **Current** chart analysis of 46 top games (icons and all thumbnails, 2026-10-24): LIVE-00 overview and table, LIVE-01…13 references |
| `LIVE_2026-10-24_assets.zip` (sent to the user privately, **not** in the repo) | unzip into the academy root | 46 icons, 222 thumbnails, contact sheets and raw data for the LIVE references |
| [tools/asset_manifest.tsv](tools/asset_manifest.tsv) + `fetch_assets.sh` / `fetch_assets.ps1` | run once | Downloads the 48 reference images (and 1 video) into `Assets/…` with the exact filenames the analyses link to |

## Evidence labels used throughout
| Label | Meaning | How to treat it |
|---|---|---|
| **[FACT]** | Engine or platform behaviour read in the official docs | Technical requirement; re-verify yearly |
| **[RBX]** | Roblox's official design guidance | Strong guidance for the platform, not proof of success |
| **[OBS IMP-xx]** | My own visual observation of a reference image | Interpretation; confidence is stated in each analysis |
| **[GEN]** | Established general UI/UX/game-feel practice | General design principle |
| **[HYP]** | Starting value or untested idea | Verify by playtest before promoting it to a rule |
| **[PREF]** | Aesthetic preference | Override freely with the user's taste |

## Reference IDs
The analyses use the prefix **`IMP-`** so they can't collide with IDs the academy already uses. When merging, either keep `IMP-` as a separate series or renumber into the academy's scheme. If you renumber, update the IDs in the filenames, headings, the `Asset:` paths, the cross-links and `tools/asset_manifest.tsv` together.

| ID | Title | Type | Category |
|---|---|---|---|
| IMP-01 | Spellbound RPG — contextual radial menu | + | HUD/menus |
| IMP-02 | Super Striker League — context-swapping buttons | ± | HUD/mobile |
| IMP-03 | The Survival Game — minimal HUD | + | HUD |
| IMP-04 | Jailbreak — season pass | ± | Progression UI |
| IMP-05 | Dragon Adventures — premium shop | ± | Shop |
| IMP-06 | Tower Defense Simulator — daily shop | ± | Shop |
| IMP-07 | Winds of Fortune — stat icon system | + | Visual language |
| IMP-08 | BotClash Simulator — inventory master-detail | + | Inventory/identity |
| IMP-09 | Winds of Fortune — shop list typography | ± | Typography |
| IMP-10 | Close-button convention ×4 games | + | Conventions |
| IMP-11 | Arcane Odyssey — health colour consistency / font noise | ± | Consistency |
| IMP-12 | Mermaid Life — themed proximity prompt | + | World UI |
| IMP-13 | Spellbound RPG — spells-as-cards metaphor | ± | Metaphor |
| IMP-14 | Berry Avenue — avatar flow (process) | + | UX flows |
| IMP-15 | Creatures of Sonaria — colour-keyed trail | + | Onboarding |
| IMP-16 | Color or Die — in-world rules sign | + | Onboarding |
| IMP-17 | Hello Kitty Cafe — spotlight and trail | + | Onboarding |
| IMP-18 | Jailbreak — footprint hint | + | Level design |
| IMP-19 | Winds of Fortune — combat feedback and waypoint | + | Game feel/VFX |
| IMP-20 | Squishmallows — contextual tutorials | ± | Onboarding |
| IMP-21 | Plant — timed hints | + | Onboarding |
| IMP-22 | "Urban Rush" action thumbnail | ± | Thumbnail |
| IMP-23 | Unclear thumbnail / non-16:9 | − | Thumbnail |
| IMP-24 | Comical theme thumbnail (AI-look) | ± | Thumbnail |
| IMP-25 | Duvall Drive horror thumbnail | + | Thumbnail |
| IMP-26 | Icon theme set (small-size test) | + | Icon |
| IMP-27 | Icon failures ×4 | − | Icon |
| IMP-28 | Colour grade → genre | + | Icon/colour |

## Link format
Cross-links use **relative Markdown links** (`[text](../folder/file.md)`), which work in Obsidian with the "Use Wikilinks" setting either on or off. The `Related Notes` paths assume the academy structure from the setup prompt. When you merge text from a package-root file (e.g., `02_UI_UX_Import.md`) into a note inside a subfolder, prefix its links with `../`.

## Known limitations of this package
- The IMP references come from Roblox docs (dated examples). The **LIVE references are current** (2026-10-24, Halloween week) but cover only icons and thumbnails, not in-game UI.
- **No video watched and no audio heard.** Animation, SFX and timing guidance is [GEN]/[HYP], not observed.
- All reference images come from Roblox's documentation, so they're **examples Roblox chose**. That's a selection bias toward "teaching" examples. Real-world negatives are still thin: IMP-23, IMP-27, LIVE-11 and LIVE-12, plus weaknesses noted inside mixed references.
- Ratings are subjective (1 = avoid, 3 = useful with caveats, 5 = exemplary for its stated lesson). They aren't performance measures.
