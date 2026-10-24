---
title: "Game Data Sources (Roblox APIs)"
tags: [sources, data]
note_type: "sources"
---

# Game Data Sources (Roblox APIs)

Accessed 2026-10-24 from the research environment (US region):
| Endpoint | Purpose |
|---|---|
| `https://apis.roblox.com/explore-api/v1/get-sorts?device=all&country=all` (+ `sortsPageToken`) | Chart sorts and game lists |
| `https://apis.roblox.com/search-api/omni-search?searchQuery=…` | Genre searches |
| `https://games.roblox.com/v1/games?universeIds=…` | Names, genres, visits, playing, created/updated, descriptions |
| `https://games.roblox.com/v1/games/votes?universeIds=…` | Up/down votes |
| `https://thumbnails.roblox.com/v1/games/icons` · `/v1/games/multiget/thumbnails` | Icon/thumbnail URLs (images from `tr.rbxcdn.com`) |
| `https://apis.roblox.com/game-passes/v1/universes/{id}/game-passes?passView=Full` | Pass names/prices |

All 85 games with links and stats: [Live Chart Study 2026 10](../02-Thumbnails-and-Icons/Live-Chart-Study-2026-10.md). Every saved image's source URL is recorded in `_tools/asset-sources.json` (re-fetch with `_tools/fetch_assets.py`).

**Note:** thumbnail CDN URLs are time-limited (`180DAY-` prefix); the saved copies are the evidence of what was observed on 2026-10-24.
