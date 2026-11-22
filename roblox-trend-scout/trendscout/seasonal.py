"""Detect seasonal niches (Christmas, Halloween, ...) and how long their season has left.

A seasonal niche can die the day the season ends, so if there isn't enough time left to
build and ship a game (~3-6 weeks), its score is reduced.
"""
from __future__ import annotations

import datetime as dt
import re

SHIP_DAYS = 60          # with fewer days left than this, the score is reduced
MAX_PENALTY = 0.45      # at 0 days left the score is cut by this share
RECENTLY_ENDED_DAYS = 60


def _easter(year: int) -> dt.date:
    """Gregorian Easter Sunday (anonymous algorithm)."""
    a, b, c = year % 19, year // 100, year % 100
    d, e = b // 4, b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = c // 4, c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = (h + l - 7 * m + 114) % 31 + 1
    return dt.date(year, month, day)


# (name, words that mark it, window(year) -> (start, end))
SEASONS = [
    ("Halloween", {"halloween", "hlwn", "spooky", "pumpkin", "trick or treat", "jack o lantern"},
     lambda y: (dt.date(y, 9, 20), dt.date(y, 11, 2))),
    ("Thanksgiving", {"thanksgiving", "turkey"},
     lambda y: (dt.date(y, 11, 1), dt.date(y, 11, 30))),
    ("Christmas", {"christmas", "xmas", "santa", "elf", "elves", "reindeer", "gingerbread", "snowman",
                   "grinch", "mistletoe", "north pole", "advent", "nutcracker"},
     lambda y: (dt.date(y, 11, 15), dt.date(y, 12, 27))),
    ("New Year", {"new year", "new years", "nye"},
     lambda y: (dt.date(y, 12, 20), dt.date(y + 1, 1, 3))),
    ("Winter", {"winter", "snowball", "snowflake", "blizzard"},
     lambda y: (dt.date(y, 12, 1), dt.date(y + 1, 2, 28))),
    ("Valentine's Day", {"valentine", "valentines", "cupid"},
     lambda y: (dt.date(y, 1, 25), dt.date(y, 2, 15))),
    ("St. Patrick's Day", {"patrick", "patricks", "leprechaun", "shamrock"},
     lambda y: (dt.date(y, 3, 1), dt.date(y, 3, 18))),
    ("Easter", {"easter", "egg hunt"},
     lambda y: (_easter(y) - dt.timedelta(days=28), _easter(y) + dt.timedelta(days=2))),
    ("April Fools", {"april fool", "april fools"},
     lambda y: (dt.date(y, 3, 25), dt.date(y, 4, 2))),
    ("Summer", {"summer", "summertime"},
     lambda y: (dt.date(y, 6, 1), dt.date(y, 8, 31))),
]


def _text(name: str) -> str:
    # Bracket tags like "[🎃 EVENT]" are temporary event updates on non-seasonal games: ignore them.
    text = re.sub(r"[\[\(\{【].*?[\]\)\}】]", " ", name or "")
    return " " + " ".join(re.sub(r"[^a-zA-Z0-9 ]+", " ", text).lower().split()) + " "


def detect(*names: str, today: dt.date | None = None) -> dict | None:
    """Return {"season", "start", "end", "days_left", "status", "factor"} or None if not seasonal."""
    today = today or dt.date.today()
    text = " ".join(_text(n) for n in names)
    for season, words, window in SEASONS:
        if not any(f" {w} " in text for w in words):
            continue
        # The relevant occurrence: the one running now, just ended, or coming up next.
        best = None
        for y in (today.year - 1, today.year, today.year + 1):
            start, end = window(y)
            if start <= today <= end:
                best = (start, end, "in season")
                break
            if end < today and (today - end).days <= RECENTLY_ENDED_DAYS:
                best = (start, end, "season over")
            if today < start and best is None:
                best = (start, end, "upcoming")
        if best is None:
            continue
        start, end, status = best
        days_left = max((end - today).days, 0) if status != "season over" else 0
        if status == "upcoming":
            factor = 1.0
        else:
            factor = 1 - MAX_PENALTY * max(0.0, (SHIP_DAYS - days_left) / SHIP_DAYS)
        return {"season": season, "start": start.isoformat(), "end": end.isoformat(),
                "days_left": days_left, "status": status, "factor": round(factor, 2)}
    return None


def describe(s: dict) -> str:
    end = dt.date.fromisoformat(s["end"]).strftime("%b %d").replace(" 0", " ")
    if s["status"] == "season over":
        msg = f"Seasonal ({s['season']}): the season already ended {end}"
    elif s["status"] == "upcoming":
        msg = f"Seasonal ({s['season']}): season runs until {end}, not started yet"
    else:
        msg = f"Seasonal ({s['season']}): season ends {end}, {s['days_left']} days left"
    if s["factor"] < 1:
        why = "the season is over" if s["status"] == "season over" else "may end before you can ship"
        msg += f"; score reduced {round((1 - s['factor']) * 100)}% ({why})"
    return msg
