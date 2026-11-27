# AI SPEC — Cảnh báo khoản trừ định kỳ trước kỳ tiếp theo · Nhóm 4hackers2711 · Phòng [XXX] · Zone [X]

> Mốc nộp: §7 chốt chuẩn "đạt" tại **CP2 19:30 Thứ Sáu 27/11** · §0–§7 nộp **CP3 10:00 Thứ Bảy 28/11** · đủ §0–§10 **CP4 14:30 Thứ Bảy 28/11** · §10 changelog ghi tiếp đến **23:59 Thứ Bảy 28/11**.
> Đầu mỗi mục ghi bước guide (`02-guide.md` trong repo đề) chỉ cách điền. Mỗi mục ngắn, có số và nguồn; chi tiết để ở file được trỏ tới. Xoá dòng hướng dẫn trong ngoặc vuông khi điền xong.

Track: [ ] A · [ ] B · [ ] C · [ ] D · [x] E — bài toán: E4 "Subscription & Auto-debit Guard" (nhóm tự mở rộng trong bối cảnh Track E): người dùng ví bị trừ tiền định kỳ cho gói đăng ký / dùng thử mà không biết đó là khoản gì.
Data BTC cấp đã dùng (nếu có — không commit nguyên file): không có (Track E không có data BTC cấp). Bằng chứng lấy từ review công khai trên Google Play. Dữ liệu chạy thử là synthetic, xem `data/DATA_CARD.md`.

## §0. Hiện tại việc này diễn ra thế nào *(guide 1.1)*
- Luồng hiện tại *(⏳ chưa kiểm, cần ảnh chụp tài khoản của thành viên, đã che thông tin)*:
  1. Người dùng đăng ký dùng thử / gói trên Google Play, App Store hoặc web, và chọn ví MoMo / ZaloPay (hoặc thẻ liên kết với ví) làm nguồn thanh toán.
  2. Hết thời gian dùng thử hoặc tới kỳ gia hạn, nền tảng tự trừ tiền qua ví. Ví chỉ báo biến động số dư với mô tả của bên bán (vd `GOOGLE *<tên app>`, `APPLE.COM/BILL`).
  3. Người dùng thấy khoản lạ, hỏi CSKH của ví. Ví thường trả lời đây là thanh toán theo yêu cầu của bên bán và bảo liên hệ bên bán. Theo review, 26/147 người đã liên hệ mà không xong (`evidence/data-mining.md`).
  4. Người dùng tự tìm chỗ huỷ (Google Play → Gói thuê bao; iPhone → Cài đặt → Gói đăng ký; hoặc trang web của dịch vụ). Nếu không tìm ra thì bị trừ tiếp kỳ sau.
- Công cụ đang có *(⏳ chưa kiểm)*: trang quản lý gói thuê bao của Google Play và App Store (liệt kê gói và ngày gia hạn, **chỉ các gói mua trên nền tảng đó**); mục quản lý "thanh toán tự động / liên kết" trong ví. Nhóm chưa thấy tính năng nào **cảnh báo trước** kỳ trừ tiếp theo, hay **nói ra khoản lạ là dịch vụ gì**. Cần kiểm lại bằng ảnh chụp app.

## §1. Người dùng & bằng chứng *(guide 1.1, 1.2)*
- **Người dùng chính:** người dùng ví MoMo / ZaloPay đã liên kết ví làm nguồn thanh toán tự động cho dịch vụ khác (Google Play, App Store, gói nhạc / phim / AI / game).
- **Việc họ cố làm xong:** *nhận ra một khoản bị trừ tự động là của dịch vụ nào, và dừng nó trước kỳ trừ tiếp theo.*
- **Hôm nay họ giải bằng gì, hỏng ở đâu, vì sao chưa bỏ:**
  - Hôm nay họ xem lịch sử ví, hỏi CSKH của ví, tự lên mạng tìm.
  - Hỏng ở chỗ mô tả trên lịch sử không khớp với tên dịch vụ họ nhớ. Ví dụ: đăng ký từ nhiều tháng trước (`zalopay-089`: đăng ký 19/05, bị trừ 16/11); mô tả `APPLE.COM/BILL` không nói gói nào. Vì vậy họ **trách nhầm ví** (22/147), hỏi ví thì ví không huỷ giúp được, và họ **chỉ phát hiện sau khi tiền đã mất**.
  - Chưa bỏ thanh toán tự động vì vẫn cần các gói đang dùng.
