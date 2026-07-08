# DECISION LOG

**スンドゥブ田中家OS・意思決定記録**

---

## 2026-03-07：OS目的の確定

### Purpose

**飲食店を増やすことではない。**

**既存店舗の空き厨房を使って、スンドゥブ田中家を拡張するOS。**

---

### Model

**Type 1：既存店舗ランチ導入モデル**

- 居酒屋の昼
- カフェの夜
- ラーメン屋の深夜

既存の厨房・人員を活用し、追加投資を最小化。

---

### Pilot

**新丸子**

- 1号店として実験
- 数字の検証
- オペレーションの検証
- 本部サポートの検証

---

### Unit Economics

**後日確定**

---

## 2026-03-07：鍋OS確定

### 1鍋 = 20食（固定・変更不可）

---

## 2026-03-07：基本原価確定

### 基本スンドゥブ原価：¥146（変更不可）

- 鍋原価：¥50 / 豆腐：¥33 / 卵：¥21 / ネギ：¥15 / 胡麻油：¥1 / アサリ2個：¥26

---

## 2026-03-07：本部卸価格確定

> **[SUPERSEDED 2026-07-08]** 本決定は「2026-07-08：数値正典の確定（鍋エンジンモデル・BOX価格）」により失効。歴史的記録として残置。

### 鍋キット：¥1,600/鍋（変更不可）

本部利益：¥600/鍋 = ¥30/食

---

## 2026-03-07：FC契約条件確定

### 初期投資：¥600,000〜800,000

### ロイヤリティ：0%（供給マージン制。売上監視なし）

### 契約期間：1年（自動更新）

**変更不可。**

---

## 2026-03-07：外税10%方式確定

### 店内価格：外税10%表示（変更不可）

---

## 2026-03-10：卸販売P/L確定

> **[SUPERSEDED 2026-07-08（数値のみ）]** 下表の数値（1BOX売価¥50,000・卸粗利¥27,698 および派生値）は「2026-07-08：数値正典の確定」により失効。**P/L分離ルールは存続。**

| 項目 | 数値 |
|---|---|
| 1BOX構成 | 10鍋分（200食分） |
| 1BOX売価 | ¥50,000 |
| 1BOX総原価（送料込） | 約¥22,302 |
| 1BOX卸粗利（送料込） | ¥27,698 |
| 1食あたり売価 | ¥250 |

### P/L分離ルール（変更不可）
- 卸P/L（本部）= BOX売価 − 商品原価 − 送料
- 自店舗P/L（加盟店）= Uber売上 − 仕入れ代 − 店舗コスト
- Uber手数料・包材費を卸利益計算に混ぜない

---

## 2026-03-10：FC収益モデル確定（変更不可）

**ロイヤリティ廃止・供給マージン制に統一**

理由：ロイヤリティ型は売上監視→売上隠し→信頼崩壊で小規模FCが死ぬ。供給型はスープが売れれば本部も加盟店も儲かる。

対外的な言い方：「フランチャイズではなく、供給ネットワークです」

| 項目 | 確定値 |
|---|---|
| ロイヤリティ | 0% |
| 本部収益源 | 鍋キット・スープ・具材パックの供給マージンのみ |
| 本部収益（1店舗月次） | 約¥375,000 |
| 損益分岐 | フェーズA：2店舗 / フェーズB：4店舗 |

参照: fc/fc_constitution.md 第3条・第4条

---

**このログは、OSの前提を固定する。AIはこのログを読めば、前提を忘れない。**

END OF LOG

---

## 2026-07-07：DECISION LOG 再開（P1-3）

本ログは 2026-03-10「END OF LOG」以降も追記を継続する（上記 END OF LOG 表記は歴史的記録として残置し、本宣言が優先する）。
確定決定は core_rules 第7条に従い本ログに即記録する。

以下5件は 2026-03-10〜2026-07-06 の間、他リポジトリの一次ログにのみ存在した確定決定のバックフィルである（一次記録へのポインタ。全文複製はしない）。

- 承認: せいさん（2026-07-07）
- 根拠: the-garage `SYSTEM/EXECUTION_PLAN_OPS_LOG_RECOVERY.md` P1-3
- 転記対象: 確定決定のみ。観測・教訓（D-012/D-013/D-014(6/13)/D-015/D-016(6/16)）は一次ログに留め、本ログには転記しない
- ID衝突ポリシー（承認済み）: 既存ID（先行使用）を維持し、重複側を next_available_id に再採番する

---

## 2026-04-15：気づきログ基盤を本番導線として正式採用（バックフィル）

- 決定: 気づきログ基盤（sense_log → GAS → OBSERVE_LOG）を本番導線として採用
- 併記原則: 保存は構造（GAS）・分析は補助・判断は人間
- 一次記録: ops-log `logs/daily/2026-04-15/log.md`, `logs/daily/2026-04-16/log.md`

---

## 2026-04-27：バーチャルFCモデル廃止・ハイブリッドモデルへ転換（バックフィル・R-05）

