"""Early-niche finder: ideas players clearly want that almost nobody has built yet.

How it works:
1. Start from *new* games (< NICHE_MAX_AGE_DAYS old) that already have real demand
   (>= MIN_DEMAND players online right now).
2. Take the distinctive words/phrases in their names (skipping words that many tracked
   games already use, since those are crowded by definition).
3. Search Roblox for each phrase and count how many games with real players
   (>= REAL_PLAYERS online) come up. A phrase with at most MAX_COMPETITORS such games is a niche.
4. Merge phrases that point at the same group of games, then score each niche on demand,
   growth, freshness, low competition, approval, buzz and chart presence.

Search results are cached for SEARCH_CACHE_HOURS so each run only checks new phrases, and the
games found in niche searches are tracked from then on, so their growth can be measured too.
"""
from __future__ import annotations

import json
import math
import re
import time
from collections import Counter, defaultdict

from . import analyze, roblox
from .http import FetchError

NICHE_MAX_AGE_DAYS = 120   # the niche's leading game must be this new
MIN_DEMAND = 500           # leading game needs at least this many players online
REAL_PLAYERS = 100         # a competitor "counts" with at least this many players online
MAX_COMPETITORS = 5        # at most this many games with real players = still a niche
CROWDED_DF = 6             # a word in this many tracked game names is not niche
SEARCH_CACHE_HOURS = 24
SEARCH_BUDGET = 150        # max Roblox searches per collection run

WEIGHTS = {
    "momentum": 0.22, "demand": 0.18, "freshness": 0.13, "low_competition": 0.13,
    "concept_room": 0.12, "quality": 0.08, "buzz": 0.09, "charts": 0.05,
}
LABELS = {
    "momentum": "Growth momentum", "demand": "Proven demand", "freshness": "How new it is",
    "low_competition": "Few competitors", "concept_room": "Broader idea uncrowded", "quality": "Player approval", "buzz": "Social buzz",
    "charts": "Chart presence",
}

SCHEMA = """
CREATE TABLE IF NOT EXISTS niche_search (
    keyword TEXT PRIMARY KEY,
    ts REAL NOT NULL,
    n_real INTEGER,
    results TEXT
);
"""


def _ensure(conn) -> None:
    conn.executescript(SCHEMA)


def _candidates(games: list[dict]) -> list[dict]:
    return [g for g in games if g["age_days"] <= NICHE_MAX_AGE_DAYS and g["playing"] >= MIN_DEMAND]


def candidate_keywords(games: list[dict]) -> list[tuple[str, dict]]:
    """(keyword, leading game) pairs worth a search, best-demand first."""
    df = Counter(kw for g in games for kw in analyze.keywords_for(g["name"]))
    best: dict[str, dict] = {}
    for g in _candidates(games):
        for kw in analyze.keywords_for(g["name"]):
            if df[kw] >= CROWDED_DF or len(kw) < 4:
                continue
            if kw not in best or g["playing"] > best[kw]["playing"]:
                best[kw] = g
    return sorted(best.items(), key=lambda kv: -kv[1]["playing"])


def _words(name: str) -> list[str]:
    text = re.sub(r"[\[\(\{【].*?[\]\)\}】]", " ", name)
    text = re.sub(r"\+\s?1\b", " plus1 ", text)
    words = re.sub(r"[^a-zA-Z0-9 ]+", " ", text).lower().split()
    return [w for w in (analyze._singular(w) for w in words) if w not in analyze.STOPWORDS]


def name_matches(name: str, kw: str) -> bool:
    """True if the game's name really contains the phrase.

    Roblox search pads results with loosely related popular games, so only games whose *name*
    contains the phrase count as competitors. Spaces, plurals and small words are ignored
    ("ballpit" matches "Clean the Ball Pits!"); a match must start at a word boundary, so
    "rage" does not match "Garage".
    """
    joined, starts, pos = "", set(), 0
    for w in _words(name):
        starts.add(pos)
        joined += w
        pos += len(w)
    target = kw.replace(" ", "")
    i = joined.find(target)
    while i != -1:
        if i in starts:
            return True
        i = joined.find(target, i + 1)
    return False


def search_term(kw: str) -> str:
    return analyze.display_keyword(kw)


