"""Làm sạch và đếm khảo sát khoản trừ tự động.

Chạy:  python evidence/survey/count.py [evidence/survey/raw-responses-1900.csv]

- Đọc bản xuất gốc từ Google Form (`raw-*`, không commit).
- Ghi `evidence/survey/results.csv`: bỏ cột giờ nộp chi tiết (chỉ giữ ngày) và câu 12,
  thêm cột `cach_thu` và `lam_sach`.
- In số chính để đối chiếu với `evidence/hypothesis.md`. Chạy lại ra đúng số.

Cách thu (xác nhận với Thông 27/11 ~18:15):
- `tu_dien`: người trả lời tự điền form. Đó là các dòng gửi lúc 15:49:55, 15:51:33, 15:52:39, 17:56:15.
- `hoi_mieng`: Thông hỏi miệng trực tiếp từng người, ghi lại, rồi nhập form bằng script
  theo từng đợt (các cụm gửi cách nhau 1–3 giây). Ghi chép gốc do Thông giữ, không commit.

Làm sạch theo đúng quy tắc rẽ nhánh của form (script nhập hộ đã bỏ qua phần rẽ nhánh):
- Câu 2 = "không dùng" → không tính vào mẫu số (form lẽ ra dừng ở đây).
- Câu 4 = "0" hoặc "không nhớ" → bỏ câu 5–9 (form lẽ ra chuyển tới câu 10).
"""
import csv
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
RAW = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "raw-responses-1900.csv"
OUT = HERE / "results.csv"

TU_DIEN = {"27/11/2026 15:49:55", "27/11/2026 15:51:33", "27/11/2026 15:52:39", "27/11/2026 17:56:15"}
COLS = ["stt", "ngay", "cach_thu", "q1_ban_la", "q2_vi_dang_dung", "q3_co_lien_ket_tu_dong",
        "q4_so_lan_3_thang", "q5_hoa_ra_la_gi", "q6_phat_hien_sau", "q7_mat_bao_lau",
        "q8_da_lam_gi", "q9_so_tien", "q10_biet_ngay_tru_tiep", "q11_ke_lai", "lam_sach"]
GAP = ("1", "2", "3 lần trở lên")
LATE = ("1 tuần đến 1 tháng", "hơn 1 tháng")
SLOW = ("15 đến 60 phút", "hơn 1 giờ")
SUB = ("dùng thử hết hạn tự chuyển sang trả phí", "gói tự gia hạn mà mình quên",
       "dịch vụ mình không nhớ đã đăng ký")
ERR = ("giao dịch lỗi hoặc bị trừ 2 lần", "lừa đảo hoặc bị hack")


def clean(raw_rows):
    rows = []
    for i, x in enumerate(raw_rows, 1):
        x = [c.strip() for c in x] + [""] * (13 - len(x))
        note = []
        q = x[1:12]
        if x[2] == "không dùng":
            note.append("câu 2 = không dùng → loại khỏi mẫu số")
        if x[4] not in GAP and any(q[4:9]):
            q[4:9] = [""] * 5
            note.append("câu 4 = %s → bỏ câu 5–9 theo rẽ nhánh" % x[4])
        rows.append([i, datetime.strptime(x[0], "%d/%m/%Y %H:%M:%S").strftime("%Y-%m-%d"),
                     "tu_dien" if x[0] in TU_DIEN else "hoi_mieng"] + q + ["; ".join(note)])
    return rows


def report(rows, label):
    d = {c: [r[k] for r in rows] for k, c in enumerate(COLS)}
    vi = [r for r in rows if r[4] != "không dùng"]
    gap = [r for r in vi if r[6] in GAP]
    late = [r for r in gap if r[8] in LATE or r[9] in SLOW]
    print("== %s: %d phản hồi · dùng ví / thẻ: %d" % (label, len(rows), len(vi)))
    if not vi:
        return
    pct = lambda a, b: "%d/%d" % (a, b) + (" (%.0f%%)" % (100 * a / b) if b >= 10 else "")
    print("  H1 gặp ≥1 lần trong 3 tháng (câu 4):", pct(len(gap), len(vi)))
    print("  H2 trong số đó, phát hiện sau ≥1 tuần HOẶC mất ≥15 phút:", pct(len(late), len(gap)))
    print("     phát hiện sau ≥1 tuần:", pct(sum(r[8] in LATE for r in gap), len(gap)),
          "· mất ≥15 phút:", pct(sum(r[9] in SLOW for r in gap), len(gap)))
    print("  H3 gói đăng ký / dùng thử vs giao dịch lỗi + lừa đảo:",
          sum(r[7] in SUB for r in gap), "vs", sum(r[7] in ERR for r in gap))
    for name, k, base in (("câu 4", 6, vi), ("câu 5", 7, gap), ("câu 6", 8, gap), ("câu 7", 9, gap),
                          ("câu 9", 11, gap), ("câu 10", 12, vi), ("câu 3", 5, vi), ("câu 1", 3, vi)):
        print("  %s (n=%d): %s" % (name, len(base), dict(Counter(r[k] for r in base).most_common())))


def main():
    with RAW.open(encoding="utf-8-sig", newline="") as f:
        raw = list(csv.reader(f))[1:]
    rows = clean(raw)
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(COLS)
        w.writerows(rows)
    print("Đã ghi %s (%d dòng)\n" % (OUT.relative_to(HERE.parents[1]), len(rows)))
    report(rows, "TẤT CẢ")
    report([r for r in rows if r[2] == "hoi_mieng"], "hoi_mieng")
    report([r for r in rows if r[2] == "tu_dien"], "tu_dien")
    dup = Counter(r[13] for r in rows if r[13])
    for text, n in dup.items():
        if n > 1:
            print("\n⚠ câu 11 trùng nguyên văn ở dòng", [r[0] for r in rows if r[13] == text])


if __name__ == "__main__":
    main()
