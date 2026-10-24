---
title: "LU-15 — Input handling (keyboard, gamepad, touch)"
tags: [luau, input, mobile, gamepad]
note_type: "procedure"
evidence: "official docs; not executed"
---

# LU-15 — Input handling (keyboard, gamepad, touch)

## Purpose
One set of gameplay actions that works on every device, switches with game phase (play vs menu), and shows the right button prompts.

## Approach: Input Action System (official, documented 2026-10)
- `InputContext`: a group of actions, for example `PlayContext` for gameplay and `NavContext` for menus. Toggle `Enabled` when menus open or close. `Priority` plus `Sink` lets a higher context consume keys so they do not reach lower ones; an open inventory, for example, can block gameplay keys.
- `InputAction`: a mechanic ("Jump", "Sprint", "Interact"). The default `Type` is `Bool` (press/release); other types exist for directional input.
- `InputBinding`: maps an action to keys, gamepad buttons and touch.
- `InputAction.PreferredBinding` returns the binding for the player's current device. Use it to show the correct prompt glyph.
- The docs recommend a `Folder` named `Inputs` in `ReplicatedStorage` that holds the contexts.

For older code, `ContextActionService` (bind/unbind actions, optional touch buttons) and `UserInputService` (raw input events, `PreferredInput`) still exist. Pick one approach per project.

## Procedure
1. List actions per game phase (play, menu, vehicle, spectate).
2. Create a context per phase, with actions and bindings for keyboard/mouse, gamepad and touch.
3. In the client controller, connect to each action's events and send **intents** to the server (validated per [LU-05](LU-05-Server-Validation.md)).
4. Show prompts from `PreferredBinding` and update them when the device changes.
5. On menu open: enable `NavContext` and disable `PlayContext`. Reverse on close.

## Common mistakes
- Hard-coding "Press E" text. Gamepad and touch players see wrong instructions.
- Only keyboard bindings, with mobile "handled later". Mobile is a large share of Roblox play; design touch from day one.
- Leaving gameplay input active behind an open menu (the player jumps while clicking Buy).
- Sending raw key presses to the server instead of intents.

## Test cases
- Keyboard, gamepad (Controller Emulator in Studio) and touch (Device Emulator): every action works and the prompt glyph matches the device.
- With the menu open, gameplay actions do not fire.

## Acceptance criteria
All actions bound for 3 input types; prompts come from `PreferredBinding`; context switching verified.

## References
- https://create.roblox.com/docs/input/input-action-system · https://create.roblox.com/docs/input/mobile · [Input and Controls (reference)](../14-Technical-Reference/Input-and-Controls.md)
