---
title: "Roblox Development Academy 2.0 — Overview"
tags: [start-here]
note_type: "start-here"
---

# Roblox Development Academy 2.0 — Overview

**Purpose:** make the next Roblox game better than it would have been by improving five things: **design** (what makes it engaging and readable), **execution** (working systems and assets), **judgment** (spotting weak work and why), **validation** (checking real output against criteria) and **learning** (keeping mistakes and fixes).

## How to use it on a real task (agent or human)
1. **Find the area.** Use [Master Index → Find by question](Master-Index.md).
2. **Read the rule and its evidence.** Open the matching principles file in `17-Design-Principles/` and one or two linked case studies or analyses. Check the confidence label.
3. **Write acceptance criteria first.** Take them from the relevant checklist ([Checklist Index](../23-Quality-Checklists/Checklist-Index.md)) and benchmark ([Benchmark Index](../19-Benchmarks-and-Practical-Exams/Benchmark-Index.md)).
4. **Follow a procedure.** Blender: `BL-xx` notes and the `_tools/blender` toolkit. Luau: `LU-xx` notes and the tested modules in `_tools/luau/src`. Feel: `AV-xx` recipes. Tutorials: `TUT-xx`.
5. **Inspect the real output** and run the [Self-Critique Loop](../18-Skill-Training/Self-Critique-Loop.md). Name defects with their causes, fix one cause at a time, re-run all checks.
6. **Check the failure library** when something breaks ([Failure and Correction Index](../15-Anti-Patterns-and-Failure-Cases/Failure-and-Correction-Index.md)).
7. **Record what you learned** as a new failure entry, principle or exercise result, in the same templates.

## When not to use a rule
Every principle lists *conditions*. A rule from a simulator case study may be wrong for a horror game. The academy deliberately avoids a single house style: the case studies span genres, and the visual-identity notes ask you to derive style from the game's intended experience.

## Structure
| Folder | Contents |
|---|---|
| 00-Start-Here | Overview, master index, methodology, quality standard, limitations, coverage, tracker |
| 01-UI-UX | Topic notes + 26 UI analyses |
| 02-Thumbnails-and-Icons | Principles, 85-game chart study, 30 analyses |
| 03-Core-Gameplay-Loops | 15-field evaluation framework, loop library (3 concepts for one theme), documented loop failures |
| 04-Game-Mechanics | 19 mechanics with conditions, exploits and Roblox notes |
| 05-Progression-and-Economy | Progression, reward presentation, pass economy study, odds and fairness |
| 06-Blender-and-3D-Assets | BL-00…BL-21 procedures, 10 executed exercises (+3 specs), training index |
| 07-Roblox-Studio-and-Luau | LU-00…LU-27 procedures linked to tested modules |
| 08-Animation-and-Game-Feel | Timing reference, feedback notes, AV-01…AV-23 recipes |
| 09-VFX | VFX principles and performance |
| 10-Sound-Design | Principles, recipes, measured audio |
| 11-Visual-Identity | Identity framework, styles, world-to-UI |
| 12-Level-Design | Environmental communication |
| 13-Onboarding-and-Multiplayer | First session, funnel evidence, co-op, low population |
| 14-Technical-Reference | Verified engine/platform facts |
| 15-Anti-Patterns-and-Failure-Cases | 28 anti-patterns, 13 real failures, 6 developer post-mortems, failure index |
| 16-Tutorials-and-Workflows | 16 official tutorials converted to procedures |
| 17-Design-Principles | 128 principles in 14 domains |
| 18-Skill-Training | Self-critique loop, 15 design recipes |
| 19-Benchmarks-and-Practical-Exams | 18 benchmarks with criteria, rubrics and the academy's own runs |
| 20-Game-Case-Studies | 54 case studies + cross-game patterns |
| 21-Video-Analyses | 19 notes on 29 official Roblox videos |
| 22-Source-Library | Sources by type, every external link, access log |
| 23-Quality-Checklists | 14 checklists |
| Assets | `Original/` (made here) + third-party reference media (fetched) |
| _tools | Validator, asset fetcher, safe copy, Blender/Luau/UI/AV tooling |

Start with [Master Index](Master-Index.md) · [Design Quality Standard](Design-Quality-Standard.md) · [Research Limitations](Research-Limitations.md).
