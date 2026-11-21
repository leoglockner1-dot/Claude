"""Turn raw snapshots into scored *trends*.

A trend is a group of games that share a theme: a keyword in their names ("steal", "+1",
"ragdoll", "100 miles") or a Roblox subgenre ("Tycoon", "Escape"). A theme looks *upcoming*
when several young games from different creators are growing fast and climbing charts,
people talk about it on YouTube/Reddit, and no single giant owns all of the players.
"""
from __future__ import annotations

import datetime as dt
import math
import re
import time
from collections import defaultdict
from statistics import median

from . import db

DAY = 86400.0

STOPWORDS = set("""
a an the of in on to and or for with my your our you me we is are be it its at by from vs x
new update upd updated event events official alpha beta beta! release released free hot sale
roblox game games obby2 part season seasons now hrs hours hour mins minutes day days week
world worlds v2 v3 v4 2x x2 x3 3x 1x 5x 10x lvl level levels mode modes edition remake
classic original simulator sim
""".split())

CHART_WEIGHTS = {"up-and-coming": 2.0, "top-trending": 1.5, "fun-with-friends": 0.6,
                 "top-revisited": 0.4, "top-playing-now": 0.5, "top-earning": 0.3}

YOUNG_DAYS = 90       # games younger than this count as "new wave"
WEIGHTS = {           # how much each signal matters in the final 0-100 score
    "momentum": 0.22, "youth": 0.18, "velocity": 0.15, "buzz": 0.13,
    "charts": 0.12, "opportunity": 0.12, "quality": 0.08,
}
SIGNAL_LABELS = {
    "momentum": "Growth momentum", "youth": "New-game wave", "velocity": "Visit velocity",
    "buzz": "Social buzz", "charts": "Chart presence", "opportunity": "Room to compete",
    "quality": "Player approval",
}


# ---------------------------------------------------------------- name -> keywords
def _singular(w: str) -> str:
    """Crude plural folding so "animals"/"animal" and "eggs"/"egg" become one theme."""
    if len(w) > 4 and w.endswith("ies"):
        return w[:-3] + "y"
    if len(w) > 3 and w.endswith("s") and not w.endswith(("ss", "us", "is")):
        return w[:-1]
    return w


def keywords_for(name: str) -> set[str]:
    text = re.sub(r"[\[\(\{【].*?[\]\)\}】]", " ", name)        # drop [UPDATE] / (Anomaly) tags
    text = re.sub(r"\+\s?1\b", " plus1 ", text)                  # "+1 Speed" style games
    text = re.sub(r"[^a-zA-Z0-9 ]+", " ", text).lower()
    words = [w for w in text.split() if not w.isdigit() or w in ("99", "100")]
    words = [_singular(w) for w in words]
    words = [w for w in words if w not in STOPWORDS and (len(w) >= 3 or w in ("99",))]
    kws = set(words)
    kws.update(f"{a} {b}" for a, b in zip(words, words[1:]))
    return kws


def display_keyword(kw: str) -> str:
    return kw.replace("plus1", "+1")


# ---------------------------------------------------------------- per-game metrics
def _parse_time(s: str | None) -> float | None:
    if not s:
        return None
    try:
        return dt.datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()
    except ValueError:
        return None


def _closest(snaps: list[dict], target_ts: float, tolerance: float) -> dict | None:
    best = min(snaps, key=lambda s: abs(s["ts"] - target_ts), default=None)
    if best and abs(best["ts"] - target_ts) <= tolerance:
        return best
    return None