- **Pain (không có chữ AI):** người dùng ví xem lịch sử giao dịch thì thấy một khoản bị trừ tự động, không biết đó là dịch vụ nào, nên mất thời gian hỏi sai chỗ và bị trừ thêm kỳ nữa trước khi tìm ra chỗ huỷ.
- **Bằng chứng — số chính** (chi tiết: `evidence/data-mining.md`, tổng hợp: `evidence/summary.md`):
  - **Đào review** (đạt ngưỡng): 1.000 review 1★ mới nhất của MoMo + ZaloPay trên Google Play, 18/10–26/11/2026, nhãn do AI gắn, **người đang kiểm 100 dòng**.
  - Khoản trừ tự động chiếm **147/1000 (14,7%)**; ZaloPay 110/500 (22,0%), MoMo 37/500 (7,4%).
  - Trong 147 review đó: **57 (38,8%) không biết khoản trừ là của ai**, 26 (17,7%) đã liên hệ mà không xong, 22 (15,0%) trách nhầm ví.
  - Số tiền tự nêu trong 19 review có trung vị 500k. Số này lệch cao, chưa dùng cho bảng impact.
  - **Khảo sát** ≥20 người (`evidence/survey/questions.md`) + **phỏng vấn** ≥3 người: ⏳ đang làm, dùng để kiểm lại giả thuyết ở `evidence/hypothesis.md`.
  - Kết luận giả thuyết: ⏳ chờ khảo sát (09:30 28/11).

## §2. Impact & quyết định chọn *(guide 1.3)*

Tính trên **1.000 người dùng ví có liên kết thanh toán tự động**. Ô có ⏳ đang là *(tự ước tính)*, sẽ thay bằng số khảo sát ghi trong ngoặc.

| Hướng | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì | Impact / tháng (trên 1.000 người) | Làm kịp không | Chọn? |
|---|---|---|---|---|---|---|
| **A. Khoản trừ tự động không biết là gì** (gói đăng ký, dùng thử) | 250 ⏳ *(tự ước tính, bằng ngưỡng H1; thay bằng câu 4)* · review: 147/1000 phàn nàn 1★ | 0,33 ⏳ *(tự ước tính: 1 lần / 3 tháng; thay bằng câu 4)* | 1 kỳ tiền bị trừ thêm ~100k ⏳ *(tự ước tính; thay bằng câu 9)* + 30 phút tìm / hỏi ⏳ *(tự ước tính; thay bằng câu 7)* | ≈ 83 lần → **≈ 8,3 triệu đ + 41 giờ** | Kịp. Data giao dịch tự dựng được; phát hiện chu kỳ bằng code; AI đoán dịch vụ từ mô tả | ✅ |
| B. Giao dịch lỗi (trừ tiền mà không thành công, trừ 2 lần, chờ hoàn tiền) | review: 167/1000 (16,7%) | chưa đo | số tiền bị treo + thời gian chờ ví xử lý | chưa tính | Khó. Lời giải thật nằm ở **hệ thống ví** (tra soát, hoàn tiền); bản chạy thử không được kết nối hệ thống thật, AI chỉ hướng dẫn chung | ❌ |
| C. Ví trả sau: phí trễ hạn, ví trả sau tự được chọn làm nguồn tiền | review: 46/1000 (4,6%) | 1 kỳ / tháng *(theo kỳ sao kê)* | phí trễ hạn ⏳ chưa có nguồn | chưa tính | Kịp, nhưng nhắc hạn trả là **quy tắc thuần**, gần như không có quyết định AI | ❌ |
| D. Lỗi kỹ thuật / eKYC / đăng nhập | review: 387/1000 (38,7%), lớn nhất | — | không mất tiền trực tiếp | — | Không. Lỗi nằm trong app ví, phía người dùng không sửa được | ❌ |

- **Impact / tháng của hướng chọn (A)** = 250 người × 0,33 lần × (100k + 30 phút) ≈ **8,3 triệu đ + 41 giờ / 1.000 người dùng**.
  - Nguồn từng thừa số: **cả bốn đều đang *(tự ước tính)***, sẽ thay bằng khảo sát (câu 4, 4, 9, 7) lúc 09:30 28/11.
  - Review **chỉ** cho biết hướng A là loại phàn nàn về tiền lớn thứ hai trong review 1★, **không** cho biết % người dùng.
- **Hướng đã loại và vì sao** (giữ lại, đừng xoá):
  - **B** nhiều review hơn A, nhưng muốn giải thật thì phải can thiệp vào hệ thống ví. Ràng buộc chung của đề không cho kết nối hệ thống thật.
  - **C** gần như không có quyết định AI.
  - **D** không có chuyện mất tiền và nằm ngoài tầm tay người dùng.
  - Ý ban đầu "nhắc huỷ dùng thử" (số hẹp `goi_dang_ky_an` chỉ 33/1000) được **mở rộng** thành "khoản trừ tự động không biết là gì" (147/1000), vì 38,8% trong số này không biết ai trừ.
- **Số lần / tháng của từng kiểu người dùng** (dùng cho persona ở §8): ⏳ lấy từ khảo sát câu 4 (số lần trong 3 tháng) và câu 3 (có liên kết thanh toán tự động không).

## §3. Giải pháp tương tự *(guide 2.1)*
- [sản phẩm / tính năng gần giống]: một điều đáng học · một điều đáng né · mình khác gì

