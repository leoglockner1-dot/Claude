# UI / UX — Import Content

**Merge into:** the `02_UI_UX/` notes. Each `##` section names its target file. Update the existing notes and don't duplicate them. Keep the evidence labels.

**Labels:**
- **[FACT]**: engine or platform behaviour, verified in the docs.
- **[RBX]**: Roblox's official design guidance (an authority, not proof).
- **[OBS IMP-xx]**: my own observation of a reference image.
- **[GEN]**: established general UI/UX practice.
- **[HYP]**: starting value or hypothesis to verify by playtest.
- **[PREF]**: aesthetic preference.

---

## → UI_Design_Principles.md

### The five Roblox UI principles [RBX]
1. **Prioritization.** Ask: what is the player doing right now, what do they most need to know, what choices do they have, what information do those choices need, and how often? Show only what the current context needs. Examples: [IMP-01](06_Reference_Analyses/IMP-01_Spellbound_RPG_Contextual_Radial_Menu.md), [IMP-02](06_Reference_Analyses/IMP-02_Super_Striker_League_Context_Buttons.md), [IMP-03](06_Reference_Analyses/IMP-03_The_Survival_Game_Minimal_HUD.md).
2. **Attention.** Five tools: **colour, size, space (padding), proximity, movement**. Use them in moderation, because "excessive use of bright, moving elements might overwhelm".
3. **Visual language.** A deliberate, consistent set of shape, colour and style choices that tells a player an element's purpose and state at a glance. Write it down as a **style guide**.
4. **Conventions.** Use shared grammar players already know: X closes, grey means unusable, padlock means locked, "E" prompt means interact, number keys pick hotbar slots, a ground circle means queue.
5. **Consistency.** Same meaning means same look, everywhere. Examples: health is always green; unaffordable prices are always red; close buttons always sit top-right.

### Identity without confusion [OBS IMP-10, IMP-08, IMP-12]
- **Keep the convention's placement and meaning; express identity through styling.** Four games put an "X" top-right and each looks completely different ([IMP-10](06_Reference_Analyses/IMP-10_Close_Button_Convention.md)).
- Pick **one geometric motif** (chamfer, pill, hexagon, brush stroke, stitched fabric…) and apply it to tabs, buttons, cards and frames ([IMP-08](06_Reference_Analyses/IMP-08_BotClash_Inventory_Master_Detail.md)). Most of what reads as "this game's UI" comes from that motif.
- **Generic ≠ conventional.** Generic copies another game's *look*. Conventional reuses the platform's *grammar*.

### Semantic colour map [RBX + OBS IMP-07, IMP-11]
- Fix a map early, before production: health, mana or energy, stamina, XP, soft currency, premium currency, each rarity tier, success, warning, danger, disabled.
- **Don't reuse semantic colours for decoration.** If green means "buy", tabs can't be green ([IMP-05](06_Reference_Analyses/IMP-05_Dragon_Adventures_Premium_Shop.md)).
- Labels take the colour of the icons or stats they affect ([IMP-07](06_Reference_Analyses/IMP-07_Winds_of_Fortune_Stat_Icon_System.md)).
- **Never colour alone** [FACT/RBX accessibility]. Pair colour with shape, icon or text (rarity colour plus a "Rare" tag).

### Feedback [RBX]
- Every action needs a response. Without one, players don't know whether they succeeded, whether the result was good, or whether the game is broken.
- Button states: **normal, hover (desktop), pressed, selected, disabled, loading or pending**. A "pending" state matters for purchase prompts and server round-trips. [GEN]

### One accent for the primary action [OBS IMP-08] [GEN]
- Each screen has **one** primary action, and it alone gets the accent colour (e.g., "DEPLOY BEST" is the only orange in a blue UI).

---

## → HUD_Design.md

- **Keep the centre third of the screen clear of persistent UI.** Put HUD elements on the edges [OBS IMP-03, IMP-02].
- **Colour shows live state; neutral shows navigation.** Saturated colour is for bars and alerts; menu buttons stay muted [OBS IMP-03].
- **Context-swap action buttons** rather than showing all actions. Keep positions fixed for muscle memory, and signal the swap [OBS IMP-02].
- **One button family per HUD.** Same shape, fill, stroke and label rules [OBS IMP-02 negative].
- Put a **solid plate or ring behind icons over the 3D world**. Translucent "glass" buttons lose contrast over bright terrain [OBS IMP-01, IMP-02].
- Use the platform HUD convention: **hotbar bottom-centre** with number hints; core stats near a corner [RBX: "replicating these patterns will ensure experienced Roblox users will intuitively understand"].
- **Never collide with Roblox core UI** (top bar, chat, player list) [FACT]. Use `ScreenInsets = CoreUISafeInsets` for interactive UI.
- Offer a **"hide UI / creator cam" toggle** for streamers and screenshots. Roblox cites Brookhaven's Creator Cam [RBX].
- Danger feedback (low HP) belongs on the periphery (vignette), never over the centre [OBS IMP-19].

---

## → Menus_and_Navigation.md

- **Design the flow before the screens.** List the player's goals, draw the flow chart, **count the taps** [RBX, IMP-14].
- **Progressive disclosure.** One parent button reveals secondary options [OBS IMP-01]. Console guidance agrees: going in and out of screens beats cramming [FACT console].
- For collections over about 12 items, use **master-detail** (browse left, inspect and act right) rather than modal popups [OBS IMP-08].
- **Two ways in** for large collections: category tabs **and** search [RBX IMP-14].
- **Selected tab = most prominent** (inverted or brighter), never darker or recessed [OBS IMP-05 negative, IMP-08 positive].
- **Gamepad:** every element must be reachable with directions, select and back. Key actions need few moves. Add shortcuts for essentials [FACT console].
- **Modals never stack.** Show one offer or dialog at a time and queue the rest [RBX contextual-purchases].
- Tutorial highlight = **arrow + outline + dim the rest**; only the target stays active [OBS IMP-17].

