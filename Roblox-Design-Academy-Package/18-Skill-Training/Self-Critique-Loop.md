---
title: "Self-Critique Loop (mandatory for every exercise and benchmark)"
tags: [skill-training, process, critique, quality]
note_type: "method"
evidence: "derived from this academy's own executed exercises; each step cites the failure that taught it"
---

# Self-Critique Loop

Every exercise, benchmark and asset in this academy goes through this loop. Each rule exists because skipping it caused a real failure in this package, and the failure is linked.

```
1 Criteria → 2 Make v1 → 3 Inspect output → 4 Name defects → 5 Fix one cause → 6 Re-run ALL checks → 7 Decide
      ↑                                                                                              │
      └───────────────────────────────── if any criterion fails (max 4 versions) ───────────────────┘
```

## 1. Write the acceptance criteria before making anything
- Make them observable: "reads as a pick in a gameplay-distance silhouette", not "looks good".
- Mark each criterion with its source: Roblox spec, documented guidance, or house rule.
- **If a criterion turns out to be wrong, change it openly.** Record the old one, why it was wrong and the new one. Never quietly loosen it.
  *Learned from:* modular kit criterion K2 required a 5-stud footprint for 1-stud walls ([BL-EX-09](../06-Blender-and-3D-Assets/Exercises/BL-EX-09-Modular-Building-Kit.md)).

## 2. Make v1 quickly
v1 exists to be inspected. Don't polish before the first inspection.

## 3. Inspect the output, not your intention
- Look at the render, the screenshot, the test log or the measurement: the actual artefact.
- **Never write v2 critique before v1 exists.** Predicted defects are hypotheses, not findings.
  *Learned from:* [FC-ART-01](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-ART-01-Pre-Written-Critique.md). The pre-written critique included defects that did not exist and missed real ones.
- Use more than one view: orthographic, 3/4, silhouette at gameplay distance, and at small size. For UI, use several devices. For sound, listen and measure the duration.
- Check the presentation too: a ground plane hid pivots in our renders ([BL-11](../06-Blender-and-3D-Assets/BL-11-Lighting-and-Rendering.md)).

## 4. Name each defect and its cause
| Write | Not |
|---|---|
| "At 3/4 the head reads as an umbrella canopy because the profile is a crescent." | "Pickaxe looks off." |
| "Coin emboss disappears below 64 px: relief too shallow for the size." | "Needs more detail." |
| "Spec v1 reused one state; the mutation defect masked the boundary test." | "Test flaky." |

A defect without a cause leads to a guessed fix. *Learned from:* thickening the pickaxe head (v2) **failed**, because the cause was the profile, not the thickness ([BL-EX-05](../06-Blender-and-3D-Assets/Exercises/BL-EX-05-Pickaxe-Tool.md)).

## 5. Fix one cause at a time
Change the thing the cause names and nothing else, so the next inspection tells you whether the diagnosis was right.

## 6. Re-run every check, not only the one you were fixing
Fixes create new defects.
*Learned from:* the n-gon fix created T-junctions ([FC-BL-03](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-BL-03-Ngon-Fix-Created-T-Junction.md)), and the chest's bevels plus exact contact left a hinge gap ([FC-BL-05](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-BL-05-Exact-Contact-Leaves-Gap.md)).

**Check your checks.** An automated check that passes can be wrong. Probe it with a case that must fail.
*Learned from:* three blind spots in our own validators ([FC-QA-01](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-QA-01-Validator-Blind-Spots.md)). The BM-03 HUD checker passed a layout whose progress cue was weak, and it never tested elements against each other ([BM-03](../19-Benchmarks-and-Practical-Exams/BM-03-Fix-Mobile-HUD-Hierarchy.md)).

**Check claims against sources.** Any statement like "the engine guarantees X" gets looked up in the docs before it is written.
*Learned from:* [FC-RES-01](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-RES-01-Assumed-Engine-Guarantee.md).

## 7. Decide
- **All criteria pass:** ship. Record the final evidence and the version history, failed versions included.
- **A criterion fails and fewer than 4 versions exist:** loop to step 3.
- **Still failing after v4:** stop. Record the item as *not passed*, with the remaining defects and what you would try next. A documented failure is a valid result; a hidden one is not.

## Version log template
```
### vN
- Change: <the one cause addressed>
- Inspection: <views/tests used, links to renders/logs>
- Result per criterion: <pass/fail each>
- New defects found: <named, with cause>
```

## Questions to ask at every inspection
1. What would a player see in the first second (silhouette, contrast, motion)?
2. Does it still work at the smallest size, on the smallest device, and at the quietest volume?
3. Which criterion am I *least* sure about, and have I actually checked it?
4. Is anything here copied from a reference's identity (character, layout, branding)?
5. What did I not test, and is that written down?

## Where this loop was applied (evidence)
| Item | Versions | Notable failed version |
|---|---|---|
| [Treasure chests](../06-Blender-and-3D-Assets/Exercises/BL-EX-04-Treasure-Chests.md) | 4 | Premium read as a crate; cartoon read as a sofa |
| [Pickaxe](../06-Blender-and-3D-Assets/Exercises/BL-EX-05-Pickaxe-Tool.md) | 3 | v2 thickness fix did not work |
| [Rocks](../06-Blender-and-3D-Assets/Exercises/BL-EX-01-Stylized-Rocks.md) | 2 | Boulder read as an egg |
| [Modular kit](../06-Blender-and-3D-Assets/Exercises/BL-EX-09-Modular-Building-Kit.md) | 2 | Non-manifold doorway; criterion revised |
| [Coin burst](../08-Animation-and-Game-Feel/Recipes/AV-03-Collecting.md) | 2 | v1 did not read |
| [BM-02 spec](../19-Benchmarks-and-Practical-Exams/BM-02-Debug-Buggy-Luau-Module.md) | 2 | One defect masked another |
| [BM-03 HUD](../19-Benchmarks-and-Practical-Exams/BM-03-Fix-Mobile-HUD-Hierarchy.md) | 2 | Checker pass hid a weak progress cue |
| [TUT-14](../16-Tutorials-and-Workflows/TUT-14-Proximity-Prompts.md) | 2 | Unchecked engine-guarantee claim |

## Related
- [Design Quality Standard](../00-Start-Here/Design-Quality-Standard.md)
- [Failure and Correction Index](../15-Anti-Patterns-and-Failure-Cases/Failure-and-Correction-Index.md)
- [Benchmark Index](../19-Benchmarks-and-Practical-Exams/Benchmark-Index.md)
