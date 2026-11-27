# TIMELINE — mốc và đánh dấu việc xong

> **Xong việc thì đánh dấu ở đây:** đổi `[ ]` thành `[x]`, gạch dòng bằng `~~…~~`, rồi ghi giờ xong + commit hoặc link ở cuối dòng. Ví dụ:
> `- [x] ~~E1 · Hiếu · hypothesis.md~~ ✅ 15:20 · a1b2c3d`
> Chi tiết từng việc (file nào, thế nào là xong) xem `TASKS.md` theo mã. Trễ hoặc kẹt thì thêm `⚠ <lý do>` ở cuối dòng, đừng xoá dòng.
> Sửa trên GitHub web cũng được. Nếu sửa ở máy thì `git pull` trước khi sửa.

Tên viết tắt: **H** = Hiếu · **L** = Long · **N** = Nghĩa · **T** = Thông

## ✅ Đã xong (sáng 27/11)
- [x] ~~Đào review: 1.000 review 1★ MoMo + ZaloPay, bộ nhãn, đếm~~ ✅ `ad7b40c`
- [x] ~~Nháp `evidence/data-mining.md` + mẫu 100 dòng để người kiểm nhãn~~ ✅ `1b93f1d`

## 🔴 CP1 · 17:00 Thứ Sáu 27/11 · 3 điểm
- [x] ~~E1 · H · `evidence/hypothesis.md` (giả thuyết cho khảo sát)~~ ✅ 15:14 · 108e535
- [x] ~~E2 · H+T · Tạo Google Form từ `evidence/survey/questions.md`~~ ✅ 15:28 · https://forms.gle/q7rfiWSYTywBPX2U6 · đã gửi Zalo, Slack, Facebook cá nhân
- [ ] E2b · cả nhóm · Mỗi người gửi link form cho ≥5 người quen có dùng ví — trước 16:30
- [x] ~~T0 · T · Sửa mã học viên trong `TEAMS.md`~~ ✅ · c40f048
- [x] ~~C0 · cả nhóm · chốt bài toán + lát cắt + chuẩn đạt + câu thử~~ ✅ 15:40 · biên bản `CHOT-1600.md`
- [x] ~~C3 · cả nhóm · Điền cột "Phần việc chính" trong `TEAMS.md`~~ ✅ 15:40 · `run.py check` không lỗi
- [x] ~~C1 · H · `canvas.md` đủ 7 dòng (bản nháp — cả nhóm xem lại lúc chốt C0)~~ ✅ 15:14 · 108e535
- [ ] C2 · H · Push, mở repo bằng cửa sổ ẩn danh, **nộp CP1** — 16:50–16:55

## 🟠 CP2 · 19:30 Thứ Sáu 27/11 · 4 điểm
- [ ] I1 · mỗi người · 1 cuộc phỏng vấn (10–15 phút), ghi `evidence/interviews/P1–P4.md` — 17:00–18:00
- [ ] G1 · cả nhóm · 18:00–18:20 tổng hợp: phỏng vấn + số khảo sát đến lúc đó → chốt lát cắt + vẽ sơ đồ cùng nhau
- [ ] D1 · N · `spec.md` §4 sơ đồ + công cụ + chỗ chặn rủi ro + chỗ người duyệt — trước 19:00
- [ ] D2 · N · `spec.md` §5 ≥6 chỗ khó + 2 câu tấn công
- [ ] X1 · L · `codebase/` khung chạy hết luồng với AI giả (`python run.py`) — trước 19:00
- [x] ~~S1 · H · `spec.md` §0–§2 bài toán + bảng impact 4 hướng~~ ✅ 15:20 (agent) · ⚠ các thừa số impact đang *(tự ước tính)*, thay bằng số khảo sát lúc 09:30
- [x] ~~V3 · T · Script sinh data synthetic có seed + nhãn (`data/gen_transactions.py`)~~ ✅ 15:20 (agent làm theo lời H; T đọc lại)
- [x] ~~V4 · T · `data/DATA_CARD.md` bản đầu~~ ✅ 15:20 (agent) · ⚠ còn trống mục "Người kiểm" — T kiểm tay 10 chuỗi
- [x] ~~V1 · H · `eval/benchmark.csv` ≥10 câu~~ ✅ 15:40 · 15 câu
- [x] ~~V2 · H · `eval/metric_spec.yaml` 6 metric + chuẩn "đạt" §7 (≥70%, 100% tu_choi, 0 số lệch)~~ ✅ 15:40 · **KHÔNG sửa nữa**
- [ ] V5 · T · Người thứ hai chấm thử 5 output (≥4/5)
- [ ] G2 · cả nhóm · 19:00–19:15 đổi chéo review X ↔ Y; `python run.py check` không lỗi
- [ ] C4 · H · Canvas cập nhật (số đầu tiên + 1 trích dẫn + dòng "đã đổi gì so với CP1")
- [ ] C2 · H · Push + **nộp CP2** — 19:25
- [ ] X3 · L · Lấy API key, gọi thử 1 câu — **trước khi rời lớp**

## 🟡 CP3 · 10:00 Thứ Bảy 28/11
- [ ] E3 · L · Kiểm 100 nhãn AI → `human_check.py merge` → điền `data-mining.md` mục 3b — trước 23:00 27/11
- [ ] E2c · T · Khảo sát: kiểm số người lúc 22:00 (mục tiêu ≥20), nhắc lại nếu thiếu
- [ ] X2 · N · `detect_recurring` (code thuần) chạy đúng trên data synthetic
- [ ] X6 · N · Bảng hướng dẫn huỷ ≥8 dịch vụ, có link chính thức + ngày xem; `lookup_cancel_guide`
- [ ] X4 · L · Nối model thật (`codebase/ai.py`), `run.py eval --try` chạy được — **tối 27/11**
- [ ] X5 · L · Chặn rủi ro Track E (số từ công cụ, không OTP, không tư vấn đầu tư, huỷ chỉ đưa hướng dẫn)
- [ ] V6 · H+T · Bộ câu thử lên 20–30 câu (≥5 `kho`, ≥2 `tu_choi`)
- [ ] E4 · T · Chốt khảo sát 09:30, xuất `evidence/survey/results.csv` (đã xoá thông tin cá nhân)
- [ ] E5 · H · `evidence/summary.md`: số chính + ≥5 trích dẫn + kết luận đúng / sai / phải đổi; cập nhật bảng impact
- [ ] R1 · cả nhóm · 09:00–09:45 chạy **lượt 1** cùng nhau → `eval/run-1.csv`, chấm `pass`
- [ ] C2 · H · Push + **nộp CP3** — 09:55

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
