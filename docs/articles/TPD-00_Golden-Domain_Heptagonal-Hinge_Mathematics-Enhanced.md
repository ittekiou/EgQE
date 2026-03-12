---
layout: math
title: "TPD-00｜The Golden Domain and the Heptagonal Hinge: Between φ and θα under lαg｜定理部分の数理強化（Draft）"
---
### Toroponic Polygonic Dynamics I
## The Golden Domain and the Heptagonal Hinge: Between φ and θα under lαg
# 定理部分の数理強化（Draft）

👉 [EgQE｜Seven-Core｜Seven Architecture Map: Structural Organization of the Heptagonal Hinge](https://camp-us.net/articles/Core_TPD_Seven-Architecture-Map.html)  

---

## 定義 1（回転力学系）

$$  
T_\omega(x)=x+\omega \pmod 1,  
\qquad \omega \in \mathbb{R}\setminus\mathbb{Q}  
$$

---

## 定義 2（m-分割粗視化）

$$  
I_k=\left[\frac{k}{m},\frac{k+1}{m}\right),\quad k=0,\dots,m-1  
$$

$$  
\pi_m(x)=k \text{ if } x\in I_k  
$$

---

## 定義 3（可約性）

m-分割が可約であるとは：

$$  
\exists\,\ d \mid m,\quad 1<d<m  
$$

であり、

$$  
\pi_d \circ T_\omega  
$$

が同型的に低次分割へ射影可能な場合。

---

## 補題 1（合成数の可約性）

m が合成数なら、m-分割は可約。

_証明略_：  
m = ab とすると、分割は a と b に因数分解可能。

---

## 補題 2（素数分割の既約性）

m が素数なら、非自明な分解は存在しない。

したがって粗視化は既約。

---

## 補題 3（低次対称吸収）

m ≤ 6 の素数分割は、

- 2 → 二元対称
    
- 3 → 三角閉包
    
- 5 → 黄金閉包
    

により回収可能。

（ここは少し議論を書く必要があるが、構造的主張として置ける。）

---

## 定理（最小非可約粗視化）

**Theorem.**

m ≥ 2 に対し、最小の非可約かつ低次対称吸収を受けない回転粗視化は

$$  
m=7  
$$

である。∎

---

- 可約性
    
- 素数既約
    
- 低次対称吸収
    
- 七の最小性
    

---

# 2️⃣ 図設計（φ ↔ θα ↔ 7ヒンジ）

図は三層で描く。

---

## 構造案（横配置）

```
 φ  ←──────  7  ──────→  θα
(closure)   (hinge)   (dispersion)
```

---

## 円環モデル（推奨）

単位円：

- 黄金角回転矢印
    
- 七分割マーク
    
- φ側に trace condensation
    
- θα側に generative motion
    

中央に：Tropotic lαg Axis

---

## 図キャプション案

**Figure 1. The Golden Domain and the Heptagonal Hinge.**

Irrational rotation under the golden angle (θα) generates maximal non-overlapping distribution.  
Trace condensation under coarse-graining produces proportional stabilization (φ).  
Seven-fold partition constitutes the minimal irreducible hinge sustaining coherence between closure and dispersion under lαg.

---

- 数理
    
- 幾何
    
- 存在論
    

が一枚に。

---

<svg xmlns="http://www.w3.org/2000/svg" width="980" height="560" viewBox="0 0 980 560" role="img" aria-label="TPD: φ ↔ θα with the Heptagonal Hinge and Tropotic lαg Axis">
  <defs>
    <style>
      .bg { fill: #ffffff; }
      .ink { fill: #111111; }
      .stroke { stroke: #111111; stroke-width: 2; }
      .thin { stroke: #111111; stroke-width: 1.4; }
      .dash { stroke: #111111; stroke-width: 1.4; stroke-dasharray: 6 6; }
      .label { font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Arial, sans-serif; font-size: 16px; fill: #111111; }
      .small { font-size: 13px; }
      .title { font-size: 20px; font-weight: 700; }
      .mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }
    </style>

    <marker id="arrow" markerWidth="14" markerHeight="14" refX="11" refY="7" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L14,7 L0,14 Z" fill="#111111"/>
    </marker>

    <marker id="arrowThin" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L12,6 L0,12 Z" fill="#111111"/>
    </marker>
  </defs>

  <!-- Background -->
  <rect class="bg" x="0" y="0" width="980" height="560" rx="16" fill="#ffffff" opacity="0.96" stroke="#111" stroke-width="2"/>

  <!-- Title -->
  <text class="label title" x="40" y="48" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="24" font-weight="700" fill="#111">The Golden Domain and the Heptagonal Hinge</text>
  <text class="label small" x="40" y="74" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="16" font-weight="700" fill="#111">φ (closure / trace)  ↔  θ<tspan baseline-shift="sub">α</tspan> (dispersion / rotation) under the Tropotic lαg Axis</text>

  <!-- Main Axis -->
  <line class="stroke" x1="90" y1="150" x2="890" y2="150" stroke="#333" stroke-width="1" marker-end="url(#arrow)"/>
  <text class="label mono" x="425" y="102" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="14" font-weight="700" fill="#111">Tropotic lαg Axis</text>

  <!-- Left: phi (trace condensation / closure) -->
  <circle class="thin" cx="150" cy="150" r="34" fill="none" rx="16" opacity="0.96" stroke="#111" stroke-width="2"/>
  <text class="label" x="141" y="166">φ</text>
  <text class="label small" x="98" y="205">trace condensation</text>
  <text class="label small" x="112" y="225">(closure tendency)</text>

  <!-- Right: theta_alpha (generative rotation / dispersion) -->
  <circle class="thin" cx="830" cy="150" r="34" fill="none" rx="16" opacity="0.96" stroke="#111" stroke-width="2"/>
  <text class="label" x="820" y="166">θ<tspan baseline-shift="sub">α</tspan></text>
  <text class="label small" x="778" y="205">generative rotation</text>
  <text class="label small" x="790" y="225">(dispersion tendency)</text>

  <!-- Center: Heptagonal hinge node -->
  <circle class="stroke" cx="490" cy="150" r="42" fill="none" rx="16" opacity="0.96" stroke="#111" stroke-width="2"/>
  <text class="label" x="485" y="166">7</text>
  <text class="label small" x="425" y="205">heptagonal hinge</text>
  <text class="label small" x="408" y="225">minimal irreducible</text>
  <text class="label small" x="435" y="245">coarse-graining</text>

  <!-- Metastable domain bracket -->
  <path class="dash" d="M210,170 C285,240 375,270 490,270 C605,270 695,240 770,170"  stroke="#333" stroke-width="1" fill="none"/>
  <text class="label small" x="408" y="298">metastable “breathing zone”</text>
  <text class="label small" x="372" y="318">between closure (φ) and dispersion (θ<tspan baseline-shift="sub">α</tspan>)</text>

  <!-- Lower panel: Circle model -->
  <text class="label" x="40" y="342">Coarse-graining on the circle (illustrative)</text>

  <!-- Circle -->
  <circle class="stroke" cx="310" cy="450" r="95" fill="none" rx="16" opacity="0.96" stroke="#111" stroke-width="2"/>

  <!-- 7 partitions (radial lines) -->
  <!-- angles chosen for aesthetics; equal-ish spacing -->
  <g class="thin">
    <line x1="310" y1="450" x2="310" y2="355" stroke="#333" stroke-width="1" class="thin"/>
    <line x1="310" y1="450" x2="381" y2="383" stroke="#333" stroke-width="1" class="thin"/>
    <line x1="310" y1="450" x2="404" y2="455" stroke="#333" stroke-width="1" class="thin"/>
    <line x1="310" y1="450" x2="363" y2="536" stroke="#333" stroke-width="1" class="thin"/>
    <line x1="310" y1="450" x2="257" y2="536" stroke="#333" stroke-width="1" class="thin"/>
    <line x1="310" y1="450" x2="216" y2="455" stroke="#333" stroke-width="1" class="thin"/>
    <line x1="310" y1="450" x2="239" y2="383" stroke="#333" stroke-width="1" class="thin"/>
  </g>

  <!-- rotation arrow (theta_alpha) -->
  <path class="stroke" d="M250,395 A95,95 0 0 1 365,385" fill="none" stroke="#333" stroke-width="1" marker-end="url(#arrowThin)"/>
  <text class="label small" x="258" y="400">θ<tspan baseline-shift="sub">α</tspan> rotation</text>

  <!-- Trace condensation arrow toward phi -->
  <line class="thin" x1="430" y1="470" x2="560" y2="470" stroke="#333" stroke-width="1" marker-end="url(#arrowThin)"/>
  <text class="label small" x="442" y="458">trace → ratio</text>

  <!-- Right mini block: key claims -->
  <rect x="560" y="375" width="370" height="170" fill="none" class="thin" rx="16" opacity="0.96" stroke="#111" stroke-width="2"/>
  <text class="label" x="580" y="404">Key relations</text>

  <text class="label small" x="580" y="432">• θ<tspan baseline-shift="sub">α</tspan> : maximal non-overlap (generative motion)</text>
  <text class="label small" x="580" y="454">• φ : sedimented trace of redistribution (ratio)</text>
  <text class="label small" x="580" y="476">• 7 : minimal irreducible hinge for coherence</text>
  <text class="label small" x="580" y="498">• higher modes : appear via projection as traces</text>
  <text class="label small" x="580" y="520">• stability : sustained transition under lαg</text>

  <!-- Footer -->
  <text class="label small" x="40" y="550">TPD-00 Figure 1.</text>
</svg>

**Figure 1. The Golden Domain and the Heptagonal Hinge.** Irrational rotation under the golden angle (θₐ) generates maximal non-overlapping distribution. Under coarse-graining, sustained redistribution condenses as proportional trace (φ). Seven-fold partitioning functions as the minimal irreducible hinge sustaining coherence between closure and dispersion under the Tropotic lαg Axis.

---

# IV章（強化版）に入れる数理パーツ一式

## 4.1 Setup（力学系＋等分割コーディング）

$$  
T_\omega:\mathbb T^1\to\mathbb T^1,\qquad T_\omega(x)=x+\omega\ (\mathrm{mod}\ 1),\quad \omega\notin\mathbb Q.  
$$

等分割：

$$  
I_k^{(m)}=\Big[\frac{k}{m},\frac{k+1}{m}\Big),\quad k=0,\dots,m-1  
$$

$$  
\pi_m(x)=k\ \ \text{iff}\ \ x\in I_k^{(m)}.  
$$

コーディング列：

$$  
s_n^{(m)}(x)=\pi_m(T_\omega^n x)\in\{0,\dots,m-1\}.  
$$

---

## 4.2 Reducibility（因子写像としての可約性）

**Definition (Equal-partition factor / reducibility).**  
$d\mid m$ のとき、自然な合成（ブロック化）

$$  
\rho_{m\to d}:\{0,\dots,m-1\}\to\{0,\dots,d-1\},\qquad \rho_{m\to d}(k)=\lfloor k/(m/d)\rfloor  
$$

を通じて

$$  
\pi_d = \rho_{m\to d}\circ \pi_m  
$$

が成り立つ。このとき、m-分割は **d-分割へ因子化（factor）** する。

---

## 4.3 確実な定理

### Lemma 1（合成数は必ず因子化できる）

$m$ が合成数なら、ある $1<d<m$ が存在し $d\mid m$。したがって上の $\rho_{m\to d}$ により等分割コーディングは低次へ因子化する。  
（証明：定義通り）

### Lemma 2（素数は「等分割の意味で」既約）

$m=p$ が素数なら、等分割に関しては $d\mid p$ の非自明因子が存在しないため、**等分割→等分割**の経路での因子化は存在しない。

> ここまでで言えること：**「等分割という枠内では、既約性は素数で保証される」**  

---

# 4.4 “symmetry absorption” を数学として書ける形に落とす

ここが③の核心。「2/3/5 は吸収される」を、**恣意に見えない定義**にする。

## Definition（低次吸収：低アルファベット因子）

m-分割コーディングが **低次吸収**されるとは：

> m-分割のコーディングが、ある $k<m$ の有限アルファベット $\{0,\dots,k-1\}$ 上のコーディングへ **因子化**（ブロック写像）できること。

形式的には、ある有限窓長 (r) と写像

$$  
\Phi:\{0,\dots,m-1\}^{2r+1}\to\{0,\dots,k-1\}  
$$

が存在し、得られる列が別のシフト系を与える、という形（標準的な symbolic dynamics の factor）。

---

## 4.5 5（黄金閉包）の扱いを“定理寄り”にする

ここで黄金平均回転を明示する。

$$  
\omega=\frac{\sqrt5-1}{2}=\frac1\phi.  
$$

このとき回転の二分割（閾値1−ωの2区間）で得られるコーディングは **Sturmian** になり、Fibonacci substitution と結びつく（古典的事実）。

> 論文での役割：  
> **5は「等分割の既約」ではあるが、黄金回転に対しては“2文字（Sturmian）因子”が自然に立つ**  
> → “golden closure” 側へ吸収される、を数学的に支えられる。

この部分は、Related/Appendix で短く引用スタイルにすれば十分。

---

# 4.6 7の「最小性」を“二段定理”にする

ここがポイント。**一発で「7が絶対」** と言い切らずに、論文の強度を上げる書き方にする。

---

## Theorem A（硬い核：等分割既約の最小性）

等分割→等分割という制約の下では、既約となる最小の $m$ は素数であり、最小は $m=2$。  
（これは数学的に完全に正しい）

---

## Theorem B（TPD条件付き最小性：Heptagonal Hinge）

次の追加条件を課す：

- (C1) **低次対称吸収**（小アルファベット因子）を除外する
    
- (C2) **黄金閉包吸収**（Sturmian/Fibonacci 因子に回収されるレジーム）を除外する
    
- (C3) 過剰分割（高次の投影・凝縮が支配的なレジーム）を除外する
    

この条件下で、最小の等分割既約ヒンジは

$$  
m=7  
$$

である。

> ここで重要なこと：  
> **7は「数学だけ」で出るのではなく、TPDの“観測＝粗視化”条件（C1–C3）を入れたときに最小になる**。

---

# 4.7 論文に入れる“短い証明スケッチ”の雛形

- 合成数は Lemma1 で落ちる
    
- 素数は Lemma2 で等分割既約
    
- しかし 2,3 は低次対称吸収（C1）により排除
    
- 5 は黄金回転で Sturmian/Fibonacci 因子（C2）により排除
    
- 7 は prime で等分割因子なし、かつ C1–C3 の排除条件の外側に残る最小
    

この論法が一番“堅い”。

---

# 次（図に反映する最小修正）

SVG図に、**数理強化の痕跡**を最小だけ足す：

- 7ノードの下に小さく  
    `prime ⇒ no equal-partition factor`
    
- 5（φ側）に小さく  
    `Sturmian/Fibonacci factor (ω=1/φ)`
    

この2行で、図が“数学の図”になる。

---

# Figure 1

## φ ↔ θα ↔ 7 Hinge

### Structural Irreversible Redistribution Axis

---

## 図の構造（数学的に厳密）

横軸を Tropotic lαg Axis とする：

$$  
\phi \quad \longrightarrow \quad \theta_\alpha \quad \longrightarrow \quad 7  
$$

---

## 左端：φ（Golden Ratio Regime）

**Label:**  
Golden Closure Regime

**数理的説明：**

- Continued fraction:  
	
    $$  
    \phi = [1;1,1,1,\dots]  
    $$
    
- Most irrational number
    
- Generates Sturmian minimal symbolic complexity
    
- Fibonacci substitution
    
- Two-interval coding sufficient
    

**構造的意味：**

- 最小複雑性
    
- 準周期的安定
    
- 生成はあるが閉じやすい
    

→ _Absorption threshold_

---

## 中央：θₐ（Golden Angle Regime）

$$  
\theta_\alpha = 2\pi\left(1-\frac{1}{\phi}\right)  
$$

**Label:**  
Maximal Quasi-Uniform Redistribution

**数理的説明：**

- Equidistribution on circle
    
- No rational locking
    
- Irrational rotation class
    

**構造的意味：**

- 拡散最大化
    
- 非同期性の純粋形
    
- 痕跡化未固定
    

→ _Upper redistribution bound_

---

## 右端：7（Minimal Irreducible Hinge）

**Label:**  
Minimal Non-Absorbed Coarse-Graining

**数理的説明：**

- Smallest prime not absorbed under:
    
    - equal-partition factorization
        
    - low-alphabet collapse
        
    - golden closure reduction
        
- First prime beyond golden regime
    

**構造的意味：**

- 不安定の安定中心
    
- 非吸収的粗視化
    
- Tropotic pivot
    

→ _Minimal hinge of structural irreversibility_

---

# 図のビジュアル構造

```
Golden Closure      Redistribution Field        Irreducible Hinge
     φ  ----------------  θα  ----------------  7
   (closure)             (diffusion)           (hinge)
```

下部に：

$$  
l\alpha g = \text{structural irreversible redistribution}  
$$

---

# キャプション（論文用）

**Figure 1.**  
Structural axis of toroponic redistribution between the Golden Ratio (closure regime), the Golden Angle (maximal non-simultaneity), and the minimal irreducible coarse-grained hinge (7). The heptagonal regime emerges as the smallest prime partition surviving structural absorption and symbolic collapse.

---

<svg xmlns="http://www.w3.org/2000/svg" width="980" height="560" viewBox="0 0 980 560" role="img" aria-label="TPD-02 Figure: φ ↔ θₐ ↔ 7 as the Tropotic lαg Axis with structural notes">
  <defs>
    <style>
      .bg { fill:#ffffff; }
      .ink { fill:#111111; }
      .stroke { stroke:#111111; stroke-width:2; }
      .thin { stroke:#111111; stroke-width:1.4; }
      .dash { stroke:#111111; stroke-width:1.4; stroke-dasharray:6 6; }
      .label { font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Arial, sans-serif; font-size:16px; fill:#111111; }
      .small { font-size:13px; }
      .tiny { font-size:12px; }
      .title { font-size:20px; font-weight:700; }
      .mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }
      .box { fill:none; stroke:#111111; stroke-width:1.4; }
    </style>

    <marker id="arrow" markerWidth="14" markerHeight="14" refX="11" refY="7" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L14,7 L0,14 Z" fill="#111111"/>
    </marker>

    <marker id="arrowThin" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L12,6 L0,12 Z" fill="#111111"/>
    </marker>
  </defs>

  <!-- Background -->
  <rect class="bg" x="0" y="0" width="980" height="560" rx="16" fill="#ffffff" opacity="0.96" stroke="#111" stroke-width="2"/>

  <!-- Title -->
  <text class="label title" x="40" y="40" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="24" font-weight="700" fill="#111">TPD-02 Figure 1 — The Golden Domain and the Heptagonal Hinge</text>
  <text class="label small" x="40" y="65" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="16" font-weight="500" fill="#111">φ (golden closure / trace)  ↔  θ<tspan baseline-shift="sub">α</tspan> (maximal redistribution / rotation)  ↔  7 (minimal non-absorbed hinge)</text>

  <!-- Main axis -->
  <line class="stroke" x1="90" y1="140" x2="890" y2="140" stroke="#333" stroke-width="1" marker-end="url(#arrow)"/>
  <text class="label mono" x="414" y="100" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="20" font-weight="400" fill="#111">Tropotic lαg Axis</text>
  <text class="label tiny" x="260" y="188" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="14" font-weight="300" fill="#111">lαg = irreversible structural redistribution (non-simultaneity under conservation)</text>

  <!-- Nodes: φ, θ_α, 7 -->
  <!-- φ -->
  <circle class="thin" cx="160" cy="140" r="34" fill="none" rx="16" opacity="0.96" stroke="#111" stroke-width="2"/>
  <text class="label" x="155" y="130">φ</text>
  <text class="label small" x="118" y="210">golden closure</text>
  <text class="label small" x="120" y="226">trace regime</text>

  <!-- θ_α -->
  <circle class="thin" cx="490" cy="140" r="34" fill="none" rx="16" opacity="0.96" stroke="#111" stroke-width="2"/>
  <text class="label" x="482" y="128">θ<tspan baseline-shift="sub">α</tspan></text>
  <text class="label small" x="427" y="210">max redistribution</text>
  <text class="label small" x="450" y="226">(irrational rotation)</text>

  <!-- 7 -->
  <circle class="stroke" cx="820" cy="140" r="34" fill="none" rx="16" opacity="0.96" stroke="#111" stroke-width="2"/>
  <text class="label" x="817" y="130">7</text>
  <text class="label small" x="758" y="210">irreducible hinge</text>
  <text class="label small" x="740" y="226">non-absorbed coarse-grain</text>

  <!-- Metastable bracket under axis -->
  <path class="dash" d="M205,158 C290,240 380,270 490,270 C600,270 690,240 775,158" stroke="#333" stroke-width="1" fill="none"/>
  <text class="label small" x="402" y="298">metastable golden domain</text>
  <text class="label tiny" x="290" y="318">coherence sustained between closure (φ) and dispersion (θ<tspan baseline-shift="sub">α</tspan>)</text>

  <!-- Left panel: φ notes -->
  <rect class="box" x="45" y="340" width="295" height="170" rx="16" fill="#ffffff" opacity="0.96" stroke="#111" stroke-width="2"/>
  <text class="label" x="60" y="368">φ — Golden Closure Regime</text>
  <text class="label tiny" x="60" y="394" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="14" font-weight="300" fill="#111">• continued fraction: φ = [1;1,1,1,…]</text>
  <text class="label tiny" x="60" y="414" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="14" font-weight="300" fill="#111">• “most irrational” ⇒ minimal resonance</text>
  <text class="label tiny" x="60" y="434" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="14" font-weight="300" fill="#111">• Sturmian / Fibonacci factorization (ω=1/φ)</text>
  <text class="label tiny" x="60" y="454" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="14" font-weight="300" fill="#111">• ratio as trace condensation</text>
  <text class="label tiny" x="60" y="474" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="14" font-weight="300" fill="#111">• absorption threshold (closure tendency)</text>

  <!-- Middle panel: θ_α notes -->
  <rect class="box" x="350" y="340" width="295" height="170" rx="16" fill="#ffffff" opacity="0.96" stroke="#111" stroke-width="2"/>
  <text class="label" x="365" y="368">θ<tspan baseline-shift="sub">α</tspan> — Redistribution Field</text>
  <text class="label tiny" x="365" y="394" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="14" font-weight="300" fill="#111">• θ<tspan baseline-shift="sub">α</tspan> = 2π(1 − 1/φ)</text>
  <text class="label tiny" x="365" y="414" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="14" font-weight="300" fill="#111">• irrational rotation: Tω(x)=x+ω (mod 1)</text>
  <text class="label tiny" x="365" y="434" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="14" font-weight="300" fill="#111">• equidistribution / no rational locking</text>
  <text class="label tiny" x="365" y="454" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="14" font-weight="300" fill="#111">• maximal non-overlap (generative motion)</text>
  <text class="label tiny" x="365" y="474" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="14" font-weight="300" fill="#111">• source of trace that condenses into φ</text>

  <!-- Right panel: 7 notes -->
  <rect class="box" x="655" y="340" width="300" height="170" rx="16" fill="#ffffff" opacity="0.96" stroke="#111" stroke-width="2"/>
  <text class="label" x="670" y="368">7 — Minimal Non-Absorbed Hinge</text>
  <text class="label tiny" x="670" y="394" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="14" font-weight="300" fill="#111">• prime ⇒ no equal-partition factor (d ∤ 7)</text>
  <text class="label tiny" x="670" y="414" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="14" font-weight="300" fill="#111">• excludes low-alphabet absorption (C1)</text>
  <text class="label tiny" x="670" y="434" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="14" font-weight="300" fill="#111">• excludes golden closure factorization (C2)</text>
  <text class="label tiny" x="670" y="454" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="14" font-weight="300" fill="#111">• avoids over-refinement projection (C3)</text>
  <text class="label tiny" x="670" y="474" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="14" font-weight="300" fill="#111">• minimal irreducible coarse-grained hinge</text>

  <!-- Small connector arrows between nodes -->
  <line class="thin" x1="200" y1="140" x2="455" y2="140" stroke="#333" stroke-width="1" marker-end="url(#arrowThin)"/>
  <line class="thin" x1="525" y1="140" x2="785" y2="140" stroke="#333" stroke-width="1" marker-end="url(#arrowThin)"/>

  <!-- Footer caption -->
  <text class="label tiny" x="40" y="538" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="13" font-weight="300" fill="#111">Caption: φ (trace/closure) ↔ θₐ (irrational rotation / maximal redistribution) ↔ 7 (minimal irreducible non-absorbed hinge) along the Tropotic lαg Axis.</text>
</svg>

**Caption (paper-ready):**  
**Figure 1.** Structural axis of toroponic redistribution between the Golden Ratio (φ; closure/trace regime), the Golden Angle (θₐ; maximal non-simultaneity under irrational rotation), and the minimal non-absorbed coarse-grained hinge (7). The heptagonal regime is the smallest prime partition surviving equal-partition factorization and structural absorption (C1–C3), thereby sustaining coherence between closure and dispersion under lαg.

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
<p align="center">| Drafted Feb 18, 2026 · Web Feb 19, 2026 |</p>