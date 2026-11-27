"""Cào review MỚI NHẤT trên Google Play của các ví — KHÔNG lọc keyword, KHÔNG lọc số sao.

Cách chọn mẫu (ghi trước khi đọc, guide 1.2):
    N review mới nhất mỗi app, Google Play Việt Nam (lang=vi, country=vn), mọi mức sao,
    sắp theo "mới nhất" tại thời điểm chạy. Ngày chạy + khoảng ngày của mẫu ghi vào file meta.

Cài:   python -m pip install google-play-scraper
Chạy:  python evidence/reviews/scrape_reviews.py              # mặc định 200 review / app
       python evidence/reviews/scrape_reviews.py --n 300
       python evidence/reviews/scrape_reviews.py --n 500 --scores 1 --out raw-reviews-1star.csv      # mẫu chính: 500 review 1★ / app

Ra:
    evidence/reviews/raw-reviews.csv        full text để gắn nhãn — KHÔNG commit (.gitignore: evidence/**/raw-*)
    evidence/reviews/reviews-meta.json      tham số + ngày chạy + khoảng ngày — commit được

Luật dữ liệu (01-challenge-brief): không lưu tên người viết, ảnh đại diện. Trích lên repo tối đa 2 câu / review.
Chạy lại vào ngày khác sẽ ra tập khác (review mới đổ vào) → giữ nguyên raw-reviews.csv của lần chạy dùng để đếm.
"""
import argparse
import csv
import json
import os
import time
from datetime import datetime

from google_play_scraper import Sort, reviews

HERE = os.path.dirname(os.path.abspath(__file__))

APPS = {
    "momo": "com.mservice.momotransfer",
    "zalopay": "vn.com.vng.zalopay",
}

# Cột để nhóm gắn nhãn (định nghĩa nhãn: evidence/reviews/LABELS.md)
LABEL_COLS = ["label", "flags", "nguoi_gan", "label_2", "ghi_chu"]


def fetch(app_id: str, n: int, score=None) -> list:
    out, token = [], None
    while len(out) < n:
        batch, token = reviews(app_id, lang="vi", country="vn", sort=Sort.NEWEST, filter_score_with=score,
                               count=min(200, n - len(out)), continuation_token=token)
        if not batch:
            break
        out.extend(batch)
        if token is None or token.token is None:
            break
        time.sleep(1)
    return out[:n]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=200, help="số review mới nhất mỗi app (mặc định 200)")
    ap.add_argument("--apps", default=",".join(APPS), help="danh sách app, cách nhau bằng dấu phẩy")
    ap.add_argument("--scores", default="", help="chỉ lấy các mức sao này, vd 1,2,3 — N / app chia đều cho các mức sao. "
                                                 "Bỏ trống = mọi mức sao. Lọc sao thì phải ghi rõ khi báo số")
    ap.add_argument("--out", default="raw-reviews.csv", help="tên file ra (nên bắt đầu bằng raw-)")
    args = ap.parse_args()
    scores = [int(x) for x in args.scores.split(",") if x.strip()] or [None]
    k = len(scores)
    n_each = [args.n // k + (1 if i < args.n % k else 0) for i in range(k)]   # vd 500 / 3 → 167, 167, 166

    rows, meta = [], {"run_at": datetime.now().isoformat(timespec="seconds"),
                      "method": "N review mới nhất / app, Google Play VN (lang=vi, country=vn), "
                                + ("mọi mức sao" if scores == [None] else "chỉ %s sao, N / app chia đều cho các mức sao" % args.scores)
                                + ", không lọc keyword",
                      "n_per_app": args.n, "scores": args.scores or "tất cả", "apps": {}}
    for key in args.apps.split(","):
        key = key.strip()
        app_id = APPS[key]
        got = [r for sc, m in zip(scores, n_each) for r in fetch(app_id, m, sc)]
        got.sort(key=lambda r: r["at"], reverse=True)
        dates = [r["at"] for r in got]
        meta["apps"][key] = {
            "app_id": app_id, "n": len(got),
            "from": min(dates).isoformat() if dates else None,
            "to": max(dates).isoformat() if dates else None,
            "by_score": {s: sum(1 for r in got if r["score"] == s) for s in range(1, 6)},
        }
        for i, r in enumerate(got, 1):
            rows.append({
                "id": "%s-%03d" % (key, i),          # mã ngắn để trích dẫn trong evidence/
                "review_id": r["reviewId"],          # để truy lại, không phải thông tin cá nhân
                "app": key,
                "date": r["at"].strftime("%Y-%m-%d"),
                "score": r["score"],
                "app_version": r.get("reviewCreatedVersion") or "",
                "thumbs_up": r.get("thumbsUpCount", 0),
                "text": (r.get("content") or "").replace("\r", " ").replace("\n", " ").strip(),
                **{c: "" for c in LABEL_COLS},
            })
        print("%-8s %d review · %s → %s · sao 1–5: %s" % (
            key, len(got), meta["apps"][key]["from"], meta["apps"][key]["to"],
            meta["apps"][key]["by_score"]))

    raw = os.path.join(HERE, args.out)
    with open(raw, "w", newline="", encoding="utf-8-sig") as f:   # utf-8-sig: Excel mở đúng tiếng Việt
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    meta_path = os.path.join(HERE, args.out.replace("raw-", "").replace(".csv", "") + "-meta.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    print("→ %s (%d dòng, KHÔNG commit) · %s" % (os.path.relpath(raw), len(rows), os.path.relpath(meta_path)))


if __name__ == "__main__":
    main()
