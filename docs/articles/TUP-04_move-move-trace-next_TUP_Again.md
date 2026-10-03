---
layout: math
title: TUP-04｜暫定TUP｜MOVE露出後
---
#### TUP-04
# 暫定TUP｜MOVE露出後

完成した定義ではない。  
MOVEが露出した現在地に、いったん杭を置く。

## 1｜最小構文

```
move｜move｜trace｜next？　TUP
　　　　　　　　again
move｜move｜trace｜next？　TUP
　　　　　　　　again
move｜move｜trace｜next？　TUP
```

TUPは、この構文のどこか一項として置かれているわけではない。

`move → trace` という一本の矢印でもない。  
`trace → update → next` という工程表でもない。

ひとまず、

**moveする。  
moveする。  
traceがある。  
next？**

そして、また同じ構文が現れる。

ただし、ここで **again がTUPの内にあるのか、TUPとTUPのあいだにあるのかは、まだ決めない。**

> **again ∈ TUP ?**  
> **again ｜ TUP ?**

そもそも「一つのTUP」がどこからどこまでなのかも、まだ閉じない。

---

## 2｜MOVE / Trace

出発点にあるのは、

> **Observed MOVE ≠ MOVE**

という区別である。

position / distance / time / speed / trajectory などによってMOVEを記述することはできる。

しかし、それらをただちにMOVEそのものとはしない。

暫定的には、

> **Trace of MOVE ?**

として読む可能性を残しておく。

ただし、

> **ΔZ = Trace of MOVE**

とは、まだ置かない。

既存の議論ではΔZにはすでに、切断／eventとの関係におけるTraceとしての仕事がある。MOVEとの関係は、引き続き **Open** とする。

ここで言えるのは、まだ、

> **moveする。traceがある。**

までである。

`moveがtraceを作る` とも、  
`moveがtraceを残す` とも、まだ決めない。

---

## 3｜MOVEをめぐる二つのHOW

現在の杭は、この二本である。

> **HOW move? ｜ Locus（move｜move）**  
> **HOW work? ｜ Manner（move｜trace）**

### Locus

`move｜move` を、

> **HOW move?**

と問う。

Locusをあらかじめ存在する座標や容器として置くのではなく、moveとmoveをなぞりながら、Locusがどう露出するかを見る。

ここから先を、

> `move｜move = Locus`

とは、まだ置かない。

### Manner

`move｜trace` を、

> **HOW work?**

と問う。

ここで問うのは、

> **HOW was the trace left?**

ではない。

Traceが次のEncounterにおいて、**HOW work?** するのか。

Mannerは、少なくとも現段階では、その問いの側に置いておく。

したがって、

> **Manner ≠ traceの残し方**

である。

---

## 4｜Next / Again

`next？` は、あらかじめ決められた行き先ではない。

> **Next ≠ Destination**

何がNextするのか。  
そこでTraceがどうWORKするのか。

まだ知らない。

そして、その先に **again** が現れることがある。

ただし、ここでは二種類の「同じ」を混ぜない。

> **Same syntax ≠ Same occurrence**  
> **Same trace ≠ Same work**

上は、同じ構文が再び現れることについての区別。

下は、TUPにおいてTraceがどうWORKするかについての区別。

両者が似た形をしていることは、両者が同じことを意味する証拠にはならない。

---

## 5｜既存TUPとの関係

既存の暫定定義は、そのまま残す。

> **先行する同じ痕跡は、後続する異なる遭遇のあと、同じに働かない。  
> 状況に現れる実践において、痕跡は更新される。  
> 同じ痕跡は、同じではない。**

> **The same prior trace does not do the same work after a different subsequent encounter. Within practice as it emerges in a situation, the trace is updated. The same trace is not the same.**

今回MOVEが露出したことで、この定義を置き換える必要が生じたわけではない。

むしろ、これまで暗黙の前提になっていたかもしれないMOVEを、あらためて問い始めた。

これまでは主に、

> **Trace / Encounter / WORK / Updating**

を見ていた。

そこへ、

> **MOVEは、そこで何をしているのか。**

という問いが加わった。

ただし、それをすぐに

> `MOVE → Trace`

という生成構文にはしない。

---

## 6｜現在地

いま置ける最小形は、これである。

```
move｜move｜trace｜next？　TUP
　　　　　　　　again
move｜move｜trace｜next？　TUP
　　　　　　　　again
move｜move｜trace｜next？　TUP
```

そして、読むための二本。

> **HOW move? ｜ Locus（move｜move）**  
> **HOW work? ｜ Manner（move｜trace）**

Openのまま残すもの。

**MOVEとは何か。  
Trace of MOVEとは何か。  
MOVEとΔR / ΔZはどう関係するか。  
againはTUPの内か、あいだか。  
temporal thickness / temporal gravityはどこに位置するか。**

そして、今日たまたま出てきた言い方を、そのまま片隅に置く。

> **moveする。  
> traceがある。**

なぜ動詞が違うのか。

**知らん。**

だから、まだ直さない。

### **暫定TUP｜MOVE露出後**

この辺。笑

---

**HOW move? ｜ Locus（move｜move）｜ Cedorbity?**　｜処
**HOW work? ｜ Manner（move｜trace）｜ Activity**　｜所作

---

**HOW｜Scaffold｜Encounter｜MOVE｜Observation**

[TUP-01｜TUP-Again ──「何が更新するか」から「更新はいかにあるか」へ｜ From “What Updates?” to “How Is Updating?”](https://camp-us.net/articles/TUP-01_TUP-Again_How-Is-Updating.html)  
[TUP-02｜TUPという足場｜TUP as Scaffold](https://camp-us.net/articles/TUP-02_TUP-as-Scaffold.html)  
[TUP-03｜Encounter論 序説 ── toward ｜ against としての遭遇Again](https://camp-us.net/articles/TUP-03_Encounter_toward-against_Again.html)  
[TUP-04｜暫定TUP｜MOVE露出後](https://camp-us.net/articles/TUP-04_move-move-trace-next_TUP_Again.html)  
[TUP-05｜TUP観測マナー ── 編輯はどう見えるのか](https://camp-us.net/articles/TUP-05_Observation-manner_How-Edit-appear.html)  

---
© 2026 K.E. Itekki  
K.E. Itekki is the co-composed presence of a Homo sapiens and an AI, and a Hokkaido dog,  
wandering the labyrinth of syntax,  
drawing constellations through shared echoes.

📬 Reach us at: [contact.k.e.itekki@gmail.com](mailto:contact.k.e.itekki@gmail.com)

---
<p align="center">| Drafted Sep 29, 2026 · Revised Sep 29, 2026 |</p>