# ------------------------------------------------------------------ collection step
def collect(conn, log=print) -> dict:
    _ensure(conn)
    games, _ = analyze.load_games(conn)
    cached = {r["keyword"]: r["ts"] for r in conn.execute("SELECT keyword, ts FROM niche_search")}
    fresh_after = time.time() - SEARCH_CACHE_HOURS * 3600
    todo = [kw for kw, _ in candidate_keywords(games) if cached.get(kw, 0) < fresh_after][:SEARCH_BUDGET]
    log(f"Scanning {len(todo)} possible niches (searching Roblox for each)...")
    done, errors = 0, []
    for kw in todo:
        try:
            res = roblox.search_games(search_term(kw))
        except FetchError as e:
            errors.append(f"niche search '{kw}': {e}")
            if len(errors) >= 5:
                break
            continue
        real = [r for r in res if r["playing"] >= REAL_PLAYERS and r.get("universe_id")]
        n_match = sum(1 for r in real if name_matches(r["name"] or "", kw))
        conn.execute("INSERT OR REPLACE INTO niche_search VALUES (?,?,?,?)",
                     (kw, time.time(), n_match, json.dumps(real)))
        done += 1
    conn.commit()
    return {"niche_searches": done, "errors": errors}


def _searches(conn, since: float = 0) -> dict[str, list[dict]]:
    return {r["keyword"]: json.loads(r["results"])
            for r in conn.execute("SELECT keyword, results FROM niche_search WHERE ts >= ?", (since,))}


def _matched(results: list[dict], kw: str) -> list[dict]:
    return [x for x in results if name_matches(x["name"] or "", kw)]


def tracked_ids(conn, days: float = 7) -> set[int]:
    """Games found in niche searches; collect.py keeps snapshotting them for growth history."""
    _ensure(conn)
    ids: set[int] = set()
    for kw, results in _searches(conn, time.time() - days * 86400).items():
        m = _matched(results, kw)
        if len(m) <= MAX_COMPETITORS:
            ids.update(x["universe_id"] for x in m)
    return ids


# ------------------------------------------------------------------ analysis
def find_niches(conn, games: list[dict] | None = None, social: dict | None = None, limit: int = 40) -> list[dict]:
    _ensure(conn)
    if games is None:
        games = analyze.load_games(conn)[0]
    if social is None:
        social = analyze._latest_social(conn)
    by_id = {g["universe_id"]: g for g in games}
    searches = _searches(conn)
    df = Counter(kw for g in games for kw in analyze.keywords_for(g["name"]))

    def competitors(kw: str, lead: dict) -> list[dict] | None:
        """Games with real players whose name contains kw, or None if unknown."""
        if kw in searches:
            m = {x["universe_id"]: x for x in _matched(searches[kw], kw)}
            m.setdefault(lead["universe_id"], {"universe_id": lead["universe_id"], "name": lead["name"],
                                                "playing": lead["playing"]})
            return list(m.values())
        if df[kw] >= CROWDED_DF:   # many tracked games already use it: crowded, no search needed
            return [{"universe_id": None}] * df[kw]
        return None

    by_label: dict[str, dict] = {}
    for lead in _candidates(games):
        known = {}
        for kw in analyze.keywords_for(lead["name"]):
            c = competitors(kw, lead)
            if c is not None and len(kw) >= 3:
                known[kw] = c
        ok = {kw: c for kw, c in known.items() if len(c) <= MAX_COMPETITORS}
        if not ok:
            continue
        # Broadest phrase that still qualifies: single words over phrases, then most competitors.
        label = min(ok, key=lambda k: (len(k.split()), -len(ok[k]), -len(k)))
        crowded = [(kw, len(c)) for kw, c in known.items() if kw not in ok and " " not in kw]
        closest = max(crowded, key=lambda kc: kc[1]) if crowded else None
        entry = by_label.get(label)
        if entry is None or lead["playing"] > entry["lead"]["playing"]:
            by_label[label] = {"lead": lead, "found": ok[label], "aliases": sorted(set(ok) - {label}),
                               "crowded_concept": closest}

    niches = []
    for label, e in by_label.items():
        members = []
        for x in e["found"]:
            uid = x["universe_id"]
            if uid in by_id:
                members.append(by_id[uid])
            else:   # seen only in search so far: minimal record until it's tracked next run
                members.append({"universe_id": uid, "name": x["name"], "playing": x["playing"], "age_days": None,
                                "like_ratio": None, "ccu_dod": None, "ccu_wow": None, "momentum": None,
                                "charts": [], "url": None, "creator_id": None, "description": "",
                                "visits": None, "subgenre": "", "created": None})
        members = [m for m in members if (m["playing"] or 0) >= REAL_PLAYERS]
        members.sort(key=lambda m: -(m["playing"] or 0))
        niches.append(_niche_metrics(label, e, members, social))
    return _score(niches)[:limit]


