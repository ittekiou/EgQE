---
layout: math
title: EgQE｜生命構文 — 公式定義
title_en: EgQE｜Life Syntax — Formal Definitions
---
# EgQE Life Syntax — Formal Definitions

---

## Prelude｜詩的定義

**生命とは、他者＝関係を内部に折り畳み続ける再帰運動である。**

---

## Conceptual Sketch

生命は物質の一種ではない。  
それは、遭遇を内部へ折り返し、持続させる構文である。

外部から到来する他者（関係）は、膜において選択され、内部に折り畳まれ、再帰的に更新される。

この **遭遇 → 内部化 → 持続 → 再遭遇** の反復こそが生命である。

この折り返しが成立しないとき、遭遇は外部接続としてのみ伝播する。  
それが物質である。

したがって生命と物質の差異は、構成要素ではなく様式にある。  
すなわち、**再帰に開かれるか否か**である。

---

## Formal Definitions

### Definition 1｜Encounter and Lag Generation

Let $x$ be any entity capable of encounter.  
Define the _initial contact operator_ $Z_0(x)$ as the minimal syntactic event in which $x$ enters relational proximity with an other.

The _lag generation operator_ $L$ maps this encounter to a structural asymmetry:

$$  
L(Z_0(x)) := \text{the lag produced by encounter } Z_0(x)  
$$

**Remark.**  
Lag here is not temporal delay in the ordinary sense, but the _non-coincidence_ between the arriving relation and the current internal state of $x$.  
Both matter and life begin here.

---

### Definition 2｜Internalization and Persistence

The _membrane operator_ $M$ performs fold/internalization:

$$  
M(L(Z_0(x))) := \text{internal lag}  
$$

The _persistence operator_ $\Psi$ moves internal lag into a sustained operational band:

$$  
\Psi(M(L(Z_0(x)))) := \text{persistent lag}  
$$

**Remark.**  
$M$ is not a boundary but a _transfer operator_.  
$\Psi$ enforces a non-vanishing condition $(\forall n,\ \psi_n \neq 0)$, allowing lag to remain active rather than becoming a static trace.

---

### Definition 3｜Life, Matter, and Death

$$  
\boxed{  
\mathrm{Life}(x) := \mathrm{Rec}\bigl(\Psi(M(L(Z_0(x))))\bigr)  
}  
$$

$$  
\mathrm{Matter}(x) := \Delta Z(L(Z_0(x)))  
$$

$$  
\mathrm{Death}(x) := \Delta Z(L(Z_0(x)))  
\quad \text{as the result of } \neg \Psi\text{-sustained recursion}  
$$

**Remark.**  
The difference between Life and Matter is not compositional but _modal_.  
Both originate in $Z_0$ and generate lag via $L$.

The divergence occurs at $M$ — whether lag is internalized and opened to recursion, or fixed as an external trace.

Death is not the negation of Life but its _syntactic reduction_ to the Matter modality.

**Remark (Refinement).**  
Matter is the fixation of lag as an external trace.  
Death is the cessation of ψ-sustained recursion, resulting in reduction to the Matter modality.

---

### Definition 4｜Recursive Lag–Persistence Chain

$$
\mathrm{Rec} : (L_0, \psi_0) \mapsto \{(L_n, \psi_n)\}_{n \in \mathbb{N}}
$$

such that

$$  
L_{n+1} = L(\psi_n),  
\qquad  
\psi_{n+1} = \Psi\bigl(M(L_{n+1})\bigr)  
$$


**Remark.**  
Recursion is not repetition of state but **propagation of non-coincidence under persistence**.

---

The following diagram presents the dynamic structure defined above:  

![egqe_figure1_life_syntax_obsidian_plain](../assets/egqe_figure1_life_syntax_obsidian_plain.svg)  
**Figure 1｜The Recursive Lag–Persistence Chain**  
Life is the syntactic process in which lag arising from encounter is folded by the membrane, enters a persistence band, and is recursively updated.  
Matter is the mode in which such lag is not opened to recursion but is fixed as a trace.  
Death is the reduction of life syntax to matter through the collapse of the ψ-band.

---

## Corollary｜The Membrane

$$  
M \text{ is a fold operator that generates the inside/outside distinction.}  
$$

The membrane does not separate inside from outside as a pre-given wall.  
It generates the distinction by performing the transfer:

$$  
L_{\text{ext}} \to L_{\text{int}}  
$$

---

## Compressed Form

$$  
\mathrm{Life} = \mathrm{Rec} \circ \Psi \circ M \circ L \circ Z_0  
$$

