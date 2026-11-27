"""Công cụ của bài toán — NHÓM VIẾT. Điền ở guide bước 2.2 (thiết kế) và 3.2 (code).

Mỗi công cụ là một hàm Python có @tool. Docstring ghi đúng 4 ý như sơ đồ ở spec.md §4:
    tên · input · output · có tác động ra ngoài không (gửi tin, sửa dữ liệu, chấm điểm…)
Khung tự ghi mỗi lần gọi công cụ vào trace (tên, input, output rút gọn, thời gian, lỗi).

Số công cụ, kiểu công cụ do thiết kế của nhóm quyết định — có bài chỉ cần một công cụ tra cứu.
Công cụ có tác động ra ngoài: KHÔNG tự làm. Trả về bản nháp chờ người duyệt (guide bước 2.2, "chỗ người duyệt").
Dữ liệu công cụ đọc (bài mẫu, thông báo mẫu, lịch…): để trong data/ và mô tả ở data/DATA_CARD.md.
"""
import csv
import re
import unicodedata
from calendar import monthrange
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path

from tracing import tool, TOOLS  # noqa: F401  (TOOLS: danh sách công cụ đã đăng ký, dùng khi viết vòng lặp agent)


DATA_DIR = Path(__file__).resolve().parents[1] / "data"
MERCHANT_ALIASES = (
    (re.compile(r"spotify(?: .*)?"), "spotify"),
    (re.compile(r"netflix(?: .*)?"), "netflix"),
    (re.compile(r"(?:openai )?chatgpt(?: .*)?"), "chatgpt"),
    (re.compile(r"(?:evn.* )?tien dien(?: .*)?|evnhanoi hd"), "electricity"),
)
BILLING_PREFIXES = (
    "apple com bill", "chatgpt", "electricity", "google", "netflix", "paypal",
    "spotify", "tt dv gtgt",
)
MIN_PAID_CHARGES = 3
DUPLICATE_WINDOW = timedelta(minutes=2)


@dataclass(frozen=True)
class Charge:
    tx_id: str
    time: datetime
    description: str
    amount_vnd: int


@dataclass(frozen=True)
class Cadence:
    unit: str
    nominal_days: int
    next_date: date


def _words(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value.casefold()).replace("đ", "d")
    plain = "".join(char for char in normalized if not unicodedata.combining(char))
    return " ".join(re.findall(r"[a-z0-9]+", plain))


def _merchant_key(description: str) -> str:
    words = _words(description)
    for pattern, merchant in MERCHANT_ALIASES:
        if pattern.fullmatch(words):
            return merchant
    return words


def _split_duplicates(charges: list[Charge]) -> tuple[list[Charge], list[list[Charge]]]:
    by_amount = defaultdict(list)
    for charge in charges:
        if charge.amount_vnd > 0:
            by_amount[charge.amount_vnd].append(charge)

    duplicates = []
    for same_amount in by_amount.values():
        run = []
        for charge in same_amount:
            if run and charge.time - run[-1].time > DUPLICATE_WINDOW:
                if len(run) > 1:
                    duplicates.append(run)
                run = []
            run.append(charge)
        if len(run) > 1:
            duplicates.append(run)

    duplicate_ids = {charge.tx_id for run in duplicates for charge in run}
    return [charge for charge in charges if charge.tx_id not in duplicate_ids], duplicates


def _cadence(charges: list[Charge]) -> Cadence | None:
    days = [charge.time.date() for charge in charges if charge.amount_vnd > 0]
    if len(days) < MIN_PAID_CHARGES:
        return None

    months = [day.year * 12 + day.month - 1 for day in days]
    anchor = max(day.day for day in days)
    if all(right - left == 1 for left, right in zip(months, months[1:])) and all(
        day.day == min(anchor, monthrange(day.year, day.month)[1]) for day in days
    ):
        year, month_index = divmod(months[-1] + 1, 12)
        month = month_index + 1
        next_date = date(year, month, min(anchor, monthrange(year, month)[1]))
        return Cadence("month", 30, next_date)

    gaps = {(right - left).days for left, right in zip(days, days[1:])}
    if len(gaps) == 1:
        days_apart = gaps.pop()
        if days_apart >= 2:
            return Cadence("days", days_apart, days[-1] + timedelta(days=days_apart))
    return None


def _candidate(
    charges: list[Charge], source: str, evidence_status: str,
    as_of_date: date, cadence: Cadence | None = None, *, essential: bool = False,
) -> dict:
    last = charges[-1]
    return {
        "evidence_status": evidence_status,
        "last_date": last.time.date().isoformat(),
        "amount_vnd": last.amount_vnd,
        "next_date": (
            cadence.next_date.isoformat() if cadence and cadence.next_date >= as_of_date else None
        ),
        "cycle_unit": cadence.unit if cadence else None,
        "cycle_days": cadence.nominal_days if cadence else None,
        "source": source,
        "essential_bill": essential,
        "tx_ids": [charge.tx_id for charge in charges],
        "descriptions": list(dict.fromkeys(charge.description for charge in charges)),
    }


