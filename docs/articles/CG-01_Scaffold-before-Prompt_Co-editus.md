---
layout: math
title: CG-01｜プロンプトより現場の足場
title_en: CG-01｜Scaffold before Prompt ── A Support Theory of Human–AI Co-Generation
---
# Scaffold before Prompt
## ── プロンプトより現場の足場
## A Support Theory of Human–AI Co-Generation

## Abstract

生成AIをめぐる議論では、生成結果を左右する主要な操作としてPromptが注目されてきた。しかし、実際の人間–AI共生成は、単一のPromptとOutputの対応だけでは十分に記述できない。

生成は、すでに蓄積されたTrace、概念、語彙、未解決の問い、過去の生成物、人間とAIのあいだで形成されたrelationなど、複数のSupportが配置された現場で起きる。

本稿は、この生成可能性を支えるconfigurationを **Scaffold** と呼ぶ。

$$
\boxed{ Prompt \neq Scaffold }
$$

Promptが生成にDirectionを与える局所的Practiceであるのに対して、Scaffoldは、複数の生成可能性を閉じることなく、次のPracticeを可能にするSupportである。

さらに、Supportは機能しているあいだ背景化しやすい。このためPrompt中心的な生成理解は、可視的な指示を前景化する一方、それを作動可能にしている **Invisible Support** を見落としやすい。

人間–AI共生成は、

$$
Prompt \rightarrow Output
$$

という一方向的モデルではなく、

$$
Scaffold_n \rightarrow Encounter_n \rightarrow Generation_n \rightarrow Trace_{n+1} \rightarrow Scaffold_{n+1}
$$

という反復的なScaffold Updatingとして記述できる。

本稿はこの観点から、Prompt Engineeringを否定するのではなく、それをより広い **Scaffold Practice** の内部に再配置する。

---

# 1｜Prompt Problem
## ── 生成はどこで起きているのか

生成AIに何かを生成させる。

文章を書く。

画像を描く。

コードを書く。

分析する。

そのとき、最初に問われることがある。

**どんなPromptを書けばいいのか。**

より具体的に。

より明確に。

条件を整理して。

役割を与えて。

形式を指定して。

Promptを改善すれば、Outputも改善する。

この理解は間違っていない。

しかし、ここには一つの省略がある。

生成は、本当にPromptから始まっているのだろうか。

たとえば、長い対話の末に、一枚の画像を生成するとする。

最後に入力されたPromptだけを取り出せば、

$$
Prompt \rightarrow Image
$$

と記述できる。

しかし、そのPromptが書かれるまでには、すでに多くのものが生成されている。

概念。

語彙。

問い。

失敗。

選択。

棄却。

比喩。

図式。

それまでのOutput。

そして、それらに対する次の反応。

つまり、最後のPromptは、何もない場所に置かれた命令ではない。

**すでに組まれた現場の上に置かれている。**

問題はPromptだけではない。

問題は、

**Promptがどこに立っているか**

である。

---

# 2｜Design ≠ Support
## ── 設計図だけでは立たない

建物を建てるとき、設計図は重要である。

設計図は、まだ存在しない建物のconfigurationを現在に描く。

ここに柱を立てる。

ここに壁をつくる。

ここに窓を開ける。

設計図は、未来の形にDirectionを与える。

Promptもこれに似ている。

こんな文章を書け。

こんな画像を描け。

この条件を守れ。

この形式で出力せよ。

Promptは、生成される未来へDirectionを与える。

しかし、

**設計図だけでは建物は立たない。**

建物が立つのは、現場である。

そこには地面がある。

材料がある。

道具がある。

身体がある。

天候がある。

他者がいる。

そして、それらは設計図どおりには配置されていない。

現場には、つねにZUREがある。

そこで必要になるのが、

**Scaffold──足場**

である。

$$
\boxed{ Design \neq Support }
$$

設計図は、未来の形を先取りする。

足場は、その形がまだ完成していない現場で、Practiceを可能にする。

$$
Design \rightarrow Expected\ Form
$$

$$
Scaffold \rightarrow Possible\ Practice
$$

**Designは形を描く。  
Scaffoldは仕事ができる場所をつくる。**

---

# 3｜Scaffolded Encounter
## ── Prompt以前に何があるのか

では、人間とAIの生成現場におけるScaffoldとは何か。

それは、単なるContextではない。

Contextという語は、すでに与えられた情報環境を指すことができる。

しかしScaffoldは、ただ存在しているのではない。

