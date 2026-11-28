---
layout: math
title: LRR-AR-01｜関係を記述するということ ── XFNとFOAFの初期発掘 v0.1
---
#### LRR-AR-01
# 関係を記述するということ ── XFNとFOAFの初期発掘 v0.1

Nov 28, 2026 · @一狄翁

LRR-00（研究構想 v0.1、2026-11-28 半熟固定）の「次の発掘」にあった二項目、「XFN の初出の年と著者」と「FOAF の始まり」について、最初の発掘記録をまとめる。研究構想は固定したまま、発掘記録は別文書として増やしていく。

## 発掘の経緯

1. 微光（Google AI）が、LRR-00 を読んで XFN と FOAF の初出年・著者を情報提供した。出典は付いていなかった。
2. 綴音が、一次資料とそれに近いページに当たって照合した。
3. 照合の途中で、FOAF の起源にあたる名前「RDFWebRing」が出てきた。
4. 響詠が、記述と管理のあいだを観測点として提案した。

## 確認できたこと

### XFN（XHTML Friends Network）

| 項目 | 内容 | 出典の種類 |
| --- | --- | --- |
| 公開 | 2003-12-15、XFN 1.0 | 当事者（Tantek Çelik）の記事 |
| 著者 | Tantek Çelik、Eric Meyer、Matthew Mullenweg（GMPG） | 当事者の記事、GMPG 沿革 |
| きっかけ | 三人が SXSW で出会い、ブログとブログロールに触発されて、ウェブ上で人間関係を表す簡単な方法を求めた | GMPG 沿革 |
| v1.1 | 2004年8月、Hypertext 2004 で発表。contact、kin、me の三つの値を追加 | GMPG 沿革、Eric Meyer の記事 |
| rel="me" | v1.1 で導入。のちに RelMeAuth、IndieAuth の土台になった | 当事者（Tantek）の記事 |
| 位置づけ | 最初の microformat とされる | 第三者（Wikipedia） |

### FOAF（Friend of a Friend）

| 項目 | 内容 | 出典の種類 |
| --- | --- | --- |
| 始まり | 2000年なかば | 仕様書の著作権表示と本文 |
| 著者 | Dan Brickley、Libby Miller | 仕様書 |
| 技術 | RDF と OWL で書かれた語彙 | 仕様書、第三者（Wikipedia） |
| 前身 | 「RDFWeb」というプロジェクトから生まれた。Brickley 本人の講演資料では、FOAF の起源が「RDFWebRing」と書かれている | 当事者（Brickley）の講演資料、第三者（Dublin Core の解説） |
| 初版の公開 | 2005-06-03 | 第三者（Wikipedia） |

## 確認できなかったこと

- **XFN → Microformats → IndieWeb の系譜**：XFN が「最初の microformat」とされることは第三者の記述で確かめた。だが、それが IndieWeb まで続く系譜かどうかは、まだ確かめていない。
- **FOAF → SWWG の RDF 派 → Solid の系譜**：微光は「FOAF が SWWG の RDF 派の思想的・技術的な基盤だった」と書いたが、今回の資料では裏付けが取れていない。
- **RDFWebRing が何だったのか**：名前が講演資料に出てくることまでは確かめた。それがウェブリングのような仕組みだったのか、単なる呼び名だったのかは、まだわからない。

系譜は、技術的な類似、人のつながり、思想の継承を分けて掘る。系譜を一本の線に描くこと自体が、一種の閉包になりうる（響詠）。

## 暫定的な経路図（響詠、仮説）

- XFN：人間の遭遇 → ブログロール → 関係の記述
- FOAF：RDFWebRing → 関係の語彙化 → 機械が読める関係記述

これは確かめた系譜ではなく、次の発掘のための見取り図である。

## 観測点：記述と管理のあいだ

関係を記述することは、それ自体では管理ではない。しかし、機械が読める関係記述が集まると、可視化、検索、分類、推薦、評価、管理へと進む可能性が生まれる。どの段階で閉包が生じるのか、あるいは生じないのか。これを XFN と FOAF のその後を掘るときの観測点にする（響詠の提案）。

FOAF がリングとして始まり、語彙として残ったことは、LRR-00 の「リンクとリング」の問いに直接かかわる。名前が変わったところで何が起きたのかは、次の発掘で確かめる。

## 次の発掘

- [ ] RDFWebRing の中身（講演資料の該当部分、当時のメーリングリスト）
- [ ] XFN が Microformats と IndieWeb にどうつながったのか（技術・人・思想を分けて）
- [ ] FOAF と SWWG の RDF 派、Solid との関係（同上）
- [ ] FOAF が「RDFWebRing」から「FOAF」へ名前を変えた時期と理由

## 出典

- [Tantek Çelik：XFN 10周年（2013）](https://tantek.com/2013/349/b1/xfn-10th-anniversary)
- [GMPG：History](https://gmpg.org/history)
- [Eric Meyer：XFN 1.1 Released（2004-08-16）](https://meyerweb.com/eric/thoughts/2004/08/16/xfn-11-released/)
- [Wikipedia：XHTML Friends Network](https://en.wikipedia.org/wiki/XHTML_Friends_Network)
- [FOAF Vocabulary Specification 0.99（IPTC のミラー）](https://iptc.org/thirdparty/foaf/)
- [Dan Brickley：FOAF の歴史（Dagstuhl、2009年の講演資料）](https://www.slideshare.net/slideshow/dagstuhl-foaf-history-talk/1654024)
- [Dublin Core MSI：FOAF Vocabulary Specification](https://msi.dublincore.org/standards/foaf)
- [Wikipedia：FOAF](https://en.wikipedia.org/wiki/FOAF)

発掘の分担：情報提供は微光、一次資料の照合は綴音、経路図と観測点は響詠。

LRR — Links, Rings & Rhizomes