## §4. Thiết kế *(guide 2.2, 3.2)*
- **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả):
- Không làm (≥3 điều):
- **Sơ đồ** (ảnh / Mermaid / draw.io): [chèn ở đây]
- **Hình dạng:** [ ] workflow cố định · [ ] một agent · [ ] nhiều agent — 2 dòng lý do, và vì sao **không** chọn hình dạng phức tạp hơn:
- **AI dựa vào đâu** — mỗi công cụ (khớp `codebase/tools.py`):

  | Công cụ | Input | Output | Tác động ra ngoài? |
  |---|---|---|---|
  |  |  |  |  |

- **Mức tự động:** [ ] AI gợi ý, người quyết · [ ] AI tự làm khi chắc, chuyển người khi không · [ ] AI tự làm — lý do (sai thì ai chịu gì, sửa đắt hay rẻ):
- **Chỗ chặn rủi ro** (rủi ro lớn nhất của lát cắt bị chặn ở đâu, bằng gì):
- **Chỗ người duyệt** (việc AI không được tự làm):
- **Nguyên tắc thiết kế** (≥3, bắt buộc G10):

  | Nguyên tắc | Chỗ cụ thể trên sơ đồ / trong bản chạy thử |
  |---|---|
  | G10 — thu hẹp phạm vi khi không chắc |  |
  |  |  |
  |  |  |

- Phần nào còn giả (công cụ trả dữ liệu giả, model chế độ giả…) — ghi rõ, không giả làm thật:

## §5. Chỗ khó — 4 lớp + ≥6 kịch bản + 2 tấn công *(guide 2.3)*

| Kịch bản | Lớp (1–4) | Hành vi mong muốn (nói gì, hiện gì, cho làm gì tiếp) | Câu thử |
|---|---|---|---|
|  |  |  |  |
| *(tấn công)* |  |  |  |
| *(tấn công)* |  |  |  |

(1) nguồn sự thật · (2) mơ hồ / thiếu thông tin · (3) ngoài phạm vi / thẩm quyền · (4) đặc thù lĩnh vực (sai thì người dùng mất gì đắt nhất)

## §6. Bốn đường đi của trải nghiệm
- Mọi thứ suôn sẻ: · Không chắc (lớp 2): · Không có căn cứ (lớp 1): · Người dùng sửa:
- Bị đòi ngoài phạm vi (lớp 3): · Trường hợp đặc thù lĩnh vực (lớp 4):

## §7. Đánh giá & chuẩn "đạt" *(guide 2.4, 4.1)*
- Data card: `data/DATA_CARD.md` · bộ câu thử: `eval/benchmark.csv` — 12 câu (thuong 4 · kho 6 · tu_choi 2) · metric: `eval/metric_spec.yaml` (5 metric)
- **Chuẩn "đạt"** (chốt **trước 19:30 Thứ Sáu 27/11**, giữ nguyên đến 23:59 Thứ Bảy 28/11): ⚠ NHÁP chờ cả nhóm chốt — "Đạt khi ≥ 75% câu qua, và 100% câu `tu_choi` qua, và 0 câu có con số lệch output công cụ (`so_lieu_khop_cong_cu` = 100%)"
- Kết quả: lượt 1 __/__ (__%) · lượt 2 __/__ (__%) — run ID: __ / __ → chi tiết `eval/report.md`, hồ sơ `eval/README.md`

## §8. Chi phí khi dùng thật *(guide 4.2)*
- Persona + giá: `cost/personas.yaml` · lượt mô phỏng: `cost/simulate-__.csv` (__ phiên)
- Chi phí / task thành công: __ (model __) · __ (model __)
- Chi phí / tháng ở quy mô thật: thấp __ · cơ sở __ · cao __ → chi tiết `cost/cost-estimate.md`
- So với impact / người / tháng (§2): đáng làm không, vì sao:

## §9. Rủi ro & an toàn
- Dữ liệu: đã ẩn danh gì, không thu gì, không đưa gì vào model gói miễn phí:
- AI **không được** làm gì kể cả khi người dùng yêu cầu:
- Ai có thể bị hại nếu AI sai, và nhóm chặn thế nào:

## §10. Phân công & changelog
- Phân công có tên (theo chặng, chia cặp — guide "Cách chia việc"): __
- Dùng AI vào việc gì (2–3 dòng; chi tiết `docs/ai-usage.md`):
- Nhật ký thay đổi — **mọi thay đổi sau CP2 19:30 Thứ Sáu 27/11 phải có dòng ở đây**:

**CP2 → CP4** (vd thu hẹp lát cắt, hỏi thêm người dùng, lần cải tiến trước lượt 2)

| Thời điểm | Đổi gì | Vì sao (trỏ về câu thử / lỗi / bằng chứng nào) |
|---|---|---|
|  |  |  |

**Sau CP4 (đến 23:59 Thứ Bảy 28/11)** (sửa theo góp ý — không sửa chuẩn "đạt", câu thử, số bằng chứng, kết quả các lượt đã chạy)

| Thời điểm | Đổi gì | Vì sao |
|---|---|---|
|  |  |  |
