---
title: "Input and Controls"
tags: [technical, input]
note_type: "technical-reference"
---

# Input and Controls

> **Verified** against the Roblox Creator Docs (GitHub mirror commit 4e795e6 and create.roblox.com, accessed 2026-10-24). Re-check yearly. Items marked *(recommendation)* are design advice, not engine facts.

- **Input Action System** (`InputAction`, bindings, `InputActionLabel` for no-code device-correct hints) is the current cross-platform recommendation. [input action system](https://create.roblox.com/docs/input/input-action-system)
- `UserInputService.PreferredInput` reports the current primary input and updates on device switch; `InputAction.PreferredBinding` complements it.
- `UserInputService:GetImageForKeyCode()` / `GetStringForKeyCode()` for manual glyphs.
- `ContextActionService` remains supported for legacy bindings (docs mention CAS for experiences already relying on it).
- Console: design for 8–10 ft distance; TV-safe area; all UI reachable via directions + select + back; minimise moves for key actions; **disable chat window on console**; haptics via `HapticEffect` (use sparingly). [console guidelines](https://create.roblox.com/docs/production/publishing/console-guidelines)
- *(recommendation)* Touch targets ≥44×44 pt (Apple HIG) — Roblox gives no number.
