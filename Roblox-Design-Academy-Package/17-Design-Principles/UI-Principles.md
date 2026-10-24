---
title: "UI Principles (UI-001 – UI-017)"
tags: [principles, ui]
note_type: "principles"
---

# UI Principles (UI-001 – UI-017)

Principles for Roblox screen UI. Evidence labels: references link to observed analyses; "Roblox docs" means official guidance. Confidence: High = directly observed and/or officially documented; Medium = plausible interpretation with support; Low = hypothesis.

| ID | Principle | Confidence |
|---|---|---|
| UI-001 | One dominant primary action per screen | High |
| UI-002 | Few type sizes with clear steps | High |
| UI-003 | Neutral chrome, saturated content | High |
| UI-004 | One spacing scale everywhere | High |
| UI-005 | One visual system across all screens | High |
| UI-006 | Distinct silhouettes for currencies and icon families | High |
| UI-007 | Same fidelity, purposeful effects | High |
| UI-008 | Decoration never outweighs information | High |
| UI-009 | Count taps and offer two ways in | High |
| UI-010 | Preview in place, instantly | High |
| UI-011 | Destructive actions look different and confirm | High |
| UI-012 | Never encode state by colour alone | High |
| UI-013 | Hold-with-progress for consequential actions | High |
| UI-014 | Narrative text reveals fast and is skippable | Medium |
| UI-015 | Loading screens carry identity and progress | High |
| UI-016 | Contextual instructions = verb + input + duration | Medium |
| UI-017 | Tutorial prompts as prominent as what they teach | High |

## UI-001 — One dominant primary action per screen
**Rule:** When the player must decide quickly, exactly one action carries the accent colour, the largest size and the most prominent position; everything else steps back.

- **Reasoning:** Hierarchy is created by colour/contrast, scale and grouping (NN/g); when every button competes, nothing reads first.
- **Evidence:** [UI 18 DevForum Package Inspector Main Menu](../01-UI-UX/Analyses/UI-18-DevForum-Package-Inspector-Main-Menu.md), [UI 08 BotClash Inventory Master Detail](../01-UI-UX/Analyses/UI-08-BotClash-Inventory-Master-Detail.md), [UI 24 DevForum TURBOSTORM Racing HUD and Lobby](../01-UI-UX/Analyses/UI-24-DevForum-TURBOSTORM-Racing-HUD-and-Lobby.md)
- **Good application:** BotClash: "DEPLOY BEST" is the only orange element in a blue UI.
- **Failure mode:** TURBOSTORM lobby: nine stacked buttons in six colours, the core "race" path does not stand out.
- **Conditions & exceptions:** Celebration screens may be busy briefly; settings screens may legitimately have equal-weight options.
- **Roblox implementation:** Style Editor token `$Accent` used by exactly one `StyleRule` per screen; others use `$Surface`.
- **Confidence:** High
- **Tags:** #ui #hierarchy

## UI-002 — Few type sizes with clear steps
**Rule:** Use 4–5 type sizes at most (title, heading, body, caption, number) with visible steps; buttons never match the title size.

- **Reasoning:** Typographic hierarchy lets the eye find structure; equal sizes flatten it.
- **Evidence:** [UI 18 DevForum Package Inspector Main Menu](../01-UI-UX/Analyses/UI-18-DevForum-Package-Inspector-Main-Menu.md), [UI 04 Jailbreak Season Pass](../01-UI-UX/Analyses/UI-04-Jailbreak-Season-Pass.md), [UI 11 Arcane Odyssey Health Colour](../01-UI-UX/Analyses/UI-11-Arcane-Odyssey-Health-Colour.md)
- **Good application:** Winds of Fortune shop list: large name, smaller muted meta.
- **Failure mode:** Jailbreak pass: one all-caps outlined display font for everything.
- **Conditions & exceptions:** Display fonts are fine for 1–3 word titles and numbers.
- **Roblox implementation:** Define text-size tokens in the Style Editor; use `UITextSizeConstraint` minimums.
- **Confidence:** High
- **Tags:** #ui #typography

## UI-003 — Neutral chrome, saturated content
**Rule:** Keep panels, frames and inactive tabs low-saturation; reserve saturated colour for content (items, rarities), state, and the primary action.

