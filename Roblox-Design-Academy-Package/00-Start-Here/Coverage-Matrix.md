---
title: "Coverage Matrix"
tags: [start-here, meta]
note_type: "start-here"
---

# Coverage Matrix

## Coverage by research domain
| Domain | Coverage | Evidence | Start note |
|---|---|---|---|
| A. UI/UX — HUD, shops, inventory, menus, mobile | **Strong** | 26 UI analyses + 9 topic notes | [UI UX Overview](../01-UI-UX/UI-UX-Overview.md) |
| A. UI/UX — quests, notifications, confirmations, settings | **Medium** | Quest panels (UI-16, GF-01), destructive actions (UI-20), mixer (V05) | [Rewards Progress and Notifications](../01-UI-UX/Rewards-Progress-and-Notifications.md) |
| A. UI/UX — loading, death/respawn, round transitions | **Medium** | V18, V21/V22, V08/V09, DevForum death screen (text only) | [Loading Death and Round Transitions](../01-UI-UX/Loading-Death-and-Round-Transitions.md) |
| A. UI/UX — social interfaces, matchmaking, limited-time events UI | **Weak** | Season pass (UI-04), lobby voting (UI-24); no direct captures of social/matchmaking UIs of top games | [Menus and Navigation](../01-UI-UX/Menus-and-Navigation.md) |
| B. Thumbnails & icons | **Strong** | 30 analyses, 85-game chart study, brief template, composition checklist | [Thumbnail Principles](../02-Thumbnails-and-Icons/Thumbnail-Principles.md) |
| C. Core loops & mechanics | **Medium-Strong** | 54 case studies (inferred loops), 15-field framework, 3 worked concepts, 19 mechanics, 6 developer post-mortems; no gameplay played/watched | [Core Loop Evaluation Framework](../03-Core-Gameplay-Loops/Core-Loop-Evaluation-Framework.md) |
| D. Progression, rewards, economy | **Strong (data) / Medium (design)** | 1,041-pass study, odds policy, reward presentation | [Game Pass Economy Study](../05-Progression-and-Economy/Game-Pass-Economy-Study.md) |
| E. Animation, VFX, game feel | **Medium-Strong** | 19 video notes with measured timing; docs-only footage | [Timing Reference](../08-Animation-and-Game-Feel/Timing-Reference.md) |
| F. Sound design | **Medium** | Measured (not listened) audio from 12 videos; recipes are synthesized | [Measured Audio Observations](../10-Sound-Design/Measured-Audio-Observations.md) |
| G. Visual identity & art direction | **Medium-Strong** | Framework, style catalogue, identity analyses | [Visual Identity Framework](../11-Visual-Identity/Visual-Identity-Framework.md) |
| H. Level design & environmental communication | **Weak** | 8 docs-based references; no level walkthroughs | [Environmental Communication](../12-Level-Design/Environmental-Communication.md) |
| I. Onboarding & FTUE | **Strong** | Roblox guidance + 6 analyses + developer funnel data | [Onboarding Evidence From Developers](../13-Onboarding-and-Multiplayer/Onboarding/Onboarding-Evidence-From-Developers.md) |
| J. Social & multiplayer | **Medium** | Case studies, co-op thumbnails, low-population/bot guidance (largely synthesized) | [Cooperative and Social Design](../13-Onboarding-and-Multiplayer/Multiplayer/Cooperative-and-Social-Design.md) |
| K. Technical constraints | **Strong** | 11 verified reference notes | [Roblox Platform Facts](../14-Technical-Reference/Roblox-Platform-Facts.md) |
| L. Anti-patterns | **Strong** | 28 anti-patterns with evidence + AI-look detection | [Anti Pattern Catalog](../15-Anti-Patterns-and-Failure-Cases/Anti-Pattern-Catalog.md) |
| N. Blender & 3D assets (2.0) | **Strong (technical) / Medium (visual quality)** | 22 procedures, 10 executed exercises with renders, QC JSON and exports, 6 real failures fixed; no Studio import, no human art review | [Blender Training Index](../06-Blender-and-3D-Assets/Blender-Training-Index.md) |
| O. Luau & Studio (2.0) | **Strong (logic) / Weak (engine)** | 28 procedures, 13 modules, 54 passing specs, 2 tutorial defects reproduced; no Studio runs | [Luau Training Index](../07-Roblox-Studio-and-Luau/Luau-Training-Index.md) |
| P. Tutorials, benchmarks, self-critique (2.0) | **Strong** | 16 tutorials → procedures, 18 benchmarks (15 executed), self-critique loop with 8 logged cycles | [Benchmark Index](../19-Benchmarks-and-Practical-Exams/Benchmark-Index.md) |
| M. External references | **Weak-Medium** | NN/g ×3, Apple HIG ×2; several sites inaccessible | [External Design Sources](../22-Source-Library/External-Design-Sources.md) |

