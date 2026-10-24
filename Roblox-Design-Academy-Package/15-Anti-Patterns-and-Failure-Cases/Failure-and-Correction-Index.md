---
title: "Failure and Correction Index"
tags: [index, failure-case, anti-pattern, qa]
note_type: "index"
---

# Failure and Correction Index

Three kinds of entries, always labelled:
- **A. Real failures from this academy's own work.** Observed and fixed in this session, with the evidence linked.
- **B. Documented failures of other developers.** Reported in DevForum threads or shown as "don't" examples in Roblox docs. The cause is the community's or Roblox's diagnosis; the correction was **not** tested by us.
- **C. Generalized anti-patterns.** Patterns abstracted from many references ([Anti-Pattern Catalog](Anti-Pattern-Catalog.md)). Not single experiments.

Every A entry records the problem, context, symptoms, cause, correction, how it was tested, the result and the reusable lesson.

## A. Real failures (this session)
| ID | Area | Failure | Lesson |
|---|---|---|---|
| [FC-LU-01](Failures/FC-LU-01-Luau-Type-Alias-Parse-Error-Silent-Require.md) | Luau | A bare tuple type alias broke parsing; `require` returned the error string | Type-check every file before running tests |
| [FC-LU-02](Failures/FC-LU-02-Float-Truncation-HUD-Numbers.md) | Luau / UI | HUD showed 9.86M for 9,870,000 | Boundary-test display math; epsilon before floor |
| [FC-BL-01](Failures/FC-BL-01-Headless-EEVEE-Needs-EGL.md) | Blender / environment | EEVEE crashed headless (no EGL) | Probe engines first; Cycles fallback |
| [FC-BL-02](Failures/FC-BL-02-Bmesh-Import-Order.md) | Blender / Python | `bmesh` import failed before `bpy` | Import bpy first |
| [FC-BL-03](Failures/FC-BL-03-Ngon-Fix-Created-T-Junction.md) | Geometry | The n-gon fix created non-manifold T-junctions | Re-run the full QC after every fix |
| [FC-BL-04](Failures/FC-BL-04-Rotation-Around-World-Origin.md) | Blender / transforms | Coins flung by rotating around the world origin | Rotate in mesh space |
| [FC-BL-05](Failures/FC-BL-05-Exact-Contact-Leaves-Gap.md) | Modeling | Bevelled parts touching exactly left a gap | Overlap slightly |
| [FC-BL-06](Failures/FC-BL-06-Stale-Matrix-World.md) | Blender / pivot | Pivot off by 1.5 studs from a stale matrix | Update the view layer before reading transforms |
| [FC-QA-01](Failures/FC-QA-01-Validator-Blind-Spots.md) | QA tooling | Three of my own checks gave false results | Validate the validator |
| [FC-ART-01](Failures/FC-ART-01-Pre-Written-Critique.md) | Process | Critique written before seeing the render | Critique follows evidence |
| [FC-WF-01](Failures/FC-WF-01-Pkill-Matched-Own-Shell.md) | Workflow | `pkill -f` killed its own launcher | Kill by PID |
| [FC-RES-01](Failures/FC-RES-01-Assumed-Engine-Guarantee.md) | Research / security | Draft claimed a prompt trigger proves proximity; the security docs say otherwise | Check security pages before stating engine guarantees |
| [FC-DATA-01](Failures/FC-DATA-01-Lost-Gitignored-Assets.md) | Workflow / assets | 367 gitignored media files lost | Anything uncommittable needs a committed rebuild path |

Also recorded inside the exercise notes (each with before/after evidence):
- Visual design defects: premium chest read as a crate; cartoon chest read as a sofa, then a floating slab; pickaxe read as an umbrella (thickness fix failed, profile fix worked); boulder read as an egg; coin emboss invisible at small sizes; VFX render blown out. See [BL-EX-04](../06-Blender-and-3D-Assets/Exercises/BL-EX-04-Treasure-Chests.md), [BL-EX-05](../06-Blender-and-3D-Assets/Exercises/BL-EX-05-Pickaxe-Tool.md), [BL-EX-01](../06-Blender-and-3D-Assets/Exercises/BL-EX-01-Stylized-Rocks.md), [BL-EX-02](../06-Blender-and-3D-Assets/Exercises/BL-EX-02-Collectible-Gem-and-Coin.md), [BL-EX-12](../06-Blender-and-3D-Assets/Exercises/BL-EX-12-VFX-Geometry.md).
- Presentation defect: the ground plane hid centre- and grip-pivot assets in inspection renders ([BL-11](../06-Blender-and-3D-Assets/BL-11-Lighting-and-Rendering.md)).
- Mis-specified acceptance criterion (a 5-grid footprint for 1-stud walls), corrected openly ([BL-EX-09](../06-Blender-and-3D-Assets/Exercises/BL-EX-09-Modular-Building-Kit.md)).
- UI benchmark failures and fixes: see [Benchmarks](../19-Benchmarks-and-Practical-Exams/Benchmark-Index.md).

