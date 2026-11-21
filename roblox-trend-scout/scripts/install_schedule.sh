#!/bin/bash
# Installs a macOS LaunchAgent that runs a collection every 3 hours while you're logged in.
# If the laptop is asleep at that time, it runs once when it wakes up.
set -e
cd "$(dirname "$0")/.."
ROOT="$(pwd)"
LABEL="com.trendscout.collect"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
INTERVAL="${1:-10800}"   # seconds (10800 = 3 hours)

case "$ROOT" in
  "$HOME/Desktop"*|"$HOME/Documents"*|"$HOME/Downloads"*)
    echo "WARNING: macOS blocks background jobs from reading Desktop/Documents/Downloads."
    echo "Move the folder to your home folder (e.g. ~/roblox-trend-scout) and run this again."
    exit 1;;
esac

mkdir -p "$HOME/Library/LaunchAgents" "$ROOT/logs"
cat > "$PLIST" <<PL
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>$LABEL</string>
  <key>ProgramArguments</key>
  <array>
    <string>$ROOT/.venv/bin/python</string><string>-m</string><string>trendscout</string><string>collect</string>
  </array>
  <key>WorkingDirectory</key><string>$ROOT</string>
  <key>StartInterval</key><integer>$INTERVAL</integer>
  <key>RunAtLoad</key><true/>
  <key>StandardOutPath</key><string>$ROOT/logs/collect.log</string>
  <key>StandardErrorPath</key><string>$ROOT/logs/collect.log</string>
</dict>
</plist>
PL
launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"
echo "Background collection installed (every $((INTERVAL / 3600))h). Log: $ROOT/logs/collect.log"
