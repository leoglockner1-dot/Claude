"""Collectors for Roblox's public web APIs (no login or key needed)."""
from __future__ import annotations

import uuid

from .http import FetchError, get_json

SORTS_URL = "https://apis.roblox.com/explore-api/v1/get-sorts"
SEARCH_URL = "https://apis.roblox.com/search-api/omni-search"
GAMES_URL = "https://games.roblox.com/v1/games"
VOTES_URL = "https://games.roblox.com/v1/games/votes"

# Charts that matter most for spotting what's *upcoming*.
KEY_SORTS = ("up-and-coming", "top-trending", "top-playing-now", "fun-with-friends",
             "top-revisited", "top-earning", "top-rated", "most-popular")


def fetch_charts(max_pages: int = 6) -> dict[str, list[int]]:
    """Return {sort_id: [universe_id, ...in rank order]} for every game chart on Explore."""
    session_id = str(uuid.uuid4())
    charts: dict[str, list[int]] = {}
    token = None
    for _ in range(max_pages):
        params = {"device": "all", "country": "all", "sessionId": session_id}
        if token:
            params["sortsPageToken"] = token
        data = get_json(SORTS_URL, params)
        for sort in data.get("sorts", []):
            games = sort.get("games") or []
            if sort.get("contentType") == "Games" or games:
                ids = [g["universeId"] for g in games if g.get("universeId")]
                if ids:
                    charts[sort.get("sortId") or sort.get("id")] = ids
        token = data.get("nextSortsPageToken")
        if not token:
            break
    return charts


def _chunks(seq: list, n: int):
    for i in range(0, len(seq), n):
        yield seq[i:i + n]


def fetch_game_details(universe_ids: list[int]) -> list[dict]:
    out: list[dict] = []
    for chunk in _chunks(universe_ids, 50):
        data = get_json(GAMES_URL, {"universeIds": ",".join(map(str, chunk))})
        for g in data.get("data", []):
            creator = g.get("creator") or {}
            out.append({
                "universe_id": g["id"],
                "root_place_id": g.get("rootPlaceId"),
                "name": g.get("name") or "",
                "description": (g.get("description") or "")[:1500],
                "creator_id": creator.get("id"),
                "creator_name": creator.get("name"),
                "creator_type": creator.get("type"),
                "genre_l1": g.get("genre_l1") or "",
                "genre_l2": g.get("genre_l2") or "",
                "created": g.get("created"),
                "updated": g.get("updated"),
                "url_path": g.get("canonicalUrlPath"),
                "playing": g.get("playing") or 0,
                "visits": g.get("visits") or 0,
                "favorites": g.get("favoritedCount") or 0,
            })
    return out


def fetch_votes(universe_ids: list[int]) -> dict[int, tuple[int, int]]:
    votes: dict[int, tuple[int, int]] = {}
    for chunk in _chunks(universe_ids, 50):
        try:
            data = get_json(VOTES_URL, {"universeIds": ",".join(map(str, chunk))})
        except FetchError:
            continue
        for v in data.get("data", []):
            votes[v["id"]] = (v.get("upVotes") or 0, v.get("downVotes") or 0)
    return votes


def search_games(keyword: str, pages: int = 1) -> list[dict]:
    """Search Roblox for a theme keyword. Used to measure supply (how many games compete)."""
    session_id = str(uuid.uuid4())
    results: list[dict] = []
    token = None
    for _ in range(pages):
        params = {"searchQuery": keyword, "sessionId": session_id, "pageType": "all"}
        if token:
            params["pageToken"] = token
        data = get_json(SEARCH_URL, params)
        for group in data.get("searchResults", []):
            if group.get("contentGroupType") != "Game":
                continue
            for c in group.get("contents", []):
                results.append({"universe_id": c.get("universeId"), "name": c.get("name"),
                                "playing": c.get("playerCount") or 0})
        token = data.get("nextPageToken")
        if not token:
            break
    return results
