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

## Academy 2.0 session (2026-10-24)
| Source | Result | Consequence |
|---|---|---|
| Roblox creator-docs (GitHub, sparse clone, commit 4e795e6) | ✅ | Tutorials, specs and security pages read as Markdown source |
| media.githubusercontent.com (Git LFS media of creator-docs) | ✅ | Docs images/videos fetched where needed (e.g. the reserved-zones illustration measured for BM-03; not committed) |
| raw.githubusercontent.com | ✅ (LFS files return pointer text only) | Used for text files |
| docs.blender.org (5.2 LTS manual) | ✅ | 8 manual pages read; cited in BL notes |
| PyPI (`bpy` 5.2.3) | ✅ | Blender run headless for all exercises |
| github.com/luau-lang/luau | ✅ | Luau CLI built from source (commit 32c2808) |
| Roblox APIs: games, votes, game passes, omni-search, thumbnails | ✅ | 113 games collected; data for case studies CS-19…CS-54 |
| badges.roblox.com | ❌ blocked by network policy | Badge data not used |
| devforum.roblox.com (search and topic JSON) | ✅ | Post-mortems and threads for FC-GD notes and case studies |
| gamedeveloper.com, 80.lv, romonitorstats.com | ✅ reachable | Little used; no claims depend on them |
| en.wikipedia.org, *.fandom.com | ❌ blocked by network policy | Game wikis not used; case studies rely on Roblox data and developer posts |
| YouTube video pages | ❌ blocked | **No video tutorial or gameplay video watched** |
| Sportskeeda, Dexerto, Polygon, PC Gamer, Game Rant and similar | ❌ blocked by network policy | Not used |
| Roblox Studio | ❌ not available (Linux container, no Studio) | **No in-Studio verification** of any import, script or UI; marked "not verified" throughout |

Network access for blocked hosts can be changed in the cloud environment's settings (Network access), see <https://code.claude.com/docs/en/cloud-environments#network-access>.
