
# 庭解剖探検隊｜標本01 観測記録

**記録日：2026-11-19**  
**状態：観測記録 v0.1.1／Open**（綴音監査の三点を反映：ハッシュ対応表、解釈文の移動、YearsAgoの適用範囲）  
**上位プロトコル：v0.3 Fixed（変更なし）**  
**v0.4候補：時間の多層性／表示機構と原稿適用の分離**

## 0｜対象と境界

対象：Maggie Appleton, *Tending Evergreen Notes in Roam Research*（slug: `roam-garden`）。現行公開ページは <https://maggieappleton.com/roam-garden>。調査対象はV1候補、V2、V3の原稿・表示コード・Git差分。Git履歴は公開サイトへのデプロイ履歴と同義ではない。著者の意味づけはコードから推測しない。

- V1候補：<https://github.com/MaggieAppleton/maggieappleton.com>（`master`、`content/notes/roam-garden.mdx`）
- V2：<https://github.com/MaggieAppleton/maggieappleton.com-V2>（`posts/notes/roam-garden.mdx`）
- V3：<https://github.com/MaggieAppleton/maggieappleton.com-V3>（`src/content/notes/roam-garden.mdx`）

**調査過程の訂正**：一度「V1の公開リポジトリは特定できなかった」と報告したが、これはv0.1で指定済みのリポジトリを直接開かず別名検索したため。後に直接照合し、V1候補に原稿が存在することを確認した。

## 1｜原稿の日付の変遷（V1候補）

| コミット（UTC） | 対象の変更 | 判定 |
| --- | --- | --- |
| 2020-06-20 | `roam-garden.mdx` の確認できた最初のファイルコミット | `2020-05-31`より20日後。執筆開始日とは断定しない |
| 2021-01-15 | `date: 2020-05-31` → `updated: 2020-05-31` | フィールド名変更 |
| 2021-06-27 | `updated: 2020-05-31` → `startDate: 2020-05-31` と `updated: 2021-06-27` | **標本01に二日付が揃った日** |
| 2021-07-04 | `updated: 2021-06-27` → `updated: 2021-07-05` | 本文変更を伴う。日付差の理由は未判定 |
| 2021-07-11 | `updated: 2021-07-05` → `updated: 2021-07-11` | 本文変更を伴う。正式な変更分類は保留 |

6月27日の決定的差分：

```diff
-updated: 2020-05-31
+startDate: 2020-05-31
+updated: 2021-06-27
```

**厳密な記述**：「古い値を移動した」のではなく、旧 `updated` の値を新しい `startDate` に保存し、`updated` に別の日付を宣言した。同じ `2020-05-31` が、後のスキーマでは「植えた日」の値として用いられる。ただし、著者が当初その日をどう理解していたかは不明。

主要差分（ハッシュ・日時・内容）：

