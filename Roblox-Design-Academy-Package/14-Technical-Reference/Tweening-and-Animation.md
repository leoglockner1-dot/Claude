---
title: "Tweening and Animation"
tags: [technical, animation]
note_type: "technical-reference"
---

# Tweening and Animation

> **Verified** against the Roblox Creator Docs (GitHub mirror commit 4e795e6 and create.roblox.com, accessed 2026-10-24). Re-check yearly. Items marked *(recommendation)* are design advice, not engine facts.

- `TweenService:Create(instance, TweenInfo, goals)`; `TweenInfo.new(time, EasingStyle, EasingDirection, repeatCount, reverses, delay)`.
- Default EasingStyle **Quad**, default EasingDirection **Out**; Linear ignores direction. Styles include Sine, Quad, Cubic, Quart, Quint, Exponential, Circular, Back, Bounce, Elastic. [UI animation](https://create.roblox.com/docs/ui/animation)
- UI style transitions via `StyleRule`s (CSS-like).
- `CanvasGroup.GroupTransparency` to fade groups uniformly.
- Text effects: `MaxVisibleGraphemes` (typewriter), `RichText` tags.
- Reduced motion: `GuiService.ReducedMotionEnabled` → snap or fade instead of move (docs code samples).
- Character animation: Animation Editor keyframe easing (Linear/Cubic/Elastic/Bounce…), Animation Graphs (announced as full release on the DevForum: <https://devforum.roblox.com/t/4739840>), IK constraints. [animation editor](https://create.roblox.com/docs/animation/editor)
Measured examples: [Timing Reference](../08-Animation-and-Game-Feel/Timing-Reference.md)
