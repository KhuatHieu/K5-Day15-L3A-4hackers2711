"""Lập báo cáo chi phí từ lượt mô phỏng thật, chỉ dùng thư viện chuẩn.

Chạy từ thư mục gốc: python cost/build_estimate.py cost/simulate-1.csv
Cần giữ cost/personas.yaml đúng cấu hình của lượt chạy; không sửa CSV/trace.
Ghi cost/cost-estimate.md từ kết quả mô phỏng Gemini.
Không gọi API và không chấm chất lượng output.
"""

import csv
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re
import sys

import simulate


def write_table(path, rows):
    """Ghi bảng tính dẫn xuất, không thay đổi CSV/trace mô phỏng gốc."""
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def detailed_k1(path, rows, cfg, model):
    """Đối chiếu trace và tính USD bằng Decimal từ token nguyên, giá trong YAML."""
    trace_path = Path(simulate.ROOT) / "traces" / (path.stem + ".jsonl")
    events = [json.loads(line) for line in trace_path.read_text(encoding="utf-8").splitlines()
              if line.strip()]
    if {event["run_id"] for event in events} != {rows[0]["run_id"]}:
        raise ValueError("Run ID trong trace không khớp CSV.")
    calls = [event for event in events if event.get("kind") == "model" and not event.get("error")]
    for field in ("tokens_in", "tokens_out"):
        if sum(int(row[field]) for row in rows) != sum(event.get(field, 0) or 0 for event in calls):
            raise ValueError("Token CSV/trace lệch: " + field)
    if len(rows) < 50 or len({r["session"] for r in rows}) != len(rows):
        raise ValueError("K1 cần ít nhất 50 phiên, mã phiên không trùng.")
    million = Decimal(1_000_000)
    dec = lambda value: Decimal(str(value))
    dollar = lambda value: "$" + format(value, ".10f").rstrip("0").rstrip(".")
    price = next(item for item in cfg["prices"] if item["model"] == model)
    rate_in, rate_out = dec(price["input"]), dec(price["output"])
    session_costs = []
    for row in rows:
        input_cost = dec(row["tokens_in"]) * rate_in / million
        output_cost = dec(row["tokens_out"]) * rate_out / million
        session_costs.append({
            "run_id": row["run_id"], "session": row["session"], "persona": row["persona"],
            "status": "error" if row["error"] else "no_api_error",
            "tokens_in": row["tokens_in"], "tokens_out": row["tokens_out"],
            "input_usd": str(input_cost), "output_usd": str(output_cost),
            "total_usd": str(input_cost + output_cost),
        })
    session_path = path.with_name("session-costs-" + path.stem + ".csv")
    write_table(session_path, session_costs)
    input_total = sum(dec(row["input_usd"]) for row in session_costs)
    output_total = sum(dec(row["output_usd"]) for row in session_costs)
    total = input_total + output_total
    ok = [row for row in session_costs if row["status"] == "no_api_error"]
    ok_total = sum(dec(row["total_usd"]) for row in ok)
    per_ok = ok_total / len(ok)
    lines = [
        "### Phép tính K1 chi tiết (USD)", "",
        "Giá Flash-Lite: USD vào = token vào × %s / 1.000.000; "
        "USD ra = token ra × %s / 1.000.000; chi phí phiên = USD vào + USD ra."
        % (rate_in, rate_out), "",
        "- Toàn bộ %d phiên: tiền token vào **%s**, tiền token ra **%s**, tổng **%s**."
        % (len(rows), dollar(input_total), dollar(output_total), dollar(total)),
        "- %d phiên không lỗi API có tổng **%s** → trung bình **%s / phiên**."
        % (len(ok), dollar(ok_total), dollar(per_ok)),
        "- Trung bình trên mọi phiên, kể cả lỗi: **%s / lượt thử**. "
        "Phiên timeout không trả usage không được coi là miễn phí đã xác nhận; "
        "đây chỉ là phần token đo được." % dollar(total / len(rows)),
        "- Đã đối chiếu tổng token và run ID giữa CSV với trace; có %d mã phiên duy nhất. "
        "Bảng [chi phí từng phiên](%s) có đủ %d dòng, gồm phiên lỗi."
        % (len(rows), session_path.name, len(rows)), "",
        "| Nhóm | Phiên không lỗi / tổng | Token vào / ra (phiên không lỗi) | "
        "Tổng USD không lỗi | USD / phiên không lỗi | Tỉ lệ người | Phiên/người/tháng (tự ước tính) |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    grouped = {}
    for persona in cfg["personas"]:
        subset = [row for row in ok if row["persona"] == persona["name"]]
        all_group = [row for row in rows if row["persona"] == persona["name"]]
        if not subset:
            raise ValueError("Chưa đo được phiên không lỗi cho persona " + persona["name"])
        group_total = sum(dec(row["total_usd"]) for row in subset)
        grouped[persona["name"]] = group_total / len(subset)
        lines.append("| %s | %d/%d | %d / %d | %s | %s | %.6f%% | %s |" % (
            persona["name"], len(subset), len(all_group),
            sum(int(row["tokens_in"]) for row in subset),
            sum(int(row["tokens_out"]) for row in subset), dollar(group_total),
            dollar(grouped[persona["name"]]),
            100 * persona["share"] / cfg["total_share"], persona["uses_per_month"]))
    lines.extend([
        "", "Công thức cho mỗi kịch bản và nhóm j:", "",
        "```text",
        "Người nhóm j = tổng người × share_j / tổng share",
        "Phiên nhóm j/tháng = người nhóm j × phiên/người/tháng_j",
        "USD nhóm j/tháng = phiên nhóm j/tháng × USD/phiên không lỗi_j",
        "USD toàn kịch bản/tháng = tổng USD nhóm j/tháng",
        "```", "",
        "Tỉ lệ persona được giữ nguyên giữa ba quy mô. Các số người và phiên lẻ "
        "là kỳ vọng của mô hình, không phải đếm người thực tế. Không nhân chi phí "
        "bình quân chung với tần suất chung, vì từng nhóm có chi phí/phiên khác nhau.", "",
        "| Kịch bản | Người (tự ước tính) | Phiên/tháng kỳ vọng (tự ước tính) | "
        "USD ít | USD vừa | USD nhiều | Tổng USD/tháng Flash-Lite | "
        "Tính giá Pro trên cùng token |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ])
    scenario_rows = []
    pro = next(item for item in cfg["prices"] if item["model"] != model)
    pro_ratio_in = dec(pro["input"]) / rate_in
    pro_ratio_out = dec(pro["output"]) / rate_out
    if pro_ratio_in != pro_ratio_out:
        raise ValueError("Bảng so sánh hiện cần hai giá model có cùng hệ số vào/ra.")
    for scenario in simulate.SCENARIOS:
        scenario_total = Decimal(0)
        session_total = Decimal(0)
        components = []
        for persona in cfg["personas"]:
            users = dec(cfg["users"][scenario]) * dec(persona["share"]) / dec(cfg["total_share"])
            sessions = users * dec(persona["uses_per_month"])
            monthly = sessions * grouped[persona["name"]]
            scenario_total += monthly
            session_total += sessions
            components.append(monthly)
            scenario_rows.append({
                "run_id": rows[0]["run_id"], "scenario": scenario, "persona": persona["name"],
                "users_expected": str(users), "sessions_month_expected": str(sessions),
                "usd_per_session": str(grouped[persona["name"]]),
                "usd_month_flash_lite": str(monthly),
                "usd_month_pro_same_tokens": str(monthly * pro_ratio_in),
            })
        lines.append("| %s | %s | %.6f | %s | %s | %s | **%s** | %s |" % (
            simulate.SCENARIO_VI[scenario], cfg["users"][scenario], session_total,
            *(dollar(value) for value in components), dollar(scenario_total),
            dollar(scenario_total * pro_ratio_in)))
    scenarios_path = path.with_name("scenario-costs-" + path.stem + ".csv")
    write_table(scenarios_path, scenario_rows)
    lines.extend([
        "", "Bảng [phân rã kịch bản](%s) giữ đầy đủ số trước làm tròn. "
        "Pro có cả hai đơn giá bằng %s lần Flash-Lite nên cột so sánh bằng "
        "chi phí Flash-Lite × %s; đây không phải chi phí Pro đã đo."
        % (scenarios_path.name, pro_ratio_in, pro_ratio_in),
        "", "**K1 hoàn thành:** đã mô phỏng ít nhất 50 phiên, lưu CSV và trace, "
        "tính chi phí bằng usage API, có ba kịch bản quy mô và phép tính tái lập. "
        "Chi phí/task thành công phụ thuộc eval lượt 2 cùng model ở K4, chưa thể "
        "dùng số phiên không lỗi API làm tỉ lệ đạt chất lượng.",
    ])
    return lines


def build(path):
    cfg, warnings = simulate.load_config()
    if warnings:
        raise ValueError("Cấu hình cần xử lý: " + "; ".join(warnings))
    with path.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    if not rows or len({r["run_id"] for r in rows}) != 1:
        raise ValueError("CSV phải có đúng một run ID và ít nhất một phiên.")
    ok = [r for r in rows if not r["error"]]
    models = {m for r in rows for m in r["model"].split(", ") if m}
    if not ok or "fake" in models or len(models) != 1:
        raise ValueError("Cần một model thật, có phiên không lỗi.")
    model = next(iter(models))
    price = next(p for p in cfg["prices"] if p["model"] == model)
    if sum(int(r["tokens_in"]) + int(r["tokens_out"]) for r in rows) <= 0:
        raise ValueError("Không có usage token thật.")
    cost = lambda r: (int(r["tokens_in"]) * price["input"] +
                      int(r["tokens_out"]) * price["output"]) / 1_000_000
    avg = sum(map(cost, ok)) / len(ok)
    total = sum(map(cost, rows))
    fmt = lambda value: simulate.money(value)
    generated = path.with_name(path.stem + "-summary.md")
    summary = generated.read_text(encoding="utf-8").split("\n", 4)[4].strip()
    # Đổi cách hiển thị bản sao trong báo cáo; giữ nguyên file khung đã sinh.
    summary = re.sub(r" \(≈ [^)]* ₫\)", "", summary)
    # Chỉ lấy bảng giá tổng hợp; số liệu persona và công thức đã có ở phần chi tiết.
    summary_lines = summary.splitlines()
    table_start = next(i for i, line in enumerate(summary_lines) if line.startswith("| Model (giá)"))
    table_end = next((i for i in range(table_start, len(summary_lines))
                      if not summary_lines[i].startswith("|")), len(summary_lines))
    summary = "\n".join(summary_lines[table_start:table_end])
    grouped = {}
    for persona in cfg["personas"]:
        subset = [r for r in ok if r["persona"] == persona["name"]]
        grouped[persona["name"]] = sum(map(cost, subset)) / len(subset) if subset else avg
    per_user = sum(p["share"] / cfg["total_share"] * p["uses_per_month"] *
                   grouped[p["name"]] for p in cfg["personas"])
    detail_lines = detailed_k1(path, rows, cfg, model)
    lines = [
        "# Chi phí khi dùng thật",
        "",
        "> Báo cáo do `python cost/build_estimate.py %s` tạo từ CSV thật và cấu hình hiện tại."
        % path.as_posix(),
        "> Chưa thay thế kết quả CP4 với đúng model và tỉ lệ đạt lượt 2.",
        "",
        "## 1. Đầu vào và giả định",
        "",
        "- Model thực đo: `%s`; seed %s; %s phiên, mỗi phiên một lượt hỏi."
        % (model, cfg["seed"], len(rows)),
        "- Đầu vào được lấy mẫu từ benchmark loại `thuong` và `kho`, không phải lưu lượng "
        "khách hàng thật. Phiên được code xử lý mà không cần AI có chi phí model bằng 0; "
        "phiên cần nhiều lần gọi được cộng đủ usage. Trung bình bỏ phiên lỗi theo khung, "
        "còn tổng usage bên dưới giữ cả phần đo được trong phiên lỗi.",
        "- Persona từ khảo sát tạm, câu 4: ít 12/33 (gộp 0 và không nhớ), vừa 13/33, "
        "nhiều 8/33. Câu 3: 23 Có, 5 Không, 5 Không chắc liên kết tự động.",
        "- Tần suất 1/4/12 phiên/người/tháng **(tự ước tính)**; khảo sát chưa đo nhu cầu dùng "
        "sản phẩm. Chưa chốt mẫu ngoài nhóm và hai dòng trùng.",
        "- MoMo công bố hơn 30 triệu người dùng: "
        "[thông cáo MoMo](https://www.momo.vn/tin-tuc/thong-cao-bao-chi/"
        "momo-dong-hanh-ngay-tai-chinh-so-2026-khang-dinh-8835), xem 27/11/2026. "
        "Lấy nền 30 triệu, giả định tiếp cận 0,01% / 0,1% / 1% → "
        "3.000 / 30.000 / 300.000 người **(tự ước tính)**. Không phải khách hàng đã có; không cộng ZaloPay.",
        "- Giá [Google Standard trả phí](https://ai.google.dev/gemini-api/docs/pricing), "
        "xem 27/11/2026: Flash-Lite $0,25 vào / $1,50 ra; Pro Preview $2 vào / $12 ra "
        "trên một triệu token (prompt ≤200k). Token ra gồm thinking. Pro chỉ so sánh giá "
        "trên token Flash-Lite, chưa chạy Pro để đo token hoặc chất lượng.",
        "- Chỉ báo cáo bằng **USD**, không quy đổi tiền Việt. Chỉ tính tiền model; "
        "chưa gồm hosting, lưu trữ, gửi cảnh báo, thuế và công người duyệt.",
        "",
        "## 2. Kết quả đo và bảng do khung sinh",
        "",
        "- Run ID: `%s`. CSV: [%s](%s); trace: [%s](../traces/%s.jsonl)."
        % (rows[0]["run_id"], path.name, path.name, path.stem + ".jsonl", path.stem),
        "- Phiên không lỗi API: **%d/%d**; phiên lỗi: **%d/%d**. "
        "Đây là khả năng chạy, không phải tỉ lệ đạt chất lượng."
        % (len(ok), len(rows), len(rows) - len(ok), len(rows)),
        "- Tổng usage tất cả phiên (kể cả phần gọi thành công trong phiên lỗi): "
        "**%d token vào, %d token ra**; quy theo giá trả phí Flash-Lite: **%s**. "
        "Request lỗi không trả usage nên chưa biết có phát sinh tiền ngoài phần đo được hay không."
        % (sum(int(r["tokens_in"]) for r in rows), sum(int(r["tokens_out"]) for r in rows), fmt(total)),
        "- Trung bình mỗi phiên không lỗi: **%s**. Chi phí trên là quy đổi theo bảng giá, "
        "không phải hoá đơn thực tế nếu đang dùng free tier." % fmt(avg),
        "",
        summary,
        "",
        *detail_lines,
        "",
        "## 3. Độ nhạy và so với impact",
        "",
        "Chi phí/task thành công = chi phí/phiên ÷ tỉ lệ đạt cùng model. Chưa có eval "
        "đã chấm cho Flash-Lite; không dùng 18/20 của gpt-6.2-sol. Bảng dưới chỉ là "
        "giả định **(tự ước tính)**, chưa gồm retry:",
        "",
        "| Tỉ lệ đạt giả định | Chi phí / task thành công Flash-Lite |",
        "|---|---:|",
    ]
    lines.extend("| %d%% | %s |" % (round(rate * 100), fmt(avg / rate))
                 for rate in (0.7, 0.9, 1.0))
    lines.extend([
        "",
        "- Chi phí model / người / tháng theo persona: **%s**. "
        "Nếu toàn bộ tần suất giả định tăng gấp đôi, chi phí tháng cũng tăng gấp đôi." % fmt(per_user),
        "- Impact tạm tham chiếu `spec.md` §2, chưa quy đổi tiền tệ để so sánh trực tiếp. "
        "Đây là tổn thất ước tính từ khảo sát, không phải số tiền sản phẩm chắc chắn tiết kiệm được.",
        "- **Đáng thử tiếp về tiền model** vì chi phí model / phiên thấp; "
        "chưa kết luận hiệu quả kinh doanh trước khi có chất lượng cùng model, chi phí vận hành "
        "và dữ liệu khảo sát chốt. Các lỗi quota có thể làm người dùng lỡ cảnh báo.",
        "",
        "## 4. K0 và cách chạy lại",
        "",
        "K0: `simulate-try@20261127-214818`, 10 phiên, 8 không lỗi và 2 lỗi HTTP 429. "
        "Usage tổng 7.798 vào / 685 ra; xem [bằng chứng K0](k0-check.json). "
        "K0 dùng cấu hình cũ 1/3/5 lượt, chỉ kiểm luồng; bảng chính dùng lượt đầy đủ một lượt/phiên.",
        "",
        "```powershell",
        "$env:MODEL_NAME = 'gemini-3.1-flash-lite'",
        "python run.py check",
        "python run.py simulate --wait 4",
        "python cost/build_estimate.py cost/simulate-N.csv",
        "```",
        "",
        "Giữ đúng cấu hình `cost/personas.yaml` khi tái lập báo cáo của lượt này. "
        "Không chạy lại `--try` nếu muốn giữ nguyên file thử cũ. Lượt đủ tiếp theo tự tăng số N. "
        "Không sửa file CSV/trace đã chạy; log lỗi trước đó giữ riêng và được gitignore. "
        "Bản summary gốc có quy đổi tiền Việt do cấu hình tại thời điểm chạy; báo cáo này "
        "chỉ bỏ phần hiển thị quy đổi theo yêu cầu, không sửa dữ liệu đo hay giá USD.",
        "",
        "- SHA-256 CSV: `%s`." % hashlib.sha256(path.read_bytes()).hexdigest(),
        "- SHA-256 personas.yaml: `%s`."
        % hashlib.sha256(Path(simulate.PERSONAS).read_bytes()).hexdigest(),
    ])
    output = Path(simulate.COST_DIR) / "cost-estimate.md"
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Da ghi:", output.name)
    print("Run ID:", rows[0]["run_id"])
    print("Sessions without API error:", len(ok), "/", len(rows))
    print("USD total:", total)
    print("USD/session:", avg)
    print("USD/user/month:", per_user)
    for scenario in simulate.SCENARIOS:
        print(scenario, "users:", cfg["users"][scenario], "USD/month:",
              per_user * cfg["users"][scenario])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Cach chay: python cost/build_estimate.py cost/simulate-N.csv")
    build(Path(sys.argv[1]))