---

## → Shops_and_Inventory.md

- **Value ladder.** Hero offer > popular > others. The hero gets **space and size**, not just a badge [RBX + OBS IMP-05].
- **Product art scales with quantity** (stack → bag → chest → vault), so value is readable without numbers [OBS IMP-05].
- **One "buy" colour**, used nowhere else in the panel [OBS IMP-05].
- **Real-money (Robux) buttons look distinct from soft-currency buttons**, not just a different small icon [OBS IMP-06; HYP for safety].
- **Rarity = card background colour + text tag** [OBS IMP-06, IMP-08].
- **Locked = grey + padlock + reason** ("Reach level 10") [RBX convention + GEN].
- **Unaffordable = price in red** (keep the button visible and add a "get more" path) [RBX consistency example].
- **Balance visible inside the shop**, next to the prices [OBS IMP-09].
- **Restock or end timers sit in the header** of the section that changes [OBS IMP-06].
- **Row hierarchy:** name → currency-coloured price → muted meta. Information shared by all rows goes in the header [OBS IMP-09].
- **Paid random items (eggs, crates, spins, luck boosts):** show all outcomes and their **% odds summing to 100%** *before* purchase. A labelled "Odds" or "Details" button is OK; a bare (i) is not [FACT policy].
- **Pending state** on purchase buttons while `MarketplaceService` prompts are open. The Robux flow can take several seconds [FACT contextual-purchases].
- Contextual offers ("right item, right time"): pre-play shops (Doors' elevator), intermission offers (Dress to Impress), and complementary passes [RBX]. Never interrupt active play with a purchase modal [RBX].

---

## → Mobile_UI.md

Facts [FACT]:
- Most Roblox users play on mobile. Roblox says to design UI and UX **mobile-first**.
- Use `ScreenInsets`: `CoreUISafeInsets` for interactive UI, `DeviceSafeInsets` to clear notches only, `None` only for backgrounds.
- Prefer `Scale` sizing, plus `UISizeConstraint` and `UITextSizeConstraint` limits, plus `ViewportDisplaySize` (Small/Medium/Large) to adapt layouts.
- `UserInputService.PreferredInput` and `InputActionLabel` show the correct glyphs per device.
- Respect `PreferredTextSize` (and avoid relying on `TextScaled`, which ignores it), `PreferredTransparency` and `ReducedMotionEnabled`.
- Move less important buttons into a collapsible menu on small screens [RBX adaptive design].

Practice [GEN/HYP]:
- **Touch targets:** at least about **44–48 px (dp)**. This is Apple and Google platform guidance; Roblox's docs give no number. Use an invisible larger hit area around small glyphs.
- **Thumb zone:** primary actions bottom-right (right-handed default), movement stick bottom-left (Roblox default). Never put frequent actions top-centre.
- Hide keyboard key-letters on touch [OBS IMP-03].
- **Minimum readable text** on a phone: about 14–16 px at 1× for body text, more for anything read mid-action [HYP: verify on your baseline phone].
- Test on a real phone: the Studio emulator is fine for aspect ratio and controls, but not representative for memory or feel [FACT performance].

---

## → Typography_and_Spacing.md

- **At most two font families.** Set roles by size and weight: Display for titles, numbers and short labels; a readable sans for body and descriptions [GEN; OBS IMP-11 negative, IMP-09 positive].
- **All-caps display fonts only for 1–3 word labels.** Sentences in all caps with outlines flatten hierarchy and slow reading [OBS IMP-04].
- **Body text never italic-grey-small on translucent backgrounds** [OBS IMP-11, IMP-07].
- **Contrast:** aim for WCAG-like ratios, 4.5:1 for body and 3:1 for large text and UI shapes [GEN heuristic]. Text over 3D needs a stroke (`UIStroke`) or a plate.
- **Spacing scale:** pick one base unit (e.g., 4 or 8 px) and use only its multiples for padding and gaps [GEN]. Apply it via `UIPadding` and `UIListLayout.Padding`.
- **Two-level hierarchy per row or card:** primary (name or value) large and bright; secondary (meta) smaller and muted [OBS IMP-09].
- Avoid "excessively decorative or thin fonts" [RBX adaptive design].
- Builder Sans, Builder Extended and Builder Mono are Roblox's fonts and are free to use [FACT license].
- Test the longest localized string. Visual (icon-led) UI is easier to localize, and younger users are reading-averse [RBX].

---

## → UI_Anti_Patterns.md (summary; full catalog in [07_Bad_Examples/Anti_Pattern_Catalog.md](07_Bad_Examples/Anti_Pattern_Catalog.md))

- Two or more button styles in one HUD [IMP-02]
- Selected tab rendered darker than unselected ones [IMP-05]
- All-caps outlined text for sentences [IMP-04]
- Four or more typefaces [IMP-11]
- Translucent buttons over variable 3D backgrounds [IMP-02]
- Clipped or overlapping tags and labels [IMP-06]
- The same green for tabs and buy buttons [IMP-05]
- Robux and soft-currency buttons that look identical [IMP-06]
- Stacked purchase modals [RBX]
- Redundant per-row metadata [IMP-09]
- Stale or impossible states shown ("ends in 0s" + "coming soon") [IMP-04]
