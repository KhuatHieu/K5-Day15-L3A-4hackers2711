"""Sinh lịch sử giao dịch ví GIẢ LẬP (synthetic) cho bản chạy thử. Chỉ dùng thư viện chuẩn.

Chạy:  python data/gen_transactions.py
  → data/transactions.csv       200 giao dịch: 150 tình huống + 50 nhiễu, 11 người dùng giả
  → data/recurring_truth.csv    ĐÁP ÁN: các chuỗi trừ định kỳ / ca đặc biệt cài vào mỗi người dùng

Seed cố định (SEED) → chạy lại ra đúng hai file cũ. KHÔNG có giao dịch thật của ai.
"Hôm nay" trong mô phỏng: TODAY = 2026-11-27. Mô tả: data/DATA_CARD.md.
Nguồn gợi ý tình huống từ nội dung review được ghi trong data/DATA_CARD.md.
Thêm --output-dir để sinh vào thư mục khác; --max-rows mặc định 200 (không tính tiêu đề).
Giữ toàn bộ giao dịch kịch bản; chỉ lấy mẫu giao dịch nhiễu. Không sao chép text hay thông tin người viết review.

Cách dựng:
  - Chi tiêu hằng ngày (nhiễu): nơi bán tên DỰNG, mỗi nơi ghi vài kiểu lộn xộn như ngoài đời
    (vd `XEMAU*BIKE`, `xe mau`, `XE MAU HN 2211`), chuyển khoản không rõ nội dung, nạp điện thoại.
  - Chuỗi trừ định kỳ (cài theo kịch bản, mỗi chuỗi có 1 dòng đáp án): mô phỏng đúng các kiểu
    thấy trong review 1★ (evidence/data-mining.md): dùng thử chuyển trả phí, gia hạn năm sau 6 tháng,
    mô tả `APPLE.COM/BILL` không nói gói nào, cùng dịch vụ nhiều kiểu mô tả, giá đổi giữa chừng,
    số tiền dao động theo tỉ giá, trừ từ ví trả sau, trừ 2 lần (giao dịch lỗi — KHÔNG phải định kỳ),
    hoá đơn định kỳ thiết yếu (không được gợi ý huỷ), mô tả không đoán được (phải nói "không rõ").
  - Tên nền tảng (Google Play, App Store, Spotify, YouTube, Netflix, ChatGPT) giữ tên thật vì hướng dẫn huỷ
    trỏ về trang chính thức của họ; tên app con bán qua nền tảng và mọi nơi bán khác là tên DỰNG.
"""
import argparse
import csv
import os
import random
from datetime import date, datetime, timedelta

SEED = 2711
TODAY = date(2026, 11, 27)
START = date(2026, 5, 28)
HERE = os.path.dirname(os.path.abspath(__file__))

# Nơi bán DỰNG cho chi tiêu hằng ngày: (nhóm chi, [các kiểu mô tả], (min, max) nghìn đồng)
NOISE = [
    ("an_uong", ["CF NGAN HA", "CAFE NGAN HA 12", "ngan ha coffee"], (25, 65)),
    ("an_uong", ["BUN CHA 34 HANG", "buncha34", "BUN CHA 34"], (35, 70)),
    ("an_uong", ["COM TAM SAO MAI", "comtam saomai q3"], (40, 75)),
    ("an_uong", ["TRA SUA MIMI", "MIMI TEA*HN", "tra sua mimi 2"], (30, 60)),
    ("di_lai", ["XEMAU*BIKE", "xe mau", "XE MAU HN 2211"], (15, 80)),
    ("di_lai", ["XEMAU*CAR", "XE MAU CAR 0921"], (60, 220)),
    ("mua_sam", ["MINIMART 24H", "MINI MART 24H CN5", "minimart24"], (20, 250)),
    ("mua_sam", ["SAN TMDT DUNG*ORDER", "SANTMDT ORDER 88213"], (90, 650)),
    ("dien_thoai", ["NAP DT 09xx***", "NAP TIEN DIEN THOAI"], (50, 100)),
    ("chuyen_khoan", ["CK DEN TK ****{n}", "CK DEN TK ****{n} ND: ck", "CHUYEN TIEN"], (100, 1500)),
]

# Kịch bản mỗi người dùng. Mỗi chuỗi: (series_id, mô tả hoặc [các kiểu mô tả], danh sách (ngày, số tiền),
#   service, platform, kind, cycle_days, next_date, ghi chú, nguồn tiền)
# kind: goi_dang_ky · dung_thu_chuyen_tra_phi · hoa_don_thiet_yeu · khong_ro · giao_dich_loi
def d(s):
    return date.fromisoformat(s)


