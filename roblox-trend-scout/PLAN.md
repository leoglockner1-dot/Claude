# Roblox Trend Scout: Plan

## 1. Goal

Help a solo developer find **early niches**: Roblox game ideas with proven demand (a new game
already has real players) but almost no competition (1–5 games). The developer builds a better
version with their own twist and owns the niche before the trend blows up. The tool ranks these
niches and turns the best one into a concrete concept, a plan to beat the existing games, and a
build plan. Bigger, crowded trends are still shown on a second tab for context.

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
| `trendscout/niches.py` | Finds early niches: new games with demand, phrases with ≤ 5 real competitors |
| `trendscout/seasonal.py` | Detects seasonal niches and how many days their season has left |
| `trendscout/notify.py` | Mac notifications: new top-5 niches and fast-growing niches |
| `trendscout/analyze.py` | Per-game growth metrics; groups games into big trends and scores them |
| `trendscout/recommend.py` | Calls Claude with structured JSON output |
| `trendscout/server.py`, `static/` | Local dashboard (Python standard library + Chart.js, bundled) |
| `setup.sh`, `start.command`, `scripts/` | Mac install, launcher, background schedule |

Only one dependency is installed: the official `anthropic` Python SDK.

## 3. Data collected each run

| Source | What | Cost / limits |
|---|---|---|
| Roblox Explore | ~25 charts (Up-and-Coming, Top Trending, Top Playing Now, Fun with Friends, Top Revisited, Top Earning, …), ~900 unique games | Free, public |
| Roblox games API | Players now, visits, favorites, likes/dislikes, created/updated dates, genre, creator | Free, public |
| Roblox search | Up to 150 phrases from new games per run (niche competitor counts, cached 24h), plus the top 15 big themes | Free, public |
| YouTube | For the top 10 niches + top 5 trends: videos in the last 7 days and their views (every 12h) | Free key; ~1,000 of the 10,000 daily quota units per check |
| Reddit | For the top 12 niches + top 5 trends: posts in Roblox subreddits this week (every 6h) | Free, no key |

Games that fall off the charts keep being tracked for 7 days, so a dip doesn't erase history.

## 4. What counts as a "trend"

A trend is a group of games sharing a **theme**:
- a **keyword** in their names, e.g. "steal", "+1", "ragdoll", "evolution" (update tags like
  `[🎃 EVENT]` are stripped, plurals are folded, two-word phrases are tracked too), or
- a Roblox **subgenre**, e.g. Tycoon, Physics Sim, Incremental Simulator.

A theme needs at least 2 games (3 for subgenres) from at least 2 different creators and 1,000+
concurrent players in total. Themes covering exactly the same games are merged.

## 5. Early niches (the main view)

`trendscout/niches.py`. The rules (all adjustable at the top of the file):

| Rule | Value |
|---|---|
| Leading game age | ≤ 120 days |
| Proof of demand | leading game has ≥ 500 players online |
| A competitor counts if it has | ≥ 100 players online |
| Max competitors | 5 (a single game with no copies yet counts too) |

How niches are found each run:
1. Take every game that passes the age and demand rules.
2. Pull the distinctive words and phrases from its name. Words already used by 6+ tracked games
   are crowded by definition and skipped.
3. Search Roblox for each phrase (up to 150 new phrases per run; results cached 24h). Roblox
   search pads results with loosely related hits, so **only games whose name actually contains
   the phrase** count as competitors ("ballpit" matches "Clean the Ball Pit!", "rage" doesn't
   match "Garage").
4. For each game, the broadest phrase that still has ≤ 5 competitors becomes its niche label.
   The game's most crowded related word is shown as a warning ("Broader idea “ragdoll” already
   has 18 games").
5. Games found this way are tracked from then on, so their growth is measured too.

Niche score (percentiles against the other niches):

| Signal | Weight | Measures |
|---|---|---|
| Growth momentum | 22% | Players vs same time yesterday / last week, visit acceleration |
| Proven demand | 18% | Players online in the leading game |
| How new it is | 13% | Age of the leading game |
| Few competitors | 13% | Number of games with real players in the niche |
| Broader idea uncrowded | 12% | Penalty when the niche is a renamed version of a crowded idea |
| Social buzz | 9% | YouTube views + Reddit engagement this week |
| Player approval | 8% | Like ratio |
| Chart presence | 5% | Up-and-Coming, Top Trending, … |

