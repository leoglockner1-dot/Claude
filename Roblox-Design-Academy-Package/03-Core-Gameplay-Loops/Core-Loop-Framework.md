---
title: "Core Loop Framework"
tags: [core-loop]
note_type: "topic"
---

# Core Loop Framework

## Roblox's three layers (official)
1. **Minute-to-minute interaction** — constant baseline activity.
2. **Most repeated set of actions** — the defining mechanic.
3. **Progression engine** — without it, Roblox says, a game becomes "repetitive, boring, and shallow".
Source: [Core loops](https://create.roblox.com/docs/production/game-design/core-loops).

## Academy extension: five loop types to map for every game
| Loop | Question | Example (inferred from case studies) |
|---|---|---|
| Main loop | What do players do every 10–60 s? | Steal games: buy → place → steal → defend ([CS-04](../20-Game-Case-Studies/CS-04-Steal-Loop-Games.md)) |
| Supporting loops | What feeds the main loop? | Pre-run shop in DOORS ([CS-07](../20-Game-Case-Studies/CS-07-DOORS.md)) |
| Meta-progression | What persists across sessions? | Weapon keys in RIVALS ([CS-02](../20-Game-Case-Studies/CS-02-RIVALS.md)) |
| Social loop | How do players affect each other? | Runway voting ([CS-03](../20-Game-Case-Studies/CS-03-Dress-To-Impress.md)) |
| Monetization loop | What can be bought, when, why? | Intermission theme props (Roblox docs) |

## The first-session sequence to design explicitly
| Moment | Target | Evidence |
|---|---|---|
| First 10 s | Player knows what they are and where to go (world points, no text walls) | ONB-01…03 |
| First 60 s | Core verb performed, first feedback received | LOOP-002, CS-16 funnel |
| First reward | Within the first minutes, visibly travels to a counter | GF-01, FEEL-005 |
| First upgrade | Changes something visible | PROG-002, V12 counter-example |
| Session end | Moment of joy + visible next goals | ONB-008 |

## Effort ↔ reward
Short cycles (seconds) need small, frequent, consistent feedback; long cycles (minutes) need anticipation and bigger reveals (FEEL-006, R05). Keep the ratio legible: show "how much more until X".

## Why simple games stay engaging (synthesis, Medium confidence)
Observed winners state one verb + stakes in their name/description (99 Nights, Steal a Brainrot, Hot Potato, Tower of Hell) and add depth through **contexts** (randomised towers, rarer eggs, nights) rather than new systems (LOOP-003). Feature-rich games with unclear objectives struggled in developer reports ([CS-17](../20-Game-Case-Studies/CS-17-Outbreak-Mayhem.md)).

## Related
[Core Loop Principles](../17-Design-Principles/Core-Loop-Principles.md) · [Genre Loop Library](Genre-Loop-Library.md) · [R15 Satisfying Core Loop](../18-Skill-Training/Design-Recipes/R15-Satisfying-Core-Loop.md) · [CL 04 Core Loop Review](../23-Quality-Checklists/CL-04-Core-Loop-Review.md)
