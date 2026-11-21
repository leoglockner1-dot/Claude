# Roblox Trend Scout: Plan

## 1. Goal

Help a solo or small-team developer decide **which Roblox game to build next** by finding
trends that are rising *before* they peak, ranking them, and turning the best one into a concrete
game concept and build plan.

Requirements:
- Runs on a Mac laptop at home, set up with one script.
- Collects data automatically in the background every ~3 hours.
- A local browser dashboard: ranking, evidence, charts, AI pick.
- Data sources: Roblox charts and game stats, YouTube, Reddit.
- An AI (Claude) writes the final recommendation and reasoning.

## 2. How it works

```
 every 3h (macOS launchd)           on demand (dashboard button)
          │                                   │
          ▼                                   ▼
 ┌─────────────────┐  SQLite   ┌──────────────────┐   top 10   ┌───────────────────┐
 │ collect.py      │──────────▶│ analyze.py       │──────────▶│ recommend.py      │
 │ Roblox charts   │ snapshots │ build themes,    │  trends    │ Claude: top pick, │
 │ game stats      │           │ growth metrics,  │            │ concept, plan     │
 │ competition     │           │ 0–100 score      │            └─────────┬─────────┘
 │ YouTube/Reddit  │           └────────┬─────────┘                      │
 └─────────────────┘                    ▼                                ▼
                               ┌──────────────────────────────────────────────────┐
                               │ server.py + static/  →  http://127.0.0.1:8765     │
                               └──────────────────────────────────────────────────┘
```

| File | Job |
|---|---|
| `trendscout/roblox.py` | Roblox Explore charts (`explore-api/get-sorts`), game details, votes, search |
| `trendscout/social.py` | YouTube Data API (videos + views in the last 7 days), Reddit search |
| `trendscout/collect.py` | One collection run; writes snapshots to `data/trends.db` |
| `trendscout/analyze.py` | Groups games into trends, computes metrics, scores them |
| `trendscout/recommend.py` | Calls Claude with structured JSON output |
| `trendscout/server.py`, `static/` | Local dashboard (Python standard library + Chart.js, bundled) |
| `setup.sh`, `start.command`, `scripts/` | Mac install, launcher, background schedule |

Only one dependency is installed: the official `anthropic` Python SDK.

## 3. Data collected each run

| Source | What | Cost / limits |
|---|---|---|
| Roblox Explore | ~25 charts (Up-and-Coming, Top Trending, Top Playing Now, Fun with Friends, Top Revisited, Top Earning, …), ~900 unique games | Free, public |
| Roblox games API | Players now, visits, favorites, likes/dislikes, created/updated dates, genre, creator | Free, public |
| Roblox search | For the top 15 themes: how many games compete and how concentrated the players are | Free, public |
| YouTube | For the top 10 themes: videos in the last 7 days and their views (every 12h) | Free key; ~1,000 of the 10,000 daily quota units per check |
| Reddit | For the top 12 themes: posts in Roblox subreddits this week (every 6h) | Free, no key |

Games that fall off the charts keep being tracked for 7 days, so a dip doesn't erase history.

## 4. What counts as a "trend"

A trend is a group of games sharing a **theme**:
- a **keyword** in their names, e.g. "steal", "+1", "ragdoll", "evolution" (update tags like
  `[🎃 EVENT]` are stripped, plurals are folded, two-word phrases are tracked too), or
- a Roblox **subgenre**, e.g. Tycoon, Physics Sim, Incremental Simulator.

A theme needs at least 2 games (3 for subgenres) from at least 2 different creators and 1,000+
concurrent players in total. Themes covering exactly the same games are merged.

## 5. Scoring (0–100)

Each signal is turned into a percentile against all other trends (so it adapts to whatever
the market looks like), then weighted:

| Signal | Weight | Measures |
|---|---|---|
| Growth momentum | 22% | Players vs the same time yesterday and last week, plus visit-rate acceleration |
| New-game wave | 18% | Share of players in games < 90 days old × how many such games |
| Visit velocity | 15% | Visits per day flowing into the young games |
| Social buzz | 13% | YouTube views + Reddit engagement this week |
| Chart presence | 12% | Up-and-Coming (strongest), Top Trending, Fun with Friends, … |
| Room to compete | 12% | Players per competing game, penalized when one game owns most of the players |
| Player approval | 8% | Like ratio weighted by player count |

