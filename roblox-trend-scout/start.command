#!/bin/bash
# Double-click this file in Finder to open the Roblox Trend Scout dashboard.
cd "$(dirname "$0")"
if [ ! -x .venv/bin/python ]; then
  echo "Please run ./setup.sh first."; read -r -p "Press Enter to close."; exit 1
fi
exec ./.venv/bin/python -m trendscout serve
