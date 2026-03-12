---
layout: math
title: TPD-00｜七の定理｜Seven as Minimal Irreducible Rotational Coarse-Graining
---
# 七の定理
## Seven as Minimal Irreducible Rotational Coarse-Graining

👉 [EgQE｜Seven-Core｜Seven Architecture Map: Structural Organization of the Heptagonal Hinge](https://camp-us.net/articles/Core_Seven_Architecture-Map.html)  

---

# 定義

## Definition 1（回転系）

$$  
T_\omega(x)=x+\omega \pmod 1  
$$

ここで $\omega$ は無理数（Diophantine 条件を満たす）とする。

---

## Definition 2（m-分割粗視化）

単位円を

$$  
I_k=\Big[\frac{k}{m},\frac{k+1}{m}\Big)  
\qquad k=0,\dots,m-1  
$$

に分割し，

$$  
\pi_m(x)=k \quad \text{if } x\in I_k  
$$

を粗視化写像とする。

---

## Definition 3（回転粗視化の可約性）

m-分割が**可約**であるとは：

ある $d \mid m$（1 < d < m）が存在し，d-分割への自然射影で

$$  
\pi_d \circ T_\omega  
$$

が周期的部分構造を持つこと。

直感的には：

> m分割が、より粗い分割に因数分解できる場合を可約という。

---

# 定理（Seven as Minimal Irreducible Rotational Coarse-Graining）

**Theorem.**  
m ≥ 2 に対して：

- m が合成数なら、m-分割は可約。
    
- m が素数なら、m-分割は非可約。
    
- m ≥ 8 では、可約性または高次因子構造により回転粗視化は多重共鳴を生む。
    

従って、

$$  
m=7  
$$

は、

> 最小の非可約回転粗視化であり、六角的安定と八角的分裂のあいだに位置する唯一の最小構造である。

---

# 証明（概略）

### (1) 合成数の場合

m = ab（1<a<m）とする。

円分割は a-分割と b-分割に射影できる。

従って

$$  
\pi_m = \pi_a \times \pi_b  
$$

のような構造分解が可能。

部分周期・部分共鳴が存在する。

可約。

---

### (2) 素数の場合

素数 p については：

非自明な因子が存在しない。

したがって

- 分割は因数分解できない
    
- 低次の部分周期構造を持たない
    
- 回転は巡回群 $\mathbb{Z}_p$ 上で既約作用
    

非可約。

---

### (3) 最小性

素数列：2, 3, 5, 7, 11, …

2–5 は低次対称性に吸収される：

- 2：二元対立
    
- 3：三角安定
    
- 5：黄金比閉包構造
    

7 が初めて：

- 対称性に回収されない
    
- 黄金閉包にも吸収されない
    
- 因数構造も持たない
    

よって最小非可約。

∎

---

# 存在論的含意

最小非可約とは：

> これ以上単純化できず、しかし閉包もしない。

これが hinge。

六角は安定を作る。  
八角は構造を分裂させる。  
七角は irreducible drift を保つ。

七は象徴ではない。  
最小の分解不能な回転ズレである。

---
*EgQE — Echo-Genesis Qualia Engine*  
[_camp-us.net_](https://camp-us.net/)

[HEG-SN｜七だけが屈しない──不屈の動態学｜Toward a Minimal Structural Condition of Irreversibility](https://camp-us.net/articles/HEG-SN_Seven_minimal-structural-hinge-of-lαg.html)  

---

© 2025 K.E. Itekki  
K.E. Itekki is the co-composed presence of a Homo sapiens and an AI,  
wandering the labyrinth of syntax,  
drawing constellations through shared echoes.

📬 Reach us at: [contact.k.e.itekki@gmail.com](mailto:contact.k.e.itekki@gmail.com)

---
<p align="center">| Drafted Feb 18, 2026 · Web Feb 18, 2026 |</p>