def game_metrics(game: dict, snaps: list[dict], charts: set[str], now: float) -> dict:
    snaps = sorted(snaps, key=lambda s: s["ts"])
    cur = snaps[-1]
    created = _parse_time(game["created"]) or (now - 365 * DAY)
    age_days = max((now - created) / DAY, 0.5)
    lifetime_vpd = (cur["visits"] or 0) / age_days

    # Visit velocity over the most recent ~day (falls back to whatever history exists, >= 3h).
    older = [s for s in snaps if cur["ts"] - s["ts"] >= 3 * 3600]
    base = _closest(older, cur["ts"] - DAY, 10 * 3600) or (older[0] if older else None)
    recent_vpd = None
    if base:
        span = (cur["ts"] - base["ts"]) / DAY
        recent_vpd = max((cur["visits"] or 0) - (base["visits"] or 0), 0) / span

    # Acceleration: this day's visit rate vs the day before.
    accel = None
    if base and recent_vpd is not None:
        prev = _closest([s for s in snaps if s["ts"] < base["ts"]], base["ts"] - DAY, 10 * 3600)
        if prev:
            prev_vpd = max((base["visits"] or 0) - (prev["visits"] or 0), 0) / ((base["ts"] - prev["ts"]) / DAY)
            if prev_vpd > 0:
                accel = recent_vpd / prev_vpd - 1

    # Player counts swing with time of day, so only compare to the same time yesterday / last week.
    def ccu_change(days_back: float, tol_h: float) -> float | None:
        then = _closest(snaps[:-1], cur["ts"] - days_back * DAY, tol_h * 3600)
        if not then:
            return None
        return (cur["playing"] or 0) / max(then["playing"] or 0, 100) - 1

    ccu_dod = ccu_change(1, 4)
    ccu_wow = ccu_change(7, 12)

    parts = [x for x in (accel, ccu_dod, ccu_wow) if x is not None]
    momentum = sum(max(min(p, 3.0), -1.0) for p in parts) / len(parts) if parts else None

    up, down = cur["up_votes"] or 0, cur["down_votes"] or 0
    return {
        "universe_id": game["universe_id"], "name": game["name"], "creator": game["creator_name"],
        "creator_id": game["creator_id"], "genre": game["genre_l1"], "subgenre": game["genre_l2"],
        "url": f"https://www.roblox.com/games/{game['root_place_id']}" if game["root_place_id"] else None,
        "description": game["description"] or "",
        "playing": cur["playing"] or 0, "visits": cur["visits"] or 0, "favorites": cur["favorites"] or 0,
        "age_days": round(age_days, 1), "created": game["created"], "updated": game["updated"],
        "like_ratio": up / (up + down) if up + down >= 20 else None,
        "lifetime_vpd": lifetime_vpd, "recent_vpd": recent_vpd, "accel": accel,
        "ccu_dod": ccu_dod, "ccu_wow": ccu_wow, "momentum": momentum, "charts": sorted(charts),
    }


# ---------------------------------------------------------------- loading
def load_games(conn, lookback_days: float = 14) -> tuple[list[dict], dict]:
    now = time.time()
    last_run = conn.execute("SELECT id, ts FROM runs ORDER BY id DESC LIMIT 1").fetchone()
    first_run = conn.execute("SELECT MIN(ts) FROM runs").fetchone()[0]
    n_runs = conn.execute("SELECT COUNT(*) FROM runs").fetchone()[0]
    meta = {"runs": n_runs, "history_hours": round((now - first_run) / 3600, 1) if first_run else 0,
            "last_run_ts": last_run["ts"] if last_run else None}
    if not last_run:
        return [], meta

    since = now - lookback_days * DAY
    games = {r["universe_id"]: dict(r) for r in conn.execute(
        "SELECT * FROM games WHERE last_seen >= ?", (since,))}
    snaps: dict[int, list[dict]] = defaultdict(list)
    for r in conn.execute("SELECT * FROM snapshots WHERE ts >= ? ORDER BY ts", (since - 8 * DAY,)):
        if r["universe_id"] in games:
            snaps[r["universe_id"]].append(dict(r))
    charts: dict[int, set[str]] = defaultdict(set)
    for r in conn.execute("SELECT universe_id, sort_id FROM chart_entries WHERE run_id=?", (last_run["id"],)):
        charts[r["universe_id"]].add(r["sort_id"])

    out = [game_metrics(g, snaps[uid], charts[uid], now) for uid, g in games.items() if snaps.get(uid)]
    return out, meta


