# Đào data — cách đếm và kết quả

> Nguồn: review công khai của ví MoMo và ZaloPay trên Google Play. Script, nhãn, cách chọn mẫu ở `evidence/reviews/`.
> Repo chỉ chứa số đã tổng hợp, nhãn **không có text** (`evidence/reviews/labels.csv`) và trích dẫn ≤2 câu. Full text review **không commit** (luật dữ liệu: trích tối đa 2 câu / review).
> Nhãn do AI gắn; **người đã kiểm 100 dòng** (27/11 tối) — độ khớp theo tầng và giới hạn của cách kiểm ở mục 3b.

## 1. Cách đếm

- **Data dùng:** 500 review **1 sao mới nhất** mỗi app, Google Play Việt Nam (`lang=vi, country=vn`), **không lọc keyword** → N = 1000. Cào 27/11/2026 11:09.
  - MoMo (`com.mservice.momotransfer`): 18/10 → 26/11/2026 · ZaloPay (`vn.com.vng.zalopay`): 14/10 → 25/11/2026 (≈ 6 tuần).
  - Tham số và số review theo sao: `evidence/reviews/reviews-1star-meta.json` · script: `evidence/reviews/scrape_reviews.py`.
- **Vì sao chỉ lấy 1 sao:** thử lấy review mới nhất mọi mức sao trước (500 / app, `reviews-meta.json`): 885/1000 là 5 sao, 755/1000 dài dưới 20 ký tự ("tốt", "ok"), 500 review chỉ phủ 2–8 ngày → mẫu số bị lời khen ngắn lấp. Mục tiêu là tìm **loại** pain → chọn 1 sao. Bối cảnh: trong 1000 review mới nhất mọi mức sao, 1 sao chiếm 79/1000.
- **Đếm gì:** mỗi review đúng 1 nhãn chính + 0..n cờ phụ, theo định nghĩa trong `evidence/reviews/LABELS.md` (12 nhãn, 7 cờ, luật ưu tiên).
- **Mẫu số:** N = 1000 = **mọi** review trong mẫu, kể cả review khen, vô nghĩa, không liên quan.
- **Ai gắn:** AI (Gemini) gắn cả 1000 dòng theo `LABELS.md` bản 27/11 ~11:30; người kiểm 100 dòng (mục 3b). Prompt: `__` *(dán vào `evidence/reviews/` và `docs/ai-usage.md`)*.
- **Chạy lại:** `python evidence/reviews/count_labels.py evidence/reviews/labels.csv` → ra đúng bảng ở mục 3.
- **Trung thực về thứ tự:** bộ nhãn viết trước khi gắn. Sau lượt gắn đầu, bộ nhãn **được sửa một lần** (thêm `tu_tru_khong_ro`, siết `goi_dang_ky_an`, thêm luật ưu tiên) vì ~65 review chỉ nói "tự trừ tiền" bị gán rải rác 8 nhãn — lý do và ví dụ ở mục "Đã sửa" của `LABELS.md`; nhãn lượt 1 còn giữ ở `evidence/reviews/relabel-ids.csv` (cột `nhan_cu`). Số dưới đây là của lượt 2.

## 2. Đọc trước, đếm sau

Đọc thử các review 1–2 sao trước khi đặt nhãn. Các kiểu hành vi thấy được:
- Bị trừ tiền **tự động** mà không nhớ đã đồng ý — có người nêu được dịch vụ (Google Play, Apple, Spotify, ChatGPT, Locket, Canva, game, "app khác"), nhiều người **không** biết khoản đó là gì.
- Giao dịch tự làm bị treo "đang xử lý", trừ tiền mà nạp / chuyển không thành công, trừ 2 lần.
- Lỗi kỹ thuật: lag, đăng nhập, xác thực khuôn mặt / NFC / eKYC.
- Phí chuyển / rút tiền; ví trả sau tự được chọn làm nguồn tiền rồi tính phí.
- Bị khoá tài khoản; lừa đảo; khuyến mãi / hoàn tiền không như quảng cáo; CSKH chậm, toàn bot.

