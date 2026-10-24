---
title: "Research Tracker"
tags: [meta]
note_type: "meta"
---

# Research Tracker

## Academy 2.0 — final state (2026-10-24)
| Item | Count / status |
|---|---|
| Categories covered | 16 domains (A–P in [Coverage Matrix](Coverage-Matrix.md)) |
| Games examined | 113 collected via Roblox APIs in 2.0; 54 written up as case studies; 85 in the v1 chart study (overlapping) |
| Sources inspected | 320 distinct external URLs cited in notes ([All External Links](../22-Source-Library/All-External-Links.md)), plus 367 asset source URLs in the registry; creator-docs pages read as Markdown; 8 Blender manual pages; 47 DevForum topics cited |
| Assets saved | 123 original (renders, QC JSON, exports, audio, GIFs, screenshots, test logs) + 367 third-party (registry, re-fetchable) |
| Tutorials analysed | 16 official Roblox tutorials (text); 0 video tutorials (blocked) |
| Principles | 128 (34 added in 2.0) |
| Recipes | 23 AV recipes + 15 design recipes |
| Benchmarks | 18 (15 executed, 1 partly, 2 specification only) |
| Checklists | 14 |
| Tests completed | Luau: 54 module specs + 6 tutorial-defect repros + BM-02 spec (buggy fails 6, fixed passes 9); Blender: QC + round-trip export on 10 exercises; BM-03: Playwright HUD checks at 2 viewports; validator: 0 broken links; fetch_assets from empty: 352 created + 15 derived, 0 failed; safe_copy tested on a fake vault |
| Real failures logged | 13 ([Failure index](../15-Anti-Patterns-and-Failure-Cases/Failure-and-Correction-Index.md)) |

### 2.0 access failures
Wikipedia, Fandom, YouTube video pages, games-press sites (Sportskeeda, Dexerto, Polygon, PC Gamer, Game Rant) and badges.roblox.com are blocked by the environment's network policy. Roblox Studio is unavailable. Details: [Access Log](../22-Source-Library/Access-Log.md).

### 2.0 remaining gaps → next highest-value tasks
1. **Studio verification pass:** import the 10 Blender exports, run the Luau modules in a test place, and check BM-03-style layouts with the real Device Emulator. Record results in the exercise notes.
2. **Play and record 10 case-study games** (first 5 minutes with sound) to replace inferred loops with observed ones.
3. **Playtest one Core Loop Library concept** with fresh players (BM-18) and attach the results.
4. **Execute BM-17** (an original thumbnail and icon tested in a genre grid).
5. **BM-12 pacing table** against a stated income model.
6. **Video analyses:** add at least one more inspected video when a video host is reachable (target 20 notes).

---

# v1 tracker (kept for history)

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
