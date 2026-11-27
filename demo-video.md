# P2 — Kịch bản video dự phòng · Long + Thông

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
