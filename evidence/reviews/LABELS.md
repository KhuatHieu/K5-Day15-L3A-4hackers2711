# Bộ nhãn review — định nghĩa (chốt TRƯỚC khi gắn nhãn)

> Dùng cho **mẫu chính** `raw-reviews-1star.csv` do `scrape_reviews.py` sinh ra. Đếm bằng `python evidence/reviews/count_labels.py evidence/reviews/raw-reviews-1star.csv`.
> Mẫu: 500 review **1 sao mới nhất** mỗi app (MoMo, ZaloPay), **không lọc keyword** → mẫu số N gồm cả review không liên quan. Mẫu chỉ có người đang phàn nàn: số cho biết **loại** pain phổ biến, không phải % người dùng gặp pain (lấy từ khảo sát).
> `raw-reviews.csv` (mọi mức sao) chỉ dùng làm bối cảnh "1★ chiếm bao nhiêu trong review mới nhất" — xem `reviews-meta.json`, không cần gắn nhãn.
> Sửa định nghĩa thì sửa ở đây **trước** khi gắn tiếp, ghi dòng vào mục "Đã sửa" cuối file.

## Cách gắn

- Mỗi review **đúng 1 nhãn chính** ở cột `label` (chọn nhãn khớp **vấn đề chính** người viết phàn nàn). Hai nhãn cùng khớp → dùng **luật ưu tiên** bên dưới.
- Cột `flags`: 0, 1 hoặc nhiều cờ phụ, cách nhau bằng `;` — cờ đếm riêng, không ảnh hưởng nhãn chính. **Xét đủ mọi cờ cho mọi dòng**, không chỉ dòng thuộc nhãn liên quan.
- Cột `nguoi_gan`: ai gắn — viết tắt tên người (vd `H`), hoặc `AI:<tên model>` nếu AI gắn.
- Cột `label_2`: **người** gắn độc lập, **không nhìn** cột `label` (xem mục "Kiểm nhãn do AI gắn").
- Không chắc giữa hai nhãn → theo luật ưu tiên; vẫn không chắc → ghi lý do ở `ghi_chu`.
- **Chỉ đọc chữ trong review, không đoán** điều người viết không nói. Câu "tự trừ tiền" không nói gì về gói đăng ký → **không** được suy ra là gói đăng ký.

## Nhãn chính (`label`)