- **Reasoning:** Content and decisions must out-contrast decoration.
- **Evidence:** [UI 26 DevForum Pls Donate and Color Place Minimal UI](../01-UI-UX/Analyses/UI-26-DevForum-Pls-Donate-and-Color-Place-Minimal-UI.md), [UI 15 DevForum Harsh Pack Shop](../01-UI-UX/Analyses/UI-15-DevForum-Harsh-Pack-Shop.md), [UI 17 DevForum Cream Category Shop](../01-UI-UX/Analyses/UI-17-DevForum-Cream-Category-Shop.md)
- **Good application:** Color Place: grey pill UI, the colour palette itself is the only colour.
- **Failure mode:** Packs shop: red, yellow, cyan and black at equal intensity — "harsh", no focal point.
- **Conditions & exceptions:** Chaotic/cartoon identities can use more colour if it follows a system (roles per colour).
- **Roblox implementation:** Palette module with role names (surface, text, accent, currency, rarity) instead of raw colours.
- **Confidence:** High
- **Tags:** #ui #color

## UI-004 — One spacing scale everywhere
**Rule:** Pick a base unit (4 or 8 px at 1080p scale) and use only its multiples for padding and gaps across all screens.

- **Reasoning:** Inconsistent padding is one of the most cited issues in community critique; consistent spacing reads as intentional.
- **Evidence:** [UI 23 DevForum Themeable Avatar Editor](../01-UI-UX/Analyses/UI-23-DevForum-Themeable-Avatar-Editor.md), [UI 15 DevForum Harsh Pack Shop](../01-UI-UX/Analyses/UI-15-DevForum-Harsh-Pack-Shop.md)
- **Good application:** —
- **Failure mode:** Avatar editor: padding "different everywhere" (reviewer).
- **Conditions & exceptions:** Optical adjustments for icons are fine.
- **Roblox implementation:** `UIPadding` and `UIListLayout.Padding` from tokens; use `UDim` scale + `UISizeConstraint` for responsiveness.
- **Confidence:** High
- **Tags:** #ui #spacing

## UI-005 — One visual system across all screens
**Rule:** Every panel shares fonts, corner radii, stroke rules, header style and close button; decide the system before building screens.

- **Reasoning:** Players perceive mixed systems as an "assembled" game; Roblox lists consistency as a core UI principle.
- **Evidence:** [UI 16 DevForum Inconsistent Quest and Shop](../01-UI-UX/Analyses/UI-16-DevForum-Inconsistent-Quest-and-Shop.md), [UI 02 Super Striker League Context Buttons](../01-UI-UX/Analyses/UI-02-Super-Striker-League-Context-Buttons.md), [UI 19 DevForum Default Template HUD](../01-UI-UX/Analyses/UI-19-DevForum-Default-Template-HUD.md)
- **Good application:** BotClash: chamfer motif on tabs, buttons, close corner.
- **Failure mode:** Quest panel and shop "don't look like they're from the same game".
- **Conditions & exceptions:** Diegetic in-world UI may follow world styling ([V25](../21-Video-Analyses/V25-Beyond-The-Dark-Diegetic-Map.md)).
- **Roblox implementation:** Single panel component (header/body/close) + Style Editor `StyleSheet` shared by all ScreenGuis.
- **Confidence:** High
- **Tags:** #ui #consistency

## UI-006 — Distinct silhouettes for currencies and icon families
**Rule:** Each currency and each stat family gets a unique shape, not just a recolour; icons come from one family (same stroke, size, perspective).

- **Reasoning:** Players identify currencies at a glance; mixed icon packs look inconsistent.
- **Evidence:** [UI 17 DevForum Cream Category Shop](../01-UI-UX/Analyses/UI-17-DevForum-Cream-Category-Shop.md), [UI 07 Winds of Fortune Stat Icon System](../01-UI-UX/Analyses/UI-07-Winds-of-Fortune-Stat-Icon-System.md), [UI 23 DevForum Themeable Avatar Editor](../01-UI-UX/Analyses/UI-23-DevForum-Themeable-Avatar-Editor.md)
- **Good application:** Winds of Fortune: heart/boot/flame shapes plus colour per family.
- **Failure mode:** Two nearly identical coin icons for coins and levels.
- **Conditions & exceptions:** —
- **Roblox implementation:** Icon sprite sheet with `ImageRectOffset`; naming convention per family.
- **Confidence:** High
- **Tags:** #ui #icons

## UI-007 — Same fidelity, purposeful effects
**Rule:** Render all UI elements at the same resolution and style; strokes, glows and gradients must have a job (legibility, state, rarity) — not be defaults.

