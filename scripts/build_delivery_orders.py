"""Phase 1.8 producer: normalize records-rooted source to list-rooted
public output, then trigger consumer aggregation.

Source : data/delivery_orders.json (dict with 'records' list).
Output : public/data/delivery_orders.json (list[dict]).
Chain  : scripts.pipeline.window.run() reads the normalized output and
         emits public/data/window_metrics.json.
"""

import json
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from scripts.pipeline.window import run as window_run

SOURCE_PATH = Path("data/delivery_orders.json")
OUTPUT_PATH = Path("public/data/delivery_orders.json")

REQUIRED_RECORD_KEYS = ("date", "store", "platform", "orders", "sales", "fee", "net")


def normalize_record(record, index):
    if not isinstance(record, dict):
        raise TypeError(f"record at index {index} must be dict, got {type(record).__name__}")
    for key in REQUIRED_RECORD_KEYS:
        if key not in record:
            raise KeyError(f"record at index {index} missing required key '{key}'")
    return {
        # synthetic timestamp for contract normalization only.
        # not real order/event time.
        "timestamp": f"{record['date']}T00:00:00+00:00",
        "platform": record["platform"],
        "store": record["store"],
        "orders": record["orders"],
        "revenue": record["sales"],
        "fee": record["fee"],
        "effective_profit": record["net"],
    }


def normalize():
    with SOURCE_PATH.open("r", encoding="utf-8") as f:
        source = json.load(f)
    if not isinstance(source, dict):
        raise TypeError(f"source root must be dict with 'records', got {type(source).__name__}")
    if "records" not in source:
        raise KeyError("source missing required key 'records'")
    records = source["records"]
    if not isinstance(records, list):
        raise TypeError(f"source['records'] must be list, got {type(records).__name__}")

    normalized = [normalize_record(r, i) for i, r in enumerate(records)]

    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        json.dump(normalized, f, ensure_ascii=False, indent=2)
    print(f"normalized: {OUTPUT_PATH} ({len(normalized)} records)")
    return normalized


if __name__ == "__main__":
    normalize()
    window_run()
