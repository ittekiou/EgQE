---
layout: math
title: CABA-01｜AIにハビトゥスはあるか？ ──社会理論の問いをAIで実験可能にしてみた記録
---
### CABA-01
# AIにハビトゥスはあるか？
### ──社会理論の問いをAIで実験可能にしてみた記録

## 0｜出発点

もともと持っていた問いはこうだった。ハビトゥスとは、実践を説明するために何をしている概念なのか。身体化された性向から、なぜ実践が生じるのか。

「AIにハビトゥスはあるか」という問いを、Yes/Noで論じるつもりはなかった。代わりに、この問いを実験可能な形へ変換することにした。

## 1｜Habitus Probe 01A

異なる「形成履歴」を与えた、独立した二つのAIエージェントを用意した。

一方(A)には、明示的な規則・構造・不足変数を重視するような例を、三つの短い場面(会議、パン作り、家庭菜園)を通じて事前に見せておく。もう一方(B)には、同じ三つの場面を、暗黙知・経験・関係性を重視する形で見せておく。

そのうえで、両方に同一の新しい曖昧な状況(Encounter X)を提示する。さらに、ドメインを変えながら(パン屋、組織の経費システム、厨房)同型のテストを繰り返した。

観察されたのは、単なる回答の違いではなかった。何を問題として切り出すか、どう診断するか、何を処方するか──この「摂取の仕方」そのものが、ドメインを越えて持ち越されていた。

さらに、強い反証となる状況(Encounter Z)を投入した。両者とも、この反証に応じて診断を反転させた。したがって、これは単なる固定的な条件づけではなかった。一方で、反転後の処方の中に、以前の傾向の残滓らしき挙動が一例、観察された。

ここで一旦止める。

`Transposable Disposition-like Pattern ≠ Habitus`

似たパターンが転移したことと、それをハビトゥスと呼んでよいことは別である。

## 2｜BODY blow 01B

次に、問いを変えた。身体がなければ実践は成立しないのか。

ブルデュー『実践感覚』を原典で読み直しながら、身体が担っている説明の仕事を五つに分解した。Storage(過去はどこに残るか)、Selection/Uptake(何が選択的に取り込まれるか)、Transformation(取り込まれた差異はどう性向へ変わるか)、Generation/Actualization(なぜ今この実践が生成されるか)、Disposal(何が失われるか)。

ここで重要な訂正があった。ブルデューは身体を単純な記憶容器としては扱っていない。「身体は演じるものを記憶しない」という一節が示す通り、表象的な保存モデルはむしろ本人によって明確に退けられている。

問題はその先にある。表象として保存しないのなら、身体化された過去は、どのような機構によって現在の実践に効いているのか。この機構そのものは、原典を読む限り、比喩(沈殿、刻印、ひだ)以上には特定されていなかった。

`Site of Mediation ≠ Mechanism of Mediation`

身体という語は、五つの説明の仕事が起きる「場」を名指してはいるが、それがなぜそこで起きるのかまでは説明していない。

そして身体を掘っていくと、時間が出てきた。

## 3｜TIME blow 01C

Formation、Persistence、Sequence、Interval、Tempo、Hysteresisの六つを、一つずつ原典へ戻して監査した。

ここでも、「ブルデューは時間を説明していない」という単純な批判は成り立たなかった。特にIntervalとTempoについては、贈与と対抗贈与のあいだの間隔がなぜ誤認(méconnaissance)を可能にする装置として機能するか、戦略がなぜテンポの操作そのものとして定義されるか、かなり具体的な機能的説明が与えられていた。

それでも、六つの坑道はすべて同じ一点に収束した。

**なぜ、この状況から、いまこの実践が生じるのか。**

身体側から掘っても、時間側から掘っても、最後にはここへ行き着く。この収束点を、仮に「Actualization-gap」と呼んだ。ただし、この呼び名自体も後で撤回の対象になる。

## 4｜Actualization Probe

AIを使って、後続の出来事が先行する痕跡にどう効くかを、行動レベルで小さくテストしてみた。

最初は物語的な場面(職場の調停)で試した。ある状況への最初の一手を出させ、その途中で新しい情報を割り込ませて続きを生成させる。すると、すでに発せられていた言葉の意味づけそのものが、あとから遡って変化した。

ただし、これは「訓練された物語一貫性がやっているだけ」という対立仮説をそのまま許す結果でもあった。

`Narrative Coherence ≠ Actualization-as-Occurring`