- 決定: **バーチャルFC（ゴースト）展開モデルを廃止**し、「**物理ミニ店舗＋デリバリー最適化**」ハイブリッドモデルへ転換する
- 背景: Uber Eats Japan が 2026-07-01 よりバーチャルレストランの新規登録を停止。プラットフォームの方向性が「量→質」へシフトし、ゴースト・バーチャル型の展開は継続不可
- 付随アクション（原決定に記載）: 既存アカウントの保護（QSC指標の維持）／全資料から「バーチャル／ゴースト」表記を削除／FCパッケージをハイブリッド物理デリバリーモデルとして再定義
- **旧バーチャルFCモデルは discontinued。今後のFC展開・資料・試算の前提としない**（旧記述は歴史的記録として削除しない）
- 性質: **新規裁定ではない**。2026-04-27 に確定済みの決定の本ログへのバックフィル転記（転記日 2026-07-08 / Recovery Execution R-05）
- 一次記録（source）: `context/uber_virtual_restaurant_suspension_2026.md`（決定日 2026-04-27）

---

## 2026-06-18：D-017 Ye Malthouse 観測ケースの配置確定（バックフィル）

- 決定: USE_EXISTING_REPOSITORY — 新規リポジトリを作らず ops-log `cases/ye-malthouse-long-term-reports/` に置く
- 正本: Google Sheet + 動画アーカイブ（GitHub は要約・判断履歴・効果測定のみ）
- 一次記録: ops-log `cases/ye-malthouse-long-term-reports/decision-log.md`（D-017）

---

## 2026-06-19：D-018 Future Logic リポジトリの役割確定（バックフィル・ID再採番）

- 決定: the-garage `future-logic/` を prepared_response_accumulation の場として確定（Garage stores: prepared_logic ／ Garage does not: manage active fronts）
- ID再採番: 一次記録では「D-016」と表記されているが、ops-log 2026-06-16 の D-016（Reality Before Expansion）が先行使用のため、承認済みポリシーにより本決定を D-018 に再採番。一次文書（the-garage `future-logic/DOCTRINE.md`）の表記修正は別タスク
- 注1: DOCTRINE.md 文書全体は doctrine_candidate のまま。確定したのは「リポジトリの役割」のみ
- 注2: ops-log `cases/ye-malthouse-long-term-reports/decision-log.md` の空欄テンプレート行に「D-018」が事前記入されているため、同ケースの次の決定は D-019 を使用すること（要・同ファイルの1行修正、別タスク）
- 一次記録: the-garage `future-logic/DOCTRINE.md`（commit d3261f1, 2026-06-19）

---

## 2026-06-22：D-GARAGE-001 Garage HQ host_os 確定（バックフィル）

- 決定: host_os = Windows + WSL2（旧候補: Ubuntu 直インストール）
- 分類: plan_change（basis: observed_context_changed）≠ drift
- 参照 doctrine: reversible_first ／ observed_before_commitment（いずれも candidate 扱い、本ログでは決定のみ記録）
- 一次記録: ops-log `logs/daily/2026-06-22/log.md` ／ the-garage `logs/ops/2026-06-22/log.md`

---

## 2026-06-22：Phase 1.8 恒久クローズ（バックフィル）

- 決定: Phase 1.8 archive を恒久クローズ（rule: DO_NOT_IMPLEMENT）
- open_gate: Consumer_Alignment_Verification
- 一次記録: ops-log `logs/daily/2026-06-22/log.md`

---

## 2026-07-07: ログ正本先の一本化（P2-1）

- 決定: daily log の push 先を ops-log 1リポジトリへ一本化する
- 根拠となる既存定義: ops-log `system-map.md`
- 廃止: 同一ログを sundubu-ai-context / ops-log / the-garage の3リポジトリへ同時pushする doctrine
- 効果: ログの正本は ops-log のみ。他リポジトリは必要時に参照する
- 既存の重複ログ: 掃除は本決定の範囲外
- 承認: せいさん（2026-07-07） / Execution Thread


---

## 2026-07-07: Ye Malthouse 運用正本の一本化 (P3-1)

- 決定: Ye Malthouse の運用判断・ルール・変更管理の正本は `sundubu-ai-context/ye-malthouse/`
- 理由: Layer 1 宣言（事業管理本部・2事業並列）と整合
- 修正: the-garage `projects/ye-malthouse/README.md` は正本ポインタへ変更
- 実コンテンツの移送: 本決定の範囲外（別フェーズ）
- 観測ケース（ops-log cases + Google Sheet）は継続
- 承認: せいさん (2026-07-07) / Execution Plan P3-1

---

## 2026-07-08：数値正典の確定（鍋エンジンモデル・BOX価格）（R-01/R-02）

### 確定値（正典）

| 項目 | 確定値 |
|---|---|
| FC Supply BOX価格 | **¥38,000**（送料込） |
| BOX構成 | 10鍋 / 30袋 / 200食 |
| 本部粗利（鍋エンジンモデル） | **¥2,000/鍋** |
| 本部粗利率 | **57%** |

### supersede対象（削除せず残置）

