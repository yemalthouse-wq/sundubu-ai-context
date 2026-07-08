> **[FROZEN 2026-07-08]** 本ファイルは凍結（decision_log「2026-07-08：鮮度断層の解消方針 D3」）。以後更新しない。
> 記載スレッドの多くは他リポジトリ（ops-log / the-garage）系であり、ops-log / the-garage への移送は別フェーズで扱う（今回は残置のみ）。
> 以下の本文は historical index として残置する。AIはこのファイルを現状把握に使わないこと。

# THREAD_INDEX

Purpose:
三銃士OSのスレッド地図。統合ではなく索引。
INDEXは本文ではなく入口。

Rule:
Pointer only. No logic. No lore. No history.

---

## payroll-dashboard
Identity:
給与計算OS / 売上分析契約層
Boundary:
- XRPL Verification Layer
- 評価ログOS
- AI冗長化 / INDEX設計
Wait:
Square closed_at 実データ受領 / payroll-engine Phase5 着手指示
Trigger:
Square実CSV受領 / derive_minutes.py 着手指示

---

## XRPL Verification Layer
Identity:
AI検証OS / hash anchoring / canonicalization
Boundary:
- 投機
- token価格
- 全文オンチェーン
Wait:
canonicalization spec v0 未確定
Trigger:
canonicalization spec 初稿完成

---

## drop評価ログOS
Identity:
日次観測 → 月次解釈 → owner裁定
Boundary:
- 売上dashboard
- payroll計算
- AI自動評価 / ranking
Wait:
monthly_review 運用テスト
Trigger:
kizuki_log 実運用データ蓄積

---

## AI冗長化 / 移植準備
Identity:
AIを交換可能部品として扱うためのOS固定層
Boundary:
- 個別実装
- 全会話移植
- memory依存
Wait:
TERMINOLOGY_DICTIONARY / ROLE_MAP 未作成
Trigger:
THREAD_INDEX 初版固定

---

## The Garage Infrastructure
Identity:
Mac mini / GitHub / VS Code / repo運用基盤
Boundary:
- 店舗評価制度
- 銀行融資
- 商品開発
Wait:
VS Code / repo配置整理
Trigger:
Mac mini 環境確認
