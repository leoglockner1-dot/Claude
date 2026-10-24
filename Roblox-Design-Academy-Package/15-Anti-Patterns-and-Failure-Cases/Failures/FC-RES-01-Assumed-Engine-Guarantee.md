---
title: "FC-RES-01 — Research: I assumed an engine guarantee (prompt proximity) that the security docs contradict"
tags: [failure-case, research, security, method]
note_type: "failure-case"
evidence: "real failure observed in this session (2026-10-24)"
---

# Research: I assumed an engine guarantee (prompt proximity) that the security docs contradict

| Field | Record |
|---|---|
| **Problem** | A draft of [TUT-14](../../16-Tutorials-and-Workflows/TUT-14-Proximity-Prompts.md) said a `ProximityPrompt` trigger "proves the player was near". |
| **Context** | Converting the official proximity-prompt tutorial into a procedure. The tutorial itself makes no such claim; I inferred it from the prompt's `MaxActivationDistance`. |
| **Observable symptoms** | None in the note itself: the claim read plausibly. It surfaced while checking a different claim (Touched range) in `scripting/security/security-tactics.md`, which lists "Trigger client-initiated events such as Touched events or ProximityPrompt activations at any range or frequency" as an exploiter capability. |
| **Cause (established)** | I treated a client-side presentation setting (activation distance) as a server-side guarantee, without checking the security documentation. |
| **Correction** | TUT-14 now says the trigger does not prove proximity, cites the page, and adds an acceptance criterion: a trigger simulated from 40 studs is refused by a server distance check. The correction is noted inside TUT-14. |
| **How the correction was tested** | Source check only: the sentence was read in the creator-docs Markdown (commit 4e795e6). Not tested in Studio. |
| **Final result** | Fixed in the note before publishing. |
| **Reusable lesson** | For every "the engine guarantees X" statement about client-triggered events, search the security pages for that event name before writing it down. |
| **Related** | [TUT-02](../../16-Tutorials-and-Workflows/TUT-02-Player-Hazards-and-Collectibles.md), [LU-05 Server Validation](../../07-Roblox-Studio-and-Luau/LU-05-Server-Validation.md) |
