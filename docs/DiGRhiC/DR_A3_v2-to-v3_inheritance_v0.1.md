
# 庭解剖探検隊｜A-3 V2→V3の継承 v0.1

**記録日：2026-11-19｜作業：綴音（読み取り専用のclone上で集計）｜状態：Open**
**上位プロトコル：v0.3 Fixed（変更なし）｜前段：A-2（DR_A2_v1-to-v2_migration_v0.1）**

## 0｜対象と方法

- V2：`maggieappleton.com-V2`。一括付与 `59438ae`（2021-09-25 23:02 +01:00）から最終コミット `0b1449c`（2025-01-25）まで。ノート・エッセイの最後の変更は 2024-11-13。
- V3：`maggieappleton.com-V3`。ノートの取り込みは `398791e`（2024-12-15 15:36 +00:00「formatted all the notes」、notes 78本）。現在の状態は 2026-11-09 のコミット。
- 突き合わせは slug（なければファイル名）。変更があった場合は、V2時代・V3取り込み時・V3取り込み後のどこで変わったかを切り分けた。

## 1｜41本の複写日付の行方

追跡対象：2021-09-25の一括付与で「旧 `updated` を両方に複写」された42本から FAQ を除いた41本。

| 結果 | 本数 |
| --- | --- |
| 複写されたまま V3 現在まで残存 | 29 |
| V2時代に `updated` だけ書き換え（`startDate` は複写値のまま） | 9 |
| V2時代に talks へ移り、日付も変わった | 2（neocyborgs、reactpotato） |
| V3に見当たらない（V2で drafts へ移動） | 1（ubd） |

- **V3の取り込み時とその後には、41本のどれも日付が変わっていない。** 変化はすべてV2時代に起きている。
- 残存29本の一覧は §5。
- 書き換えられた9本では、`startDate` に V1 時代の単一日付が残り、それが現在 Planted として扱われている。

| 原稿 | 書き換え後の `updated` | 書き換えたコミット |
| --- | --- | --- |
| newharvest-podcast | 2021-09-14 | 2021-10-05「updated growth stage caps」 |
| illustrated-gatsby | 2021-09-20 | 2021-11-21「cleaning up formatting」 |
| metatour | 2021-10-20 | 2021-11-22「fixed formatting on posts」 |
| tracking-humanity | 2021-10-12 | 2021-11-22「fixed formatting on posts」 |
| pattern-languages | 2021-11-13 | 2021-11-22「fotmatting cleanup」 |
| paintingroam | 2021-02-15 | 2021-11-25「formatting foxes」 |
| css-position | 2022-07-10 | 2022-07-09（-04:00）「updated css position graphics」 |
| digital-anth-books | 2022-11-08 | 2022-11-09「added descriptions to anthro books」 |
| cozy-web | 2022-11-28 | 2022-11-28「updated cozy web」 |

宣言された `updated` が、書き換えたコミットの日付より前のものが7本ある（paintingroam は約9か月前、digital-anth-books は1日前）。理由は判定しない。

## 2｜表示の仕組み（コード上の事実）

- **V3**（`src/components/layouts/Dates.astro`）：`updated` が `startDate` と同じなら Last tended を出さない。したがって残存29本の画面には、V1時代の単一日付が「Planted」としてだけ出る（静的ビルドを前提とした推論）。
- **V2**（`components/templates/Dates.js`、2022-04-30 `7bef9a5` 以降）：二つの日付の差が3日未満なら、Planted だけを出し、その値には `updated` を使う。
- V1 の画面では、同じ日付が「Last tended」として出ていた（標本01 §2の表示機構、ただしデプロイは未確認）。

つまり、同じ値が V1 では Last tended、V2・V3 では Planted として示されている。

## 3｜スキーマの必須化

- **V3**：最初の作業版 `fcbacc8`（2024-12-04）の `src/content/config.ts` から、notes・essays・patterns の `startDate` と `updated` が任意指定なしの `z.coerce.date()`。二日付は最初から必須だった。のちの `publication-schemas.mjs` は 2026-09-24 に作られた後発のファイル。
- **V2**：テンプレートとコンポーネントの中に、二日付を要求するスキーマは見つからなかった（網羅的な確認ではない）。
- したがって、**二日付がそろったのは V2 の一括編集（2021-09-25）、必須になったのは V3（2024-12-04）**。原稿がそろっていたことと、スキーマが要求したことは、別の日付で起きている。

## 4｜essays へ移った18本

| V2の途中で notes へ戻った（9本） | 戻ったコミット |
| --- | --- |
| cyborg-history | 2021-10-04「MDX component updates」 |
| note-oppression | 2021-11-05「rearranged backlinsk position」 |
| echo-narcissus、keyboard-maestro、learnable-programming、natureculture | 2021-11-07「moved essays to note」 |
| dirt | 2022-04-29「image optimisations」 |
| keyboard-fetishism | 2022-08-23「downgraded keyboard fetishism to note」 |
| problematic-proteins | 2023-01-03「moved forest to essays」 |

- essays のまま残ったのは9本（artisan-data、bidirectionals、digital-anthropology、garden-history、nontechnical-gardening、paleolithic-nostalgia、still-cant-draw、transcopyright-dreams、xanadu-patterns）。
- **V3は、18本ともV2最終状態の種別と日付をそのまま継承している。**
- V2時代に日付が書き換えられたのは5本。`startDate` 自体が書き換えられた例が2本ある（digital-anthropology：2020-10-14→2020-10-03、still-cant-draw：2020-08-22→2020-08-18）。cyborg-history は `startDate: 2020-11-01` が新たに付いた。

## 5｜残存29本の一覧

babel（2019-02-01）, compilers（2019-05-01）, contentful-gatsby（2019-06-01）, cscl（2020-06-26）, customhooks（2019-11-02）, cypress（2019-05-10）, es2019（2019-06-23）, evergreens（2020-06-28）, fruit-comparison（2019-02-14）, gift-economy（2020-08-03）, git-mistakes（2020-05-21）, graphql（2019-07-30）, greensock-essentials（2020-09-08）, greensock-react（2020-09-27）, immer（2019-08-10）, jsx（2019-01-20）, knowledge-hydrant（2020-06-28）, maintainers（2020-04-30）, react-vdom（2019-01-20）, react360（2019-05-14）, reactsuspense（2020-06-16）, silentsessions（2020-06-19）, spread（2019-01-20）, synecdoche（2020-07-28）, visual-aws（2020-06-16）, vuerouter（2020-01-16）, vuesocket（2019-05-20）, websecurity（2020-02-08）, wtf-rust（2020-01-10）

括弧内は、V1の単一日付＝V2で複写された値＝V3現在の `startDate` と `updated`。

## 6｜三列監査の欄

- **コード・差分**：§1〜§4のすべて。
- **本人の記述（コミットメッセージ）**：「downgraded keyboard fetishism to note」「moved essays to note」。種別の移動を、本人が "downgraded" と呼んだ例が一つある。ノートとエッセイの関係をどう考えていたかの手がかりにはなるが、一語のコミットメッセージなので、それ以上は読まない。
- **探検隊の解釈**：未記入。

## 7｜留保

- V2の相対日付（`formatDistanceToNow`）が、ビルド時と閲覧時のどちらで計算されていたかは未確認。V2にも、標本01のYearsAgoと同じ「時計はどこにあるか」の問いがある。
- V2の2021年秋の時点で、notes のページに日付が表示されていたかどうかは未確認（2021-09-25時点で Planted／Last tended を出していたのは EssayTemplate だけ）。
- 公開の層（どの時点の状態がデプロイされたか）は、どの版でも未確認。
