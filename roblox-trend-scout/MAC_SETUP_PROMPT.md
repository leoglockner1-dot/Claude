# Prompt for setting up Roblox Trend Scout on a Mac with Claude Code

Copy everything inside the box below and paste it as your first message in a new
**Claude Code** chat on your Mac (desktop app or `claude` in Terminal).

````text
Please set up my "Roblox Trend Scout" tool on this Mac and get it fully running. I'm a beginner,
so explain each step in plain words, and run the commands yourself whenever you can.

WHAT IT IS
A Python tool (in my GitHub repo) that finds early Roblox game niches: ideas with proven demand
but only 1-5 games. It collects Roblox data every 3 hours in the background (macOS LaunchAgent),
shows a local dashboard at http://127.0.0.1:8765, sends Mac notifications, and uses the Claude
API for an "AI pick". Full docs are in README.md and PLAN.md in the project folder: read
README.md first.

WHERE THE CODE IS
- Repo: https://github.com/leoglockner1-dot/Claude
- Branch: claude/youthful-darwin-ga0uw1
- Project folder inside the repo: roblox-trend-scout/
- Put it at ~/claude-repo (my home folder). NOT in Desktop, Documents or Downloads: macOS blocks
  background jobs from reading those folders.

STEPS
1. Check the basics: macOS version, whether git works (if macOS offers to install the
   "command line developer tools", tell me to click Install and wait), and whether Homebrew
   is installed.
2. Clone: git clone -b claude/youthful-darwin-ga0uw1 https://github.com/leoglockner1-dot/Claude.git ~/claude-repo
   If it asks for a login (the repo may be private): if the `gh` command exists, run
   `gh auth login` and walk me through it; otherwise help me sign in with GitHub Desktop or
   download the branch as a ZIP from GitHub and unzip it to ~/claude-repo. If ~/claude-repo
   already exists, run `git pull` there instead.
3. Python 3.10 or newer is required (the python3 built into macOS is often 3.9, too old).
   Check for python3.10 to python3.13. If none is found: if Homebrew exists, run
   `brew install python@3.12`; otherwise tell me to install the latest Python 3 from
   https://www.python.org/downloads/macos/ and wait until I say it's done.
4. cd ~/claude-repo/roblox-trend-scout and run ./setup.sh
   (it creates .venv, installs the one dependency, creates .env, installs the 3-hour background
   job and sends a test notification. It won't stop to ask questions when you run it.)
5. Notifications: ask me whether a "Roblox Trend Scout" test notification appeared. If not,
   guide me to System Settings > Notifications > Script Editor > Allow Notifications, then
   re-test with: .venv/bin/python -m trendscout notify-test
6. API keys. IMPORTANT: I must never paste a key into this chat. Open the file for me with
   `open -e .env` so I can paste keys there and save. Walk me through getting them:
   a) ANTHROPIC_API_KEY (required for the AI pick): https://console.anthropic.com -> sign up /
      log in -> Billing: add a little credit (about $5 is plenty; one AI pick costs about
      $0.10-0.25) -> API Keys -> Create Key -> copy it into .env after ANTHROPIC_API_KEY=
   b) YOUTUBE_API_KEY (optional, free, recommended): https://console.cloud.google.com ->
      create a project -> APIs & Services -> Library -> enable "YouTube Data API v3" ->
      Credentials -> Create credentials -> API key -> paste after YOUTUBE_API_KEY=
   Afterwards check that the keys are filled in WITHOUT printing them, e.g.
   grep -c '^ANTHROPIC_API_KEY=..' .env   and   grep -c '^YOUTUBE_API_KEY=..' .env
7. Verify everything and show me the results:
   - .venv/bin/python -m unittest discover -s tests   (all tests should pass)
   - launchctl list | grep trendscout   (the background job is installed)
   - .venv/bin/python -m trendscout collect   (first real snapshot, takes about 5 minutes)
   - .venv/bin/python -m trendscout report    (shows the early niches; summarize the top 5 for me)
   - tail -20 logs/collect.log   (if the background job already ran)
8. Ask me before running the AI pick (it costs a few cents). If I say yes:
   .venv/bin/python -m trendscout recommend   and summarize the top pick in plain words.
   If it fails with an authentication or billing error, help me fix the key or credit.
9. Dashboard: tell me to double-click start.command in Finder (folder:
   ~/claude-repo/roblox-trend-scout). If macOS says it's from an unidentified developer:
   right-click > Open > Open. Don't start the dashboard server from this chat, because it
   keeps running and would block the chat.
10. Finish with a short summary: what's installed, where the files are, how to open the
    dashboard, what happens automatically, and when the results get good (growth tracking needs
    ~24 hours of data, picks are most trustworthy after ~7 days).

RULES
- Never print, log or commit the contents of .env.
- Don't change the tool's code unless something actually fails. If a fix is needed, explain what
  broke and what you changed, and check with me before committing or pushing anything to GitHub.
- If a step fails, read the error, look at README.md's Troubleshooting table, and try the fix
  before asking me.
````

## What will happen

1. Claude Code checks your Mac, downloads the code to `~/claude-repo`, and installs Python if needed.
2. It runs the setup, which turns on background collection every 3 hours and sends a test notification.
3. It opens `.env` in TextEdit and walks you through getting your keys. You paste them into
   that file yourself, never into the chat.
4. It runs the first collection (~5 minutes), shows you the top niches, and asks before
   spending a few cents on the first AI pick.
5. You open the dashboard by double-clicking `start.command`.
