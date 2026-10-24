---
title: "LU-24 — Mobile support"
tags: [luau, mobile, input, ui, performance]
note_type: "procedure"
evidence: "official docs + house guidance"
---

# LU-24 — Mobile support

## Purpose
Make phones a first-class platform: readable UI, reachable controls, an affordable frame budget.

## Facts (input/mobile and related docs)
- Detect the input type through `UserInputService.PreferredInput` (a touch device can switch to a gamepad).
- Default orientation is **LandscapeSensor**; set `StarterGui.ScreenOrientation` to change it. Five modes exist: two sensor-based and three locked.
- Haptic feedback is available on supported devices (`HapticService`).
- Particle emitters cap at 100 particles/s on mobile (vs 400/s elsewhere).
- `GuiService.ViewportDisplaySize` reports Small/Medium/Large for UI variants.

## Checklist procedure
1. **Controls:** every action has a touch binding ([LU-15](LU-15-Input-Handling.md)). Primary actions sit within thumb reach (bottom-right for right-handed default). They do not overlap the jump button or the thumbstick area.
2. **UI:** CoreUISafeInsets; minimum tap targets around 44 px or more (a widely used mobile guideline; see the [Mobile and Accessibility](../01-UI-UX/Mobile-Controller-and-Accessibility.md) sources); text 14–16 px minimum at phone size.
3. **Performance:** budget draw calls and particles for phones; test the worst area of the map on a phone profile or a real device.
4. **Session shape:** phones get interrupted. Save more often at checkpoints; make the first meaningful action happen fast ([First-Minute Timeline](../03-Core-Gameplay-Loops/First-Minute-Timeline.md)).

## Test cases
- Device Emulator: a small phone in landscape. Every button is reachable with thumbs and nothing hides under the notch or core UI.
- Real device test where possible (the emulator does not show performance).

## Acceptance criteria
Phone layout verified on at least two phone profiles; no action is keyboard-only; frame rate measured on a phone.

## References
- https://create.roblox.com/docs/input/mobile · https://create.roblox.com/docs/studio/device-simulator · [CL-07 Mobile and Accessibility](../23-Quality-Checklists/CL-07-Mobile-and-Accessibility.md)