## 3. Kết quả

### 3a. Theo nhãn (N = 1000; MoMo 500, ZaloPay 500)

| Đếm gì | Tất cả | MoMo | ZaloPay | Ghi chú |
|---|---|---|---|---|
| `ky_thuat_ekyc` | 387/1000 (38.7%) | 195/500 (39.0%) | 192/500 (38.4%) | lớn nhất, nhưng không có chuyện mất tiền |
| `giao_dich_loi` | 167/1000 (16.7%) | 114/500 (22.8%) | 53/500 (10.6%) | |
| **Khoản trừ tự động — rộng** (`goi_dang_ky_an` + `tu_tru_khong_ro`) | **147/1000 (14.7%)** | 37/500 (7.4%) | **110/500 (22.0%)** | hướng nhóm đang xét |
| ↳ **hẹp** `goi_dang_ky_an` (nêu được gói / dịch vụ) | 33/1000 (3.3%) | 11/500 (2.2%) | 22/500 (4.4%) | |
| ↳ `tu_tru_khong_ro` (không nêu được là khoản gì) | 114/1000 (11.4%) | 26/500 (5.2%) | 88/500 (17.6%) | |
| `khac_tieu_cuc` | 83/1000 (8.3%) | 42/500 (8.4%) | 41/500 (8.2%) | |
| `khong_ro` | 58/1000 (5.8%) | 24/500 (4.8%) | 34/500 (6.8%) | |
| `tra_sau_tin_dung` | 46/1000 (4.6%) | 38/500 (7.6%) | 8/500 (1.6%) | |
| `phi_khong_ro` | 36/1000 (3.6%) | 12/500 (2.4%) | 24/500 (4.8%) | |
| `lua_dao_chan_gd` | 26/1000 (2.6%) | 15/500 (3.0%) | 11/500 (2.2%) | |
| `cashback_khuyen_mai` | 24/1000 (2.4%) | 12/500 (2.4%) | 12/500 (2.4%) | |
| `cskh` | 15/1000 (1.5%) | 10/500 (2.0%) | 5/500 (1.0%) | |
| `khen_trung_tinh` | 11/1000 (1.1%) | 1/500 (0.2%) | 10/500 (2.0%) | |

**Trong 147 review "khoản trừ tự động" (rộng):**

| Cờ | x / 147 | Ý nghĩa cho bài toán |
|---|---|---|
| `khong_biet_ai_tru` | 57/147 (38.8%) | không biết khoản trừ là của dịch vụ / ai |
| `da_lien_he_khong_xong` | 26/147 (17.7%) | đã hỏi CSKH / đòi hoàn tiền nhưng không xong |
| `do_loi_nham_vi` | 22/147 (15.0%) | trách ví về khoản thực ra trả cho bên khác (Google, Apple, app) — 22/33 review hẹp |
| `bi_tru_nhieu_ky` | 10/147 (6.8%) | bị trừ nhiều lần / nhiều tháng mới phát hiện |
| `quen_huy` | 8/147 (5.4%) | nói rõ quên huỷ / không tìm được chỗ huỷ |

**Số tiền người viết tự nêu** (19 review rộng có số rõ, đọc tay từ text — id để kiểm lại): 30k (`zalopay-101`, `zalopay-398`) · 179k (`zalopay-234`) · 250k (`momo-133`) · 300k (`zalopay-280`, `zalopay-369`) · 400k (`zalopay-050`) · 450k (`momo-299`) · 500k (`zalopay-106`, `zalopay-165`) · 543k (`momo-147`) · 600k (`momo-167`, `zalopay-159`) · 759k (`zalopay-089`) · 900k (`zalopay-331`) · 1 triệu (`zalopay-197`, `zalopay-379`) · 1,09 triệu (`zalopay-340`) · 1,2 triệu (`zalopay-404`). **Trung vị 500k / review.** Không tính `zalopay-468` ("gần cả triệu", cộng dồn 2–3 lần). Giới hạn: số tự báo, có thể là cộng dồn; người mất nhiều dễ viết review hơn → số này **lệch cao**, chỉ dùng để hình dung, không dùng làm "mỗi lần tốn" trong bảng impact nếu chưa kiểm bằng khảo sát.