| Nhãn | Định nghĩa — gắn khi review… | Ví dụ dạng câu *(tự viết, không phải review thật)* |
|---|---|---|
| `goi_dang_ky_an` | nói bị trừ tiền **tự động / định kỳ** VÀ **nêu ít nhất một** trong: gói / đăng ký / thuê bao / gia hạn / dùng thử / tên dịch vụ hoặc nơi bán cụ thể (Apple, iCloud, Google Play, CH Play, YouTube, Spotify, Canva, ChatGPT, game, "app khác", "ứng dụng nào đó") | "quên huỷ dùng thử, hết hạn bị trừ 99k" · "tự trừ tiền mua gói trên app" |
| `tu_tru_khong_ro` | nói bị trừ / bị thanh toán **tự động, không cho phép, không rõ lý do**, nhưng **không nêu** gói, dịch vụ hay nơi bán nào, và **không** nói tới lừa đảo / bị hack | "tự trừ tiền" · "không mua gì tự nhiên bị trừ 300k" |
| `phi_khong_ro` | nói bị trừ **phí** của ví / ngân hàng (phí duy trì, phí rút, phí chuyển, phí SMS, phí dịch vụ nạp…) mà không hiểu hoặc cho là vô lý | "rút tiền mất phí mà không báo trước" |
| `giao_dich_loi` | giao dịch **do chính người dùng làm** bị lỗi: tiền đã trừ mà không thành công, treo "đang xử lý", **bị trừ 2 lần**, giao dịch đã huỷ / bị từ chối mà sau đó vẫn trừ, chờ hoàn tiền lâu, chuyển nhầm | "trừ tiền rồi mà nạp không vào" · "thanh toán 1 lần bị trừ 2 lần" |
| `cashback_khuyen_mai` | không nhận được hoàn tiền / voucher / ưu đãi như quảng cáo, hoặc điều kiện khuyến mãi khó hiểu | "nói hoàn 50k mà không thấy đâu" |
| `tra_sau_tin_dung` | ví trả sau / thẻ tín dụng / khoản vay: phí trễ hạn, lãi, nhắc nợ, không hiểu dư nợ, **ví trả sau bị chọn làm nguồn tiền** mà người dùng không muốn — khi review **không** nêu gói / dịch vụ định kỳ | "trễ 1 ngày mà phạt phí cao" · "tự dùng ví trả sau để thanh toán" |
| `lua_dao_chan_gd` | **nói rõ** bị lừa đảo, bị hack / chiếm tài khoản, giao dịch bị chặn / tạm giữ, tài khoản bị khoá vì rủi ro | "bị hack mất 400k" · "bị khoá ví không rõ lý do" |
| `ky_thuat_ekyc` | lỗi app, lag, đăng nhập, OTP không về, xác thực khuôn mặt / eKYC / NFC, liên kết ngân hàng lỗi — **không** có chuyện mất tiền | "không xác thực khuôn mặt được" |
| `cskh` | phàn nàn **chủ yếu** về chăm sóc khách hàng (tổng đài khó gọi, trả lời máy móc), không nêu rõ vấn đề tiền thuộc nhãn khác | "chat với tổng đài toàn bot" |
| `khac_tieu_cuc` | phàn nàn khác **không** thuộc các nhãn trên (quảng cáo, giao diện, gọi điện làm phiền, bắt tải app khác…). **Không** dùng cho review có chuyện bị trừ tiền | "app nặng, nhiều quảng cáo" |
| `khen_trung_tinh` | khen, cảm ơn, hoặc trung tính **về app**, không nêu vấn đề | "app tiện lợi" |
| `khong_ro` | quá ngắn / vô nghĩa / lạc đề / không đọc được ý ("ok", "lỏ", emoji), hoặc câu hỏi cách dùng không nêu vấn đề | "👍" · "chỉ cách đăng nhập với" |

## Luật ưu tiên (khi hai nhãn cùng khớp)

1. Có **bị trừ 2 lần**, hoặc giao dịch **đã huỷ / bị từ chối mà vẫn trừ**, hoặc giao dịch người dùng tự làm bị treo → `giao_dich_loi` (kể cả khi có chữ "tự động").
2. Bị trừ tự động **có nêu** gói / dịch vụ / nơi bán → `goi_dang_ky_an`, **kể cả khi tiền lấy từ ví trả sau** (gắn thêm cờ `nguon_tra_sau`).
3. Bị trừ tự động **không nêu** gì → `tu_tru_khong_ro`. Chỉ chuyển sang `lua_dao_chan_gd` khi review **nói rõ** lừa đảo / hack / chiếm tài khoản.
4. Ví trả sau bị chọn làm nguồn tiền / phí trả sau, không nêu gói định kỳ → `tra_sau_tin_dung`.
5. Vấn đề tiền + phàn nàn CSKH → nhãn của vấn đề tiền, gắn cờ `da_lien_he_khong_xong`.
6. Câu chửi chung "app lừa đảo", "ăn cướp tiền" **không** kèm chuyện cụ thể → `khac_tieu_cuc` (không suy ra lừa đảo thật hay bị trừ tiền).

## Cờ phụ (`flags`)

