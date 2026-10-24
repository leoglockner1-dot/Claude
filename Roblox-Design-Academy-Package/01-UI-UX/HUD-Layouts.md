---
title: "HUD Layouts"
tags: [ui, hud]
note_type: "topic"
---

# HUD Layouts

## What the evidence shows
- **Centre clear, edges busy.** Survival Game, Super Striker League and TURBOSTORM keep the play focus free and park information in corners ([UI 03 The Survival Game Minimal HUD](Analyses/UI-03-The-Survival-Game-Minimal-HUD.md) · [UI 02 Super Striker League Context Buttons](Analyses/UI-02-Super-Striker-League-Context-Buttons.md) · [UI 24 DevForum TURBOSTORM Racing HUD and Lobby](Analyses/UI-24-DevForum-TURBOSTORM-Racing-HUD-and-Lobby.md)).
- **Colour = live state; neutral = navigation.** Health/hunger bars carry colour; menu buttons stay muted (UI-03).
- **Context-swap actions** (Tackle/Sprint ↔ Deke/Pass) instead of showing everything (UI-02).
- **Genre conventions** speed comprehension: racing (position list top-left, timer + map top-right, speedometer bottom-right), survival (bars top-right, hotbar bottom-centre).
- **Feedback stack** for combat answers separate questions (hit? how much? danger? reward?) ([GF-01](../05-Animation-and-Game-Feel/Analyses/GF-01-Winds-of-Fortune-Combat-Feedback.md)).
- **Meters**: tween ≈0.25 s perceived, colour + length, peripheral flash for damage ([V06/V07](../16-Video-Analyses/V06-V07-HUD-Meter-Tween-and-Damage-Flash.md)).

## Layout template (adapt, don't copy)
| Zone | Typical content | Notes |
|---|---|---|
| Top-left | Roblox top bar (reserved) → below it: objectives/quests | Use `CoreUISafeInsets` |
| Top-centre | Round timer, banners, contextual ability prompts | Short-lived only |
| Top-right | Vital stats (health, energy), currency | Colour-coded |
| Centre | Nothing persistent | Hit markers, reticle only |
| Bottom-centre | Hotbar (≤5 early) | Number hints on keyboard only |
| Bottom-right | Primary touch actions (thumb zone) | ≥44 pt hit targets (Apple HIG) |
| Bottom-left | Movement stick (Roblox default on touch) | Don't place buttons here on mobile |
| Edges | Menu buttons (shop, inventory) in one family | Progressive disclosure |

## Rules
UI-001, UI-003, UI-005, UI-012, UI-016, TECH-001 — see [UI Principles](../14-Design-Principles/UI-Principles.md).

## Recipe
[R02 Clean Readable Gameplay HUD](../13-Reusable-Design-Recipes/R02-Clean-Readable-Gameplay-HUD.md)

## Common mistakes
Two button languages in one HUD (UI-02), translucent buttons over bright terrain, centre overlays during action (UI-24), keyboard letters shown on touch (UI-03), default-template stacks (UI-19).
