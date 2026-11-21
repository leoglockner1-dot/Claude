"""Tiny HTTP helper (standard library only) with retries and polite pacing."""
from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request

from . import config


class FetchError(Exception):
    pass


def get_json(url: str, params: dict | None = None, retries: int = 3, pause: float = 0.35,
             headers: dict | None = None) -> dict:
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    hdrs = {"User-Agent": config.USER_AGENT, "Accept": "application/json"}
    hdrs.update(headers or {})
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=hdrs)
            with urllib.request.urlopen(req, timeout=25) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            time.sleep(pause)
            return data
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(2 ** attempt * 2)
                continue
            raise FetchError(f"HTTP {e.code} for {url.split('?')[0]}") from e
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
            last_err = e
            time.sleep(2 ** attempt)
    raise FetchError(f"Failed after {retries} tries: {url.split('?')[0]} ({last_err})")
