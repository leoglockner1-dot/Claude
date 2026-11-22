"""Mac notifications after each collection.

Alerts:
- a niche enters the top TOP_N that wasn't there after the previous collection
- a niche's leading game has JUMP_THRESHOLD more players than the same time yesterday

Each niche alerts at most once per COOLDOWN_HOURS, and all alerts from one run are grouped into a
single notification so you don't get spammed.
"""
from __future__ import annotations

import json
import platform
import subprocess
import time

from . import config, niches

TOP_N = 5
JUMP_THRESHOLD = float(config.get("NOTIFY_JUMP", "0.5") or 0.5)   # 0.5 = +50% vs yesterday
COOLDOWN_HOURS = 24
ENABLED = config.get("NOTIFICATIONS", "on").lower() not in ("off", "0", "false", "no")

SCHEMA = """
CREATE TABLE IF NOT EXISTS alert_state (key TEXT PRIMARY KEY, value TEXT);
CREATE TABLE IF NOT EXISTS alerts (ts REAL, kind TEXT, niche_id TEXT, text TEXT);
"""


def send(title: str, message: str, subtitle: str = "") -> bool:
    """Show a macOS notification. Returns False (and prints instead) on other systems."""
    if platform.system() != "Darwin":
        print(f"[notification] {title}: {subtitle} {message}")
        return False
    q = lambda s: '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    script = f"display notification {q(message[:250])} with title {q(title)}"
    if subtitle:
        script += f" subtitle {q(subtitle[:120])}"
    script += ' sound name "Glass"'
    try:
        subprocess.run(["osascript", "-e", script], check=True, timeout=10, capture_output=True)
        return True
    except (OSError, subprocess.SubprocessError) as e:
        print(f"Could not show notification: {e}")
        return False


def _get(conn, key: str, default):
    row = conn.execute("SELECT value FROM alert_state WHERE key=?", (key,)).fetchone()
    return json.loads(row[0]) if row else default


def _set(conn, key: str, value) -> None:
    conn.execute("INSERT OR REPLACE INTO alert_state VALUES (?, ?)", (key, json.dumps(value)))


def check(conn, niche_list: list[dict] | None = None, log=print) -> list[str]:
    """Compare the current niches with the last run, notify about changes, return alert texts."""
    conn.executescript(SCHEMA)
    if niche_list is None:
        niche_list = niches.find_niches(conn)
    now = time.time()
    last_alert: dict = _get(conn, "last_alert", {})
    prev_top = _get(conn, "top", None)
    top = [x["id"] for x in niche_list[:TOP_N]]

    def cooled(nid: str) -> bool:
        return now - last_alert.get(nid, 0) >= COOLDOWN_HOURS * 3600

    def short(x: dict) -> str:
        tag = f" [{x['seasonal']['season']}]" if x.get("seasonal") else ""
        return f"{x['label']}{tag}: {x['lead_name'][:40]} ({x['lead_playing']:,} players, {round(x['lead_age_days'])}d old)"

    alerts: list[tuple[str, dict]] = []
    if prev_top is not None:   # first run ever: just remember the top list, don't alert
        for rank, x in enumerate(niche_list[:TOP_N], 1):
            if x["id"] not in prev_top and cooled(x["id"]):
                alerts.append(("new_top", x))
    for x in niche_list:
        dod = x.get("lead_ccu_dod")
        if dod is not None and dod >= JUMP_THRESHOLD and cooled(x["id"]) and all(a[1] is not x for a in alerts):
            alerts.append(("jump", x))

    texts = []
    for kind, x in alerts:
        text = (f"New in top {TOP_N}: {short(x)}" if kind == "new_top"
                else f"Up {x['lead_ccu_dod']:+.0%} vs yesterday: {short(x)}")
        texts.append(text)
        last_alert[x["id"]] = now
        conn.execute("INSERT INTO alerts VALUES (?,?,?,?)", (now, kind, x["id"], text))
    _set(conn, "top", top)
    _set(conn, "last_alert", {k: v for k, v in last_alert.items() if now - v < 7 * 86400})
    conn.commit()

    if texts:
        log(f"{len(texts)} alert(s): " + " | ".join(texts))
        if ENABLED:
            title = "Roblox Trend Scout"
            if len(texts) == 1:
                send(title, texts[0].split(": ", 1)[1], subtitle=texts[0].split(": ", 1)[0])
            else:
                send(title, " • ".join(t.split(": ", 1)[1].split(":")[0] for t in texts),
                     subtitle=f"{len(texts)} niche alerts, open the dashboard")
    return texts


def recent(conn, limit: int = 10) -> list[dict]:
    conn.executescript(SCHEMA)
    return [dict(r) for r in conn.execute("SELECT * FROM alerts ORDER BY ts DESC LIMIT ?", (limit,))]
