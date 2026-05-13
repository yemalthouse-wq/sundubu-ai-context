"""Window classification and aggregation (Phase 1.7, consumer: dashboard)."""

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

from scripts.pipeline.window_definitions import VERSION, WINDOW_DEFINITIONS

JST = timezone(timedelta(hours=9))

INPUT_PATH = Path("public/data/delivery_orders.json")
OUTPUT_PATH = Path("public/data/window_metrics.json")


def parse_utc_timestamp(ts):
    if not isinstance(ts, str):
        raise ValueError(f"timestamp must be str, got {type(ts).__name__}")
    normalized = ts[:-1] + "+00:00" if ts.endswith("Z") else ts
    dt = datetime.fromisoformat(normalized)
    if dt.tzinfo is None:
        raise ValueError(f"naive timestamp not allowed: {ts}")
    return dt.astimezone(timezone.utc)


def classify_window(dt_utc):
    if not isinstance(dt_utc, datetime):
        raise TypeError(f"classify_window requires datetime, got {type(dt_utc).__name__}")
    if dt_utc.tzinfo is None:
        raise ValueError("classify_window requires UTC-aware datetime")
    t_jst = dt_utc.astimezone(JST).time()
    for name, start, end in WINDOW_DEFINITIONS:
        if start <= t_jst < end:
            return name
    return "out_of_window"


def aggregate(orders):
    if not isinstance(orders, list):
        raise TypeError(f"input root must be list[dict], got {type(orders).__name__}")

    windows = {name: 0 for name, _, _ in WINDOW_DEFINITIONS}
    out_of_window = 0

    for index, order in enumerate(orders):
        if not isinstance(order, dict):
            raise TypeError(f"order at index {index} must be dict, got {type(order).__name__}")
        if "timestamp" not in order:
            raise KeyError(f"order at index {index} missing required key 'timestamp'")
        dt_utc = parse_utc_timestamp(order["timestamp"])
        label = classify_window(dt_utc)
        if label == "out_of_window":
            out_of_window += 1
        else:
            windows[label] += 1

    return {
        "version": VERSION,
        "generated_at": datetime.now(JST).isoformat(timespec="seconds"),
        "windows": windows,
        "out_of_window": out_of_window,
        "source_count": len(orders),
    }


def run():
    with INPUT_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)
    metrics = aggregate(data)
    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        json.dump(metrics, f, ensure_ascii=False, indent=2)
    print(f"generated: {OUTPUT_PATH}")
    print(f"source_count: {metrics['source_count']}")
    print(f"windows: {metrics['windows']}")
    print(f"out_of_window: {metrics['out_of_window']}")
    return metrics