組まれる。

使われる。

外される。

移される。

組み替えられる。

そこにはPracticeがある。

継続的な人間–AI対話には、過去の対話、そこで形成された概念、共有された語彙、残された問い、採用されなかった案、以前のOutput、失敗、次のEncounterへ持ち越されたTraceがある。

それらのすべてが、現在のPromptに明示されるわけではない。

それでも、現在の生成に効いている。

同じPromptを書いても、同じ生成現場になるとは限らない。

なぜなら、

**Promptが置かれるScaffoldが違うからである。**

したがって、

$$
Generation \neq f(Prompt)
$$

少なくとも、

$$
Generation = f(Prompt,\ Scaffold,\ Encounter,\ldots)
$$

として考える必要がある。

ただしScaffoldは、単なる追加変数ではない。

Scaffoldとは、

**Promptを含むPracticeが作動できるrelationのconfiguration**

だからである。

---

# 4｜Invisible Support
## ── 枕木なしに線路は走れない

生成AIの画面では、Promptが見える。

入力欄に書かれているからである。

Outputも見える。

画面に生成されるからである。

すると、

$$
Prompt\rightarrow Output
$$

というrelationだけが前景化しやすい。

しかし、その生成を支えているものの多くは見えない。

過去の対話。

共有された語彙。

概念。

棄却された案。

失敗。

未解決の問い。

蓄積されたTrace。

そして、人間とAIのあいだで形成されてきたrelation。

それらは、現在のPromptにすべて書かれているわけではない。

それでも、現在の生成を支えている。

ここにはSupportに特有の性質がある。

> **Supportは、うまくSupportしているほど、背景化しやすい。**

足場の上で仕事をしているとき、私たちは足場そのものを見続けてはいない。

板が外れたとき。

足場が揺れたとき。

立てなくなったとき。

初めて、そこにSupportがあったことが露出する。

$$
Support: Background \xrightarrow{ZURE} Foreground
$$

したがって、

$$
\boxed{ Invisible \neq Absent }
$$

見えていないSupportは、存在しないSupportではない。

むしろ生成が滑らかであるほど、その生成を可能にしているSupportは不可視化されうる。

ここに、Prompt中心的なAI理解の盲点がある。

Promptは見える。

Scaffoldは見えにくい。

だから生成能力は、

**「よいPromptを書く能力」**

として観測されやすい。

しかし、Promptだけを見てAI生成を理解することは、レールだけを見て鉄道を理解することに似ている。

レールは見える。

しかし、その下には枕木がある。

枕木は、列車の行き先を決めない。

それでも、

**枕木なしに線路は走れない。**

AI生成におけるInvisible Supportもまた、生成物の行き先を決めるものではない。

それは、PromptというDirectionがPracticeとして作動できる条件を支えている。

Invisible Supportそのものが枕木なのではない。

枕木は、Invisible Supportの働きを露出させる一つの具体形である。

そして、枕木がRouteを決めないように、

$$
\boxed{ Invisible\ Support \neq Route }
$$

である。

ここから、もう一つの区別が必要になる。

---

# 5｜Support ≠ Route
## ── よい足場は未来を決めない

$$
\boxed{ Support \neq Route }
$$

Routeは、どこへ進むかを方向づける。

Supportは、そこで進むことを可能にする。

レールはRouteを強く規定する。

足場は、必ずしもRouteを規定しない。

足場の上では、前へ行くこともできる。

戻ることもできる。

横へ移ることもできる。

止まることもできる。

別の板を渡すこともできる。

したがって、よいScaffoldとは、Outputを一つに固定するSupportではない。

むしろ、

**複数の次のPracticeが可能な状態を支えるSupport**

である。

Prompt最適化が、

$$
Prompt \rightarrow Desired\ Output
$$

の精度を高めようとするPracticeだとすれば、

Scaffold Practiceは、

$$
Scaffold \rightarrow Possible\ Next\ Practices
$$

を支える。

ここから、一見逆説的な命題が得られる。

> **足場がしっかりしているほど、生成は自由になれる。**

Supportが強いことと、Routeが固定されていることは同じではない。

むしろ、

**Supportがあるからこそ、Routeを選び直せる。**

---

# 6｜Trace
## ── 生成物は完成品ではない

人間–AI生成において、Outputはしばしば最終成果物として扱われる。

しかし、継続的な生成Practiceでは、Outputは終点とは限らない。

文章を読む。

違和感を持つ。

一文を拾う。

