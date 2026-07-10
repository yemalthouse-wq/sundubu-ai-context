# Operational Boundary v1 — 事業・法人・運用境界の設計

**作成日：2026-07-10**
**status：Boundary v1 COMPLETE（設計）／承認待ち（PR merge をもって owner 承認とする）**
**性質：境界設計のみ。実装は一切含まない（No Implementation / Structure First）**

---

## 0. 目的と適用範囲

個人事業・法人（予定）・Garage HQ・Repository・GitHub・Google Drive・AI運用について、
長期運用可能な **Operational Boundary（運用境界）** を設計・固定する。

### scope（9領域）

Banking / Asset / Repository / GitHub / Google Drive / Dashboard / AI Runtime / Hardware / Subscription

### out_of_scope（本文書で扱わないもの）

- 税務判断・法務判断（すべて専門家確認前提。本文書は境界の**構造**のみ定義する）
- 資金調達の判断
- ランタイム実装（deploy / build / pipeline 実行を含む）
- 新規リポジトリの作成
- Future Logic（the-garage `future-logic/` の内容判断）

### 変更手続（execution_rule）

```
One Boundary → One PR → One Merge → One Verification
```

境界の新設・変更は 1境界 = 1PR とし、merge（= owner 承認）後に
decision_log へ記録し、Verification を1回実施する。

---

## 1. Boundary Map（境界地図）

すべての資産・契約・アカウントは、次の **3境界のいずれか1つ** に帰属する。

```
                     せいさん（個人・最終判断者）
                               │ 所有・最終判断
      ┌────────────────────────┼────────────────────────┐
      │                        │                        │
 [Boundary S]             [Boundary Y]             [Boundary C]
 スンドゥブ田中家           Ye Malthouse              共通基盤層
 （法人化予定）            （個人事業主継続・変更不可）  （せいさん個人所有・両事業へ按分）
      │                        │                        │
 ├ FC事業・卸販売          ├ パブ営業・DX推進         ├ AI三銃士（Claude / ChatGPT / Gemini）
 ├ 数値正典・FC憲法        ├ ye-malthouse/（運用正本） ├ GitHub アカウント＋3リポジトリ
 ├ 商標（Phase 2 登録予定） ├ 観測ケース（ops-log）    ├ Google Drive / Google Sheet
 ├ 新丸子パイロット        └ QRメニュー等 DX資産      ├ Vercel（dormant・R-09B 例外）
 └ 鍋OS・レシピ                                      ├ Hardware（Mac mini / Garage HQ）
                                                     └ 共通 Subscription
```

### 境界の基本原則

1. **S と Y は並列**。主従なし（core_rules 第4条）。違いは法人格のみ
2. **C は第三の境界**であり、S にも Y にも属さない。せいさん個人が所有し、コストを両事業へ按分する（project_context「2法人の管理ルール」準拠）
3. 二重帰属は禁止。両事業で使うものは必ず C に置く
4. **法人化前の現時点では、3境界すべての法的所有者はせいさん個人**。境界は会計・運用・記録の区分として機能し、法人化時に S の移転リスト（§5）の起点となる

---

## 2. Ownership Matrix（所有マトリクス）

凡例：**S** = スンドゥブ田中家 / **Y** = Ye Malthouse / **C** = 共通基盤層（せいさん個人・按分）

