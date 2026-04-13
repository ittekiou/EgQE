---
layout: math
title: "MU-03｜Golden Seven Rondo Theory: 閉包・包放・最小ヒンジとしての七 ― 比と回転のあいだに持続が生まれる構造理論 ―"
title_en: "MU-03｜Golden Seven Rondo Theory: Closure, Envelopment, and the Minimal Hinge in ℤ₁₂ ― A Structural Account of Heptatonic Persistence Between Ratio and Rotation"
---
# Golden Seven Rondo Theory
## 閉包・包放・最小ヒンジとしての七
### ― 比と回転のあいだに持続が生まれる構造理論 ―
# Closure, Envelopment, and the Minimal Hinge in ℤ₁₂
## A Structural Account of Heptatonic Persistence Between Ratio and Rotation

---

## Abstract

This paper formalizes the structural relation between the 12-tone pitch-class lattice and the 7-tone heptatonic subset using group-theoretic language.  
Let $G = \mathbb{Z}_{12}$ denote the cyclic group of pitch classes under addition modulo 12, and let $S \subset G$ with $\|S\|=7$ represent a heptatonic scale.  
Under the fifth-map transformation $T(x)=x+7 \pmod{12}$, we prove that while $G$ forms a closed cyclic structure ($T^{12}=\mathrm{id}$), the subset $S$ exhibits non-absorptive rotational persistence due to $\gcd(7,12)=1$.  
This produces what we define as a **Rondo Structure**: circular closure at the global level and spiral persistence at the subset level.  
We show that 7 is the minimal cardinality greater than 1 that resists absorption into proper sublattices of $\mathbb{Z}_{12}$.  
The theory provides a structural reinterpretation of heptatonic musical organization as minimal envelopment-rotation within a closed lattice.

---

## 1. The Closed Lattice

Let

$$  
G = \mathbb{Z}_{12}  
$$

be the cyclic group of pitch classes under addition modulo 12.

Define the fifth transformation:

$$  
T(x) = x + 7 \pmod{12}.  
$$

Since (\gcd(7,12)=1), 7 generates the entire group. Therefore,

$$  
T^{12} = \mathrm{id}_G.  
$$

Thus, the 12-tone system is a closed cyclic structure under fifth-iteration.

We call this the **Closure Condition**.

---

## 2. The Heptatonic Subset

Let

$$  
S \subset G, \quad |S| = 7.  
$$

Example (C-major class set):

$$  
S = {0,2,4,5,7,9,11}.  
$$

The subset $S$ is not invariant under $T$:

$$  
T^k(S) \neq S \quad \text{for} \quad 0<k<12.  
$$

However, since $T^{12} = \mathrm{id}$, the orbit of $S$ is finite and cyclic.

This produces:

- global closure,
    
- local non-invariance,
    
- eventual return.
    

We call this the **Envelopment Condition**.

---

## 3. Definition: Rondo Structure

Let $G=\mathbb{Z}_{12}$, $S \subset G$, and $T(x)=x+7$.

The pair ($G,S$) forms a **Rondo Structure** if:

1. $T^{12}=\mathrm{id}$ (closure),
    
2. $T^k(S)\neq S$ for $0<k<12$ (non-absorption),
    
3. There exists $m>0$ such that $T^m(S)=S$ (return).
    

This structure yields:

> Circular closure at the level of $G$.  
> Spiral persistence at the level of $S$.

---

## 4. Minimality of Seven

We prove:

**Theorem (Heptatonic Minimality).**  
In $G=\mathbb{Z}_{12}$, a subset of cardinality 7 is the smallest subset size greater than 1 such that:

1. $\gcd(\|S\|,12)=1$,
    
2. $S$ cannot be absorbed into any proper cyclic substructure of (G),
    
3. the orbit of $S$ under $T$ achieves maximal rotational complexity.
    

Since

$$  
\gcd(7,12)=1,  
$$

7 is the minimal non-absorptive hinge of the 12-lattice.

---

## 5. Numerical Non-Closure

Although pitch classes close in 12 iterations, frequency ratios do not:

$$  
\left(\frac{3}{2}\right)^{12} \neq 2^7.  
$$

The deviation

$$  
\frac{3^{12}}{2^{19}} \approx 1.01364  
$$

(the Pythagorean comma)

demonstrates that closure is lattice-level, not acoustic-level.

Thus, music structurally contains both:

- closure (lattice symmetry),
    
- non-closure (ratio deviation).
    

---

## 6. Preliminary Conclusion

Music is not founded on perfect closure.  
It is founded on the interaction between closure and envelopment.

Twelve governs the circle.  
Seven governs the hinge.

Music persists where the two form a Rondo.

---

## 7. Internal Hinge Axis

We introduce an internal structural axis within the Rondo Structure:

$$  
\varphi \longleftrightarrow \theta_\alpha \longleftrightarrow 7  
$$

where:

- $\varphi$ represents closure tendency (ratio condensation),
    
- $\theta_\alpha$ represents maximal deflection (angular redistribution),
    