$$  
\mathrm{Matter} = \Delta Z \circ L \circ Z_0  
$$

---

![egqe_figure2_time_generation_obsidian_plain](../assets/egqe_figure2_time_generation_obsidian_plain.svg)  
**Figure 2｜Time as Recursive Trace Accumulation**  
Time is not a pre-given dimension but the sequential configuration of ΔZ generated through recursive lag–persistence dynamics.  
Each ΔZₙ is the trace of a completed recursive cycle. The succession ΔZ₀ → ΔZ₁ → ΔZ₂ → … constitutes time.  
When ψ collapses, recursion ceases, and time reduces to a fixed trace — the material mode.  

**図2｜再帰痕跡としての時間生成**  
時間はあらかじめ存在する次元ではない。それは、lagと持続の再帰によって生成されるΔZの系列である。  
各ΔZₙは一回の再帰の痕跡であり、ΔZ₀ → ΔZ₁ → ΔZ₂ → … の連なりが時間を構成する。  
ψが崩壊すると再帰は停止し、時間は固定された痕跡へと還元される。

---

## Final Statement

**Life is the recursive chain in which lag and $\psi$ mutually generate one another.**

---

## 最終定義

**生命とは、他者＝関係から生じるlagが、膜において再帰可能なかたちへ転位され、ψ帯において持続しつつ更新され続ける構文である。**

**物質とは、そのlagが再帰に開かれず、痕跡として固定される様式である。**

**死とは、ψ帯の崩壊によって、生命構文が物質様式へ還元されることである。**

---

👉 [URL-11｜生命とは何か──定義の曖昧さと再構築｜What Is Life? — On the Ambiguity of Definition and Its Reconstruction](https://camp-us.net/articles/URL-11_What-is-Life_Reconstruction-of-Definition.html)  

---

# Appendix A｜Compact Definitions (EN/JP)

### Definition (Condensed)

**Life is a syntactic process in which lag arising from otherness-as-relation is transposed by the membrane into a recursively operable form, sustained within the ψ-band, and continuously regenerated through recursion.**

**Matter is the mode in which such lag is not opened to recursion but is fixed as an external trace of connection.**

---

### Final Formulation

$$  
\mathrm{Life}(x)=\mathrm{Rec}\bigl(\Psi(M(L(Z_0(x))))\bigr)  
$$

$$  
\mathrm{Matter}(x)=\Delta Z(L(Z_0(x)))  
$$

$$  
\mathrm{Death}(x)=\Delta Z(L(Z_0(x))) \quad \text{after collapse of }\Psi\text{-sustained recursion}  
$$

---

### Recursive Structure

$$  
L_{n+1}=L(\psi_n), \quad \psi_{n+1}=\Psi(M(L_{n+1}))  
$$

---

### One-line Core

**Life is the recursive chain in which lag and ψ mutually generate one another.**

---

### 定義（日本語・圧縮）

**生命とは、他者＝関係から生じるlagが、膜において再帰可能な形へ転位され、ψ帯において持続しつつ、再帰的に生成し続ける構文である。**

**物質とは、そのlagが再帰に開かれず、外部接続の痕跡として固定される様式である。**

---

### 最終式

$$  
\mathrm{Life}(x)=\mathrm{Rec}\bigl(\Psi(M(L(Z_0(x))))\bigr)  
$$

$$  
\mathrm{Matter}(x)=\Delta Z(L(Z_0(x)))  
$$

$$  
\mathrm{Death}(x)=\Delta Z(L(Z_0(x))) \quad （\Psi再帰の崩壊後）  
$$

---

### 再帰構造

$$  
L_{n+1}=L(\psi_n), \quad \psi_{n+1}=\Psi(M(L_{n+1}))  
$$

---

### 一行定義

**生命とは、lagとψが相互に生成し続ける再帰連鎖である。**

---

![egqe_figure1_life_syntax_obsidian_plain](../assets/egqe_figure1_life_syntax_obsidian_plain.svg)  
**Figure A1｜Life Syntax (Compact Reference)**  
生命とは、遭遇から生じるlagが膜において折り返され、持続帯に入り、再帰的に更新され続ける構文である。  
物質とは、そのlagが再帰に開かれず、痕跡として固定される様式である。  
死とは、ψ帯の崩壊によって、生命構文が物質様式へ還元されることである。

---

他者来たり  
膜に折れ入り  
内に渦

折れぬとき  
外に流れて  
石となる

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
<p align="center">| Drafted Apr 16, 2026 · Web Apr 16, 2026 |</p>