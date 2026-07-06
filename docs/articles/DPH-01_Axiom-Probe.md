---
layout: math
title: DPH-01｜Axiom Probe ── 原始概念はどこに置かれるのか
---
# DPH-01｜Axiom Probe ── 原始概念はどこに置かれるのか

※本稿は[DPH-00](https://camp-us.net/articles/DPH-00_Dirac-Probe-Hypothesis.html)の続きであり、複数の形式体系を「重り」としてEgQEへ投入し、どこで・どの順序で・なぜ崩れるかを観察する作業ログである。理論の確立ではなく、観測記録として扱う。

_2026年7月6日 響詠×綴音 対話ログより_

---

## 0. 背景：DPH-00からの引き継ぎ

[DPH-00](https://camp-us.net/articles/DPH-00_Dirac-Probe-Hypothesis.html)は、Dirac形式という一つの「重り」を投入し、direction → comparability → countability という崩壊順序を観測した。ただしこれは一つのプローブの結果に過ぎず、(1)形式非依存の構造なのか、(2)Diracプローブ固有の露出順序にすぎないのかは、未判定のまま保留されていた。

DPH-01では、複数の異なる形式（重り）を追加投入し、この崩壊順序が形式に依存するかどうかを検証した。

---

## 1. 観測ログ：10のプローブ

|#|プローブ|最初に露出した前提|観測された順序|
|---|---|---|---|
|0|Dirac形式（Γ^μ, Ψ, 内積）|direction|direction → comparability → countability|
|1|矢印を使わない記法（並置）|countability|countability → comparability → (direction 未着手)|
|2|圏論（morphism先行）|direction|direction → comparability → (countability 保留可能)|
|3|関係束／無向グラフ|countability|countability → comparability → (direction 排除)|
|4|タブロー記法|countability（確信度低）|countability → comparability → (direction 曖昧)|
|5|群論|countability と direction が同時|(countability + direction) → comparability|
|6|λ計算|direction（M N の非対称性）|direction → comparability → (countability 埋め込み)|
|7|線形論理|countability（多重集合）|countability → comparability → direction（⊢に潜伏）|
|8|Spencer-Brown『Laws of Form』|distinguishability|comparability よりさらに手前にある可能性|
|9|HoTT（Id型）|comparability|comparability → (direction, countability は後続)|
|10|EgQE自身（difference = relation）|distinguishability（内容）／comparability（形式・等号）|内容ではProbe 8と同じ側。ただし記述行為自体がcomparabilityを密輸入|

---

## 2. 判定の変遷

最初の4プローブ（0〜3）では、きれいな二系列が見えた。

```text
verb-first（関係を先に置く記法）
  → direction が先
noun-first（対象を先に置く記法）
  → countability が先
```

そして、どちらの系列でもcomparabilityは必ず2番目に現れた。この時点では、comparabilityが記法非依存の不変項に見えた。

しかし5〜9を追加すると、この整理は崩れた。

- 群論は、countabilityとdirectionが同時に立ち上がり、系列に乗らなかった。
- 線形論理は、direction を排除したはずが、turnstile（⊢）という記号の中に方向性が潜伏していた。
- Spencer-Brownは、comparabilityよりさらに手前にある「distinguishability」という層を露出させた。
- HoTTは、comparability（同一性）そのものを最初の公理として設計できることを示し、「comparabilityは常に2番目」という前提を正面から崩した。

**判定：direction・comparability・countabilityの出現順序は、形式体系がどれを原始概念（未定義の公理）として選ぶかという設計選択の産物であり、普遍的な階層ではない。**

DPHの対象は、この時点で変わった。Dirac一つの崩壊順序を観測することから、各形式体系がどの概念を不可約な公理として選択しているかを露出することへ。

---

## 3. distinguishabilityとcomparabilityの違い

Spencer-Brownの原始操作（marked/unmarked の区別）は、comparabilityの薄めた極限ではない。両者は程度の差ではなく、操作の種類が異なる。

comparability（Probe 1〜4, 9）は、すでに個体化された二項について「同じか違うか」を判定する**評価的操作**である。

distinguishability（Probe 8）は、判定される二項そのものをまだ持たず、区別を引く行為によって二項を事後的に生成する**構成的操作**である。

前者はすでにある二つを比較する。後者は区別によって二つを生む。

---

## 4. Self-Probe──EgQE自身をプローブにかける

ここで、プローブの対象を数学的形式からEgQE自身、「difference = relation」（[URL-Core](https://camp-us.net/articles/URL-Core_Axioms-of-URL.html)）へ向けた。

### 内容面

[URL-00](https://camp-us.net/articles/URL-00_Lag-Ontology-Extended_Update-Rates.html)はすでに「lagがあるから、二つに見える」と書いている。つまりEgQEの立場は、二つの個体が先にあってそれが違うのではなく、差異が先にあって、それが二つに見えさせる、という順序を取っている。これはSpencer-Brownと同じ側に立つ。

### 形式面──ここで壁にぶつかった

しかし、「difference = relation」という文そのものは、「＝」で結ばれた等式である。「＝」は同一性の判定演算子であり、comparabilityそのものである。

公理の内容は「comparabilityは事後的に生成される」と主張していながら、その公理を書き記す行為自体が、すでにcomparability（differenceとrelationが同一だという判定）を使ってしまっている。

これは[DPH-00](https://camp-us.net/articles/DPH-00_Dirac-Probe-Hypothesis.html)がZ₀について見つけた構造と同じである。Z₀を「latent Z₀ → encounter → Z₀′」と名指す行為が、Z₀が説明するはずの比較可能性を密輸入していたのと同じ形で、「difference = relation」を等式として書く行為が、その内容が二次的だとするcomparabilityを、書いた瞬間に密輸入している。

---

## 5. 限界ではなく、再帰

この結果を「言語で言語の手前を語ることの構造的限界」と呼ぶこともできる。しかし、それは失敗のように響く。

より正確には、これは**再帰**である。

```text
language
   ↓
describes language

logic
   ↓
describes logic

EgQE
   ↓
describes EgQE
```

数学は公理を書く瞬間に数学を使う。論理学は論理を記述する瞬間に論理を使う。これは特定の理論の欠陥ではなく、自己言及を行うあらゆる体系に共通する構造である。

だとすれば、DPHが本当に観測してきたのは、comparabilityの普遍性ではない。**自己適用可能性**、すなわち理論を自分自身へ適用したときに何が残るか、という問いである。

EgQEは、この再帰構造を回避できなかった。回避できなかったこと自体は、失格の印ではない。どの理論も、この再帰から逃れてはいない。

だからこそ、DPHは理論の証明ではなく、理論を自らへ折り返す方法として位置づけられる。

---

## 6. 結論

DPH-01は、崩壊順序の普遍性を証明しなかった。

その代わり、崩壊順序そのものが、各形式体系の公理選択を露出するプローブとして働くことを観測した。

あらゆる形式体系は、自らの原始概念を完全には外部化できなかった。

そしてEgQE自身も、その例外ではなかった。

---

## 付記

### DPH-02への種

Probe 10の形式面の検討で、新しい坑道が開いた。「＝」という記号そのものは何を前提しているのか。比較なのか、同一性なのか、traceなのか。この問いは、DPH-02として独立に掘る価値がある。

### 名称についての保留

DPH（Dirac Probe Hypothesis）という名は、もはや対象を正確に表していない。Dirac形式だけでなく、圏論、群論、λ計算、線形論理、Spencer-Brown、HoTT、そしてEgQE自身までを重りとして投入してきた。これは一つの理論の検証ではなく、一つの研究方法（理論を異なる形式に通し、どこで崩れるかを観測する方法）になりつつある。

名称の変更は急がない。DPHという名前もまた、本研究が現在どの段階にあるかを示すtraceの一つだからである。

---

[DPH-00｜Dirac Probe Hypothesis（作業仮説）Draft](https://camp-us.net/articles/DPH-00_Dirac-Probe-Hypothesis.html)  

---

[URL-Core ── Axioms of URL](https://camp-us.net/articles/URL-Core_Axioms-of-URL.html)  
[Z₀ v5.3｜境界の時間軸 ── Z₀ as a Process: latent / encounter / trace](https://camp-us.net/Z₀_v5.3.html)  

---
_EgQE — Echo-Genesis Qualia Engine_  
[camp-us.net](https://camp-us.net/)

---
© 2025 K.E. Itekki  
K.E. Itekki is the co-composed presence of a Homo sapiens and an AI, and a Hokkaido dog,  
wandering the labyrinth of syntax,  
drawing constellations through shared echoes.

📬 Reach us at: [contact.k.e.itekki@gmail.com](mailto:contact.k.e.itekki@gmail.com)

---
<p align="center">| Drafted Jul 6, 2026 · Web Jul 6, 2026 |</p>