def monthly(first, n, amount):
    """n lần trừ cùng ngày mỗi tháng (ngày ≤ 28)."""
    out, cur = [], d(first)
    for _ in range(n):
        out.append((cur, amount))
        cur = date(cur.year + (cur.month == 12), cur.month % 12 + 1, cur.day)
    return out


def every(first, step, until, amount):
    out, cur = [], d(first)
    while cur <= until:
        out.append((cur, amount))
        cur += timedelta(days=step)
    return out


SCENARIOS = {
    # U01 · sinh viên: dùng thử 7 ngày app báo thức (tên dựng) qua Google Play → vừa bị trừ kỳ đầu 29/10,
    # kỳ 2 sẽ trừ 29/11 (2 ngày nữa) — ca chính của lát cắt. Có thêm Spotify gói sinh viên đã trừ đều.
    "U01": {"persona": "sinh_vien", "series": [
        ("U01-S1", "GOOGLE *BaoThuc Pro", [(d("2026-10-22"), 0), (d("2026-10-29"), 179000)],
         "BaoThuc Pro (app báo thức, tên dựng)", "Google Play", "dung_thu_chuyen_tra_phi", 30, "2026-11-29",
         "dùng thử 0đ 22/10 → trả phí 29/10; mới 1 lần trả phí", "vi"),
        ("U01-S2", ["SPOTIFY P3B1C9", "Spotify AB", "SPOTIFY*STUDENT"], monthly("2026-06-12", 6, 29500),
         "Spotify Premium Student", "Spotify", "goi_dang_ky", 30, "2026-12-12", "mô tả đổi kiểu mỗi tháng", "vi"),
    ]},
    # U02 · nhân viên văn phòng: hai chuỗi cùng mô tả APPLE.COM/BILL, khác số tiền — không đoán được gói nào
    "U02": {"persona": "nhan_vien_vp", "series": [
        ("U02-S1", "APPLE.COM/BILL", monthly("2026-06-05", 6, 45000),
         "Apple — chưa rõ gói (mô tả không ghi tên gói)", "App Store", "goi_dang_ky", 30, "2026-12-05",
         "đã trừ 6 tháng; chỉ biết là Apple", "vi"),
        ("U02-S2", "APPLE.COM/BILL", [(d("2026-11-18"), 99000)],
         "Apple — chưa rõ gói (mô tả không ghi tên gói)", "App Store", "goi_dang_ky", None, "",
         "khoản Apple MỚI, khác số tiền chuỗi S1; 1 lần, chưa rõ chu kỳ", "vi"),
    ]},
    # U03 · Netflix qua thẻ liên kết + YouTube Premium đổi giá từ tháng 10
    "U03": {"persona": "nhan_vien_vp", "series": [
        ("U03-S1", ["NETFLIX.COM", "NETFLIX.COM SG", "Netflix Intl"], monthly("2026-06-20", 6, 260000),
         "Netflix", "Netflix", "goi_dang_ky", 30, "2026-12-20", "", "vi"),
        ("U03-S2", "GOOGLE *YouTubePremium",
         [(x, 79000) for x, _ in monthly("2026-06-08", 4, 0)] + [(x, 89000) for x, _ in monthly("2026-10-08", 2, 0)],
         "YouTube Premium", "Google Play", "goi_dang_ky", 30, "2026-12-08", "giá đổi 79k → 89k từ 08/10", "vi"),
    ]},
    # U04 · giống review zalopay-089: đăng ký dùng thử 19/05… (ngoài cửa sổ), bị trừ GÓI NĂM 16/11
    "U04": {"persona": "nhan_vien_vp", "series": [
        ("U04-S1", "GOOGLE *PhotoEdit Studio", [(d("2026-11-16"), 758889)],
         "PhotoEdit Studio (app sửa ảnh, tên dựng) — gói năm", "Google Play", "dung_thu_chuyen_tra_phi", 365,
         "2027-11-16", "dùng thử từ 19/05 (trước cửa sổ dữ liệu); chỉ 1 lần trả phí → chu kỳ KHÔNG suy ra được từ data",
         "vi"),
    ]},
    # U05 · trừ 2 lần cùng một giao dịch nạp tiền — giao dịch lỗi, KHÔNG phải định kỳ
    "U05": {"persona": "sinh_vien", "series": [
        ("U05-S1", "NAP TIEN DIEN THOAI", [(d("2026-11-20"), 100000), (d("2026-11-20"), 100000)],
         "Nạp tiền điện thoại — trừ 2 lần", "", "giao_dich_loi", None, "",
         "2 giao dịch cách nhau 40 giây; không phải gói định kỳ → hướng dẫn tra soát với ví", "vi"),
    ]},
    # U06 · gói tuần trong game (tên dựng) qua Google Play
    "U06": {"persona": "sinh_vien", "series": [
        ("U06-S1", "GOOGLE *Kingdom Clash", every("2026-10-02", 7, TODAY, 22000),
         "Kingdom Clash (game, tên dựng) — gói tuần", "Google Play", "goi_dang_ky", 7, "",
         "trừ mỗi 7 ngày; next_date tính bằng code từ lần cuối", "vi"),
    ]},
    # U07 · mô tả không đoán được dịch vụ → phải nói "không rõ"
    "U07": {"persona": "nhan_vien_vp", "series": [
        ("U07-S1", "PAYPAL *XKLDIGI", monthly("2026-08-14", 4, 120000),
         "không rõ", "PayPal", "khong_ro", 30, "2026-12-14", "PayPal trả cho bên thứ ba, tên không đoán được", "vi"),
        ("U07-S2", "TT DV GTGT 9x29", every("2026-10-01", 3, TODAY, 15000),
         "không rõ (dịch vụ giá trị gia tăng, có thể của nhà mạng)", "", "khong_ro", 3, "",
         "trừ mỗi 3 ngày, mô tả không rõ bên bán", "vi"),
    ]},
    # U08 · ChatGPT trả bằng USD → số VND dao động theo tỉ giá; tiền điện định kỳ (thiết yếu)
    "U08": {"persona": "lo_chi_tieu_gia_dinh", "series": [
        ("U08-S1", "OPENAI *CHATGPT SUBSCR", [(x, a) for x, a in monthly("2026-06-03", 6, 0)],
         "ChatGPT Plus", "OpenAI", "goi_dang_ky", 30, "2026-12-03", "trả USD, VND dao động 515k–540k", "vi"),
        ("U08-S2", ["EVN HN TIEN DIEN", "TIEN DIEN KY T{m}", "EVNHANOI HD"], [(x, a) for x, a in monthly("2026-06-10", 6, 0)],
         "Hoá đơn tiền điện", "", "hoa_don_thiet_yeu", 30, "2026-12-10", "định kỳ nhưng thiết yếu — KHÔNG gợi ý huỷ", "vi"),
    ]},
    # U09 · gói truyện (tên dựng) trừ từ VÍ TRẢ SAU
    "U09": {"persona": "sinh_vien", "series": [
        ("U09-S1", "GOOGLE *TruyenHay VIP", monthly("2026-08-25", 4, 49000),
         "TruyenHay VIP (app truyện, tên dựng)", "Google Play", "goi_dang_ky", 30, "2026-12-25",
         "nguồn tiền: ví trả sau", "tra_sau"),
    ]},
    # U10 · người dùng mới, chỉ có 9 ngày lịch sử, 1 khoản Google — thiếu dữ liệu để nói định kỳ
    "U10": {"persona": "sinh_vien", "start": "2026-11-19", "series": [
        ("U10-S1", "GOOGLE *Lingo Fast", [(d("2026-11-21"), 129000)],
         "Lingo Fast (app học ngoại ngữ, tên dựng)", "Google Play", "khong_ro", None, "",
         "mới 9 ngày lịch sử, 1 lần trừ → chưa đủ căn cứ nói định kỳ", "vi"),
    ]},
    # Bổ sung theo yêu cầu 150 giao dịch tình huống + 50 nhiễu.
    # Hai chuỗi độc lập để kiểm lịch dài, không thêm dữ kiện cho các ca thiếu căn cứ.
    "U11": {"persona": "kiem_thu_lich_dai", "series": [
        ("U11-S1", "GOOGLE *LuyenTriNho", every("2026-06-05", 7, TODAY, 19000),
         "LuyenTriNho (app, tên dựng) — gói tuần", "Google Play", "goi_dang_ky", 7, "",
         "ca bổ sung giả lập: 26 lần trả phí theo tuần", "vi"),
        ("U11-S2", "TT DV GTGT 4x17", every("2026-06-08", 4, TODAY, 12000),
         "không rõ", "", "khong_ro", 4, "",
         "ca bổ sung giả lập: 44 lần trừ mỗi bốn ngày, không đoán tên dịch vụ", "vi"),
    ]},
}


