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
- [x] ~~G2 · cả nhóm · đổi chéo review X ↔ Y; `python run.py check` không lỗi~~ ✅ 18:15 · cả nhóm đã đổi chéo review; `run.py check` không lỗi (18:51)
- [x] ~~C4 · H · Canvas cập nhật (số đầu tiên + 1 trích dẫn + dòng "đã đổi gì so với CP1")~~ ✅ 18:15 · số khảo sát tạm (n=33) + P2 + review
- [x] ~~C2 · H · Push + **nộp CP2** — 19:25~~ ✅ 18:55 · đã nộp, commit 9cfa94c (§7 có kết quả lượt 1: 18/20, đạt)
- [x] ~~X3 · L · Lấy API key, gọi thử 1 câu — **trước khi rời lớp**~~ ✅ 16:00 · ad4bcc5 (Gemini `gemini-3.1-flash-lite`)

## ✅ Đã xong ngoài kế hoạch (chiều 27/11, ghi bù để không ai làm lại)
- [x] ~~N · `spec.md` §3 giải pháp tương tự (Google Play / Apple)~~ ✅ 15:41 · 5b20c90
- [x] ~~N · Lịch gia hạn giả lập có nguồn (`data/renewal_schedules.csv`, `lookup_renewal_schedule`) cho U01~~ ✅ 16:55 · 6c6e4ec
- [x] ~~L · Đổi model sang Claude Haiku 5.5 + thêm giá vào `cost/personas.yaml`~~ ✅ 16:56 · 92b0f33
- [x] ~~N · Trace ghi đủ số tiền và ngày (để chấm `so_lieu_khop_cong_cu`) + thêm `test_agent.py`~~ ✅ 17:40 · 99c744a
- [x] ~~N · B16–B20 + lượt 1 OpenAI `gpt-6.2-sol` (18/20) + `eval/report.md`, `eval/README.md`~~ ✅ 18:45 · 7b3f098
- [x] ~~H · Mã phòng / mã zone demo trong `spec.md`~~ ✅ 18:26 · 01f9fca
- [x] ~~H · Khảo sát: `count.py` làm sạch + `results.csv` có cột `cach_thu`; `summary.md`, canvas CP2~~ ✅ 18:16 · 6b6fedc
- [x] ~~H · `spec.md` §0, §2 (impact từ khảo sát tạm), nháp §6, §10; B21–B23 nguồn `nguoi_dung`~~ ✅ 21:05 · fe0aa6c

