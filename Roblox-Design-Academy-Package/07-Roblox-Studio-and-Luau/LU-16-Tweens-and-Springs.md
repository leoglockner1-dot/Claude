---
title: "LU-16 — TweenService, springs and UI motion"
tags: [luau, animation, ui, game-feel]
note_type: "procedure"
evidence: "official docs + tested math (Feel.luau)"
code: "_tools/luau/src/Feel.luau"
---

# LU-16 — TweenService, springs and UI motion

## Purpose
Motion that communicates (a press, a reward, a state change) without being slow or noisy.

## Facts (ui/animation docs)
- `TweenService:Create(instance, TweenInfo.new(time, EasingStyle, EasingDirection), goals)`. The default style is **Quad** and the default direction is **Out**. Linear ignores direction.
- Tween several properties in one goal table; chain with `tween.Completed`.
- Use `CanvasGroup` to fade a whole panel. Tween `UIScale.Scale` for pops so layout does not shift.

## When to use what
| Need | Tool | Why |
|---|---|---|
| Fixed A→B transition (panel slide-in, fade) | TweenService | Engine-driven; cheap; cancellable |
| Motion that must follow a *changing* target (health bar chasing value, camera follow, magnet pickup) | Spring (`Feel.springStep`) | Retargets smoothly mid-motion; tweens restart abruptly |
| Number count-up | Tween a `NumberValue` and format on `.Changed`, or step it yourself with `Feel.ease` | Keeps text in sync |

## Timing starting points (house guidance; see [Timing Reference](../08-Animation-and-Game-Feel/Timing-Reference.md) for the measured basis)
- Button press: scale to 0.94 over 0.06–0.08 s, back over 0.1–0.15 s with `Back`/Out.
- Panel open: 0.18–0.25 s Quad/Out. Close faster than open (0.12–0.18 s).
- Reward pop: `backOut`. The tested curve peaks about 10% above target (asserted between 1.05 and 1.15).

## Spring (tested)
`Feel.springStep(x, v, target, omega, dt)` is a critically damped spring, closed form. The tests show:
- it settles to the target within 120 frames at ω = 12 **without overshoot**;
- it stays **stable with a 5-second frame** (a lag spike): no explosion, no NaN.
Use ω 10–20 for snappy UI and 4–8 for a soft camera (starting points).

```lua
local x, v = bar.Size.X.Scale, 0
RunService.RenderStepped:Connect(function(dt)
    x, v = Feel.springStep(x, v, targetHealthFraction, 14, dt)
    bar.Size = UDim2.fromScale(x, 1)
end)
```
Connect per-frame updates only while something is animating, and disconnect when settled ([LU-23](LU-23-Performance-Profiling.md)).

## Common mistakes
- Creating a new tween every frame. Create it once per change.
- Long, decorative motion on frequently used UI (a 0.6 s shop open becomes painful by the 20th time).
- Animating `Size`/`Position` of layout children, which fights the layout. Animate a `UIScale` or an inner frame instead.
- Unbounded spring `dt` with explicit Euler integration (explodes on lag spikes). The closed form here is safe.

## Acceptance criteria
Feedback starts within one frame of input; no transition on a frequently used path takes longer than 0.25 s; tests for any custom easing math pass.

## References
- https://create.roblox.com/docs/ui/animation · [Feedback Arc and Impact](../08-Animation-and-Game-Feel/Feedback-Arc-and-Impact.md)
