---
title: "R12 — Reusable button animation system"
tags: [recipe, ui, animation, technical]
note_type: "recipe"
---

# R12 — Reusable button animation system

## 1. Goal
One module that gives every button consistent hover/press/selected/disabled/pending feedback.

## 2. When to use
Any project with more than a handful of buttons.

## 3. Required inputs
Design tokens (colours, scale values, durations).

## 4. Recommended structure
A ModuleScript `ButtonFX.attach(button, opts)` connecting `MouseEnter/MouseLeave/MouseButton1Down/Up`, `SelectionGained/Lost` (gamepad) and an API for `setDisabled`, `setPending`.

## 5. Step-by-step implementation
```lua
-- ButtonFX (sketch)
local TweenService = game:GetService("TweenService")
local GuiService = game:GetService("GuiService")
local ButtonFX = {}
local function tween(obj, t, goal)
    local time = GuiService.ReducedMotionEnabled and 0 or t
    TweenService:Create(obj, TweenInfo.new(time, Enum.EasingStyle.Quad, Enum.EasingDirection.Out), goal):Play()
end
function ButtonFX.attach(button: GuiButton)
    local scale = button:FindFirstChildOfClass("UIScale") or Instance.new("UIScale", button)
    button.MouseEnter:Connect(function() tween(scale, 0.08, {Scale = 1.04}) end)
    button.MouseLeave:Connect(function() tween(scale, 0.10, {Scale = 1.00}) end)
    button.MouseButton1Down:Connect(function() tween(scale, 0.06, {Scale = 0.95}) end)
    button.MouseButton1Up:Connect(function() tween(scale, 0.12, {Scale = 1.04}) end)
    button.SelectionGained:Connect(function() tween(scale, 0.08, {Scale = 1.04}) end)
    button.SelectionLost:Connect(function() tween(scale, 0.10, {Scale = 1.00}) end)
end
return ButtonFX
```
Add colour changes via Style Editor states or tweening `BackgroundColor3` from tokens; pending = spinner + `Active=false`.

## 6. Animation guidance
Hover 1.04 (0.08 s), press 0.95 (0.06 s), release back (0.12 s). Values are starting points.

## 7. Sound guidance
Optional press click from a pooled Sound; same frame as press.

## 8. Mobile considerations
No hover on touch — press feedback must stand alone; selection states for gamepad.

## 9. Performance considerations
One TweenInfo per state cached; avoid creating new UIScale each time.

## 10. Common mistakes
Different animation per screen; elastic easing on frequent buttons (DevForum debate, UI-26 notes); feedback only after server reply.

## 11. QA checklist
- [ ] All buttons use the module
- [ ] Gamepad selection visible
- [ ] ReducedMotion snaps

## 12. References & confidence
[UI 26 DevForum Pls Donate and Color Place Minimal UI](../../01-UI-UX/Analyses/UI-26-DevForum-Pls-Donate-and-Color-Place-Minimal-UI.md) · [Game Feel Principles](../../17-Design-Principles/Game-Feel-Principles.md) · [Tweening and Animation](../../14-Technical-Reference/Tweening-and-Animation.md)

**Confidence:** High (APIs verified); values Medium.
