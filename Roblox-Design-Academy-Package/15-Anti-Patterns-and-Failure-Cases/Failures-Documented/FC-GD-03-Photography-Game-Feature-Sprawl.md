---
title: "FC-GD-03- — Be A Photographer: feature sprawl, AI-generated UI clutter and a hollow core activity"
tags: [failure-case, documented, core-loop, ui, economy, scope]
note_type: "failure-case"
evidence: "documented by the game's developer on the Roblox DevForum (2026-09-22); diagnosis by community replies; correction NOT tested by the academy"
source: "https://devforum.roblox.com/t/looking-for-testers-on-my-game-user-retention-sucks-players-do-not-complete-a-lot-fo-the-game/4888167"
---

# Be A Photographer: feature sprawl, AI-generated UI clutter and a hollow core activity

| Field | Record |
|---|---|
| **Problem** | Be A Photographer: feature sprawl, AI-generated UI clutter and a hollow core activity |
| **Source** | [https://devforum.roblox.com/t/looking-for-testers-on-my-game-user-retention-sucks-players-do-not-complete-a-lot-fo-the-game/4888167](https://devforum.roblox.com/t/looking-for-testers-on-my-game-user-retention-sucks-players-do-not-complete-a-lot-fo-the-game/4888167) (2026-09-22) |
| **Context** | Photography game with a boat and camera; tested with ads. Players joined and left quickly. |
| **Observable symptoms (as reported)** | A reviewer said they knew within 10 seconds that the like ratio was low because of "millions of layers of horrendous vibe coded UI"; unclear short- and long-term goals; an unpicturesque map; a tiny hidden stamina bar with no consequence; skill trees that could be cut; reward popups that are a hassle to click through; like/join-group popups. Economy: display income repaid the whole gallery's value roughly every 100 s, and spam-click selling allowed low-effort income. Progression locked behind randomness; too many camera bodies; player data reset with an update. |
| **Cause (reported / suggested)** | Reviewer diagnosis: the 'keep it simple' choice removed the fun part of photography (zoom, focus, exposure) and left "an empty shell of the activity", while many unrelated features added clutter. AI-built UI prototypes had "no regard for UX or proper styling". |
| **Correction** | Reviewer advice (not tested by us): a scenic map; make the core activity believable (camera modes unlocked over time); cut the fluff; rebuild the economy with separate currencies for selling and for displaying; deliberate purchases instead of slot machines; hand-design a few UI screens, write the rules into stylesheets, then extend; never wipe persistent progress without warning. |
| **How the correction was tested** | Not tested by the academy; outcome unknown unless stated in the thread. |
| **Reusable lesson** | The fun of a simulator comes from the *activity's own decisions*. Simplifying them away to add systems produces a game with many features and no core. |
| **Related** | [UI-25 AI look](../../01-UI-UX/Analyses/UI-25-DevForum-Roll-a-Cupcake-AI-Look.md), [AI and Template Look Detection](../AI-and-Template-Look-Detection.md), [AP-25 Unnecessary systems](../Anti-Pattern-Catalog.md) |
