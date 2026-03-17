"""
scripts/drop_candidate_generator/loader.py

ログ取得・正規化モジュール。

契約:
  - timestampは必ずISO8601 (YYYY-MM-DDTHH:MM:SS) に正規化して返す
  - CSVは信用しない。Parser側で正規化する
  - fee: CSVにfee列があれば使用、なければ gross - net で計算
  - 存在しないファイルは空リストで返す（エラーで止めない）
"""

import json
import csv
import os
import re
from datetime import datetime
from typing import Optional

_TS_FORMATS = [
    "%Y-%m-%dT%H:%M:%S",
    "%Y-%m-%dT%H:%M",
    "%Y/%m/%d %H:%M:%S",
    "%Y/%m/%d %H:%M",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d %H:%M",
]

def normalize_timestamp(raw):
    if not raw:
        return None
    raw = raw.strip()
    for fmt in _TS_FORMATS:
        try:
            dt = datetime.strptime(raw, fmt)
            return dt.strftime("%Y-%m-%dT%H:%M:%S")
        except ValueError:
            continue
    return None

def extract_time_hhmm(timestamp):
    if not timestamp:
        return None
    m = re.search(r"T(\d{2}:\d{2})", timestamp)
    return m.group(1) if m else None

def load_delivery_orders(filepath):
    if not os.path.exists(filepath):
        return []
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".json":
        with open(filepath, encoding="utf-8") as f:
            records = json.load(f)
        return [_normalize_delivery_record(r) for r in records]
    elif ext == ".csv":
        records = []
        with open(filepath, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                records.append(_normalize_delivery_record(dict(row)))
        return records
    return []

def _normalize_delivery_record(r):
    ts = normalize_timestamp(r.get("timestamp", ""))
    gross = _to_number(r.get("gross", 0))
    net = _to_number(r.get("net", 0))
    if "fee" in r and r["fee"] not in ("", None):
        fee = _to_number(r["fee"])
    else:
        fee = gross - net
    return {
        "date": r.get("date", ts[:10] if ts else ""),
        "timestamp": ts,
        "platform": r.get("platform", "").lower().strip(),
        "order_id": r.get("order_id", ""),
        "item": r.get("item", ""),
        "qty": int(_to_number(r.get("qty", 1))),
        "gross": gross,
        "fee": fee,
        "net": net,
        "category": r.get("category"),
        "delay_flag": _to_bool(r.get("delay_flag")),
        "cancel_flag": _to_bool(r.get("cancel_flag")),
    }

_VALID_EVENT_TYPES = {
    "training", "peak_support", "recovery",
    "handoff", "solo_operation", "issue_response",
}

def load_staff_events(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, encoding="utf-8") as f:
        records = json.load(f)
    return [_normalize_staff_event(r) for r in records]

def _normalize_staff_event(r):
    ts = normalize_timestamp(r.get("timestamp", ""))
    return {
        "timestamp": ts,
        "time": extract_time_hhmm(ts),
        "date": ts[:10] if ts else r.get("date", ""),
        "staff": r.get("staff", ""),
        "event_type": r.get("event_type", "").strip(),
        "note": r.get("note"),
        "duration_min": _to_number(r.get("duration_min")) if r.get("duration_min") else None,
        "tag": r.get("tag", []) if isinstance(r.get("tag"), list) else [],
        "id": r.get("id", ts),
    }

def load_store_events(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, encoding="utf-8") as f:
        records = json.load(f)
    return [_normalize_store_event(r) for r in records]

def _normalize_store_event(r):
    ts = normalize_timestamp(r.get("timestamp", ""))
    return {
        "timestamp": ts,
        "time": extract_time_hhmm(ts),
        "date": ts[:10] if ts else r.get("date", ""),
        "event": r.get("event", "").strip(),
        "note": r.get("note"),
        "id": r.get("id", ts),
    }

def load_day(date, base_dir="logs"):
    ym = date[:7]
    return {
        "delivery_orders": load_delivery_orders(os.path.join(base_dir, "delivery_orders", ym, f"{date}.json")),
        "staff_events":    load_staff_events(os.path.join(base_dir, "staff_events", ym, f"{date}.json")),
        "store_events":    load_store_events(os.path.join(base_dir, "store_events", ym, f"{date}.json")),
    }

def _to_number(v):
    if v is None or v == "":
        return 0.0
    if isinstance(v, (int, float)):
        return float(v)
    cleaned = str(v).replace(",", "").replace("¥", "").replace("円", "").strip()
    try:
        return float(cleaned)
    except ValueError:
        return 0.0

def _to_bool(v):
    if v is None or v == "":
        return None
    if isinstance(v, bool):
        return v
    return str(v).lower() in ("true", "1", "yes")