| # | 領域 | 対象 | 現所有（法人化前） | 帰属境界 | 法人化後の方針 | 根拠・備考 |
|---|---|---|---|---|---|---|
| 1 | Banking | スンドゥブ田中家の事業資金 | せいさん個人（事業別区分管理） | S | 法人口座へ移行（**専門家確認前提**） | 実際の口座構成は owner 確認待ち（§6） |
| 1 | Banking | Ye Malthouse の事業資金 | せいさん個人（事業別区分管理） | Y | 個人事業用として継続 | 法人格変更なし（business_models「変更不可」） |
| 2 | Asset | 数値正典・FC憲法・FCモデル・鍋OS・レシピ | せいさん個人 | S | 法人へ帰属（移転手続きは**専門家確認前提**） | FC加盟店との IP 帰属条項は fc_constitution 第9条で別途定義（要記入・未完） |
| 2 | Asset | 商標「スンドゥブ田中家」 | 未登録（Phase 2 登録予定） | S | 出願名義は法人化タイミングと併せて**専門家確認** | ROADMAP Phase 2 |
| 2 | Asset | Ye Malthouse ブランド・レシピ・DX資産 | せいさん個人 | Y | 個人事業のまま | — |
| 2 | Asset | doctrine 構造・AI運用ノウハウ | せいさん個人 | C | 個人保持 | 両事業の経営OSそのもの |
| 3 | Repository | sundubu-ai-context | せいさん個人 GitHub | C | 現状維持 | business_doctrine_root。2事業の doctrine を収容するため C |
| 3 | Repository | ops-log | せいさん個人 GitHub | C | 現状維持 | daily log 正本（decision_log 2026-07-07 P2-1）。Ye Malthouse 観測ケースを含む（D-017） |
| 3 | Repository | the-garage | せいさん個人 GitHub | C | 現状維持 | prepared_logic 蓄積（D-018）・Garage HQ 運用 |
| 4 | GitHub | GitHub アカウント本体 | せいさん個人 | C | 現状維持。法人 org 化は別フェーズ（本 v1 では判断しない） | AI（クロちゃん）は operator として書き込むのみ。所有しない |
| 5 | Google Drive | Google アカウント（yemalthouse@gmail.com）・Drive 全体 | せいさん個人 | C | 現状維持 | — |
| 5 | Google Drive | The Garage フォルダ | せいさん個人 | C | 現状維持 | Garage HQ 文書層 |
| 5 | Google Drive | Ye Malthouse 観測正本（Google Sheet＋動画アーカイブ） | せいさん個人 | Y | 個人事業のまま | D-017：正本は Sheet＋動画。GitHub は要約・判断履歴のみ |
| 6 | Dashboard | Vercel アカウント・deploy（vercel.json / public/） | せいさん個人 | C | 稼働実態確認後の separate future phase で判断 | R-09B 実装同居例外。**dormant・不触**。sense_log.html は稼働確認まで不触 |
| 6 | Dashboard | public/data・data/（pipeline 入出力） | せいさん個人 | C | 同上 | Phase 1.8 恒久クローズ（DO_NOT_IMPLEMENT）に服する |
| 7 | AI Runtime | Claude（クロちゃん）アカウント | せいさん個人 | C | 現状維持・按分 | AI は operator。所有・判断はしない（§4） |
| 7 | AI Runtime | ChatGPT（ぐぷちゃん）アカウント | せいさん個人 | C | 現状維持・按分 | 同上 |
| 7 | AI Runtime | Gemini（ゲンちゃん）アカウント | せいさん個人 | C | 現状維持・按分 | 同上 |
| 8 | Hardware | Mac mini（ローカルリポジトリ hosting） | せいさん個人 | C | 個人所有継続。法人利用分の扱いは**専門家確認前提** | CLAUDE.md リポジトリパス |
| 8 | Hardware | Garage HQ マシン（Windows + WSL2） | せいさん個人 | C | 同上 | D-GARAGE-001（2026-06-22） |
| 9 | Subscription | AI三銃士・GitHub・Google・Vercel 等の共通サブスク | せいさん個人契約 | C | 個人契約継続・両事業へ按分 | 契約の実在庫（一覧・金額）は owner 確認待ち（§6） |
| 9 | Subscription | 事業専用アカウント（例：Uber Eats 店舗アカウント） | せいさん個人契約 | 当該事業（S or Y） | 事業専用のものは C に入れず当該境界へ帰属 | 実在庫は owner 確認待ち（§6） |

**ownership 判定ルール：迷ったら「両事業で使うか？」を問う。Yes → C。No → 使う側の事業（S / Y）。**

---

## 3. Responsibility Matrix（責任マトリクス）

判断・承認は**すべてせいさん**（project_context「三銃士の役割」）。AI は支援のみ。

