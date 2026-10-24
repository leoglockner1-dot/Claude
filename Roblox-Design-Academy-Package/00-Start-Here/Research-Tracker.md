---
title: "Research Tracker"
tags: [meta]
note_type: "meta"
---

# Research Tracker

## Phase 1 — Capabilities (2026-10-24)
| Source | Status | Use |
|---|---|---|
| Roblox Creator Docs (create.roblox.com + GitHub mirror commit 4e795e6) | ✅ | Technical facts, official design guidance, 835 official videos |
| Roblox web APIs (explore, games, thumbnails, game-passes) | ✅ | Charts, game metadata, icons, thumbnails, pass prices |
| roblox.com game pages | ⚠️ JS-rendered; APIs used instead | — |
| DevForum (search/topic JSON + upload CDN) | ✅ | Developer UI/feedback threads with screenshots |
| YouTube | ❌ Google bot-check ("Sign in to confirm you're not a bot") on video and page requests; only cover images (i.ytimg.com) load | No gameplay-video analysis possible; not bypassed |
| Material Design, Apple HIG, NN/g, FMOD, Unity, Blender docs, 80.lv, Mobbin | ✅ reachable | Supporting general principles |
| W3C, GDC Vault, Game Developer, web.archive.org, Figma.com | ❌ timeout | — |
| ArtStation, Epic docs | ❌ 403 | — |
| Tools | ffmpeg ✅, Pillow/numpy ✅, yt-dlp installed but blocked by YouTube | Frame extraction, timing and waveform measurement on docs videos |

## Final state (2026-10-24)
| Item | Count |
|---|---|
| Categories researched | 13 domains (see [Coverage Matrix](Coverage-Matrix.md)) |
| Roblox docs pages used | ≈45 |
| DevForum threads read | 30 |
| External pages | 5 (NN/g ×3, Apple HIG ×2) |
| Live games with data | 85 (icons 85, thumbnails 268 fetched, 103 saved) |
| Game passes analysed | 1,041 (695 for sale) |
| Official videos analysed | 29 (19 notes) |
| Reference analyses | 64 (+19 video notes, 18 case studies) |
| Principles | 94 |
| Recipes | 15 |
| Checklists | 12 (+ critique + composition) |
| Anti-patterns | 28 |
| Assets | 367 files (+ registry) |

## Access failures
YouTube (bot check — not bypassed); W3C, GDC Vault, Game Developer, web.archive.org, figma.com (timeouts); ArtStation, Epic docs (403); Material & FMOD (JS-only); some DevForum searches (HTTP 429). Details: [Access Log](../22-Source-Library/Access-Log.md)

## Remaining gaps → next highest-value tasks
1. Capture in-game UI of 20 top games (screenshots + 10 s clips **with sound**) — fills social/matchmaking/event UI gaps.
2. Measure reward reveals (eggs/crates) in 5 top simulators (timing + audio).
3. Level-design walkthrough captures (spawn → first goal) for 10 games.
4. Listen-based audio review (the research could only measure waveforms).
5. Re-run the chart study outside the Halloween season to separate seasonal effects.
