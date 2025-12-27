---
title_en: floc —On the Structural Boundary of Calculability in Cosmology
layout: math
---
# **floc**

## _On the Structural Boundary of Calculability in Cosmology_

---

### Short Critical Commentary

---

Recent Radiation General Relativistic Magnetohydrodynamic (GRMHD) simulations of black hole accretion represent one of the most comprehensive efforts to model extreme astrophysical environments within a fully relativistic and radiatively coupled framework. By incorporating spacetime curvature, magnetized plasma dynamics, and radiation transport, these studies faithfully implement the contemporary cosmological requirement that physical systems be described as closed, self-consistent, and computationally enumerable.

A notable and robust outcome of these simulations is that increasing physical completeness does not lead to greater structural closure. Instead, the resulting solutions systematically exhibit geometrically thick accretion flows, reduced radiative efficiency, multiphase stratification, and pronounced anisotropy. Importantly, these characteristics arise as converged and numerically stable solutions, rather than as artifacts of insufficient resolution or incomplete modeling.

From a cosmological perspective, the primary significance of this result lies not in the identification of a novel accretion regime, but in the clarification of a structural boundary of calculability. Even when spacetime dynamics, magnetic fields, and radiation are jointly and consistently treated, the system resists reduction to a compact, efficiently interpretable, and globally closed description.

In this sense, the simulations function as boundary indicators for contemporary computational cosmology. They demonstrate that the explanatory power of fully enumerated models is intrinsically limited, not by technical shortcomings, but by the emergence of structural complexity that exceeds efficient recovery of globally coherent meaning from local dynamical variables.

Accordingly, these results suggest that progress in computational cosmology depends not only on increasing physical fidelity, but also on recognizing the implicit constraints under which calculability itself remains viable. The work therefore contributes less to cosmological model construction than to the precise identification of the conceptual and structural limits within which such models can operate.

---
## Abstract

#### _(Scientific Poetic Commentary / Academic Tone)_

This commentary evaluates recent Radiation General Relativistic Magnetohydrodynamic (GRMHD) simulations of black hole accretion not as a proposal of a new cosmological model, but as a precise exposition of the limits of calculability in contemporary astrophysical cosmology.

By integrating spacetime dynamics, magnetized plasma, and radiative transfer within a fully relativistic numerical framework, the study realizes, with remarkable fidelity, the modern cosmological demand that extreme astrophysical systems be described as closed, self-consistent, and computationally tractable structures. In this sense, the model represents one of the most rigorous implementations of a _Z₀-type constructive framework_, in which physical processes are explicitly enumerated, evolved, and quantified.

However, the resulting solutions systematically exhibit geometric thickening, reduced radiative efficiency, multiphase stratification, strong anisotropy, and nonlocal coupling—features that persist not as numerical artifacts, but as converged and stable outcomes of the simulations. Paradoxically, increasing formal completeness leads not to closure, but to the emergence of structural excess beyond efficient recovery of observable meaning.

This commentary argues that the cosmological significance of the work lies precisely in this outcome. Rather than extending cosmological explanation, the simulations function as a _boundary marker_, demonstrating where fully enumerated physical descriptions cease to produce closed, efficient, or globally coherent representations of the system.

From this perspective, the study implicitly reveals the necessity of an underlying generative domain—here referred to as a _floc-like field_—that must be excluded in advance for calculability to remain intact. The work therefore stands as an exemplary case in which contemporary cosmology, through its own internal rigor, makes visible the structural limits of its explanatory reach.

---

## **Prelude｜計算と閉じ、その限界について（詠評）**

現代の宇宙論は、計算とともに進んできた。  
一般相対論、磁気流体力学、放射輸送──  それらを統合する数値計算は、時空・物質・エネルギーを一つの枠組みの中に閉じ込め、「計算できる宇宙」を現実のものにしてきた。

計算は、いまや技術ではなく、理解そのものの条件になりつつある。  
計算可能であることは、説明可能であることと、ほとんど同義に扱われる。  
閉じたモデル、保存される量、意味をもつ出力。  
それらが揃ってはじめて、私たちは「わかった」と言う。

だが、その前提は本当に自明なのだろうか。

