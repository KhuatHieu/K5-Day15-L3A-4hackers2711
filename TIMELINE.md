# TIMELINE — mốc và đánh dấu việc xong

> **Xong việc thì đánh dấu ở đây:** đổi `[ ]` thành `[x]`, gạch dòng bằng `~~…~~`, rồi ghi giờ xong + commit hoặc link ở cuối dòng. Ví dụ:
> `- [x] ~~E1 · Hiếu · hypothesis.md~~ ✅ 15:20 · a1b2c3d`
> Chi tiết từng việc (file nào, thế nào là xong) xem `TASKS.md` theo mã. Trễ hoặc kẹt thì thêm `⚠ <lý do>` ở cuối dòng, đừng xoá dòng.
> Sửa trên GitHub web cũng được. Nếu sửa ở máy thì `git pull` trước khi sửa.

Tên viết tắt: **H** = Hiếu · **L** = Long · **N** = Nghĩa · **T** = Thông

## ✅ Đã xong (sáng 27/11)
- [x] ~~Đào review: 1.000 review 1★ MoMo + ZaloPay, bộ nhãn, đếm~~ ✅ `ad7b40c`
- [x] ~~Nháp `evidence/data-mining.md` + mẫu 100 dòng để người kiểm nhãn~~ ✅ `1b93f1d`

## ✅ CP1 · 17:00 Thứ Sáu 27/11 · 3 điểm — ĐÃ NỘP 15:45
- [x] ~~E1 · H · `evidence/hypothesis.md` (giả thuyết cho khảo sát)~~ ✅ 15:14 · 108e535
- [x] ~~E2 · H+T · Tạo Google Form từ `evidence/survey/questions.md`~~ ✅ 15:28 · https://forms.gle/q7rfiWSYTywBPX2U6 · đã gửi Zalo, Slack, Facebook cá nhân
- [x] ~~E2b · cả nhóm · Mỗi người gửi link form cho ≥5 người quen có dùng ví~~ ✅ 15:45
- [x] ~~C0 · cả nhóm · chốt bài toán + lát cắt + chuẩn đạt + câu thử~~ ✅ 15:40 · biên bản `CHOT-1600.md`
- [x] ~~C3 · cả nhóm · Điền cột "Phần việc chính" trong `TEAMS.md`~~ ✅ 15:40 · `run.py check` không lỗi
- [x] ~~C1 · H · `canvas.md` đủ 7 dòng (bản nháp — cả nhóm xem lại lúc chốt C0)~~ ✅ 15:14 · 108e535
- [x] ~~C2 · H · Push, mở repo bằng cửa sổ ẩn danh, **nộp CP1**~~ ✅ 15:45 · đã nộp, commit 0e90494