## 🟡 CP3 · 10:00 Thứ Bảy 28/11
- [x] ~~E3 · L · Kiểm 100 nhãn AI → `human_check.py merge` → điền `data-mining.md` mục 3b — trước 23:00 27/11~~ ✅ 19:05 · e5e32fa (khớp 87/100: goi 28/33 · tu_tru 28/30 · khác 31/37; ⚠ người gắn từng thấy nhãn AI ở lần thử, ghi ở 3b)
- [ ] E2c · T · Khảo sát: kiểm số người lúc 22:00 (mục tiêu ≥20), nhắc lại nếu thiếu · ⚠ đã kiểm bản tạm 27/11: 34 phản hồi, 33 dùng ví/thẻ; chưa có bản xuất lúc 22:00 và chưa xác nhận người ngoài nhóm, xem `evidence/survey/questions.md`
- [x] ~~X2 · N · `detect_recurring` (code thuần) chạy đúng trên data synthetic~~ ✅ 15:57 · [kiểm công cụ](codebase/test_tools.py)
- [x] ~~X6 · N · Bảng hướng dẫn huỷ ≥8 dịch vụ, có link chính thức + ngày xem; `lookup_cancel_guide`~~ ✅ 15:57 · [bảng hướng dẫn](data/cancel_guides.csv)
- [x] ~~X4 · L · Nối model thật (`codebase/ai.py`), `run.py eval --try` chạy được — **tối 27/11**~~ ✅ 17:22 · 92b0f33 (Claude Haiku 5.5; `eval --try` 3/3 câu, token > 0, ~630 vào / ~40 ra mỗi câu)
- [x] ~~X5 · L · Chặn rủi ro Track E (số từ công cụ, không OTP, không tư vấn đầu tư, huỷ chỉ đưa hướng dẫn)~~ ✅ 17:19 · 0c9633e (B11, B12 qua với AI giả + Claude Haiku; 13 câu khác không đổi; `codebase/test_scope.py`)
- [x] ~~V6 · H+T · Bộ câu thử lên 20–30 câu (≥5 `kho`, ≥2 `tu_choi`)~~ ✅ 18:45 · 20 câu (thuong 7 · kho 11 · tu_choi 2), B16–B20 do Nghĩa thêm (7b3f098) · ✅ 21:20 thêm B21–B23 nguồn `nguoi_dung` (P3, P2, P1) → 23 câu, 10/23 nguồn thật · ghi `spec.md` §10
- [ ] E4 · T · Chốt khảo sát 09:30, xuất `evidence/survey/results.csv` (đã xoá thông tin cá nhân) · bản tạm 18:15: 34 phản hồi → `count.py` → `results.csv` (cột `cach_thu`: 30 hỏi miệng, 4 tự điền) · ⚠ chạy lại `count.py` với bản xuất 09:30 (sửa danh sách `TU_DIEN` cho người tự điền mới); xác nhận không có thành viên nhóm và câu 11 trùng ở dòng 26/30
- [x] ~~E5 · H · `evidence/summary.md`: số chính + ≥5 trích dẫn + kết luận đúng / sai / phải đổi; cập nhật bảng impact~~ ✅ 07:01 28/11 · [tổng hợp](evidence/summary.md) có 7 trích dẫn review và kiểm nhãn 87/100. Kết luận và impact ghi theo mẫu tạm. Chờ bản chốt ở E4 để thay số.
- [x] ~~R1 · cả nhóm · 09:00–09:45 chạy **lượt 1** cùng nhau → `eval/run-1.csv`, chấm `pass`~~ ✅ chạy sớm 18:35 27/11 · `run-1@20261127-183503` · gpt-6.2-sol · **18/20 (90%), đạt** · [CSV](eval/run-1.csv) · [trace 20 câu](traces/run-1.jsonl).
- [x] ~~D3 · N · Duyệt nháp `spec.md` §6 "Bốn đường đi" (agent viết 21:20) — CP3 cần đủ §0–§7~~ ✅ 07:01 28/11 · [spec §6](spec.md), đối chiếu ca qua/trượt và đường xử lý của CLI.
- [x] ~~X8 · N · Bổ sung bộ nối OpenAI, lưu riêng lượt Gemini 16:44 và cập nhật hồ sơ đánh giá~~ ✅ 07:01 28/11 · [cấu hình](docs/connect-model.md), [CSV Gemini gốc](eval/run-gemini-1644.csv), [trace Gemini gốc](traces/run-gemini-1644.jsonl). Demo gọi OpenAI thật. File Gemini ghi 20 câu cục bộ B01–B20, 2 lỗi HTTP 503, chưa chấm.
- [x] ~~X7a · cả nhóm · Chọn cải tiến và chạy lượt 2 trên 23 câu cùng model~~ ✅ 11:40 · R2 đã chốt, code 9944cd6 + nguồn d5609b5, lượt `run-2@20261128-113802`.
- [x] ~~P3 · L · **Video 30 giây** bản chạy thử gọi AI thật (`python run.py`: B01, B13 `kiem_tra`, B11 từ chối) → YouTube "Không công khai", mở thử bằng cửa sổ ẩn danh — **bắt buộc CP3**, trước 09:30~~ ✅ 09:44 · https://youtu.be/Osshub09iA8
- [x] ~~K0 · T · `python run.py simulate --try` (10 phiên) để kiểm khung mô phỏng chi phí — guide 3.4 yêu cầu thử trước CP3~~ ✅ 21:51 27/11/2026 · chưa commit · Gemini `gemini-3.1-flash-lite`, 10 phiên: 8 không lỗi, 2 lỗi quota HTTP 429; token từ usage API, log thử được gitignore; xem `cost/cost-estimate.md`. Model đặt riêng cho tiến trình, không sửa `.env`.
- [x] ~~Q1 · cả nhóm · Trước khi nộp: `git log -p | grep -iE "api[_-]?key|sk-|AIza"` không ra gì; không có file `.env`, `raw-*` trên repo~~ ✅ 07:01 28/11 · đã quét file theo dõi, gói CP3 và lịch sử Git bằng mẫu thông tin xác thực. Các dòng chỉ nêu tên biến hoặc mẫu cấu hình được phân biệt với key. Không phát hiện key, file `.env` hoặc `raw-*` đã theo dõi.
- [x] ~~C2 · H · Push + **nộp CP3** — 09:55 · kèm link video + kết quả lượt 1 + run ID~~ ✅ 10:26 (trễ ~26 phút) · nộp Form 2: summary.md, video https://youtu.be/Osshub09iA8, lượt 1 18/20 `run-1@20261127-183503`

