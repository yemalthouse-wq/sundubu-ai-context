import json
import os
from datetime import datetime

OUTPUT_DIR = "public/data"
HISTORY_DIR = "public/data/history"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "delivery_orders.json")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(HISTORY_DIR, exist_ok=True)

orders = [
    {
        "item_name": "スンドゥブ",
        "qty": 3,
        "gross": 2700,
        "fee": 810,
        "delay_flag": False
    }
]

# KPI計算
gross_total    = sum(o["gross"] for o in orders)
fee_total      = sum(o["fee"]   for o in orders)
net            = gross_total - fee_total
fee_rate       = round(fee_total / gross_total, 4) if gross_total > 0 else 0
order_count    = len(orders)
item_qty_total = sum(o["qty"] for o in orders)

kpi = {
    "gross_total":    gross_total,
    "fee_total":      fee_total,
    "net":            net,
    "fee_rate":       fee_rate,
    "order_count":    order_count,
    "item_qty_total": item_qty_total
}

data = {
    "date":         "2026-03-19",
    "platform":     "uber",
    "orders":       orders,
    "kpi":          kpi,
    "generated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
}

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"generated: {OUTPUT_FILE}")

date_str = data["date"]
history_file = os.path.join(HISTORY_DIR, f"{date_str}.json")
with open(history_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"generated: {history_file}")
