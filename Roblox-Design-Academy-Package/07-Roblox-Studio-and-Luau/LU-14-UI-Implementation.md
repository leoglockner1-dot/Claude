---
title: "LU-14 — UI implementation and scaling"
tags: [luau, ui, scaling, mobile]
note_type: "procedure"
evidence: "official docs; not executed (needs Studio)"
---

# LU-14 — UI implementation and scaling

## Purpose
Turn a UI design into a ScreenGui that stays readable and tappable from phone to TV, and that code can drive without hard-coded pixel positions.

## Preconditions
A wireframe with hierarchy decided ([Menus and Navigation](../01-UI-UX/Menus-and-Navigation.md), [HUD Layouts](../01-UI-UX/HUD-Layouts.md)) and a palette/type scale ([Typography, Color and Spacing](../01-UI-UX/Typography-Color-and-Spacing.md)).

## Approach
1. **Container:** one `ScreenGui` per screen region (HUD, Shop, Popups), with `ScreenInsets = CoreUISafeInsets` for anything interactive. Disable `ResetOnSpawn` for persistent UI so it is not rebuilt on every respawn.
2. **Layout:** position by **Scale** plus `AnchorPoint` (for example, anchor (1,0) at (1,0) for top-right). Use `UIListLayout`/`UIGridLayout` plus `UIPadding` instead of hand-placed offsets.
3. **Constraints:** `UISizeConstraint` (min/max pixels) on panels, `UIAspectRatioConstraint` on icons and cards, `UITextSizeConstraint` or `TextScaled` with a max for labels.
4. **Styling:** put palette, type sizes and spacing in Style Editor tokens, so a theme change is one edit. Use style queries such as `@PreferredInputTouch` or `@ViewportDisplaySizeSmall` for device variants.
5. **Code drives state, not layout:** controllers set `Visible`, text and values. Layout objects handle placement.

```lua
-- Client: a controller owns one screen and exposes intent-level functions.
local ShopController = {}
function ShopController.start(gui: ScreenGui, buyRemote: RemoteFunction)
    local panel = gui:WaitForChild("Panel") :: Frame
    for _, card in panel.Items:GetChildren() do
        if card:IsA("GuiButton") then
            card.Activated:Connect(function()         -- Activated covers mouse, touch and gamepad
                card.Active = false                   -- debounce while pending
                local ok, res = buyRemote:InvokeServer({ itemId = card.Name, qty = 1 })
                card.Active = true
                if ok then ShopController.showOwned(card, res) else ShopController.showError(card, res) end
            end)
        end
    end
end
return ShopController
```

## Common mistakes
- Offset-only sizes that look right in the Studio window and overflow on phones.
- `MouseButton1Click` instead of `Activated`. The latter covers touch and gamepad.
- Buttons under the core top bar or chat. Test with core UI visible.
- Text under 14–16 px on phones (a house guideline; verify with the Device Emulator at actual phone sizes).

## Test cases
- Device Emulator: a small phone (landscape), a tablet, a 1080p monitor and TV (ViewportDisplaySize Large). Nothing clipped, overlapping core UI, or under the thumb-unsafe corners.
- Gamepad: every button reachable with selection navigation ([CL-07](../23-Quality-Checklists/CL-07-Mobile-and-Accessibility.md)).

## Acceptance criteria
All test devices pass; no hard-coded absolute pixel positions for primary layout; theme tokens drive colours.

## References
- [UI Layout and Scaling (technical reference)](../14-Technical-Reference/UI-Layout-and-Scaling.md) · https://create.roblox.com/docs/ui · https://create.roblox.com/docs/ui/styling/editor
