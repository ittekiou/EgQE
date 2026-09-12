---
layout: math
title: TUP-DN-04｜Traceなしで、どこまで記述できるか
title_en: TUP-DN-04｜The Trace-Free Description Test ── How Far Can We Go Without Trace?
---
# TUP-DN-04｜The Trace-Free Description Test

## How Far Can We Go Without Trace?

### Traceなしで、どこまで記述できるか

> **Do not remove Trace by definition.**  
> **Try describing without it.**

[TUP-DN-03｜TraceなしのTracing / TracingなしのTrace｜The Trace–Tracing Cross Test ── Dog / AI / Homo sapiens](https://camp-us.net/articles/TUP-DN-03_Trace-Tracing-Cross-Test_Dog-AI-Homo-sapiens.html)  

---

Traceを定義する前に、一度、Traceを使わずに考えてみる。

Traceが必要だと仮定しない。

Traceが不要だとも仮定しない。

ただ、**Traceという語を使わずに、どこまで記述できるか。**

試してみる。

検体は三つ。

**Dog.**

**AI.**

**Homo sapiens.**

---

# 1｜Dog without Trace

犬が初めてある店へ行く。

そこでご褒美を食べる。

翌日。

散歩に出た犬が、自発的にその店へ向かう。

ここで、

「昨日の記憶が残っていた」

とは言わない。

「Traceがあった」

とも言わない。

「昨日をTracingした」

とも言わない。

観察できることだけを書く。

**t₀**

以前、犬はその店へ自発的に向かわなかった。

**t₁**

犬が店に入り、ご褒美を食べた。

**t₂**

翌日、犬が自発的に店へ向かった。

以上。

まだTraceはいらない。

---

# 2｜Difference

次に言えるのは、differenceがあるということである。

t₀とt₂で、観察された行動が違う。

**Behavior at t₂ differs from behavior at t₀.**

そして、そのあいだにt₁がある。

だから、

**t₀ | t₁ | t₂**

と並べることができる。

まだ矢印は置かない。

**t₀ → t₁ → t₂**

とは書かない。

順序があることと、一方が他方を生じさせたことは、同じではないからである。

---

# 3｜Repetition

翌日だけではない。

その後も犬が繰り返し店へ向かったとする。

t₃。

t₄。

t₅。

観察が増える。

すると、

t₁以前とt₁以後で、行動の分布が異なる、と言うことができる。

たとえば、

**P(approaching the shop | after t₁)**

と、

**P(approaching the shop | before t₁)**

にdifferenceが観察される。

これでも、Traceはいらない。

---

# 4｜Persistenceもまだ使わない

ここで、

「differenceがpersistした」

と言いたくなる。

しかし、

**Persistence**

も慎重に扱う。

同じdifferenceが時間をまたいで保存された、

とすでに読んでしまうかもしれないからである。

より弱く書くなら、

**A difference is repeatedly observable between observations before and after t₁.**

となる。

毎回観察されるdifferenceが、「同じ何か」である必要はない。

まだ、

何かが時間を越えて運ばれた、とは言わない。

---

# 5｜AI without Trace

次にAI。

条件Aでは、AIに昨日の会話を与える。

条件Bでは、昨日の会話を与えない。

それぞれについて、多数の出力を観察する。

二群の出力分布に、系統的なdifferenceが観察されたとする。

言えるのは、

**Input conditions differ.**

そして、

**Output distributions differ.**

である。

必要なら、両者のassociationを測定することもできる。

それでも、

「昨日のTraceがAIに残った」

とは言わなくてよい。

---

# 6｜Homo sapiens without Trace

人間についても同じことをする。

条件Aでは、ある文章を読む。

条件Bでは、その文章を読まない。

翌日、ある判断を求める。

二群のresponseにdifferenceが観察される。

ここでも、

「記憶が残った」

「Traceが保存された」

「昨日の経験をTracingした」

と言わずに記述できる。

**Prior exposure conditions differ.**

**Later response distributions differ.**

そして、両者のあいだにassociationが観察される。

まだTraceはいらない。

---

# 7｜Causeまで行けるか

さらに進める。

実験条件を十分に統制したとする。

すると、

prior exposureがlater responseに、何らかのcausal effectを与えた、

と推論できる場合もある。

ここで、

**effect**

が現れる。

しかし、

effectを認めたからといって、Traceを認める必要はない。

**A affected B.**

と言うことと、

**AからBへTraceが運ばれた。**

と言うことは同じではない。

したがって、

**Effect ≠ Trace.**

「効いた」ことが確認できても、

Traceという存在者を置く必要は、まだない。

---

# 8｜Connectionもまだ使わない

では、

t₁とt₂にはconnectionがある、と言えばよいだろうか。

これも一度止める。

**Connection**

という語は、離れた二点をすでに一つの関係として読んでいる。

観察されたのは、

t₁。

そしてt₂。

そのあいだのconnectionは、

観察されたものなのか。

推論されたものなのか。

記述者によって構成されたものなのか。

だから、

connectionも最初から置かない。

---

# 9｜何が渡ったのか

ここまでTraceなしで来ることができた。

Dog。

AI。

Homo sapiens。

before / after。

difference。

distribution。

association。

場合によってはcausal effect。

まだTraceはいらない。

ところが、ある問いを立てると状況が変わる。

> **What crossed the interval?**

t₁とt₂のあいだに、

何があったのか。

何が渡ったのか。

何が持ち越されたのか。

何が残ったのか。

この問いを立てた瞬間、何かを置きたくなる。

memory。

information。

state change。

record。

remainder。

そして、**Trace.**

---

# 10｜Something crossed?

しかし、ここで止まる。

t₁とt₂にdifferenceがあることから、

**something crossed the interval**

と言ってよいのだろうか。

before / afterにdifferenceがある。

associationがある。

effectがある。

そこから、

時間をまたいで「何か」が運ばれた、と推論する。

この瞬間に、われわれはprocessを、somethingへ変換していないだろうか。

つまり、

**実体化**

である。

---

# 11｜Traceを入れる誘惑

ここまでの流れを並べる。

**Observed difference across observations**

↓

**Association**

↓

**Effect**

↓

**Connection?**

↓

**Something crossed the interval?**

↓

**Trace?**

Traceは最初からそこにあったのではない。

少なくとも記述上は、かなり後になって現れる。

では、Traceという語を導入すると、何が新しく区別できるのだろう。

---

# 12｜Translation Gain Test

ここでテストを変える。

問うのは、

**What is a Trace?**

ではない。

問うのは、

> **What does “Trace” allow us to distinguish that we could not distinguish without it?**

Traceを使わずに記述する。

次に、Traceという語を一度だけ導入する。

そのとき、

それまで区別できなかった何かが、区別できるようになるか。

もし何も増えないなら、Traceは理論的に余剰かもしれない。

もし何かが増えるなら、そのdifferenceこそ、

Traceという語を残す理由になる。

---

# 13｜三つの検体

Dogについて、Traceは何を増やすのか。

AIについて、Traceは何を増やすのか。

Homo sapiensについて、Traceは何を増やすのか。

三者に同じgainがあるのか。

それとも、異なるgainがあるのか。

さらに、

Traceを導入することで、かえって見えなくなるものはないのか。

**GainだけでなくLossも監査する必要がある。**

---

# 14｜「効く」は生き残るか

Traceを消しても、一つの語が残った。

**effect.**

あるいは日常語なら、

**「効く」**

である。

prior conditionのdifferenceによって、later configurationの分布が変わる。

これはTraceを置かなくても記述できる。

だとすれば、以前、

**Traceとは、次のrelationに効くdifferenceである**

と呼んでいたものから、Traceだけを消して、

**differenceがlater configurationに効く**

と記述することもできる。

では、

生き残るのはTraceではなく、「効く」のほうなのか。

それもまだ分からない。

effectと「効く」が同じなのかも、まだ決めない。

---

# 15｜Trace-Free

いま言えることは少ない。

**Difference ≠ Trace.**

**Effect ≠ Trace.**

**Connection ≠ Trace.**

**Persistence ≠ Trace.**

少なくとも、等号はまだ置けない。

そして、Dog / AI / Homo sapiensについて、

われわれは予想以上に遠くまで、Traceなしで記述できる。

これはTraceが不要だという結論ではない。

むしろ、

Traceが本当に必要になる地点を、ようやく探せるようになった、

ということである。

---

> **Describe without Trace as far as possible.**
> 
> **Introduce Trace once.**
> 
> **What becomes distinguishable?**

もし何も変わらないなら、Traceはいらない。

もし何かが変わるなら、そこから、Traceを考えればよい。

まだ、Traceを救わない。

まだ、Traceを捨てない。

**Translation Gain Test begins here.**

---

[TUP-DN-05｜What Does Trace Add?｜Translation Gain Test ── Dog / AI / Homo sapiens](https://camp-us.net/articles/TUP-DN-05_Translation-Gain-Test_What-Does-Trace-Add.html)  

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
<p align="center">| Drafted Sep 12, 2026 · Web Sep 12, 2026 |</p>