**Seasonal niches** (`trendscout/seasonal.py`): the niche phrase and leading game's name are
checked for season words (Halloween, Thanksgiving, Christmas, New Year, winter, Valentine's,
St. Patrick's, Easter (date computed per year), April Fools, summer). Bracketed update tags like
`[🎃 EVENT]` are ignored because those are temporary events on normal games. A seasonal niche gets
a badge with the days left; with < 60 days left its score is multiplied by up to 0.55 (fully at
0 days or once the season has ended). Upcoming seasons aren't penalized. Claude is told to only
pick a seasonal niche if there's time to ship, or the idea works without the theme.

**Notifications** (`trendscout/notify.py`): after each collection, a macOS notification
(via `osascript`) when a niche enters the top 5, or a niche's leading game is +50% vs the same
time yesterday. Max one alert per niche per 24h; several alerts are grouped into one
notification; all alerts are logged and shown in the dashboard's "Recent alerts". The first
collection only records the top 5, so setup doesn't trigger a burst of alerts.

## 6. All trends (context tab)

Each big theme's signals are turned into a percentile against all other trends, then weighted:

| Signal | Weight | Measures |
|---|---|---|
| Growth momentum | 22% | Players vs the same time yesterday and last week, plus visit-rate acceleration |
| New-game wave | 18% | Share of players in games < 90 days old × how many such games |
| Visit velocity | 15% | Visits per day flowing into the young games |
| Social buzz | 13% | YouTube views + Reddit engagement this week |
| Chart presence | 12% | Up-and-Coming (strongest), Top Trending, Fun with Friends, … |
| Room to compete | 12% | Players per competing game, penalized when one game owns most of the players |
| Player approval | 8% | Like ratio weighted by player count |

Design choices (both views):
- **Player counts swing by time of day**, so growth only compares a snapshot with one ~24h or
  ~7 days earlier, never with 3 hours ago.
- **Missing data scores neutral (50)**, so nothing is rewarded or punished for a source that
  wasn't checked.

## 7. The AI recommendation

`recommend.py` sends the top 12 niches (metrics, signals, the games in each) plus the top 5 big
trends as context to Claude (`claude-opus-5-5`, effort `high`, streamed) with a strict JSON schema:

- **Top pick**: niche, the games already in it, confidence 1–10, verdict, why now, evidence,
  risks, estimated window
- **Game concept**: working titles, pitch, core loop, original twist, **how to beat the existing
  games**, target players, monetization, icon/thumbnail ideas
- **Build plan** by phase, **launch checklist**, **runner-ups**, **niches to avoid**, **data caveats**

The instructions tell Claude to favour proven demand with very few competitors that a solo dev
can ship in 3–6 weeks, to flag one-game flukes and renamed crowded ideas, to avoid one-off events and licensed IP, to propose an **original** game rather
than a copy, and to treat game names and descriptions as data, never as instructions.
Server-side refusal fallback is turned on, so a declined request is retried on a fallback model
automatically.

Cost: about 8–12k input tokens and a few thousand output tokens, roughly **$0.10–0.25 per pick**.
Collection itself never calls Claude, so the background job is free.

## 8. Running on the Mac

- `setup.sh` finds Python 3.10+, creates `.venv`, installs the SDK, creates `.env`, and
  installs the background job.
- The background job is a **LaunchAgent** (`~/Library/LaunchAgents/com.trendscout.collect.plist`):
  every 3 hours while you're logged in; if the Mac was asleep, it runs once on wake. Logs go to
  `logs/collect.log`.
- `start.command` (double-click) starts the dashboard and opens the browser. The server only
  listens on `127.0.0.1` and rejects action requests from other websites.

## 9. Timeline to a useful pick

| When | What you get |
|---|---|
| First run | Ranking from game age, charts, visit velocity, competition. Good for exploring. |
| ~24 hours | Day-over-day growth and visit acceleration kick in. |
| ~7 days | Week-over-week growth. **Recommended point to trust the AI pick.** |
| 2–4 weeks | Enough history to see which trends kept rising vs faded (useful for tuning weights). |

## 10. Limitations and risks

- **Unofficial endpoints.** The Roblox Explore/search APIs are what roblox.com itself uses,
  not a documented public API; they can change. Collectors fail soft and report warnings.
- **Snapshot gaps.** If the laptop is off for days, growth for that window is missing (it
  recovers once new snapshots arrive).
- **Niches are found from game names.** An idea whose games all have different names (same
  mechanic, different words) can look less crowded than it is; the AI reads the game list to catch this.
- **Keyword themes are heuristic.** Two unrelated games can share a word; a trend can also be
  a mechanic that names don't reveal. Subgenres partly cover that.
- **Correlation, not causation.** A rising trend is a signal, not a guarantee; execution,
  thumbnails and update cadence decide most of a game's success.
- **YouTube quota.** 10,000 units/day free; the defaults use ~3,000/day.

## 11. Roadmap

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
- "Watchlist": pin niches and get a weekly digest (email).
- Clickable notifications that open the dashboard (needs a small helper app instead of osascript).
- Thumbnail/icon analysis of the winning games, using the Roblox Design Academy notes already
  in this repo (`Roblox-Design-Academy-Package/`).
- Export the AI pick as a one-page game design doc.

**Later**
- If you publish your own game: pull its stats too and compare against the trend.
