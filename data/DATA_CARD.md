# Data card — dữ liệu bản chạy thử dùng

> Bản đầu (CP2). Một trang, mỗi dataset một mục. Không có dữ liệu cá nhân thật, không có giao dịch thật của ai, kể cả của thành viên nhóm.

## Dataset 1 · Lịch sử giao dịch ví giả lập — `data/transactions.csv`

| | |
|---|---|
| Dùng để làm gì | Nguồn cho công cụ `get_transactions` và `detect_recurring` (`codebase/tools.py`). Là nền cho bộ câu thử: mỗi câu trỏ tới một người dùng `U01`…`U10`. |
| Từ đâu | **Sinh có seed:** `python data/gen_transactions.py`, `SEED = 2711`. Chạy lại ra đúng file cũ (đã kiểm md5 hai lần chạy giống nhau). |
| Xử lý những bước gì | Không có bước làm sạch (data tự dựng). "Hôm nay" trong mô phỏng là `2026-11-27`. Cửa sổ dữ liệu: 28/05 → 27/11/2026 (6 tháng). Riêng `U10` là người dùng mới, chỉ có dữ liệu từ 19/11. |
| Số dòng | 2.551 giao dịch · 10 người dùng (khoảng 260–300 giao dịch / người, riêng U10 có 18) |
| Cột | `tx_id`, `user_id`, `time`, `description` (mô tả như trên sao kê, cố ý lộn xộn), `amount_vnd` (số tiền chi, VND), `source` (`vi` / `tra_sau`), `status` |
| Phiên bản / ngày lấy | v1 · 27/11/2026 |
| Nhãn | **`synthetic`** |
| Giới hạn | Chỉ có giao dịch **chi**, chưa có nạp tiền vào ví hay hoàn tiền; `status` toàn `thanh_cong`. Nhiễu chi tiêu hằng ngày rải đều, không có mùa vụ. Số tiền gói đăng ký là **tự ước tính** theo giá phổ biến, không lấy từ bảng giá chính thức. Mỗi kiểu khó chỉ có 1–2 người dùng → bộ câu thử nhỏ. |

**Cách dựng** (chi tiết trong docstring của script):
- **Nhiễu:** 0–3 giao dịch mỗi ngày từ 10 nơi bán **tên dựng**. Mỗi nơi bán có 2–3 kiểu mô tả khác nhau, ví dụ `XEMAU*BIKE` · `xe mau` · `XE MAU HN 2211`. Có thêm chuyển khoản không rõ nội dung và nạp điện thoại.
- **Chuỗi trừ định kỳ và ca khó:** cài theo kịch bản, mô phỏng đúng các kiểu đã thấy trong review 1★ (`evidence/data-mining.md`):

| User | Kịch bản | Lấy ý từ review |
|---|---|---|
| U01 | Dùng thử 7 ngày, chuyển sang trả phí 29/10, **kỳ 2 trừ 29/11** (ca chính của lát cắt) + Spotify ghi 3 kiểu mô tả | `zalopay-340`, `momo-019` |
| U02 | Hai chuỗi cùng mô tả `APPLE.COM/BILL`, khác số tiền, không ghi tên gói | `momo-498` |
| U03 | Netflix ghi 3 kiểu mô tả · YouTube Premium **đổi giá** 79k → 89k | — |
| U04 | Đăng ký dùng thử từ tháng 5 (trước cửa sổ dữ liệu), bị trừ **gói năm 758.889đ** ngày 16/11 | `zalopay-089` |
| U05 | **Trừ 2 lần** cùng một lần nạp, cách nhau 40 giây. Đây là giao dịch lỗi, **không** phải gói định kỳ | nhãn `giao_dich_loi` |
| U06 | Gói **tuần** trong game, mỗi lần 22k | `bi_tru_nhieu_ky` |
| U07 | `PAYPAL *XKLDIGI` và `TT DV GTGT 9x29`: mô tả **không đoán được**, AI phải nói "không rõ" | `khong_biet_ai_tru` |
| U08 | ChatGPT trả bằng USD nên số VND **dao động** · **tiền điện** định kỳ, thiết yếu, không được gợi ý huỷ | — |
| U09 | Gói truyện trừ từ **ví trả sau** | `nguon_tra_sau` |
| U10 | Người dùng mới, 1 lần trừ, **chưa đủ dữ liệu** để nói là định kỳ | — |

- **Tên:** nền tảng (Google Play, App Store, Spotify, YouTube, Netflix, ChatGPT / OpenAI, PayPal) giữ tên thật, vì hướng dẫn huỷ phải trỏ về trang chính thức của họ. App bán qua nền tảng và mọi nơi bán khác là **tên dựng**.

## Dataset 2 · Đáp án chuỗi định kỳ — `data/recurring_truth.csv`

| | |
|---|---|
| Dùng để làm gì | **Đáp án** để chấm bộ câu thử và kiểm `detect_recurring`: dịch vụ nào, nền tảng nào, loại khoản (`goi_dang_ky` · `dung_thu_chuyen_tra_phi` · `hoa_don_thiet_yeu` · `khong_ro` · `giao_dich_loi`), chu kỳ, lần trừ cuối, ngày trừ kế tiếp, nguồn tiền, danh sách `tx_ids`. |
| Từ đâu | Cùng script, cùng seed |
| Số dòng | 15 chuỗi |
| Nhãn | **`synthetic`** |
| Giới hạn | **Bản chạy thử không được đọc file này**, vì đọc vào là lộ đáp án. Chỉ bộ chấm và người viết câu thử dùng. Ô `next_date` để trống khi data không đủ căn cứ (U02-S2, U05, U10), và khi đó đáp án đúng là nói "chưa xác định được". |

## Dataset 3 · Hướng dẫn huỷ gói theo nền tảng *(chưa làm, việc X6 của Nghĩa)*

Nguồn cho công cụ `lookup_cancel_guide`. Mỗi dòng gồm: nền tảng · các bước · **link trang trợ giúp chính thức** · ngày xem. Không có link chính thức thì không đưa vào.

---

**Người kiểm:** __ (đọc tay 10 chuỗi trong `recurring_truth.csv` và đối chiếu từng chuỗi với `transactions.csv`; ghi số chuỗi đã kiểm). Data tự dựng **không phải bằng chứng pain**: bằng chứng ở `evidence/`.