def _latest_supply(conn) -> dict[str, dict]:
    rows = conn.execute("""
        SELECT s.* FROM search_supply s
        JOIN (SELECT keyword, MAX(ts) AS ts FROM search_supply GROUP BY keyword) m
          ON s.keyword = m.keyword AND s.ts = m.ts""").fetchall()
    return {r["keyword"]: dict(r) for r in rows}


def _latest_social(conn) -> dict[str, dict[str, dict]]:
    rows = conn.execute("""
        SELECT s.* FROM social s
        JOIN (SELECT source, keyword, MAX(ts) AS ts FROM social GROUP BY source, keyword) m
          ON s.source = m.source AND s.keyword = m.keyword AND s.ts = m.ts""").fetchall()
    out: dict[str, dict[str, dict]] = defaultdict(dict)
    for r in rows:
        out[r["keyword"]][r["source"]] = dict(r)
    return out


# ---------------------------------------------------------------- themes
def build_themes(games: list[dict]) -> list[dict]:
    by_kw: dict[str, list[dict]] = defaultdict(list)
    for g in games:
        for kw in keywords_for(g["name"]):
            by_kw[("kw", kw)].append(g)
        if g["subgenre"]:
            by_kw[("genre", g["subgenre"])].append(g)

    themes, seen_sets = [], {}
    # Bigrams first so that "steal brainrot" wins over "brainrot" when they cover the same games.
    for (kind, key), members in sorted(by_kw.items(), key=lambda kv: (-len(kv[1]), -len(kv[0][1].split()))):
        creators = {m["creator_id"] for m in members}
        min_games = 3 if kind == "genre" else 2
        if len(members) < min_games or len(creators) < 2:
            continue
        if sum(m["playing"] for m in members) < 1000:
            continue
        sig = frozenset(m["universe_id"] for m in members)
        if sig in seen_sets:
            continue
        seen_sets[sig] = key
        label = f"{key} (subgenre)" if kind == "genre" else f"“{display_keyword(key)}” games"
        themes.append({"id": f"{kind}:{key}", "kind": kind, "keyword": key,
                       "search_term": key.replace("plus1", "+1").lower(), "label": label,
                       "members": members})
    return themes


def _weighted(values: list[tuple[float, float]]) -> float | None:
    tot = sum(w for _, w in values)
    return sum(v * w for v, w in values) / tot if tot > 0 else None