| ハッシュ | 日時（UTC） | 内容 |
| --- | --- | --- |
| [`c82e2e760`](https://github.com/MaggieAppleton/maggieappleton.com/commit/c82e2e760) | 2021-01-15 08:46 | `Note.js` に `startDate`／`Planted` の条件付き表示を追加（表示機構。§2） |
| [`77fa86595e`](https://github.com/MaggieAppleton/maggieappleton.com/commit/77fa86595e) | 2021-01-15 09:05 | 原稿の `date` → `updated` 改名とテンプレート側の対応（上表の2021-01-15行） |
| [`29e3417d5b`](https://github.com/MaggieAppleton/maggieappleton.com/commit/29e3417d5b) | 2021-06-27 | `startDate` 追加、`updated: 2021-06-27`（変更ファイルは標本01の1件のみ） |
| [`a37d58fcce`](https://github.com/MaggieAppleton/maggieappleton.com/commit/a37d58fcce) | 2021-07-04 21:50:14 | `updated: 2021-07-05`、本文変更を伴う（GitHubコミット差分で直接照合済み：`-updated: 2021-06-27` / `+updated: 2021-07-05`。7月5日を宣言した理由は未判定） |
| [`20d9484b33`](https://github.com/MaggieAppleton/maggieappleton.com/commit/20d9484b33) | 2021-07-11 | `updated: 2021-07-11`、本文変更を伴う |

## 2｜表示機構と原稿適用の順序

V1候補の `src/components/Note.js` は `frontmatter.startDate` と `frontmatter.updated` を読み、存在する場合にそれぞれ `Planted` と `Last tended` を表示する。`src/@aengusm/gatsby-theme-brain/templates/brain.js` はGraphQLで両フィールドを取得する。

- **2021-01-15 08:46 UTC（`c82e2e760`）**：`Note.js` に `startDate`／`Planted` の条件付き表示が追加。この段階の更新日取得元はまだ `frontmatter.date`。
- **2021-01-15 09:05 UTC（`77fa86595e`）**：原稿の `date` → `updated` の改名とテンプレート側の対応。
- **2021-06-27**：標本01に `startDate` が追加。

したがって、**この標本では表示コードの準備が原稿の二日付化に先行した**。ただし、2021-01-15がサイト全体での二日付制の最初の導入日だったか、他のノートがいつ対応したかは別途照合が必要。6月27日の当該コミットで変更されたファイルは標本01の1件のみ。

コード：
- <https://github.com/MaggieAppleton/maggieappleton.com/blob/master/src/components/Note.js>
- <https://github.com/MaggieAppleton/maggieappleton.com/blob/master/src/@aengusm/gatsby-theme-brain/templates/brain.js>
- <https://github.com/MaggieAppleton/maggieappleton.com/commit/c82e2e760>

## 3｜四層監査：表示の意味と著者の意味を混同しない

| 層 | 判定 |
| --- | --- |
| コード・原稿 | 上記のフィールド変更と表示条件分岐はGit一次資料で確認 |
| 表示の推論 | 2021-01-15〜06-27、標本01では `Planted` がなく `Last tended` のみだったはず。06-27以後は併記されたはず |
| 公開表示の観測 | Wayback Machineで2021年2〜6月と6月27日以降のスナップショットを照合するまで未確認 |
| **著者の意味づけ** | コード・差分からは判定できない。著者本人の原文・発言が必要 |

表示推論の前提：①その時期に実際に公開されたサイトが該当リポジトリのコードに対応していたこと、②別経路で `startDate` が補完されていなかったこと。Gitコミット≠デプロイ≠公開画面。

**方法上の教訓**：現在のスキーマで過去の記録を読み替えない。同一の日付値が、表示機構とメタデータの変化によって異なる札を付けられうる。著者の意図は別問題。

## 4｜YearsAgo：別系統の時計

V2の2024-11-03コミット `d4a6534e` は、本文の「2020」を `<YearsAgo>2020</YearsAgo>` へ変更し、`updated` は変えていない。**本文に書かれた参照年は `updated` と独立**している。

V3の `src/components/mdx/YearsAgo.astro` は `new Date().getFullYear()` と本文の年との差を計算する。V3の `astro.config.mjs` に `output` 指定はなく、Notesを含む `src/pages/[...slug].astro` は `getStaticPaths()` を用い、`prerender = false` はない。したがって標準の静的ビルドでは相対年数は**ビルド時**に計算され、閲覧時には再計算されない。再ビルドしても新しい成果物が公開されなければ読者の表示は変わらない。具体的なビルド・デプロイ日時は未確認。

**適用範囲**：ビルド時評価を確認したのはV3のコードのみ。したがって「ビルド時に確定する」と言えるのは、V3として公開された期間に限る。V2（2024-11-03以降）については構文の導入のみ確認しており、V2の同名コンポーネントの実行時の挙動は未判定。実装の存在、実装の作動、公開された結果を混同しない。

時間の区別：①本文の参照年、②宣言された更新日、③計算時刻、④公開時刻、⑤閲覧時刻。`updated` はYearsAgoの入力ではない。

- <https://github.com/MaggieAppleton/maggieappleton.com-V2/commit/d4a6534efade441cf46efa46ded64af77a6e9867>
- <https://github.com/MaggieAppleton/maggieappleton.com-V3/blob/main/src/components/mdx/YearsAgo.astro>
- <https://github.com/MaggieAppleton/maggieappleton.com-V3/blob/main/astro.config.mjs>

時計の件（V3についての判定）はクローズ。

## 5｜V2・V3への継承と留保

V2のファイル履歴は22件（2021-09-25〜2024-11-03）、V3では当該パスに2件（2024-12-15、12-28）。V2の取り込み時点で `updated: 2021-07-11` は存在。V3の原稿でも `startDate: 2020-05-31`／`updated: 2021-07-11` が残る。V3の2件だけで過去の改稿の有無は判断できない。V2では2022-11-26の文言修正、2024-11-03のYearsAgo構文導入など、`updated` を変えないファイル変更の実例がある。

A1（`updated`変更→本文変更）・A2（本文変更→`updated`変更）は、差分の正式分類と前後の近接コミットの照合を経て判定する。「大きな改稿」という表現は未分類のため撤回し、現段階では「本文変更を伴う」に留める。

## 6｜未完の採集

1. **Wayback**：2021年2〜6月の `Last tended` 単独表示、6月27日以後の `Planted` 併記を外部観測で照合。保存されていない場合は不明のまま。
2. **サイト横断**：2021年1〜6月に他のノートが `startDate` をいつ採用したか。単一コミットの変更ファイル数から全体の導入時期を断定しない。
3. **全Git履歴**：V1/V2/V3をローカルcloneし、`git log --follow -G '^updated:' -- <path>` などで検査。本文変更とメタデータ変更が別コミットの場合も考慮。
4. **タイムゾーン**：2021-07-04 21:50:14 UTCのコミットが翌日を宣言した理由。GitHub APIのUTC正規化表示だけでは元のオフセット不明。`git log --format='%ai'` やraw patchで照合。UTC+2では現地日付はまだ7月4日。時差説はUTC+2:10以上で初めて可能。
5. **著者原文**：`Planted`／`Last tended`／`startDate`／`updated` の本人による説明。推測を著者の意図として扱わない。
6. **デプロイ**：当時のGit状態が実際の公開画面に反映された時刻・範囲は未確認。

## 7｜三列監査の境界

- **一次資料（コード／差分）**：フィールド、条件分岐、コミット、本文の変更。
- **著者の原文**：日付をどう理解・運用していたか。現段階では未採集。
- **探検隊の解釈**：「年輪の数え方は、庭師の道具として先に生まれていた」「同じ日付。異なる札。異なる読み」「組み立てが公開されなければ、読者の庭は歳を取らない」。いずれも事実そのものではなく、事実に基づく解釈。

**標本01：記録は一時集約、観測はOpen。v0.3 Fixedはそのまま。**
