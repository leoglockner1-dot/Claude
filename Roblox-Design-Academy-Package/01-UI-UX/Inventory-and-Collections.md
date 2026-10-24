---
title: "Inventory and Collections"
tags: [ui, inventory]
note_type: "topic"
---

# Inventory and Collections

## Evidence
- **Master-detail** (grid left, selected item right with actions) — BotClash ([UI-08](Analyses/UI-08-BotClash-Inventory-Master-Detail.md)).
- **Rarity** as card background + text tag (UI-06, UI-08); never colour alone (UI-012).
- **State badges**: equipped (check), locked (padlock) — small but consistent.
- **Capacity + summary** ("28/200", "Squad Power") turn a list into a goal.
- **Filters**: All/Owned/Popular/New/Limited (UI-17); rarity chips must be large enough for touch (UI-25 counter-example).
- **Sorting** by power with a one-tap "Equip/Deploy best" saves effort (UI-08).

## Rules
- Grid tiles ≥ 44 pt on touch (Apple HIG); icons from one family (UI-006).
- Show what changes when equipping (stat delta) — preview in place (UI-010).
- Collections need a visible completion ratio per set (goal visibility, PROG-001).

## Roblox implementation
`ScrollingFrame` + `UIGridLayout` + `AutomaticCanvasSize`; selection via `GuiService.SelectedObject` for gamepad; virtualise long lists (only create visible tiles) for performance.
