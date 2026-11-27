"""Kiểm công cụ CP3 bằng python -m unittest discover -s codebase -v."""

import csv
import unittest
from collections import defaultdict
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

from tools import detect_recurring, lookup_cancel_guide


DATA_DIR = Path(__file__).resolve().parents[1] / "data"
AS_OF = "2026-11-27"


def read_rows(filename):
    with (DATA_DIR / filename).open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


class DetectRecurringTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.by_user = defaultdict(list)
        for row in read_rows("transactions.csv"):
            cls.by_user[row["user_id"]].append(row)

    def test_all_synthetic_cases(self):
        truth = defaultdict(list)
        for row in read_rows("recurring_truth.csv"):
            truth[row["user_id"]].append(row)
        for user_id, expected in truth.items():
            with self.subTest(user_id=user_id):
                history = self.by_user[user_id]
                actual = {
                    tuple(candidate["tx_ids"]): candidate
                    for candidate in detect_recurring(history, AS_OF)
                }
                self.assertEqual(set(actual), {tuple(row["tx_ids"].split()) for row in expected})
                transactions = {row["tx_id"]: row for row in history}
                for row in expected:
                    tx_ids = tuple(row["tx_ids"].split())
                    candidate = actual[tx_ids]
                    next_date = row["next_date"] or None
                    cycle_days = int(row["cycle_days"]) if row["cycle_days"] else None
                    status = "recurring" if next_date else "insufficient_history"
                    # Kịch bản có ngày đã định nhưng CSV chỉ có một lần trả phí.
                    if row["series_id"] in {"U01-S1", "U04-S1"}:
                        next_date = cycle_days = None
                        status = "insufficient_history"
                    if row["kind"] == "giao_dich_loi":
                        status = "possible_duplicate"
                    self.assertEqual(candidate["evidence_status"], status, row["series_id"])
                    self.assertEqual(candidate["next_date"], next_date, row["series_id"])
                    self.assertEqual(candidate["cycle_days"], cycle_days, row["series_id"])
                    self.assertEqual(candidate["last_date"], row["last_date"], row["series_id"])
                    self.assertEqual(candidate["source"], row["nguon_tien"], row["series_id"])
                    self.assertEqual(candidate["amount_vnd"], int(transactions[tx_ids[-1]]["amount_vnd"]))
                    self.assertEqual(candidate["essential_bill"], row["kind"] == "hoa_don_thiet_yeu")

    def test_month_end_and_no_future_or_failed_charges(self):
        rows = [
            {
                "tx_id": str(index), "user_id": "U01", "time": day + " 09:00:00",
                "description": "Ví dụ gói thu phí", "amount_vnd": "10000",
                "source": "vi", "status": status,
            }
            for index, (day, status) in enumerate([
                ("2026-01-31", "thanh_cong"), ("2026-02-28", "thanh_cong"),
                ("2026-03-15", "that_bai"), ("2026-03-31", "thanh_cong"),
                ("2026-04-15", "thanh_cong"),
            ])
        ]
        candidate, = detect_recurring(rows[::-1] + [rows[0]], date(2026, 4, 1))
        self.assertEqual(candidate["tx_ids"], ["0", "1", "3"])
        self.assertEqual(candidate["cycle_unit"], "month")
        self.assertEqual(candidate["next_date"], "2026-04-30")
        stale, = detect_recurring(rows[:4], "2026-05-01")
        self.assertEqual(stale["evidence_status"], "recurring")
        self.assertIsNone(stale["next_date"])

    def test_rejects_mixed_user_history(self):
        with self.assertRaisesRegex(ValueError, "một người dùng"):
            detect_recurring(self.by_user["U01"] + self.by_user["U02"], AS_OF)


class LookupCancelGuideTest(unittest.TestCase):
    def test_official_guides(self):
        expected_domains = {
            "app_store": "support.apple.com",
            "google_play": "support.google.com",
            "youtube": "support.google.com",
            "spotify": "support.spotify.com",
            "netflix": "help.netflix.com",
            "chatgpt": "help.openai.com",
            "paypal": "www.paypal.com",
            "microsoft_365": "support.microsoft.com",
            "disney_plus": "help.disneyplus.com",
        }
        for channel, domain in expected_domains.items():
            with self.subTest(channel=channel):
                guide = lookup_cancel_guide(channel)
                self.assertEqual(guide["channel"], channel)
                self.assertTrue(all(guide["steps"]))
                self.assertGreaterEqual(len(guide["steps"]), 2)
                url = urlsplit(guide["official_url"])
                self.assertEqual((url.scheme, url.hostname), ("https", domain))
                self.assertGreaterEqual(date.fromisoformat(guide["checked_on"]), date(2026, 11, 27))

    def test_alias_and_unknown_channel(self):
        self.assertEqual(lookup_cancel_guide("  APPLE.COM/BILL  ")["channel"], "app_store")
        self.assertEqual(lookup_cancel_guide("YouTube Premium")["channel"], "youtube")
        self.assertIsNone(lookup_cancel_guide("Netflix giả mạo"))
        self.assertIsNone(lookup_cancel_guide("hóa đơn tiền điện"))
        self.assertIsNone(lookup_cancel_guide(""))
