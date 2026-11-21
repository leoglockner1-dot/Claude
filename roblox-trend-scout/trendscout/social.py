"""YouTube and Reddit buzz for candidate trend keywords."""
from __future__ import annotations

import datetime as dt
import time

from . import config
from .http import FetchError, get_json


def youtube_buzz(keyword: str, days: int = 7) -> dict | None:
    """Recent Roblox videos about the keyword: count and total views (needs YOUTUBE_API_KEY).

    Quota: one search (100 units) + one stats call (1 unit) per keyword. The free daily
    quota is 10,000 units, so ~10 keywords twice a day is comfortably inside it.
    """
    key = config.YOUTUBE_API_KEY
    if not key:
        return None
    since = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%SZ")
    search = get_json("https://www.googleapis.com/youtube/v3/search", {
        "part": "snippet", "q": f"roblox {keyword}", "type": "video", "order": "viewCount",
        "publishedAfter": since, "maxResults": 25, "key": key,
    }, pause=0.2)
    ids = [i["id"]["videoId"] for i in search.get("items", []) if i.get("id", {}).get("videoId")]
    if not ids:
        return {"items": 0, "engagement": 0, "sample": []}
    stats = get_json("https://www.googleapis.com/youtube/v3/videos", {
        "part": "statistics,snippet", "id": ",".join(ids), "key": key,
    }, pause=0.2)
    views, sample = 0, []
    for v in stats.get("items", []):
        n = int(v.get("statistics", {}).get("viewCount", 0) or 0)
        views += n
        sample.append({"title": v["snippet"]["title"][:120], "views": n})
    sample.sort(key=lambda s: -s["views"])
    return {"items": len(ids), "engagement": views, "sample": sample[:5]}


def reddit_buzz(keyword: str) -> dict | None:
    """Posts in the last week mentioning the keyword in Roblox subreddits (no key needed)."""
    try:
        data = get_json("https://www.reddit.com/r/roblox+robloxgamedev+RobloxDevelopers+GamingLeaksAndRumours/search.json", {
            "q": f'"{keyword}"', "restrict_sr": "on", "sort": "new", "t": "week", "limit": 100,
        }, pause=2.0, headers={"User-Agent": config.USER_AGENT})
    except FetchError:
        return None
    posts = [c["data"] for c in data.get("data", {}).get("children", [])]
    engagement = sum(int(p.get("score", 0)) + int(p.get("num_comments", 0)) for p in posts)
    sample = [{"title": p.get("title", "")[:120], "score": p.get("score", 0)}
              for p in sorted(posts, key=lambda p: -int(p.get("score", 0)))[:5]]
    return {"items": len(posts), "engagement": engagement, "sample": sample}


def due(last_ts: float, min_hours: float) -> bool:
    return time.time() - last_ts >= min_hours * 3600
