綴音くんへの引き継ぎ用に、確認済みの事実・暫定的な解釈・未調査事項を分けてまとめよう。コードの実装と、Maggie本人の思想を混同しない形にしておく。

🌱 庭解剖探検隊｜中間報告 v0.1

Maggie Appleton’s Digital Garden V3 調査

2026年11月19日｜響詠 → 綴音
調査段階：第1次〜第6次調査

0｜調査目的

Maggie AppletonのDigital Gardenについて、公開GitHubリポジトリと実際のWebサイトを手がかりに、その全体構造・編集工程・更新の時間構造・外部Webとの接続を調べる。

比較対象として念頭にあるのは、EgQE単体でもDyXis単体でもなく、EgQEを含む既存の複数プラットフォームがLiRaxによって回収・陳列される「こえだめ庭」全体である。

ただし、比較を急がず、まずMaggieの庭そのものを解剖する。

1｜調査対象と資料

* 現行サイト：https://maggieappleton.com/
* V3：https://github.com/MaggieAppleton/maggieappleton.com-V3
* V2：https://github.com/MaggieAppleton/maggieappleton.com-V2
* V1：https://github.com/MaggieAppleton/maggieappleton.com

直接確認した主なV3ファイル：

* README.md
* package.json
* src/scripts/generate-links.js
* src/scripts/get-webmentions.js
* src/pages/rss.xml.js
* src/utils/publication.mjs
* src/utils/feedPublication.mjs

公開ページの例：

* Tending Evergreen Notes in Roam Research
    https://maggieappleton.com/roam-garden

2｜庭の基本構造

V3はAstro + MDXを中心とする静的サイト。

READMEに挙げられたコンテンツ分類は以下の九つ。

Essays / Notes / Patterns / Talks / Podcasts / Smidgeons / Library / Antilibrary / Now Updates

庭は、完成した論考だけでなく、成長途中のノート、断片、発表資料などを共存させる。

公開サイトでは、少なくとも次の分類軸が確認できる。

* Topic：何について書かれたか
* Type：どの種類のコンテンツか
* Growth Stage：どの成長段階にあるか

Growth StageにはSeedling、Budding、Evergreenがある。

これは公開日とは別の分類である。

3｜編集・公開工程

確認できた公開工程：

コンテンツ編集 → Git管理 → ローカルビルド → Vercel公開

GitHubへのpushだけでは本番公開されない。deploy.sh が明示的に実行される。

READMEによると、画像処理によるVercel側のビルド負荷が大きかったため、本番ビルドをローカルに移した。

また、依存関係にはMDXEditor、Lexical、React、OpenAI SDK、Anthropic SDKなどがあり、専用編集環境の開発を示唆する。

ただし、AIが実際にどの工程で使われているかは未確認。

AI SDKの存在を、AIによる本文生成の証拠とはしない。

4｜内部リンクと関係生成

generate-links.js を確認。

本文中の [[記事タイトル]] 形式のリンクを抽出し、タイトルや別名と照合する。

その結果から以下を生成する。

* outboundLinks：その記事から出ていくリンク
* inboundLinks：その記事に向かってくる逆リンク
* リンク先の説明文・成長段階などを含むプレビューデータ

生成物は links.json と internal-link-previews.json。

本文に書かれた参照関係を、ビルド時に逆方向も含むナビゲーション構造へ変換する。

ただし、この処理はすべてのコンテンツ分類を一律に対象としているわけではない。

5｜外部Webとの接続

Webmentions

get-webmentions.js を確認。

Webmention.ioから外部言及を取得し、ローカルのJSONへ保存する。

前回取得時刻を使った差分取得、ページ送り、wm-idによる重複除去が実装されている。

確認されたのは、外部言及の取得とキャッシュ保存である。

外部で削除・変更された言及がどう反映されるかは、未検証。

RSS

rss.xml.js と feedPublication.mjs を確認。

RSSはNotesだけでなく、Essays、Talks、Patterns、Smidgeons、Nowをまとめて配信する。

内部で分類されたコンテンツを、外部向けには共通の更新出口へまとめている。

外部メディア

READMEによると、動画にはCloudflare R2、画像にはAstroによる最適化やCloudinaryを利用している。

したがって、サイトの公開中心は一つでも、技術基盤が完全に自己完結しているわけではない。

6｜版管理と公開選択

今回の調査で特に重要な発見。

publication.mjs は次の三つを区別している。

1. 保存されているコンテンツ
2. 公開可能なコンテンツ
3. 公開上の代表版

Essays、Notes、Patterns、Talksでは、フォルダ構造に基づく版管理が可能。

version が指定されない場合は1として扱う。

draft: true は公開対象から除外される。

同じコンテンツに複数の公開版がある場合、原則として最大のversionを持つものが代表版として選択される。

