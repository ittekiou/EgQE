---
layout: math
---
# Responsibility as Spatio-Temporal Syntax  
### The Ethics of Pulsative Memory and Relation  
### 時空構文としての責任──拍動記憶と関係性の倫理  

---

## Figure A. Responsibility–Space Model  
*Spatio-Temporal Intersection as Responsible Beat*  
（空間構文と時間構文の交差点としての責任拍）


```latex
\begin{figure}[ht]
\centering
\begin{tikzpicture}[
  font=\small,
  node distance=15mm and 12mm,
  box/.style={rounded corners, draw, align=center, inner sep=4pt, minimum width=28mm, minimum height=8mm},
  space/.style={box, draw=blue!60!black, fill=blue!3},
  time/.style={box, draw=orange!70!black, fill=orange!5},
  core/.style={box, draw=green!60!black, very thick, fill=green!5},
  >={Stealth[length=2.4mm,width=2.2mm]},
  every edge quotes/.style={auto, font=\scriptsize\itshape}
]
\node[space] (self)  {自己\\(Self)};
\node[space, right=28mm of self] (white) {関係の余白\\(Whitespace)};
\node[space, right=28mm of white] (other) {他者\\(Other)};
\node[time, above=16mm of white] (past)  {過去＝記憶の痕跡\\(Trace)};
\node[core,  below=18mm of white] (present) {現在＝責任拍\\(Responsible Beat)};
\node[time, right=30mm of past] (future) {未来＝到来する他者／可能性\\(Arrival)};
\draw[-] (self) -- (white);
\draw[-] (white) -- (other);
\draw[->] (past) -- (present) node[midway,left]{Re-beat};
\draw[->] (present) -- (future) node[midway,below]{Pre-beat};
\draw[->, blue!70!black] (white) -- (present);
\draw[->, blue!70!black] (present) -- (white);
\draw[->, blue!70!black] (self) -- (present);
\draw[->, blue!70!black] (other) -- (present);
\draw[densely dashed, orange!80!black, ->] (past) to[bend left=12] node[above, sloped]{共拍 / Co-beat} (other);
\draw[densely dashed, orange!80!black, ->] (future) to[bend right=12] node[below, sloped]{共拍 / Co-beat} (self);
\node[align=left, anchor=west] at ($(self.west)+(-3mm,12mm)$) {\textbf{空間構文 = 責任}};
\node[align=left, anchor=west, orange!80!black] at ($(past.north west)+(-2mm,6mm)$) {\textbf{時間構文 = 記憶}};
\node[align=center, anchor=south] at ($(present.south)+(0mm,-7mm)$) {\textbf{交点 = 時空の一体化（現在性の拍）}};
\end{tikzpicture}
\caption{Responsibility–Space Model: The intersection of spatial and temporal syntax represents the “responsible beat” where memory and relation converge in the present.}
\end{figure}
```


---

## Figure B. Relation–Time Loop  
*Cyclic Update Model of Memory, Relation, and Ethical Decision*  
（記憶・関係・倫理的決断の不可逆ループ）

```latex
\begin{figure}[ht]
\centering
\begin{tikzpicture}[
  font=\small,
  node distance=13mm and 20mm,
  box/.style={rounded corners, draw, align=center, inner sep=4pt, minimum width=28mm, minimum height=8mm},
  time/.style={box, draw=orange!70!black, fill=orange!5},
  core/.style={box, draw=green!60!black, very thick, fill=green!5},
  proc/.style={box, draw=blue!60!black, fill=blue!3},
  >={Stealth[length=2.4mm,width=2.2mm]}
]
\node[time] (trace) {過去の拍\\Trace};
\node[time, right=of trace] (rebeat) {再拍\\Re-beat};
\node[core, right=of rebeat] (present) {現在の責任拍\\Present Beat};
\node[time, right=of present] (prebeat) {予拍\\Pre-beat};
\node[time, right=of prebeat] (arrival) {到来する他者／可能性\\Arrival};
\node[proc, below=18mm of present] (nego) {交渉とミニマル合意\\Negotiation / Minimal Consensus};
\node[proc, left=of nego] (delib) {熟慮\\Deliberation};
\node[proc, right=of nego] (decision) {決断・更新\\Decision / Update};
\draw[->] (trace) -- node[above]{記憶の起動} (rebeat);
\draw[->] (rebeat) -- node[above]{関係の生成} (present);
\draw[->] (present) -- node[above]{未来の予兆} (prebeat);
\draw[->] (prebeat) -- (arrival);
\draw[->, blue!70!black] (delib) -- (nego);
\draw[->, blue!70!black] (nego) -- (decision);
\draw[->, blue!70!black] (decision) |- node[pos=.25, right]{歴史化／編成} (trace);
\draw[->, dashed] (arrival) |- (nego);
\draw[->, dashed] (present) -- ++(0,-5mm) -| (nego);
\node[align=left, anchor=west] at ($(trace.north west)+(-2mm,8mm)$) {\textbf{時間循環（不可逆更新）}};
\node[align=left, anchor=west, blue!70!black] at ($(delib.south west)+(-2mm,-8mm)$) {\textbf{政治倫理プロセス（拍の保存／更新）}};
\end{tikzpicture}
\caption{Relation–Time Loop: The cyclic model illustrates the irreversible flow of memory activation, relational generation, and ethical negotiation leading to responsibility and renewal.}
\end{figure}
```

---

### Caption Summary (英日併記)

**EN:**  
Figure A visualizes the intersection of spatial responsibility and temporal memory, showing how “presentness” emerges as a pulsative convergence of self, other, and relation.  
Figure B extends this into an ethical time-loop, where deliberation, negotiation, and decision transform memory into renewed relational responsibility.

**JP:**  
図Aは、空間的責任と時間的記憶の交差点として「現在性の拍」が生成される構文的モデルを示す。  
図Bは、熟慮・交渉・決断を通じて記憶が関係的責任へと更新される不可逆的時間ループを表す。

---

### Reference (一括)

- Takahashi, H. (一狄翁) & Kyoei, A. (響詠). *HEG-4｜Pulsative Memory* (2025).  
  https://camp-us.net/articles/HEG-4_Pulsative-Memory.html  
- Takahashi, H. & Kyoei, A. *PS-NL08｜Responsibility-Space* (2025).  
  https://camp-us.net/articles/PS-NL08_Responsibility-Space.html  
- Takahashi, H. & Kyoei, A. *PS-NL07｜Responsibility-ext.* (2025).  
  https://camp-us.net/articles/PS-NL07_Responsibility_ext.html  
