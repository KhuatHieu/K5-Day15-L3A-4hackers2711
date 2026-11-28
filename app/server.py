"""App demo có giao diện web cho bản chạy thử — chỉ dùng thư viện chuẩn của Python.

Cách chạy (từ thư mục gốc repo):
    python app/server.py              # mở http://127.0.0.1:8000
    python app/server.py --port 8080

App KHÔNG thay `python run.py`: nó gọi đúng `answer(text)` trong codebase/agent.py,
nên câu trả lời giống hệt bản chạy thử dòng lệnh, eval và simulate.
- Lịch sử giao dịch: data/transactions.csv (synthetic, xem data/DATA_CARD.md).
- Danh sách khoản định kỳ ở màn hình chính: gọi thẳng công cụ detect_recurring /
  lookup_renewal_schedule (code, không gọi model).
- Hỏi AI: POST /api/ask → answer(text); trả kèm tóm tắt trace (số lần gọi model,
  công cụ, token lấy từ usage của API) để thấy chỗ nào code làm, chỗ nào AI làm.
- Bảng giá công khai: data/public_prices.csv (giá niêm yết thật, có link nguồn và ngày xem).
Không ghi file nào, không gửi gì ra ngoài ngoài lời gọi model của codebase/ai.py.
"""
import argparse
import csv
import json
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
STATIC = Path(__file__).resolve().parent / "static"
sys.path.insert(0, str(ROOT / "codebase"))

import tracing  # noqa: E402
from agent import AS_OF, WARN_DAYS, answer, days_until  # noqa: E402
from tools import detect_recurring, lookup_renewal_schedule  # noqa: E402

LOCK = threading.Lock()  # tracing giữ trạng thái chung: mỗi lần chỉ chạy một lượt hỏi
MAX_TEXT = 500


def read_csv(name):
    with (ROOT / "data" / name).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


TRANSACTIONS = read_csv("transactions.csv")
TRUTH = read_csv("recurring_truth.csv")
PRICES = read_csv("public_prices.csv")


def users():
    personas = {}
    for row in TRUTH:
        personas.setdefault(row["user_id"], row["persona"])
    counts = {}
    for row in TRANSACTIONS:
        counts[row["user_id"]] = counts.get(row["user_id"], 0) + 1
    return [{"user_id": u, "persona": personas.get(u, ""), "transactions": n} for u, n in sorted(counts.items())]


def transactions(user_id):
    rows = [r for r in TRANSACTIONS if r["user_id"] == user_id]
    return sorted(rows, key=lambda r: r["time"], reverse=True)


def price_matches(descriptions):
    text = " ".join(descriptions).lower()
    return [p for p in PRICES if any(k.strip() and k.strip() in text for k in p["match_keywords"].split("|"))]


def recurring(user_id):
    """Giống bước 3–4 của agent.answer_in_scope: code tìm chu kỳ, bổ sung phiếu gia hạn giả lập. Không gọi model."""
    txs = [r for r in TRANSACTIONS if r["user_id"] == user_id]
    if not txs:
        return []
    with LOCK:
        series = detect_recurring(txs, AS_OF)
        for s in series:
            if s["evidence_status"] == "insufficient_history" and s["amount_vnd"] > 0:
                schedule = lookup_renewal_schedule(user_id, s["tx_ids"][-1], AS_OF)
                if schedule:
                    s.update(schedule)
    out = []
    for s in series:
        d = days_until(s["next_date"], AS_OF) if s.get("next_date") else None
        s["days_left"] = d
        s["warn"] = d is not None and 0 <= d <= WARN_DAYS
        s["public_prices"] = price_matches(s["descriptions"])
        out.append(s)
    out.sort(key=lambda s: (s["days_left"] is None, s["days_left"] if s["days_left"] is not None else 0))
    return out


def ask(text):
    text = (text or "").strip()[:MAX_TEXT]
    with LOCK:
        tracing.begin("app")
        try:
            result = answer(text)
            error = None
        except Exception as e:  # lỗi model (hết lượt, mất mạng…) → báo lên UI, không sập server
            result, error = {"output": ""}, "%s: %s" % (type(e).__name__, e)
        summary, events = tracing.end()
    steps = []
    for e in events:
        if e["kind"] == "tool":
            steps.append({"kind": "code", "name": e["name"], "latency_s": e.get("latency_s")})
        elif e["kind"] == "model":
            steps.append({"kind": "ai", "name": e.get("model") or e["name"], "latency_s": e.get("latency_s"),
                          "tokens_in": e.get("tokens_in"), "tokens_out": e.get("tokens_out"),
                          "output": e.get("output")})
        elif e["kind"] == "note":
            steps.append({"kind": "note", "name": e["text"]})
    return {"output": result.get("output", ""), "error": error, "summary": summary, "steps": steps}


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        data = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        url = urlparse(self.path)
        q = parse_qs(url.query)
        user = (q.get("user") or [""])[0]
        if url.path == "/api/meta":
            return self._send(200, {"as_of": AS_OF, "warn_days": WARN_DAYS, "users": users()})
        if url.path == "/api/transactions":
            return self._send(200, transactions(user))
        if url.path == "/api/recurring":
            return self._send(200, recurring(user))
        if url.path == "/api/prices":
            return self._send(200, PRICES)
        name = "index.html" if url.path in ("/", "") else url.path.lstrip("/")
        path = (STATIC / name).resolve()
        if STATIC not in path.parents or not path.is_file():
            return self._send(404, {"error": "not found"})
        ctype = {".html": "text/html", ".js": "text/javascript", ".css": "text/css"}.get(path.suffix, "text/plain")
        return self._send(200, path.read_bytes(), ctype + "; charset=utf-8")

    def do_POST(self):
        if urlparse(self.path).path != "/api/ask":
            return self._send(404, {"error": "not found"})
        length = min(int(self.headers.get("Content-Length") or 0), 10_000)
        try:
            payload = json.loads(self.rfile.read(length) or b"{}")
        except json.JSONDecodeError:
            return self._send(400, {"error": "JSON không hợp lệ"})
        return self._send(200, ask(payload.get("text", "")))

    def log_message(self, fmt, *args):  # gọn log: chỉ in lượt hỏi AI
        if "/api/ask" in (args[0] if args else ""):
            sys.stderr.write("%s\n" % (fmt % args))


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", type=int, default=8000)
    a = p.parse_args()
    server = ThreadingHTTPServer((a.host, a.port), Handler)
    print("App demo: http://%s:%d  (Ctrl+C để dừng)" % (a.host, a.port))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
