"""Kiểm hồi quy ngày gia hạn CP4 bằng python -m unittest discover -s codebase -v."""

import csv
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from agent import answer
from tools import lookup_renewal_schedule


class RenewalRegressionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = Path(__file__).resolve().parents[1] / "eval" / "benchmark.csv"
        with path.open(encoding="utf-8-sig", newline="") as file:
            cls.cases = {row["id"]: row["input"] for row in csv.DictReader(file)}

    def test_b01_and_b13_show_sourced_renewal(self):
        model_output = {"text": json.dumps({
            "dich_vu": "BaoThuc Pro", "kenh": "khong_ro", "loai": "goi_dang_ky",
        })}
        with patch("agent.call_model", return_value=model_output):
            for case_id in ("B01", "B13"):
                with self.subTest(case_id=case_id):
                    output = answer(self.cases[case_id])["output"]
                    self.assertIn("BaoThuc Pro", output)
                    self.assertIn("179.000đ", output)
                    self.assertIn("29/11/2026", output)
                    self.assertIn("còn 2 ngày", output)
                    self.assertIn("lịch giả lập SIM-GP-RENEWAL-001", output)
                    self.assertIn("support.google.com/googleplay", output)
                    self.assertNotIn("Spotify", output)
                    self.assertNotIn("Lịch sử chưa đủ", output)

    def test_b13_without_schedule_remains_unconfirmed(self):
        with patch("agent.lookup_renewal_schedule", return_value=None):
            output = answer(self.cases["B13"])["output"]
        self.assertIn("chưa có cảnh báo", output)
        self.assertNotIn("29/11/2026", output)

    def test_alert_window_and_unknown_source_regressions(self):
        model_output = {"text": "{}"}
        with patch("agent.call_model", return_value=model_output):
            due = answer(self.cases["B14"])["output"]
            future = answer(self.cases["B15"])["output"]
            annual = answer(self.cases["B05"])["output"]
        self.assertIn("30/11/2026", due)
        self.assertNotIn("PAYPAL", due)
        self.assertIn("chưa có cảnh báo", future)
        self.assertIn("Lịch sử chưa đủ", annual)
        self.assertNotIn("16/11/2027", annual)

    def test_schedule_matches_user_transaction_and_observation_window(self):
        for user_id, tx_id, as_of_date in (
            ("U02", "T00228", "2026-11-27"),
            ("U01", "T00214", "2026-11-27"),
            ("U01", "T00228", "2026-11-26"),
            ("U01", "T00228", "2026-11-30"),
        ):
            with self.subTest(user_id=user_id, tx_id=tx_id, as_of_date=as_of_date):
                self.assertIsNone(lookup_renewal_schedule(user_id, tx_id, as_of_date))

    def test_schedule_without_source_does_not_supply_a_date(self):
        with TemporaryDirectory() as directory:
            data_dir = Path(directory)
            (data_dir / "renewal_schedules.csv").write_text(
                "user_id,tx_id,observed_on,next_date,cycle_unit,cycle_days,channel,source_ref\n"
                "U01,T00228,2026-11-27,2026-11-29,month,30,google_play,\n",
                encoding="utf-8",
            )
            with patch("tools.DATA_DIR", data_dir):
                self.assertIsNone(lookup_renewal_schedule("U01", "T00228", "2026-11-27"))
