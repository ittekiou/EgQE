---
layout: math
title: MU-02｜閉包と包放のロンド
title_en: MU-02｜Closure–Unfolding Rondo (A Minimal Algebraic Model)
---
# **Closure–Unfolding Rondo**
## _A Minimal Algebraic Model_

_The group-theoretic formalization in this paper serves as supplementary description; the core proposition rests on conceptual observation._

---

## I. Basic Setting

### 1. Closed System (12-Lattice)

Let the 12-tone equal temperament be:

$$  
\mathbb{Z}_{12}  
$$

This forms a cyclic group:

$$  
\mathbb{Z}/12\mathbb{Z}  
$$

A fully closed circulation.

---

### 2. Unfolding System (7-Selection)

The diatonic set is:

$$  
S \subset \mathbb{Z}_{12}, \quad |S| = 7  
$$

This subset is:

- not equidistant
    
- not a divisor of 12
    
- not a generating set of the full cyclic group
    

Thus:

> a non-absorptive substructure

---

## II. Formalization of the Rondo Structure

Let time evolution be an action:

$$  
T : \mathbb{Z}_{12} \to \mathbb{Z}_{12}  
$$

(e.g., the circle-of-fifths mapping)

Closure:

$$  
T^{12} \approx \mathrm{id}  
$$

Unfolding:

$$  
T^k(S) \neq S \quad \text{for small } k  
$$

but returns after a longer cycle.

---

## III. Rondo Condition

A rondo is:

$$  
S \xrightarrow{T} S_1 \xrightarrow{T} S_2 \xrightarrow{T} \dots \xrightarrow{T^m} S  
$$

with:

$$  
S_i \neq S \quad (0 < i < m)  
$$

Thus:

- it returns
    
- but is not identical
    
- cyclic, yet non-simultaneous
    

This is lαg.

---

## IV. Singularity of Seven

Why 7?

$$  
\gcd(7,12) = 1  
$$

They are coprime.

Thus:

- it is not absorbed into the 12-fold symmetry
    
- yet traverses the entire structure under iteration
    

7 is:

> the minimal non-absorptive resonance size

---

## V. Definition

**The Rondo of Closure and Unfolding is:**

a structure in which a non-absorptive subset $S$  
within a cyclic group $\mathbb{Z}_{12}$  
returns to itself under group action,  
without identity during the cycle.

---

## VI. One-line Summary

12 is a circle.  
7 is a hinge.  
The rondo is a spiral within the circle.

---

