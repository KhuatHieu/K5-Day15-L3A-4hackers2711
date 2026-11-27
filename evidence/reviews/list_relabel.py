"""Xuất danh sách id cần gắn nhãn lại sau khi sửa LABELS.md (27/11 ~11:30). Chỉ dùng thư viện chuẩn.

Chạy:  python evidence/reviews/list_relabel.py [file_da_gan_nhan.csv]
Ra:    evidence/reviews/relabel-ids.csv  — id, nhãn cũ, cờ cũ, lý do (không có text review → commit được)

Regex ở đây CHỈ để chọn dòng cần xem lại, KHÔNG dùng để đếm hay gắn nhãn.
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

AUTO = re.compile(r"t[ựu] (động |ý |nhiên )?(trừ|thanh toán|thành toán|thánh toán|gd|nạp|lấy|chuyển|rút|liếm|đớp)"
                  r"|tự (cài|liên kết|gia hạn)|thanh toán tự động|tự động thanh toán", re.I)
UNKNOWN = re.compile(r"(không|ko|k|chưa|chẳng) (mua|đăng k[ýí]|dùng|sử dụng|xài)|dịch vụ (gì|nào)|ứng dụng nào"
                     r"|không rõ (lý do|nguyên nhân)|không biết", re.I)
CANCEL = re.compile(r"quên|h[ủu]y|huỷ|gia hạn|dùng thử|miễn phí", re.I)
TWICE = re.compile(r"2 lần|hai lần|2 giao dịch|trừ lại|lại trừ|đã (hủy|huỷ|từ chối)", re.I)

# Nhãn mà định nghĩa / luật ưu tiên thay đổi → xem lại toàn bộ
WHOLE = {
    "goi_dang_ky_an": "siết định nghĩa: phải nêu gói / dịch vụ / nơi bán",
    "khac_tieu_cuc": "không còn dùng cho chuyện bị trừ tiền",
    "khen_trung_tinh": "lạc đề / câu hỏi cách dùng chuyển sang khong_ro",
    "tra_sau_tin_dung": "luật ưu tiên 2 và 4 (gói qua ví trả sau)",
    "lua_dao_chan_gd": "luật ưu tiên 3 (chỉ khi nói rõ lừa đảo / hack)",
    "cskh": "luật ưu tiên 5 (vấn đề tiền + CSKH)",
}


def main() -> int:
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "raw-reviews-1star.csv")
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    out = []
    for r in rows:
        t, why = r["text"], []
        if r["label"] in WHOLE:
            why.append("nhãn %s: %s" % (r["label"], WHOLE[r["label"]]))
        if AUTO.search(t):
            why.append("có chữ 'tự trừ / tự thanh toán' → xét goi_dang_ky_an / tu_tru_khong_ro / luật ưu tiên")
        if TWICE.search(t):
            why.append("có dấu hiệu trừ 2 lần / đã huỷ vẫn trừ → luật ưu tiên 1")
        if UNKNOWN.search(t) and "khong_biet_ai_tru" not in r["flags"]:
            why.append("có thể thiếu cờ khong_biet_ai_tru")
        if CANCEL.search(t):
            why.append("xét cờ mới quen_huy")
        if why:
            out.append({"id": r["id"], "nhan_cu": r["label"], "co_cu": r["flags"], "ly_do": " · ".join(why)})
    dst = os.path.join(HERE, "relabel-ids.csv")
    with open(dst, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=["id", "nhan_cu", "co_cu", "ly_do"])
        w.writeheader()
        w.writerows(out)
    print("%d/%d dòng cần gắn lại → %s" % (len(out), len(rows), os.path.relpath(dst)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
