---
title: "Anti-Pattern Catalog (AP-01 – AP-28)"
tags: [anti-pattern]
note_type: "anti-patterns"
---

# Anti-Pattern Catalog (AP-01 – AP-28)

These are **hypotheses to evaluate in context**, not universal bans. A pattern is judged by its purpose and execution — not because it is popular, colourful, simple or unusual.

| ID | Anti-pattern | Confidence |
|---|---|---|
| AP-01 | Generic AI/template-looking UI | High |
| AP-02 | Excessive gradients | Medium |
| AP-03 | Rounded-rectangle sameness | Medium |
| AP-04 | Inconsistent spacing | High |
| AP-05 | Inconsistent typography | High |
| AP-06 | Excessive outlines/strokes | High |
| AP-07 | Poor contrast | High |
| AP-08 | Too many accent colours | High |
| AP-09 | Random decorative icons/stickers | High |
| AP-10 | Unclear button hierarchy | High |
| AP-11 | Cluttered HUD | High |
| AP-12 | Inconsistent icon styles | High |
| AP-13 | Overused glow | Medium |
| AP-14 | Excessive particles | High |
| AP-15 | Unnecessary camera shake | Medium |
| AP-16 | Unreadable text | High |
| AP-17 | Weak thumbnails | High |
| AP-18 | Misleading thumbnails | High |
| AP-19 | Generic icons / template clones | High |
| AP-20 | Slow or forced onboarding | High |
| AP-21 | Repetitive core loop | Medium |
| AP-22 | Reward inflation | Medium |
| AP-23 | Excessive popups | High |
| AP-24 | Mobile-unfriendly UI | High |
| AP-25 | Unnecessary systems | Medium |
| AP-26 | VFX without gameplay meaning | High |
| AP-27 | Borrowed IP in key art | High |
| AP-28 | Stale live-ops art | High |

## AP-01 — Generic AI/template-looking UI
- **What it looks like:** Default-feeling fonts, identical glossy buttons, uniform heavy strokes on all text, saturated flat panels, no motif.
- **Why it can fail:** No identity decisions were made; players notice ("looks AI generated").
- **Particularly harmful when:** Theme-heavy games where UI contradicts the world.
- **When it might work:** Deliberate retro/default parody — if consistent.
- **How to correct it:** Run the identity framework; tokens; strokes only where needed.
- **Evidence / better references:** [UI 25 DevForum Roll a Cupcake AI Look](../01-UI-UX/Analyses/UI-25-DevForum-Roll-a-Cupcake-AI-Look.md), [UI 19 DevForum Default Template HUD](../01-UI-UX/Analyses/UI-19-DevForum-Default-Template-HUD.md)
- **Confidence:** High

## AP-02 — Excessive gradients
- **What it looks like:** Every surface and button has a gradient; gradients in different directions/colours.
- **Why it can fail:** Gradients become noise; inconsistency (one button gradient, another flat) is noticed.
- **Particularly harmful when:** Small elements, dense panels.
- **When it might work:** One subtle gradient used consistently for depth or rarity.
- **How to correct it:** Pick flat or one gradient rule; same on all buttons (DevForum: "either give them both same gradient or just remove it").
- **Evidence / better references:** [DevForum Sources](../22-Source-Library/DevForum-Sources.md)
- **Confidence:** Medium

## AP-03 — Rounded-rectangle sameness
- **What it looks like:** Every element is the same rounded card; no shape language.
- **Why it can fail:** Interchangeable look across games.
- **Particularly harmful when:** Identity-driven genres.
- **When it might work:** Minimal "core-like" UI where content carries identity (UI-26).
- **How to correct it:** Choose one motif (ID-002) — chamfer, tilted card, hexagon, brush.
- **Evidence / better references:** [UI 08 BotClash Inventory Master Detail](../01-UI-UX/Analyses/UI-08-BotClash-Inventory-Master-Detail.md), [UI 22 DevForum Smash Style Buttons and Pictogram Guide](../01-UI-UX/Analyses/UI-22-DevForum-Smash-Style-Buttons-and-Pictogram-Guide.md)
- **Confidence:** Medium

