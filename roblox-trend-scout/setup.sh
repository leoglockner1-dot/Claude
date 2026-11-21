#!/bin/bash
# One-time setup for Roblox Trend Scout on macOS.
# Run it from Terminal:   cd ~/roblox-trend-scout && ./setup.sh
set -e
cd "$(dirname "$0")"

echo "== Roblox Trend Scout setup =="

# 1) Find a Python 3.10+ (macOS's built-in python3 is often 3.9, which is too old).
PY=""
for c in python3.13 python3.12 python3.11 python3.10 /usr/local/bin/python3 /opt/homebrew/bin/python3 python3; do
  if command -v "$c" >/dev/null 2>&1 && "$c" -c 'import sys; sys.exit(0 if sys.version_info >= (3,10) else 1)' 2>/dev/null; then
    PY="$(command -v "$c")"; break
  fi
done
if [ -z "$PY" ]; then
  echo
  echo "You need Python 3.10 or newer."
  echo "  1. Open https://www.python.org/downloads/macos/ and install the latest Python 3 (the macOS installer)."
  echo "  2. Close and reopen Terminal, then run ./setup.sh again."
  exit 1
fi
echo "Using $PY ($("$PY" --version))"

# 2) Private environment with the one dependency (the Claude SDK).
if [ ! -d .venv ]; then "$PY" -m venv .venv; fi
./.venv/bin/python -m pip install --quiet --upgrade pip
./.venv/bin/python -m pip install --quiet -r requirements.txt
echo "Installed dependencies."

# 3) Settings file for your API keys.
if [ ! -f .env ]; then
  cp .env.example .env
  echo "Created .env - open it and paste your ANTHROPIC_API_KEY (and optional YOUTUBE_API_KEY)."
fi
chmod +x start.command scripts/*.sh 2>/dev/null || true

# 4) Background collection every 3 hours.
read -r -p "Collect data automatically every 3 hours in the background? [Y/n] " ans
if [[ ! "$ans" =~ ^[Nn] ]]; then ./scripts/install_schedule.sh; fi

echo
echo "Setup done! Next steps:"
echo "  1. open -e .env          (paste your API keys, save)"
echo "  2. Double-click start.command (or run ./start.command) to open the dashboard"