## ✅ CP2 · 19:30 Thứ Sáu 27/11 · 4 điểm — ĐÃ NỘP 18:55
- [x] ~~I1 · mỗi người · 1 cuộc phỏng vấn (10–15 phút), ghi `evidence/interviews/P1–P4.md` — 17:00–18:00~~ ✅ 18:39 · H: `P1.md` · L: `P2.md` · N: `P3.md` (e111b70) · T: `P4.md` (thành viên nhóm, không tính) · **ngoài nhóm 3/3**
- [x] ~~I1 · T · Ghi trải nghiệm trong `evidence/interviews/P4.md`, người dùng xác nhận thời lượng 10–15 phút~~ ✅ 18:23 27/11/2026 · chưa commit · người trả lời là thành viên nhóm, không tính vào số người ngoài nhóm.
- [x] ~~G1 · cả nhóm · 18:00–18:20 tổng hợp: phỏng vấn + số khảo sát đến lúc đó → chốt lát cắt + vẽ sơ đồ cùng nhau~~ ✅ 18:16 · tổng hợp ở `evidence/summary.md` + canvas dòng "Đã đổi gì" (6b6fedc); sơ đồ §4 giữ bản của Nghĩa
- [x] ~~D1 · N · `spec.md` §4 sơ đồ + công cụ + chỗ chặn rủi ro + chỗ người duyệt — trước 19:00~~ ✅ 15:32 · [spec.md](spec.md)
- [x] ~~D2 · N · `spec.md` §5 ≥6 chỗ khó + 2 câu tấn công~~ ✅ 15:32 · [spec.md](spec.md)
- [x] ~~X1 · L · `codebase/` khung chạy hết luồng với AI giả (`python run.py`) — trước 19:00~~ ✅ 16:16 · 6303988 (đã nối công cụ thật của Nghĩa; B11–B12 chờ X5)
- [x] ~~S1 · H · `spec.md` §0–§2 bài toán + bảng impact 4 hướng~~ ✅ 15:20 (agent) · ⚠ các thừa số impact đang *(tự ước tính)*, thay bằng số khảo sát lúc 09:30
- [x] ~~V3 · T · Script sinh data synthetic có seed + nhãn (`data/gen_transactions.py`)~~ ✅ 15:20 (bản đầu); cập nhật 16:39 · chưa commit · v2: 200 dòng = 150 tình huống + 50 nhiễu; nguồn nội dung review, tái tạo giống từng byte; Trương Văn Thông đã kiểm tra và xác nhận ngày 27/11/2026; xem `data/DATA_CARD.md`
- [x] ~~V4 · T · `data/DATA_CARD.md` bản đầu~~ ✅ 15:20 (bản đầu); cập nhật 16:39 · chưa commit · mô tả dữ liệu v2, kiểm tương thích công cụ; Trương Văn Thông đã kiểm tra và xác nhận ngày 27/11/2026
- [x] ~~V1 · H · `eval/benchmark.csv` ≥10 câu~~ ✅ 15:40 · 15 câu
- [x] ~~V2 · H · `eval/metric_spec.yaml` 6 metric + chuẩn "đạt" §7 (≥70%, 100% tu_choi, 0 số lệch)~~ ✅ 15:40 · **KHÔNG sửa nữa**
- [x] ~~V5 · T · Người thứ hai chấm thử 5 output (≥4/5)~~ ✅ 18:41 27/11/2026 · chưa commit · Thông cung cấp điểm Hiếu và Thông đều `11110` cho B01/B06/B07/B11/B14; khớp 5/5 (100%). Xem `eval/second-review.md` và `eval/second-review-comparison.csv`. Chưa cung cấp output/trace hoặc run ID/model local.
- [ ] G2 · cả nhóm · 19:00–19:15 đổi chéo review X ↔ Y; `python run.py check` không lỗi · ⚠ nộp sớm 18:55 trước giờ đổi chéo; `run.py check` không lỗi (18:51). Vẫn đổi chéo lúc 19:00, sửa gì thì ghi `spec.md` §10. **Không sửa §7 / `metric_spec.yaml`**
- [x] ~~C4 · H · Canvas cập nhật (số đầu tiên + 1 trích dẫn + dòng "đã đổi gì so với CP1")~~ ✅ 18:15 · số khảo sát tạm (n=33) + P2 + review
- [x] ~~C2 · H · Push + **nộp CP2** — 19:25~~ ✅ 18:55 · đã nộp, commit 9cfa94c (§7 có kết quả lượt 1: 18/20, đạt)
- [x] ~~X3 · L · Lấy API key, gọi thử 1 câu — **trước khi rời lớp**~~ ✅ 16:00 · ad4bcc5 (Gemini `gemini-3.1-flash-lite`)

