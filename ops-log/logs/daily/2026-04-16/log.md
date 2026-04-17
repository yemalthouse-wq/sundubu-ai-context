# 2026-04-16

## What happened
- sense_log.htmlのJS停止原因を調査・余分なcatch/await混入を除去
- UI復旧確認（ボタン押下・Recent Log表示まで復旧）
- GAS書き込みが発火しない問題を切り分け
- CORS/405を受け、no-cors + FormData方式に修正
- GAS doPost(e)をe.parameter.data / e.postData.contents対応に再構成
- OBSERVE_LOG appendRow用カラム構成A〜Iで固定
- GASを再デプロイし本番運用可能な状態まで到達

## Decisions
- 気づきログを「手入力メモ」から「運用OSの正式な入力導線」へ昇格
- フロント送信形式とGAS受信形式を揃えることが本質
- 三銃士OSとして「気づき→保存→蓄積→後から分析」の入口が実装レベルで成立

## Why
- UIが死ぬ原因はGASではなく、フロントのJSが1行の構文エラーで全停止する構造
- no-corsでは通信失敗が見えにくい

## Next actions
- OBSERVE_LOGに最低10件投入し、入力粒度・項目の過不足・実運用のだるさを検証

## 今日のボツ案
- await fetchをそのまま入れる案
- no-corsのまま成功判定しようとする案
