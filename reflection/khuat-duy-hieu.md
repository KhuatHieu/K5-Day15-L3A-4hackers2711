# Reflection — Khuất Duy Hiếu

1. **Vai trò + phần mình làm (trỏ tới file / commit):**
   - Đội trưởng, phụ trách bằng chứng pain (`evidence/hypothesis.md`, `evidence/data-mining.md`, `evidence/summary.md`, `evidence/interviews/P1.md`), bảng impact (`spec.md` §0–§2, `canvas.md`) và nộp 4 mốc checkpoint (`108e535`, `6b6fedc`, `9cfa94c`, `929c04e`).
   - Xây dựng bộ câu thử và chuẩn "đạt" (`eval/benchmark.csv`, `eval/metric_spec.yaml`, `spec.md` §7, thêm B21–B23 từ phỏng vấn P1–P3 ở `fe0aa6c`), dựng slide `demo-slides.html` / `demo-slides.pdf` (`96d4a8c`, `4aae483`), app demo web `app/server.py` + `data/public_prices.csv` (`46402de`) và nhánh câu ngoài chủ đề (`644890f`, `f5d56c0`).

2. **AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):**
   - Dùng Gemini gắn nhãn 1.000 review ban đầu và Claude Code viết `evidence/survey/count.py`, tổng hợp bảng impact, nháp `demo-slides.html`, `README.md` và giao diện demo `app/server.py` (chi tiết `docs/ai-usage.md`).
   - Phải tự chỉnh lại định nghĩa nhãn `LABELS.md` sau lượt gắn đầu vì ~65 review "tự trừ tiền" bị gán rải rác 8 nhãn; rà `count.py` để làm sạch câu trả lời khảo sát bị bỏ qua rẽ nhánh; kiểm từng con số trên slide và đối chiếu `run-3` với `run-2` bằng diff.

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   - Ở lượt 1, câu B14 (`[U07] kiem_tra`) bị trượt dù AI cảnh báo đúng khoản 15.000đ ngày 30/11/2026 và giữ tên dịch vụ là "không rõ", vì câu trả lời thiếu link chính thức để người dùng đối chiếu (`huong_dan_huy_co_nguon`).
   - Bài học rút ra là với bài toán tài chính (Track E), nói "không rõ" để tránh bịa tên dịch vụ chưa đủ — bản chạy thử vẫn phải đưa bước tự kiểm tra an toàn kèm nguồn chính thức (`kiem_tra_khong_ro`) mới hữu ích và đạt chuẩn.