### 3b. Người kiểm nhãn AI *(E3 · 27/11 19:05, `python evidence/reviews/human_check.py merge`)*

Mẫu 100 dòng, seed 2711, phân tầng (`evidence/reviews/human-check-ids.csv`): **tất cả** 33 dòng `goi_dang_ky_an` + 30 dòng ngẫu nhiên `tu_tru_khong_ro` + 37 dòng ngẫu nhiên nhãn khác. Người gắn trên file chỉ có text (`raw-human-check.csv`, không có cột nhãn AI, không có cột tầng), theo `LABELS.md` bản 27/11 ~11:30. Kết quả ghép vào cột `label_2` / `flags_2` / `nguoi_gan_2` của `labels.csv`.

| Tầng | Người khớp AI |
|---|---|
| `goi_dang_ky_an` (tất cả) | 28/33 (85%) |
| `tu_tru_khong_ro` (ngẫu nhiên) | 28/30 (93%) |
| nhãn khác (ngẫu nhiên) | 31/37 (84%) |
| **Chung** *(không đại diện cả 1000 dòng vì lấy dư 2 tầng đầu)* | 87/100 (87%) |

Người gắn: 1 thành viên nhóm (cặp X, `nguoi_gan_2 = L`) · Cặp lệch nhiều nhất: `goi_dang_ky_an` ↔ `tu_tru_khong_ro` (3 dòng), `ky_thuat_ekyc` ↔ `khong_ro` (2), còn lại mỗi cặp 1 dòng (`giao_dich_loi` ↔ `khac_tieu_cuc`, `khong_ro` ↔ `khen_trung_tinh`, `ky_thuat_ekyc` ↔ `giao_dich_loi`). In bằng `python evidence/reviews/count_labels.py evidence/reviews/labels.csv`.

**Đọc số:** cặp lệch nhiều nhất chính là ranh giới hẹp / rộng của hướng "khoản trừ tự động" (review có nêu gói / dịch vụ hay không), nên số **hẹp** (33) chắc chắn kém hơn số **rộng** (147, gộp cả hai nhãn nên lệch giữa chúng không làm đổi số rộng).

**Ghi thật về cách kiểm:**
- Người gắn **đã lỡ thấy nhãn AI** ở một lần gắn thử trước đó (gắn trên file đầy đủ có cột `label`). Lần đó **bỏ**, gắn lại từ đầu trên file ẩn nhãn ở trên. Vì đã từng thấy nhãn, độ khớp có thể **cao hơn** so với một người hoàn toàn chưa xem.
- 4 dòng (`zalopay-343`, `zalopay-234`, `momo-442`, `zalopay-379`) được người gắn sửa thành `goi_dang_ky_an` sau khi đối chiếu lại định nghĩa trong `LABELS.md` (chữ "gói", "đăng ký", "app khác" đủ điều kiện) — đối chiếu với định nghĩa, **không** nhìn nhãn AI. Lý do ghi ở `ghi_chu` trong file gắn (không commit).
- Người gắn là thành viên nhóm, không phải người ngoài; chưa có người thứ ba gắn để tính độ khớp giữa hai người.

## 4. Ví dụ nguyên văn (≤2 câu, bỏ tên người viết; nguồn: Google Play, review 1 sao, cào 27/11/2026)

