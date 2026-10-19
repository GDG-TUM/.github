from datetime import date
from pathlib import Path
import importlib.util
import unittest

import yaml

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "update_events.py"
SPEC = importlib.util.spec_from_file_location("update_events", MODULE_PATH)
update_events = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(update_events)


class UpdateEventsTests(unittest.TestCase):
    def test_events_file_is_valid_yaml_with_upcoming_events(self):
        events_path = Path(__file__).resolve().parents[1] / "data" / "events.yml"
        events = yaml.safe_load(events_path.read_text(encoding="utf-8"))

        self.assertIsInstance(events, dict)
        self.assertIn("upcoming_events", events)
        self.assertIsInstance(events["upcoming_events"], list)

    def test_transition_moves_expired_events_without_duplicates(self):
        today = date(2026, 10, 20)
        upcoming = [
            {"title": "Expired", "url": "https://example.com/1", "date": date(2026, 10, 19)},
            {"title": "Upcoming", "url": "https://example.com/2", "date": date(2026, 10, 21)},
        ]
        past = [
            {"title": "Expired", "url": "https://example.com/1", "date": date(2026, 10, 19)},
        ]

        next_upcoming, next_past = update_events.transition_events(upcoming, past, today)

        self.assertEqual([e["title"] for e in next_upcoming], ["Upcoming"])
        self.assertEqual([e["title"] for e in next_past], ["Expired"])

        rerun_upcoming, rerun_past = update_events.transition_events(next_upcoming, next_past, today)
        self.assertEqual(rerun_upcoming, next_upcoming)
        self.assertEqual(rerun_past, next_past)

    def test_render_past_orders_most_recent_first(self):
        past = [
            {"title": "Older", "url": "https://example.com/older", "track": "cloud", "date": date(2026, 10, 12)},
            {"title": "Newer", "url": "https://example.com/newer", "track": "cloud", "date": date(2026, 10, 16)},
        ]

        rendered = update_events.render_past(sorted(past, key=lambda e: e["date"], reverse=True))
        self.assertLess(rendered.find("Newer"), rendered.find("Older"))


if __name__ == "__main__":
    unittest.main()
