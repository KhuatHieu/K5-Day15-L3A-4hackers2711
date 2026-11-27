"""Nối model — chỗ DUY NHẤT trong bản chạy thử gọi model AI. NHÓM VIẾT phần gọi model thật.

Hợp đồng (giữ nguyên để khung đo được token):
    call_model(system: str, user: str) -> dict với 4 khoá
        "text":       str   chữ model trả về
        "model":      str   tên model đã gọi (để tra giá ở bảng giá model)
        "tokens_in":  int   số token vào, lấy từ trường usage trong phản hồi API — KHÔNG ước lượng
        "tokens_out": int   số token ra, gồm cả token suy luận / suy nghĩ nếu API tính riêng
    @model_call (từ tracing.py) tự ghi mỗi lần gọi vào trace; agent.py gọi call_model bao nhiêu lần
    cũng được, khung tự cộng token.
    Lỗi gọi model (hết lượt, sai key, mất mạng): cứ để exception bay ra — khung ghi lỗi vào cột error.

Chế độ giả (mặc định khi .env chưa có MODEL_PROVIDER, hoặc MODEL_PROVIDER=fake):
    trả một câu giả cố định, model "fake", token 0 — để luồng chạy hết từ trước CP2 (guide bước 3.2).
    Lượt `run.py eval` / `run.py simulate` chạy bằng model giả KHÔNG được tính.

Nối model thật: điền .env (chép từ .env.example), rồi viết nhánh gọi API ở dưới theo docs/connect-model.md
(có ví dụ OpenAI, Claude, model chạy trên máy, và cách nối nhà cung cấp khác). Không dán API key vào file này.
"""
import json
import os
import urllib.error
import urllib.request

from tracing import model_call

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_env(path=os.path.join(ROOT, ".env")):
    """Đọc file .env (KEY=VALUE mỗi dòng) vào biến môi trường, không ghi đè biến đã có. Khung — không cần sửa."""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env()
MODEL_PROVIDER = (os.environ.get("MODEL_PROVIDER") or "fake").strip().lower()
MODEL_NAME = (os.environ.get("MODEL_NAME") or "").strip()
API_KEY = (os.environ.get("API_KEY") or "").strip()


@model_call
def call_model(system: str, user: str) -> dict:
    if MODEL_PROVIDER == "fake":
        last = (user.strip().splitlines() or [""])[-1]
        return {"text": "[câu trả lời giả — chưa nối model] " + last[:60], "model": "fake", "tokens_in": 0, "tokens_out": 0}

    if MODEL_PROVIDER == "anthropic":
        r = call_claude(system, user)
    elif MODEL_PROVIDER == "gemini":
        r = call_gemini(system, user)
    else:
        raise NotImplementedError(
            "chưa viết phần gọi model thật cho MODEL_PROVIDER=%s trong codebase/ai.py — xem docs/connect-model.md"
            % MODEL_PROVIDER)
    return {"text": r["text"], "model": MODEL_NAME, "tokens_in": r["tokens_in"], "tokens_out": r["tokens_out"]}


SHOW_RAW = False   # đổi thành True để in nguyên phản hồi của API khi cần tìm tên trường
URL_GEMINI = "https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent"
URL_CLAUDE = "https://api.anthropic.com/v1/messages"


def call_claude(system, user):
    """Gọi Claude Messages API đúng MỘT lần (urllib, theo docs/connect-model.md mục 2.2).
    Trả về {"text", "tokens_in", "tokens_out"}. Token lấy từ usage: input_tokens / output_tokens
    (output_tokens của Claude đã gồm token suy nghĩ — Haiku 5.5 bật suy nghĩ sẵn).
    effort "low": việc của model chỉ là trả JSON nhận diện dịch vụ, không cần suy nghĩ sâu → ít token hơn."""
    body = {"model": MODEL_NAME, "max_tokens": 2048, "output_config": {"effort": "low"},
            "messages": [{"role": "user", "content": user}]}
    if system:
        body["system"] = system
    data = post_json(URL_CLAUDE, {"x-api-key": API_KEY, "anthropic-version": "2023-06-01"}, body)
    # phản hồi có thể có khối "thinking" trước khối "text" → chỉ lấy khối text
    text = "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")
    if not text:
        raise RuntimeError("Claude không trả chữ (stop_reason=%s)" % data.get("stop_reason"))
    u = data["usage"]
    return {"text": text, "tokens_in": int(u["input_tokens"]), "tokens_out": int(u["output_tokens"])}


def post_json(url, headers, body, timeout=60):
    """Gửi POST JSON, trả về JSON phản hồi. Chỉ dùng thư viện chuẩn (urllib)."""
    req = urllib.request.Request(
        url, data=json.dumps(body).encode("utf-8"), method="POST",
        headers=dict({"Content-Type": "application/json"}, **headers))
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise RuntimeError("HTTP %d: %s" % (e.code, e.read().decode("utf-8", "replace")[:300]))
    if SHOW_RAW:
        print(json.dumps(data, ensure_ascii=False, indent=2)[:3000])
    return data


def call_gemini(system, user):
    """Gọi Gemini REST API (generateContent) đúng MỘT lần. Trả về {"text", "tokens_in", "tokens_out"}.
    Token lấy từ usageMetadata: vào = promptTokenCount; ra = candidatesTokenCount + thoughtsTokenCount
    (token suy nghĩ Google tính tiền như token ra)."""
    body = {"contents": [{"role": "user", "parts": [{"text": user}]}]}
    if system:
        body["systemInstruction"] = {"parts": [{"text": system}]}
    data = post_json(URL_GEMINI % MODEL_NAME, {"x-goog-api-key": API_KEY}, body)
    cands = data.get("candidates") or []
    parts = (cands[0].get("content") or {}).get("parts", []) if cands else []
    text = "".join(p.get("text", "") for p in parts)
    if not text:
        raise RuntimeError("Gemini không trả chữ (finishReason=%s)" % (cands[0].get("finishReason") if cands else data))
    u = data.get("usageMetadata") or {}
    return {"text": text,
            "tokens_in": int(u.get("promptTokenCount", 0)),
            "tokens_out": int(u.get("candidatesTokenCount", 0)) + int(u.get("thoughtsTokenCount", 0))}
