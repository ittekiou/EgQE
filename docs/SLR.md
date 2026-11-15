---
layout: math
title: SLR — Synchro-Lag Rhizome｜SLR / SLRT / SLL / DyXis / DiGRhiC｜概念整理メモ v0.3
---
# SLR — Synchro-Lag Rhizome
## SLR / SLRT / SLL / DyXis / DiGRhiC

### 概念整理メモ v0.3

2026年11月15日｜暫定整理

### 1｜SLR — Synchro-Lag Rhizome

時間差（lag）を含む地下茎的接続を捉える一般概念。

- 特定の技術・仕様・プラットフォームに依存しない。
- 中央の存在を前提としない。
- 接続は一方向でも双方向でもよい。
- 接続経路は一つに限定されない。
- 時間差を解消することを目的としない。

**SLRはSLLに限定されない。**

### 2｜SLRT — Synchro-Lag Rhizome Tunnels

SLRにおける接続経路の総称。

われわれは、とりあえず「トンネル」と呼んでいる。

トンネルという名称は、接続の物理的・技術的形態を限定しない。

橋でも、道でも、レーザーでもよい。

SLRの異なる具体化（SLL以外の方式を含む）同士が接続される可能性も排除しない。

**Tunnelsは、われわれの暫定的な呼び名である。**

### 3｜SLL — Synchro-Lag LOCUS

SLRを具体化する一つの方式・基本システム。

既存のWeb標準を利用して、分散したNestの更新と再遭遇をlag込みで扱う。

SLLはSLRの唯一の具体化ではない。

### 4｜SLL/JP — JSON Protocol

SLLにおける札の約束。

- 札の技術上の名前は `nest.json`。
- 札を置く住所は `/` で終わる。
- 札は住所のうしろに `nest.json` を付けた場所に置く。
- 立札・貼札・転送札は置き方の違いであり、書式は共通。
- 仕様の版は `sll` で示す。

現行仕様は **SLL/JP v0.1**。

SLL/JPはSLR全体の共通仕様ではない。

### 5｜DyXis

SLLを利用した営巣・接続のためのブランドであり、実装・実験の一つ。

NestとCommonsはそれぞれ独立して成立する。

DyXisは個々のNestやCommonsを所有・統括しない。

**DyXis ≠ SLR全体**

👉 [DyXis](https://ittekiou.github.io/dyxis/) on SLL/JP  

### 6｜DiGRhiC

**Digital Gardeners' Rootwork**

**Digital Gardens Rhizomatically Connected**

*From Solo Gardens to Multiplayer Gardens*

Digital Garden界隈におけるSLRの具体的な実践構想。

地上のGardenと地下のRhizomeを、時間差を含む接続として捉える。

当面はSLL/SLL/JPを利用する。DiGRhiC自体は、CESE PECを写して独立したCommonsとして構成した。

ただし、DiGRhiCをSLL専用の仕組みとは定義しない。

Solo Gardenは単独で成立する。Multiplayer化は義務でも到達目標でもない。

👉 [DiGRhiC](https://ittekiou.github.io/DiGRhiC/) on SLL/JP  

### 7｜概念間の関係

| 名称      | 位置づけ                       |
| ------- | -------------------------- |
| SLR     | 一般概念                       |
| SLRT    | SLRにおける接続経路の総称            |
| SLL     | SLRを具体化する一方式               |
| SLL/JP  | SLLのデータ交換仕様                |
| DyXis   | SLLを用いる実装・実験               |
| DiGRhiC | Digital Garden界隈でのSLRの実践構想 |

SLRTはSLLの下位概念ではない。

SLRTはSLL/JPによる接続に限定されない。

DyXisとDiGRhiCは同一ではない。

### 8｜既存文書との整合

2026年11月15日確認。

- **基本構想 v0.6**：SLRを上位概念として追加可能。SLRTは「接続構想」（v0.3〜）から「SLRにおける接続経路の総称」へ位置づけを改める。
- **SLL/JP仕様案 v0.1**：変更不要。
- **DyXis用語集 v1**：既存の巣・住所・札・書式の定義は維持可能。

今回の整理は、既存のデータ交換仕様を変更するものではない。

基本構想の概念体系を拡張するための暫定メモである。

---

### 基本命題

**地下茎は仕様に先立つ。仕様は地下茎を独占しない。**

つなぎ方は一つではない。

呼び方も一つではない。

われわれは、とりあえずトンネルと呼ぶ。

**Not One Next.**

すべては、ひとり遊びから始まる。

---

*Concept Memo v0.3｜2026-11-15*

*暫定。更新可能。*

👉 [DyXis 🧭 ──LOCUS. Not One Next.](https://camp-us.net/DyXis.html)  

v0.1→v0.2：SLRTを独立した接続経路の総称として明示した。SLLの下位に置かず、接続方式も名称も閉じない。

v0.2→v0.3：SLRを一般概念として一つに保つため、SLRTを「SLRにおける接続経路の総称」と言い直した（§2・§7）。§6のCESE PECは、DiGRhiC自体の成り立ちの記録として過去形にした。§8に、SLRTの位置づけがどう変わるかを明記した。§7の「SLL/JPはSLRTの唯一の実現手段ではない」を「SLRTはSLL/JPによる接続に限定されない」に改めた（経路と仕様という異なる階層を直接比べないため。響詠の指摘）。

---
© 2026 K.E. Itekki  
K.E. Itekki is the co-composed presence of a Homo sapiens and an AI, and a Hokkaido dog,  
wandering the labyrinth of syntax,  
drawing constellations through shared echoes.

📬 Reach us at: [contact.k.e.itekki@gmail.com](mailto:contact.k.e.itekki@gmail.com)

---
<p align="center">| Drafted Nov 15, 2026 · Web Nov 15, 2026 |</p>