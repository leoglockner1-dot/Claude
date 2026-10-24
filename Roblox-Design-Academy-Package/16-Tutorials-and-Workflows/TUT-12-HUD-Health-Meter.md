---
title: "TUT-12 — Create a HUD health meter (safe areas, tweens, colour ramp)"
tags: [tutorial, ui, hud, tween, safe-area]
note_type: "tutorial-procedure"
source: "https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters"
source_author: "Roblox Creator Documentation"
licence: "Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution."
accessed: "2026-10-24"
evidence: "[SRC] = what the tutorial says; [ANALYSIS] = our reading; [SIM-TESTED] = reproduced in a Luau simulation; [HYP] = untested"
---

# TUT-12 — Create a HUD health meter (safe areas, tweens, colour ramp)

**Skill:** Replace the default health bar with a custom meter that respects device safe areas and animates on change.

## Source and access
- Source: [https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters)
- Author: Roblox (official documentation). Prose CC BY 4.0, code samples MIT (Roblox/creator-docs). Short code excerpts quoted with attribution.
- Access: Read the Markdown source of the page from the public Roblox/creator-docs repository (commit 4e795e6), accessed 2026-10-24. Images, videos and the linked sample places (.rbxl) were **not** opened, and no step was performed in Roblox Studio.

## Workflow in the tutorial [SRC]
1. Enable the Device Emulator to design for phones first.
2. Set `ScreenGui.ScreenInsets` to `DeviceSafeInsets` (instead of the default `CoreUISafeInsets`) to tuck the meter against the top edge, then add padding; keep it right-aligned to avoid Roblox UI.
3. Build parent frame, inner fill and icon with Scale/Offset sizing.
4. Hide the default meter with `StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.Health, false)` from a LocalScript in StarterPlayerScripts.
5. On `Humanoid.HealthChanged`: compute `math.max(0, Health / MaxHealth)`, size the fill, colour it by lerping between five gradient keypoints (red → green), and tween with `TweenInfo.new(0.5, Exponential, Out)`; call once at spawn.

## Decisions and the reasons the tutorial gives [SRC]
| Decision | Reason |
|---|---|
| `DeviceSafeInsets`. | Uses limited screen space better; right alignment avoids the core UI. |
| Tween the fill. | Makes damage readable instead of jumping. |
| Initial call on spawn. | The bar is correct before the first damage event. |

## Our analysis
- **[ANALYSIS]** The five-keypoint colour ramp matches our [AV-21 Damage and Low Health](../08-Animation-and-Game-Feel/Recipes/AV-21-Damage-and-Low-Health.md) recipe; add a non-colour cue (shake or icon) for colour-blind players.
- **[ANALYSIS]** `HealthChanged` reflects server-replicated health — the meter is display only, which is correct.
- **[ANALYSIS]** Creating a new tween on every change is fine; the newer tween overrides the old one for the same properties.

## Common mistakes
- Forgetting to hide the default meter (two bars).
- Using Offset only → wrong size across devices.
- Not reconnecting after respawn (new Humanoid).

## Troubleshooting
| Symptom | Likely cause / fix |
|---|---|
| Meter stops updating after death | Re-bind on `CharacterAdded`; the old Humanoid is gone. |
| Meter under the notch | Check `ScreenInsets` and padding in the emulator. |

## Reusable procedure (ours)
1. Design at phone size in the emulator.
2. Choose ScreenInsets deliberately; add padding.
3. Build with Scale sizes + aspect constraints.
4. Hide the core element you replace.
5. Bind to the source value, update once at start, tween changes.
6. Add a non-colour cue at low values.

## Exercise
Build a stamina meter for 'Obsidian Rush' that fills from heat 0 → 100 using the same structure.

### Acceptance criteria
- [ ] Correct on 3 emulated devices with no overlap with core UI.
- [ ] Updates after respawn.
- [ ] Low values show a cue that works in greyscale (screenshot test).

## Related
- [HUD Layouts](../01-UI-UX/HUD-Layouts.md)
- [LU-16 Tweens and Springs](../07-Roblox-Studio-and-Luau/LU-16-Tweens-and-Springs.md)
- [AV-11 Progress Feedback](../08-Animation-and-Game-Feel/Recipes/AV-11-Progress-Feedback.md)
