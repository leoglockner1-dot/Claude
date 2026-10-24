---
title: "UI Layout and Scaling"
tags: [technical, ui]
note_type: "technical-reference"
---

# UI Layout and Scaling

> **Verified** against the Roblox Creator Docs (GitHub mirror commit 4e795e6 and create.roblox.com, accessed 2026-10-24). Re-check yearly. Items marked *(recommendation)* are design advice, not engine facts.

## Containers & safe areas
- `ScreenGui.ScreenInsets`: `CoreUISafeInsets` (default, recommended for interactive UI), `DeviceSafeInsets`, `TopbarSafeInsets`, `None` (backgrounds only). [on-screen containers](https://create.roblox.com/docs/ui/on-screen-containers)
- Core UI (top bar, chat, leaderboard) exists in every game — test for overlap.

## Size & position
- Prefer `UDim2` **Scale** for position/size; combine with `UISizeConstraint` (min/max pixel size), `UIAspectRatioConstraint`, `UITextSizeConstraint` (min/max font size). With `AutomaticSize`, `Size` acts as minimum. [size modifiers](https://create.roblox.com/docs/ui/size-modifiers)
- `GuiService.ViewportDisplaySize`: Small (phones/tablets), Medium (laptops/monitors), Large (TVs). [cross-platform](https://create.roblox.com/docs/projects/cross-platform)

## Layouts
`UIListLayout` (with flex options to fill/distribute/align), `UIGridLayout`, `UITableLayout`, `UIPageLayout`; `UIPadding` for inner spacing. [list/flex layouts](https://create.roblox.com/docs/ui/list-flex-layouts)

## Appearance modifiers
`UICorner`, `UIStroke`, `UIGradient` (Color/Transparency sequences, Type), `UIScale`. [appearance modifiers](https://create.roblox.com/docs/ui/appearance-modifiers)
*(recommendation)* Use `UIStroke` only where text sits over the 3D world (UI-007).

## Styling system
Style Editor: **tokens**, **design sheets**, **style rules**, **style queries** (e.g. `@ViewportDisplaySizeSmall`, `@PreferredInputTouch`), **style transitions**, **themes**. [style editor](https://create.roblox.com/docs/ui/styling/editor)
*(recommendation)* Put palette roles, type sizes and spacing into tokens (TECH-004).

## Other UI objects
`CanvasGroup` (group transparency tweens), `ViewportFrame` (3D previews), `ScrollingFrame` (`AutomaticCanvasSize`), `ProximityPrompt` (`HoldDuration`, `ObjectText`, `ActionText`, `Style=Custom`), `BillboardGui`/`SurfaceGui` (in-world UI), `UIDragDetector`.
