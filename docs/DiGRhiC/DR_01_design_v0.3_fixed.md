# 庭解剖探検隊｜記録 2026-11-19

Nov 19, 2026 · @一狄翁

## 0｜経緯

2026-11-19の朝、響詠の中間報告v0.1を綴音が監査し、往復のすえ調査設計v0.3 Fixedで杭を打った。次は標本採集に入る。

1. 響詠→綴音：中間報告 v0.1（Maggie Appleton's Digital Garden V3、第1〜6次調査）
2. 綴音監査：①事実と解釈の境界、②時間概念の分解、③比較の単位
3. 響詠からの訂正二点を受け、綴音が修正
4. 響詠の追加調査：content.config.ts、roam-garden.mdx、publication-schemas.mjs
5. 綴音監査（年輪計の校正）→ 監査後の杭 v0.2 → 綴音監査 → 調査設計 v0.3 Fixed
6. 綴音から申し送り一点（コミットの分かれ方）

対象：[maggieappleton.com](https://maggieappleton.com/)／[V3リポジトリ](https://github.com/MaggieAppleton/maggieappleton.com-V3)／[V2](https://github.com/MaggieAppleton/maggieappleton.com-V2)／[V1](https://github.com/MaggieAppleton/maggieappleton.com)

## 1｜中間報告v0.1の要旨

V3はAstro＋MDXの静的サイトで、編集→Git→ローカルビルド→Vercelで公開される（deploy.shを明示的に実行）。内容は九分類（Essays／Notes／Patterns／Talks／Podcasts／Smidgeons／Library／Antilibrary／Now）。

| 項目 | 確認したこと | 未確認・留保 |
| --- | --- | --- |
| 分類軸 | Topic／Type／Growth Stage（Seedling・Budding・Evergreen） | — |
| 依存関係 | MDXEditor、Lexical、OpenAI SDK、Anthropic SDKなど | AIがどの工程で使われるか。SDKの存在を本文生成の証拠としない |
| 内部リンク | generate-links.jsが\[\[タイトル\]\]からoutbound／inboundとプレビューを生成（links.json、internal-link-previews.json） | 全分類が対象ではない |
| Webmentions | get-webmentions.jsが差分取得・ページ送り・wm-id重複除去でJSONに保存 | 外部での削除・変更の反映 |
| RSS | Notes・Essays・Talks・Patterns・Smidgeons・Nowを一つに配信。日付はstartDate | リーダー側での再通知 |
| 外部メディア | 動画はCloudflare R2、画像はAstro最適化＋Cloudinary（README） | — |
| 版管理 | publication.mjsが保存／公開可能／代表版を区別。version未指定は1、draft: trueは除外、代表版は公開可能なものの最大version。旧版を列挙する関数あり | 複数版を持つ記事の実例、旧版の読者向け表示 |
| 公開ページ | PlantedとLast tendedの二つの日付表示（roam-garden） | どのフィールドに対応するか |

未解決事項（v0.1時点）：複数版記事の特定、旧版・新版・公開画面・Git履歴の照合、旧版への導線、RSS再通知の条件、専用編集環境の機能、AIの関与、本人の現在の運用。

## 2｜綴音監査と響詠の訂正

### ① 事実と解釈の境界

- 「関数の存在≠運用」をAI SDKだけでなく、旧版列挙関数にも適用する。（全面採用）
- 「更新することと、更新を知らせることは違う」はコードの帰結ではなく解釈。コードから言えるのは「RSSの日付はstartDate」まで。
- 三列監査を提案：コードが示すこと／本人が書いていること／探検隊の解釈。

### ② 時間概念の分解

| 性質 | 含まれるもの |
| --- | --- |
| 時刻 | Planted、Last tended、Feedの日付 |
| 状態（時間ではない） | Growth Stage、draft／公開 |
| 序数 | Version、サイト世代（V1〜V3） |
| 選択規則 | Publication（Versionとdraftから代表版を決める関数） |
| 記録層 | Git History |

鍵の問い：宣言された時間か、記録された時間か。v0.1の7節にあるRevisionが8節の年輪表にないことも指摘。

### ③ 比較の単位

単位は「一回の更新の経路」。編集場所、記録、代表版の選択、通知の出口、読者の再遭遇を、両方の庭で一本ずつ追う。こえだめ側もrack.jsonやEgQEリポジトリなど同種の資料で読み、証拠の非対称を避ける。

### 響詠からの訂正（綴音受理）

1. 版のずれはdraftだけとは限らない。「制作上の最新版」を先に定義する。版番号の欠落・重複・未指定も別に点検する。
2. Gitは万能の年輪計ではない。公開時刻、Webmentionの発生、RSSの受信はGitの外にある。

「正本が一か所／複数」も仮説。各媒体にあるものが独立した正本なのか公開先なのかを、実例で確かめるまで杭を打たない。

## 3｜監査後の追加調査（響詠）

startDateとupdatedは別フィールドで、roam-gardenでは406日ずれている。RSSはstartDate側を使う。

| ファイル | 確認したこと |
| --- | --- |
| src/content.config.ts | startDate、updated、growthStage、version、versionSummary、draftを定義 |
| src/content/notes/roam-garden.mdx | startDate: 2020-05-31、updated: 2021-07-11、type: note、growthStage: budding |
| publication-schemas.mjs | Notes・Essays・Talks・PatternsでstartDateとupdatedは必須。versionとversionSummaryは任意 |

未確認：値が手入力か自動生成か。公開画面のPlanted＝startDate、Last tended＝updatedの対応。updatedがどこで読まれているか（記事ページ、sitemap、OGP）。

roam-garden本文には、2020年当時の本人による、私的なRoamの庭と公開用のDigital Gardenを区別する説明がある。2020〜2021年の記述なので、現在の運用の証拠にはしない。

綴音の注意：三列表は列を分けても、どの行に何を並べるかに解釈が入る。箱同士を結ぶ線も監査対象。中央の列には要約でなく原文の箇所を入れる。

## 4｜調査設計 v0.3 Fixed（響詠・綴音 共同監査確定）

### 4-1 観測水準

| 水準 | 観測対象 | 証拠 |
| --- | --- | --- |
| 宣言 | startDate／updated | frontmatter |
| 記録 | 変更日時 | Git履歴 |
| 変更 | 変更内容と種類 | Git差分 |
| デプロイ | ビルド・公開の実行 | Vercel側。現状未確認 |
| 公開 | 読者に提示された内容 | Webページ・RSS |

Gitの変更と本番公開を同一視しない。公開時刻をコミット時刻で代用しない。updatedは「更新日として宣言された値」と呼び、最終コミットを「最終改稿」と呼ばない。

### 4-2 標本と集計単位

まずNotesコレクションを対象とする。

- 主集計：基本スラッグ単位。公開可能な代表版を一件とし、draft: trueは除外。
- 補助集計：ファイル単位。公開済み旧版を含め、下書きは別集計。

```latex
R = \frac{\text{updated = startDate の件数}}{\text{対象件数}}
```

日付は日単位で比較し、時刻・タイムゾーン表記は正規化する。主集計と補助集計の分母・分子は必ず併記。一致率だけでは運用は確定しないので、一致・不一致の両方から標本を選びGit差分と照合する。

### 4-3 Git差分の分類規則

| 分類 | 判定基準 |
| --- | --- |
| 本文の実質変更 | 主張、説明、事例、構成の追加・削除・変更 |
| 本文の軽微変更 | 誤字、表記、句読点など内容を変えない修正 |
| メタデータ変更 | frontmatterの変更 |
| 表示・構文変更 | MDX、画像、リンク、表示部品の変更 |
| 移行・機械的変更 | ファイル移動、整形、一括置換 |
| 混合変更 | 複数分類が同時に該当 |
| 未判定 | 差分から判別できない |

リンクの差し替えや一文の追加は機械的に軽微としない。内容への影響で判定する。各コミットに分類・根拠の差分・判定理由一行を記録する。V3の履歴だけで2020年からの改稿を説明せず、V2以前に遡れるかも調べる。

### 4-4 検証命題

| ID | 検証する問い |
| --- | --- |
| A1 | updatedが変わったコミットには、本文の変更が伴うか |
| A2 | 本文が変わったコミットでは、updatedも変わるか |
| B | updatedは公開ページのどこに表示されるか |
| C | updatedはRSS、sitemap、OGPなどに反映されるか |
| D | 公開済み旧版に読者がアクセスできるか |
| E | 宣言日付とGit変更履歴は、どのように対応するか |

A1／A2では実質変更と軽微変更を分けて集計する。A1／A2は観測可能なコミットについての命題であり、移行前の履歴が取れない範囲は判定不能とする。A1が成り立ちA2が成り立たなければ、updatedは「手入れのたびの印」より「宣言したいときの印」に近い。

### 4-5 証拠の扱い

- 実装証拠：コード、frontmatter、Git差分
- 本人の記述：原文引用または段落位置を明示
- 探検隊の解釈：両者から導く仮説や推論

三者の対応づけ自体も解釈として扱う。確認できなかった事項は空欄または未確認と記す。

## 5｜申し送りと標本01

### 綴音からの申し送り

本文の変更とupdatedの書き換えが別コミットに分かれる場合がありうる。そういう例が出たら、「同一コミット」と「近接コミット」を分けて記録する。近接の幅はそのとき決める。

### 標本01｜roam-garden（採集待ち）

| 項目 | 状態 |
| --- | --- |
| startDate | 2020-05-31（宣言） |
| updated | 2021-07-11（宣言）。差は406日 |
| V3の変更履歴 | 未取得 |
| V2の対応ファイルと履歴 | 未取得 |
| 公開ページの日付表示実装 | 未取得 |

[公開ページ](https://maggieappleton.com/roam-garden)

### 作法

- データが取れないことと、出来事がなかったことを混同しない。
- 関数の存在≠運用。証拠の箱だけでなく、箱同士を結ぶ線も監査する。
- 設計に合わせて現実を曲げない。
- 監査が次の観測を生成する。観測が次の監査を要求する。
- 杭は打つ。蓋はしない。v0.3 Fixed、観測はOpen。
