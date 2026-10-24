---
title: "UI/UX Overview — how to use this section"
tags: [ui, index]
note_type: "topic"
---

# UI/UX Overview — how to use this section

Roblox's official UI/UX guidance names five UI principles — **prioritization, attention, visual language, conventions, consistency** — and three UX tools — **conventions, metaphors, feedback** ([Roblox docs](https://create.roblox.com/docs/production/game-design/ui-ux-design)). This section turns them into decisions, backed by 26 UI analyses.

## Navigation
| Topic | Note |
|---|---|
| HUD composition | [HUD Layouts](HUD-Layouts.md) |
| Menus, lobbies, flows | [Menus and Navigation](Menus-and-Navigation.md) |
| Shops & monetization UI | [Shops and Monetization UI](Shops-and-Monetization-UI.md) |
| Inventory & collections | [Inventory and Collections](Inventory-and-Collections.md) |
| Rewards, progress bars, quests, notifications | [Rewards Progress and Notifications](Rewards-Progress-and-Notifications.md) |
| Mobile, controller, accessibility | [Mobile Controller and Accessibility](Mobile-Controller-and-Accessibility.md) |
| Typography, colour, spacing | [Typography Color and Spacing](Typography-Color-and-Spacing.md) |
| Loading, death, respawn, round transitions | [Loading Death and Round Transitions](Loading-Death-and-Round-Transitions.md) |
| Principles UI-001…017 | [UI Principles](../14-Design-Principles/UI-Principles.md) |

## The five decisions that separate intentional UI from template UI
1. **What is the one primary action on this screen?** (UI-001) — if you cannot name it, the screen has no hierarchy.
2. **What is the system?** Fonts, radii, stroke rule, palette roles, spacing unit, icon family — written down before screens (UI-005, ID-001). Community critique repeatedly points at mixed systems ([UI-16](Analyses/UI-16-DevForum-Inconsistent-Quest-and-Shop.md)).
3. **What is decoration doing?** Every glow, stroke, gradient and ornament needs a job (UI-007, UI-008; [UI-25](Analyses/UI-25-DevForum-Roll-a-Cupcake-AI-Look.md)).
4. **Which conventions do we keep?** Placement/meaning of X, padlock, grey-disabled, "E" prompt, hotbar numbers — keep; express identity in styling ([UI-10](Analyses/UI-10-Close-Button-Convention.md)).
5. **What happens on input within 0.1 s?** Hover/press/selection feedback for every interactive element (FEEL-007).

## Evidence map (all UI analyses)
| ID | Lesson | Type |
|---|---|---|
| UI-01 | Progressive disclosure via radial reveal | + |
| UI-02 | Context-swapping buttons; mixed button languages | ± |
| UI-03 | Centre clear; colour = live state | + |
| UI-04 | Free vs premium track by position + colour; all-caps everywhere | ± |
| UI-05 | Value ladder, art scales with value | ± |
| UI-06 | Grouping by container; rarity tag + colour | ± |
| UI-07 | Icon grammar by colour + shape | + |
| UI-08 | Master-detail, one accent, one motif | + |
| UI-09 | Row typography hierarchy | ± |
| UI-10 | Convention in placement, identity in style | + |
| UI-11 | Semantic colour map; too many fonts | ± |
| UI-12 | Restyled proximity prompt | + |
| UI-13 | Metaphor (spells as cards); unreadable cards | ± |
| UI-14 | Flow chart + tap count | + |
| UI-15 | Harsh four-hue shop (community critique) | − |
| UI-16 | Two screens, two systems | ± |
| UI-17 | Warm system + clashing tabs; currency icons | ± |
| UI-18 | One dominant menu action | + |
| UI-19 | Default-template HUD | − |
| UI-20 | Tone mismatch; destructive action placement | ± |
| UI-21 | Over-decoration; genre-skin copying | ± |
| UI-22 | Pictogram rule guide; tilted-card motif | + |
| UI-23 | Theme tokens; padding/icon consistency | ± |
| UI-24 | Racing HUD conventions; rainbow lobby | ± |
| UI-25 | "AI-looking" strokes and buttons | − |
| UI-26 | Neutral chrome, colourful content; hover tweens | + |