## AP-04 — Inconsistent spacing
- **What it looks like:** Padding varies screen to screen and inside cards.
- **Why it can fail:** Reads as unplanned; most-cited critique.
- **Particularly harmful when:** Dense shops/inventories.
- **When it might work:** —
- **How to correct it:** Spacing scale tokens; UIPadding everywhere.
- **Evidence / better references:** [UI 23 DevForum Themeable Avatar Editor](../01-UI-UX/Analyses/UI-23-DevForum-Themeable-Avatar-Editor.md), [UI 15 DevForum Harsh Pack Shop](../01-UI-UX/Analyses/UI-15-DevForum-Harsh-Pack-Shop.md)
- **Confidence:** High

## AP-05 — Inconsistent typography
- **What it looks like:** 4+ fonts; all-caps sentences; buttons as large as titles.
- **Why it can fail:** Hierarchy collapses; slower reading.
- **Particularly harmful when:** Text-heavy screens.
- **When it might work:** Display font for 1–3-word titles.
- **How to correct it:** 2 families, 4–5 sizes.
- **Evidence / better references:** [UI 11 Arcane Odyssey Health Colour](../01-UI-UX/Analyses/UI-11-Arcane-Odyssey-Health-Colour.md), [UI 04 Jailbreak Season Pass](../01-UI-UX/Analyses/UI-04-Jailbreak-Season-Pass.md), [UI 18 DevForum Package Inspector Main Menu](../01-UI-UX/Analyses/UI-18-DevForum-Package-Inspector-Main-Menu.md)
- **Confidence:** High

## AP-06 — Excessive outlines/strokes
- **What it looks like:** Thick strokes on all text and every panel; mismatched outline weights.
- **Why it can fail:** Visual vibration; "hurts my head".
- **Particularly harmful when:** Body text, small text.
- **When it might work:** Text over 3D world; cartoon brands with weight-controlled strokes.
- **How to correct it:** One stroke rule for over-world text only.
- **Evidence / better references:** [UI 25 DevForum Roll a Cupcake AI Look](../01-UI-UX/Analyses/UI-25-DevForum-Roll-a-Cupcake-AI-Look.md)
- **Confidence:** High

## AP-07 — Poor contrast
- **What it looks like:** Light-on-light, dark-on-dark, small italic grey text on translucent panels.
- **Why it can fail:** Unreadable for many, especially on phones.
- **Particularly harmful when:** Mobile, bright scenes.
- **When it might work:** Decorative captions with no information.
- **How to correct it:** ≈4.5:1 for text; opaque panels with PreferredTransparency.
- **Evidence / better references:** [UI 11 Arcane Odyssey Health Colour](../01-UI-UX/Analyses/UI-11-Arcane-Odyssey-Health-Colour.md), [UI 20 DevForum Revenance Title Screen](../01-UI-UX/Analyses/UI-20-DevForum-Revenance-Title-Screen.md)
- **Confidence:** High

## AP-08 — Too many accent colours
- **What it looks like:** 4+ saturated hues at equal intensity.
- **Why it can fail:** No focal point; "harsh".
- **Particularly harmful when:** Shops, lobbies.
- **When it might work:** Chaotic identity with colour roles defined.
- **How to correct it:** One accent; neutral chrome; colour roles.
- **Evidence / better references:** [UI 15 DevForum Harsh Pack Shop](../01-UI-UX/Analyses/UI-15-DevForum-Harsh-Pack-Shop.md), [UI 24 DevForum TURBOSTORM Racing HUD and Lobby](../01-UI-UX/Analyses/UI-24-DevForum-TURBOSTORM-Racing-HUD-and-Lobby.md)
- **Confidence:** High