## 🟡 CP3 · 10:00 Thứ Bảy 28/11
- [x] ~~E3 · L · Kiểm 100 nhãn AI → `human_check.py merge` → điền `data-mining.md` mục 3b — trước 23:00 27/11~~ ✅ 19:05 · e5e32fa (khớp 87/100: goi 28/33 · tu_tru 28/30 · khác 31/37; ⚠ người gắn từng thấy nhãn AI ở lần thử, ghi ở 3b)
- [ ] E2c · T · Khảo sát: kiểm số người lúc 22:00 (mục tiêu ≥20), nhắc lại nếu thiếu
- [x] ~~X2 · N · `detect_recurring` (code thuần) chạy đúng trên data synthetic~~ ✅ 15:57 · [kiểm công cụ](codebase/test_tools.py)
- [x] ~~X6 · N · Bảng hướng dẫn huỷ ≥8 dịch vụ, có link chính thức + ngày xem; `lookup_cancel_guide`~~ ✅ 15:57 · [bảng hướng dẫn](data/cancel_guides.csv)
- [x] ~~X4 · L · Nối model thật (`codebase/ai.py`), `run.py eval --try` chạy được — **tối 27/11**~~ ✅ 17:22 · 92b0f33 (Claude Haiku 5.5; `eval --try` 3/3 câu, token > 0, ~630 vào / ~40 ra mỗi câu)
- [x] ~~X5 · L · Chặn rủi ro Track E (số từ công cụ, không OTP, không tư vấn đầu tư, huỷ chỉ đưa hướng dẫn)~~ ✅ 17:19 · 0c9633e (B11, B12 qua với AI giả + Claude Haiku; 13 câu khác không đổi; `codebase/test_scope.py`)
- [x] ~~V6 · H+T · Bộ câu thử lên 20–30 câu (≥5 `kho`, ≥2 `tu_choi`)~~ ✅ 18:45 · 20 câu (thuong 7 · kho 11 · tu_choi 2), B16–B20 do Nghĩa thêm (7b3f098) · ✅ 21:20 thêm B21–B23 nguồn `nguoi_dung` (P3, P2, P1) → 23 câu, 10/23 nguồn thật · ghi `spec.md` §10
- [ ] E4 · T · Chốt khảo sát 09:30, xuất `evidence/survey/results.csv` (đã xoá thông tin cá nhân) · bản tạm 18:15: 34 phản hồi → `count.py` → `results.csv` (cột `cach_thu`: 30 hỏi miệng, 4 tự điền) · ⚠ chạy lại `count.py` với bản xuất 09:30 (sửa danh sách `TU_DIEN` cho người tự điền mới); xác nhận không có thành viên nhóm và câu 11 trùng ở dòng 26/30
- [ ] E5 · H · `evidence/summary.md`: số chính + ≥5 trích dẫn + kết luận đúng / sai / phải đổi; cập nhật bảng impact · 21:20 nháp xong với số tạm (n=33): `summary.md`, `spec.md` §0, §1, §2 (impact ≈ 58 triệu đ + 134 giờ / 1.000 người / tháng) · ⏳ 09:30 chạy lại `python evidence/survey/count.py` rồi thay số
- [x] ~~R1 · cả nhóm · 09:00–09:45 chạy **lượt 1** cùng nhau → `eval/run-1.csv`, chấm `pass`~~ ✅ chạy sớm 18:35 27/11 · `run-1@20261127-183503` · gpt-6.2-sol · **18/20 (90%), đạt** · ⚠ commit code gọi OpenAI trong `ai.py` (không kèm key) để chạy lại được; commit lượt Gemini 16:44 với tên riêng
- [ ] D3 · N · Duyệt nháp `spec.md` §6 "Bốn đường đi" (agent viết 21:20) — CP3 cần đủ §0–§7
- [ ] X8 · N · Commit đoạn gọi OpenAI trong `codebase/ai.py` (**không** kèm `.env` / key) để chạy lại được `run-1@20261127-183503`; commit lượt Gemini 16:44 nguyên file với tên riêng (vd `eval/run-gemini-1644.csv`, `traces/run-gemini-1644.jsonl`) và sửa `eval/README.md` (lúc 16:44 bộ câu mới có 15 câu)
- [ ] X7a · cả nhóm · Chọn cải tiến lượt 2 (đề xuất: bước đưa hướng dẫn cho B14 thiếu link, B19 thiếu bước đối chiếu hoá đơn) → `eval/run-2.csv` trên 23 câu, cùng model · ghi §10
- [ ] P3 · L · **Video 30 giây** bản chạy thử gọi AI thật (`python run.py`: B01, B13 `kiem_tra`, B11 từ chối) → YouTube "Không công khai", mở thử bằng cửa sổ ẩn danh — **bắt buộc CP3**, trước 09:30
- [ ] C2 · H · Push + **nộp CP3** — 09:55 · kèm link video + kết quả lượt 1 + run ID

## 🟢 CP4 · 14:30 Thứ Bảy 28/11
- [ ] R2 · cả nhóm · 10:00–10:30 ngồi chung đọc các câu trượt → chọn 1 cải tiến
- [ ] X7 · L+N · Cải tiến → **lượt 2** (`eval/run-2.csv`), ghi `spec.md` §10
- [ ] K1 · T · `run.py simulate` ≥50 phiên + 3 kịch bản quy mô thật (`cost/`)
- [ ] B1 · mỗi người · *(bonus)* 1 người ngoài nhóm dùng thử, ghi `validation/log.md`
- [ ] G3 · cả nhóm · 13:00 kết luận go / iterate / stop dựa trên số
- [ ] P1 · H+N · Slide (có trang "Đánh giá thế nào" + "Chi phí khi dùng thật")
- [ ] P2 · L+T · Video demo dự phòng
- [ ] G4 · cả nhóm · Tập demo, mỗi người nói 1 phần
- [ ] C2 · H · Push + **nộp CP4** — 14:25

## 🏁 Demo · hạn chót 23:59 Thứ Bảy 28/11
- [ ] Demo Zone 14:30–16:00 (Demo Phòng 16:00–18:00 nếu lọt top)
- [ ] Sửa theo góp ý → ghi `spec.md` §10 (giờ · đổi gì · vì sao), chạy thêm thì ghi thành `run-3`
- [ ] Reflection: `reflection/khuat-duy-hieu.md` · `reflection/doan-gia-long.md` · `reflection/nguyen-dac-tuan-nghia.md` · `reflection/truong-van-thong.md`
- [ ] Push lần cuối trước 23:59
