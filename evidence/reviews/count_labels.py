"""Đếm nhãn review → bảng x/N (%) để dán vào evidence/data-mining.md. Chỉ dùng thư viện chuẩn.

Chạy:  python evidence/reviews/count_labels.py                       # đọc raw-reviews.csv
       python evidence/reviews/count_labels.py duong/dan/file.csv     # file đã gắn nhãn (vd tải từ Google Sheets)
       python evidence/reviews/count_labels.py --export               # ghi thêm labels.csv (KHÔNG có text) để commit

Mẫu số N = mọi review đã gắn nhãn (kể cả khen_trung_tinh, khong_ro). Dòng chưa có nhãn bị bỏ và được báo số lượng.
Nhãn / cờ hợp lệ: evidence/reviews/LABELS.md.
"""
import csv
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))

LABELS = ["goi_dang_ky_an", "tu_tru_khong_ro", "phi_khong_ro", "giao_dich_loi", "cashback_khuyen_mai", "tra_sau_tin_dung",
          "lua_dao_chan_gd", "ky_thuat_ekyc", "cskh", "khac_tieu_cuc", "khen_trung_tinh", "khong_ro"]
FLAGS = ["khong_biet_ai_tru", "do_loi_nham_vi", "bi_tru_nhieu_ky", "quen_huy", "nguon_tra_sau",
         "da_lien_he_khong_xong", "neu_so_tien"]
EXPORT_COLS = ["id", "review_id", "app", "date", "score", "label", "flags", "nguoi_gan", "label_2"]


def pct(x, n):
    return "%d/%d (%.1f%%)" % (x, n, 100.0 * x / n) if n else "0/0"


def table(title, rows, groups):
    """rows: list dòng đã gắn nhãn; groups: {tên cột: hàm lọc}."""
    ns = {g: [r for r in rows if f(r)] for g, f in groups.items()}
    print("\n### %s\n" % title)
    print("| Nhãn | " + " | ".join("%s (N=%d)" % (g, len(v)) for g, v in ns.items()) + " |")
    print("|---|" + "---|" * len(ns))
    for lab in LABELS:
        print("| `%s` | " % lab + " | ".join(pct(sum(1 for r in v if r["label"] == lab), len(v))
                                         for v in ns.values()) + " |")
    for fl in FLAGS:
        print("| cờ `%s` | " % fl + " | ".join(pct(sum(1 for r in v if fl in r["_flags"]), len(v))
                                             for v in ns.values()) + " |")


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    path = args[0] if args else os.path.join(HERE, "raw-reviews.csv")
    with open(path, encoding="utf-8-sig", newline="") as f:
        allrows = list(csv.DictReader(f))

    bad, rows = [], []
    for r in allrows:
        r["label"] = (r.get("label") or "").strip()
        r["_flags"] = {x.strip() for x in (r.get("flags") or "").split(";") if x.strip()}
        if not r["label"]:
            continue
        if r["label"] not in LABELS or r["_flags"] - set(FLAGS):
            bad.append(r["id"])
        rows.append(r)
    print("File: %s · %d dòng · đã gắn nhãn %d · chưa gắn %d" % (
        os.path.relpath(path), len(allrows), len(rows), len(allrows) - len(rows)))
    if bad:
        print("⚠ %d dòng có nhãn / cờ không nằm trong LABELS.md: %s" % (len(bad), ", ".join(bad[:20])))
    if not rows:
        return 1

    apps = sorted({r["app"] for r in rows})
    groups = {"tất cả": lambda r: True}
    groups.update({a: (lambda r, a=a: r["app"] == a) for a in apps})
    table("Theo app", rows, groups)
    if len({r["score"] for r in rows}) > 1:
        table("Theo số sao (tất cả app)", rows, {
            "1–2 sao": lambda r: r["score"] in ("1", "2"),
            "3 sao": lambda r: r["score"] == "3",
            "4–5 sao": lambda r: r["score"] in ("4", "5")})

    # "Có vấn đề về tiền": nhóm nhãn gộp, dùng cho mẫu số phụ khi so các hướng
    money = {"goi_dang_ky_an", "tu_tru_khong_ro", "phi_khong_ro", "giao_dich_loi", "cashback_khuyen_mai", "tra_sau_tin_dung"}
    neg = [r for r in rows if r["label"] not in ("khen_trung_tinh", "khong_ro")]
    print("\nReview có phàn nàn: %s · trong đó về tiền bị trừ / phí: %s" % (
        pct(len(neg), len(rows)), pct(sum(1 for r in neg if r["label"] in money), len(neg))))

    # Hướng "khoản trừ tự động": số hẹp / rộng (LABELS.md mục "Báo số")
    narrow = sum(1 for r in rows if r["label"] == "goi_dang_ky_an")
    broad = narrow + sum(1 for r in rows if r["label"] == "tu_tru_khong_ro")
    print("Khoản trừ tự động — hẹp (goi_dang_ky_an): %s · rộng (+ tu_tru_khong_ro): %s" % (
        pct(narrow, len(rows)), pct(broad, len(rows))))

    # Độ khớp giữa hai người gắn (nếu có label_2)
    pair = [r for r in rows if (r.get("label_2") or "").strip()]
    if pair:
        agree = sum(1 for r in pair if r["label_2"].strip() == r["label"])
        print("Độ khớp 2 người gắn: %s" % pct(agree, len(pair)))
        off = Counter((r["label"], r["label_2"].strip()) for r in pair if r["label_2"].strip() != r["label"])
        for (a, b), c in off.most_common(5):
            print("   lệch %s ↔ %s: %d" % (a, b, c))

    if "--export" in sys.argv:
        out = os.path.join(HERE, "labels.csv")
        with open(out, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=EXPORT_COLS, extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
        print("→ %s (không có text review — commit được; chạy lại: count_labels.py %s)" % (
            os.path.relpath(out), os.path.relpath(out)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
