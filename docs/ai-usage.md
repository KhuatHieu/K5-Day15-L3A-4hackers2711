# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Codex | Viết `detect_recurring`, `lookup_cancel_guide`, bộ kiểm thử và đối chiếu nguồn cho bảng hướng dẫn hủy. | Đã chạy kiểm tự động trên dữ liệu giả lập. Nghĩa đọc diff trước khi commit. | Nguyễn Đắc Tuấn Nghĩa (X2, X6) |
| Prompt / thiết kế lời gọi mô hình | | | | |
| Đào data (viết script đếm, gợi ý nhãn) | | | Kiểm tay __ dòng, khớp __ | |
| Rà câu hỏi phỏng vấn / khảo sát | | Chỉ rà câu dẫn dắt | | |
| Ghi chép I1 của Thông | Codex | Sắp xếp câu trả lời người dùng cung cấp thành `evidence/interviews/P4.md`; chuẩn hóa “500k” thành 500.000 đồng; đánh dấu thông tin còn thiếu. Không dùng nội dung phỏng vấn giả định trước đó. | Người dùng bổ sung ngày trừ 13/11, phát hiện 15/11/2026, nhận ra dịch vụ, xử lý trên MoMo trong 5 phút, 1 lần lặp, đã tắt và không bị trừ nữa; xác nhận thời lượng 10–15 phút. Các điểm chưa rõ tiếp tục được ghi trong bản ghi. | Trương Văn Thông |
| Viết câu thử (benchmark) | | | Mỗi câu thử có `source`; câu thử AI viết được ghi rõ | |
| Sinh data `synthetic` (V3/V4) | Codex | Đọc nội dung CSV review người dùng cung cấp, không dùng cột nhãn review; cập nhật script và DATA_CARD, ghi nguồn tình huống trong DATA_CARD. Tạo 200 giao dịch: 150 tình huống + 50 nhiễu theo yêu cầu. | Seed 2711, lấy mẫu nhiễu seed 2712; kiểm tự động tái tạo và liên kết 17 chuỗi; 11 kiểm thử công cụ và tích hợp qua; script sinh đồng bộ giao dịch, đáp án và lịch gia hạn. Trương Văn Thông đã kiểm tra và xác nhận bộ dữ liệu cùng tài liệu V3/V4 ngày 27/11/2026. | Trương Văn Thông |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Chuẩn bị V5 | Codex | Đọc chuẩn chấm, chọn trước B01/B06/B07/B11/B14 và tạo phiếu chấm độc lập cùng hướng dẫn đối chiếu. Chưa chấm output, chưa tạo điểm hoặc độ khớp. | Người dùng cho biết người đầu đã chấm; Thông cần nhận output/trace, tự kiểm và chấm độc lập trước khi xem điểm người đầu. | Trương Văn Thông |
| Slide, văn bản | | | | |
| Tổng hợp khảo sát + phỏng vấn P1 + canvas CP2 | Claude Code | Chép ghi lại phỏng vấn của Hiếu vào `P1.md` (không thêm nội dung), viết `evidence/survey/count.py` làm sạch theo rẽ nhánh form và đếm, phát hiện các cụm nhập bằng script và câu 11 trùng, nháp `summary.md` và canvas dòng 4 / "Đã đổi gì". | Hiếu đọc diff; Thông xác nhận cách thu (hỏi miệng / tự điền). Câu trả lời khảo sát là của người trả lời thật, AI không thêm hay sửa câu nào. | Khuất Duy Hiếu |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
