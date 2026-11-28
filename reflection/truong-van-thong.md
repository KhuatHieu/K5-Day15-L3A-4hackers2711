# Reflection — Trương Văn Thông


1. **Vai trò và phần việc**
   - Dữ liệu giả lập: `data/gen_transactions.py`, `data/DATA_CARD.md`; 200 giao dịch, 17 chuỗi đáp án, seed cố định.
   - Khảo sát và chấm chéo: `evidence/survey/`, `eval/second-review.md`; số khảo sát còn tạm, độ khớp chấm V5 là 5/5 theo điểm đã cung cấp.
   - Chi phí K1: `cost/personas.yaml`, `cost/cost-estimate.md`; 50 phiên Gemini, token đo được tương ứng $0.00607025; một phiên timeout, không coi phiên không lỗi API là đạt chất lượng.
   - Chốt K4/S2: `cost/build_k4.py`, `spec.md` §8; gpt-6.2-sol đạt 23/23 ở lượt 2, chi phí $0.00093678/task thành công; ba kịch bản 3.000/30.000/300.000 người là giả định tiếp cận.

2. **AI hỗ trợ và phần cần kiểm**
   - Codex hỗ trợ script, bảng tính và tài liệu; chi tiết ở `docs/ai-usage.md`.
   - Kiểm seed tái lập, liên kết đáp án, token CSV khớp trace và nguồn đơn giá; giá GPT dùng bảng K3 của nhóm, không tự coi là giá vừa tra lại.
   - Sửa model gọi thử từ tên lỗi 404 sang model API xác nhận có; tần suất dùng và quy mô tiếp cận phải ghi tự ước tính.
   - Rà lại ngày 28/11: 29 test qua; dữ liệu sinh lại khớp nội dung; K1 khớp trace và K4 khớp token eval. Khảo sát vẫn là bản tạm, chưa đủ thông tin để xác nhận số người ngoài nhóm.

3. **Một câu trượt và bài học đề xuất**
   - B14 ở lượt 1 cảnh báo đúng khoản trừ nhưng thiếu URL chính thức để kiểm tra gói (`eval/report.md`).
   - Lượt 2 bổ sung hướng dẫn kiểm tra có nguồn, B14/B19 chuyển sang đạt; 20 câu chung tăng từ 18/20 lên 20/20, toàn bộ 23 câu đạt 23/23.
   - Nhận diện và số tiền đúng chưa đủ; người dùng còn cần bước xử lý có nguồn.
   - Giữ câu trượt và chuẩn chấm, kiểm cải tiến bằng lượt mới; không coi phiên không lỗi API là output đạt chất lượng.
