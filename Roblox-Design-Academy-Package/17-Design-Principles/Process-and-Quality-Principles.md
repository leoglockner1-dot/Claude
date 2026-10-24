---
title: "Process and Quality Principles (PROC-001 – PROC-008)"
tags: [principles, proc]
note_type: "principles"
---

# Process and Quality Principles (PROC-001 – PROC-008)

How to work: self-critique, validation and honesty rules, each learned from a real event in this session.

| ID | Principle | Confidence |
|---|---|---|
| PROC-001 | Critique follows evidence | Medium-high |
| PROC-002 | Rank defects by impact | Medium-high |
| PROC-003 | Re-run every check after a fix | Medium-high |
| PROC-004 | Validate the validator | Medium-high |
| PROC-005 | A failed fix diagnoses the cause | Medium-high |
| PROC-006 | Question the criterion | Medium-high |
| PROC-007 | State what was not verified | Medium-high |
| PROC-008 | Rebuildable evidence | Medium-high |

## PROC-001 — Critique follows evidence
**Rule:** Write defects only after inspecting the actual output; label pre-planned changes as hypotheses.

- **Reasoning:** Pre-written critique invented defects and missed real ones.
- **Evidence:** [FC-ART-01](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-ART-01-Pre-Written-Critique.md).
- **Good application:** Props v2 rewritten after viewing v1.
- **Failure mode:** Notes claiming defects no one saw.
- **Conditions & exceptions:** —
- **Roblox implementation:** Inspection sheet first, defect list second.

## PROC-002 — Rank defects by impact
**Rule:** Fix the defect that breaks identity or function first; polish last.

- **Reasoning:** Limited iterations; the biggest defect masks others.
- **Evidence:** Chest iteration log ([BL-EX-04](../06-Blender-and-3D-Assets/Exercises/BL-EX-04-Treasure-Chests.md)).
- **Good application:** Sofa-looking chest fixed before n-gons.
- **Failure mode:** Polishing bevels on an unreadable object.
- **Conditions & exceptions:** Blocking QC FAILs (export-breaking) can jump the queue.
- **Roblox implementation:** Numbered defect list in every iteration note.

## PROC-003 — Re-run every check after a fix
**Rule:** After each fix, re-run the full check suite, not only the check that failed.

- **Reasoning:** The n-gon fix created non-manifold edges.
- **Evidence:** [FC-BL-03](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-BL-03-Ngon-Fix-Created-T-Junction.md).
- **Good application:** Full QC per iteration.
- **Failure mode:** Regressions shipped.
- **Conditions & exceptions:** —
- **Roblox implementation:** Scripts that always run the whole suite.

## PROC-004 — Validate the validator
**Rule:** Probe every automated check with known edge cases before trusting it.

- **Reasoning:** Three checks in this session gave false results.
- **Evidence:** [FC-QA-01](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-QA-01-Validator-Blind-Spots.md).
- **Good application:** Ray-cast probe at 9.99…10.01.
- **Failure mode:** Shipping because a broken check said 'pass'.
- **Conditions & exceptions:** —
- **Roblox implementation:** A tests-for-tests habit.

## PROC-005 — A failed fix diagnoses the cause
**Rule:** If a fix doesn't change the symptom, the assumed cause is wrong; change hypothesis, not magnitude.

- **Reasoning:** Pickaxe: a thicker head didn't fix the umbrella read; a profile change did.
- **Evidence:** [BL-EX-05](../06-Blender-and-3D-Assets/Exercises/BL-EX-05-Pickaxe-Tool.md).
- **Good application:** —
- **Failure mode:** Endlessly tweaking one slider.
- **Conditions & exceptions:** —
- **Roblox implementation:** Write the hypothesis next to each change.

## PROC-006 — Question the criterion
**Rule:** When an acceptance criterion fails, first check whether the criterion itself is right, and record any revision openly.

- **Reasoning:** A 5-grid footprint rule wrongly failed 1-stud walls.
- **Evidence:** [BL-EX-09](../06-Blender-and-3D-Assets/Exercises/BL-EX-09-Modular-Building-Kit.md).
- **Good application:** Revised K2 with a note.
- **Failure mode:** Silently changing goals to pass, or 'fixing' a correct asset.
- **Conditions & exceptions:** —
- **Roblox implementation:** Criteria versioned in the exercise note.

## PROC-007 — State what was not verified
**Rule:** Every result says what remains unverified (e.g. Studio import, real devices, gameplay observation).

- **Reasoning:** Honest scope prevents false confidence downstream.
- **Evidence:** All exercise notes; case study method boxes.
- **Good application:** 'Studio import not tested' in BL-15.
- **Failure mode:** Implying platform verification from a Blender round trip.
- **Conditions & exceptions:** —
- **Roblox implementation:** A 'Not verified' section in every note.

## PROC-008 — Rebuildable evidence
**Rule:** Anything that cannot be committed (third-party media) needs a committed, tested way to rebuild it.

- **Reasoning:** 367 media files were lost once.
- **Evidence:** [FC-DATA-01](../15-Anti-Patterns-and-Failure-Cases/Failures/FC-DATA-01-Lost-Gitignored-Assets.md).
- **Good application:** fetch_assets.py tested from an empty copy.
- **Failure mode:** Broken image links after a container reset.
- **Conditions & exceptions:** —
- **Roblox implementation:** asset-sources.json + fetch script.