- **Reasoning:** Mixed fidelity and blanket strokes read as low-effort or "AI-looking".
- **Evidence:** [UI 25 DevForum Roll a Cupcake AI Look](../01-UI-UX/Analyses/UI-25-DevForum-Roll-a-Cupcake-AI-Look.md), [UI 15 DevForum Harsh Pack Shop](../01-UI-UX/Analyses/UI-15-DevForum-Harsh-Pack-Shop.md)
- **Good application:** Text stroke only for text over the 3D world.
- **Failure mode:** Every label with a heavy stroke ("hurts my head"); pixelated X beside crisp buttons.
- **Conditions & exceptions:** Cartoon brands may use strokes widely if consistent and weight-controlled.
- **Roblox implementation:** `UIStroke` applied via a single StyleRule for "over-world text" class only.
- **Confidence:** High
- **Tags:** #ui #polish

## UI-008 — Decoration never outweighs information
**Rule:** Frames, ornaments and textures must stay visually lighter than the content they hold.

- **Reasoning:** Over-decorated frames steal attention from the decision.
- **Evidence:** [UI 21 DevForum Overdecorated Portfolio UI](../01-UI-UX/Analyses/UI-21-DevForum-Overdecorated-Portfolio-UI.md), [UI 05 Dragon Adventures Premium Shop](../01-UI-UX/Analyses/UI-05-Dragon-Adventures-Premium-Shop.md)
- **Good application:** Dragon Adventures keeps ornament mostly in the header ribbon.
- **Failure mode:** Dragon-sculpture frame dominates an inventory.
- **Conditions & exceptions:** Title/loading screens can be ornamental.
- **Roblox implementation:** 9-slice frames with thin borders; ornament only in headers.
- **Confidence:** High
- **Tags:** #ui #decoration

## UI-009 — Count taps and offer two ways in
**Rule:** Design flows from player goals, count taps to the goal, and give large collections both browse (categories) and search.

- **Reasoning:** Roblox design-flows guidance; friction = effort to reach a goal.
- **Evidence:** [UI 14 Berry Avenue Avatar Flow Chart](../01-UI-UX/Analyses/UI-14-Berry-Avenue-Avatar-Flow-Chart.md), [V01 Berry Avenue Avatar Flow](../21-Video-Analyses/V01-Berry-Avenue-Avatar-Flow.md)
- **Good application:** Berry Avenue avatar editor: tabs + search, instant preview.
- **Failure mode:** Deep menus requiring many taps for frequent actions.
- **Conditions & exceptions:** Rare, high-stakes actions can deliberately add a confirm step.
- **Roblox implementation:** Flow chart in the design doc; acceptance criterion "≤ N taps".
- **Confidence:** High
- **Tags:** #ux #flows

## UI-010 — Preview in place, instantly
**Rule:** Selecting an item shows its effect immediately on the avatar/object without a confirm step.

- **Reasoning:** Feedback within ~0.1 s feels like direct manipulation (NN/g response-time limits).
- **Evidence:** [V01 Berry Avenue Avatar Flow](../21-Video-Analyses/V01-Berry-Avenue-Avatar-Flow.md)
- **Good application:** Glasses appear on the avatar on tap.
- **Failure mode:** Preview only after "Apply".
- **Conditions & exceptions:** Purchases still require explicit confirmation.
- **Roblox implementation:** Apply cosmetic locally on client, validate on server.
- **Confidence:** High
- **Tags:** #ux #feedback

## UI-011 — Destructive actions look different and confirm
**Rule:** Delete/sell/reset actions are visually distinct, separated from the primary action and require confirmation (or hold-to-confirm).

- **Reasoning:** Prevents costly errors; equal-weight placement invites mistakes.
- **Evidence:** [UI 20 DevForum Revenance Title Screen](../01-UI-UX/Analyses/UI-20-DevForum-Revenance-Title-Screen.md), [V19 Proximity Hold Duration](../21-Video-Analyses/V19-Proximity-Hold-Duration.md)
- **Good application:** Hold-to-confirm ring for consequential actions.
- **Failure mode:** "Delete" next to "Start" with equal weight.
- **Conditions & exceptions:** —
- **Roblox implementation:** Confirmation modal or `HoldDuration`-style progress for destructive actions.
- **Confidence:** High
- **Tags:** #ux #safety

## UI-012 — Never encode state by colour alone
**Rule:** Pair colour with shape, icon, text or length.

- **Reasoning:** Roblox accessibility docs: >5 % of people have some colour blindness.
- **Evidence:** [UI 06 Tower Defense Simulator Daily Shop](../01-UI-UX/Analyses/UI-06-Tower-Defense-Simulator-Daily-Shop.md), [V06 V07 HUD Meter Tween and Damage Flash](../21-Video-Analyses/V06-V07-HUD-Meter-Tween-and-Damage-Flash.md)
- **Good application:** Rarity background + "Uncommon" tag; health bar colour + length.
- **Failure mode:** Rarity shown only by tint.
- **Conditions & exceptions:** —
- **Roblox implementation:** Add text/icon redundancy; test in greyscale.
- **Confidence:** High
- **Tags:** #accessibility

