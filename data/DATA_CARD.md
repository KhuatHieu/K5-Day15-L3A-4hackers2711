# Data card — V3/V4 · giao dịch ví giả lập

Cập nhật 27/11/2026. Dữ liệu chỉ dùng chạy thử, không có giao dịch thật hay thông tin cá nhân của người viết review.

## Nguồn và cách tạo

Nguồn gợi ý là file `raw-reviews-1star.csv` người dùng cung cấp: 1.000 review, gồm 500 MoMo và 500 ZaloPay, ngày trong CSV từ 14/10 đến 26/11/2026. Đây là review, không phải sao kê. Chỉ dùng nội dung và các cột `id`, `app`, `date`, `score`, `text`; không dùng hay đánh giá cột nhãn AI. File đầy đủ được giữ ở Downloads, không sao chép vào repo.

Bảng tình huống dưới đây ghi nguồn review và phần bổ sung giả lập. Tên app con, số tiền và lịch thu là **giả lập (tự ước tính)**, không chứng minh giá hay lịch thanh toán thật. Riêng số 758.889đ và mốc 16/11 được lấy ý từ `zalopay-089`; tên app và giả thiết gói năm vẫn là dựng.

## Cách chạy lại

```powershell
python data/gen_transactions.py
python -m unittest discover -s codebase -v
```

Lệnh đầu tạo lại hai CSV synthetic. Chỉ cần thư viện chuẩn Python, không cần API hay file review trên máy để chạy. Nội dung review đã được đối chiếu khi dựng kịch bản. `--output-dir` cho phép sinh thử vào thư mục riêng. `--max-rows` mặc định 200, không tính dòng tiêu đề; nhỏ hơn 150 sẽ báo lỗi vì không được cắt mất giao dịch tình huống.

Seed sinh giao dịch là **2711**. Nhiễu được sinh theo lịch rồi chọn lại bằng seed **2712**, giữ tối thiểu hai dòng nhiễu cho mỗi người. Cùng cấu hình và script sinh lại giống từng byte; đã đối chiếu hai lần chạy trong thư mục tạm.

## Dataset 1 — transactions.csv

| Mục | Mô tả |
|---|---|
| Mục đích | Input của `get_transactions` ở `codebase/agent.py` và `detect_recurring` ở `codebase/tools.py`. |
| Quy mô | **200 dòng dữ liệu = 150 giao dịch tình huống + 50 giao dịch nhiễu**; 11 hồ sơ giả lập U01–U11. Không tính tiêu đề. |
| Nhãn nguồn | `synthetic`, sinh bằng code; không phải sao kê thật. |
| Thời gian | Ngày mô phỏng `2026-11-27`; cửa sổ cấu hình 28/05–27/11/2026, riêng U10 từ 19/11. Dữ liệu sau lấy mẫu không phải lịch sử chi tiêu đầy đủ từng ngày. |
| Cột | `tx_id`: ID giao dịch; `user_id`: hồ sơ giả; `time`: thời điểm; `description`: mô tả; `amount_vnd`: số tiền chi, VND; `source`: `vi`/`tra_sau`; `status`: trạng thái. |
| Phiên bản | v2, 27/11/2026; giới hạn theo yêu cầu 150 + 50. |
| Giới hạn | Có một dòng dùng thử 0đ, còn lại là khoản chi; chưa có nạp vào ví hay hoàn tiền. `status` đều là `thanh_cong`, kể cả giao dịch bị trừ trùng. Không có mùa vụ, không đại diện tần suất hay tỷ lệ người gặp pain. |

