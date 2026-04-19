## What happened
- GAS doPost受信確認のトラブル対応
- fetch(no-cors)と通信不確実性の問題を特定
- UIと実通信の分離に気づいた

## So What
- ログが習慣依存でシステム化されていなかった
- 通信レイヤーの不確実性がボトルネック
- 「動いてるように見える」状態が危険と判明

## Now What
- RECV_RAWで通信可視化
- GET→POST確認フロー固定
- Queue & Retry設計に移行
