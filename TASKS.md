# TASKS — ai làm gì

> **Bản đề xuất** của đội trưởng, cả nhóm chỉnh trong 5 phút rồi chốt. Đổi người thì sửa cả ở đây lẫn ở `TIMELINE.md`.
> Mỗi việc có mã (`E1`, `X2`…). **Đánh dấu xong ở `TIMELINE.md`**, không đánh dấu ở file này.
> Cột "Phần việc chính" trong `TEAMS.md` lấy 1 dòng từ đây.

**Cách chia** (theo guide): cả nhóm đi cùng nhau ở các mốc chung, còn trong từng chặng thì chia 2 cặp.
- **Cặp X (thiết kế + bản chạy thử):** Long, Nghĩa
- **Cặp Y (bằng chứng + đánh giá + chi phí):** Hiếu, Thông

**Bài toán (Track E):** người dùng ví bị trừ tiền định kỳ cho gói đăng ký / dùng thử mà không biết đó là khoản gì, nên phát hiện muộn và mất thêm tiền.
**Lát cắt (dự kiến, chốt lúc 16:00):** 1 người dùng ví · thấy một khoản trừ lạ / định kỳ trong lịch sử giao dịch · code tìm chu kỳ và ngày trừ tiếp theo, AI xác định đó là dịch vụ nào (hoặc nói "không rõ") · người dùng được cảnh báo **trước lần trừ tiếp theo**, kèm các bước huỷ có nguồn.

---

## Khuất Duy Hiếu — đội trưởng · cặp Y
**Phần việc chính:** bằng chứng pain (đào review, khảo sát), bảng impact, chuẩn "đạt", nộp các checkpoint.

| Mã | Việc | File | Xong khi |
|---|---|---|---|
| E1 | Giả thuyết cho khảo sát / phỏng vấn | `evidence/hypothesis.md` | commit trước khi gửi form |
| E2 | Tạo Google Form từ `questions.md` và gửi (cùng Thông) | `evidence/survey/questions.md` | có link form, ghi kênh và giờ mở |
| C1 | Canvas 7 dòng | `canvas.md` | đủ 7 dòng, dòng 4 có giả thuyết + nguồn |
| C2 | Nộp CP1, CP2, CP3, CP4 (sau khi push, mở repo bằng cửa sổ ẩn danh) | trang hackathon | nộp đúng giờ |
| S1 | `spec.md` §1–§2: bài toán + bảng impact ≥3 hướng (khoản trừ tự động / giao dịch lỗi / ví trả sau), mỗi số có nguồn | `spec.md` | mỗi ô có nguồn hoặc *(tự ước tính)* |
| V1 | ≥10 câu thử (CP2), ≥1/3 lấy `source` từ review | `eval/benchmark.csv` | `run.py check` không lỗi |
| V2 | `metric_spec.yaml` ≥3 metric + chuẩn "đạt" §7. **Chốt trước 19:30, không sửa sau** | `eval/metric_spec.yaml`, `spec.md` §7 | commit trước 19:30 |
| E5 | Tổng hợp review + khảo sát + phỏng vấn → kết luận đúng / sai / phải đổi | `evidence/summary.md` | có số chính + ≥5 trích dẫn |
| P1 | Slide (cùng Nghĩa) | `slides/` | có trang "Đánh giá thế nào" + "Chi phí khi dùng thật" |
| I1 | 1 cuộc phỏng vấn | `evidence/interviews/P1.md` | 10–15 phút, chuyện đã xảy ra |

## Đoàn Gia Long — cặp X
**Phần việc chính:** bản chạy thử (`codebase/`): luồng agent, nối model thật, chặn rủi ro.

