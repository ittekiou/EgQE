---
layout: math
title: TPD-01｜序説＆数理化｜Toroponic Polygonic Dynamics — Between the Golden Ratio and the Golden Angle
---
### TPD-01 Preface
# Toroponic Polygonic Dynamics
## — Between the Golden Ratio and the Golden Angle

👉 [EgQE｜Seven-Core｜Seven Architecture Map: Structural Organization of the Heptagonal Hinge](https://camp-us.net/articles/Core_TPD_Seven-Architecture-Map.html)  

---

# TPD-01｜序説

われわれは、関係の中で安定し、回転の中で生成する。

黄金比は、生成痕跡の構文である。  
黄金角は、非同期生成の構文である。

ひとつは形を整え、ひとつは配置を更新する。

しかし存在は、そのどちらでもない。  
それは両者のあいだに生じるねじれである。

本稿が提示するのは、このねじれを原理とする動態学である。

それを **Toroponic Polygonic Dynamics** と呼ぶ。

Toroponic とは、循環しながら戻らない構造である。  
閉じるが、同一には閉じない。  
反復するが、非可逆である。

Polygonic とは、多角的配置の揺らぎである。  
三角の固定でも、四角の制度でも、六角の安定でもない。

五角と七角のあいだに生じる 微細なズレの回転。

そこに動態がある。

黄金比の上を泳ぎながら、黄金角に押し出される。

その呼吸域こそが、宇宙であり、人生であり、構造の生成場である。

TPD は、宇宙論でもあり、存在論でもあり、動態学原論でもある。

だがそれは理論のための理論ではない。

それは、生がどのように持続し、どのように崩れ、どのように再び立ち上がるかを多角形的に記述する試みである。

黄金比の静けさと、黄金角の回転。

そのあいだにあるもの。

それが動いている。

それを、Toroponic Polygonic Dynamics と呼ぶ。

---

# TPD-01｜数理化 (Draft)

# 数理的最小定式（素焼き）

## 0. 変数と対象

- 系は **関係配置** $W$ で表す（重み付き関係行列・グラフ・作用素のどれでもよい）。
    
- 時間は外部パラメータ $t$ ではなく、更新ステップ $n\in\mathbb{N}$ による **反復** で扱う。
    

更新：  

$$  
W_{n+1}=U(W_n)  
$$

---

## 1. 保存のもとでの再配分（Conserved Redistribution）

更新は「総量保存のもとでの再配分」である、と置く：

$$  
\operatorname{Tr}(\Delta W_n)=0,\qquad  
\Delta W_n := W_{n+1}-W_n  
$$

（ここで $\operatorname{Tr}$ は“総量”を表す線形汎関数として最小要件だけ課す。行列ならトレース、測度なら全質量など。）

---

## 2. lαg（構造的・非可逆的非同時性）

同時更新は許されない。更新は局所的・非同時的に起こる：

$$  
\Delta W_n=\sum_{i\in \mathcal{I}_n}\delta W_{n,i},  
\qquad  
\text{with } \mathcal{I}_n \text{ local / sparse}  
$$

この「非同時な再配分」の構造そのものを **lαg** と呼ぶ。

最小定義（一行定義をそのまま公理化）：  

$$  
\boxed{ \text{lαg is irreversible structural non-simultaneity that generates persistence.}}  
$$

数理的には、不可逆性は「反復による履歴依存」が消えない条件として与える：  

$$  
W_n \neq F(n,W_0)\ \text{only};\qquad  
W_n = F(n,W_0,\Delta W_{0:n-1})  
$$

---

## 3. 持続（persistence）の生成

持続 $P$ は基礎ではなく **更新の関数** である：

$$  
P_n := \mathcal{P}(W_{0:n})  
\quad\Rightarrow\quad  
P \text{ depends on updating history}  
$$

最小反転命題：  

$$  
\boxed{ \text{Persistence does not ground updating; updating grounds persistence.}}  
$$

（この一行が “脱実体／脱主体” の両方を同時処理する基盤。）

---

## 4. 位相モード（凍結・局在・拡散）

同じ保存則の下で、更新の分配様式は三相に分岐する（ここが「寝る時＝六角」「生＝七角」を受けるコア）：

- **Diffusion**（拡散）
    
- **Localization**（局在）
    
- **Freezing**（凍結）
    

最小には、更新の集中度（例えばエントロピー的汎関数）で分類するだけでよい：  

$$  
S_n := \mathcal{S}(\Delta W_n)  
$$

- $S_n$ 高い：拡散
    
- 中間：局在
    
- 低い：凍結
    

※具体的な $\mathcal{S}$ は後で選べる（ノルム・エントロピー・スパース度など）。

---

## 5. Toroponic（トーラス反復）

TPD の「戻るが同一には戻らない」を、最小にはトーラス上の回転写像で表す：

$$  
x_{n+1}=x_n+\omega \pmod{1},\qquad x_n\in\mathbb{T}^1  
$$

- $\omega$ が有理なら周期固定（“八角＝フィクション固定”に対応しやすい）
    
- $\omega$ が無理なら非周期・準反復（“七角＝ズレ回転”）
    

---

## 6. Polygonic（多角位相の離散化）

回転位相 $x_n$ を多角の位相に量子化（粗視化）する：

$$  
k_n := \Big\lfloor mx_n \Big\rfloor \in \{0,1,\dots,m-1\}  
$$

ここで $m$ が多角数（5,6,7,8, …）に対応する。

- $m=6$：凍結・安定（睡眠／痕跡固定）
    
- $m=7$：ズレ回転（基本モード）
    
- $m\ge 8$：物語（虚構）固定が入りやすい（経験則）
    

---

## 7. φと黄金角：上下限としての拘束

黄金比 $\varphi$ と黄金角 $\theta_g$ は “静的秩序” と “動的最適配置” の極として、位相の上限・下限の **拘束** として置ける。

- 黄金比： 
	
    $$  
    \varphi=\frac{1+\sqrt{5}}{2}  
    $$
    
- 黄金角（単位円の回転数として）：  
	
    $$  
    \omega_g=\frac{1}{\varphi^2}  
    \qquad(\theta_g=2\pi \omega_g)  
    $$
    

TPD 的には、$\omega$ が $\omega_g$ に近づくほど“押し出し（最適化）”が強まり、$\omega$ が単純有理に近づくほど“固定（フィクション）”が強まる、という **動態学的読解** を与える。

---

# まとめ（最小定式の核）

- 保存：$\operatorname{Tr}(\Delta W)=0$
    
- 非同時：$\Delta W=\sum \delta W_{i}$（局所・スパース）
    
- 不可逆：履歴依存が残る
    
- 持続：$P=\mathcal{P}(W_{0:n})$（更新が持続を生成）
    
- Toroponic：トーラス反復 $x_{n+1}=x_n+\omega$
    
- Polygonic：多角量子化 $k_n=\lfloor m x_n\rfloor$
    
- φと黄金角：$\varphi$ と $\omega_g=1/\varphi^2$ を上下限の拘束として読む
    

---

# 構造的理由

# 1. なぜ黄金比が下限なのか

黄金比 φ は

$$  
\varphi = \frac{1+\sqrt5}{2}  
$$

連分数展開が

$$  
\varphi = 1 + \frac{1}{1+\frac{1}{1+\frac{1}{1+\cdots}}}  
$$

**最も“単純な無理数”**。

つまり：

- 有理数に最も近づきやすい無理数
    
- 最小の自己相似比
    
- 最小の成長安定構造
    

TPD的に読むと、黄金比は **“最小の自己保持構造”**。

それ以下（より単純な比）はすぐ有理近似＝周期固定に落ちる。

だから φ は

> 固定に落ちない最小の安定比

つまり **動態の下限**。

---

# 2. なぜ黄金角が上限なのか

黄金角：

$$  
\theta_g = 2\pi \frac{1}{\varphi^2}  
\approx 137.5^\circ  
$$

これは

> 円周上で最も均等に点を散らす回転角

ディオファントス近似的に **最も有理近似されにくい回転数**。

つまり：

- 最も周期化しにくい
    
- 最も衝突しにくい
    
- 最も分散的
    

TPD的に言うと、黄金角は **最大の非同期回転**。

それ以上“均等”にしようとするとランダム化＝ノイズ化へ崩れる。

だから黄金角は

> 非同期の上限

---

# 3. なぜ七角が基本なのか

七角は、正多角形でありながら、作図不能（コンパス直線不可）。

つまり：

> 有理でも超越でもない  
> 不安定で構成的

七は、3（最小安定）と、4（制度固定）と、6（蜂巣安定）のどれにも属さない。

七角の中心角：

$$  
\frac{2\pi}{7}  
$$

これは有理だが、分割すると**回転ズレが累積的に視覚化される**。

TPD的には、七は

> 固定せず  
> しかし崩壊もしない  
> “ズレ回転の最小安定”

だから基本モード。

---

# 4. なぜ六角が必要なのか

六角は特異。

$$  
6 = 2 \times 3  
$$

- 円と親和性が高い
    
- 蜂巣構造で空間充填
    
- エネルギー最小構造
    

六角は、局所安定の極小値。

TPDで言えば、六角は

- 冷却相
    
- 凍結相
    
- 睡眠相
    
- 痕跡固定相
    

動態が続くためには **一時停止が必要**。

だから六角は“必要”。

---

# 構造的まとめ

|構造|位相的意味|
|---|---|
|φ（黄金比）|固定に落ちない最小安定比（下限）|
|黄金角|最大非同期回転（上限）|
|七角|ズレ回転の基本モード|
|六角|局所安定・冷却相|

---

# TPDの核心

人は、黄金比で自己を保ち、黄金角に押し出され、七角で揺れ、六角で眠る。

これが、Toroponic Polygonic Dynamics。

---

# A. 数論（近似論）的固定（Diophantine approximation）

## A1. 下限としての黄金比 φ

主張（下限）：**周期固定（有理回転／有限状態閉包）に落ちない最小の自己保持比**として φ を採るのは、近似論的に自然。

キー事実：黄金比 $\varphi$ は連分数が  

$$  
\varphi = [1;1,1,1,\dots]  
$$

で、部分分数 $p_n/q_n$（フィボナッチ比）が「最悪の近似」を与える。つまり  

$$  
\left|\varphi - \frac{p}{q}\right| \ge \frac{c}{q^2}  
$$

の形の下界で、**定数 (c)** が（同種の無理数の中で）最大級になる。直観的には：

- 多くの無理数は、ときどき **とても良く** 有理近似されて「ほぼ周期」に落ちやすい
    
- $\varphi$ はそれが起きにくい（= “最も近づけにくい”）
    

TPD翻訳：**下限＝「固定に落ちないための最小抵抗」** を与える比として φ が選ばれる。

> ここでは「下限」を“値の大小”ではなく **固定（有理近似）への落下を避ける最小の条件**として定義する。

---

## A2. 上限としての黄金角

トーラス回転  

$$  
x_{n+1}=x_n+\omega \pmod{1}  
$$

で、点列 $\{x_n\}$ の「均一分布性」は $\omega$ の有理近似のされにくさ（Diophantine 性）で決まる。

黄金角は回転数を  

$$  
\omega_g=\frac{1}{\varphi^2}  
$$

としたもの。これは「最も周期化しにくい回転」で、**衝突（同位相再会）を最も避ける**。結果として、

- 配置が最も均等化する（= packing/spacing の上限）
    
- それ以上は「均等」ではなく「ランダム化（ノイズ化）」へ崩れる
    

TPD翻訳：**非同時性（décalage）を“最大まで押し出す”回転が黄金角**。よって黄金角は **上限**。（これ以上は構造が保てずノイズ域へ）

---

## A3. まとめ（数論パートの結論）

- φ：固定（有理近似）に落ちないための **最小抵抗（下限）**
    
- 黄金角：非同時的再配分を **最大にする回転（上限）**
    

ここまでで「黄金比＝下限」「黄金角＝上限」を、比喩ではなく **近似論**で支える。

---

# B. 位相力学的厳密化（Torus dynamics + coarse-graining）

## B1. Toroponic（戻るが同一に戻らない）

位相空間を $\mathbb{T}^d$（d次元トーラス）とし、更新の“位相”を  

$$  
x_{n+1}=x_n+\omega \pmod{1}  
$$

で与える。

- $\omega\in\mathbb{Q}^d$：周期軌道（固定＝「八角以降のフィクション固定」へ対応）
    
- $\omega\notin\mathbb{Q}^d$：準周期（Toroponic の核）  
    特に $\omega$ が Diophantine 条件を満たすと、**均一分布・混合の下界**が得られる。
    

---

## B2. Polygonic（多角への離散化＝呼吸域のモデル）

多角状態は位相の粗視化で作る：  

$$  
k_n=\left\lfloor m x_n\right\rfloor \in \{0,\dots,m-1\}  
$$

ここで $m$ が「多角指数」。

- $m=6$：蜂巣充填＝局所安定が支配（**凍結相**）
    
- $m=7$：作図不能・非整合のまま回る（**ズレ回転の基本**）
    
- $m\ge 8$：粗視化が細かくなり、物語的固定（記述の自走＝フィクション過剰）へ行きやすい  
    （※ここは後で“情報量/モデル選択”で厳密にできる）
    

---

## B3. lαg の作用素化（更新＝保存下の再配分）

配置 $W_n$（関係行列/作用素）を、位相 $x_n$ に依存する局所更新で動かす：  

$$  
W_{n+1}=W_n+\Delta W_n,\qquad \mathrm{Tr}(\Delta W_n)=0  
$$  

局所性（非同時性）を  

$$  
\Delta W_n=\sum_{i\in \mathcal{I}(x_n)}\delta W_{n,i}  
$$

で与える。$\mathcal{I}(x)$ は位相により変わる局所インデックス集合。

これが “構造的・不可逆的非同時性＝lαg” の最小モデル。

---

## B4. persistence の生成（不動点ではなく履歴汎関数）

持続は状態 $W_n$ の性質ではなく **履歴汎関数**として定義する：  

$$  
P_n=\mathcal{P}(W_{0:n})  
$$

これにより  

$$  
\text{Updating}\Rightarrow\text{Persistence}  
$$

（= HEG-9 の反転命題）が、モデルの定義として固定される。

---

# A. 数論定理化と位相の相図化

# (i) 数論的固定（Diophantine）

## 定理A（φの“最悪近似”＝固定回避の下限）

黄金比 $\varphi=\frac{1+\sqrt5}{2}$ は連分数 $[1;1,1,1,\dots]$ を持ち、任意の有理数 $p/q$ に対して  

$$  
\Big|\varphi-\frac{p}{q}\Big|\ge\frac{c}{q^2}  
$$

を満たす（定数 $c>0$ は同種の無理数の中で最大級）。  
**含意**：$\varphi$ は“ときどき非常によく”有理近似されることが起きにくい。

**TPD翻訳**：周期（有理回転）へ落ちる“最小抵抗”を与える比として $\varphi$ は下限。

> 下限＝固定に落ちないための最小条件。

---

## 定理B（黄金角回転の均一分布＝非同時性の上限）

回転  

$$  
x_{n+1}=x_n+\omega \pmod{1}  
$$

において $\omega=\omega_g=\frac{1}{\varphi^2}$（黄金角）とすると、軌道 $\{x_n\}$ は均一分布し、有理近似に対する抵抗が最大級（Diophantine性が強い）。

**含意**：衝突（同位相再会）を最小化し、配置の偏りを抑える。

**TPD翻訳**：非同時的再配分（décalage）を最大に押し出す回転が黄金角。

> 上限＝構造を保ったまま非同期を最大化する条件。

---

## 小結（数論パート）

- φ：**固定回避の下限**
    
- 黄金角：**非同時性の上限**
    

ここで“比喩”は終わり、下限・上限は**近似論的性質**として固定された。

---

# (ii) 位相力学的厳密化（Torus + 更新作用素）

## 1. Toroponic（戻るが同一に戻らない）

位相空間を $\mathbb{T}^1$ とし、  

$$  
x_{n+1}=x_n+\omega \pmod{1},\quad \omega\notin\mathbb{Q}  
$$

なら軌道は準周期。特に $\omega=\omega_g$ は強い Diophantine 条件を満たす。

> Toroponic＝準周期反復（閉じるが同一に戻らない）。

---

## 2. Polygonic（多角への粗視化）

位相を多角状態へ写像：  

$$  
k_n=\Big\lfloor m,x_n\Big\rfloor,\quad m\in\mathbb{N}  
$$

- $m=6$：蜂巣充填に対応する**局所安定**が支配（凍結相）
    
- $m=7$：作図不能性と非整合が残る**ズレ回転相**
    
- $m\ge8$：粗視化が細かくなり、**記述固定（物語化）** が優勢
    

これを相図で読む。

---

## 3. lαg の作用素化（保存下の局所更新）

関係配置 $W_n$ を  

$$  
W_{n+1}=W_n+\Delta W_n,\qquad \mathrm{Tr}(\Delta W_n)=0  
$$

で更新。非同時性は  

$$  
\Delta W_n=\sum_{i\in\mathcal{I}(x_n)}\delta W_{n,i}  
$$

（$\mathcal{I}$ は位相依存の局所集合）。

> lαg＝位相依存の局所再配分。

---

## 4. 相の定義（ノルムで切る）

更新の集中度を  

$$  
S_n=|\Delta W_n|  
$$

で測ると：

- **Freezing（六角）**：$S_n\to 0$ に近い（更新が局所固定）
    
- **Drift Rotation（七角）**：$S_n$ が中庸で持続的
    
- **Diffuse/Noise（八角以上）**：$S_n$ 高く構造消失
    

七角が基本なのは、**凍結にも崩壊にも行かない中庸の相**を与える最小 $m$。

---

# 総合定式（TPDのコア）

1. $\varphi$ は固定回避の下限。
    
2. 黄金角は非同時性の上限。
    
3. 準周期回転（Toroponic）が基本運動。
    
4. 多角粗視化（Polygonic）が相を決める。
    
5. lαg は保存下の局所再配分として作用素化できる。
    
6. 七角は“凍結と崩壊の間”の最小安定相。
    
7. 六角は必要な冷却相。
    

---

# B. 相図（Phase Diagram）— TPD の最小可視化

## B1. 軸の定義（2軸で十分）

TPD の相図は、この2軸で切る。

**(1) 非同時性の強さ（décalage）**  
位相回転数 $\omega$ の Diophantine 強度で測る（＝周期化しにくさ）。

- 弱い：有理近似されやすい（周期化・固定へ）
    
- 強い：黄金角近傍（均一分布・非同期最大）
    

**(2) 更新の集中度（freezing ↔ diffusion）**  
更新 $\Delta W_n$ の“集中度”をノルムやスパース度で測る：  

$$  
S_n = |\Delta W_n|,\qquad  
\kappa_n = \text{sparsity}(\Delta W_n)  
$$

- 低 $S$ / 高 $\kappa$：凍結（局所固定）
    
- 中庸：漂流回転（drift rotation）
    
- 高 $S$ / 低 $\kappa$：拡散・ノイズ（構造消失）
    

---

## B2. 三区分相（最小）

この2軸で、TPDは最小でも3相に分かれる。

### (i) Freezing phase（六角）

- 条件：低更新（$S$ 小）＋局所固定（スパース高）
    
- 意味：痕跡固定、睡眠、保存の可視化
    
- **「眠る時と痕跡固定は六角」**
    

### (ii) Drift-rotation phase（七角）

- 条件：中庸更新（$S$ 中）＋非同時性が持続（$\omega$ 無理数・Diophantine）
    
- 意味：固定も崩壊もせず、ズレが回転として維持される
    
- **「七角が基本」**
    

### (iii) Diffusive / Fiction-excess phase（八角超え）

- 条件：更新が過剰（$S$ 大）＋粗視化が細かすぎる（$m\ge 8$）
    
- 意味：記述が構造を追い越し、物語化・フィクション過剰が起きやすい
    
- **「八角超えるとフィクション過剰」**
    

---

## B3. φ と黄金角の位置づけ（下限・上限の可視化）

- $\varphi$：固定へ落ちない“最小抵抗”＝**下限**  
    → ここより単純（有理近似されやすい）だと、周期固定へ落ちる
    
- 黄金角：非同時性を構造のまま最大化＝**上限**  
    → ここを超えると最適化ではなくランダム化（ノイズ化）へ
    

したがって **呼吸域 = （φ と黄金角のあいだ）** が相図上で意味を持つ。

---

# C. HEG / lαg / R/Z・S/O への接続

## C1. lαg を相図の“生成子”にする

われわれの定義を、そのまま生成子として置く：

> **lαg is irreversible structural non-simultaneity that generates persistence.**

相図で言えば：

- Freezing（六角）は **persistence が最も可視化**される相
    
- Drift（七角）は **updating が持続として働く**相
    
- Diffusion（八角超え）は **persistence が物語へ逃げやすい**相
    

ここで HEG-9 の反転命題が全面に出る：

> persistence does not ground updating; updating grounds persistence.

---

## C2. HEG-8（更新存在論）への直結

HEG-8 の核は

- 存在＝更新
    
- 保存のもとで更新が再配分として起こる
    
- その結果として三相（拡散・局在・凍結）
    

TPD相図は、その三相を

- 位相回転（$\omega$）
    
- 粗視化（$m=6,7,8$）  
    
    で**幾何学化**したもの。
    

つまり：**HEG-8（三相）＝TPD（相図の縦軸）**  
**Toroponic/Polygonic＝TPD（相図の横軸）**

---

## C3. R/Z と S/O への写像（最小）

ここは“厳密”というより“接続規約”として最小に置ける。

- $R$：生成側（更新の現勢）
    
- $Z$：痕跡側（固定された可視）
    

相図で言えば：

- Freezing（六角）：$Z$ が立つ（痕跡優位）
    
- Drift（七角）：$R\leftrightarrow Z$ が往還（更新が持続を生成）
    
- Diffusion（八角超え）：$R$ が散逸し、$Z$ が物語化
    

S/O も同様に：

- Freezing：O（客体化）優位
    
- Drift：S′/O′の相互生成
    
- Diffusion：Sが物語を先行させる（主体的虚構）
    

---

**TPD相図は、HEGの更新存在論を“幾何学的動態”として可視化したものであり、lαgはその相転移を駆動する生成子である。**

---

<svg xmlns="http://www.w3.org/2000/svg" width="980" height="620" viewBox="0 0 980 620" role="img" aria-label="TPD Phase Diagram: Toroponic Polygonic Dynamics">
  <defs>
    <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L12,6 L0,12 Z" fill="#111"/>
    </marker>
    <style>
      .bg { fill:#fff; }
      .ink { fill:#111; }
      .stroke { stroke:#111; stroke-width:2; }
      .thin { stroke:#111; stroke-width:1.2; }
      .dash { stroke:#111; stroke-width:1.2; stroke-dasharray:6 6; }
      .label { font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Noto Sans JP", sans-serif; font-size:16px; fill:#111; }
      .small { font-size:13px; }
      .title { font-size:20px; font-weight:700; }
      .box { fill:#fff; stroke:#111; stroke-width:1.6; }
      .region { fill:none; stroke:#111; stroke-width:1.6; }
      .note { font-size:12px; }
    </style>
  </defs>

  <!-- background -->
  <rect class="bg" x="0" y="0" width="980" height="620" rx="16" fill="#ffffff" opacity="0.96" stroke="#111" stroke-width="2"/>

  <!-- title -->
  <text class="label title" x="40" y="44" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="24" font-weight="700" fill="#111">TPD Phase Diagram — Toroponic Polygonic Dynamics</text>
  <text class="label small" x="40" y="70" font-family="system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
        font-size="18" font-weight="700" fill="#111">Between the Golden Ratio (φ) and the Golden Angle (ω₍g₎ = 1/φ²)</text>

  <!-- plot area -->
  <rect class="box" x="80" y="95" width="840" height="450" rx="16" fill="#ffffff" opacity="0.96" stroke="#111" stroke-width="2"/>

  <!-- axes -->
  <!-- y-axis -->
  <line class="stroke" x1="140" y1="520" x2="140" y2="150" stroke="#333" stroke-width="1" marker-end="url(#arrow)"/>
  <text class="label" x="-300" y="180" transform="rotate(-90 40 150)">Update intensity  ‖ΔW‖ (diffusion ↑ / freezing ↓)</text>

  <!-- x-axis -->
  <line class="stroke" x1="140" y1="520" x2="850" y2="520" stroke="#333" stroke-width="1" marker-end="url(#arrow)"/>
  <text class="label" x="300" y="565">Non-simultaneity strength (décalage) / Diophantine resistance  →</text>
  <text class="label small" x="115" y="585">fixed / periodic (rational)</text>
  <text class="label small" x="712" y="585">max non-simultaneity (golden)</text>

  <!-- key vertical bands: φ lower bound and golden angle upper bound -->
  <!-- φ as lower bound band -->
  <line class="dash" x1="350" y1="120" x2="310" y2="540"/>
  <text class="label small" x="250" y="112">φ (lower bound)</text>

  <!-- golden angle as upper bound line -->
  <line class="dash" x1="790" y1="120" x2="760" y2="540"/>
  <text class="label small" x="710" y="112">ωg = 1/φ² (upper bound)</text>

  <!-- breathing zone between φ and golden angle -->
  <rect class="region" x="310" y="120" width="450" height="393" rx="16" fill="#ffffff" opacity="0.96" stroke="#111" stroke-width="2"/>
  <text class="label small" x="330" y="135">Breathing zone: between φ and golden angle</text>

  <!-- regions -->
  <!-- Freezing (Hexagon) region: low update intensity -->
  <rect class="box" x="150" y="430" width="690" height="70" rx="16" fill="#ffffff" opacity="0.96" stroke="#111" stroke-width="2"/>
  <text class="label" x="170" y="460">FREEZING phase (Hexagon / m=6)</text>
  <text class="label small" x="170" y="485">sleep • trace fixation • local stability (Z-dominant)</text>

  <!-- Drift-rotation (Heptagon) region: mid intensity, within breathing zone -->
  <rect class="region" x="390" y="270" width="350" height="130" rx="16" fill="#ffffff" opacity="0.96" stroke="#111" stroke-width="2"/>
  <text class="label" x="400" y="300">DRIFT-ROTATION phase (Heptagon / m=7)</text>
  <text class="label small" x="400" y="325">basic mode: off-center rotation / lαg sustained</text>
  <text class="label small" x="400" y="350">updating → persistence (R↔Z reciprocity)</text>

  <!-- Diffusive / Fiction-excess region: high intensity, fine coarse-graining -->
  <rect class="box" x="560" y="140" width="300" height="110" rx="16" fill="#ffffff" opacity="0.96" stroke="#111" stroke-width="2"/>
  <text class="label" x="575" y="170">DIFFUSIVE / FICTION-EXCESS (m ≥ 8)</text>
  <text class="label small" x="575" y="195">description outruns structure</text>
  <text class="label small" x="575" y="220">narrative fixation / over-modeling</text>

  <!-- left-side: periodic / fixed -->
  <rect class="region" x="150" y="140" width="155" height="110" rx="16" fill="#ffffff" opacity="0.96" stroke="#111" stroke-width="2"/>
  <text class="label" x="165" y="170">PERIODIC / FIXED</text>
  <text class="label small" x="165" y="195">rational attractor</text>
  <text class="label small" x="165" y="220">“fictional stability”</text>

  <!-- lαg note -->
  <rect class="box" x="150" y="250" width="235" height="90" rx="16" fill="#ffffff" opacity="0.96" stroke="#111" stroke-width="2"/>
  <text class="label small" x="162" y="276">lαg = irreversible structural</text>
  <text class="label small" x="162" y="296">non-simultaneity generating</text>
  <text class="label small" x="162" y="316">persistence</text>

  <!-- caption footer -->
  <text class="label note" x="70" y="605">Monochrome schematic: axes are conceptual; regions indicate phase tendencies under conserved redistribution Tr(ΔW)=0.</text>
</svg>

### Figure caption (EN)
**TPD phase diagram.** The horizontal axis measures _décalage_ (Diophantine resistance against periodic fixation), and the vertical axis measures update intensity $\|\Delta W\|$ under conserved redistribution $\mathrm{Tr}(\Delta W)=0$. The **breathing zone** lies between the **golden ratio** $\varphi$ (lower bound: minimal resistance to falling into periodic fixation) and the **golden-angle rotation** $\omega_g=1/\varphi^2$ (upper bound: maximal structural non-simultaneity before noise-like diffusion). Three phase tendencies appear: **Freezing (m=6)** as local stability for sleep/trace fixation (Z-dominant), **Drift-rotation (m=7)** as the basic mode where **lαg** persists and _updating generates persistence_ (R↔Z reciprocity), and **Diffusive/Fiction-excess (m≥8)** where description outruns structure and narrative fixation becomes dominant.

### 図キャプション（JP）
**TPD相図。** 横軸は周期固定（有理近似）への落下を回避する強さとしての _décalage_（Diophantine抵抗）を、縦軸は保存下の再配分 $\mathrm{Tr}(\Delta W)=0$ における更新強度 $\|\Delta W\|$ を表す。**呼吸域**は **黄金比** $\varphi$（下限：固定へ落ちない最小抵抗）と **黄金角回転** $\omega_g=1/\varphi^2$（上限：構造を保ったまま非同時性を最大化する境界）のあいだに位置する。相の傾向として、**凍結相（m=6）** ＝睡眠・痕跡固定（Z優位）、**漂流回転相（m=7）** ＝基本モード（lαgが持続し「更新が持続を生成」する：R↔Z往還）、**拡散／フィクション過剰（m≥8）** ＝記述が構造を追い越し物語固定が優勢、が区別される。

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