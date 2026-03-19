import json
import os
from datetime import datetime

OUTPUT_DIR = "public/data"
HISTORY_DIR = "public/data/history"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "delivery_orders.json")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(HISTORY_DIR, exist_ok=True)

data = {
    "date": "2026-03-19",
    "platform": "uber",
    "orders": [
        {
            "item_name": "スンドゥブ",
            "qty": 3,
            "gross": 2700,
            "fee": 810,
            "delay_flag": False
        }
    ],
    "generated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
}

date_str = data["date"]

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"generated: {OUTPUT_FILE}")

history_file = os.path.join(HISTORY_DIR, f"{date_str}.json")
with open(history_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"generated: {history_file}")