| Mã | Việc | File | Xong khi |
|---|---|---|---|
| E3 | Kiểm 100 nhãn do AI gắn (**không** mở `labels.csv` khi gắn), rồi chạy `human_check.py merge` | `evidence/reviews/raw-human-check.csv` (nhận qua Drive, **không commit**) | có độ khớp theo tầng ở `data-mining.md` mục 3b |
| X1 | Khung `codebase/agent.py` + `tools.py` chạy hết luồng với **AI giả** | `codebase/` | `python run.py` chạy hết, không lỗi |
| X3 | Lấy API key, gọi thử 1 câu **trước khi rời lớp** | `.env` (**không commit**), `docs/connect-model.md` | 1 câu chạy được với model thật |
| X4 | Nối model thật, token lấy từ `usage` | `codebase/ai.py` | `run.py eval --try` chạy thật |
| X5 | Chặn rủi ro Track E: mọi con số lấy từ công cụ, không xin OTP / mật khẩu, không tư vấn đầu tư, việc huỷ chỉ đưa hướng dẫn, không tự làm | `codebase/agent.py` | câu `tu_choi` qua |
| X7 | Cải tiến sau lượt 1 → lượt 2 (cùng Nghĩa) | `codebase/`, `eval/run-2.csv` | ghi thay đổi vào `spec.md` §10 |
| P2 | Video demo dự phòng (cùng Thông) | thư mục gốc | ≤2 phút |
| I1 | 1 cuộc phỏng vấn | `evidence/interviews/P2.md` | |

## Nguyễn Đắc Tuấn Nghĩa — cặp X
**Phần việc chính:** thiết kế giải pháp (`spec.md` §3–§5, sơ đồ), công cụ phát hiện chu kỳ, dữ liệu hướng dẫn huỷ.

| Mã | Việc | File | Xong khi |
|---|---|---|---|
| D1 | `spec.md` §4: sơ đồ (hình dạng + lý do), dữ liệu và công cụ AI dùng, chỗ chặn rủi ro, chỗ người duyệt, phần nào đang giả | `spec.md` | có sơ đồ trước 19:00 |
| D2 | `spec.md` §5: ≥6 chỗ khó theo 4 lớp + 2 câu tấn công → đưa cho Hiếu làm câu thử | `spec.md` | |
| X2 | Công cụ `detect_recurring` (code thuần, **không** dùng AI): tìm chu kỳ, ngày trừ tiếp theo, số tiền | `codebase/tools.py` | chạy đúng trên data synthetic |
| X6 | Bảng hướng dẫn huỷ ≥8 dịch vụ (App Store, Google Play, YouTube, Spotify, Netflix, ChatGPT…), **mỗi dòng có link trang chính thức + ngày xem**; công cụ `lookup_cancel_guide` | `data/`, `codebase/tools.py` | không bước nào thiếu nguồn |
| X7 | Cải tiến sau lượt 1 (cùng Long) | | |
| P1 | Slide (cùng Hiếu) | `slides/` | |
| I1 | 1 cuộc phỏng vấn | `evidence/interviews/P3.md` | |

## Trương Văn Thông — cặp Y
**Phần việc chính:** dữ liệu giả lập + DATA_CARD, khảo sát, mô phỏng chi phí.

| Mã | Việc | File | Xong khi |
|---|---|---|---|
| E2 | Giữ form khảo sát, nhắc mọi người gửi, theo dõi số người (mục tiêu 20 người lúc 22:00, 25 người lúc 09:30), xuất `results.csv` đã xoá thông tin cá nhân | `evidence/survey/` | ≥20 người ngoài nhóm |
| V3 | Script sinh lịch sử giao dịch **synthetic** (seed cố định): có khoản định kỳ, dùng thử chuyển sang trả phí, tên trên lịch sử bị lệch, giao dịch lỗi / trừ 2 lần để gây nhiễu, kèm nhãn đúng | `data/` | chạy lại ra đúng file cũ |
| V4 | `DATA_CARD.md` bản đầu (CP2) | `data/DATA_CARD.md` | |
| V5 | Người thứ hai chấm thử 5 output, khớp ≥4/5 | `eval/` | |
| V6 | Mở rộng lên 20–30 câu thử (cùng Hiếu, trước CP3) | `eval/benchmark.csv` | ≥5 `kho`, ≥2 `tu_choi` |
| K1 | Mô phỏng chi phí ≥50 phiên + 3 kịch bản quy mô thật | `cost/` | `run.py simulate` |
| P2 | Video demo dự phòng (cùng Long) | | |
| I1 | 1 cuộc phỏng vấn | `evidence/interviews/P4.md` | |

## Việc chung
- **Mỗi người:** 1 cuộc phỏng vấn (17:00–18:00), ghi theo `evidence/interviews/TEMPLATE.md`, bỏ tên. Gửi link form cho ≥5 người quen có dùng ví.
- **Mỗi người:** `reflection/<ten-khong-dau>.md` trước 23:59 28/11.
- **Mỗi người:** khi demo, nói ≥1 phần.