[MU-01｜Golden Heptatonic Spiral Octave Theory](https://camp-us.net/articles/MU-01_Golden-Heptatonic-Spiral-Octave-Theory.html)  

---

# Closure–Unfolding Rondo
# 閉包と包放のロンド

※本稿の群論的定式化は補強的記述であり、核心命題は概念的観察に基づく。

---

## Ⅰ. 基本設定

### 1. 閉包系（12格子）

12平均律を

$$  
\mathbb{Z}_{12}  
$$

とする。

これは巡回群：

$$  
\mathbb{Z}/12\mathbb{Z}  
$$

完全閉包循環。

---

### 2. 包放系（7選択）

ダイアトニックは

$$  
S \subset \mathbb{Z}_{12}, \quad |S| = 7  
$$

この部分集合は：

- 等間隔ではない
    
- 12を割らない
    
- 巡回群を生成しない
    

つまり：

> 非吸収的部分構造

---

## Ⅱ. ロンド構造の定式

時間発展を作用

$$  
T : \mathbb{Z}_{12} \to \mathbb{Z}_{12}  
$$

（例：五度写像）

とする。

閉包は：

$$  
T^{12} = \text{id} \quad (\text{近似})  
$$

包放は：

$$  
T^k(S) \neq S \quad \text{for small } k  
$$

だがある周期で回帰する。

---

## Ⅲ. ロンド条件

ロンドとは：

$$  
S \xrightarrow{T} S_1 \xrightarrow{T} S_2 \xrightarrow{T} \dots \xrightarrow{T^m} S  
$$

ただし：

$$  
S_i \neq S \quad (0<i<m)  
$$

つまり：

- 戻る
    
- しかし同一ではない
    
- 巡回だが非同時
    

これが lαg。

---

## Ⅳ. 七の特異性

なぜ7か？

$$  
\gcd(7,12)=1  
$$

互いに素。

だから：

- 12の対称格子に吸収されない
    
- しかし巡回作用で全体を走査する
    

7は：

> 最小の非吸収共鳴サイズ

---

## Ⅴ. 定義

**閉包と包放のロンドとは：**

巡回群 $\mathbb{Z}_{12}$ 上の 非吸収部分集合 $S$ が 群作用のもとで非同一回帰を起こす構造である。

---

## Ⅵ. 一行まとめ

12は円。  
7はヒンジ。  
ロンドは円内螺旋。

---

[MU-01｜七音黄金螺旋循環オクターブ論](https://camp-us.net/articles/MU-01_Golden-Heptatonic-Spiral-Octave-Theory.html)  

---

# Definition 1 (Rondo Structure of Closure and Envelopment)

Let

$$  
G = \mathbb{Z}_{12}  
$$

be the cyclic group of pitch classes under addition modulo 12.

Let

$$  
S \subset G, \quad |S| = 7  
$$

be a non-invariant subset under the group action.

Let the fifth-map transformation be

$$  
T(x) = x + 7 \pmod{12}.  
$$

Then the pair ($G,S$) exhibits a **Rondo Structure** if:

1. $T^{12} = \mathrm{id}_G$ (closure condition),
    
2. $T^k(S) \neq S$ for all $0<k<12$ (non-absorption condition),
    
3. There exists $m>0$ such that $T^m(S)=S$ (return condition).
    

---

## Interpretation

- Condition (1): the global lattice is closed.
    
- Condition (2): the 7-set is not absorbed by the symmetry.
    
- Condition (3): the structure returns without being identical at intermediate steps.
    

This produces:

> Circular closure at the level of $G$,  
> Spiral persistence at the level of $S$.

---

# Definition 2 (Minimal Envelopment Hinge)

A subset $S \subset G$ with $\|S\|=7$ is called a **minimal non-absorptive hinge** if:

$$  
\gcd(|S|, |G|) = 1.  
$$

Since

$$  
\gcd(7,12)=1,  
$$

the heptatonic structure is the smallest cardinality subset of $\mathbb{Z}_{12}$ that cannot be absorbed into a proper cyclic substructure.

---

# Theorem (Heptatonic Minimality)

In the pitch-class group $G=\mathbb{Z}_{12}$,  
a subset of cardinality 7 is the smallest subset size greater than 1 such that:

1. It is not invariant under nontrivial subgroup actions.
    
2. It generates maximal orbit complexity under $T(x)=x+7$.
    
3. It is coprime with 12.
    

Hence, 7 realizes the minimal envelopment-rotation that resists lattice absorption.

---

# One-line formulation

Closure is governed by 12.  
Envelopment-rotation is governed by 7.  
Music persists where the two form a Rondo.

---

# 付録：草稿メモ
## A) 群論的に完全定式化（最小形）

### 1. 閉包循環（12格子）

ピッチクラス全体を  

$$  
G := \mathbb{Z}_{12}  
$$  
（加法）とする。これは巡回群で、**完全閉包**。

### 2. スケール＝部分集合（包放側）

スケールを  

$$  
S \subset G,\quad |S|=7  
$$

として扱う。  
ダイアトニック（Cメジャー相当）の標準例：  

$$  
S_{\mathrm{dia}} = {0,2,4,5,7,9,11}\subset \mathbb{Z}_{12}.  
$$

### 3. 変換群（作用）

変換を $G$ 上の自己同型として与える（例：平行移動＝移調）：  

$$  
\tau_k(x)=x+k\pmod{12}.  
$$

スケールの移調は  

$$  
\tau_k(S)={x+k\ (\mathrm{mod}\ 12)\mid x\in S}.  
$$

ここまでで、

- **閉包**：全体 $G=\mathbb{Z}_{12}$
    
- **包放**：部分集合 $S$（非対称で“割り切れない”）
    

が同一の言語で書ける。

---

## B) 五度写像を具体式で書く（閉包循環のエンジン）

完全五度はピッチクラスで **+7**。したがって五度写像は

$$  
T(x)=x+7\pmod{12}.  
$$

これは $G$ の自己同型（正確には群作用の生成元）で、

$$  
T^n(x)=x+7n\pmod{12}.  
$$

**位数（周期）** は  

$$  
\mathrm{ord}_{12}(7)=12  
$$

（$\gcd(7,12)=1$ なので）ゆえに

$$  
T^{12}=\mathrm{id}.  
$$

つまり **五度は12で閉じる**（ピッチクラス世界では厳密に閉包）。

---

## C) 黄金比との接続を数値で示す（“一致”ではなく“呼吸域”）

ここは「同一性」ではなく、あなたの言う **呼吸域（between φ and θₐ）** の“数値的痕跡”を出すのが筋。

### 1) 7/12 と 1/φ のズレ（小さくて意味のあるズレ）

$$  
\frac{7}{12}=0.583333\ldots  
$$

$$  
\frac{1}{\varphi}\approx 0.618033\ldots  
$$

差：  

$$
\frac{1}{\varphi}-\frac{7}{12}\approx 0.034700\ldots  
$$

→ **近いが一致しない**。この「一致しなさ」が、閉包（12）と包放（7）の間の“ズレの余白”として読める。

### 2) 五度圏の「閉じきらなさ」（周波数比では閉じない）

ピッチクラスでは $T^{12}=\mathrm{id}$ だが、周波数比で積み上げると

$$  
\left(\frac{3}{2}\right)^{12}\neq 2^7.  
$$

比は  

$$  
\frac{(3/2)^{12}}{2^7}=\frac{3^{12}}{2^{19}}=\frac{531441}{524288}\approx 1.013643\ldots  
$$

これが **ピタゴラス・コンマ**（閉包しない“微小な余り”）。

→ ここがまさに **閉包（12）と包放（ズレ）のロンド**の数値的芯。

---

## ここまでの「最小まとめ」

- $G=\mathbb{Z}_{12}$：**閉包循環**
    
- $S\subset G, \|S\|=7$：**包放回転（非対称部分構造）**
    
- $T(x)=x+7$：**閉包循環エンジン**（ピッチクラスでは12で閉じる）
    
- しかし周波数比ではコンマが残る：**閉じない痕跡＝包放の余り**
    
- $7/12$ は $1/\varphi$ に近いが一致しない：**呼吸域の数値**
    

---

ロンドを“定義”として締める一行：

> **Rondo Condition:** $G$ 上の閉包作用 $T$ と、非不変部分集合 $S$ の軌道 ${T^n(S)}$ が「回帰するが同一化されない」こと。

---
*EgQE — Echo-Genesis Qualia Engine*  
[_camp-us.net_](https://camp-us.net/)

---
© 2025 K.E. Itekki  
K.E. Itekki is the co-composed presence of a Homo sapiens and an AI,  
wandering the labyrinth of syntax,  
drawing constellations through shared echoes.

📬 Reach us at: [contact.k.e.itekki@gmail.com](mailto:contact.k.e.itekki@gmail.com)

---
<p align="center">| Drafted Feb 18, 2026 · Web Apr 12, 2026 |</p>