Design choices:
- **Player counts swing by time of day**, so growth only compares a snapshot with one ~24h or
  ~7 days earlier, never with 3 hours ago.
- **Missing data scores neutral (50)**, so a trend isn't rewarded or punished for a source
  that wasn't checked.
- **Weights live in one place** (`WEIGHTS` in `analyze.py`) so they can be tuned.

## 6. The AI recommendation

`recommend.py` sends the top 10 trends (metrics, signals, top 6 games each) to Claude
(`claude-opus-5-5`, effort `high`, streamed) with a strict JSON schema, so the dashboard always
gets the same fields:

- **Top pick**: trend, confidence 1–10, verdict, why now, evidence, risks, estimated window
- **Game concept**: working titles, pitch, core loop, original twist, target players,
  monetization, icon/thumbnail ideas
- **Build plan** by phase, **launch checklist**, **runner-ups**, **trends to avoid**, **data caveats**

The instructions tell Claude to favour young, multi-creator, growing themes a solo dev can ship
in 3–6 weeks, to avoid one-off events and licensed IP, to propose an **original** game rather
than a copy, and to treat game names and descriptions as data, never as instructions.
Server-side refusal fallback is turned on, so a declined request is retried on a fallback model
automatically.

Cost: about 12k input tokens and a few thousand output tokens, roughly **$0.10–0.25 per pick**.
Collection itself never calls Claude, so the background job is free.

## 7. Running on the Mac

- `setup.sh` finds Python 3.10+, creates `.venv`, installs the SDK, creates `.env`, and
  installs the background job.
- The background job is a **LaunchAgent** (`~/Library/LaunchAgents/com.trendscout.collect.plist`):
  every 3 hours while you're logged in; if the Mac was asleep, it runs once on wake. Logs go to
  `logs/collect.log`.
- `start.command` (double-click) starts the dashboard and opens the browser. The server only
  listens on `127.0.0.1` and rejects action requests from other websites.

## 8. Timeline to a useful pick

| When | What you get |
|---|---|
| First run | Ranking from game age, charts, visit velocity, competition. Good for exploring. |
| ~24 hours | Day-over-day growth and visit acceleration kick in. |
| ~7 days | Week-over-week growth. **Recommended point to trust the AI pick.** |
| 2–4 weeks | Enough history to see which trends kept rising vs faded (useful for tuning weights). |

## 9. Limitations and risks

- **Unofficial endpoints.** The Roblox Explore/search APIs are what roblox.com itself uses,
  not a documented public API; they can change. Collectors fail soft and report warnings.
- **Snapshot gaps.** If the laptop is off for days, growth for that window is missing (it
  recovers once new snapshots arrive).
- **Keyword themes are heuristic.** Two unrelated games can share a word; a trend can also be
  a mechanic that names don't reveal. Subgenres partly cover that.
- **Correlation, not causation.** A rising trend is a signal, not a guarantee; execution,
  thumbnails and update cadence decide most of a game's success.
- **YouTube quota.** 10,000 units/day free; the defaults use ~2,000/day.

## 10. Roadmap

**v1 (built now):** collection, trend detection, scoring, AI pick, dashboard, Mac scheduler, tests.

**v1.1 – quality (next 1–2 weeks of data)**
- Backtest: score trends from 7 days ago and check which actually grew; tune `WEIGHTS`.
- Trend history: score over time for each trend, "new this week" and "fading" badges.
- Seasonal flag (Halloween, Christmas, summer) so short event spikes are labeled.

**v1.2 – more signals**
- Google Trends search interest (optional, rate-limited).
- TikTok/YouTube Shorts mentions if a reliable free source exists.
- Game update frequency (how often top games in a theme push updates).

**v1.3 – decision support**
- "Watchlist": pin trends and get a weekly digest (macOS notification or email).
- Thumbnail/icon analysis of the winning games, using the Roblox Design Academy notes already
  in this repo (`Roblox-Design-Academy-Package/`).
- Export the AI pick as a one-page game design doc.

**Later**
- If you publish your own game: pull its stats too and compare against the trend.
