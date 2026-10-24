---
title: "Loading, Death, Respawn and Round Transitions"
tags: [ui, transitions]
note_type: "topic"
---

# Loading, Death, Respawn and Round Transitions

## Evidence
- Spinner-only loading ([V18](../16-Video-Analyses/V18-Loading-Spinner.md)): fine for short waits; for longer waits add identity + progress (NN/g: percent-done for >~10 s).
- Respawn fades ≈0.7 s; scene transport ≈1.2 s black + blur→focus ([V21/V22](../16-Video-Analyses/V21-V22-Duvall-Cutscene-and-Respawn.md)).
- Victory/defeat: same layout, different words/timbre; lacks motion ([V08/V09](../16-Video-Analyses/V08-V09-Victory-and-Defeat-Screens.md)).
- DevForum death-screen critique: numbers that bounce are hard to read; zoom the camera so the UI is not the only death signal (thread 4744175).

## Rules
- Death: show cause (what killed you), cost (what you lost), and the fastest way back.
- Round transitions: countdown to next round, results in ≤3 s, skip for repeat players.
- Loading: `ReplicatedFirst` UI, `PreloadAsync` progress, tips relevant to current map.
