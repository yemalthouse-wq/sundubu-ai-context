# Restaurant OS Data Contracts

## Purpose

This document defines the canonical data contracts for the Restaurant OS.

These contracts are the single source of truth for:

- dashboard integration
- event logging
- drop candidate generation
- future analysis and review workflows

---

# Core Data Objects

The Restaurant OS currently uses four primary data objects:

1. `delivery_orders.json`
2. `staff_events.json`
3. `store_events.json`
4. `drop_candidates.json`

Future object:
5. `orders.json` (in-store / Square integration)

---

# 1. delivery_orders.json

## Purpose

Normalized delivery order data from Uber / RocketNow.

## Required Fields

| Field | Type | Required | Description |
|------|------|----------|-------------|
| date | string | yes | Order date in YYYY-MM-DD format |
| timestamp | string | yes | Full timestamp |
| platform | string | yes | `uber` or `rocketnow` |
| order_id | string | yes | Unique order reference |
| item | string | yes | Item name |
| qty | number | yes | Quantity sold |
| gross | number | yes | Gross sales amount |
| fee | number | yes | Platform fee |
| net | number | yes | Net received amount |

## Optional Fields

| Field | Type | Required | Description |
|------|------|----------|-------------|
| category | string | no | Product category |
| prep_time | number | no | Estimated prep or handling time |
| delay_flag | boolean | no | Whether order was delayed |
| cancel_flag | boolean | no | Whether order was cancelled |

## Example

```json
[
  {
    "date": "2026-03-17",
    "timestamp": "2026-03-17T19:12:00",
    "platform": "uber",
    "order_id": "UB12345",
    "item": "期間限定スタミナもつドゥブ",
    "qty": 2,
    "gross": 2960,
    "fee": 1036,
    "net": 1924
  }
]
