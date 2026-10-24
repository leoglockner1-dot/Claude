---
title: "R01 — Polished main menu"
tags: [recipe, ui, menus]
note_type: "recipe"
---

# R01 — Polished main menu

## 1. Goal
A menu that gets players into play in one tap while expressing the game's identity.

## 2. When to use
Games with a pre-play menu or lobby screen (story, competitive, round-based).

## 3. Required inputs
Identity statement (motif, palette roles, type pair); list of destinations; background scene or animated world view.

## 4. Recommended structure
- **Left or centre column**: logo → **one primary button** (accent colour, largest) → 3–5 secondary buttons (neutral) → small progress summary (level, currency).
- **Background**: live world camera or slow pan of a signature location (not a static blur).
- Settings and credits as small icons; destructive actions only inside sub-screens with confirmation.

## 5. Step-by-step implementation
1. Write the identity statement and pick tokens (Style Editor).
2. Build one `MenuButton` component (normal/hover/pressed/selected/disabled states).
3. Place primary + secondary buttons in a `UIListLayout` (spacing from token).
4. Background: `Camera` CFrame tween along 2–3 points (slow, 20–40 s loop) or a living lobby.
5. Primary button calls the play flow directly; secondary open panels with one shared panel component.
6. Gamepad: set `GuiService.SelectedObject` to the primary button on open; set `NextSelection*` for column order.
7. Instrument: funnel step "Pressed Play".

## 6. Animation guidance
Menu enters with a 0.2–0.3 s fade + slight upward offset (Quad Out); buttons hover-scale 1.04 (0.08 s); primary may breathe subtly (scale 1.00↔1.02, 2 s) — only one element animates idly.

## 7. Sound guidance
Soft hover tick (optional), press pop, short brand sting when Play pressed; menu music bed fades out over ~0.5 s into gameplay.

## 8. Mobile considerations
Primary button ≥ 44 pt tall and in thumb reach; keep text ≥ phone-readable minimum; no hover-only information.

## 9. Performance considerations
Avoid heavy blur/post-processing on the menu background on mobile; preload the first gameplay assets while the menu is open.

## 10. Common mistakes
Buttons same size as the logo (UI-18 critique); rainbow button lists (UI-24); emoji icons; three modals on open; menus that block joining friends.

## 11. QA checklist
- [ ] Exactly one accent-coloured element
- [ ] Play reachable in 1 tap/click/button
- [ ] Gamepad selection starts on Play
- [ ] Looks correct at Small/Medium/Large viewport sizes
- [ ] No overlap with Roblox top bar

## 12. References & confidence
[UI 18 DevForum Package Inspector Main Menu](../01-UI-UX/Analyses/UI-18-DevForum-Package-Inspector-Main-Menu.md) · [UI 24 DevForum TURBOSTORM Racing HUD and Lobby](../01-UI-UX/Analyses/UI-24-DevForum-TURBOSTORM-Racing-HUD-and-Lobby.md) · [UI Principles](../14-Design-Principles/UI-Principles.md)

**Confidence:** High for structure (observed + docs); Medium for timing values (hypotheses).
