"""One collection run: charts -> game stats -> supply search -> social buzz."""
from __future__ import annotations

import json
import time

from . import analyze, config, db, roblox, social
from .http import FetchError

SUPPLY_TOP_N = 15     # how many top themes get a Roblox search (competition check)
YOUTUBE_TOP_N = 10
REDDIT_TOP_N = 12


def run(log=print) -> dict:
    t0 = time.time()
    summary: dict = {"errors": []}
    with db.session() as conn:
        run_id = db.new_run(conn)
        now = time.time()

        log("Fetching Roblox charts...")
        charts = roblox.fetch_charts()
        chart_ids = {uid for ids in charts.values() for uid in ids}
        log(f"  {len(charts)} charts, {len(chart_ids)} unique games")

        # Keep tracking games we saw this week even if they fell off the charts.
        tracked = {r[0] for r in conn.execute(
            "SELECT universe_id FROM games WHERE last_seen >= ? ORDER BY last_seen DESC LIMIT 600",
            (now - 7 * 86400,))}
        ids = sorted(chart_ids | tracked)

        log(f"Fetching stats for {len(ids)} games...")
        details = roblox.fetch_game_details(ids)
        votes = roblox.fetch_votes(ids)
        for g in details:
            db.upsert_game(conn, g, now)
            up, down = votes.get(g["universe_id"], (None, None))
            conn.execute(
                "INSERT OR REPLACE INTO snapshots VALUES (?,?,?,?,?,?,?,?)",
                (run_id, g["universe_id"], now, g["playing"], g["visits"], g["favorites"], up, down))
        for sort_id, uids in charts.items():
            conn.executemany("INSERT OR IGNORE INTO chart_entries VALUES (?,?,?,?)",
                             [(run_id, uid, sort_id, rank) for rank, uid in enumerate(uids, 1)])
        conn.commit()
        summary.update(games=len(details), charts=len(charts))

        # First-pass ranking decides which themes deserve the (slower) extra lookups.
        ranked = analyze.analyze(conn, limit=SUPPLY_TOP_N)["trends"]
        terms = [t["search_term"] for t in ranked]

        log(f"Checking competition for {len(terms)} themes...")
        for term in terms:
            try:
                res = roblox.search_games(term)
            except FetchError as e:
                summary["errors"].append(f"search '{term}': {e}")
                continue
            playing = [r["playing"] for r in res]
            conn.execute("INSERT OR REPLACE INTO search_supply VALUES (?,?,?,?,?,?)",
                         (run_id, term, now, len(res), sum(playing), max(playing, default=0)))
        conn.commit()

        for source, fn, top_n, min_h, enabled in (
            ("youtube", social.youtube_buzz, YOUTUBE_TOP_N, config.YOUTUBE_MIN_HOURS, bool(config.YOUTUBE_API_KEY)),
            ("reddit", social.reddit_buzz, REDDIT_TOP_N, config.REDDIT_MIN_HOURS, True),
        ):
            if not enabled:
                log(f"Skipping {source} (no API key set)")
                continue
            if not social.due(db.last_social_ts(conn, source), min_h):
                log(f"Skipping {source} (checked less than {min_h:g}h ago)")
                continue
            log(f"Checking {source} buzz...")
            ok = 0
            for term in terms[:top_n]:
                try:
                    res = fn(term)
                except FetchError as e:
                    summary["errors"].append(f"{source} '{term}': {e}")
                    if "HTTP 403" in str(e) or "HTTP 400" in str(e):
                        break      # bad key / quota used up: don't hammer it
                    continue
                if res is None:
                    continue
                conn.execute("INSERT OR REPLACE INTO social VALUES (?,?,?,?,?,?)",
                             (now, source, term, res["items"], res["engagement"], json.dumps(res["sample"])))
                ok += 1
            conn.commit()
            summary[source] = ok

        conn.execute("UPDATE runs SET notes=? WHERE id=?", (json.dumps(summary), run_id))
    summary["seconds"] = round(time.time() - t0, 1)
    log(f"Done in {summary['seconds']}s" + (f" ({len(summary['errors'])} warnings)" if summary["errors"] else ""))
    return summary
