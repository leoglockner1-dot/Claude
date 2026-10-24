---
title: "Social & Multiplayer Principles (SOCIAL-001 – SOCIAL-006)"
tags: [principles, multiplayer]
note_type: "principles"
---

# Social & Multiplayer Principles (SOCIAL-001 – SOCIAL-006)

Multiplayer design principles for Roblox audiences.

| ID | Principle | Confidence |
|---|---|---|
| SOCIAL-001 | Design for friends joining | High |
| SOCIAL-002 | Make roles legible | Medium |
| SOCIAL-003 | Solo fallback for every multiplayer loop | Medium |
| SOCIAL-004 | Let players be content for each other | High |
| SOCIAL-005 | Visible social status | Medium |
| SOCIAL-006 | Support streamers | High |

## SOCIAL-001 — Design for friends joining
**Rule:** Make it easy and rewarding to play with friends (shared goals, bonuses, free private servers).

- **Reasoning:** Roblox: social connection is a core platform strength.
- **Evidence:** [Cooperative and Social Design](../13-Onboarding-and-Multiplayer/Multiplayer/Cooperative-and-Social-Design.md), [CS 11 Tycoon Group](../20-Game-Case-Studies/CS-11-Tycoon-Group.md)
- **Good application:** Raft Tycoon: "+10 % per friend"; several co-op games advertise free VIP servers.
- **Failure mode:** Private servers priced prohibitively (Roblox warns).
- **Conditions & exceptions:** Pressure-to-invite mechanics are not social design.
- **Roblox implementation:** Friend detection via `Player:IsFriendsWith`; group bonuses.
- **Confidence:** High
- **Tags:** #multiplayer

## SOCIAL-002 — Make roles legible
**Rule:** In co-op/asymmetric games, each player's role and link are visible in world and marketing.

- **Reasoning:** Comprehension of the partner role is the hook.
- **Evidence:** [TI 22 Asymmetric CoOp Explained In One Image](../02-Thumbnails-and-Icons/Analyses/TI-22-Asymmetric-CoOp-Explained-In-One-Image.md), [CS 09 Small CoOp Games](../20-Game-Case-Studies/CS-09-Small-CoOp-Games.md)
- **Good application:** Be My Camera: "CAN'T SEE" / "CAMERA".
- **Failure mode:** Hidden role differences.
- **Conditions & exceptions:** —
- **Roblox implementation:** Role-coloured outlines (`Highlight`), role HUD badge.
- **Confidence:** Medium
- **Tags:** #multiplayer

## SOCIAL-003 — Solo fallback for every multiplayer loop
**Rule:** Every core loop can be completed with one player (bots, scaling, async).

- **Reasoning:** Low-population servers are common; empty servers kill games (developer concern).
- **Evidence:** [Low Population Design](../13-Onboarding-and-Multiplayer/Multiplayer/Low-Population-Design.md)
- **Good application:** Waiting-room shooting gallery idea (DevForum).
- **Failure mode:** Team game unplayable alone.
- **Conditions & exceptions:** Strict 2-player games must make matchmaking effortless instead.
- **Roblox implementation:** NPC bots, difficulty scaling by player count.
- **Confidence:** Medium
- **Tags:** #multiplayer #ai-bots

## SOCIAL-004 — Let players be content for each other
**Rule:** Give tools for expression and interaction (emotes, building, trading, roleplay props).

- **Reasoning:** Roblox: roleplay games thrive on player-generated situations.
- **Evidence:** [CS 08 Brookhaven](../20-Game-Case-Studies/CS-08-Brookhaven.md), [CS 03 Dress To Impress](../20-Game-Case-Studies/CS-03-Dress-To-Impress.md)
- **Good application:** Runway voting in Dress To Impress.
- **Failure mode:** No way to show off or interact.
- **Conditions & exceptions:** —
- **Roblox implementation:** Emote wheel, voting, trading UIs.
- **Confidence:** High
- **Tags:** #multiplayer

## SOCIAL-005 — Visible social status
**Rule:** Let achievements and cosmetics be seen by others (titles, auras, pets).

- **Reasoning:** Avatar expression matters to Roblox players (Roblox design doc).
- **Evidence:** [Game Pass Economy Study](../05-Progression-and-Economy/Game-Pass-Economy-Study.md)
- **Good application:** Trails/auras are the largest pass category.
- **Failure mode:** Rewards only visible in menus.
- **Conditions & exceptions:** —
- **Roblox implementation:** Overhead `BillboardGui` titles, cosmetic slots.
- **Confidence:** Medium
- **Tags:** #multiplayer #economy

## SOCIAL-006 — Support streamers
**Rule:** Offer a hide-UI / creator camera mode and moments that read well on video.

- **Reasoning:** Roblox cites Brookhaven's Creator Cam; influencers drive discovery.
- **Evidence:** [CS 08 Brookhaven](../20-Game-Case-Studies/CS-08-Brookhaven.md)
- **Good application:** Creator Cam toggle.
- **Failure mode:** UI that cannot be hidden.
- **Conditions & exceptions:** —
- **Roblox implementation:** Settings toggle that disables ScreenGuis + free camera.
- **Confidence:** High
- **Tags:** #multiplayer #marketing