| 領域 | 判断・承認 | 実務・管理（operator） | 分析・監視 | 戦略・設計 |
|---|---|---|---|---|
| Banking | せいさん | せいさん（AI は口座・資金に触れない） | ゲンちゃん（数値レポートのみ） | ぐぷちゃん（スキーム案のみ・実行しない） |
| Asset | せいさん | クロちゃん（文書化・契約書ドラフト） | — | ぐぷちゃん（FCモデル設計） |
| Repository | せいさん | クロちゃん（ファイル作成・push・構造管理） | — | — |
| GitHub | せいさん（アカウント・権限） | クロちゃん（リポジトリ操作のみ） | — | — |
| Google Drive | せいさん（アカウント・共有権限） | せいさん（クロちゃんは指示時のみ読み書き） | ゲンちゃん（Sheet 分析） | — |
| Dashboard | せいさん | **凍結中（R-09B：不触・no deploy）** | — | — |
| AI Runtime | せいさん（契約・役割変更） | 各AI（自らの役割範囲内のみ・越境禁止） | — | — |
| Hardware | せいさん | せいさん | — | — |
| Subscription | せいさん（契約・解約） | せいさん | ゲンちゃん（コスト按分レポート） | — |

**責任の境界ルール：**

- AI三銃士は自分の担当領域を越境しない（core_rules 第9条）
- 契約・解約・支払い・口座操作は AI の責任範囲外。せいさんのみが実行する
- 新しい決定はすべて decision_log に記録する（core_rules 第7条）。記録の実務はクロちゃん、承認はせいさん

---

## 4. Operational Boundary v1 — 境界ルール

| ID | ルール |
|---|---|
| **B-01** | **並列原則**：S と Y の間で資金・資産・会計を相互流用しない。税務・法務は事業ごとに別管理する |
| **B-02** | **三分割原則**：すべての資産・契約・アカウントは S / Y / C のいずれか**1つ**に帰属する。二重帰属は禁止。両事業で使うものは C に置く |
| **B-03** | **按分原則**：C のコスト（AI三銃士・共通サブスク・横断部署 AI-SEO / AI-Ops）は両事業へ按分する。按分比率は本 v1 では定義しない（owner 確認後に別途確定・§6） |
| **B-04** | **正本一意性**：決定 = `context/decision_log.md`、現在地 = `LATEST.md`、日次ログ = ops-log、Ye Malthouse 運用 = `ye-malthouse/`、Ye Malthouse 観測 = Google Sheet＋動画（D-017）。正本の二重化を作らない |
| **B-05** | **法人化前固定**：法人化まで、全境界の法的所有者はせいさん個人で固定する。法人化時の S への移転は §5 のリストを起点とし、実行は専門家確認後の separate phase とする |
| **B-06** | **AI operator 原則**：AI は運用者（operator）であり、所有者でも判断者でもない。アカウント・資産・資金の所有はすべてせいさん。判断はすべてせいさん |
| **B-07** | **実装資産例外**：`vercel.json` / `public/` / `scripts/` / `data/` は R-09B 例外に服する C 内の dormant 資産。本 boundary はその**帰属のみ**を定義し、稼働・移送の判断はしない（separate future phase） |
| **B-08** | **変更手続**：境界の新設・変更は One Boundary / One PR / One Merge / One Verification。merge 後に decision_log へ記録する |
| **B-09** | **先決原則**：新規のアカウント・サブスク・リポジトリ・資産を作る場合、**作る前に**帰属境界（S / Y / C）を決める。境界未定のまま作成しない |
| **B-10** | **専門家確認原則**：税務・法務・資金調達に関わる境界の**実行**（口座開設・移転・出願・契約変更）は、本文書の対象外であり専門家確認を前提とする。本文書が定義するのは構造のみ |

---

## 5. 法人化時の移転候補リスト（構造のみ・実行しない）

スンドゥブ田中家の法人化時に、せいさん個人 → 法人への移転を**検討**する対象。
実行判断・手続き・税務処理はすべて専門家確認前提（B-10）。本リストは境界の起点にすぎない。