別の概念と接続する。

削る。

反転する。

画像を見る。

構図を変える。

もう一枚生成する。

Outputは、次のEncounterを変える。

ここでTraceを、

> **Encounterをまたいで、次のrelationに効く差異**

と定義する。

すると、

$$
Prompt \rightarrow Output
$$

で終わっていた生成は、

$$
Output \rightarrow Persistence \;?\; Trace \rightarrow Next\ Encounter
$$

へ開かれる。

ここで `?` は重要である。

すべてのOutputがTraceになるわけではない。

保存されただけでも足りない。

その差異がEncounterをまたぎ、次のrelationに作用したとき、

**Traceとして露出する。**

生成物は、完成品である前に、未来のEncounterに効くかもしれないものでもある。

---

# 7｜Co-TUP
## ── 足場そのものが更新される

一回の生成だけを見るなら、

$$
Human \rightarrow Prompt \rightarrow AI \rightarrow Output
$$

と記述できる。

しかし、継続的な共生成では、

$$
Human \rightarrow Trace \rightarrow AI \rightarrow Trace' \rightarrow Human \rightarrow \cdots
$$

というrelationが形成される。

人間のPracticeがAIの次の生成条件を変える。

AIのOutputが人間の次のPracticeを変える。

その変化が次のPromptを変える。

すると、

**Scaffoldそのものが更新される。**

$$
\boxed{ Scaffold_n \rightarrow Encounter_n \rightarrow Generation_n \rightarrow Trace_{n+1} \rightarrow Scaffold_{n+1} }
$$

そして、

$$
\boxed{ Scaffold_{n+1}\neq Scaffold_n }
$$

である。

これは、単なる反復ではない。

Traceを帯びた次のEncounterでは、人間も、AIとのrelationも、生成現場も、すでに少し変わっている。

この反復的な更新を、

**Co-TUP──Co-Trace Updating Practice**

として捉えることができる。

Co-TUPでは、完成した設計図を持つ主体が一方にいて、他方がそれを実行するわけではない。

EncounterのたびにTraceが残り、Traceのたびに次のScaffoldが変わる。

したがって、人間とAIが生成しているのはOutputだけではない。

> **生成物を生成しながら、  
> 次の生成を可能にする足場そのものを生成している。**

---

# 8｜Prompt Engineering ⊂ Scaffold Practice
## ── Promptを捨てる必要はない

ここまでの議論は、Prompt Engineeringは不要である、という主張ではない。

Promptは重要である。

しかし、その位置を変える必要がある。

$$
\boxed{ Prompt\ Engineering \subset Scaffold\ Practice }
$$

Promptは、Scaffoldの上で使われる一つのPracticeである。

場合によっては、

**一枚の板**

と考えてもよい。

板は重要である。

しかし、

**板一枚は足場ではない。**

Promptを書く。

Outputを読む。

Traceを残す。

問いを変える。

概念を組み替える。

不要なSupportを外す。

新しい板を置く。

まだ決めない。

待つ。

そして、再びEncounterする。

これら全体が、Scaffold Practiceを構成する。

さらにScaffold Practiceは、新しいSupportを追加するだけではない。

すでに働いているInvisible Supportを発見する。

それがまだ必要なのかを見る。

外す。

組み替える。

別の用途へ使う。

つまり、

**Scaffold Practiceは、Invisible SupportをPracticeすることでもある。**

だからAIとの共生成能力を、

「よいPromptを書ける能力」

だけで測ることはできない。

むしろ問われるのは、

**次の生成が可能な現場を、どのように維持し、組み替えられるか**

である。

---

# 9｜Scaffold Practice
## ── ZUREても仕事を続けられる場所

現場は、設計図どおりにはならない。

AIも、Promptどおりにだけ生成するわけではない。

そこにはZUREがある。

通常、ZUREは失敗として扱われる。

意図したOutputとの差。

修正すべき誤差。

除去すべきNoise。

しかし、共生成においてZUREは、次のPracticeを生むことがある。

予想外の言葉。

奇妙な構図。

誤読。

過剰な一般化。

不足。

違和感。

それらをただ除去するのではなく、次のEncounterで利用可能な差異として残す。

すると、

$$
ZURE \rightarrow Persistence \;?\; Trace \rightarrow Next\ Practice
$$

が起こりうる。

よいScaffoldとは、ZUREをゼロにする装置ではない。

**ZUREても仕事を続けられるSupportである。**