## Academy 2.0 coverage targets (requested vs actual, 2026-10-24)
Targets are from the 2.0 brief; actual = files present (see [MANIFEST](../MANIFEST.md)).

| Target | Requested | Actual | Met? | Note |
|---|---|---|---|---|
| Roblox game case studies | 40+ | 54 | ✅ | Public data only; gameplay not observed |
| Useful visual references | 80+ | 367 third-party files + 123 original renders/screenshots | ✅ | Third-party media fetched by script, private study |
| Video analyses of content actually inspected | 20+ | 19 notes covering 29 official videos | ⚠️ partly | 29 videos inspected, grouped into 19 notes; YouTube blocked, so no new videos in 2.0 |
| Actionable design principles | 50+ | 128 | ✅ | |
| Practical Blender/3D procedures | 20+ | 22 procedures + 10 executed exercises (+3 specs) | ✅ | Studio import unverified |
| Core-loop and mechanic analyses | 20+ | 19 mechanics + 3 worked loop concepts + 6 documented loop failures = 28 | ✅ | Loops of live games are inferred |
| Luau/Roblox technical procedures | 20+ | 28 (LU-00…LU-27) | ✅ | Logic tested with the Luau CLI; not in Studio |
| Animation, VFX and sound recipes | 20+ | 23 AV recipes (+15 design recipes) | ✅ | Previews synthesized |
| Tutorials transformed into procedures | 15+ | 16 | ✅ | Official text tutorials; no video tutorials |
| Repeatable benchmarks | 15+ | 18 (15 executed, 1 partly, 2 spec only) | ✅ | Self-graded |
| Complete QA checklists | 10+ | 14 | ✅ | |

**Not met / partly met:** video analyses (19 notes, below the 20 target). No new video could be watched in 2.0 because video hosts are blocked, and the academy did not pad the count by splitting existing notes.

## v1 coverage targets (for reference)

| Target | Requested | Actual |
|---|---|---|
| Distinct Roblox games investigated | ≥40 | 85 (live data) + 17 named in Roblox docs examples + 15 DevForum projects ≈ 117 (overlaps removed approx.) |
| Useful visual references | ≥80 | 367 asset files; ≈290 images actually inspected (85 icons, 103 thumbnails, 48 docs images, ~55 DevForum images, sheets) |
| Gameplay-video/animation analyses | ≥20 | 29 official videos in 19 notes (no YouTube gameplay — blocked) |
| UI/UX analyses | ≥25 | 26 |
| Thumbnail/icon analyses | ≥20 | 30 |
| Animation/VFX/sound breakdowns | ≥15 | 19 video notes + GF-01 + timing/audio data notes |
| Negative or mixed examples | ≥15 | ≈40 analyses rated Negative or Mixed + 28 anti-patterns |
| Authoritative technical/professional sources | ≥15 | ≈45 Roblox docs pages + 5 external pages |
| Actionable principles | ≥50 | 94 |
| Checklists | ≥10 | 12 + design critique checklist + composition checklist |
| Recipes | ≥10 | 15 |

Counts are actual files/analyses present in this package (see [MANIFEST](../MANIFEST.md)). Weak areas are listed in [Research Limitations](Research-Limitations.md).