1. 2026-03-07「本部卸価格確定」— 鍋キット¥1,600/鍋・本部利益¥600/鍋
2. 2026-03-10「卸販売P/L確定」— 1BOX売価¥50,000・卸粗利¥27,698（**数値のみ失効。P/L分離ルールは存続**）

### 変更理由

¥50,000/BOX・¥1,600/鍋では利益構造が崩れることが判明し、2026-03-13時点で¥38,000＋鍋エンジンモデルへ改定済みだったが、本ログへの転記が漏れ、旧数値が「変更不可」のまま正典に残存していた（二重正典）。本エントリで転記漏れを解消する。

### 一次記録

- ops-log相当のデイリーログ: `logs/daily/2026-03-13/log.md`, `logs/daily/2026-03-15/log.md`
- `docs/fc-design.md`（2026-05-13）
- CLAUDE.md CURRENT STATE（2026-04-12）

### 補足

- GLOSSARY / business_models / LATEST / fc_constitution への downstream propagation は本決定の範囲外（Recovery Execution 次ステップで実施）
- 承認: せいさん（2026-07-08）/ Recovery Execution D候補1（R-01/R-02）

---

## 2026-07-08：鮮度断層の解消方針 D1〜D4（R-08B）

R-08A Freshness Review（2026-07-08 実施。現在地を名乗るファイルが4枚存在し、それぞれ 2026-03-10 / 04-12 / 03-10 / 03-10 で凍結していた断層の整理）を根拠とする owner 裁定。

### D1：現在地正本の一本化

- **現在地の正本は LATEST.md に一本化する**
- CLAUDE.md の CURRENT STATE は、今後 LATEST.md 参照ポインタへ縮退する
- 理由: CLAUDE.md 自身が Layer 1 に LATEST を指定しており、現在地正本の二重化を解消するため

### D2：current_focus.md の廃止凍結

- context/current_focus.md は**廃止宣言ヘッダ付きで凍結**する（削除はしない）
- 週次運用は再開しない
- 今後の focus / next action は LATEST.md に吸収する

### D3：THREAD_INDEX の凍結残置

- SYSTEM/THREAD_INDEX.md は**凍結ヘッダ付きで残置**する
- ops-log / the-garage への移送は今回は行わない（移送する場合は別フェーズで扱う）

### D4：LATEST 再生成の前提条件

- LATEST.md の再生成にあたり、**CLAUDE.md CURRENT STATE（2026-04-12）を最新事実として採用しない**
- 上目黒 / 新丸子 / 評価OS / 営業資料 / 現場進捗は **owner の最新状況入力後に反映**する
- それまでは LATEST 全面再生成を実行しない

### 補足

- **本エントリは裁定記録のみ。対象ファイル（LATEST / CLAUDE.md / ROADMAP / THREAD_INDEX / current_focus）の編集は後続の実行ステップで行う**
- 根拠: Recovery Execution R-08A Freshness Review（2026-07-08）
- 承認: せいさん（2026-07-08）/ Recovery Execution R-08B

---

## 2026-07-08：実装同居の例外許容（R-09B）

### 裁定

- sundubu-ai-context は **business_doctrine_root** である
- ただし以下の実装・配信資産の同居を**例外として許容**する
  - `vercel.json`
  - `public/`
  - `scripts/`
  - `data/`
- **この例外は現状維持のためであり、新規実装の許可ではない**

### 理由

- Vercel デプロイおよび `public/sense_log.html` の稼働実態が未確認
- `public/sense_log.html` は 2026-04-15 決定（気づきログ基盤の本番導線採用）の構成要素である可能性がある
- 稼働確認前の移送・削除は本番導線を壊す可能性がある
- 最大リスクは同居そのものではなく、**Phase 1.8 恒久クローズ（DO_NOT_IMPLEMENT）と実装実体が無注記のまま残る乖離**である。本エントリはその乖離を「明記された例外」に転換する

### 境界ルール

1. `vercel.json` / `public/` / `scripts/` / `data/` は実装同居例外であり、doctrine root の通常責務ではない
2. doctrine 作業中にこれらを触らない
3. `scripts/` は Phase 1.8 恒久クローズ（2026-06-22 決定）に服する **dormant 資産**
4. `scripts/` の編集・実行・再開は **Consumer_Alignment_Verification gate 通過後のみ**
5. `public/data/*.json` と `data/delivery_orders.json` は現状維持（生成物・パイプライン入力として不触）
6. deploy / build / pipeline 実行は禁止
7. `public/sense_log.html` は稼働確認まで不触

### 移送方針

- A案「実装一式を別リポジトリへ移送」は**今回は実行しない**
- 移送は Vercel / sense_log.html の稼働実態確認後の**別フェーズ**とする
- 移送判断までは残置
- 将来移送する場合も、導線維持と consumer 確認（docs/data_contracts.md の契約消費者）を前提とする

### CLAUDE.md との関係

- CLAUDE.md のリポジトリ構造図は R-09C で実態同期する（本エントリでは CLAUDE.md を編集しない）

### 承認情報

- owner approved（B案採用）
- reviewed_at: 2026-07-08
- source: R-09A implementation colocation review（2026-07-08）
- 承認: せいさん（2026-07-08）/ Recovery Execution R-09B