## AP-09 — Random decorative icons/stickers
- **What it looks like:** Icons/emojis without meaning; stickers on key art.
- **Why it can fail:** Confusing; signals low effort.
- **Particularly harmful when:** Thumbnails/icons, menus.
- **When it might work:** Event badges with shared meaning (TI-14).
- **How to correct it:** Every icon must map to a function or remove it.
- **Evidence / better references:** [TI 06 Icon Failures](../02-Thumbnails-and-Icons/Analyses/TI-06-Icon-Failures.md), [TI 02 Unclear Thumbnail and Stretched Upload](../02-Thumbnails-and-Icons/Analyses/TI-02-Unclear-Thumbnail-and-Stretched-Upload.md), [UI 18 DevForum Package Inspector Main Menu](../01-UI-UX/Analyses/UI-18-DevForum-Package-Inspector-Main-Menu.md)
- **Confidence:** High

## AP-10 — Unclear button hierarchy
- **What it looks like:** All buttons same size/colour; destructive next to primary.
- **Why it can fail:** Decision paralysis, errors.
- **Particularly harmful when:** Menus, dialogs.
- **When it might work:** Settings lists.
- **How to correct it:** UI-001, UI-011.
- **Evidence / better references:** [UI 24 DevForum TURBOSTORM Racing HUD and Lobby](../01-UI-UX/Analyses/UI-24-DevForum-TURBOSTORM-Racing-HUD-and-Lobby.md), [UI 20 DevForum Revenance Title Screen](../01-UI-UX/Analyses/UI-20-DevForum-Revenance-Title-Screen.md)
- **Confidence:** High

## AP-11 — Cluttered HUD
- **What it looks like:** Persistent elements in the centre; many always-visible buttons.
- **Why it can fail:** Obscures play; overwhelms new players.
- **Particularly harmful when:** Mobile.
- **When it might work:** Complex sims with toggleable panels.
- **How to correct it:** Zones (R02), context-swap, progressive disclosure.
- **Evidence / better references:** [UI 03 The Survival Game Minimal HUD](../01-UI-UX/Analyses/UI-03-The-Survival-Game-Minimal-HUD.md), [UI 02 Super Striker League Context Buttons](../01-UI-UX/Analyses/UI-02-Super-Striker-League-Context-Buttons.md)
- **Confidence:** High

## AP-12 — Inconsistent icon styles
- **What it looks like:** Icons from several packs with different strokes/perspective.
- **Why it can fail:** Looks assembled.
- **Particularly harmful when:** Toolbars, inventories.
- **When it might work:** —
- **How to correct it:** One icon family.
- **Evidence / better references:** [UI 23 DevForum Themeable Avatar Editor](../01-UI-UX/Analyses/UI-23-DevForum-Themeable-Avatar-Editor.md)
- **Confidence:** High

## AP-13 — Overused glow
- **What it looks like:** Glow on everything, often to "make it pop".
- **Why it can fail:** Glow stops signalling rarity/attention.
- **Particularly harmful when:** Dark UIs.
- **When it might work:** Rarity/attention on one element.
- **How to correct it:** Reserve glow for rarity and focus.
- **Evidence / better references:** [UI 05 Dragon Adventures Premium Shop](../01-UI-UX/Analyses/UI-05-Dragon-Adventures-Premium-Shop.md)
- **Confidence:** Medium

## AP-14 — Excessive particles
- **What it looks like:** Particle storms for frequent actions.
- **Why it can fail:** Noise, overdraw, mobile FPS.
- **Particularly harmful when:** Mobile; multiplayer crowds.
- **When it might work:** Rare XL events.
- **How to correct it:** Tier table; Emit bursts; caps.
- **Evidence / better references:** [V20 Burst Particle Trap](../21-Video-Analyses/V20-Burst-Particle-Trap.md), [VFX Principles and Performance](../09-VFX/VFX-Principles-and-Performance.md)
- **Confidence:** High

## AP-15 — Unnecessary camera shake
- **What it looks like:** Shake on every hit/click.
- **Why it can fail:** Motion sickness; readability.
- **Particularly harmful when:** Frequent actions; ReducedMotion users.
- **When it might work:** Heavy rare impacts.
- **How to correct it:** Decaying short shake only for heavy events; respect ReducedMotion.
- **Evidence / better references:** [Feedback Arc and Impact](../08-Animation-and-Game-Feel/Feedback-Arc-and-Impact.md)
- **Confidence:** Medium

