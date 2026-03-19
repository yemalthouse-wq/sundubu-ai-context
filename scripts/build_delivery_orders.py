import json
import os

os.makedirs("public/data", exist_ok=True)

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
    ]
}

with open("public/data/delivery_orders.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("generated: public/data/delivery_orders.json")
