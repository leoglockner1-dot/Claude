import os
import sys
import tempfile
import time
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from trendscout import analyze, config, db, recommend  # noqa: E402

DAY = 86400


class KeywordTests(unittest.TestCase):
    def test_strips_tags_and_stopwords(self):
        kws = analyze.keywords_for("[🎃 NEW QUEST] Steal An Egg!")
        self.assertIn("steal", kws)
        self.assertIn("egg", kws)
        self.assertIn("steal egg", kws)
        self.assertNotIn("quest", kws)
        self.assertNotIn("new", kws)

    def test_plus_one_games(self):
        self.assertIn("plus1", analyze.keywords_for("[🌍WORLD 2] +1 Venom Evolution"))

    def test_plurals_fold(self):
        self.assertIn("animal", analyze.keywords_for("Adopt Animals"))
        self.assertIn("boss", analyze.keywords_for("Boss Fight"))


class PercentileTests(unittest.TestCase):
    def test_ranks_and_unknowns(self):
        self.assertEqual(analyze._percentiles([1, 2, 3, None]), [0.0, 0.5, 1.0, 0.5])
        self.assertEqual(analyze._percentiles([None, None]), [0.5, 0.5])


class MetricsTests(unittest.TestCase):
    def test_growth_and_velocity(self):
        now = time.time()
        game = {"universe_id": 1, "name": "X", "creator_name": "c", "creator_id": 1, "genre_l1": "",
                "genre_l2": "", "root_place_id": 9, "description": "", "updated": None,
                "created": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now - 10 * DAY))}
        snaps = [
            {"ts": now - 2 * DAY, "playing": 1000, "visits": 100_000, "favorites": 0, "up_votes": 90, "down_votes": 10},
            {"ts": now - DAY, "playing": 1000, "visits": 150_000, "favorites": 0, "up_votes": 90, "down_votes": 10},
            {"ts": now, "playing": 2000, "visits": 250_000, "favorites": 0, "up_votes": 90, "down_votes": 10},
        ]
        m = analyze.game_metrics(game, snaps, {"up-and-coming"}, now)
        self.assertAlmostEqual(m["ccu_dod"], 1.0)
        self.assertAlmostEqual(m["recent_vpd"], 100_000, delta=1)
        self.assertAlmostEqual(m["accel"], 1.0, delta=0.01)   # 100k/day vs 50k/day
        self.assertAlmostEqual(m["like_ratio"], 0.9)
        self.assertGreater(m["momentum"], 0)


class EndToEndTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        config.DATA_DIR = Path(self.tmp.name)
        config.DB_PATH = config.DATA_DIR / "t.db"

    def tearDown(self):
        self.tmp.cleanup()

    def test_young_growing_theme_beats_old_static_one(self):
        now = time.time()
        iso = lambda days: time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now - days * DAY))
        games = [  # (id, name, creator, age, ccu then, ccu now)
            (1, "Steal a Pizza", 1, 20, 2000, 6000), (2, "Steal a Car", 2, 15, 1000, 4000),
            (3, "Steal the Moon", 3, 30, 3000, 5000),
            (4, "Old Castle Wars", 4, 900, 5000, 5000), (5, "Castle Defense", 5, 1200, 4000, 3900),
        ]
        with db.session() as conn:
            r0 = db.new_run(conn)
            conn.execute("UPDATE runs SET ts=? WHERE id=?", (now - DAY, r0))
            r1 = db.new_run(conn)
            for uid, name, cr, age, c0, c1 in games:
                db.upsert_game(conn, {"universe_id": uid, "root_place_id": uid, "name": name, "description": "",
                                      "creator_id": cr, "creator_name": f"c{cr}", "creator_type": "User",
                                      "genre_l1": "Simulation", "genre_l2": "", "created": iso(age),
                                      "updated": iso(1), "url_path": ""}, now)
                conn.execute("INSERT INTO snapshots VALUES (?,?,?,?,?,?,?,?)", (r0, uid, now - DAY, c0, c0 * 100, 0, 90, 10))
                conn.execute("INSERT INTO snapshots VALUES (?,?,?,?,?,?,?,?)", (r1, uid, now, c1, c1 * 130, 0, 90, 10))
            conn.execute("INSERT INTO chart_entries VALUES (?,?,?,?)", (r1, 1, "up-and-coming", 1))
        rep = analyze.analyze()
        labels = [t["keyword"] for t in rep["trends"]]
        self.assertIn("steal", labels)
        self.assertIn("castle", labels)
        self.assertLess(labels.index("steal"), labels.index("castle"))


class SchemaTests(unittest.TestCase):
    def test_strict_schema_shape(self):
        def walk(node):
            if node.get("type") == "object":
                self.assertFalse(node["additionalProperties"])
                self.assertEqual(set(node["required"]), set(node["properties"]))
                for child in node["properties"].values():
                    walk(child)
            elif node.get("type") == "array":
                walk(node["items"])
        walk(recommend.SCHEMA)


if __name__ == "__main__":
    unittest.main()