1. "Mình đăng ký dùng thử miễn phí Alarmy, nhưng sau khi hết hạn, thẻ ngân hàng bị trừ 1.086.667 đồng. Mình đã cố gắng hủy nhưng không tìm thấy gói thuê bao trên Google Play." — `zalopay-340`, 27/10/2026 · `goi_dang_ky_an`, cờ `quen_huy`
2. "Sau khi tôi quên hủy 1 gói thuê bao trên play thì Momo đã tự nạp tiền vào ví, tự gia hạn gói đăng ký mà không hỏi tôi 1 câu" — `momo-019`, 23/11/2026 · `goi_dang_ky_an`, cờ `do_loi_nham_vi`, `quen_huy`
3. "hệ thống trừ tiền lung tung mã google từ đâu xuất hiện trừ hơn 543k…" — `momo-147`, 12/11/2026 · `goi_dang_ky_an`, cờ `khong_biet_ai_tru`, `do_loi_nham_vi`
4. "cái đăng ký thì lôi ở đâu ra từ ngày 19/05/2026 rồi trừ tiền của mình vào 16/11/2026 hỏi thì không đc. số tiền trừ của mình bị mất là zalopay trừ 758.889đ" — `zalopay-089`, 18/11/2026 · `goi_dang_ky_an` *(đăng ký 6 tháng trước mới bị trừ — người dùng không còn nhớ)*
5. "0 sao ms xứng đáng , quên tắt thành toán tự động nó tự thành toán xg muốn hoàn tiền nhắn mãi bên Zalopay mãi k rep" — `zalopay-001`, 25/11/2026 · `tu_tru_khong_ro`, cờ `quen_huy`, `da_lien_he_khong_xong`
6. "tự động trừ tiền gia hạn locket gold trong khi t không hề quét vân tay xác nhận giao dịch…, thậm chí trong phần gói thuê bao của t còn không có phần đăng ký locket gold" — `momo-498`, 18/10/2026 · `goi_dang_ky_an`
7. "tự trừ tiền khi không đăng kí" — `zalopay-209`, 08/11/2026 · `tu_tru_khong_ro`, cờ `khong_biet_ai_tru`

Link trang app: https://play.google.com/store/apps/details?id=com.mservice.momotransfer · https://play.google.com/store/apps/details?id=vn.com.vng.zalopay (xem 27/11/2026).

## 5. Giới hạn của data

- **Chỉ review 1 sao** → chỉ người đang bực. Số cho biết **loại** pain nào phổ biến trong phàn nàn, **không** phải % người dùng ví gặp pain. Tỉ lệ người dùng và số lần / tháng phải lấy từ khảo sát / phỏng vấn.
- **6 tuần gần nhất**, chỉ Google Play (không có App Store) → thiếu người dùng iPhone, thiếu mùa vụ.
- **Không phải sự cố một lần:** review "khoản trừ tự động" của ZaloPay rải đều 3–7 review / ngày suốt 6 tuần, không dồn vào ngày nào. Ngược lại, MoMo ngày **05/11** có 57 review 1 sao (trung bình mẫu MoMo ~12 review / ngày), dồn vào `ky_thuat_ekyc` (34) và `giao_dich_loi` (19) — có vẻ là sự cố, làm hai nhãn này của MoMo cao hơn bình thường.
- **ZaloPay cao hơn MoMo rõ rệt** ở nhóm rộng (22.0% vs 7.4%). Data không cho biết vì sao (khác cách liên kết thanh toán tự động? khác người dùng?) → không suy ra ví nào "tệ hơn".
- **Ranh giới nhãn:** chữ "dịch vụ" chung chung (vd "tự ý thanh toán dịch vụ") chưa có luật rõ — khoảng 4 dòng nằm giữa `goi_dang_ky_an` và `tu_tru_khong_ro`; không đổi số rộng.
- **Nhãn do AI gắn** → độ tin cậy phụ thuộc mục 3b.
- Data cho biết người ta **làm gì / gặp gì**, không cho biết **vì sao** và **bao lâu mới phát hiện**.

→ **Kiểm lại bằng khảo sát / phỏng vấn:** (1) trong 3 tháng qua có bị trừ tiền tự động mà không nhớ đã đăng ký không; (2) **bao lâu sau** mới phát hiện, bị trừ mấy kỳ; (3) có biết ngay đó là dịch vụ nào không, mất bao lâu để tìm ra; (4) mỗi lần mất bao nhiêu (khoảng tiền, không hỏi số dư).