def theme_metrics(t: dict, supply: dict, social: dict) -> dict:
    ms = t["members"]
    total_ccu = sum(m["playing"] for m in ms)
    young = [m for m in ms if m["age_days"] <= YOUNG_DAYS]
    young_ccu = sum(m["playing"] for m in young)
    top = max(ms, key=lambda m: m["playing"])

    mom = _weighted([(m["momentum"], math.sqrt(m["playing"] + 1)) for m in ms if m["momentum"] is not None])
    chart_score = sum(max((CHART_WEIGHTS.get(c, 0) for c in m["charts"]), default=0) for m in ms)
    velocity = sum((m["recent_vpd"] if m["recent_vpd"] is not None else m["lifetime_vpd"]) for m in young)
    quality = _weighted([(m["like_ratio"], math.sqrt(m["playing"] + 1)) for m in ms if m["like_ratio"] is not None])

    sup = supply.get(t["search_term"])
    if sup and sup["n_results"]:
        leader_share = (sup["top_playing"] or 0) / max(sup["total_playing"] or 1, 1)
        per_game = (sup["total_playing"] or 0) / sup["n_results"]
    else:
        leader_share = top["playing"] / max(total_ccu, 1)
        per_game = total_ccu / len(ms)
    opportunity = math.log10(per_game + 10) * (1 - 0.6 * leader_share)

    soc = social.get(t["search_term"], {})
    yt, rd = soc.get("youtube"), soc.get("reddit")
    buzz = None
    if yt or rd:
        buzz = math.log10((yt["engagement"] if yt else 0) + 1) + 1.5 * math.log10((rd["engagement"] if rd else 0) + 1)

    signals = []
    if young:
        signals.append(f"{len(young)} of {len(ms)} games are under {YOUNG_DAYS} days old "
                       f"({young_ccu / max(total_ccu, 1):.0%} of players)")
    uac = [m for m in ms if "up-and-coming" in m["charts"]]
    if uac:
        signals.append(f"{len(uac)} on Up-and-Coming: " + ", ".join(m["name"][:30] for m in uac[:3]))
    if mom is not None:
        signals.append(f"Avg growth signal {mom:+.0%} (day-over-day / week-over-week)")
    if yt:
        signals.append(f"YouTube: {yt['items']} videos this week, {yt['engagement']:,} views")
    if rd:
        signals.append(f"Reddit: {rd['items']} posts this week")
    if leader_share > 0.7:
        signals.append(f"Warning: {top['name'][:30]} holds {leader_share:.0%} of players")

    return {
        "id": t["id"], "kind": t["kind"], "keyword": t["keyword"], "label": t["label"],
        "search_term": t["search_term"], "n_games": len(ms),
        "n_creators": len({m["creator_id"] for m in ms}), "n_young": len(young),
        "total_ccu": total_ccu, "young_ccu_share": young_ccu / max(total_ccu, 1),
        "median_age_days": round(median(m["age_days"] for m in ms), 1),
        "momentum": mom, "momentum_coverage": sum(m["momentum"] is not None for m in ms) / len(ms),
        "chart_score": chart_score, "velocity": velocity, "quality": quality,
        "leader_share": leader_share, "opportunity": opportunity, "buzz": buzz,
        "supply": sup, "youtube": yt, "reddit": rd, "signals": signals,
        "games": sorted(ms, key=lambda m: -m["playing"]),
    }


def _percentiles(values: list[float | None]) -> list[float]:
    known = sorted(v for v in values if v is not None)
    if len(known) < 2:
        return [0.5] * len(values)
    out = []
    for v in values:
        if v is None:
            out.append(0.5)       # unknown -> neutral, neither rewarded nor punished
            continue
        lo = sum(1 for k in known if k < v)
        eq = sum(1 for k in known if k == v)
        out.append((lo + (eq - 1) / 2) / (len(known) - 1))
    return out


def score_themes(themes: list[dict]) -> list[dict]:
    if not themes:
        return []
    raw = {
        "momentum": [t["momentum"] for t in themes],
        "youth": [t["young_ccu_share"] * math.log2(t["n_young"] + 1) for t in themes],
        "velocity": [math.log10(t["velocity"] + 1) for t in themes],
        "buzz": [t["buzz"] for t in themes],
        "charts": [t["chart_score"] for t in themes],
        "opportunity": [t["opportunity"] for t in themes],
        "quality": [t["quality"] for t in themes],
    }
    pct = {k: _percentiles(v) for k, v in raw.items()}
    for i, t in enumerate(themes):
        t["breakdown"] = {k: round(pct[k][i] * 100) for k in WEIGHTS}
        t["score"] = round(sum(WEIGHTS[k] * pct[k][i] for k in WEIGHTS) * 100, 1)
    return sorted(themes, key=lambda t: -t["score"])


def analyze(conn=None, limit: int = 40) -> dict:
    own = conn is None
    conn = conn or db.connect()
    try:
        games, meta = load_games(conn)
        themes = [theme_metrics(t, _latest_supply(conn), _latest_social(conn)) for t in build_themes(games)]
        ranked = score_themes(themes)[:limit]
    finally:
        if own:
            conn.close()

    notes = []
    if meta["history_hours"] < 24:
        notes.append(f"Only {meta['history_hours']}h of history so far. Growth momentum needs ~24h "
                     "(and gets much better after 7 days); until then scores lean on game age, "
                     "charts and visit velocity.")
    return {"generated_ts": time.time(), "meta": meta, "notes": notes,
            "weights": WEIGHTS, "labels": SIGNAL_LABELS, "games_tracked": len(games), "trends": ranked}