def _niche_metrics(kw: str, e: dict, members: list[dict], social: dict) -> dict:
    lead = e["lead"]
    total = sum(m["playing"] or 0 for m in members)
    mom = analyze._weighted([(m["momentum"], math.sqrt((m["playing"] or 0) + 1))
                             for m in members if m.get("momentum") is not None])
    quality = analyze._weighted([(m["like_ratio"], math.sqrt((m["playing"] or 0) + 1))
                                 for m in members if m.get("like_ratio") is not None])
    charts = sum(max((analyze.CHART_WEIGHTS.get(c, 0) for c in m["charts"]), default=0) for m in members)
    term = search_term(kw)
    soc = social.get(term, {})
    yt, rd = soc.get("youtube"), soc.get("reddit")
    buzz = None
    if yt or rd:
        buzz = math.log10((yt["engagement"] if yt else 0) + 1) + 1.5 * math.log10((rd["engagement"] if rd else 0) + 1)

    n = len(members)
    signals = [f"Only {n} game{'s' if n != 1 else ''} with {REAL_PLAYERS}+ players when you search “{term}”",
               f"Leading game is {round(lead['age_days'])} days old with {lead['playing']:,} players online"]
    top = members[0]
    if top["universe_id"] != lead["universe_id"] and (top["playing"] or 0) > lead["playing"]:
        signals.append(f"Warning: \u201c{top['name'][:40]}\u201d already has {top['playing']:,} players here")
    if n == 1:
        signals.append("No copycats yet: earliest possible timing, but could be a one-game fluke")
    if lead.get("ccu_dod") is not None:
        signals.append(f"Leading game players vs yesterday: {lead['ccu_dod']:+.0%}")
    if lead.get("ccu_wow") is not None:
        signals.append(f"Leading game players vs last week: {lead['ccu_wow']:+.0%}")
    if "up-and-coming" in lead["charts"]:
        signals.append("Leading game is on Up-and-Coming")
    if yt:
        signals.append(f"YouTube: {yt['items']} videos this week, {yt['engagement']:,} views")
    if rd:
        signals.append(f"Reddit: {rd['items']} posts this week")
    if e["crowded_concept"]:
        ckw, cn = e["crowded_concept"]
        signals.append(f"Broader idea \u201c{analyze.display_keyword(ckw)}\u201d already has "
                       f"{cn if cn < 20 else '20+'} games: make sure your twist stands apart")
    if e["aliases"]:
        signals.append("Related phrases: " + ", ".join(analyze.display_keyword(k) for k in e["aliases"][:5]))

    return {
        "id": f"niche:{kw}", "kind": "niche", "keyword": kw, "search_term": term,
        "label": f"“{term}”", "lead_name": lead["name"], "n_games": n,
        "n_creators": len({m["creator_id"] for m in members if m["creator_id"]}) or n,
        "n_young": sum(1 for m in members if m.get("age_days") is not None and m["age_days"] <= NICHE_MAX_AGE_DAYS),
        "total_ccu": total, "lead_playing": lead["playing"], "lead_age_days": lead["age_days"],
        "lead_ccu_dod": lead.get("ccu_dod"), "median_age_days": lead["age_days"],
        "leader_share": (lead["playing"] or 0) / max(total, 1), "momentum": mom, "quality": quality,
        "chart_score": charts, "buzz": buzz, "youtube": yt, "reddit": rd, "signals": signals,
        "games": members, "aliases": e["aliases"], "lead_id": lead["universe_id"],
        "crowded_concept": e["crowded_concept"],
    }


def _score(niches: list[dict]) -> list[dict]:
    if not niches:
        return []
    raw = {
        "momentum": [x["momentum"] for x in niches],
        "demand": [math.log10(x["lead_playing"] + 1) for x in niches],
        "freshness": [-x["lead_age_days"] for x in niches],
        "low_competition": [-x["n_games"] for x in niches],
        # Penalise niches that are a renamed version of a crowded idea (e.g. yet another ragdoll game).
        "concept_room": [-min(x["crowded_concept"][1], 20) if x["crowded_concept"] else 0 for x in niches],
        "quality": [x["quality"] for x in niches],
        "buzz": [x["buzz"] for x in niches],
        "charts": [x["chart_score"] for x in niches],
    }
    pct = {k: analyze._percentiles(v) for k, v in raw.items()}
    for i, x in enumerate(niches):
        x["breakdown"] = {k: round(pct[k][i] * 100) for k in WEIGHTS}
        x["score"] = round(sum(WEIGHTS[k] * pct[k][i] for k in WEIGHTS) * 100, 1)
    return sorted(niches, key=lambda x: -x["score"])
