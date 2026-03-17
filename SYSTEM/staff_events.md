# SYSTEM/staff_events.md

## 概要

店舗で発生するスタッフ起点のイベントを記録するログ仕様。
評価制度（drop）の前段として、まず「何が起きたか」を残す。
自動化はしない。手動記録を基本とする。

---

## フィールド定義

| フィールド | 型 | 必須 | 説明 |
|---|---|---|---|
| `date` | string (YYYY-MM-DD) | ✅ | イベント発生日 |
| `staff` | string | ✅ | スタッフ識別名（例: `tanaka`, `yamada`）|
| `event` | string | ✅ | イベント種別（後述） |
| `drop` | string \| null | — | dropログとの紐付けID（任意） |
| `tag` | string[] | — | 補助タグ（例: `["peak", "solo"]`） |
| `note` | string \| null | — | 自由記述。文脈・経緯など |

---

## event 種別

| 値 | 意味 |
|---|---|
| `solo_op` | ワンオペ対応 |
| `new_support` | 新人フォロー |
| `peak_handle` | ピーク時対応 |
| `issue_resolve` | トラブル解決 |
| `training` | 研修・引き継ぎ |
| `other` | 上記以外（noteに詳細） |

---

## JSON例

```json
[
  {
    "date": "2026-03-17",
    "staff": "tanaka",
    "event": "solo_op",
    "drop": null,
    "tag": ["lunch", "peak"],
    "note": "ランチピーク12:00-13:30、ワンオペで完走。クレームなし。"
  }
]
```

---

## 格納パス（予定）

```
sundubu-ai-context/
└── logs/
    └── staff_events/
        └── YYYY-MM/
            └── YYYY-MM-DD.json
```

---

last updated: 2026-03-17
owner: クロちゃん（Implementation）
