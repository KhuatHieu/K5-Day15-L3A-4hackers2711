# Tóm tắt mô phỏng simulate-1@20261127-215058

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 22 | 1 | 274 | 24 | 0.8 | 4.8 |
| dung_vua | 18 | 1 | 375 | 32 | 1.1 | 5.3 |
| dung_nhieu | 9 | 1 | 352 | 32 | 1.0 | 5.2 |

Tỉ lệ đạt dùng để tính: **chưa có** lượt eval chấm xong chạy bằng gemini-3.1-flash-lite. Lượt chấm gần nhất (run-1@20261127-183503) chạy bằng gpt-6.2-sol — model khác, nên KHÔNG dùng tỉ lệ đạt đó → chưa tính chi phí / task thành công. Chạy `python run.py eval` bằng đúng model này, chấm xong (`python run.py score …`) rồi chạy lại simulate.

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (3.000 người) | Chi phí / tháng — cơ sở (30.000 người) | Chi phí / tháng — cao (300.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.00012 (≈ 3 ₫) | — | — | $1.97 (≈ 51.162 ₫) | $19.68 (≈ 511.620 ₫) | $196.78 (≈ 5.116.201 ₫) | $0.00066 (≈ 17 ₫) |
| gemini-3.1-pro-preview (vào 2.0 · ra 12.0 $/1M) | $0.00099 (≈ 26 ₫) | — | — | $15.74 (≈ 409.296 ₫) | $157.42 (≈ 4.092.961 ₫) | $1,574.22 (≈ 40.929.606 ₫) | $0.0052 (≈ 136 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.0) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gemini-3.1-flash-lite. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 1/50.
- Tỷ giá: 1 USD = 26.000 ₫ (26.000 VND/USD (tự ước tính) để lập kế hoạch, không phải tỷ giá ngân hàng.).