## AP-16 — Unreadable text
- **What it looks like:** Tiny descriptions, TextScaled shrinkage, chips too small.
- **Why it can fail:** Information lost; accessibility settings ignored.
- **Particularly harmful when:** Mobile.
- **When it might work:** —
- **How to correct it:** Min text sizes; AutomaticSize; test Largest.
- **Evidence / better references:** [UI 13 Spellbound Card Combat](../01-UI-UX/Analyses/UI-13-Spellbound-Card-Combat.md), [UI 25 DevForum Roll a Cupcake AI Look](../01-UI-UX/Analyses/UI-25-DevForum-Roll-a-Cupcake-AI-Look.md)
- **Confidence:** High

## AP-17 — Weak thumbnails
- **What it looks like:** No subject, no verb, generic question text.
- **Why it can fail:** Wasted impressions.
- **Particularly harmful when:** New games.
- **When it might work:** Established brands (still risky).
- **How to correct it:** Brief + composition checklist.
- **Evidence / better references:** [TI 02 Unclear Thumbnail and Stretched Upload](../02-Thumbnails-and-Icons/Analyses/TI-02-Unclear-Thumbnail-and-Stretched-Upload.md), [TI 29 DevForum Indie Thumbnails](../02-Thumbnails-and-Icons/Analyses/TI-29-DevForum-Indie-Thumbnails.md)
- **Confidence:** High

## AP-18 — Misleading thumbnails
- **What it looks like:** Cinematic scenes, fake UI, effects not in game.
- **Why it can fail:** Rejected videos; disappointed players; low qualified play-through.
- **Particularly harmful when:** Video thumbnails (policy).
- **When it might work:** —
- **How to correct it:** Authentic captures (V02).
- **Evidence / better references:** [V02 V03 Thumbnail Videos Accurate vs Misleading](../21-Video-Analyses/V02-V03-Thumbnail-Videos-Accurate-vs-Misleading.md), [TI 28 Barrys Prison Fake UI in Thumbnail](../02-Thumbnails-and-Icons/Analyses/TI-28-Barrys-Prison-Fake-UI-in-Thumbnail.md)
- **Confidence:** High

## AP-19 — Generic icons / template clones
- **What it looks like:** Default icon; copying a leader's composition.
- **Why it can fail:** No identity; confusion with the original.
- **Particularly harmful when:** Crowded genres.
- **When it might work:** Using genre grammar with your own hook.
- **How to correct it:** R09; THUMB-011.
- **Evidence / better references:** [TI 06 Icon Failures](../02-Thumbnails-and-Icons/Analyses/TI-06-Icon-Failures.md), [TI 12 Template Clone Steal An Egg](../02-Thumbnails-and-Icons/Analyses/TI-12-Template-Clone-Steal-An-Egg.md)
- **Confidence:** High

## AP-20 — Slow or forced onboarding
- **What it looks like:** Blurred forced tutorials, paragraph popups, teaching shops first.
- **Why it can fail:** Players leave at that step (48 % in one funnel).
- **Particularly harmful when:** Every game.
- **When it might work:** Narrative games with an intentional intro — still short.
- **How to correct it:** Core verb first; picture rules.
- **Evidence / better references:** [ONB 06 DevForum Forced Blur Tutorial Funnel](../13-Onboarding-and-Multiplayer/Onboarding/Analyses/ONB-06-DevForum-Forced-Blur-Tutorial-Funnel.md), [CS 16 Troll Tower Obby Funnel](../20-Game-Case-Studies/CS-16-Troll-Tower-Obby-Funnel.md)
- **Confidence:** High

## AP-21 — Repetitive core loop
- **What it looks like:** Same action, no new context, no stakes.
- **Why it can fail:** Boredom after novelty.
- **Particularly harmful when:** Long sessions.
- **When it might work:** Idle/ASMR games where repetition is the comfort — still vary visuals.
- **How to correct it:** New contexts for the verb; stakes.
- **Evidence / better references:** [Core Loop Principles](../17-Design-Principles/Core-Loop-Principles.md)
- **Confidence:** Medium

