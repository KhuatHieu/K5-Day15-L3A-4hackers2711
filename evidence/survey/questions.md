# Khảo sát — khoản trừ tự động trên ví điện tử

> Chép nguyên sang Google Form. **Không** thu tên, email, SĐT, mã học viên (trừ câu 11 nếu người trả lời tự để lại).
> Giả thuyết cần kiểm: `evidence/hypothesis.md`. Bộ câu này viết **trước** khi gửi form, sau khi đào review (`evidence/data-mining.md`).
> Ngưỡng: **≥20 người ngoài nhóm**, có dùng ví điện tử / app ngân hàng để thanh toán.

| Mục | Ghi |
|---|---|
| Link form | __ |
| Kênh gửi | __ (vd nhóm Zalo lớp L3A, nhóm bạn bè, gia đình — ghi từng kênh) |
| Giờ mở | __ 27/11 |
| Giờ chốt | 09:30 28/11 (trước CP3) |
| Người giữ form, xuất kết quả | Trương Văn Thông |

## Lời mở đầu (dán vào mô tả form)

> Nhóm sinh viên khoá AI20K đang tìm hiểu chuyện **bị trừ tiền tự động** trên ví điện tử / app ngân hàng (gói đăng ký, dùng thử, gia hạn…). Khảo sát ẩn danh, khoảng 3 phút, chỉ hỏi chuyện **đã xảy ra** với bạn. Không hỏi số dư, số tài khoản hay mã OTP.

## Câu hỏi

| # | Câu hỏi | Kiểu trả lời | Đo cái gì |
|---|---|---|---|
| 1 | Bạn là: | Chọn một: học viên AI20K · sinh viên · đi làm · khác | ai trả lời |
| 2 | Bạn đang dùng ví / app nào để **thanh toán online**? | Chọn nhiều: MoMo · ZaloPay · ShopeePay · VNPay / app ngân hàng · thẻ tín dụng · **không dùng** (→ nộp form) | lọc đúng người dùng |
| 3 | Ví / thẻ của bạn có đang **liên kết thanh toán tự động** cho dịch vụ nào không? (Apple / iCloud, Google Play, YouTube, Spotify, Netflix, ChatGPT, game, phần mềm…) | Có · Không · **Không chắc** | % không nắm được mình đang bị trừ tự động cho gì |
| 4 | Trong **3 tháng qua**, bạn đã bao nhiêu lần thấy một khoản **bị trừ tự động mà lúc đầu không nhận ra là khoản gì**? | 0 (→ câu 10) · 1 · 2 · 3 lần trở lên · không nhớ | **tỉ lệ người gặp** + **số lần / 3 tháng** (impact) |
| 5 | **Lần gần nhất** đó, khoản đó hoá ra là gì? | Chọn một: dùng thử hết hạn tự chuyển sang trả phí · gói tự gia hạn mà mình quên · dịch vụ mình không nhớ đã đăng ký · phí của ví / ngân hàng · giao dịch lỗi / bị trừ 2 lần · lừa đảo / bị hack · **đến giờ vẫn không biết** · khác | loại pain — so với nhãn review |
| 6 | Lần đó, bạn **phát hiện sau bao lâu** kể từ lần trừ **đầu tiên**? | Ngay hôm đó · trong 1 tuần · 1 tuần – 1 tháng · hơn 1 tháng (đã bị trừ từ 2 kỳ trở lên) | phát hiện muộn → cảnh báo trước lần 2 có ý nghĩa không |
| 7 | Lần đó, bạn mất bao lâu để **tìm ra là dịch vụ nào và cách huỷ**? | Dưới 5 phút · 5–15 phút · 15–60 phút · hơn 1 giờ · không tìm ra | **thời gian mất mỗi lần** (impact) |
| 8 | Lần đó, bạn đã làm gì, và kết quả? | Chọn nhiều: tự tìm và huỷ được · hỏi CSKH của ví · hỏi bên dịch vụ (Apple, Google…) · đòi được tiền về · không đòi được tiền · bỏ qua · khác | ví có bị trách nhầm không, có xong việc không |
| 9 | Số tiền lần đó khoảng bao nhiêu? | Dưới 50k · 50–100k · 100–200k · 200–500k · trên 500k · không nhớ | **tiền mất mỗi lần** (impact) — không hỏi số dư |
| 10 | Hiện tại, bạn có biết **ngày bị trừ tiếp theo** của các khoản đang trả tự động không? | Biết hết · biết một phần · không biết · không có khoản nào | nhu cầu cảnh báo trước |
| 11 | *(tuỳ chọn)* Kể ngắn lần đó: bị trừ cái gì, phát hiện thế nào, khó chịu nhất ở đâu? | Đoạn văn — **đừng ghi tên, số tài khoản, SĐT** | trích dẫn nguyên văn |
| 12 | *(tuỳ chọn)* Bạn có sẵn lòng cho nhóm hỏi thêm 10 phút không? | Có — để lại cách liên hệ (không bắt buộc) · Không | nguồn phỏng vấn |

Cài đặt Google Form: câu 2 chọn "không dùng" → chuyển tới trang nộp; câu 4 chọn "0" → chuyển tới câu 10. Tắt "thu thập email".

## Lưu kết quả

- `results.csv` — bản xuất **đã xoá** cột thời gian chi tiết và cột liên hệ của câu 12. Bản gốc có liên hệ **không** commit (đặt tên `raw-*.csv` để `.gitignore` chặn).
- Số chính lấy từ câu 4, 6, 7, 9 kèm ≥3 câu trả lời nguyên văn từ câu 11 → `evidence/summary.md`. Mẫu số = số người qua câu 2 (có dùng ví). Dưới 10 người thì ghi x/n, không ghi %.
- Đối chiếu với giả thuyết: `evidence/hypothesis.md` → ghi "đúng / sai / phải đổi" ở `evidence/summary.md`.