- $7$ represents the minimal non-absorptive hinge within $\mathbb{Z}_{12}$.
    

### Interpretation

- $\varphi$: asymptotic proportional stabilization
    
- $\theta_\alpha$: maximal non-coincident angular distribution
    
- $7$: minimal structural resistance to lattice absorption
    

Thus, the heptatonic subset operates as the hinge between:

- ratio-based closure ($\varphi$),
    
- angular redistribution ($\theta_\alpha$),
    
- cyclic lattice symmetry $12$.
    

This axis formalizes the structural tension underlying musical persistence.

---

## 8. Structural Non-Absorption Criterion

Let $G=\mathbb{Z}_{12}$.  
Let $H \subset G$ be a proper cyclic subgroup.

A subset $S \subset G$ is **absorptive** if:

$$  
\exists H \subsetneq G \quad \text{such that} \quad S \subset H.  
$$

Since the only proper subgroups of $\mathbb{Z}_{12}$ have orders:

$$  
1,2,3,4,6,  
$$

any subset $S$ with cardinality coprime to 12 cannot be contained in a proper subgroup.

Therefore:

$$  
\gcd(|S|,12)=1 \Rightarrow S \text{ is non-absorptive}.  
$$

Because $\gcd(7,12)=1$,  
7 is the smallest cardinality greater than 1 satisfying this condition.

---

## 9. Acoustic Non-Closure Theorem

Let

$$  
R_n = \left(\frac{3}{2}\right)^n.  
$$

Define octave equivalence:

$$  
R_n \sim 2^k.  
$$

Then there exists no integer $n < 12$ such that

$$  
\left(\frac{3}{2}\right)^n = 2^k.  
$$

Thus acoustic space exhibits irreducible non-closure relative to lattice closure.

This establishes:

> Structural duality:  
> algebraic closure vs. acoustic non-closure.

---

# Final Conclusion

Music persists not because it closes, but because closure and non-closure co-rotate.

Twelve defines the circle.  
Seven defines the hinge.  
The golden axis stabilizes the tension between ratio and rotation.

This is the Golden Seven.

---

# Golden Seven Rondo Theory
## 閉包・包放・最小ヒンジとしての七
### ― 比と回転のあいだに持続が生まれる構造理論 ―

---

# 1. 問題設定

音楽はなぜ持続するのか。

閉じるからではない。  
崩れるからでもない。

**閉包（closure）と包放（envelopment）が共回転するからである。**

本論は、十二音閉包構造（ℤ₁₂）と七音包放構造のあいだに存在する **最小非吸収ヒンジ（minimal non-absorptive hinge）としての七** を定式化する。

---

# 2. 群論的基礎

音高空間を

$$  
G = \mathbb{Z}_{12}  
$$

とする。

G の真部分群の位数は：

$$  
1,2,3,4,6  
$$

である。

---

## 定義（吸収性）

部分集合 $S \subset G$ が **吸収的（absorptive）** であるとは、

$$  
\exists H \subsetneq G \quad \text{such that} \quad S \subset H  
$$

を満たすことである。

---

## 非吸収条件

$$  
\gcd(|S|,12)=1 \Rightarrow S \text{ は非吸収的}  
$$

なぜなら、位数が 12 と互いに素である集合は 真部分群に収まらないからである。

---

## 七の特異性

$$  
\gcd(7,12)=1  
$$

7 は 1 を除けば最小の条件充足数である。

ゆえに、

> 七は最小の非吸収回転数である。

---

# 3. 音響的非閉包

完全五度写像を考える：

$$  
R_n = \left(\frac{3}{2}\right)^n  
$$

オクターブ同値：

$$  
R_n \sim 2^k  
$$

しかし、

$$  
\left(\frac{3}{2}\right)^n = 2^k  
$$

を満たす整数解は存在しない。

したがって、

> 音響空間は格子空間に対して不可約な非閉包を持つ。

---

# 4. 内部ヒンジ軸

ここで内部構造軸を導入する：

$$  
\varphi \longleftrightarrow \theta_\alpha \longleftrightarrow 7  
$$

- $\varphi$：比による閉包傾向（凝縮）
    
- $\theta_\alpha$：最大角度分布（回転拡張）
    
- 7：最小非吸収ヒンジ
    

七は、

- 比的閉包
    
- 角度的分配
    
- 格子対称性
    

のあいだで**張力を保持する中心**として機能する。

---

# 5. 黄金軸と持続

閉じすぎれば停止する。  
開きすぎれば崩壊する。

七はその中間にある。

それは安定ではない。  
**不安定の安定中心である。**

---

# 6. 黄金ロンド構造

十二は閉包を定める。  
七は包放を定める。

両者は対立しない。

> 閉包と包放はロンド的に交替する。

音楽はこの往還によって持続する。

---

# 7. 最終宣言

音楽は閉じるから続くのではない。  
閉じきらないから続くのである。

十二は円を定める。  
七はヒンジを定める。

黄金軸は、比と回転のあいだの張力を安定化する。

これが

**Golden Seven Rondo Theory**

である。

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