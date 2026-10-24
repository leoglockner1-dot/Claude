---
title: "FC-GD-02- — Battle Cars: a repetitive core loop, visible bugs and inconsistent UI led to dislikes and no organic traffic"
tags: [failure-case, documented, core-loop, bugs, ui, content-cost]
note_type: "failure-case"
evidence: "documented by the game's developer on the Roblox DevForum (2026-08-07); diagnosis by community replies; correction NOT tested by the academy"
source: "https://devforum.roblox.com/t/help-diagnosing-high-dislikes-low-retention-in-battle-cars-vehicular-combat/4781013"
---

# Battle Cars: a repetitive core loop, visible bugs and inconsistent UI led to dislikes and no organic traffic

| Field | Record |
|---|---|
| **Problem** | Battle Cars: a repetitive core loop, visible bugs and inconsistent UI led to dislikes and no organic traffic |
| **Source** | [https://devforum.roblox.com/t/help-diagnosing-high-dislikes-low-retention-in-battle-cars-vehicular-combat/4781013](https://devforum.roblox.com/t/help-diagnosing-high-dislikes-low-retention-in-battle-cars-vehicular-combat/4781013) (2026-08-07) |
| **Context** | Solo developer; vehicular arena combat. Stated loop: spawn → battle → earn → upgrade/customize in the garage. |
| **Observable symptoms (as reported)** | High dislike ratio, low retention, "dead when I don't run ads". Testers found an AI driver stuck in a wall, unscaled and mismatched UI ("loads of different colours and styles"), a map mixing ultra-high-poly and super-low-poly assets, a car spawned on top of another car, and a camera broken after leaving the gunner seat. |
| **Cause (reported / suggested)** | Community: the deathmatch loop is fun for minutes but "very repetitive" (developer agreed: "ok I've seen it all after 5 minutes"), with no long-term goals. Bugs and an inconsistent art style hurt the like ratio and the play-through rate. The developer added that solo content production (cars, parts) is too slow to feed an unlock-based meta, and AI-generated models needed heavy fixing. |
| **Correction** | Not tested by us. Implied: design progression that is cheap to extend (mastery, challenges, modes, loadout combinations) instead of content-hungry unlocks; fix the visible bugs that new players hit in the first minutes; unify the art and UI style. |
| **How the correction was tested** | Not tested by the academy; outcome unknown unless stated in the thread. |
| **Reusable lesson** | Choose a meta loop you can produce content for at your team's speed. A developer who knows how to avoid the bugs no longer sees them; fresh testers do. |
| **Related** | [AP-21 Repetitive core loop](../Anti-Pattern-Catalog.md), [BL-20](../../06-Blender-and-3D-Assets/BL-20-Modeling-Quality-Framework.md) (style consistency) |