| Hồ sơ | Tình huống và nguồn gợi ý |
|---|---|
| U01 | Dùng thử chuyển trả phí, khó tìm chỗ hủy (`zalopay-340`); quên hủy (`momo-019`). App, giá, lịch và biến thể tên Spotify là dựng. |
| U02 | Hai khoản Apple khác giá, không rõ gói. `zalopay-402`/`zalopay-495` nói về dịch vụ Apple; mô tả sao kê và lịch là dựng. |
| U03 | Netflix nhiều tên (ca bổ sung); YouTube đổi giá (lịch và giá dựng, `momo-314` chỉ gợi ý dịch vụ). |
| U04 | Đăng ký từ lâu rồi mới thấy trừ (`zalopay-089`); chỉ một lần trả phí. Review không xác nhận gói năm. |
| U05 | Trừ hai lần, không phải gia hạn. `momo-424` gợi ý bị trừ lần nữa; nạp điện thoại và khoảng cách 40 giây là dựng. |
| U06 | Gói game theo tuần, ca bổ sung giả lập. |
| U07 | Khoản trừ không nhận ra (`momo-147`, `zalopay-209`); PayPal, mã GTGT và chu kỳ là dựng. |
| U08 | ChatGPT (`momo-424`); dao động VND và hóa đơn điện thiết yếu là bổ sung giả lập. |
| U09 | Ví trả sau tự được chọn (`momo-033`); gói truyện và lịch là dựng. |
| U10 | Một lần trừ, lịch sử ngắn, chưa đủ căn cứ dự báo; ca bổ sung. |
| U11 | Ca bổ sung: 26 lần thu gói tuần + 44 lần thu GTGT mỗi bốn ngày, đủ 70 giao dịch tình huống bổ sung. |

## Dataset 2 — recurring_truth.csv

Có **17 chuỗi đáp án** liên kết đủ **150 giao dịch tình huống** qua `tx_ids`. Các dòng còn lại trong transactions.csv là 50 giao dịch nhiễu.

Các cột gồm hồ sơ/persona, mã chuỗi, ví dụ mô tả, dịch vụ, nền tảng, loại khoản, chu kỳ danh nghĩa, số lần xuất hiện, lần trừ cuối, ngày kế tiếp của kịch bản, nguồn tiền, ghi chú và danh sách ID. Chỉ người kiểm và bộ kiểm dùng file này. App không được đọc đáp án.

`cycle_days = 30` của lịch tháng là giá trị danh nghĩa; ngày kế tiếp theo lịch tháng, không luôn bằng ngày cuối cộng 30. U01-S1 và U04-S1 chỉ có một lần trả phí: `next_date` trong đáp án là **lịch cài trong kịch bản**, không thể suy ra từ giao dịch. Công cụ phải báo thiếu căn cứ và không đưa dự báo cho hai chuỗi này. Các ca trừ trùng hoặc thiếu lịch sử khác để trống ngày kế tiếp.

## Tương thích kỹ thuật của nhóm

Giữ nguyên schema hai CSV, ngày mô phỏng và các giao dịch tình huống U01–U10. Bổ sung U11 được nhận bởi bộ đọc theo `user_id`. Sau lấy mẫu, `tx_id` được đánh lại và `tx_ids` cập nhật tương ứng; không dùng ID của v1 để đối chiếu v2.

Công cụ cần tối thiểu ba lần trả phí để xác nhận chu kỳ, tách trừ trùng trong hai phút. Giữ đủ dữ liệu cho các ca đổi giá, nhiều kiểu tên, ví trả sau và thiếu căn cứ. Không thêm nhãn dịch vụ vào CSV app đọc. File đáp án không được đưa vào luồng trả lời.

B01/B13 vốn kỳ vọng dự báo ngày 29/11 từ một lần trả phí, chưa khớp yêu cầu đủ căn cứ của công cụ; V3/V4 giữ nguyên ca thiếu căn cứ, không thêm giao dịch để làm câu thử qua và không sửa `expected`. Nhóm cần xử lý điểm này trong phần tích hợp/đánh giá theo quy định đã chốt.

## Dataset 3 — cancel_guides.csv (phần X6 của Nghĩa)

Giữ nguyên bảng 9 kênh hướng dẫn hủy hiện có. Mỗi dòng có kênh, bí danh, bước tự kiểm tra/hủy, URL trợ giúp chính thức và ngày đối chiếu. V3/V4 không thay nội dung hay xác nhận lại nguồn của bảng này.

## Kiểm tra và người duyệt

Đã kiểm tự động: tái tạo hai lần giống dữ liệu hiện tại, ID duy nhất, cửa sổ ngày, số tiền, nguồn tiền, liên kết đáp án và số dòng 150 + 50. Năm kiểm thử công cụ hiện có đã qua với 17 chuỗi v2. Dùng lại bộ kiểm của đội bằng lệnh `python -m unittest discover -s codebase -v`.

**Người kiểm:** Trương Văn Thông — đã kiểm tra và xác nhận bộ dữ liệu giả lập cùng tài liệu V3/V4 ngày 27/11/2026.

Dữ liệu synthetic dùng kiểm kỹ thuật; bằng chứng pain nằm ở review, khảo sát và phỏng vấn thật trong `evidence/`.
