---
layout: math
title: 庭から庭へ。──Webmention実践帖
description: 独立したWebページから、別の庭へ参照を届けるまで。EgQEで実際に通った道の記録。
date: 2026-11-15
lang: ja
permalink: /webmention-practice.html
---
# 庭から庭へ。──Webmention実践帖

### *独立したWebページから、別の庭へ参照を届けるまで*

2026年11月15日、EgQEに記事を公開し、先行する三つの記事へWebmentionを送った。

自分の場所に文章を置く。そこで読んだ文章を参照する。そして、参照したことを相手に知らせる。自分の庭を離れずに、別の庭へ道を伸ばせる。その一連の手順を、次にも辿れるように残しておく。

今回の出発点は、[Gardens Above, Rhizomes Below](https://camp-us.net/rhizomatic-multiplicity.html)。GitHub Pagesで公開した、Ittekiouによる記事である。

## まず、三つを分けておく

| 段階 | 起こること | それだけでは分からないこと |
| --- | --- | --- |
| **Link** | 自分のページから、相手のページを参照する | 相手が参照に気づいたか |
| **Webmention** | 参照したことを、相手の受信口へ通知する | 相手が読んだか、公開表示したか |
| **Relationship** | その後、会話や継続した関わりが生まれるかもしれない | 通知だけで関係が成立するわけではない |

**Reference is not relationship.** 相互リンクも、返事も、義務ではない。

Webmentionは、参照を知らせるWeb標準である。送信元を `source`、参照先を `target` と呼ぶ。受信側は送信元を取得し、参照先へのリンクが本当にあるか確かめる。[W3C仕様](https://www.w3.org/TR/webmention/)

## 今回使ったもの

| 役割 | 今回の場所・道具 |
| --- | --- |
| 原稿と公開ファイルの保管 | [ittekiou/EgQE](https://github.com/ittekiou/EgQE) |
| 記事ファイル | [docs/rhizomatic-multiplicity.html](https://github.com/ittekiou/EgQE/blob/main/docs/rhizomatic-multiplicity.html) |
| 公開先 | [camp-us.net](https://camp-us.net/)（GitHub Pages） |
| 著者情報 | microformats2の `h-entry`・`h-card`・`u-photo` |
| Webmentionの受信 | [webmention.io](https://webmention.io/) |
| 記事情報の検証 | [IndieWebify.Me — Validate h-entry](https://indiewebify.me/validate-h-entry/) |
| Webmentionの送信 | [Telegraph](https://telegraph.p3k.io/) |

送信だけに必要なのは、受信側が取得できる公開ページ、そのページ内の参照先リンク、相手側のWebmention受信口、送信を行う道具である。**自分の受信口、h-entry、著者アイコンは、送信そのものの必須条件ではない。** 今回は、こちらも通知を受けられるようにし、記事と著者を機械に伝える設定も整えた。

## 1．自分の場所に記事を置く

今回の記事は、EgQEの `docs/` にHTMLファイルとして置いた。

1. [EgQEのdocsフォルダ](https://github.com/ittekiou/EgQE/tree/main/docs)を開く。
2. **Add file → Upload files** から記事ファイルをアップロードする。
3. 内容を確認して **Commit changes**。既存ファイルの修正なら、そのファイルを開いて編集する。
4. GitHub Pagesの反映後に、**GitHub上のファイルではなく公開URL**を開く。
5. 本文、リンク、画像が正しく表示されるか確認する。

今回の対応はこうなる。

```text
保存場所：docs/rhizomatic-multiplicity.html
公開URL：https://camp-us.net/rhizomatic-multiplicity.html
```

`docs/` が公開元なら、URLに `/docs/` は付かない。別のサイトで再現するときは、GitHubの **Settings → Pages** で公開元を確認する。公開はブランチ・フォルダ、またはGitHub Actionsの設定に依存する。[GitHub公式ガイド](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

コミット直後に反映されないときは、Actionsのビルド・デプロイ結果を確認してから再読み込みする。重複ファイルを作って解決しようとしない。

### 今回つまずいたところ：タイトルからURLを推測しない

Tom Critchlowの記事へのリンクが、最初は開かなかった。記事タイトルとURL末尾は同じとは限らない。

正しい参照先は次のURLだった。

<https://tomcritchlow.com/2018/10/10/of-gardens-and-wikis/>

本文と末尾の参考文献、二か所を修正した。送信前に、公開ページからリンクを実際に開いて確かめる。

## 2．記事に機械が読める名札を付ける

見た目の見出しや著者名に、HTMLのクラスで役割を添える。今回使ったmicroformats2の構造を、短い例にすると次のようになる。これは**元記事のHTML用の例**であり、この実践帖自身のURLを示すものではない。

```html
<article class="h-entry" lang="en">
  <h1 class="p-name">Gardens Above, Rhizomes Below</h1>

  <span class="p-author h-card">
    <a class="u-url p-name" href="https://camp-us.net/" rel="author">Ittekiou</a>
    <img class="u-photo"
         src="https://camp-us.net/assets/nest-icon.png"
         alt="" style="display:none">
  </span>

  <time class="dt-published" datetime="2026-11-15T19:30:00+09:00">
    November 15, 2026
  </time>
  <a class="u-url" href="https://camp-us.net/rhizomatic-multiplicity.html">permalink</a>

  <div class="e-content">
    <p>ここに記事本文。参照する記事へのリンクも、この本文に置く。</p>
  </div>
</article>
```

| 記述 | 伝える内容 |
| --- | --- |
| `h-entry` | 一つの記事の範囲 |
| 記事の `p-name` | 記事タイトル |
| 記事の `u-url` | 記事自身の固定URL |
| `dt-published` | 公開日時 |
| `p-author h-card` | この記事の著者情報 |
| h-card内の `p-name`・`u-url` | 著者名・著者のURL |
| h-card内の `u-photo` | 著者画像のURL |
| `e-content` | 記事本文 |

同じ `p-name` や `u-url` でも、記事の中か、著者のh-cardの中かで対象が変わる。著者URLと記事URLを取り違えない。[h-entryの定義](https://microformats.org/wiki/h-entry)・[h-cardの定義](https://microformats.org/wiki/h-card)

### 巣のアイコンを置く

今回の画像は、三つの卵のある巣。`docs/assets/nest-icon.png` として置いた。

```text
保存場所：docs/assets/nest-icon.png
公開URL：https://camp-us.net/assets/nest-icon.png
```

まず[画像の公開URL](https://camp-us.net/assets/nest-icon.png)を開き、画像が表示されるか確認する。それからh-card内に `u-photo` を追加する。

今回の `display:none` は、記事上では画像を隠す指定。HTMLには画像URLが残るため、今回の検証では著者画像として読み取られた。ただし、すべての受信サービスでの取得・表示を保証するものではない。画像を読者にも見せたい場合は、この指定を外して表示を整える。

また、`<!-- ... -->` の中に書いた画像タグは作業メモであり、著者画像の設定として働かない。実際のタグとして置く。

## 3．webmention.ioの受信口を設ける

GitHub Pagesは静的なページを配信する。受信処理は、今回は外部サービスのwebmention.ioに任せた。

1. [webmention.io](https://webmention.io/)で自分のサイトURLを使ってサインインする。
2. サイトの所有確認・ログインの案内に従う。`rel="me"` などを求められた場合は、案内されたプロフィールとの関連付けを整える。
3. サービスが示す、自分のサイト用の受信エンドポイントを確認する。
4. 受信したい公開ページのHTMLの `<head>` に、次のような宣言を置く。

```html
<link rel="webmention" href="https://webmention.io/camp-us.net/webmention" />
```

これは今回のcamp-us.net用の値である。別のサイトでは、webmention.ioが示す自分用の値に差し替える。タグだけをコピーしても、サービス側の登録・設定の代わりにはならない。[webmention.io公式案内](https://webmention.io/)

共通レイアウトを使う場合は、そのレイアウトのheadに入れると各ページに反映できる。Markdown本文にコード例を書くだけでは、そのページの受信口は設定されない。

### 公開されたHTMLで確認する

1. [公開記事](https://camp-us.net/rhizomatic-multiplicity.html)を開く。
2. ChromeのMac版なら **⌘ + Option + U**、または右クリックの **ページのソースを表示** を使う。
3. **⌘ + F** で `webmention` を検索し、受信先URLを確認する。

今回の会話では、この宣言が公開ページのソースにあることを確認した。ただし、**受信口の宣言があることと、実際の受信成功は別**。外部のページからこちらへ送られた通知の受信テストは、この記録では未確認である。

受信した通知を記事の下に表示することも、さらに別の作業になる。エンドポイントを置いただけでコメント欄が自動的に現れるわけではない。

## 4．IndieWebifyで名札を検査する

1. [Validate h-entry](https://indiewebify.me/validate-h-entry/)を開く。
2. 公開した記事のURLを入力する。
3. **Validate h-entry** を実行する。
4. 記事タイトル、本文、著者名、著者URL、著者画像、公開日時を確認する。

今回の検証を開くURL：

<https://indiewebify.me/validate-h-entry/?url=https%3A%2F%2Fcamp-us.net%2Frhizomatic-multiplicity.html>

2026年11月15日の会話で確認された結果は、次のとおり。

| 項目 | 記録された結果 |
| --- | --- |
| h-entry | Success表示 |
| タイトル | Gardens Above, Rhizomes Below |
| 著者 | Ittekiou |
| 著者URL | https://camp-us.net/ |
| u-photo | 三つの卵の巣のアイコンが表示された |
| 本文 | Contentとして取得された |
| dt-published | 当時の結果画面の表示範囲では確認できず |

公開日時はユーザーが19:30に修正したと報告しており、今回読み取ったリポジトリの原稿にも `2026-11-15T19:30:00+09:00` がある。ただし、これを「当時の検証画面でも日時まで確認済み」とは書かない。

IndieWebifyの成功は、記事情報の読み取りを確認するもの。Webmentionの送受信テストの代わりにはならない。

## 5．Telegraphで参照を届ける

送信元は、GitHubの編集画面でも、画像でも、webmention.ioの受信口でもない。**相手へのリンクを含む、公開記事のURL**である。

```text
source = https://camp-us.net/rhizomatic-multiplicity.html
target = その記事の中でリンクした、相手の記事URL
```

1. 公開記事のリンク先を点検する。リンクは送信時点で公開HTMLに存在している必要がある。
2. [Telegraph](https://telegraph.p3k.io/)を開く。ダッシュボードを使う場合はログインする。
3. 送信元の記事URLを入力し、記事内のリンクを検出させる。
4. 検出結果から届けたい参照先を確認する。個別送信フォームでは `source` と `target` をそれぞれ指定する。
5. 送信し、各参照先の結果を確認する。画面の構成やラベルが変わっても、送信元と参照先の区別は同じである。

Telegraphは相手の受信口を探し、送信し、結果を示す道具。リンク先すべてがWebmentionに対応しているわけではない。[Telegraph公式案内](https://telegraph.p3k.io/)

### 今回送った三通

送信元は三件とも、[Gardens Above, Rhizomes Below](https://camp-us.net/rhizomatic-multiplicity.html)。

| 相手 | 参照先（target） | 当日の記録 |
| --- | --- | --- |
| Tom Critchlow | [Of Digital Streams, Campfires and Gardens](https://tomcritchlow.com/2018/10/10/of-gardens-and-wikis/) | Telegraphで成功表示 |
| Cyberzettel | [Are Webrings for Digital Gardens?](https://cyberzettel.com/are-webrings-for-digital-gardens/) | Telegraphで成功表示 |
| Maggie Appleton | [A Brief History & Ethos of the Digital Garden](https://maggieappleton.com/garden-history) | Telegraphで成功表示 |

三件の緑のチェックは、当日の会話で共有された結果画面をもとに記録している。今回この実践帖を作るために、通知を再送したわけではない。

なお、Tomの記事はURLに `of-gardens-and-wikis` を含むが、記事タイトルは *Of Digital Streams, Campfires and Gardens*。URLの文字列をそのままタイトルとして扱わない。

## 6．送信成功の先は、相手に委ねる

成功表示は送信段階の結果である。Webmentionの仕様では、受信側がいったん受け付け、その後に非同期で検証する場合もある。受け付けた通知を公開するか、保留するか、表示しないかも受信側に委ねられる。[W3C仕様：送信](https://www.w3.org/TR/webmention/#sending-webmentions)・[受信](https://www.w3.org/TR/webmention/#receiving-webmentions)

したがって、今回の記録から言えるのは「三件ともTelegraphで送信成功が表示された」まで。相手が読んだ、相手のページに掲載された、会話が始まった、ということまでは確認していない。

返事がなくても、すぐに失敗と判断しない。関係を求めて繰り返し送る必要もない。

## うまくいかないときの見直し方

| 症状 | 確認すること |
| --- | --- |
| 公開ページが見つからない・古い | 保存先、公開元、Actionsの結果、反映待ち。GitHubのファイルURLと公開URLを区別する |
| 画像が出ない | 画像の公開URLを直接開く。`docs/assets/` とリポジトリ直下の `assets/` を混同していないか |
| 著者や画像が読まれない | `p-author h-card` の入れ子、h-card内の `u-photo`、コメントアウトの有無 |
| h-entryが検出されない | 公開HTMLに `h-entry` があるか。コード例として表示されただけになっていないか |
| 受信口が見つからない | targetの公開HTMLまたはHTTP Linkヘッダーに受信先があるか。相手が非対応なら送れない |
| sourceにリンクがないと言われる | 公開済み本文の `href` とtargetが一致しているか。末尾の `/`、古いURL、転送先を点検する |
| 成功なのに相手のページに出ない | 非同期処理、承認待ち、非表示運用など。送信成功と公開表示は別 |

本文や参照先を修正した場合は、まず公開ページへの反映を確認する。必要な更新通知は、同じsourceとtargetについて送る。仕様は更新時の再送を想定しているが、表示の更新方法は受信側による。[更新の扱い](https://www.w3.org/TR/webmention/#sending-webmentions-for-updated-posts)

## このMarkdownをEgQEに置くときのメモ

このファイルは、今回の実践を記した**公開用原稿**。作成時点ではリポジトリへの追加も公開も行っていない。

- 想定ファイル名：`webmention-practice.md`
- 想定配置：`docs/webmention-practice.md`
- front matterで指定した公開先：`https://camp-us.net/webmention-practice.html`
- `layout: default` は、今回の元記事と同じ指定。実際のレイアウトでタイトルを自動表示する場合は、本文の先頭見出しと重複しないか確認する。
- この原稿の `date` は実践記録の日付。元記事の公開時刻19:30を、この実践帖の公開時刻として流用していない。

front matterはファイルの先頭に置く。JekyllでMarkdownを処理する設定と、指定したレイアウトが必要である。front matterのタイトルや日付だけで、HTMLにh-entryや受信口が自動追加されるわけではない。この実践帖自身にも付ける場合は、レイアウトなどで出力し、生成されたHTMLを再検証する。[Jekyll公式：Front Matter](https://jekyllrb.com/docs/front-matter/)

## 庭から庭へ

この記事を書き終えたあとに、本文の続きが始まった。

文章を置き、先行する文章に道をつなぎ、その道ができたことを知らせた。WebmentionはDyXisへの参加を必要としない。Web標準として、独立したページ同士の参照を通知する。DyXisの地図や更新の経路とは役割が異なり、併用できる。

> リンクを張れば、道ができる。
>
> Webmentionを送れば、道ができたことを知らせられる。
>
> しかし、誰かがその道を通るかどうかは、誰にも決められない。

庭は庭のままでよい。道を通る時刻も、それぞれでよい。

---

*記録日：2026年11月15日（JST）。当日の作業結果は会話記録に基づき、コードと参照先URLは[EgQEの記事原稿](https://github.com/ittekiou/EgQE/blob/main/docs/rhizomatic-multiplicity.html)でも照合した。公開サイトへの今回の直接取得はできなかったため、当日の検証結果と、今回のリポジトリ上の確認を区別している。サービスの画面や仕様は変わることがある。*