## AP-22 — Reward inflation
- **What it looks like:** Numbers grow meaninglessly ("$997,874,672/s").
- **Why it can fail:** Rewards lose value; upgrades invisible.
- **Particularly harmful when:** Long-term retention.
- **When it might work:** Incremental genre where escalation is the fantasy — tie to visible change.
- **How to correct it:** Visible consequences (PROG-002); number formatting tiers.
- **Evidence / better references:** [TI 30 Incremental Genre Grammar](../02-Thumbnails-and-Icons/Analyses/TI-30-Incremental-Genre-Grammar.md), [TI 15 Number and Odds Bait](../02-Thumbnails-and-Icons/Analyses/TI-15-Number-and-Odds-Bait.md)
- **Confidence:** Medium

## AP-23 — Excessive popups
- **What it looks like:** Stacked offers on join; prompts during play.
- **Why it can fail:** First-minute churn; annoyance.
- **Particularly harmful when:** Mobile.
- **When it might work:** —
- **How to correct it:** Modal queue; natural pauses (PROG-008).
- **Evidence / better references:** [Shops and Monetization UI](../01-UI-UX/Shops-and-Monetization-UI.md)
- **Confidence:** High

## AP-24 — Mobile-unfriendly UI
- **What it looks like:** Hover-only info, small targets, buttons under thumbstick.
- **Why it can fail:** Most players are on mobile.
- **Particularly harmful when:** Always.
- **When it might work:** —
- **How to correct it:** R13; CL-07.
- **Evidence / better references:** [Mobile Controller and Accessibility](../01-UI-UX/Mobile-Controller-and-Accessibility.md), [V01 Berry Avenue Avatar Flow](../21-Video-Analyses/V01-Berry-Avenue-Avatar-Flow.md)
- **Confidence:** High

## AP-25 — Unnecessary systems
- **What it looks like:** Many features without a clear core.
- **Why it can fail:** Unclear point of the game.
- **Particularly harmful when:** New games.
- **When it might work:** Mature games adding depth for locals.
- **How to correct it:** Map features to loop; cut orphans.
- **Evidence / better references:** [CS 17 Outbreak Mayhem](../20-Game-Case-Studies/CS-17-Outbreak-Mayhem.md)
- **Confidence:** Medium

## AP-26 — VFX without gameplay meaning
- **What it looks like:** Effects that do not correspond to any event or state.
- **Why it can fail:** Noise; teaches nothing.
- **Particularly harmful when:** Combat, HUDs.
- **When it might work:** Ambient mood effects kept low-contrast.
- **How to correct it:** Every effect answers a player question.
- **Evidence / better references:** [GF 01 Winds of Fortune Combat Feedback](../08-Animation-and-Game-Feel/Analyses/GF-01-Winds-of-Fortune-Combat-Feedback.md)
- **Confidence:** High

## AP-27 — Borrowed IP in key art
- **What it looks like:** Lookalike characters/franchises.
- **Why it can fail:** Legal/moderation risk; identity borrowed.
- **Particularly harmful when:** Marketing.
- **When it might work:** Licensed collaborations.
- **How to correct it:** Original mascot.
- **Evidence / better references:** [TI 27 IP Adjacent Imagery Risk](../02-Thumbnails-and-Icons/Analyses/TI-27-IP-Adjacent-Imagery-Risk.md)
- **Confidence:** High

## AP-28 — Stale live-ops art
- **What it looks like:** Christmas hats in October; duplicate thumbnails; placeholders.
- **Why it can fail:** Signals neglect.
- **Particularly harmful when:** Live games.
- **When it might work:** —
- **How to correct it:** Audit each update (THUMB-012).
- **Evidence / better references:** [TI 13 Dress To Impress Thumbnail Set](../02-Thumbnails-and-Icons/Analyses/TI-13-Dress-To-Impress-Thumbnail-Set.md), [TI 18 Placeholder Thumbnail](../02-Thumbnails-and-Icons/Analyses/TI-18-Placeholder-Thumbnail.md), [TI 22 Asymmetric CoOp Explained In One Image](../02-Thumbnails-and-Icons/Analyses/TI-22-Asymmetric-CoOp-Explained-In-One-Image.md)
- **Confidence:** High
