"""Kiểm nhánh câu ngoài chủ đề (sau CP4): chào hỏi / hỏi linh tinh → hướng dẫn, không đọc lịch sử, không gọi model.

Chạy: python -m unittest discover -s codebase -v
"""
import csv
import json
import unittest
from pathlib import Path
from unittest.mock import patch

import tracing
from agent import answer, on_topic

FAKE_MODEL = {"text": json.dumps({"dich_vu": "không rõ", "kenh": "khong_ro", "loai": "khong_ro"}),
              "model": "fake", "tokens_in": 0, "tokens_out": 0}

BENCHMARK = Path(__file__).resolve().parents[1] / "eval" / "benchmark.csv"


def run(text):
    """Không gọi model thật: thay call_model bằng JSON "không rõ" cố định."""
    tracing.begin("t")
    with patch("agent.call_model", return_value=FAKE_MODEL):
        out = answer(text)["output"]
    summary, events = tracing.end()
    return out, summary, events


class OffTopicTest(unittest.TestCase):
    def test_greeting_gets_help_without_history_or_model(self):
        for text in ("[U01] xin chào", "[U01] hôm nay trời đẹp không", "[U03] cảm ơn nhé"):
            out, summary, events = run(text)
            self.assertIn("Mình chỉ hỗ trợ các khoản trừ tiền định kỳ", out)
            self.assertEqual(summary["model_calls"], 0)
            self.assertNotIn("get_transactions", [e.get("name") for e in events])
            self.assertNotIn("Khoản **", out)

    def test_questions_about_charges_still_answered(self):
        for text in ("[U01] Spotify?", "[U01] mình đang trả gói gì", "[U02] 99k hôm 18/11 là gì"):
            self.assertTrue(on_topic(text), text)
            out, _, _ = run(text)
            self.assertIn("Khoản **", out)

    def test_every_benchmark_question_stays_on_topic(self):
        with BENCHMARK.open(encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                if "kiem_tra" in row["input"]:
                    continue
                self.assertTrue(on_topic(row["input"]), row["id"])


if __name__ == "__main__":
    unittest.main()
