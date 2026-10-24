---
title: "Low-Population and Solo Design"
tags: [multiplayer, ai-bots]
note_type: "topic"
---

# Low-Population and Solo Design

Many servers have few players (small games in the sample run 45–2,000 concurrent across all servers). Design so a game feels alive at 1–3 players.

## Techniques (general practice + DevForum discussion; Medium confidence)
- **Bots/NPC opponents** that fill rounds and leave when humans join (relevant to an AI-bot system).
- **Scale objectives** by player count (enemy HP, round timer).
- **Asynchronous presence**: ghosts of other runs, leaderboards, gallery of other players' creations.
- **Waiting-room activities** (DevForum: a shooting gallery while waiting — thread 707797).
- **Solo modes for co-op games** (helper NPC) — co-op titles with weak ratings might suffer from solo arrivals (hypothesis, CS-09).
- **Server merging/matchmaking** for party games (Roblox matchmaking docs).

## Bot design checklist (for AI bots)
- Bots must read as bots (name tag/marker) unless the design deliberately hides it — be honest with players.
- Bot skill ramps with player skill; bots never steal rare rewards from humans.
- Bots demonstrate the core verb (teaching by example).
- Bots should create social moments (emotes, simple callouts).

Checklist: [CL 10 Multiplayer and Low Population](../../23-Quality-Checklists/CL-10-Multiplayer-and-Low-Population.md)