| Cờ | Gắn khi review… |
|---|---|
| `khong_biet_ai_tru` | cho thấy người viết **không biết** khoản trừ là của dịch vụ / ai / vì sao — gồm "không mua gì mà bị trừ", "không đăng ký mà bị trừ", "trừ dịch vụ gì đó", "không rõ lý do" |
| `do_loi_nham_vi` | trách ví (MoMo / ZaloPay) về khoản tiền mà **theo chính lời review** là để trả cho **bên khác** (Apple, Google, CH Play, app, game, gói dịch vụ). Review chỉ nói "ví tự trừ" mà không nhắc bên nào → **không** gắn |
| `bi_tru_nhieu_ky` | nói đã bị trừ **nhiều lần / nhiều tháng** ("mấy tháng nay", "trừ 2–3 lần rồi", "xuống ngày tự thanh toán") |
| `quen_huy` | nói **quên huỷ** gói / dùng thử / thanh toán tự động, hoặc huỷ không được / không tìm thấy chỗ huỷ |
| `nguon_tra_sau` | tiền bị trừ từ **ví trả sau** |
| `da_lien_he_khong_xong` | nói đã liên hệ CSKH / tổng đài / yêu cầu hoàn tiền nhưng không giải quyết được |
| `neu_so_tien` | có nêu số tiền cụ thể (dùng ước tính "mỗi lần mất bao nhiêu" — **không** chép số kèm thông tin định danh) |

## Báo số cho hướng "khoản trừ tự động"

Báo **hai** số, ghi rõ định nghĩa:
- **Hẹp** = `goi_dang_ky_an` — bằng chứng cho pain gói đăng ký / quên huỷ dùng thử.
- **Rộng** = `goi_dang_ky_an` + `tu_tru_khong_ro` — bằng chứng cho pain "bị trừ tự động mà không biết là khoản gì".

## Kiểm nhãn do AI gắn

- Ghi ở `evidence/data-mining.md` và `docs/ai-usage.md`: model nào, ngày gắn, prompt (dán nguyên prompt hoặc để file trong repo), đã gắn theo phiên bản nào của file này.
- **Người** gắn độc lập ≥100 dòng ngẫu nhiên (seed ghi lại) vào `label_2`, **gồm mọi dòng** AI gắn `goi_dang_ky_an` / `tu_tru_khong_ro` nếu kịp. Không nhìn cột `label` khi gắn.
- `count_labels.py` in độ khớp và các cặp lệch nhiều nhất. Báo độ khớp cạnh số chính. Lệch nhiều ở cặp nào → sửa định nghĩa cặp đó, gắn lại, ghi vào "Đã sửa".

## Trích dẫn lên repo

Khi chép ví dụ sang `evidence/data-mining.md` / `evidence/summary.md`: dùng cột `id` (vd `momo-042`), ngày, số sao, **tối đa 2 câu**, không tên người viết, kèm link trang app và ngày cào (`reviews-1star-meta.json`).

## Đã sửa

| Thời điểm | Sửa gì | Vì sao |
|---|---|---|
| 27/11 ~11:30 | Thêm nhãn `tu_tru_khong_ro`; siết `goi_dang_ky_an` (phải nêu gói / dịch vụ / nơi bán); `khac_tieu_cuc` không dùng cho chuyện bị trừ tiền; `giao_dich_loi` gồm trừ 2 lần, giao dịch đã huỷ vẫn trừ; thêm **luật ưu tiên**; viết rõ `khong_biet_ai_tru`, `do_loi_nham_vi`; thêm cờ `quen_huy`, `nguon_tra_sau`; thêm mục báo số hẹp / rộng và kiểm nhãn AI | Lượt gắn AI đầu tiên: ~65 review chỉ nói "tự trừ tiền" bị gán rải rác 8 nhãn (33 `goi_dang_ky_an`, 15 `khac_tieu_cuc`, 5 `lua_dao_chan_gd`…); câu giống nhau ra nhãn khác nhau (vd `zalopay-209` vs `zalopay-212`); trừ 2 lần bị gán gói đăng ký (`momo-314`, `momo-424`); cờ `khong_biet_ai_tru` gắn thiếu |