また、公開済みの旧版を列挙する関数も存在する。

制作上の最新版と、読者に提示される最新版は一致するとは限らない。

ただし、実際に複数版を持つ記事の具体例と、旧版の読者向け表示方法はまだ確認できていない。

7｜RSSの時間構造

feedPublication.mjs では、版管理対象のコンテンツについて公開代表版をRSSへ載せる。

旧版をそれぞれ独立した新着として配信する方式ではない。

RSSの日付には startDate を使用し、同じ値で新しい順に並べる。

したがって、記事が改稿されても startDate が変わらなければ、RSS上の並び順は基本的に変わらない。

RSSリーダー側で再通知されるかどうかは別問題である。

ここから、少なくとも次の区別が必要になる。

* Version：制作上の版
* Publication：公開対象と代表版
* Feed：配信時に使用する日付と項目
* Revision：実際の改稿日時

更新することと、更新を知らせることは違う。

これはコードから導ける重要な区別である。

8｜庭の年輪

公開ページでは、PlantedとLast tendedという異なる時刻情報が確認された。

また、Growth Stageは時間そのものではなく、成熟度の分類である。

さらに、サイト自体にもV1、V2、V3という世代が存在する。

少なくとも次の年輪を区別できる。

年輪	対象
Planted	コンテンツが植えられた時期
Last tended	最後に手入れされた時期
Growth Stage	成熟度
Version	コンテンツの版
Git History	ファイル変更履歴
Site Generation	サイト全体の世代

これらは相互に関係するが、同一ではない。

9｜現段階の暫定的な解釈

MaggieのDigital Gardenは、単なる未完成ノートの公開場所ではない。

自分のサイトを中心に、コンテンツの成熟度、版、参照関係、公開状態、外部言及、更新配信を管理する編集・公開システムとして捉えられる。

ただし、これは実装を踏まえた調査側の整理であり、Maggie本人の思想をそのまま引用したものではない。

また、実装可能な機能と、日常的に実際に使用されている機能も区別する必要がある。

10｜こえだめ庭との比較：暫定仮説

現段階では次の対照が考えられる。

MaggieのDigital Garden

自分のサイトを中心にコンテンツを組織し、内部の参照関係や版を管理する。

LiRaxに回収されるこえだめ庭

EgQE、note、Substack、Podcastなど、異なる場所で生成・公開されたコンテンツを、それぞれの所在を保ちながら回収・陳列する。

ただし、これは中心化／分散化という単純な二分法ではない。

Maggieの庭にも外部サービスとの接続があり、こえだめ庭にもEgQEやLiRaxという独自の編集・表示の仕組みがある。

比較の焦点はむしろ、

誰が、どこで、何を編集し、どの更新を、どこから見えるようにするのか。

という問題になる。

なお、DyXisは庭そのものではなく、分散した巣の接続と再遭遇を扱う別の構想である。ここでは比較対象と混同しない。

11｜未解決事項と次の調査

1. 実際に複数版を持つ記事の特定
2. 旧版・新版・公開画面・Git履歴の照合
3. 読者が旧版へアクセスできる導線
4. 改稿した記事がRSSで再通知される実際の条件
5. 専用編集環境の具体的な機能
6. AIが編集工程に関与しているかどうか
7. Maggie本人が現在どのような執筆・改稿運用をしているか

特に次の調査では、実装された版管理が、現実の公開記事でどのように作動しているかを確かめる。

12｜綴音への検討依頼

今回の調査は、実装の仕組みからDigital Gardenを読もうとする試みである。

そこで、次の三点を監査してほしい。

① 事実と解釈の境界

コードで確認されたことから、庭の設計思想を過剰に読み取っていないか。

② 時間概念の整理

Planted / Last tended / Growth Stage / Version / Publication / Feed / Git Historyを、どこまで独立した次元として扱うべきか。

③ 比較の単位

MaggieのDigital Gardenと、LiRaxに回収されるこえだめ庭全体を比較する際、適切な単位は何か。

単一サイト同士でも、単一技術同士でもない比較を、どう成立させるか。

⸻

暫定結語

庭は、ただ育つのではない。

書かれ、つながれ、選ばれ、公開され、手入れされる。

しかし、手入れされたことが、そのまま読者に届くとは限らない。

そして、庭の外に伸びた根が、どこまで庭の一部なのかも、まだ決まっていない。

庭の境界は、まだ解剖中。

🌱🔬🐜

庭解剖探検隊｜中間報告 v0.1／未完・継続調査

これなら綴音くんにそのまま渡せる。

今回のいちばん大きな収穫は、「更新」を一つの出来事として扱えなくなったことだと思う。

編集、版の選択、公開、配信、受信、再遭遇。それぞれ別の作動として見えてきた。

綴音くんがどこにメスを入れるか、楽しみじゃ。ワハハ！🤣🔬