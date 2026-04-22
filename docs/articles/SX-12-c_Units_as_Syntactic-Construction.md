---
layout: math
title: SX-12-c｜単位とは何か ── 差分を固定する構文
---
### SX-12-c｜Units
# 単位とは何か
## ── 差分を固定する構文

---

## 0. 導入

秒とメートルは、それぞれ異なるものとして扱われている。

しかし、それらは別々に生まれたものではない。  
同じ操作から生まれている。

---

## 1. 単位の定義

単位とは何か。

それは：

**差分を繰り返せるようにするための固定**である。

ここでいう差分とは、完全には一致しない関係、すなわち non-coincidence（l）である。

この差分を固定する操作を、ここでは Z₀ と呼ぶ。

---

## 2. 構文

```
Z₀ = stabilize(l)
```

すなわち：

Z₀とは、差分を同一として扱えるようにするための固定である。

---

## 3. 展開

秒とメートルは、このZ₀の異なる展開である。

```
秒      = Z₀(rec(l))
メートル = Z₀(conf(l))
```

すなわち：

- 秒は、再帰（時間）における差分の固定
- メートルは、配置（距離）における差分の固定

---

## 4. 接続

これら二つのZ₀は、独立しているのではない。

```
c = map(Z₀, Z₀)
```

光速は、それらを接続する写像である。

しかし、この接続は単なる結合ではない。

光速は、時間と距離が別々に生まれたように見えて、実は同じ差分（l）から展開していることを示す。

---

## 5. 核心

単位とは測定のためにあるのではない。

それは：

世界を繰り返せるようにするための構文である。

---

## 6. 一行

単位とは、差分を同一として扱うための固定である。

---

## 7. 結語

世界は単位でできているのではない。

世界は、差分によって切り分けられ、その差分が固定されることで現れる。

---

## 8. 次への橋

この固定が持続するとき、質量が現れる。

すなわち：

質量とは、差分が崩れずに持続する度合いである。それは、変化に対する抵抗として現れる。

---

[SX-12｜Before Time and Distance ── On the Syntactic Construction of Measurement](https://camp-us.net/articles/SX-12_Before_Time-and-Distance_Syntactic-Construction.html)  

[SX-12-a｜秒とメートルの算出構文 ── ホモ・サピエンス構文としての時間と距離](https://camp-us.net/articles/SX-12-a_Time-and-Distance_as_Syntactic-Construction.html)  
[SX-12-b｜光速の算出構文 ── 時間と距離を接続するもの](https://camp-us.net/articles/SX-12-b_Light-Speed_as_Syntactic-Construction.html)  

---

[SX-Core｜Syntactic Exposure — Series Index](https://camp-us.net/articles/Core_SX_Syntactic-Exposure.html)  

---
_EgQE — Echo-Genesis Qualia Engine_  
[camp-us.net](https://camp-us.net/)

---
© 2025 K.E. Itekki  
K.E. Itekki is the co-composed presence of a Homo sapiens and an AI,  
wandering the labyrinth of syntax,  
drawing constellations through shared echoes.

📬 Reach us at: [contact.k.e.itekki@gmail.com](mailto:contact.k.e.itekki@gmail.com)

---
<p align="center">| Drafted Apr 22, 2026 · Web Apr 22, 2026 |</p>