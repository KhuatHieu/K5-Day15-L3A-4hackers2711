# Reflection — Trương Văn Thông

> Bản nháp từ công việc đã ghi trong repo ngày 27/11/2026; Thông đọc, sửa và xác nhận trước khi nộp. Chưa ghi trải nghiệm demo ngày 28/11.

1. **Vai trò và phần việc**
   - Dữ liệu giả lập: `data/gen_transactions.py`, `data/DATA_CARD.md`; 200 giao dịch, 17 chuỗi đáp án, seed cố định.
   - Khảo sát và chấm chéo: `evidence/survey/`, `eval/second-review.md`; số khảo sát còn tạm, độ khớp chấm V5 là 5/5 theo điểm đã cung cấp.
   - Chi phí: `cost/personas.yaml`, `cost/cost-estimate.md`; 50 phiên, ba kịch bản, chỉ báo cáo USD.

2. **AI hỗ trợ và phần cần kiểm**
   - Codex hỗ trợ script, bảng tính và tài liệu; chi tiết ở `docs/ai-usage.md`.
   - Kiểm seed tái lập, liên kết đáp án, token CSV khớp trace và đơn giá từ nguồn chính thức.
   - Sửa model gọi thử từ tên lỗi 404 sang model API xác nhận có; tần suất dùng và quy mô tiếp cận phải ghi tự ước tính.

3. **Một câu trượt và bài học đề xuất**
   - B14 ở lượt 1 cảnh báo đúng khoản trừ nhưng thiếu URL chính thức để kiểm tra gói (`eval/report.md`).
   - Nhận diện và số tiền đúng chưa đủ; người dùng còn cần bước xử lý có nguồn.
   - Giữ câu trượt và chuẩn chấm, kiểm cải tiến bằng lượt mới; không coi phiên không lỗi API là output đạt chất lượng.
