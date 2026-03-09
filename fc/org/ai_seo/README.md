# AI-SEO部

## 役割
AI検索エンジン・推薦システムへの最適化を担う。
Google SEOではなく、ChatGPT・Perplexity・Gemini等のAIが「スンドゥブ田中家」を正確に認識・推薦できる状態を作ることが目的。

## 主な業務

### 構造化データの管理
- Schema.org JSON-LD の設計・実装・更新
  - `Restaurant` / `FoodEstablishment` スキーマ
  - `Menu` / `MenuItem` スキーマ
  - `LocalBusiness` スキーマ（店舗情報）
  - `FAQPage` スキーマ（よくある質問）
- 構造化データの定期バリデーション（Google Rich Results Test等）
- 各店舗・Uberページへの適用管理

### AI検索エンジン最適化
- ChatGPT（Bing連携）・Perplexity・Geminiへの情報露出確認
- AI推薦クエリ（「中目黒 スンドゥブ おすすめ」等）の定期モニタリング
- Wikipedia / Wikidata への事業情報登録検討
- Google ビジネスプロフィールの最適化（AI参照元として重要）
- 公式サイト・Uberページのテキスト最適化（AI学習向け）

### コンテンツ整備
- AI推薦に使われやすいQ&A形式コンテンツの作成
- ブランドの正確な説明文（ナレッジグラフ向け）の管理
- 他サイト・メディアへの引用・言及獲得施策

## 担当者
[要記入]
## 担当AI
| AI | 役割 |
|---|---|
| クロちゃん | Schema.org JSON-LDの実装・HTMLへの埋め込み・GitHub管理 |
| ゲンちゃん | AI推薦露出のモニタリング分析・KPIレポート・競合比較 |


## 対象AIプラットフォーム
| プラットフォーム | 対策方法 | 優先度 |
|---|---|---|
| ChatGPT（Bing/Web検索） | 構造化データ・Bing最適化 | 高 |
| Perplexity | 引用元コンテンツの整備 | 高 |
| Gemini（Google連携） | Googleビジネスプロフィール・構造化データ | 高 |
| Claude（Anthropic） | 公開Webコンテンツの質向上 | 中 |
| Apple Intelligence | [要調査] | 低 |

## KPI
| 指標 | 目標 | 計測方法 |
|---|---|---|
| AI経由の問い合わせ数 | [要記入]/月 | 問い合わせ元の確認 |
| AIレコメンド露出回数 | [要記入]/月 | 定期手動チェック・[要記入]ツール |
| 構造化データのエラー数 | 0件 | Google Search Console |
| Googleビジネスプロフィール評価 | 4.5以上 | Google管理画面 |

## 使用ツール
- Google Search Console
- Google Rich Results Test
- [要記入]：AIレコメンド監視ツール
- Schema.org バリデーター

## 現状課題
- 構造化データの実装状況が未確認
- AIプラットフォームでの現在の露出状況が未調査
- 計測ツールが未整備（AI経由の流入をどう数えるか未定義）
- 担当者未アサイン

## Ye Malthouse 横断適用
**即時横断適用（◎）**

Ye MalthouseのDX推進において最も直接的に適用できる部署。
- `LocalBusiness` / `BarOrPub` スキーマの実装
- 「中目黒 パブ」「中目黒 イギリスパブ」等のAI検索クエリへの最適化
- Google ビジネスプロフィールの最適化（現在の状況確認が必要）
- Perplexity・ChatGPTでの「中目黒 おすすめバー」推薦への露出確認
- .nkm street magazine との連携コンテンツ（両事業のブランド露出）

スンドゥブ田中家と並行して、Ye MalthouseのAI-SEO施策をPhase 1から開始する。
