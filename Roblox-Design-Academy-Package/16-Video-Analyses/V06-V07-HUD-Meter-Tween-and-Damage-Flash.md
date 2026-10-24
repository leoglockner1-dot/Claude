---
title: "V06/V07 — Health meter tween and red damage flash (measured)"
tags: [video, reference, animation, vfx, ui, hud]
reference_type: "video"
date_accessed: "2026-10-24"
---

# V06/V07 — Health meter tween and red damage flash (measured)

## Identity
- **Name:** V06/V07 — Health meter tween and red damage flash (measured)
- **Reference type:** Video (official Roblox Creator Docs recording)
- **Source page:** https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters
- Local clip: [V06-hud-meter-damage-flash.mp4](../Assets/Animation-VFX/clips/V06-hud-meter-damage-flash.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/tutorials/creating-hud-meters/Meter-Change-Damage-Effect.mp4>
- Local clip: [V07-hud-meter-tweened.mp4](../Assets/Animation-VFX/clips/V07-hud-meter-tweened.mp4) · Original: <https://media.githubusercontent.com/media/Roblox/creator-docs/main/content/en-us/assets/tutorials/creating-hud-meters/Meter-Change-Tweened.mp4>
- **Creator/publisher:** Roblox Corporation (CC BY 4.0)
- **Date accessed:** 2026-10-24
- **How it was analysed:** 12 sampled frames + per-frame motion energy (20 fps) + audio RMS envelope, onset detection and spectral centroid (16 kHz mono), plus targeted frame crops where noted. **Audio was measured as waveform data, not listened to.**

![V06-hud-meter-damage-flash analysis sheet](../Assets/Animation-VFX/video-sheets/V06-hud-meter-damage-flash-sheet.jpg)
![V07-hud-meter-tweened analysis sheet](../Assets/Animation-VFX/video-sheets/V07-hud-meter-tweened-sheet.jpg)

*Sheet legend: blue = motion energy over time, orange = audio RMS, white lines = detected audio onsets, numbers = seconds.*

## What is observable
A character stands on a glowing hot grate in a sci-fi corridor. Top-right: heart icon + horizontal health bar.

**Measurements (frame crops every 50 ms, see strips below):**
- Damage ticks are **~1.03 s apart** (red-tint peaks at 4.70, 5.73, 6.73, 7.73, 8.77, 9.77, 10.80, 11.83, 12.83 s).
- Each tick the bar **shrinks over ~0.25 s visibly, front-loaded** (4.65 → 4.90 s) — matches the tutorial's `TweenInfo.new(0.5, Enum.EasingStyle.Exponential, Enum.EasingDirection.Out)` (the long exponential tail is imperceptible).
- Bar colour moves through the tutorial's 5-stop sequence: (0,225,50) green → (150,225,0) → (255,200,0) → (255,100,0) → (225,50,0) red as health falls (yellow by 7.9 s, orange 11.4 s, red 13 s).
- **Damage flash (V06 only):** a `ColorCorrectionEffect` `TintColor` (255,25,25) is set then tweened back to white. Mean (R−G) of the frame jumps +37 in one frame then decays: +27 (33 ms), +19 (67 ms), +14, +10 (133 ms), +6 (200 ms), ≈+3 by 330 ms.

![Health bar every 50 ms during one damage tick](../Assets/Animation-VFX/video-sheets/V06-health-bar-strip-50ms.jpg)

## What works
- **Instant attack, quick decay** flash: unmistakable even in peripheral vision, gone before the next tick.
- The bar animation is fast enough (~0.25 s) to feel responsive yet visible.
- Colour encodes severity redundantly with length (not colour alone).

## Why it might work
Front-loaded easing makes the change register immediately (perceived responsiveness — compare NN/g's 0.1 s "instantaneous" limit in [Sources](../17-Source-Library/External-Design-Sources.md)); the decaying tail avoids a hard pop. A peripheral full-screen tint is noticed without looking at the bar.

## What does not work / trade-offs
- Full-screen red every second for 9+ s becomes fatiguing; real games usually scale intensity with damage size or cap frequency (hypothesis).
- Without the flash (V07), small damage is easy to miss while looking at the world.

## Reusable principles
- **FEEL-002** Fast-in / soft-out for state changes; **FEEL-006** feedback intensity proportional to event importance; **UI-012** never encode state by colour alone ([Game-feel principles](../14-Design-Principles/Game-Feel-Principles.md)).

## Roblox implementation
```lua
-- bar: Exponential Out, ~0.5 s (perceived ~0.25 s)
TweenService:Create(fill, TweenInfo.new(0.5, Enum.EasingStyle.Exponential, Enum.EasingDirection.Out),
  {Size = UDim2.fromScale(frac, 1), BackgroundColor3 = colorFor(frac)}):Play()
-- flash: set instantly, tween back
cc.TintColor = Color3.fromRGB(255,25,25)
TweenService:Create(cc, TweenInfo.new(0.5, Enum.EasingStyle.Exponential, Enum.EasingDirection.Out),
  {TintColor = Color3.new(1,1,1)}):Play()
```
Respect `GuiService.ReducedMotionEnabled` by reducing flash strength (verified setting; scaling choice is a recommendation).

## Original application
A stamina system where running drains a bar with the same fast-out tween, and hitting zero triggers a brief blue desaturation pulse instead of red — reusing the timing recipe with a different semantic colour.

## Confidence
High (frame-measured and matched to published code).

## Limitations
One environment; perception claims are inferred from general UX research, not tested with players.

## Related
[Timing Reference](../05-Animation-and-Game-Feel/Timing-Reference.md) · [R02 Clean Readable Gameplay HUD](../13-Reusable-Design-Recipes/R02-Clean-Readable-Gameplay-HUD.md) · [Tweening and Animation](../11-Roblox-Technical-Reference/Tweening-and-Animation.md)
