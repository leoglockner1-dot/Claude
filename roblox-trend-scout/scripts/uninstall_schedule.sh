#!/bin/bash
# Stops and removes the background collection job.
LABEL="com.trendscout.collect"
launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
rm -f "$HOME/Library/LaunchAgents/$LABEL.plist"
echo "Background collection removed."
