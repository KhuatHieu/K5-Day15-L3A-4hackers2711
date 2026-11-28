# Reflection — Đoàn Gia Long

> Bản nháp viết từ các việc đã ghi trong repo (TIMELINE, `spec.md` §9–§10, `docs/ai-usage.md`, `eval/report.md`). Long đọc, sửa thành lời của mình và xác nhận trước khi nộp.

1. **Vai trò và phần việc**
   - Thành viên cặp X, phụ trách bản chạy thử trong `codebase/` (`TEAMS.md`). Khung chạy hết luồng với AI giả (X1, `6303988`).
   - Nối model thật trong `codebase/ai.py`: gọi thử Gemini (X3, `ad4bcc5`), đổi sang Claude Haiku 5.5, `eval --try` lấy token từ usage (X4, `92b0f33`).
   - Chặn rủi ro Track E trong `check_scope`: không OTP, không tư vấn đầu tư, chỉ đưa hướng dẫn huỷ, số chỉ lấy từ công cụ (X5, `0c9633e`, `codebase/test_scope.py`). Viết `spec.md` §9 (S3, `375814d`).
   - Cải tiến lượt 2: thêm hướng dẫn kiểm tra có nguồn khi kênh không có hướng dẫn huỷ (X7, `9944cd6`, `test_fallback_guide.py`), chấm B01–B12. Thêm giá `gpt-6.2-sol` / `gpt-6-luna` (K3, `a35e12a`). Quay video P3 và P2.

2. **AI hỗ trợ và phần phải sửa**
   - Dùng Claude Code gợi ý khung prompt nhận diện (chỉ trả JSON, coi mô tả giao dịch là dữ liệu), đoạn gọi API và regex cho các nhóm ý trong `check_scope`.
   - Tự chọn model và sửa prompt theo output thật khi chạy `eval --try`. Kiểm token lấy từ `usage` của API, không ước lượng.
   - Regex AI gợi ý phải chạy lại với B11/B12 trên model thật và `test_scope.py`. Nháp §9 đối chiếu từng ý với code trước khi commit. Chi tiết ở `docs/ai-usage.md`.

3. **Một câu trượt và bài học**
   - B14 trượt ở lượt 1: agent cảnh báo đúng khoản 15.000đ ngày 30/11/2026 và nói rõ là chưa biết dịch vụ. Nhưng câu trả lời không có hướng dẫn kiểm tra kèm URL chính thức. B19 (hoá đơn EVN) trượt cùng nguyên nhân (`eval/report.md`).
   - Bài học: nhận diện đúng và số đúng vẫn chưa đủ. Khi agent nói "không rõ" thì người dùng vẫn cần một bước tiếp theo có nguồn, không để họ tự xoay xở.
   - Sửa nguyên nhân chung (thêm dòng `kiem_tra_*` vào bảng nguồn), không so khớp chữ của từng câu thử. Lượt 2: B14 và B19 đều đạt, 23/23. Các câu vốn đạt vẫn giữ nguyên.