## B. Documented failures of other developers (sources linked; corrections not tested by us)
| Area | Case | Source note |
|---|---|---|
| Onboarding | Forced, blurred tutorial; about a 30% onboarding rate reported by the developer | [ONB-06](../13-Onboarding-and-Multiplayer/Onboarding/Analyses/ONB-06-DevForum-Forced-Blur-Tutorial-Funnel.md) |
| Onboarding / retention | Developers asking why playtime is low, ratings terrible, or players don't understand the game | [Onboarding Evidence From Developers](../13-Onboarding-and-Multiplayer/Onboarding/Onboarding-Evidence-From-Developers.md) |
| Core loop / funnel | Troll-tower obby funnel analysis | [CS-16](../20-Game-Case-Studies/CS-16-Troll-Tower-Obby-Funnel.md) |
| Thumbnails | Unclear thumbnail; stretched non-16:9 upload (Roblox docs "don't" examples) | [TI-02](../02-Thumbnails-and-Icons/Analyses/TI-02-Unclear-Thumbnail-and-Stretched-Upload.md) |
| Icons | Default, low-res, ambiguous and non-square icons (Roblox docs) | [TI-06](../02-Thumbnails-and-Icons/Analyses/TI-06-Icon-Failures.md) |
| Thumbnails | Placeholder thumbnail; weak at small size | [TI-18](../02-Thumbnails-and-Icons/Analyses/TI-18-Placeholder-Thumbnail.md), [TI-19](../02-Thumbnails-and-Icons/Analyses/TI-19-Weak-At-Small-Size.md) |
| Thumbnail video | Inaccurate gameplay video vs accurate (Roblox docs pair) | [V02/V03](../21-Video-Analyses/V02-V03-Thumbnail-Videos-Accurate-vs-Misleading.md) |
| UI | Harsh pack shop; inconsistent quest/shop styles; over-decorated portfolio UI; AI-looking UI | [UI-15](../01-UI-UX/Analyses/UI-15-DevForum-Harsh-Pack-Shop.md), [UI-16](../01-UI-UX/Analyses/UI-16-DevForum-Inconsistent-Quest-and-Shop.md), [UI-21](../01-UI-UX/Analyses/UI-21-DevForum-Overdecorated-Portfolio-UI.md), [UI-25](../01-UI-UX/Analyses/UI-25-DevForum-Roll-a-Cupcake-AI-Look.md) |
| Game feel | Blaster without cooldown vs with cooldown (Roblox docs comparison) | [V10/V11](../21-Video-Analyses/V10-V11-Blaster-Cooldown-vs-Spam.md) |
| Audio | The same scene with and without sound (Roblox docs) | [V23/V24](../21-Video-Analyses/V23-V24-Duvall-Pantry-With-and-Without-Sound.md) |
| Accessibility | Information conveyed only by sound (Roblox docs) | [V04](../21-Video-Analyses/V04-Sound-Reliance-Phone.md) |
| Luau security | NaN bypassing range checks in a trade system (Roblox docs example) | [LU-05](../07-Roblox-Studio-and-Luau/LU-05-Server-Validation.md) |
| Performance | Duplicate mesh ids preventing instancing; leaked connections on Player objects (Roblox docs) | [LU-23](../07-Roblox-Studio-and-Luau/LU-23-Performance-Profiling.md), [LU-20](../07-Roblox-Studio-and-Luau/LU-20-Signals-and-Cleanup.md) |
| Data | Saving defaults over real data after a failed load (widely reported pattern; Roblox's sample guards against it with session locking) | [LU-08](../07-Roblox-Studio-and-Luau/LU-08-Player-Data-Persistence.md) |
| Official tutorial code | *Script an upgrade button*: coin check before a yield, deduction after it (two purchases pass) | [TUT-01](../16-Tutorials-and-Workflows/TUT-01-Upgrade-Button-Server-Purchase.md) — **reproduced by us in a Luau simulation** |
| Official tutorial code | *Save player data*: a failed load followed by collecting gold lets autosave overwrite the real save (500 → 10) | [TUT-13](../16-Tutorials-and-Workflows/TUT-13-Save-Player-Data-Safely.md) — **reproduced by us in a Luau simulation** |
| Core loop / retention | Six developer post-mortems from the DevForum (retention collapse, repetitive loop, feature sprawl, generic first impression, tutorial money gap, engaged core with low D1) | [FC-GD-01…06](../03-Core-Gameplay-Loops/Core-Loop-Failure-Cases.md) (files in `Failures-Documented/`) |
More documented cases from the game-design research: [Core Loop Failure Cases](../03-Core-Gameplay-Loops/Core-Loop-Failure-Cases.md).

## C. Generalized anti-patterns
[Anti-Pattern Catalog](Anti-Pattern-Catalog.md) (AP-01…AP-28) · [AI and Template Look Detection](AI-and-Template-Look-Detection.md) · [Design Critique Checklist](Design-Critique-Checklist.md)

## Coverage gaps (honest)
No first-hand failure cases yet for **audio production**, **mobile device testing** or **live performance profiling**: those need Studio or devices, which were not available. Documented cases (section B) partly cover them.
