"""Người kiểm nhãn do AI gắn — tạo mẫu 100 dòng (ẩn nhãn AI) và ghép kết quả về. Chỉ dùng thư viện chuẩn.

Bước 1 — tạo mẫu:
    python evidence/reviews/human_check.py make
    → evidence/reviews/raw-human-check.csv   có text, KHÔNG có nhãn AI — để người gắn (KHÔNG commit)
    → evidence/reviews/human-check-ids.csv   id + tầng lấy mẫu, không text — commit được

Bước 2 — người gắn cột label_2 (và flags_2 nếu muốn) trong raw-human-check.csv theo LABELS.md,
    KHÔNG mở labels.csv / raw-reviews-1star.csv khi đang gắn.

Bước 3 — ghép về:
    python evidence/reviews/human_check.py merge
    → điền label_2 vào evidence/reviews/labels.csv, rồi:
    python evidence/reviews/count_labels.py evidence/reviews/labels.csv   # in độ khớp

Cách lấy mẫu (phân tầng, seed cố định): TẤT CẢ dòng AI gắn goi_dang_ky_an + 30 dòng ngẫu nhiên
tu_tru_khong_ro + phần còn lại ngẫu nhiên từ các nhãn khác, đủ 100 dòng, xáo thứ tự.
Vì lấy dư hai nhãn chính, độ khớp chung KHÔNG đại diện cho cả 1000 dòng → báo độ khớp theo từng tầng.
"""
import csv
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 2711
N = 100
N_TU_TRU = 30
RAW = os.path.join(HERE, "raw-reviews-1star.csv")
LABELS = os.path.join(HERE, "labels.csv")
SHEET = os.path.join(HERE, "raw-human-check.csv")
IDS = os.path.join(HERE, "human-check-ids.csv")


def read(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write(path, rows, cols):
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def make():
    text = {r["id"]: r for r in read(RAW)}
    lab = read(LABELS)
    rnd = random.Random(SEED)
    goi = [r for r in lab if r["label"] == "goi_dang_ky_an"]
    tu = [r for r in lab if r["label"] == "tu_tru_khong_ro"]
    rest = [r for r in lab if r["label"] not in ("goi_dang_ky_an", "tu_tru_khong_ro")]
    pick = ([dict(r, tang="goi_dang_ky_an (tất cả)") for r in goi]
            + [dict(r, tang="tu_tru_khong_ro (ngẫu nhiên)") for r in rnd.sample(tu, min(N_TU_TRU, len(tu)))])
    pick += [dict(r, tang="nhãn khác (ngẫu nhiên)") for r in rnd.sample(rest, N - len(pick))]
    rnd.shuffle(pick)
    sheet = [{"stt": i, "id": r["id"], "app": r["app"], "text": text[r["id"]]["text"],
              "label_2": "", "flags_2": "", "nguoi_gan_2": "", "ghi_chu": ""} for i, r in enumerate(pick, 1)]
    write(SHEET, sheet, ["stt", "id", "app", "text", "label_2", "flags_2", "nguoi_gan_2", "ghi_chu"])
    write(IDS, pick, ["id", "tang"])
    print("%d dòng (goi_dang_ky_an %d · tu_tru_khong_ro %d · khác %d), seed %d" % (
        len(pick), len(goi), min(N_TU_TRU, len(tu)), N - len(goi) - min(N_TU_TRU, len(tu)), SEED))
    print("→ %s (để người gắn, KHÔNG commit) · %s (commit)" % (os.path.relpath(SHEET), os.path.relpath(IDS)))


def merge():
    done = {r["id"]: r for r in read(SHEET) if r["label_2"].strip()}
    tang = {r["id"]: r["tang"] for r in read(IDS)}
    lab = read(LABELS)
    cols = list(lab[0].keys())
    for c in ("flags_2", "nguoi_gan_2"):
        if c not in cols:
            cols.append(c)
    for r in lab:
        h = done.get(r["id"])
        if h:
            r["label_2"], r["flags_2"], r["nguoi_gan_2"] = h["label_2"].strip(), h["flags_2"].strip(), h["nguoi_gan_2"].strip()
    write(LABELS, lab, cols)
    print("Ghép %d/%d dòng đã gắn vào %s" % (len(done), len(tang), os.path.relpath(LABELS)))
    # độ khớp theo tầng
    by = {}
    for r in lab:
        if r["id"] in done:
            t = tang.get(r["id"], "?")
            a, n = by.get(t, (0, 0))
            by[t] = (a + (r["label"] == r["label_2"]), n + 1)
    for t, (a, n) in sorted(by.items()):
        print("   %-30s khớp %d/%d (%.0f%%)" % (t, a, n, 100.0 * a / n))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "make":
        make()
    elif cmd == "merge":
        merge()
    else:
        print(__doc__)
