---
title: "TUT-14 — Proximity prompts for interactions"
tags: [tutorial, ui, interaction, prompts, accessibility]
note_type: "tutorial-procedure"
source: "https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/proximity-prompts"
source_author: "Roblox Creator Documentation"
licence: "Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution."
accessed: "2026-10-24"
evidence: "[SRC] = what the tutorial says; [ANALYSIS] = our reading; [SIM-TESTED] = reproduced in a Luau simulation; [HYP] = untested"
---

# TUT-14 — Proximity prompts for interactions

**Skill:** Add press/hold interactions to world objects that work on keyboard, gamepad and touch.

## Source and access
- Source: [https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/proximity-prompts](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/proximity-prompts)
- Author: Roblox (official documentation). Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution.
- Access: Read the Markdown source of the page from the public Roblox/creator-docs repository (commit 4e795e6), accessed 2026-10-24. Images, videos and the linked sample places (.rbxl) were **not** opened, and no step was performed in Roblox Studio.

## Workflow in the tutorial [SRC]
1. Insert a `ProximityPrompt` into a part; set ObjectText, ActionText, KeyboardKeyCode, GamepadKeyCode.
2. `MaxActivationDistance` controls when it appears (the lock example lowers it to 4 studs); `HoldDuration` sets hold time (4 s to pick a lock).
3. Handle `ProximityPromptService.PromptTriggered`, `PromptButtonHoldBegan`, `PromptButtonHoldEnded` centrally and dispatch to an `ObjectActions` module.

## Decisions and the reasons the tutorial gives [SRC]
| Decision | Reason |
|---|---|
| Built-in prompts. | Cross-platform input and display for free. |
| Central service handler + module. | One script for all prompts instead of one per object. |
| Hold duration for meaningful actions. | Makes the action feel deliberate and prevents accidental triggers. |

## Our analysis
- **[ANALYSIS, source-supported]** `PromptTriggered` fires on the server with the player, but it does **not** prove the player was near: Roblox's security-tactics page lists triggering ProximityPrompt activations "at any range or frequency" among exploiter capabilities. The server must re-check distance and game state (is the door already open? does the player have the key?). *(An earlier draft of this note said the prompt proves proximity; corrected after reading that page.)*
- **[ANALYSIS]** Prompts are an accessible default for 'press E' interactions; use them before building custom UI ([Mobile, Controller and Accessibility](../01-UI-UX/Mobile-Controller-and-Accessibility.md)).

## Common mistakes
- Every object with its own script.
- Very long holds for frequent actions.
- Prompts overlapping when objects are close (use `Exclusivity` or spacing).

## Troubleshooting
| Symptom | Likely cause / fix |
|---|---|
| Prompt not showing | Check `Enabled`, distance, `RequiresLineOfSight` and that the parent is a part/attachment. |
| Fires twice | Both a per-prompt and a service handler connected. |

## Reusable procedure (ours)
1. Add prompt; set texts and keys.
2. Tune distance and hold time to the action's weight.
3. Handle centrally; dispatch by tag or attribute.
4. Validate distance and game state on the server before acting.
5. Add feedback on hold begin/end ([AV-01](../08-Animation-and-Game-Feel/Recipes/AV-01-Button-Feedback.md)).

## Exercise
For 'Last Boat Out': a 'Repair' prompt on the boat with a 2 s hold that only works if the player carries a part.

### Acceptance criteria
- [ ] Works with keyboard, gamepad and touch (emulator).
- [ ] Without a part, the server refuses and the player sees why.
- [ ] A trigger simulated from 40 studs away (test script calling the handler) is refused by the server's distance check.
- [ ] One handler script for all prompts.

## Related
- [LU-15 Input Handling](../07-Roblox-Studio-and-Luau/LU-15-Input-Handling.md)
- [GM mechanics index](../04-Game-Mechanics/Mechanics-Index.md)
