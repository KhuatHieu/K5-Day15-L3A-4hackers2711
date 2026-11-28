"""Tính và cập nhật báo cáo K4 bằng thư viện chuẩn.

Chạy từ gốc repo: python cost/build_k4.py
Đơn giá/câu do Thông cung cấp ngày 28/11/2026; điểm từ eval/run-2.csv.
Không gọi API, không sửa CSV/trace đã chạy hoặc cấu hình mô phỏng K1.
"""

import csv
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COST_PER_QUESTION = Decimal("0.00093678")
MODEL = "gpt-6.2-sol"
RUN_ID = "run-2@20261128-113802"
START = "<!-- K4:START -->"
END = "<!-- K4:END -->"


def main():
    """Kiểm điểm đã lưu, tính ba kịch bản và ghi phần K4 của báo cáo."""
    with (ROOT / "eval/run-2.csv").open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    if len(rows) != 23 or len({row["id"] for row in rows}) != 23:
        raise ValueError("Lượt 2 phải có 23 câu duy nhất.")
    if any((row["model"] != MODEL and not (row["model"] == "" and row["model_calls"] == "0"))
           or row["run_id"] != RUN_ID or row["error"] for row in rows):
        raise ValueError("Model, run ID hoặc trạng thái API lượt 2 không khớp.")
    passed = sum(row["pass"] == "1" for row in rows)
    rate = Decimal(passed) / len(rows)
    if passed != 23:
        raise ValueError("Điểm lượt 2 khác 23/23; cần rà lại đầu vào K4.")
    frequency = Decimal(12 * 1 + 13 * 4 + 8 * 12) / 33
    per_person = frequency * COST_PER_QUESTION
    output = []
    for label, users in (("thấp", 3000), ("cơ sở", 30000), ("cao", 300000)):
        sessions = users * frequency
        output.append(f"| {label} | {users:,} | {sessions:,.6f} | ${sessions * COST_PER_QUESTION:,.6f} |")
    per_saved_hour = per_person / (Decimal(134) / 1000)
    report = f"""{START}
## Chốt K4/S2 · 28/11/2026 · {MODEL}

- **Đầu vào được Thông cung cấp để chốt:** **${COST_PER_QUESTION}/câu**. Đây là đơn giá bình quân do người dùng xác nhận, không phải kết quả mô phỏng GPT 50 phiên mới. Một phiên trong dự toán này có một câu; áp cùng đơn giá bình quân cho cả ba persona *(tự ước tính)*.
- **Chất lượng cùng model:** **{passed}/{len(rows)} ({rate:.0%})**, run ID `{RUN_ID}`; đối chiếu [CSV lượt 2](../eval/run-2.csv), [trace](../traces/run-2.jsonl) và [báo cáo đánh giá](../eval/report.md). Tỉ lệ trên bộ câu thử không bảo đảm tỉ lệ thực tế.
- **Chi phí/task thành công = chi phí/câu ÷ tỉ lệ đạt = ${COST_PER_QUESTION} ÷ {passed}/{len(rows)} = ${COST_PER_QUESTION / rate:.8f}.** Không dùng tỉ lệ không lỗi API của Gemini làm điểm chất lượng GPT.
- **Quy mô công khai:** MoMo công bố **hơn 30 triệu người dùng** trong [thông cáo ngày 09/06/2026](https://www.momo.vn/tin-tuc/thong-cao-bao-chi/momo-dong-hanh-ngay-tai-chinh-so-2026-khang-dinh-8835), kiểm lại 28/11/2026. Chọn nền 30 triệu; tiếp cận 0,01% / 0,1% / 1% *(tự ước tính)*. Không cộng người dùng ZaloPay vì chưa loại trùng.
- **Tần suất:** trọng số 12/33, 13/33, 8/33 từ khảo sát tạm câu 4; lần lượt 1, 4, 12 phiên/người/tháng *(tự ước tính)*, xem [personas.yaml](personas.yaml). Trung bình = (12 × 1 + 13 × 4 + 8 × 12) / 33 = **{frequency:.9f} câu/người/tháng**. Tần suất sử dụng sản phẩm chưa được khảo sát đo trực tiếp.

```text
Người sử dụng = 30.000.000 × tỉ lệ tiếp cận giả định
Câu/tháng = người sử dụng × (12 × 1 + 13 × 4 + 8 × 12) / 33
USD/tháng = câu/tháng × 0.00093678
USD/người/tháng = (160 / 33) × 0.00093678
```

| Kịch bản | Người (tự ước tính) | Câu/tháng (tự ước tính) | Chi phí model USD/tháng |
|---|---:|---:|---:|
{chr(10).join(output)}

**Chi phí model/người/tháng: ${per_person:.9f}**, giống nhau ở ba quy mô vì dùng chung tần suất và đơn giá. Chỉ làm tròn khi hiển thị; số câu lẻ là kỳ vọng. Nếu tần suất tăng gấp đôi thì chi phí tháng tăng gấp đôi. Nếu tỉ lệ đạt thực tế giảm còn 90% thì chi phí/task thành công thành **${COST_PER_QUESTION / Decimal('0.9'):.8f}**, chưa tính retry.

### So với impact §2 và kết luận S2

§2 nêu tổn thất tạm **58 triệu đồng + 134 giờ/1.000 người/tháng**, tương đương **58.000 đồng + 0,134 giờ/người/tháng**; phần không đòi lại được khoảng **47.000 đồng/người/tháng**. Đây là tổn thất từ mẫu khảo sát tạm, chưa phải lợi ích sản phẩm đã chứng minh. Mức CP1 8,3 triệu đồng/1.000 người/tháng tương đương 8.300 đồng/người/tháng, cũng là giả định tham chiếu.

Chi phí model **${per_person:.9f}/người/tháng** và tổn thất tiền ở §2 khác đơn vị, nên chưa tính ROI tiền hoặc tỉ lệ lợi ích/chi phí. Không quy đổi sang VND. Có thể so theo **ngưỡng giá trị thời gian**: nếu tiết kiệm được toàn bộ 0,134 giờ thì tiền model hòa vốn khi một giờ của người dùng được định giá ít nhất **${per_saved_hour:.6f}/giờ**; nếu chỉ tiết kiệm 10% thì ngưỡng là **${per_saved_hour / Decimal('0.1'):.6f}/giờ** *(tự ước tính về mức tiết kiệm)*. Công thức: USD/người/tháng ÷ (0,134 giờ × phần thời gian thực sự tiết kiệm).

**Đáng làm không: đáng thử nghiệm tiếp với chi phí model khoảng ${per_person:.6f}/người/tháng và chất lượng bộ thử 23/23; chỉ kết luận hiệu quả kinh tế sau khi đo thời gian/tiền thực sự tiết kiệm và tổng chi phí vận hành.** Chưa gồm hosting, lưu trữ, gửi cảnh báo, thuế, retry và công người duyệt. Cảnh báo chỉ có thể giúp tránh lần trừ tương lai, không hoàn lại khoản đã mất.

Tái lập phép tính bằng `python cost/build_k4.py`; dùng Decimal, không gọi API và không sửa kết quả chạy. Phần K1 Gemini bên dưới được giữ làm bằng chứng lịch sử; lệnh `build_estimate.py` tạo lại phần K1, sau đó chạy `build_k4.py` để chèn lại kết quả chốt này.
{END}
"""
    path = ROOT / "cost/cost-estimate.md"
    content = path.read_text(encoding="utf-8")
    if START in content:
        before, rest = content.split(START, 1)
        _, after = rest.split(END, 1)
        content = before + report.rstrip() + after
    else:
        title, body = content.split("\n", 1)
        body = body.replace("> Chưa thay thế kết quả CP4 với đúng model và tỉ lệ đạt lượt 2.",
                            "> Phần Gemini K1 dưới đây là lịch sử; kết quả chốt CP4 ở phần K4/S2 phía trên.")
        content = title + "\n\n" + report + "\n## Bằng chứng K1 Gemini (27/11/2026)\n" + body
    path.write_text(content, encoding="utf-8")
    print(f"K4: {passed}/{len(rows)}; USD/task={COST_PER_QUESTION / rate:.8f}; USD/user/month={per_person:.9f}")


if __name__ == "__main__":
    main()
