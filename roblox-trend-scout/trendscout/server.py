"""Local dashboard: http://127.0.0.1:8765 (only reachable from your own laptop)."""
from __future__ import annotations

import json
import threading
import time
import traceback
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from . import analyze, collect, config, db, recommend

STATIC = Path(__file__).parent / "static"
TYPES = {".html": "text/html; charset=utf-8", ".js": "application/javascript; charset=utf-8",
         ".css": "text/css; charset=utf-8", ".svg": "image/svg+xml"}


class Jobs:
    """Runs collect / recommend in a background thread so the page stays responsive."""

    def __init__(self):
        self.lock = threading.Lock()
        self.state = {"running": None, "log": [], "last_error": None, "finished_ts": None}

    def start(self, name: str, fn) -> bool:
        with self.lock:
            if self.state["running"]:
                return False
            self.state.update(running=name, log=[], last_error=None)

        def log(line: str):
            with self.lock:
                self.state["log"] = (self.state["log"] + [line])[-40:]

        def work():
            try:
                fn(log=log)
            except Exception as e:  # report any failure to the page instead of crashing
                traceback.print_exc()
                with self.lock:
                    self.state["last_error"] = str(e)
            finally:
                with self.lock:
                    self.state.update(running=None, finished_ts=time.time())

        threading.Thread(target=work, daemon=True).start()
        return True

    def snapshot(self) -> dict:
        with self.lock:
            return dict(self.state)


JOBS = Jobs()


def _history(universe_ids: list[int]) -> dict:
    with db.session() as conn:
        out = {}
        for uid in universe_ids[:8]:
            rows = conn.execute("SELECT ts, playing FROM snapshots WHERE universe_id=? ORDER BY ts", (uid,))
            out[str(uid)] = [[r["ts"], r["playing"]] for r in rows]
        return out


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):  # keep the terminal quiet
        pass

    def _send(self, code: int, body: bytes, ctype: str):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, obj, code: int = 200):
        self._send(code, json.dumps(obj, default=str).encode(), "application/json")

    def do_GET(self):
        url = urlparse(self.path)
        try:
            if url.path in ("/", "/index.html"):
                return self._static("index.html")
            if url.path.startswith("/static/"):
                return self._static(url.path[len("/static/"):])
            if url.path == "/api/status":
                with db.session() as conn:
                    first, last, n = conn.execute("SELECT MIN(ts), MAX(ts), COUNT(*) FROM runs").fetchone()
                report_meta = {"runs": n, "last_run_ts": last,
                               "history_hours": round((time.time() - first) / 3600, 1) if first else 0}
                return self._json({"meta": report_meta, "job": JOBS.snapshot(),
                                   "keys": {"anthropic": bool(config.ANTHROPIC_API_KEY),
                                            "youtube": bool(config.YOUTUBE_API_KEY)},
                                   "model": config.CLAUDE_MODEL})
            if url.path == "/api/trends":
                rep = analyze.analyze()
                for t in rep["trends"]:
                    t["games"] = [{k: v for k, v in g.items() if k != "description"} for g in t["games"][:12]]
                return self._json(rep)
            if url.path == "/api/history":
                ids = [int(x) for x in parse_qs(url.query).get("ids", [""])[0].split(",") if x.isdigit()]
                return self._json(_history(ids))
            if url.path == "/api/recommendation":
                with db.session() as conn:
                    return self._json(db.latest_recommendation(conn))
            self._json({"error": "not found"}, 404)
        except Exception as e:
            traceback.print_exc()
            self._json({"error": str(e)}, 500)

    def do_POST(self):
        # Only accept requests from our own page (blocks other websites from poking the API).
        origin = self.headers.get("Origin", "")
        if origin and not origin.startswith((f"http://127.0.0.1:{config.PORT}", f"http://localhost:{config.PORT}")):
            return self._json({"error": "forbidden"}, 403)
        path = urlparse(self.path).path
        if path == "/api/collect":
            ok = JOBS.start("collect", collect.run)
        elif path == "/api/recommend":
            ok = JOBS.start("recommend", recommend.recommend)
        else:
            return self._json({"error": "not found"}, 404)
        self._json({"started": ok, "job": JOBS.snapshot()}, 200 if ok else 409)

    def _static(self, name: str):
        f = (STATIC / name).resolve()
        if STATIC.resolve() not in f.parents or not f.is_file():
            return self._json({"error": "not found"}, 404)
        self._send(200, f.read_bytes(), TYPES.get(f.suffix, "application/octet-stream"))


def serve(open_browser: bool = True):
    db.connect().close()
    server = ThreadingHTTPServer(("127.0.0.1", config.PORT), Handler)
    url = f"http://127.0.0.1:{config.PORT}"
    print(f"Roblox Trend Scout is running at {url}  (press Ctrl+C to stop)")
    if open_browser:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
