# Roblox Trend Scout

Finds **early niches** on Roblox: game ideas that players clearly want (a new game already has
real players) but that **almost nobody has built yet** (1–5 games). Build a better version with
your own twist and own the niche before it blows up and gets flooded with copies.

It runs on your Mac: a background job checks Roblox every 3 hours, and a local dashboard shows
the ranked niches, the games already in each one, and an AI-written top pick with a game concept,
how to beat the existing games and a build plan.

See **[PLAN.md](PLAN.md)** for how it works, the scoring method and the roadmap.

---

## Setup on your Mac (about 10 minutes, once)

### 1. Install Python
Open **https://www.python.org/downloads/macos/**, download the latest **Python 3** macOS installer
and run it. (The Python that comes with macOS is too old.)

### 2. Get the code into your home folder
Open the **Terminal** app (press `Cmd + Space`, type *Terminal*, press Enter) and paste:

```bash
cd ~
git clone -b claude/youthful-darwin-ga0uw1 https://github.com/leoglockner1-dot/Claude.git claude-repo
cd ~/claude-repo/roblox-trend-scout
```

- If `git` asks to install "command line developer tools", click **Install**, wait, then paste
  the commands again.
- If the repo is private, GitHub asks you to sign in. Easiest: install **GitHub Desktop**, sign in,
  *File → Clone repository*, and pick your home folder as the location.
- Keep it in your **home folder**, not Desktop/Documents/Downloads: macOS blocks background
  jobs from those folders.
- To update later: `cd ~/claude-repo && git pull`.

### 3. Run setup
```bash
./setup.sh
```
Answer **Y** when it asks about collecting every 3 hours.

### 4. Add your API keys
```bash
open -e .env
```
Paste your keys after the `=` signs and save:

| Key | Needed? | Where to get it |
|---|---|---|
| `ANTHROPIC_API_KEY` | Yes, for the AI pick | https://console.anthropic.com/ → *API Keys* (add a few dollars of credit; each AI pick costs roughly $0.10–0.25) |
| `YOUTUBE_API_KEY` | Recommended (free) | https://console.cloud.google.com/ → new project → *APIs & Services* → enable **YouTube Data API v3** → *Credentials* → *Create credentials* → *API key* |

Reddit and Roblox need no keys.

### 5. Open the dashboard
Double-click **`start.command`** in Finder (in `claude-repo/roblox-trend-scout`), or run
`./start.command` in Terminal. Your browser opens **http://127.0.0.1:8765**.

The first time, macOS may say the file is from an unidentified developer: right-click it →
**Open** → **Open**.

---

## Using it

1. **Collect now** takes a fresh snapshot (about 4–5 minutes). The background job does this every
   3 hours on its own while your Mac is on.
2. The **Early niches** tab (the default) lists ideas where:
   - the leading game is under **120 days** old and has **500+** players online, and
   - a Roblox search for the idea finds at most **5** games with **100+** players.

   Click one to see the games already in it, why it scored that way and a players-over-time chart.
   Each run checks up to 150 new phrases, so more niches appear over the first day.
3. **All trends** shows the bigger themes for context (mostly crowded already).
4. **Get AI pick** sends the top 12 niches to Claude. It picks the best one for a solo developer
   and writes how to beat the existing games, an original concept, a build plan and the risks.

You can change the niche rules at the top of `trendscout/niches.py` (`MAX_COMPETITORS`,
`MIN_DEMAND`, `NICHE_MAX_AGE_DAYS`, `REAL_PLAYERS`).

**Give it time.** On day one the ranking is based on game age, charts and visit counts. After
~24 hours it can measure real growth, and after ~7 days week-over-week growth too, which is
when the picks become trustworthy.

## Command line (optional)

```bash
cd ~/claude-repo/roblox-trend-scout
.venv/bin/python -m trendscout collect      # take a snapshot now
.venv/bin/python -m trendscout report       # print the ranking
.venv/bin/python -m trendscout recommend    # AI pick, printed as JSON
.venv/bin/python -m trendscout serve        # start the dashboard
```

## Troubleshooting

| Problem | Fix |
|---|---|
| `You need Python 3.10 or newer` | Install Python from python.org (step 1), close and reopen Terminal, run `./setup.sh` again. |
| Dashboard says *Claude key missing* | Put `ANTHROPIC_API_KEY=...` in `.env`, then close the Terminal window running the dashboard and start it again. |
| Background collection isn't happening | Check `logs/collect.log`. Re-install with `./scripts/install_schedule.sh`. The folder must not be on Desktop/Documents/Downloads. |
| Stop background collection | `./scripts/uninstall_schedule.sh` |
| `Address already in use` | The dashboard is already running in another window. Use that, or change `PORT` in `.env`. |
| Reddit/YouTube warnings in the log | Harmless; the tool skips that source for this run. YouTube's free quota resets daily. |

Your data lives in `data/trends.db` (SQLite). Delete it to start fresh.

## Tests
```bash
.venv/bin/python -m unittest discover -s tests
```
