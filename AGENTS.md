# AGENTS.md — hướng dẫn cho coding agent (Claude Code, Cursor, Codex…) làm việc trong repo này

> Ôn lại: ngày 12 · lab ngày 12. Nhóm sửa file này cho khớp bài của mình (thêm quy ước riêng, bỏ dòng không dùng).

## Repo này là gì

Repo nộp bài hackathon AI20K của nhóm: một bản chạy thử AI cho **một lát cắt** (xem `spec.md` §4), kèm bằng chứng, bộ câu thử và mô phỏng chi phí. Mọi câu trả lời phải chạy được bằng các lệnh dưới đây.

## Lệnh

```
python run.py                    # chạy bản chạy thử
python run.py check              # kiểm eval/benchmark.csv + eval/metric_spec.yaml
python run.py eval --try         # thử 3 câu đầu
python run.py eval               # chạy cả bộ → eval/run-N.csv + traces/run-N.jsonl
python run.py score eval/run-N.csv
python run.py simulate --try     # thử mô phỏng chi phí 10 phiên
python run.py simulate           # mô phỏng chi phí → cost/simulate-N.csv
```

Khung chỉ dùng thư viện chuẩn của Python. Thêm thư viện thì ghi vào `requirements.txt`.

## Cấu trúc code

| File | Ai sửa | Hợp đồng |
|---|---|---|
| `codebase/agent.py` | nhóm | `answer(text) -> {"output": str}` — luồng chính, đúng hình dạng ở `spec.md` §4 |
| `codebase/ai.py` | nhóm | `call_model(system, user) -> {"text", "model", "tokens_in", "tokens_out"}`, giữ `@model_call`. Token lấy từ `usage` của API, không ước lượng |
| `codebase/tools.py` | nhóm | mỗi công cụ một hàm có `@tool`, docstring: tên · input · output · có tác động ra ngoài không |
| `codebase/tracing.py`, `eval/run_eval.py`, `cost/simulate.py`, `run.py` | **khung — không sửa** | ghi trace, chạy bộ câu thử, mô phỏng chi phí |

## Luật — agent KHÔNG được làm

- Không commit `.env`, API key, dữ liệu cá nhân thật, nguyên file data BTC cấp.
- Không sửa `eval/run-*.csv`, `cost/simulate-*.csv`, `traces/*` đã chạy (trừ điền cột `pass`, `ghi_chu`).
- Không sửa chuẩn "đạt" (`spec.md` §7), `eval/metric_spec.yaml` sau CP2; không xoá câu thử trượt, không sửa `expected` cho khớp output.
- Không bịa người được phỏng vấn, trích dẫn, câu trả lời khảo sát, số liệu. Số không có nguồn thì ghi rõ *(tự ước tính)*.
- Công cụ có tác động ra ngoài (gửi tin, sửa dữ liệu, chấm điểm): chỉ tạo bản nháp chờ người duyệt.
- Không viết prompt "giấu" câu thử vào code (vd so khớp nguyên văn input của bộ câu thử).

## Quy ước của nhóm

- Ngôn ngữ trả lời người dùng: **tiếng Việt** (cả câu trả lời của bản chạy thử lẫn tài liệu trong repo). Tên biến / hàm / nhãn viết tiếng Anh hoặc tiếng Việt không dấu kiểu `snake_case`.
- Phong cách code / đặt tên: Python, **chỉ thư viện chuẩn** (cần thêm thì ghi `requirements.txt` kèm comment lý do), script có docstring ghi cách chạy ở đầu file, seed cố định cho mọi thứ ngẫu nhiên.
- Ai duyệt thay đổi do agent tạo trước khi commit: **người đang dùng agent** tự đọc diff. Đụng `spec.md` §7, `eval/metric_spec.yaml`, `TEAMS.md` thì báo đội trưởng (Hiếu) trước.

## Bối cảnh nhóm — đọc trước khi làm (nhóm 4hackers2711 · L3A · Track E – Tài chính)

- **Bài toán:** người dùng ví (MoMo / ZaloPay) bị trừ tiền định kỳ cho gói đăng ký / dùng thử mà không biết đó là khoản gì, nên phát hiện muộn và mất thêm tiền.
- **Lát cắt (dự kiến, xem `canvas.md` dòng 5 để biết bản đã chốt):** khoản trừ định kỳ xuất hiện → **code** tìm chu kỳ và ngày trừ tiếp theo → **AI** xác định đó là dịch vụ nào (hoặc nói "không rõ") và giải thích → người dùng được cảnh báo trước lần trừ tiếp theo, kèm các bước huỷ có nguồn.
- **Ai làm gì:** `TASKS.md` (theo mã việc). **Mốc thời gian và việc đã xong:** `TIMELINE.md`.
- **Bằng chứng đã có:** `evidence/data-mining.md` (1.000 review 1★, số hẹp / rộng, trích dẫn). Bộ nhãn: `evidence/reviews/LABELS.md`. Giả thuyết: `evidence/hypothesis.md`. Khảo sát: `evidence/survey/questions.md`.

## Quy trình git

- **Làm thẳng trên `main`, không tạo nhánh.** `git pull` trước khi sửa và trước khi commit, vì mọi người cũng sửa trên GitHub web.
- Chỉ commit khi người dùng bảo. Message dạng `<khu vực>: <việc>` (vd `evidence: …`, `eval: …`, `codebase: …`), viết tiếng Việt.
- **Làm xong một việc trong `TIMELINE.md`, agent đánh dấu luôn:** `- [x] ~~<mã> · <người> · <việc>~~ ✅ <giờ> · <commit>`. Không xoá dòng, kẹt thì thêm `⚠ <lý do>`.
- Không đổi người làm hay mốc trong `TASKS.md` / `TIMELINE.md` nếu chưa được người dùng đồng ý.

## Luật riêng của nhóm (thêm vào luật chung ở trên)

- **Full text review không lên repo.** File có text review hoặc thông tin người trả lời đặt tên `raw-*` (`.gitignore` đã chặn `evidence/**/raw-*`). Chia sẻ trong nhóm qua Drive.
- **Trích dẫn review:** dùng `id` (vd `momo-147`), ngày, số sao, **tối đa 2 câu**, không có tên người viết.
- **Không dùng sao kê hay giao dịch thật của ai**, kể cả của thành viên nhóm. Data giao dịch chỉ là synthetic (`data/`, có seed, có `DATA_CARD.md`).
- **Track E:** mọi con số (số tiền, ngày trừ, chu kỳ) phải đến từ **công cụ / code**, AI không tự tính hay tự bịa. Không xin OTP / mật khẩu / số thẻ. Không tư vấn đầu tư. Việc huỷ gói chỉ là **hướng dẫn kèm link nguồn chính thức**, agent không tự huỷ.
- Nhãn do AI gắn phải ghi `nguoi_gan = AI:<model>` và có người kiểm (`evidence/reviews/human_check.py`). Ghi việc dùng AI vào `docs/ai-usage.md`.
- Số không có nguồn ghi *(tự ước tính)*. Số trong khảo sát / phỏng vấn chỉ lấy từ kết quả thật. **Không bịa** người trả lời hay trích dẫn.
