---
title: "Access Log and Limitations by Source"
tags: [sources, limitations]
note_type: "sources"
---

# Access Log and Limitations by Source

| Source | Result | Consequence |
|---|---|---|
| YouTube watch pages & video | ❌ redirected to Google "sorry"/bot check; yt-dlp: "Sign in to confirm you're not a bot" | **No YouTube gameplay analysed.** Not bypassed. |
| roblox.com game pages | ⚠️ JS-rendered; APIs used | Descriptions/stats from APIs |
| create.roblox.com | ✅ (after network change) + GitHub mirror | Docs verified |
| DevForum | ✅ with 429 rate limits on search | 30 threads read; some searches failed (thumbnail feedback, vfx feedback, mobile ui, postmortem, retention, lobby/map feedback) |
| Roblox APIs (explore/games/thumbnails/game-passes) | ✅ | 85 games, 268 images, 1,041 passes |
| tr.rbxcdn.com | ✅ | Images saved |
| NN/g, Apple developer | ✅ via curl | Quoted |
| Material, FMOD | ⚠️ JS apps, no text | Not used |
| W3C, GDC Vault, gamedeveloper.com, web.archive.org, figma.com | ❌ timeout | Not used |
| ArtStation, Epic docs | ❌ 403 | Not used |
| WebFetch tool | ❌ DNS for several hosts; curl used instead | — |
