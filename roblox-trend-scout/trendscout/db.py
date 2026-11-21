"""SQLite storage. Every collection run adds a snapshot, so trends get sharper over time."""
from __future__ import annotations

import json
import sqlite3
import time
from contextlib import contextmanager

from . import config

SCHEMA = """
CREATE TABLE IF NOT EXISTS runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts REAL NOT NULL,
    notes TEXT
);
CREATE TABLE IF NOT EXISTS games (
    universe_id INTEGER PRIMARY KEY,
    root_place_id INTEGER,
    name TEXT,
    description TEXT,
    creator_id INTEGER,
    creator_name TEXT,
    creator_type TEXT,
    genre_l1 TEXT,
    genre_l2 TEXT,
    created TEXT,
    updated TEXT,
    url_path TEXT,
    first_seen REAL,
    last_seen REAL
);
CREATE TABLE IF NOT EXISTS snapshots (
    run_id INTEGER NOT NULL,
    universe_id INTEGER NOT NULL,
    ts REAL NOT NULL,
    playing INTEGER,
    visits INTEGER,
    favorites INTEGER,
    up_votes INTEGER,
    down_votes INTEGER,
    PRIMARY KEY (run_id, universe_id)
);
CREATE INDEX IF NOT EXISTS idx_snap_game ON snapshots(universe_id, ts);
CREATE TABLE IF NOT EXISTS chart_entries (
    run_id INTEGER NOT NULL,
    universe_id INTEGER NOT NULL,
    sort_id TEXT NOT NULL,
    rank INTEGER,
    PRIMARY KEY (run_id, universe_id, sort_id)
);
CREATE TABLE IF NOT EXISTS search_supply (
    run_id INTEGER NOT NULL,
    keyword TEXT NOT NULL,
    ts REAL NOT NULL,
    n_results INTEGER,
    total_playing INTEGER,
    top_playing INTEGER,
    PRIMARY KEY (run_id, keyword)
);
CREATE TABLE IF NOT EXISTS social (
    ts REAL NOT NULL,
    source TEXT NOT NULL,
    keyword TEXT NOT NULL,
    items INTEGER,
    engagement INTEGER,
    sample TEXT,
    PRIMARY KEY (ts, source, keyword)
);
CREATE TABLE IF NOT EXISTS recommendations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts REAL NOT NULL,
    model TEXT,
    payload TEXT
);
"""


def connect() -> sqlite3.Connection:
    config.DATA_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(config.DB_PATH, timeout=30)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.executescript(SCHEMA)
    return conn


@contextmanager
def session():
    conn = connect()
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def new_run(conn: sqlite3.Connection, notes: str = "") -> int:
    cur = conn.execute("INSERT INTO runs(ts, notes) VALUES (?, ?)", (time.time(), notes))
    return int(cur.lastrowid)


def upsert_game(conn: sqlite3.Connection, g: dict, now: float) -> None:
    conn.execute(
        """
        INSERT INTO games(universe_id, root_place_id, name, description, creator_id, creator_name,
                          creator_type, genre_l1, genre_l2, created, updated, url_path, first_seen, last_seen)
        VALUES (:universe_id, :root_place_id, :name, :description, :creator_id, :creator_name,
                :creator_type, :genre_l1, :genre_l2, :created, :updated, :url_path, :now, :now)
        ON CONFLICT(universe_id) DO UPDATE SET
            root_place_id=excluded.root_place_id, name=excluded.name, description=excluded.description,
            creator_id=excluded.creator_id, creator_name=excluded.creator_name,
            creator_type=excluded.creator_type, genre_l1=excluded.genre_l1, genre_l2=excluded.genre_l2,
            created=excluded.created, updated=excluded.updated, url_path=excluded.url_path,
            last_seen=excluded.last_seen
        """,
        {**g, "now": now},
    )


def last_social_ts(conn: sqlite3.Connection, source: str) -> float:
    row = conn.execute("SELECT MAX(ts) FROM social WHERE source=?", (source,)).fetchone()
    return float(row[0] or 0)


def save_recommendation(conn: sqlite3.Connection, model: str, payload: dict) -> int:
    cur = conn.execute(
        "INSERT INTO recommendations(ts, model, payload) VALUES (?, ?, ?)",
        (time.time(), model, json.dumps(payload)),
    )
    return int(cur.lastrowid)


def latest_recommendation(conn: sqlite3.Connection) -> dict | None:
    row = conn.execute("SELECT * FROM recommendations ORDER BY id DESC LIMIT 1").fetchone()
    if not row:
        return None
    return {"id": row["id"], "ts": row["ts"], "model": row["model"], **json.loads(row["payload"])}
