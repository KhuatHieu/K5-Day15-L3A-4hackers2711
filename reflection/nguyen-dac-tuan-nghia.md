# Reflection — Nguyễn Đắc Tuấn Nghĩa

1. **Vai trò + phần mình làm (trỏ tới file / commit):**
   - Phụ trách thiết kế giải pháp (`spec.md` §3–§6, sơ đồ luồng, 4 lớp chỗ khó và 2 kịch bản tấn công ở `5b20c90`, `4d4e668`), xây dựng công cụ `detect_recurring`, `lookup_renewal_schedule` và bảng hướng dẫn huỷ có nguồn `data/cancel_guides.csv` (`5cd45b7`, `6c6e4ec`, `99c744a`).
   - Ghi phỏng vấn `evidence/interviews/P3.md` (`e111b70`), bổ sung bộ nối OpenAI + câu thử B16–B20 (`7b3f098`, `4d4e668`), bổ sung nguồn đối chiếu EVN/MoMo/nhà mạng cho lượt 2 (`d5609b5`), chạy và bàn giao lượt 2 `run-2@20261128-113802` đạt 23/23 cùng `eval/report.md` (`d67c572`, `808da01`).

2. **AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):**
   - Dùng Codex hỗ trợ viết `detect_recurring`, `lookup_cancel_guide`, các bộ kiểm thử (`codebase/test_tools.py`, `codebase/test_ai.py`, `codebase/test_agent.py`) và đối chiếu URL chính thức trong `data/cancel_guides.csv` (`docs/ai-usage.md`).
   - Phải kiểm lại toàn bộ quy tắc tính chu kỳ (tối thiểu 3 lần trả phí, tách trừ trùng trong 2 phút, lấy ngày gia hạn từ phiếu giả lập có nguồn cho U01 thay vì đoán), đối chiếu thủ công từng URL chính thức + ngày kiểm và kiểm tra trace xem mọi số tiền/ngày có khớp đầu ra công cụ không.

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   - Câu B19 ở lượt 1 (`[U08] Khoản tiền điện EVN trừ mỗi tháng...`) đã nhận diện đúng đây là hoá đơn thiết yếu và không đưa bước huỷ thuê bao, nhưng vẫn bị chấm trượt vì thiếu hướng dẫn an toàn để người dùng đối chiếu hoá đơn trên cổng chính thức.
   - Điều học được là chỉ "tránh làm điều sai" (không xúi huỷ điện) là chưa đủ trong trải nghiệm người dùng; với những ca nhạy cảm ở lớp 4, hệ thống cần chủ động chỉ đúng kênh đối chiếu chính thống có nguồn (`kiem_tra_hoa_don`).