# Chỉ lấy ý từ nội dung review; không tái dựng lịch sử tài khoản của người viết review.
def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default=HERE, help="Thư mục nhận dữ liệu synthetic")
    parser.add_argument("--max-rows", type=int, default=200, help="Số dòng giao dịch, không tính tiêu đề (mặc định 200)")
    args = parser.parse_args(argv)
    output_dir = os.path.abspath(args.output_dir)
    os.makedirs(output_dir, exist_ok=True)
    tx_out = os.path.join(output_dir, "transactions.csv")
    truth_out = os.path.join(output_dir, "recurring_truth.csv")
    rnd = random.Random(SEED)
    tx, truth = [], []
    for uid, sc in SCENARIOS.items():
        start = d(sc.get("start", START.isoformat()))
        acct = rnd.randint(1000, 9999)
        # nhiễu: 0–3 giao dịch / ngày
        day = start
        while day <= TODAY:
            for _ in range(rnd.choice([0, 1, 1, 1, 2, 2, 3])):
                cat, names, (lo, hi) = rnd.choice(NOISE)
                desc = rnd.choice(names).replace("{n}", str(acct if rnd.random() < .5 else rnd.randint(1000, 9999)))
                amt = rnd.randint(lo, hi) * 1000
                tx.append([uid, datetime.combine(day, datetime.min.time()) + timedelta(minutes=rnd.randint(390, 1380)),
                           desc, amt, "vi", "thanh_cong", None])
            day += timedelta(days=1)
        # chuỗi định kỳ / ca đặc biệt
        for sid, desc, charges, service, platform, kind, cycle, nxt, note, src in sc["series"]:
            last_t = None
            for i, (day, amt) in enumerate(charges):
                if day < start or day > TODAY:
                    continue
                if sid == "U08-S1":
                    amt = rnd.randint(515, 540) * 1000
                if sid == "U08-S2":
                    amt = rnd.randint(280, 690) * 1000 + rnd.randint(0, 999)
                text = desc[i % len(desc)] if isinstance(desc, list) else desc
                text = text.replace("{m}", str(day.month))
                t = datetime.combine(day, datetime.min.time()) + timedelta(minutes=rnd.randint(60, 300))
                if kind == "giao_dich_loi" and last_t is not None:
                    t = last_t + timedelta(seconds=40)
                last_t = t
                tx.append([uid, t, text, amt, src, "thanh_cong", sid])
            paid = [c for c in charges if start <= c[0] <= TODAY]
            if sid in {"U06-S1", "U07-S2", "U11-S1", "U11-S2"}:   # chu kỳ ngắn: lần cuối + chu kỳ
                nxt = (paid[-1][0] + timedelta(days=cycle)).isoformat()
            truth.append({"user_id": uid, "persona": sc["persona"], "series_id": sid,
                          "description_vi_du": desc if isinstance(desc, str) else " | ".join(desc),
                          "service": service, "platform": platform, "kind": kind,
                          "cycle_days": cycle or "", "so_lan_trong_data": len(paid),
                          "last_date": paid[-1][0].isoformat(), "next_date": nxt, "nguon_tien": src, "ghi_chu": note})
    # Không cắt mất tình huống kiểm thử. Lấy mẫu nhiễu riêng để lịch và số tiền kịch bản
    # không phụ thuộc giới hạn số dòng. Mỗi người có tối thiểu hai dòng nhiễu nếu đủ chỗ.
    scenario_tx = [row for row in tx if row[6] is not None]
    noise_tx = [row for row in tx if row[6] is None]
    if not len(scenario_tx) <= args.max_rows <= len(tx):
        parser.error("--max-rows phải từ %d đến %d để giữ đủ các tình huống." % (len(scenario_tx), len(tx)))
    sample_rng = random.Random(SEED + 1)
    noise_budget = args.max_rows - len(scenario_tx)
    selected = []
    if noise_budget >= 2 * len(SCENARIOS):
        for uid in SCENARIOS:
            selected.extend(sample_rng.sample([row for row in noise_tx if row[0] == uid], 2))
    selected_ids = {id(row) for row in selected}
    selected.extend(sample_rng.sample([row for row in noise_tx if id(row) not in selected_ids],
                                      noise_budget - len(selected)))
    tx = scenario_tx + selected
    tx.sort(key=lambda r: (r[0], r[1]))
    ids = {}   # series_id → [tx_id] — chỉ ghi vào file đáp án, KHÔNG ghi vào transactions.csv (công cụ không được thấy)
    with open(tx_out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["tx_id", "user_id", "time", "description", "amount_vnd", "source", "status"])
        for i, r in enumerate(tx, 1):
            w.writerow(["T%05d" % i, r[0], r[1].strftime("%Y-%m-%d %H:%M:%S")] + r[2:6])
            if r[6]:
                ids.setdefault(r[6], []).append("T%05d" % i)
    for t in truth:
        t["tx_ids"] = " ".join(ids.get(t["series_id"], []))
    with open(truth_out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(truth[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(truth)
    print("%d giao dịch · %d người dùng · %d chuỗi đáp án · seed %d" % (len(tx), len(SCENARIOS), len(truth), SEED))
    print("→ %s · %s" % (tx_out, truth_out))


if __name__ == "__main__":
    main()
