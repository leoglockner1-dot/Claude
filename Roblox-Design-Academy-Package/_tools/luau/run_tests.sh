#!/usr/bin/env bash
# Type-check (strict) every module, then run the test suite. Usage: bash run_tests.sh [path/to/luau/bin]
# Needs the Luau CLI (luau + luau-analyze) from https://github.com/luau-lang/luau (releases or build from source).
set -u
BIN="${1:-}"; LUAU="${BIN:+$BIN/}luau"; ANALYZE="${BIN:+$BIN/}luau-analyze"
cd "$(dirname "$0")"
status=0
for f in src/*.luau mocks/*.luau tests/*.luau benchmarks/*.luau; do
  out=$("$ANALYZE" "$f" 2>&1)
  if echo "$out" | grep -q "Error"; then echo "TYPE ERRORS in $f"; echo "$out" | grep -A2 "Error"; status=1; fi
done
[ $status -eq 0 ] && echo "luau-analyze: 0 type errors"
"$LUAU" tests/run_all.luau || status=1
"$LUAU" tests/tutorial_repros.luau || status=1
exit $status