## 🟢 CP4 · 14:30 Thứ Bảy 28/11
- [x] ~~R2 · cả nhóm · 10:00–10:30 ngồi chung đọc các câu trượt → chọn 1 cải tiến~~ ✅ 11:27 (trễ) · cải tiến: hướng dẫn kiểm tra có nguồn khi không có hướng dẫn huỷ của kênh (dòng `kiem_tra_khong_ro`, `kiem_tra_hoa_don` trong `cancel_guides.csv`), nhắm B14 + B19 cùng nguyên nhân · code 9944cd6, dữ liệu d5609b5
- [x] ~~X7 · L+N · Cải tiến → lượt 2, ghi `spec.md` §10~~ ✅ 11:59 · Long đã ghi thay đổi và kết quả ở §10 trong `a0da52c`. B14 và B19 chuyển từ trượt sang đạt.
- [x] ~~K1 · T · `run.py simulate` ≥50 phiên + 3 kịch bản quy mô thật (`cost/`)~~ ✅ 21:58; bổ sung đầy đủ phép tính 22:03 27/11/2026 · chưa commit · `simulate-1@20261127-215058`, Gemini Flash-Lite, 50 phiên (49 không lỗi API, 1 timeout), tổng token quy giá $0.00607025; 3 kịch bản 3.000/30.000/300.000 người. Báo cáo USD có công thức, chi phí từng nhóm, phân rã người → phiên → USD; bảng `cost/session-costs-simulate-1.csv` đủ 50 phiên và `cost/scenario-costs-simulate-1.csv` đủ 9 dòng nhóm/kịch bản; token và run ID khớp trace. Xem `cost/cost-estimate.md`. K4 còn chờ eval lượt 2 cùng model để chốt chi phí/task thành công.
- [x] ~~K2 · T · `cost/personas.yaml`: ≥3 persona (ít · vừa · nhiều), số lần / tháng lấy từ khảo sát câu 4 + câu 3 (`count.py`), không đủ thì ghi *(tự ước tính)*~~ ✅ 21:58 27/11/2026 · chưa commit · tỉ lệ 12/33, 13/33, 8/33 từ câu 4 bản tạm; đối chiếu câu 3, tần suất 1/4/12 phiên/tháng ghi rõ *(tự ước tính)* vì khảo sát chưa đo tần suất dùng sản phẩm.
  - Cập nhật 22:12 27/11: từng thêm dự toán GPT theo lượt; **đã gỡ theo yêu cầu sau đó của Thông**. Báo cáo hiện tại `cost/cost-estimate.md` trở lại kết quả Gemini K1; CSV/trace mô phỏng gốc giữ nguyên.
