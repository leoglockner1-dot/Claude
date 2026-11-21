"""Settings, loaded from the .env file in the project folder (and the real environment)."""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DB_PATH = DATA_DIR / "trends.db"
ENV_PATH = ROOT / ".env"


def _load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key, value = key.strip(), value.strip().strip('"').strip("'")
        # Real environment variables win over the file; empty values are ignored.
        if value and key not in os.environ:
            os.environ[key] = value


_load_env_file(ENV_PATH)


def get(name: str, default: str = "") -> str:
    return os.environ.get(name, default).strip()


ANTHROPIC_API_KEY = get("ANTHROPIC_API_KEY")
YOUTUBE_API_KEY = get("YOUTUBE_API_KEY")
CLAUDE_MODEL = get("TRENDSCOUT_MODEL", "claude-opus-5-5")
CLAUDE_EFFORT = get("TRENDSCOUT_EFFORT", "high")
PORT = int(get("PORT", "8765") or 8765)
YOUTUBE_MIN_HOURS = float(get("YOUTUBE_MIN_HOURS", "12") or 12)
REDDIT_MIN_HOURS = float(get("REDDIT_MIN_HOURS", "6") or 6)

USER_AGENT = "RobloxTrendScout/0.1 (personal research tool)"
