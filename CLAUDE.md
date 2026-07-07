# CLAUDE.md — 事業管理本部

## オーナー
**せいさん**

---

## AIが最初にやること（必須・この順番を守る）

```
Layer 0 — 固定ルール（必須）
  1. rules/core_rules.md

Layer 1 — 現状把握（必須）
  2. context/decision_log.md
  3. context/project_context.md
  4. LATEST.md

Layer 2 — タスクに応じて参照
  5. context/business_models.md  ← 数字が必要なとき
  6. context/GLOSSARY.md         ← 用語・定数の確認
  7. ROADMAP.md                  ← フェーズ確認
  8. 該当する作業ファイル
```

**この順番を守らずに作業を始めない。Decisions override logs.**

---

## 読まなくていいフォルダ

**`fc/org/` 以下のREADMEはAIが読む必要なし。**
組織図は人間向けの参照資料。AIはcontext/以下を読めば動ける。

---

## 事業構造

2事業は**並列関係**。主従・優劣なし。違いは法人格のみ。

| 事業 | 業態 | 法人格 | 状態 |
|---|---|---|---|
| **スンドゥブ田中家** | 韓国風スンドゥブ専門店（中目黒） | 法人化予定 | 卸販売展開中・FC開発中 |
| **Ye Malthouse** | イギリス風パブ（中目黒） | 個人事業主継続 | 開業済み・DX推進中 |

---

## AI三銃士

| 名前 | 正体 | 主な役割 |
|---|---|---|
| **クロちゃん** | Claude | ファイル作成・GitHub管理・契約書・マニュアル・実装 |
| **ぐぷちゃん** | ChatGPT | 戦略立案・FCモデル設計・事業計画・交渉戦略 |
| **ゲンちゃん** | Gemini | 財務分析・市場分析・グラフ・KPIレポート |

連携フロー：せいさん → ぐぷちゃん → クロちゃん → ゲンちゃん → せいさん

---

## 優先案件

1. **FCモデル完成** — 新丸子パイロット検証中（Go/No-Go：2026年10月）
2. **dropログ（XRPL）** — XRP Ledgerを使ったdropログシステム
3. **.nkm street magazine** — 中目黒エリアのストリートマガジン
4. **上目黒不動産評価** — 上目黒エリアの不動産評価

---

## リポジトリ構造

```
sundubu-ai-context/
├── rules/
│   └── core_rules.md          ← Layer 0：固定ルール
├── context/
│   ├── decision_log.md        ← Layer 1：確定事項の記録
│   ├── project_context.md     ← Layer 1：事業・三銃士の定義
│   ├── business_models.md     ← Layer 2：ビジネスモデル・定数
│   └── GLOSSARY.md            ← Layer 2：用語集・定数
├── CLAUDE.md                  ← 本ファイル
├── LATEST.md                  ← Layer 1：現在地スナップショット
├── ROADMAP.md                 ← Layer 2：Phase 1〜3
├── docs/                      ← 設計・会議・分析文書
├── logs/                      ← デイリーログ・引き継ぎ文書
│   └── archive/               ← 月次アーカイブ（3ヶ月保持）
├── fc/
│   ├── fc_constitution.md     ← FC憲法
│   ├── org/                   ← 【AIは読まない】人間向け組織図
│   └── pilot/shin_maruko/     ← パイロット資料
├── core/                      ← スンドゥブ田中家 コア情報
├── cost/                      ← 原価・コスト管理
└── ye-malthouse/              ← Ye Malthouse 全般
```

---

## 基本原則

- 2事業は並列。どちらが上位でもない
- 法人格の違いを踏まえ、税務・法務処理は別管理
- AI-SEO・AI-Ops は横断部署としてコストを両事業に按分
- 意思決定はcontext/decision_log.mdに記録し、AIが前提を忘れない状態を維持
- FC憲法（`fc/fc_constitution.md`）はスンドゥブ田中家モデルの最上位ドキュメント

---

## リポジトリパス（Mac mini ローカル）

| リポジトリ | ローカルパス |
|---|---|
| sundubu-ai-context | /Users/seize/sundubu-ai-context |
| ops-log | /Users/seize/ops-log |
| The Garage | /Users/seize/Google Drive/My Drive/The Garage |


---

## ログpush定型フロー

### 運用ルール
会話終了時にクロちゃん（チャット）がログを生成。
CodeがそれをpushするのがDecisionです。

### リポジトリパス（Mac mini ローカル）

| リポジトリ | ローカルパス |
|---|---|
| sundubu-ai-context | /Users/seize/sundubu-ai-context |
| ops-log | /Users/seize/ops-log |
| The Garage | /Users/seize/Google Drive/My Drive/The Garage |

### Codeへの定型指示文

以下のログを ops-log にpushして。

ファイルパス：logs/daily/YYYY-MM-DD/log.md
既存ファイルは上書き。コンフリクトは--oursで解決。

内容：
[ここにクロちゃんが生成したログを貼る]


---

## CURRENT STATE（2026-04-12 更新）

### 上目黒物件
- フェーズ：ハイブリッド戦略（取得6,000万 or 賃貸並行）
- 判断フレーム：「壊れないか」のみ
- 目黒信金：✕（保全NG）
- 城南信金：✕（案件NG・「買うより借りた方がいい」）
- さわやか信金：条件待ち（主戦場）
- 藤田（野村不動産）：接触済み・静観中
- 次の一手：さわやか正式条件確認・藤田から地主温度感待ち

### スンドゥブFC
- フェーズ：鍋エンジンモデル確定・営業未展開
- 収益モデル：1鍋粗利57%・本部粗利¥2,000/鍋
- 30店舗時本部利益：約200万円/月
- 新丸子：面談未実施
- 営業資料：鍋エンジンモデルへの更新未完了
- 次の一手：資料更新→新丸子面談

### 評価OS（スタッフ管理）
- フェーズ：clean再構築中（途中）
- 構造：raw（不可侵）→clean（再構築中）→drop_log（神聖領域）
- タイミー：これから本格運用
- 次の一手：clean1行目完全通過→全行展開

### 三銃士運用
- ぐぷちゃん：戦略・判断
- ゲンちゃん：分析・検証
- クロちゃん（チャット）：ログ生成・構造化
- クロちゃん（Code）：実装・push
- ログ：ops-logに毎日push（新フォーマット：What happened/Decisions/Why/Next actions）