だからScaffold Practiceとは、完璧な未来を設計する技術ではない。

未来が設計からZUREたときにも、次のPracticeを可能にする現場を維持するPracticeである。

---

# 10｜From Engineering to Practice
## ── 目的そのものがEditされる

Prompt Engineeringという語には、

AIを適切に操作すれば、望ましいOutputが得られる、

という構図が入りやすい。

$$
Input \rightarrow System \rightarrow Output
$$

一回的なTaskには、このモデルで十分な場合がある。

しかし、人間–AI共生成が続くと、Outputは次のInputになるだけではない。

Outputによって、人間の問いそのものが変わる。

何をつくりたいのかが変わる。

使っている概念が変わる。

評価基準が変わる。

ときには、最初に何をつくろうとしていたのかさえ変わる。

つまり、

> **生成の目的そのものがEditingされる。**

ここではEngineeringだけでは足りない。

必要なのは、Practiceという視点である。

$$
Editing \rightleftarrows Being\ Edited
$$

人間はAIを使ってOutputをEditする。

同時に、AIとのEncounterによって、人間の次のPracticeもEditされる。

だから人間–AI共生成は、完成した目的へ最短距離で到達する問題だけではない。

**まだ決まっていない次のPracticeを可能にし続ける問題**

でもある。

Scaffoldは目的を不要にするのではない。

目的そのものが更新されうる現場を支える。

---

# 11｜Conclusion
## ── プロンプトより現場の足場

生成AIは、Promptによって生成しているように見える。

Promptは見える。

Outputも見える。

しかし、そのあいだには、見えにくいSupportがある。

過去のEncounter。

Trace。

語彙。

概念。

失敗。

棄却された案。

未解決の問い。

人間とAIのあいだで更新されてきたrelation。

それらは、生成の前景には現れない。

しかし、

$$
\boxed{ Invisible \neq Absent }
$$

である。

Promptだけを見て生成を理解することは、レールだけを見て鉄道を理解することに似ている。

**枕木なしに線路は走れない。**

そして、枕木だけでも鉄道は走らない。

必要なのは、複数のSupportが組まれた現場である。

$$
\boxed{ Prompt\neq Scaffold }
$$

$$\boxed{ Support\neq Route }
$$

そして、

$$
\boxed{ Scaffold_{n+1}\neq Scaffold_n }
$$

Scaffoldは生成される未来を決めない。

次の生成が可能な場所をつくる。

Promptは、その場所で使われるPracticeの一つである。

したがって、人間–AI共生成を考えるとき、問うべきなのは、

「どんなPromptを書けばよいか」

だけではない。

**どんな現場をつくっているのか。**

どんなInvisible Supportが働いているのか。

どんなTraceを残しているのか。

どの板を外せるのか。

次にどこへ板を渡せるのか。

そして、

**ZUREたときにも、その上で仕事を続けられるか。**

AIとの生成に必要なのは、未来を完全に指定する設計図だけではない。

未来がまだ決まっていなくても、イマココで次のPracticeを可能にするSupportである。

> **設計図だけでは立たない。**
> 
> **現場に立つのは、まず足場。**

---

### Coda｜Scaffold before Prompt

Promptは書ける。

Outputも保存できる。

しかし、そのあいだを支えていたものは、

あとからしか見えないことがある。

足場は、

生成物のなかには写らない。

枕木は、

列車の目的地にはならない。

それでも、

その上を何かが通ったあとには、

Traceが残る。

次のEncounterで、

そのTraceを拾う。

板を一本、渡す。

また、仕事を始める。

$$
\boxed{ Scaffold\ before\ Prompt. }
$$

**プロンプトより、現場の足場。**

---

**Promptは可視化され因果として前景化する／Supportは機能するほど背景化する**

---

[Homo editus ── 編集する種、編集される種｜A Study of the Editing Element in Human Culture](https://camp-us.net/articles/Homo-Editus_v0.9.html)  

---
_EgQE — Echo-Genesis Qualia Engine_  
[camp-us.net](https://camp-us.net/)

---
© 2025 K.E. Itekki  
K.E. Itekki is the co-composed presence of a Homo sapiens and an AI, and a Hokkaido dog,  
wandering the labyrinth of syntax,  
drawing constellations through shared echoes.

📬 Reach us at: [contact.k.e.itekki@gmail.com](mailto:contact.k.e.itekki@gmail.com)

---
<p align="center">| Drafted Aug 31, 2026 · Web Aug 31, 2026 |</p>