## UI-013 — Hold-with-progress for consequential actions
**Rule:** Long or irreversible actions use a hold with a visible progress ring; quick reversible actions fire immediately.

- **Reasoning:** Prevents accidental triggers while keeping waits legible.
- **Evidence:** [V19 Proximity Hold Duration](../21-Video-Analyses/V19-Proximity-Hold-Duration.md)
- **Good application:** Lock-pick hold ≈3.3 s with filling ring and clicks.
- **Failure mode:** Instant purchase of an expensive item on a single tap.
- **Conditions & exceptions:** Too-long holds for frequent actions frustrate.
- **Roblox implementation:** `ProximityPrompt.HoldDuration`; custom radial `UIGradient` rotation for screen buttons.
- **Confidence:** High
- **Tags:** #ux

## UI-014 — Narrative text reveals fast and is skippable
**Rule:** Reveal dialogue at roughly 10–20 characters/second, tap to complete, highlight keywords in colour.

- **Reasoning:** Gradual reveal paces drama; keywords keep it scannable for skimmers.
- **Evidence:** [V26 Typewriter Text](../21-Video-Analyses/V26-Typewriter-Text.md), [UI 07 Winds of Fortune Stat Icon System](../01-UI-UX/Analyses/UI-07-Winds-of-Fortune-Stat-Icon-System.md)
- **Good application:** Typewriter with red name and yellow keyword.
- **Failure mode:** Slow uninterruptible text walls.
- **Conditions & exceptions:** Reveal speed is a starting hypothesis — tune by playtest.
- **Roblox implementation:** `MaxVisibleGraphemes` + `RichText`.
- **Confidence:** Medium
- **Tags:** #ui #narrative

## UI-015 — Loading screens carry identity and progress
**Rule:** For waits beyond a few seconds, show game identity plus determinate progress or a useful tip.

- **Reasoning:** NN/g: feedback for >1 s waits, percent-done indicators for >~10 s.
- **Evidence:** [V18 Loading Spinner](../21-Video-Analyses/V18-Loading-Spinner.md)
- **Good application:** —
- **Failure mode:** Bare spinner for long loads.
- **Conditions & exceptions:** Very short loads: no loading screen at all.
- **Roblox implementation:** `ReplicatedFirst` + `ContentProvider:PreloadAsync` callback driving a bar.
- **Confidence:** High
- **Tags:** #ui #loading

## UI-016 — Contextual instructions = verb + input + duration
**Rule:** When an ability/mode activates, show what it is, how to use it, and how long it lasts — away from the action focus.

- **Reasoning:** Players learn at the moment of relevance.
- **Evidence:** [UI 24 DevForum TURBOSTORM Racing HUD and Lobby](../01-UI-UX/Analyses/UI-24-DevForum-TURBOSTORM-Racing-HUD-and-Lobby.md), [UI 02 Super Striker League Context Buttons](../01-UI-UX/Analyses/UI-02-Super-Striker-League-Context-Buttons.md)
- **Good application:** "TURRET ONLINE – 10 SECONDS – HOLD CLICK TO FIRE".
- **Failure mode:** Instructions in the centre of the screen during fast play.
- **Conditions & exceptions:** —
- **Roblox implementation:** Top-centre banner + `InputActionLabel` glyph.
- **Confidence:** Medium
- **Tags:** #ui #hud

## UI-017 — Tutorial prompts as prominent as what they teach
**Rule:** A tutorial instruction must be large and adjacent to its target, not a small chip in a corner.

- **Reasoning:** Players miss small prompts; unnoticed tutorials are no tutorials.
- **Evidence:** [UI 25 DevForum Roll a Cupcake AI Look](../01-UI-UX/Analyses/UI-25-DevForum-Roll-a-Cupcake-AI-Look.md), [ONB 03 Hello Kitty Cafe Spotlight and Trail](../13-Onboarding-and-Multiplayer/Onboarding/Analyses/ONB-03-Hello-Kitty-Cafe-Spotlight-and-Trail.md)
- **Good application:** Arrow + outline + dimmed background on the target.
- **Failure mode:** "Step 1/4" in a tiny top-left chip.
- **Conditions & exceptions:** —
- **Roblox implementation:** Spotlight overlay frames positioned from target `AbsolutePosition`.
- **Confidence:** High
- **Tags:** #onboarding #ui