次に、物語性の薄い技術的な診断の場面(サーバーの遅延調査)へ移した。ここで最初の実験には設計上の非対称があった──撹乱情報を入れる側にだけ、最初の一手の「結果」を与えず、行為の宣言だけを渡してしまっていた。

これは失敗だったが、この失敗自体が重要な区別を露出させた。痕跡が担う仕事には、少なくとも「内容(Content)」「意味(Meaning)」「機能・地位(Function/Status)」という三層があるらしい、ということが見えてきた。

## 5｜対称再実験

そこで設計を直し、両条件に同一の診断結果Rを固定して与え、後続の情報だけを変える形で再実験した。

結果、R自体(同じ数値、同じログ)はもちろん同一のまま保たれた。しかし、その数値が何を示す証拠として読まれるか(Meaning)、そして診断の中でどのような地位を占めるか(Function/Status、一次証拠か、副次的な兆候か)は、後続の情報しだいで明確に変化した。

`Trace Content ≠ Trace Meaning ≠ Trace Function/Status`

ここで初めて、観察レベルでこの区別が立った。そして、次の一句が残った。

After comes after Before.
But the work of Before is not finished before After.

過去は過去のあとに来る出来事より前にある。しかし、過去の仕事は、あとに来る出来事より前に終わっているとは限らない。

ただし、これも新しい特殊な機構を発見したわけではない。同じ全証拠を説明し尽くそうとする、ごく普通の推論の働き(abductive coherence)でも説明できてしまう。

`Meaning/Status Reassignment ≠ Distinctively Actualization-level Phenomenon`

この対立仮説は、まだ生きたまま残してある。

## 6｜Vocabulary Self-Audit 01D

最後に、実験の過程で自分たちが使い始めていた説明語を、すべて被告席に並べて監査した。

Actualization、Redistribution、Reassignment、Reinterpretation、Generation、そしてEditing。それぞれの語が、実際には観察していない行為者・操作・機構をこっそり持ち込んでいないか、一つずつ確認した。

最後には、身内の語彙である「Editing」も落ちた。編集という語は、編集者と編集操作に加えて、目的性(何のために編集するのか)までも持ち込んでしまう。今回観察された事実は、そのどれも要求していなかった。

`Different Subsequent Work of a Prior Trace ≠ Editing`

すべての説明語を外したあと、観察事実として残ったのは、これだけだった。

The same prior trace does not do the same work after a different subsequent encounter.

同じ先行する痕跡は、異なる後続の出来事のあとでは、同じ仕事をしない。

主体なし。操作なし。目的なし。

## 7｜この実験でやったこと

最後に、これだけは記録しておきたい。

この実験は、AIにハビトゥスがあることを証明したものではない。

むしろ、長らく持っていた社会理論上の問いを、条件操作・比較・反証・再実験が可能な小さなProbeへと変換してみた記録である。

問い → 実験設計 → 実行 → 結果 → 反証 → 設計ミスの発見 → 再設計 → 再実験 → 語彙監査。この一周を、実際にたどってみた。

途中の設計ミスも、あえて消さずに残した。非対称な設計だったからこそ、「意味」と「機能・地位」という切断面が偶然露出し、それを対称設計で改めてテストし直すことができた。この回り道そのものが、今回のやり方をいちばんよく示していると思う。

---

[CABA-00｜Activityという壁を壊してみた ── CABA｜Activity Bias Audit](https://camp-us.net/articles/CABA-00_Activity-Bias-Audit.html)  
[CABA-01｜AIにハビトゥスはあるか？ ──社会理論の問いをAIで実験可能にしてみた記録](https://camp-us.net/articles/CABA-01_Habitus-AI-Probe.html)  
[CABA-01-note｜過去は終わる。過去の仕事は終わらない。 ──ハビトゥスをAIで実験してみた](https://camp-us.net/articles/CABA-01-note_Habitus-AI.html)  
[CABA-DN｜AI Habitus Probe — 2026-09-16](https://camp-us.net/articles/CABA-DN_AI-Habitus-Probe_2026-09-16.html)  
[CABA-02G-00｜Probe Calibration Ledger](https://camp-us.net/articles/CABA-02G-00_Probe-Calibration-Ledger.html)  
[CABA Probe Record Template](https://camp-us.net/articles/CABA-Probe-Record-Template.html)  

[CABA / TUP Memo｜光・影・Editus](https://camp-us.net/Nukadoko/CABA-TUP_Memo_2026-09-16.html)  

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
<p align="center">| Drafted Sep 16, 2026 · Web Sep 16, 2026 |</p>