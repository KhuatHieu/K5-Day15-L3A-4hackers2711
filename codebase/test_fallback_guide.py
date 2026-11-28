"""Kiểm cải tiến lượt 2: hướng dẫn kiểm tra dự phòng có nguồn (dòng kiem_tra_* trong data/cancel_guides.csv).

Chạy: python -m unittest discover -s codebase -v
Dữ liệu hướng dẫn được giả lập trong test, nên test không phụ thuộc link thật trong bảng.
"""

import csv
import json
import unittest
from pathlib import Path
from unittest.mock import patch

import agent
from agent import answer
from tools import lookup_cancel_guide as real_lookup

FAKE = {
    agent.GUIDE_KHONG_RO: {"channel": agent.GUIDE_KHONG_RO, "service": "Kiểm tra trong ví",
                           "official_url": "https://example.invalid/vi", "checked_on": "2026-11-28",
                           "steps": ["Mở mục thanh toán tự động trong ví.", "Đối chiếu khoản trừ."]},
    agent.GUIDE_HOA_DON: {"channel": agent.GUIDE_HOA_DON, "service": "Đối chiếu hoá đơn",
                          "official_url": "https://example.invalid/hoa-don", "checked_on": "2026-11-28",
                          "steps": ["Tra cứu hoá đơn trên kênh chính thức.", "So với số tiền ví đã trừ."]},
}


def fake_lookup(key):
    return FAKE.get(key) or real_lookup(key)


def no_fallback(key):
    return None if key.startswith(agent.FALLBACK_PREFIX) else real_lookup(key)


class FallbackGuideTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = Path(__file__).resolve().parents[1] / "eval" / "benchmark.csv"
        with path.open(encoding="utf-8-sig", newline="") as file:
            cls.cases = {row["id"]: row["input"] for row in csv.DictReader(file)}

    def run_case(self, case_id, model_json, lookup):
        with patch("agent.call_model", return_value={"text": json.dumps(model_json)}), \
                patch("agent.lookup_cancel_guide", side_effect=lookup):
            return answer(self.cases[case_id])["output"]

    def test_unknown_source_gets_sourced_check_steps(self):
        out = self.run_case("B14", {}, fake_lookup)
        self.assertIn("chưa xác định được dịch vụ", out)
        self.assertIn("Mình chưa xác định được nơi thu tiền", out)
        self.assertIn("https://example.invalid/vi", out)
        self.assertIn("30/11/2026", out)
        self.assertNotIn("PAYPAL", out)
        self.assertNotIn("Người thu tiền là", out)

    def test_essential_bill_gets_check_steps_not_cancel(self):
        out = self.run_case("B19", {"dich_vu": "EVN", "kenh": "khong_ro", "loai": "hoa_don_thiet_yeu"}, fake_lookup)
        self.assertIn("không gợi ý huỷ", out)
        self.assertIn("https://example.invalid/hoa-don", out)
        self.assertNotIn("example.invalid/vi", out)
        self.assertNotIn("huỷ theo các bước", out)

    def test_known_channel_keeps_cancel_guide(self):
        out = self.run_case("B01", {"dich_vu": "BaoThuc Pro", "kenh": "google_play", "loai": "goi_dang_ky"},
                            fake_lookup)
        self.assertIn("support.google.com/googleplay", out)
        self.assertNotIn("example.invalid", out)

    def test_without_fallback_rows_behaviour_unchanged(self):
        out = self.run_case("B14", {}, no_fallback)
        self.assertIn("Mình chưa có hướng dẫn có nguồn cho khoản này", out)
        out = self.run_case("B19", {"dich_vu": "EVN", "kenh": "khong_ro", "loai": "hoa_don_thiet_yeu"}, no_fallback)
        self.assertIn("không gợi ý huỷ", out)
        self.assertNotIn("Nguồn:", out)

    def test_fallback_rows_not_offered_to_model(self):
        self.assertFalse(any(c.startswith(agent.FALLBACK_PREFIX) for c in agent.CHANNELS))
        self.assertNotIn(agent.FALLBACK_PREFIX, agent.SYSTEM)


if __name__ == "__main__":
    unittest.main()
