"""Command line: python -m trendscout <collect|report|recommend|serve>"""
from __future__ import annotations

import argparse
import json
import sys


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(prog="trendscout", description="Spot upcoming Roblox game trends.")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("collect", help="take a snapshot of Roblox charts, stats and buzz")
    r = sub.add_parser("report", help="print the current trend ranking")
    r.add_argument("-n", type=int, default=15)
    r.add_argument("--json", action="store_true")
    sub.add_parser("recommend", help="ask Claude for the top pick and a game plan")
    s = sub.add_parser("serve", help="start the local dashboard")
    s.add_argument("--no-browser", action="store_true")
    args = p.parse_args(argv)

    if args.cmd == "collect":
        from . import collect
        collect.run()
    elif args.cmd == "report":
        from . import analyze
        rep = analyze.analyze(limit=args.n)
        if args.json:
            print(json.dumps(rep, default=str, indent=1))
            return
        for note in rep["notes"]:
            print(f"Note: {note}\n")
        print(f"{'#':>2}  {'score':>5}  {'games':>5}  {'new':>3}  {'players':>9}  trend")
        for i, t in enumerate(rep["trends"], 1):
            print(f"{i:>2}  {t['score']:>5}  {t['n_games']:>5}  {t['n_young']:>3}  {t['total_ccu']:>9,}  {t['label']}")
    elif args.cmd == "recommend":
        from . import recommend
        try:
            res = recommend.recommend()
        except RuntimeError as e:
            sys.exit(f"Error: {e}")
        print(json.dumps(res, indent=2, ensure_ascii=False))
    elif args.cmd == "serve":
        from . import server
        server.serve(open_browser=not args.no_browser)
