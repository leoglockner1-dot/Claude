#!/usr/bin/env bash
# Downloads the reference images listed in asset_manifest.tsv into the academy's Assets/ folders.
# Usage: ./fetch_assets.sh "/path/to/vault/Roblox Design Academy"
# Existing files are skipped, never overwritten.
set -euo pipefail
ACADEMY="${1:?Pass the path to the 'Roblox Design Academy' folder}"
MANIFEST="$(dirname "$0")/asset_manifest.tsv"
grep -v '^#' "$MANIFEST" | while IFS=$'\t' read -r ref path url; do
  dest="$ACADEMY/$path"
  if [ -e "$dest" ]; then echo "skip (exists) $path"; continue; fi
  mkdir -p "$(dirname "$dest")"
  curl -fsSL -o "$dest" "$url" && echo "ok   $path" || echo "FAIL $path  <- $url"
done
