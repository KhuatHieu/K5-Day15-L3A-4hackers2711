# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Codex | Viết `detect_recurring`, `lookup_cancel_guide`, bộ kiểm thử và đối chiếu nguồn cho bảng hướng dẫn hủy. | Đã chạy kiểm tự động trên dữ liệu giả lập. Nghĩa đọc diff trước khi commit. | Nguyễn Đắc Tuấn Nghĩa (X2, X6) |
| Prompt / thiết kế lời gọi mô hình | Claude Code | Gợi ý khung prompt nhận diện (chỉ trả JSON, coi mô tả là dữ liệu) và đoạn gọi API Gemini / Claude trong `ai.py`. | Long tự chọn model, sửa prompt theo output thật, chạy `eval --try` kiểm token lấy từ usage. | Đoàn Gia Long (X3, X4) |
| Khung chạy + chặn rủi ro Track E | Claude Code | Gợi ý regex cho các nhóm ý trong `check_scope` và test mẫu. | Long thiết kế luồng X1 và 5 nhóm chặn, viết câu từ chối, chạy `test_scope.py` và B11/B12 với model thật. | Đoàn Gia Long (X1, X5) |
| Đào data (viết script đếm, gợi ý nhãn) | | | Kiểm tay __ dòng, khớp __ | |
| Rà câu hỏi phỏng vấn / khảo sát | | Chỉ rà câu dẫn dắt | | |
| Ghi chép I1 của Thông | Codex | Sắp xếp câu trả lời người dùng cung cấp thành `evidence/interviews/P4.md`; chuẩn hóa “500k” thành 500.000 đồng; đánh dấu thông tin còn thiếu. Không dùng nội dung phỏng vấn giả định trước đó. | Người dùng bổ sung ngày trừ 13/11, phát hiện 15/11/2026, nhận ra dịch vụ, xử lý trên MoMo trong 5 phút, 1 lần lặp, đã tắt và không bị trừ nữa; xác nhận thời lượng 10–15 phút. Các điểm chưa rõ tiếp tục được ghi trong bản ghi. | Trương Văn Thông |
| Viết câu thử (benchmark) | | | Mỗi câu thử có `source`; câu thử AI viết được ghi rõ | |
| Sinh data `synthetic` (V3/V4) | Codex | Đọc nội dung CSV review người dùng cung cấp, không dùng cột nhãn review; cập nhật script và DATA_CARD, ghi nguồn tình huống trong DATA_CARD. Tạo 200 giao dịch: 150 tình huống + 50 nhiễu theo yêu cầu. | Seed 2711, lấy mẫu nhiễu seed 2712; kiểm tự động tái tạo và liên kết 17 chuỗi; 11 kiểm thử công cụ và tích hợp qua; script sinh đồng bộ giao dịch, đáp án và lịch gia hạn. Trương Văn Thông đã kiểm tra và xác nhận bộ dữ liệu cùng tài liệu V3/V4 ngày 27/11/2026. | Trương Văn Thông |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Chuẩn bị và ghi báo cáo V5 | Codex | Chuẩn bị phiếu B01/B06/B07/B11/B14 và kiểm thử riêng trong chat; ghi báo cáo từ điểm Thông cung cấp, tính độ khớp bằng Python. Không lấy điểm AI trong chat thay cho kết quả chấm local. | Thông cung cấp điểm Hiếu và Thông đều `11110`, khớp 5/5 (100%); xác nhận tự chạy/chấm local. Output/trace và run ID/model local chưa được cung cấp; các mục này để trống. | Trương Văn Thông |
| Slide, văn bản | | | | |
| `spec.md` §9 + hướng dẫn P3 | Claude Code | Nháp §9 từ code và test đã có; liệt kê các bước quay, đăng video. | Long đọc, sửa, đối chiếu từng ý với code trước khi commit. | Đoàn Gia Long (S3, P3) |
| CP3 của Thông và ước tính chi phí | Codex | Rà TASKS/TIMELINE, đếm lại khảo sát tạm bằng code, chạy K0 và mô phỏng 50 phiên với API Gemini; đối chiếu giá Google và quy mô MoMo, ghi rõ giả định tần suất, tiếp cận. Báo cáo USD theo yêu cầu của Thông. Không thêm phản hồi khảo sát, không sửa kết quả chạy đã có. | Kiểm tự động benchmark; token lấy từ usage API. Thông cần đọc diff và duyệt các giả định; dữ liệu khảo sát mới, thành viên nhóm và hai dòng trùng chưa được xác nhận. | Trương Văn Thông |
| Hoàn thiện phép tính K1 | Codex | Bổ sung script tính USD bằng Decimal, xuất đủ 50 dòng chi phí từng phiên và 9 dòng nhóm/kịch bản; giải thích cách cộng chi phí theo persona. Dùng dữ liệu đo đã có, không gọi API thêm. | Kiểm tự động tổng token và run ID khớp trace, chi phí từng phiên khớp đơn giá, tổng ba kịch bản khớp báo cáo. Thông đọc diff trước khi commit; số phiên dùng sản phẩm và tỉ lệ tiếp cận vẫn là tự ước tính. | Trương Văn Thông |
| Tài liệu cá nhân và demo | Codex | Viết nháp reflection theo mẫu từ việc đã ghi trong repo; kịch bản P2 ≤2 phút; rút gọn báo cáo chi phí. | Thông duyệt lời reflection; Long và Thông còn quay video thực tế. Không tạo trải nghiệm hay video giả. | Trương Văn Thông |
| Dự toán GPT đã gỡ | Codex | Từng tạo dự toán GPT theo token giả định; sau đó xoá script và CSV theo yêu cầu của Thông, khôi phục báo cáo K1 Gemini. | Giữ nguyên dữ liệu mô phỏng gốc; số dự toán GPT không còn là báo cáo hiện hành. | Trương Văn Thông |
| Tổng hợp khảo sát + phỏng vấn P1 + canvas CP2 | Claude Code | Chép ghi lại phỏng vấn của Hiếu vào `P1.md` (không thêm nội dung), viết `evidence/survey/count.py` làm sạch theo rẽ nhánh form và đếm, phát hiện các cụm nhập bằng script và câu 11 trùng, nháp `summary.md` và canvas dòng 4 / "Đã đổi gì". | Hiếu đọc diff; Thông xác nhận cách thu (hỏi miệng / tự điền). Câu trả lời khảo sát là của người trả lời thật, AI không thêm hay sửa câu nào. | Khuất Duy Hiếu |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