| 対象 | 現境界 | 移転方針 |
|---|---|---|
| スンドゥブ田中家の事業資金・口座 | S（個人管理） | 法人口座へ |
| レシピ・FCモデル・数値正典・鍋OS | S | 法人へ帰属 |
| 商標（未登録） | S | 出願名義を専門家と確認 |
| FC契約（新丸子ほか） | S | 契約主体を法人へ |
| Uber Eats 等の事業専用アカウント（S側） | S | 名義変更を確認 |
| C 層の資産（GitHub / Drive / AI / Hardware / 共通サブスク） | C | **移転しない**（個人所有継続・按分継続）。法人 org 化等は別フェーズで再評価 |
| Ye Malthouse の全資産 | Y | **移転しない**（個人事業主継続・変更不可） |

---

## 6. unresolved（owner 確認待ち・推測で埋めない）

以下は境界の**構造**には影響しないが、境界の**運用**に必要な事実情報。LATEST.md の unresolved 運用に準拠し、推測で埋めない。

- 実際の銀行口座構成（事業別区分の現状）
- サブスクリプションの実在庫（サービス一覧・契約名義・金額）
- 事業専用アカウントの実在庫（Uber Eats 等の名義・帰属）
- C 層コストの按分比率（B-03 の運用値）
- Vercel / sense_log.html の稼働実態（→ Dashboard 境界の移送判断の前提。R-09B）

---

## 7. Verification Report

検証日：2026-07-10 ／ 検証方法：本文書と Layer 0〜2 正典（core_rules / decision_log / project_context / LATEST / GLOSSARY / ROADMAP / CLAUDE.md）との突合

| 検証項目 | 結果 | 根拠 |
|---|---|---|
| **ownership_complete** | ✅ PASS | scope 9領域（Banking / Asset / Repository / GitHub / Google Drive / Dashboard / AI Runtime / Hardware / Subscription）すべてが Ownership Matrix（§2）で S / Y / C いずれかに帰属。帰属先未定の領域なし |
| **responsibility_complete** | ✅ PASS | 9領域すべてに判断者（せいさん）と operator が割り当て済み（§3）。判断者が空欄の領域なし |
| **no_conflict_detected** | ✅ PASS | 既存決定との矛盾なし：2事業並列（core_rules 4条）＝B-01、按分（project_context）＝B-03、ログ正本一本化（P2-1）＝B-04、Ye Malthouse 運用正本（P3-1）＝B-04、観測正本（D-017）＝B-04、実装同居例外（R-09B）＝B-07、Phase 1.8 恒久クローズ＝§2 #6、Garage HQ host_os（D-GARAGE-001）＝§2 #8。decision_log の確定事項を1件も変更していない |
| **boundary_consistent** | ✅ PASS | 全領域が三分割原則（B-02）で単一帰属。二重帰属なし。S/Y の並列性を崩す記述なし。「事業専用は当該境界・共用は C」の判定ルールが全行で一貫 |

**completion_definition：Operational Boundary v1 = COMPLETE（設計として）。承認は PR merge をもって成立。**

---

## 8. 承認と decision_log 転記（merge 後の後続ステップ）

本文書は設計成果物であり、**merge（= owner 承認）までは確定決定ではない**。
merge 後、以下のドラフトを `context/decision_log.md` へ転記する（転記は別コミット・core_rules 第7条）。

> ### 2026-07-XX：Operational Boundary v1 確定
>
> - 決定：事業・法人・運用境界を 3境界モデル（S：スンドゥブ田中家 / Y：Ye Malthouse / C：共通基盤層）で確定
> - 境界ルール B-01〜B-10 を採用（正本：`docs/operational_boundary_v1.md`）
> - 法人化時の移転は §5 リストを起点とし、実行は専門家確認後の separate phase
> - 境界変更手続：One Boundary / One PR / One Merge / One Verification
> - 承認：せいさん（merge 日）

---

*本文書は境界の構造定義のみを行う。税務・法務・資金調達の実行判断は専門家確認前提。実装は行わない。*
