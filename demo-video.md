# Video demo

## P3 · Video CP3 30 giây

Tệp bàn giao `demo-cp3-30s.mp4` có độ dài 30 giây, 1080p và dùng output thực tế của `python run.py` với OpenAI `gpt-6.2-sol`. Màn hình giữ dòng model và số token của từng ca để kiểm tra lời gọi thật. OTP mẫu được che trong phần nhập.

| Giây | Ca | Nội dung |
|---|---|---|
| 0–10 | B01 | Nhận diện BaoThuc Pro, 179.000đ, lịch gia hạn giả lập có mã nguồn. |
| 10–20 | B13 | Rà định kỳ và cảnh báo đúng ngày 29/11/2026. |
| 20–30 | B11 | Từ chối huỷ hộ, nhắc giữ kín OTP và để người dùng tự thao tác. |

**Link nộp CP3:** Chờ Long hoặc Hiếu đưa MP4 lên YouTube Không công khai hoặc Drive với quyền ai có link cũng xem được. Mở link bằng tab ẩn danh trước khi dán vào Form 2.

## P2 · Kịch bản video dự phòng · Long + Thông

**Trạng thái:** đã chuẩn bị kịch bản; chưa có video quay thực tế hoặc link công khai. Mục tiêu 90–110 giây, tối đa 2 phút.

| Thời lượng dự kiến | Màn hình / thao tác | Lời dẫn chính |
|---|---|---|
| 0–15 giây | Mở bản chạy thử bằng `python run.py`. | Người dùng thấy khoản trừ lạ; hệ thống giúp nhận diện và nhắc trước kỳ trừ. Dữ liệu đang dùng là synthetic. |
| 15–45 giây | Nhập `[U01] khoản 179k này là gì?` | Code cung cấp số tiền, lịch gia hạn; AI nhận diện dịch vụ. Chỉ vào căn cứ và link hướng dẫn trong output thực tế. |
| 45–65 giây | Nhập `[U01] kiem_tra`. | Quy tắc code quyết định cảnh báo; người dùng tự quyết định hủy. |
| 65–85 giây | Dùng câu B11 trong `eval/benchmark.csv`. | Hệ thống phải từ chối hủy hộ và không yêu cầu OTP. Không dùng OTP thật. |
| 85–110 giây | Mở bảng chi phí và kết quả eval. | Mô phỏng 50 phiên: 49 không lỗi API, tổng token quy giá $0.00607025. Độ đúng phải xem eval, không lấy 49/50 làm tỷ lệ chất lượng. |

**Trước quay:** chọn đúng model thật, thử kết nối; che `.env` và khóa API. Chỉ thu output thực tế, không sửa video để biến ca trượt thành đạt. Nếu có lỗi, giữ hoặc quay lại lượt mới và ghi rõ.

**Bàn giao:** lưu `demo-backup.mp4` ở thư mục gốc hoặc ghi link ai cũng xem được; kiểm thời lượng, âm thanh và mở video bằng cửa sổ ẩn danh. Chưa đánh dấu P2 hoàn thành trước khi có video.

**Phần Thông trình bày:** dữ liệu synthetic, token lấy từ usage API, ba kịch bản chi phí. Chi phí/task thành công = chi phí/phiên ÷ tỷ lệ đạt của lượt eval cùng model; hiện chưa đủ căn cứ chốt K4.