@tool
def detect_recurring(transactions: list[dict], as_of_date: str | date) -> list[dict]:
    """Phát hiện chu kỳ từ các dòng CSV của một người dùng và ngày chạy ISO.

    Trả các cụm theo ngày trừ gần nhất. `evidence_status` là `recurring`,
    `insufficient_history` hoặc `possible_duplicate`. `amount_vnd` là số đã
    trừ gần nhất. Với `cycle_unit="month"`, `cycle_days=30` là số danh nghĩa
    và `next_date` tính theo lịch. Không dự báo ngày đã qua. Không tác động ra ngoài.
    """
    cutoff = date.fromisoformat(as_of_date) if isinstance(as_of_date, str) else as_of_date
    if len({row["user_id"] for row in transactions}) > 1:
        raise ValueError("detect_recurring chỉ nhận lịch sử của một người dùng")

    groups = defaultdict(list)
    seen_ids = set()
    for row in transactions:
        if row["status"] != "thanh_cong":
            continue
        timestamp = datetime.fromisoformat(row["time"])
        if timestamp.date() > cutoff:
            continue
        tx_id = row["tx_id"]
        amount = int(row["amount_vnd"])
        merchant = _merchant_key(row["description"])
        if amount < 0 or not merchant or tx_id in seen_ids:
            continue
        seen_ids.add(tx_id)
        # Apple dùng cùng một mô tả trên sao kê cho nhiều gói.
        apple_amount = amount if merchant == "apple com bill" else None
        groups[merchant, row["source"], apple_amount].append(
            Charge(tx_id, timestamp, row["description"], amount)
        )

    candidates = []
    for (merchant, source, _), charges in groups.items():
        ordered = sorted(charges, key=lambda charge: (charge.time, charge.tx_id))
        remaining, duplicate_runs = _split_duplicates(ordered)
        essential = merchant == "electricity"
        for run in duplicate_runs:
            candidates.append(_candidate(run, source, "possible_duplicate", cutoff, essential=essential))

        cadence = _cadence(remaining)
        if cadence:
            candidates.append(_candidate(remaining, source, "recurring", cutoff, cadence, essential=essential))
        elif remaining and any(
            merchant == prefix or merchant.startswith(prefix + " ") for prefix in BILLING_PREFIXES
        ) and any(charge.amount_vnd > 0 for charge in remaining):
            candidates.append(_candidate(remaining, source, "insufficient_history", cutoff, essential=essential))

    return sorted(candidates, key=lambda item: (item["last_date"], item["tx_ids"][-1]), reverse=True)


@tool
def get_charge_facts(series: dict, charges: list[dict]) -> dict:
    """Trả số tiền và ngày dùng trong câu trả lời, từ một chuỗi và các giao dịch của chuỗi.

    Đầu ra giữ gọn để trace ghi đủ. Công cụ chỉ tính trên dữ liệu đầu vào.
    """
    facts = {key: series[key] for key in ("amount_vnd", "last_date", "next_date")}
    paid_rows = [row for row in charges if int(row["amount_vnd"]) > 0]
    amounts = [int(row["amount_vnd"]) for row in paid_rows]
    price_levels = set(amounts)
    if len(price_levels) < 2:
        return facts
    if len(price_levels) == 2 and amounts == sorted(amounts, key=amounts.index):
        change = next(index for index, amount in enumerate(amounts) if amount != amounts[0])
        facts.update(old_amount_vnd=amounts[0], new_amount_vnd=amounts[change],
                     change_date=paid_rows[change]["time"][:10])
    else:
        facts.update(min_amount_vnd=min(price_levels), max_amount_vnd=max(price_levels))
    return facts


@tool
def lookup_renewal_schedule(user_id: str, tx_id: str, as_of_date: str) -> dict | None:
    """Tra lịch gia hạn giả lập theo mã người dùng, mã giao dịch và ngày mô phỏng.

    Trả lịch còn hiệu lực, kênh thanh toán và mã phiếu nguồn. Trả None nếu
    thiếu căn cứ hoặc trùng phiếu. Công cụ chỉ đọc CSV cục bộ.
    """
    cutoff = date.fromisoformat(as_of_date)
    with (DATA_DIR / "renewal_schedules.csv").open(encoding="utf-8", newline="") as file:
        matches = [
            row for row in csv.DictReader(file)
            if (row["user_id"], row["tx_id"]) == (user_id, tx_id)
            and row["source_ref"].strip()
            and date.fromisoformat(row["observed_on"]) <= cutoff <= date.fromisoformat(row["next_date"])
        ]
    if len(matches) != 1:
        return None
    row = matches[0]
    return {
        "next_date": row["next_date"],
        "cycle_unit": row["cycle_unit"],
        "cycle_days": int(row["cycle_days"]),
        "renewal_channel": row["channel"],
        "renewal_source": row["source_ref"],
    }


@tool
def lookup_cancel_guide(payment_channel: str) -> dict | None:
    """Tra kênh thanh toán đã xác minh trong bảng hướng dẫn hủy cục bộ.

    Input là mã kênh, tên dịch vụ hoặc bí danh trong bảng. Output gồm tên,
    các bước, URL chính thức và ngày kiểm tra, hoặc None khi không có. Không
    tác động ra ngoài và không hủy thay người dùng.
    """
    key = _words(payment_channel)
    if not key:
        return None
    with (DATA_DIR / "cancel_guides.csv").open(encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            names = [row["channel"], row["service"], *row["aliases"].split("|")]
            if key in {_words(name) for name in names}:
                return {
                    "channel": row["channel"],
                    "service": row["service"],
                    "official_url": row["official_url"],
                    "checked_on": row["checked_on"],
                    "steps": row["steps"].split("|"),
                }
    return None


@tool
def search_example(query: str) -> list:
    """(ví dụ — thay bằng công cụ của nhóm) Tra dữ liệu mẫu theo câu hỏi.
    Input: câu hỏi (str). Output: danh sách đoạn {"code", "text"}. Không tác động ra ngoài."""
    return [{"code": "VD-1", "text": "(ví dụ) đoạn dữ liệu giả — thay bằng dữ liệu thật của bài toán"}]