- [x] ~~K3 · T+L · Giá model phải khớp model chạy lượt 2: thêm giá `gpt-6.2-sol` vào `cost/personas.yaml` (≥2 mức: rẻ + mạnh)~~ ✅ 13:43 · a35e12a · Long thêm `gpt-6.2-sol` 2.00 / 10.00 (Lớn, model lượt 2) và `gpt-6-luna` 0.10 / 0.50 (Nhỏ) từ `model-prices.md` repo đề (BTC tra 25/11); giữ 2 dòng Gemini. Theo token eval lượt 2: $0.00093678 / câu với `gpt-6.2-sol`.
- [x] ~~K4 · T · Quy mô thật: số người dùng MoMo / ZaloPay **có link nguồn công khai** (không dùng số 700 của khoá) → chi phí / tháng 3 kịch bản; chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt **lượt 2**~~ ✅ 13:52 28/11/2026 · chưa commit · gpt-6.2-sol, $0.00093678/câu do Thông cung cấp, lượt 2 23/23 → $0.00093678/task thành công. Nguồn MoMo >30 triệu người; 3.000/30.000/300.000 người → $13.625891/$136.258909/$1,362.589091 mỗi tháng. Xem `cost/cost-estimate.md`; tái lập bằng `python cost/build_k4.py`.
- [x] ~~S2 · T · `spec.md` §8 chi phí: điền từ `cost/cost-estimate.md`, so với impact / người / tháng ở §2 → 1 dòng "đáng làm không"~~ ✅ 13:52 28/11/2026 · chưa commit · §8 đã có chi phí $0.004541964/người/tháng, so với impact §2 qua ngưỡng giá trị thời gian, không quy đổi VND. Kết luận đáng thử tiếp; cần đo lợi ích thực tế và tổng chi phí vận hành.
- [x] ~~S3 · L · `spec.md` §9 rủi ro & an toàn: dữ liệu (synthetic, không gửi gì thật), AI không được làm gì (OTP, huỷ thay, đầu tư, dữ liệu người khác), ai bị hại nếu sai và chặn ở đâu (`check_scope`, số từ công cụ)~~ ✅ 09:38 · 375814d
- [x] ~~S4 · H · `spec.md` §10: dòng "Phân công có tên" + "Dùng AI vào việc gì" (2–3 dòng)~~ ✅ 14:00 · d6dc90a
- [x] ~~R3 · N+L · Chốt báo cáo so sánh trong `eval/report.md` và `eval/README.md` mục 5–6~~ ✅ 11:59 · `run-2@20261128-113802`, 18/20 → 20/20 trên bộ chung, 3/3 câu mới, 23/23 toàn lượt. Điểm B01–B12 của Long ở `a0da52c`, B13–B23 của Nghĩa ở `d67c572`.
- [x] ~~D4 · H · `README.md` của repo vẫn là khung ("[Tên nhóm]", mục 0): điền tên nhóm, lát cắt, cách chạy, link các file chính; xoá mục 0~~ ✅ 14:00 · d6dc90a · video dự phòng còn chờ P2
- [ ] A1 · mỗi người · `docs/ai-usage.md`: mỗi người tự thêm dòng việc mình dùng AI (dòng "Prompt / thiết kế lời gọi mô hình", "Slide, văn bản" còn trống) · Thông đã có khai báo dữ liệu, khảo sát, V5, K0/K1 và tài liệu bàn giao; không xác nhận thay các thành viên khác.
- [ ] B1 · mỗi người · *(bonus)* 1 người ngoài nhóm dùng thử, ghi `validation/log.md`
- [ ] G3 · cả nhóm · 13:00 kết luận go / iterate / stop dựa trên số
- [x] ~~P1 · H+N · Slide (có trang "Đánh giá thế nào" + "Chi phí khi dùng thật"), từ `slides/outline.md` · xuất **`demo-slides.pdf` ở thư mục gốc** (guide 5.2) hoặc link ai cũng xem được~~ ✅ 14:10 · `demo-slides.html` ở thư mục gốc (9 trang; kết luận "Iterate" chờ nhóm chốt ở G3)
- [ ] P2 · L+T · Video demo dự phòng · ⚠ 22:06 27/11 đã có kịch bản ngắn và cách bàn giao ở `demo-video.md`; còn quay video thực tế ≤2 phút và kiểm link.
- [ ] G4 · cả nhóm · Tập demo, mỗi người nói 1 phần · ai cũng trả lời được 4 câu (guide 5.2): *Vì sao chọn hình dạng này? · Lỗi nguy hiểm nhất là gì? · Chi phí / task thành công tính thế nào? · Phần bạn làm là gì?*
- [ ] C2 · H · Push + **nộp CP4** — 14:25 · form cần: phòng demo + link repo, tích 7 hạng mục, lượt 1 → lượt 2, chi phí / task thành công kèm tên model, link slide + video dự phòng, phần chưa xong

## 🏁 Demo · hạn chót 23:59 Thứ Bảy 28/11
- [ ] Demo Zone 14:30–16:00 (Demo Phòng 16:00–18:00 nếu lọt top)
- [ ] Sửa theo góp ý → ghi `spec.md` §10 (giờ · đổi gì · vì sao), chạy thêm thì ghi thành `run-3`
- [ ] Reflection: `reflection/khuat-duy-hieu.md` · `reflection/doan-gia-long.md` · `reflection/nguyen-dac-tuan-nghia.md` · `reflection/truong-van-thong.md` · ⚠ 22:06 27/11 đã viết nháp của Thông theo 3 câu trong TEMPLATE; Thông cần đọc, sửa và xác nhận trước nộp.
- [ ] H · Dọn repo: `CHOT-1600.md` giữ làm biên bản hay xoá; sửa `AGENTS.md` mục Quy trình git cho khớp cách làm thật (nhánh + PR)
- [ ] (tuỳ chọn) E6 · ai rảnh · Ảnh chụp trang Gói thuê bao Google Play / mục thanh toán tự động trong ví (che thông tin) để bỏ ⏳ ở `spec.md` §0
- [ ] Push lần cuối trước 23:59