計算が成立するためには、境界が必要であり、局所性が必要であり 外部化された時間が必要であり、全体を貫く会計としてのエネルギーが必要であり、そして何より、世界が「数えられる」ことが必要である。  
これらの条件は、ほとんど語られることなく、計算の背後で静かに働いてきた。

本稿は、新しい宇宙像を提示するものではない。  
むしろ、計算が最も成功している場所で、何が同時に成立しなくなるのかを追う。  
Radiation GRMHD に代表される極限的数値宇宙論は、物理的完全性を高めるほどに、説明としての閉じを失っていく。  
計算は続く。  
だが、意味が回収できなくなる。

ここで起きているのは、物理法則の破綻ではない。  
記述構造の限界である。  
本稿は、計算が壊れるのではなく、閉じが壊れる地点に注目する。

以下ではまず、計算可能性が成立するための条件を明示し、それらが同時に満たされなくなる構造を辿る。  
その過程で現れる生成的領域を、便宜的に _floc_ と呼ぶ。  
それは原因でも実体でもなく、計算が成功したときにのみ姿を現す、限界の名前である。

計算は続く。  
それでも、物語は閉じない。  
本稿は、その地点を記すための科学詠評である。

---

##### reference ──ZURE Science Review (ZSR):  
[ZS-010_Z₀ 構文の極限と floc 宇宙の境界標識 — Radiation GRMHD 論文を読む —](https://camp-us.net/critics/ZS-010_Radiation-GRMHD.html)  

---

## Introduction（日本語）

近年の計算天体物理学の進展は、ブラックホール降着現象の記述を、かつてない物理的忠実度の水準へと押し上げた。  
とりわけ放射付き一般相対論的磁気流体力学（Radiation GRMHD）は、放射輸送・磁場・乱流・強重力を自己無撞着に組み込んだ、完全三次元・相対論的シミュレーションを可能にしている。

こうした発展は、「計算できること」の範囲を飛躍的に拡張した。  
しかし同時に、より根源的な問いを突きつける。  
**計算可能性が極限まで押し進められたとき、それでもなお閉じきらないものは何か。**

本稿は、新たな宇宙論モデルを提案するものではない。  
また、新しい物理的実体や因果機構を導入することも目的としない。  
本稿が行うのは、恒星質量ブラックホール降着を扱った最新のフル放射GRMHDシミュレーションを、現代計算宇宙論が到達しうる _境界事例_ として読み直すことである。

エディントン比の広い範囲にわたって、これらのシミュレーションは興味深い共通像を示す。  
超エディントン領域では放射圧に支えられた幾何学的に厚い円盤と強いアウトフローが現れ、一方でサブ〜ニア・エディントン領域では、磁場条件に依存した薄い円盤とコロナ構造が形成される。  
この意味で降着円盤像は連続的かつ統一的に整理できる。

しかし同時に、磁場トポロジーやブラックホールスピンに紐づく構造差は消失せず、計算解像度・物理モデル・計算時間をいかに高めても、単一の閉じた描像へとは収束しない。

本稿は、この分岐の持続を「未完成」や「改良不足」としては解釈しない。  
むしろそれは、計算が高度化し、物理的忠実度が極限に近づいた _結果として_ 初めて可視化された現象である。  
ここに現れているのは、個別物理の欠如ではなく、計算可能性そのものの構造的境界である。

この領域を指示するために、本稿では **floc** という語を用いる。  
floc は物理的実体でも、場でも、原因でもない。  
それは、計算が持続し続けるにもかかわらず、説明が閉じきらない状況を最小限に記述するための構造的標識である。

Radiation GRMHD の成果をこの視点から読み直すことで、本稿は、高忠実度数値シミュレーションを単なる予測装置としてではなく、**宇宙論における「計算可能性の限界」を診断するための装置**として再定位する。

---

## **Prelude: On Computation, Closure, and the Question of Limits**

Contemporary cosmology increasingly operates at the intersection of physical completeness and computational rigor. Advances in numerical relativity, magnetohydrodynamics, and radiative transfer have enabled models in which spacetime, matter, and energy are treated within unified, self-consistent frameworks. These developments have not merely expanded the scope of calculable phenomena; they have sharpened the question of what it means for a physical description to be complete.

The ambition of computational cosmology is not only to simulate physical systems, but to render them intelligible through closure. A model is expected to evolve coherently, conserve quantities globally, and produce outputs that can be meaningfully interpreted as a whole. In this sense, calculability has come to function as an implicit criterion of explanatory success. What can be computed is assumed to be, in principle, explainable.

Yet this assumption is rarely examined directly. The conditions that allow computation to yield closure—enumerability, locality, boundary-defined isolation, and externally parameterized time—are typically presupposed rather than articulated. They operate silently in the background of numerical practice, becoming visible only when they begin to fail.

This work is concerned not with proposing an alternative cosmological model, but with examining the structural limits that arise when calculability itself is pursued to its extreme. Recent Radiation GRMHD simulations provide a particularly instructive context for this inquiry. These models incorporate an unprecedented degree of physical fidelity, yet systematically exhibit behaviors that resist reduction to compact, globally coherent accounts. The systems remain computable, while closure becomes elusive.

Rather than treating this outcome as a deficiency, we take it as a signal. The persistence of computation alongside the dissolution of closure points to a boundary within which computational description remains effective, and beyond which its organizing principles reconfigure. It is this boundary—not a breakdown of physical law, but a limit of descriptive structure—that the present work seeks to clarify.

To do so, we proceed in three steps. First, we articulate the structural conditions under which physical systems are rendered calculable. Second, we examine how these conditions fail to be simultaneously satisfied in physically extreme regimes. Finally, we introduce a minimal terminology to designate the generative domain revealed by this failure, without reifying it as a new causal entity.

The sections that follow do not argue that the universe is uncomputable, nor that existing theories are incomplete in a technical sense. Instead, they trace how computation can continue even as explanation fragments, efficiency declines, and narrative coherence dissolves. In doing so, they aim to situate computational cosmology within a broader understanding of its own limits—limits that are structural, not accidental, and that emerge precisely where calculability appears most successful.

---

### Part I｜Foundations

---

## **1. Introduction**

Recent advances in computational astrophysics have pushed black hole accretion modeling to an unprecedented level of physical fidelity.  
In particular, Radiation General Relativistic Magnetohydrodynamics (Radiation GRMHD) now enables fully relativistic, three-dimensional simulations that self-consistently incorporate radiation transport, magnetic fields, turbulence, and strong gravity.

These developments have dramatically expanded the domain of what can be _calculated_.  
At the same time, however, they raise a deeper question:  
**what, if anything, fails to close even when calculability is maximized?**

This paper does not propose a new cosmological model, nor does it introduce additional physical entities or causal mechanisms.  
Instead, it treats recent full radiation GRMHD simulations of stellar-mass black hole accretion as _boundary cases_—sites where contemporary computational cosmology approaches its structural limits.

Across a wide range of Eddington ratios, these simulations reveal a striking pattern.  
While accretion flows can be organized into broadly unified regimes—ranging from geometrically thick, radiation-pressure-dominated disks at super-Eddington rates to thinner, magnetically structured disks with coronae at sub- and near-Eddington rates—key features do not converge to a single, closed description.  
In particular, differences tied to magnetic field topology and black hole spin persist even as numerical resolution, physical completeness, and simulation duration are pushed to extremes.

This persistence of branching structures is not interpreted here as a failure of modeling or an absence of further refinement.  
On the contrary, it emerges precisely _because_ the simulations are physically rich and computationally exhaustive.  
The non-closure exposed in these results therefore points not to missing physics in a narrow sense, but to a structural boundary of calculability itself.

To designate this regime, we introduce the term **floc**.  
Floc is not a physical substance, field, or causal agent.  
It is a minimal structural marker for situations in which calculability continues—often with increasing precision—while explanatory closure does not occur.

By reading Radiation GRMHD results through this lens, the present work reframes high-fidelity numerical astrophysics not merely as a tool for prediction, but as an instrument for diagnosing the limits of computable closure in cosmology.

---

## **2. Conditions of Calculability**

### Conditions of Calculability

Any computational cosmology implicitly presupposes a set of structural conditions under which physical systems can be rendered calculable. These conditions are rarely stated explicitly, yet their satisfaction is necessary for numerical closure, predictive stability, and coherent interpretation.

We summarize these conditions as follows.

---

### **(C1) Well-defined boundary conditions**

The system must admit explicit boundary conditions—spatial, temporal, or causal—within which physical processes are specified, initialized, and numerically evolved. Without such boundaries, the system cannot be isolated as a computable object.

---

### **(C2) Localizability of physical interactions**

Physical interactions must be expressible in terms of local or quasi-local variables, allowing the decomposition of global dynamics into computationally tractable substructures. This condition underwrites discretization, parallelization, and numerical convergence.

---

### **(C3) Monotonic and externally parameterized time**

Time must function as a monotonic, ordered parameter external to the dynamics it indexes. This separation allows temporal evolution to be implemented as a sequence of computational steps rather than as an emergent or entangled variable.

---

### **(C4) Global conservation and bookkeeping of energy**

Energy must be globally definable and conserved in a manner that permits consistent bookkeeping across the system. This condition ensures numerical stability and enables the interpretation of efficiency, dissipation, and transfer processes.

---

### **(C5) Enumerability of degrees of freedom** _(structural condition)_

The relevant degrees of freedom must be enumerable in principle, such that the system can be represented as a finite or controllably infinite set of state variables. This condition is not physical but structural: it enables the very formulation of a computational state space.

---

### **Remark**

Conditions (C1)–(C4) concern the physical organization of the system. Condition (C5), by contrast, concerns the syntactic structure of description itself. When (C5) fails, the operational meaning of the remaining conditions becomes indeterminate.

---

## **Failure of Co-satisfiability in Radiation GRMHD**

Recent Radiation GRMHD simulations of black hole accretion provide a concrete setting in which the above conditions are individually implemented with high fidelity. Boundary conditions are explicitly defined, local interactions are resolved through relativistic MHD, temporal evolution is parameterized numerically, and global energy accounting is enforced.

Nevertheless, the resulting solutions consistently exhibit behaviors that signal a failure of co-satisfiability among these conditions.

---

### **(C1) Boundary conditions under geometric thickening**

While spatial and causal boundaries are formally specified, the emergence of geometrically thick accretion flows and extended radiative regions renders the effective boundary of the system diffuse and dynamically variable. The boundary remains defined, yet loses its isolating function.

---

### **(C2) Breakdown of effective localizability**

Although local equations of motion are solved, strong radiative coupling and magnetic connectivity introduce nonlocal dependencies. Physical influence propagates across scales faster than local decomposition can accommodate, eroding the operational meaning of locality.

---

### **(C3) Time as an insufficient external parameter**

The simulations evolve in monotonic coordinate time; however, the physical processes being modeled—radiative trapping, delayed escape, and feedback-driven restructuring—introduce timescales that are not reducible to stepwise temporal indexing. Time ordering remains formal, but explanatory sufficiency degrades.

---

### **(C4) Energy bookkeeping without explanatory closure**

Global energy conservation is maintained numerically, yet radiative efficiency systematically declines. Energy is generated, transported, and conserved, but not efficiently recoverable as interpretable output. Conservation persists without explanatory closure.

---

### **(C5) Loss of effective enumerability**

As multiphase stratification, anisotropy, and scale-coupling intensify, the effective degrees of freedom proliferate beyond controllable enumeration. While the system remains formally discretized, the state space ceases to be operationally enumerable.

---

### **Synthesis**

Radiation GRMHD thus realizes each condition of calculability in isolation, while demonstrating their failure to hold simultaneously under physically extreme regimes. The system remains computable, yet no longer structurally closed.

---

## **3. Definition and Structural Status of _floc_**

### **Definition (floc)**

We refer to the generative domain in which the necessary conditions for calculability fail to be simultaneously satisfied as **floc**.  
The term _floc_ does not denote a physical substance, field, force, or hidden variable. Rather, it designates a structural regime in which enumerability, locality, boundary-defined isolation, and externally parameterized temporal evolution lose operational coherence as a unified descriptive framework.

### **Proposition: _floc_ is not a cause but a consequence**

**Proposition.**  
_floc_ should not be interpreted as a causal agent responsible for the breakdown of computational closure in physical systems. Instead, _floc_ emerges as a structural consequence of imposing calculability constraints on regimes whose physical organization exceeds the simultaneous satisfiability of those constraints.

In this sense, _floc_ is not that which disrupts computation from the outside. It is what becomes visible when the requirements of calculability are applied beyond their domain of co-satisfiability. The appearance of _floc_ therefore signals not a failure of physical law, but a limit of descriptive closure inherent to computational cosmology itself.

### **Remark**

The introduction of _floc_ does not extend the causal structure of existing physical theories. It serves to name the boundary regime in which fully enumerated, closed-form descriptions remain formally computable yet cease to yield globally coherent or efficiently interpretable representations.

---

## **4. Corollary: Reconfiguration of Calculability Conditions in _floc_**

When _floc_ emerges, conditions (C1)–(C4) do not fail independently. Rather, their operational coherence collapses through the loss of effective enumerability (C5).

In the absence of controllable enumerability, boundary conditions remain formally specified yet lose isolating power; locality persists at the level of equations while failing as an organizing principle; time remains monotonic as a parameter but becomes insufficient as an explanatory index; and global energy conservation holds numerically without yielding coherent interpretability. Computation continues, but closure does not.

### **Implication**

The emergence of _floc_ therefore does not signify the breakdown of computability itself, but the transition to a regime in which calculability persists without explanatory closure. This transition marks a structural reconfiguration rather than a physical anomaly.

---

### Part II｜Three Failures without Breakdown

---

## **5. Time: Why Time Persists Yet Loses Explanatory Force**

Time is the first structural element to persist formally while losing explanatory efficacy in the emergence of _floc_. In computational cosmology, time is required to function as a monotonic, externally parameterized index that orders dynamical evolution into discrete, iterable steps. This requirement is fully satisfied in regimes such as Radiation GRMHD, where simulations advance coherently in coordinate time. Yet, as physical processes become dominated by radiative trapping, delayed escape, feedback-driven restructuring, and multi-scale coupling, temporal ordering ceases to organize causal understanding. Events remain sequential, but their succession no longer yields a compressible account of why particular configurations arise. Time continues to advance as a parameter of computation, while failing as a principle of explanation.

As _floc_ emerges, time ceases to operate as an external ordering principle and begins to fold into the dynamics it was meant to index. Temporal evolution remains well-defined at the level of simulation steps, yet the causal relevance of those steps becomes inseparable from spatial, energetic, and informational entanglement across scales. Processes unfold not merely _in_ time, but _through_ configurations whose effective duration cannot be localized or hierarchically ordered. In such regimes, time no longer compresses complexity; it accumulates it. The succession of moments remains intact, but their explanatory leverage dissolves as temporal distance fails to correlate with causal separation.

### **Corollary (Time)**

When _floc_ emerges, time does not disappear or reverse; it persists as a computational parameter while ceasing to function as an explanatory organizer of physical structure.

---

## **6. Gravity: Why Gravity Is Conserved Yet Loses Efficiency**

Gravity remains formally intact even after time has lost its explanatory force. In regimes approaching _floc_, gravitational dynamics continue to obey conservation laws and field equations, and their numerical implementation remains stable. Yet the capacity of gravity to organize energy into efficiently recoverable structure degrades. Mass–energy is accumulated, transported, and conserved, but increasingly fails to translate into coherent work, luminosity, or globally interpretable output. What persists is not the productive role of gravity as an ordering principle, but its residual bookkeeping function. Gravity continues to act, but no longer _pays off_ in explanatory or energetic terms.

The loss of gravitational efficiency in _floc_ does not indicate dissipation or violation of conservation, but a decoupling between accumulation and return. Gravitational binding increases structural density and dynamical complexity, yet the pathways by which stored energy becomes globally recoverable narrow or fragment. As a result, measures such as radiative efficiency, work extraction, or large-scale ordering cease to scale with mass–energy input. Gravity continues to shape configurations, but the relationship between cause and yield becomes non-compressive: more structure no longer produces proportionally more explanatory or energetic output. Efficiency fails not because gravity weakens, but because the conditions that allow gravity to _mean_ something operationally have already eroded.

---

## **7. Observation: Why Observables Remain Defined Yet Fail to Describe the Whole**

Observation is the final surface at which _floc_ becomes visible. Even after time has lost explanatory force and gravity has lost efficiency, observables remain well-defined. Measurements can be taken, spectra computed, distributions plotted, and correlations quantified. Data do not disappear. What fails is not observability, but totality. Individual observables retain precision, yet their aggregation no longer yields a coherent global description. The system can be sampled exhaustively without becoming narratable as a whole. Observation persists, but synthesis collapses.

---

### Part III｜Synthesis

---

## **8. General Corollary: Structural Reconfiguration under _floc_**

Across the emergence of _floc_, the conditions of calculability (C1–C5) do not collapse symmetrically. Computation persists, equations remain valid, and numerical evolution proceeds. What reconfigures is the role each condition plays in sustaining explanatory closure.

Time (C3) persists as a parameter but loses its capacity to organize causal understanding. Gravity and energy conservation (C4) remain formally intact while decoupling from efficient return and global interpretability. Boundary specification and locality (C1–C2) survive at the level of formal description yet fail to isolate the system as a coherent whole. Underlying these shifts is the loss of effective enumerability (C5), through which the remaining conditions retain form without function.

Accordingly, _floc_ designates a regime in which calculability endures without closure. The system remains computable, observable, and dynamically lawful, while resisting reduction to a compact, globally coherent account. This is not a failure of physical theory, but a structural limit of computational description.

---

### **Summary**

- **Computation** continues.
    
- **Explanation** fragments.
    
- **Closure** dissolves.
    

---

## **9. Discussion: Computation without Closure**

The analysis developed in this work does not argue for a revision of physical law, nor does it propose a new cosmological model. Instead, it clarifies a structural distinction that has remained largely implicit in computational cosmology: the difference between _calculability_ and _closure_. The results presented across the preceding sections demonstrate that these two notions, often treated as equivalent, diverge under physically extreme regimes.

Radiation GRMHD provides a paradigmatic example. Even with an unprecedented degree of physical completeness—incorporating spacetime curvature, magnetized plasma dynamics, and radiative transfer—the resulting systems remain fully computable while resisting reduction to compact, globally coherent descriptions. Time advances monotonically, energy is conserved, and observables are well-defined. Yet explanation fragments, efficiency declines, and narrative synthesis fails. These outcomes are not numerical artifacts but stable, converged features of the models.

This divergence motivates the introduction of _floc_ as a minimal structural designation. Crucially, _floc_ is not posited as an additional physical entity or causal mechanism. It names the regime in which the necessary conditions for calculability—enumerability, locality, boundary-defined isolation, and externally parameterized time—can no longer be simultaneously satisfied. In this sense, _floc_ marks a limit internal to computational description itself, rather than an external failure imposed by unknown physics.

The three analyses of time, gravity, and observation make this limit explicit. Time persists as a parameter while losing explanatory force; gravity remains conserved while decoupling from efficient return; observation continues to yield precise measurements while failing to support global synthesis. Across these domains, the same pattern recurs: computation endures, but closure dissolves. What fails is not lawfulness, but the capacity to compress dynamics into an interpretable whole.

This perspective reframes how the success of computational cosmology should be understood. Increasing physical fidelity does not guarantee explanatory closure; indeed, it may instead expose the structural boundaries within which closure is possible. The appearance of _floc_ is therefore not a sign of inadequacy, but an indicator that computation has reached its most revealing limit—one where the organizing assumptions of calculability become visible precisely through their breakdown.

Finally, this work suggests a shift in emphasis for future inquiry. Rather than asking whether the universe is computable, it may be more productive to ask under what structural conditions computation yields closure, and where it does not. _floc_ provides a vocabulary for this distinction, enabling cosmological models to be situated not only by what they calculate, but by how and where their explanations cease to close.

---

## **Appendix: Concluding Poem (Scientific Poetic Commentary)**

**Computation continues.**  
Time advances, gravity accumulates,  
observation multiplies its counts.

Yet still,  
only the narrative refuses to close.

_Here, floc remains._  

---

計算は続く。  
時間は進み、重力は蓄え、  
観測は数を増やす。

それでも、  
物語だけが閉じない。

——ここに、_floc_ がある。

---

What appears here is not a breakdown of cosmology, but the cosmological analogue of Wittgenstein’s ladder.

---

© 2025 K.E. Itekki  
K.E. Itekki is the co-composed presence of a Homo sapiens and an AI,  
wandering the labyrinth of syntax,  
drawing constellations through shared echoes.

📬 Reach us at: [contact.k.e.itekki@gmail.com](mailto:contact.k.e.itekki@gmail.com)

---
<p align="center">| Drafted Dec 26, 2025 · Web Dec 27, 2025 |</p>