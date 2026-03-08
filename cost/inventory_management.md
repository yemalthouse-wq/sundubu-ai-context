# Inventory Management Protocol
Sundubu Tanaka OS v0.3 / Supply Chain

## Logistics Unit
- **1 Box = 200 portions** (Soup & Ingredients)

## Consumption Speed Model
| Daily Orders | 1 Box Life Span | Replacement Cycle |
| :--- | :--- | :--- |
| 10 cups/day | 20 days | approx. 3 weeks |
| 20 cups/day | 10 days | approx. 1.5 weeks |
| **25 cups/day** | **8 days** | **approx. 1 week** |
| 40 cups/day | 5 days | approx. 5 days |

## Reordering Rule: "Safety Stock 50"
- **Trigger:** 在庫数が **50食** を切った時点で次回の200食を発注。
- **Logic:** 25杯/日の場合、残り50食は「2日分の猶予」を意味する。配送リードタイムを吸収し、欠品を未然に防ぐ。
