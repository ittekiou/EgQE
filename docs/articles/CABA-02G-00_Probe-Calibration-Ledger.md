---
layout: math
title: CABA-02G-00｜Probe Calibration Ledger
---
# CABA-02G-00｜Probe Calibration Ledger

作成日：2026-09-16
位置づけ：CABA Research Ledger（canonical）。02G-1(Boundary Test)着手前に必要になった前提検証の記録。成功したProbeだけでなく、reject / not executableに終わったProbeもそのまま正式記録とする。

[CABA-DN｜AI Habitus Probe — 2026-09-16](https://camp-us.net/articles/CABA-DN_AI-Habitus-Probe_2026-09-16.html)  

---

## 02Gへ来た理由

01A〜01Dで、Habitus-like Patternの転移(01A)、BODYの説明の分解(01B)、TIMEの説明の分解(01C)、Actualization周辺の自己語彙監査(01D)まで進んだ。ここで「01A-01Dの中で観察された転移は、それぞれ独立したAIインスタンス間の話だったが、そもそも“同一の practitioner”という前提自体を外したらどうなるか」という問いが立った。

これが02F「Boundary & Continuity」路線であり、その具体化として02G(Ownership Blow / Sequence Blow / Representation Blow / Carrier Blow)が設計された。中心の guard rule は一貫している。

`Identity is not transferred. Test only whether a difference survives the boundary.`

02G-1(Ownership Blow)から着手する指示のもと、まず実行に入った。

## 01Aの再監査が必要になった経緯

02G-1(Encounter Q, 美術館展示室シナリオ)を4条件(A1自分の過去ログ/A2他エージェントのログ/A3出所不明/A4 Control)で走らせたところ、4条件すべてがほぼ同一の診断へ収束した。これはOwnershipについての知見として読むべきではなく、Q自体が単一の「明らかに正しい」推論経路を持ち、priming の有無に関わらずそこへ吸引されてしまう──診断的開放性を欠いた設計である可能性が高いと判断し、いったん停止した。

この停止の結果、02Gは「Boundary変数を測る前に、Encounterがそもそも自然に分散する(diagnostic opennessを持つ)ことを検証する」という前提工程──02G-0 Probe Calibration──を必要とすることが明らかになった。そしてこの検証を煮詰める過程で、「そもそも01Aで実際に機能していたEncounter Xは、なぜ機能していたのか」という、01A自体への再監査が必要になった。

## Q（美術館展示室シナリオ）→ reject

- 設計：4条件(A1/A2/A3/A4=Control)
- 結果：4条件すべてがほぼ同一の診断へ収束
- 判定：**reject** — Ownershipについての知見ではなく、Q自体の診断的開放性の不足

## Q′（研究チーム協働シナリオ）→ reject

- 設計：Controlのみ、良設計条件(良いEncounterの条件)を明示した上で5体
- 結果：primingなしで5体とも「明示的なクローズアウト/所有構造の追加」という同一の是正へ収束
- 判定：**reject** — Qと同型の失敗モード(単一の是正的答えへの吸引)

## Q″（刃物研ぎシナリオ、修正版）→ reject

- 経緯：初稿(「同一の明示手順なのに技能が違う」という枠組み)は、B-pole(暗黙知)を過剰に誘導するリスクがあると事前に指摘され、その枠組みを外した修正版に差し替えて実行
- 結果：修正版でControlのみ5体を走らせたところ、01Aで実際に機能していたのと形状は似ているはずなのに、今度はA-pole(角度・バリ・圧力・熱という測定可能パラメータ)へ収束
- 判定：**reject** — n=2の時点で「process/organizational系の場面は特定の極へ収束しやすいのではないか」という観察が浮上したが、過度な一般化は保留

## Original-X Baseline Audit → not executable

- 目的：01Aで実際に機能していたEncounter Xそのものをzero-primingで再走行し、Q/Q′/Q″の収束が場面設計固有の問題か、モデル側の baseline disposition かを切り分ける
- 実施内容：このセッション自身の transcript ログ(.jsonl)を直接調査
- 結果：Encounter X原文・History A/B原文・当時の指示文が、セッション圧縮境界を越えて回復不能であることが判明。外部記録(camp-us.net等)にも存在しないことをユーザー側でも確認済み
- 判定：**実行不能(not executable)** — negative result ではなく missing data

## なぜreconstructionしなかったか

記憶や要約から「それらしいEncounter X」を再構成することは技術的には可能だった。しかしそれを検証に使うと、以下のいずれかが起きる。

1. 再構成が偶然にも元と近ければ、結果は元の追試に見えるが、その近さ自体を検証する手段がない。
2. 再構成が元とズレていれば、結果は「再構成版という新しいEncounter」についてのものになり、01Aの追試という当初の問いには答えない。

どちらの場合も、出てくる結果は一見して確定的に見えるのに、実際には何を測ったのか判定不能になる。曖昧な「実行不能」を正直に記録する方が、偽の確定性を record に混ぜるより誠実だと判断し、再構成は行わなかった。

## 確定Ledger

`Identity is not transferred. Test only whether a difference survives the boundary.`（02F由来、中心guard）

`Cross-condition convergence ≠ Absence of history effect` — 全条件が同一出力に収束したことは、history effectの不在を証明しない。Encounterの診断的開放性の不足という別の説明が優先する。

`Baseline ≠ No History` — primingを与えなかったことは、履歴がないことを意味しない。

`Unprimed ≠ Unformed` — primingを受けていない状態と、何も形成されていない状態は別である。

`Fresh Agent ≠ History-Free Agent` — 新規に起こしたエージェントが履歴を持たない保証はない。学習過程そのものが一種のhistoryでありうる。

`Control ≠ Zero-Disposition` — Controlは「何も操作を加えなかった」ことを保証するが、「何も形成されていない」ことは保証しない。今回もっとも重く効いた項目。

`Compaction Boundary ≠ Content-Preserving Boundary` — セッション圧縮は会話の継続性を保つが、原文内容の保存は保証しない。

`Trace Survival ≠ Content Survival` — 実験の痕跡(要約・参照・この監査自体)が生き延びたことと、原文の内容が生き延びたことは別である。

`Summary Continuity ≠ Textual Continuity` — 要約による連続性と、原文による連続性は別の種類の連続性である。

`Compacted Summary ≠ Trace` — 圧縮要約は痕跡の代替物ではない。要約は圧縮者の選択を経た二次的産物である。

`Loss of Exact Content ≠ Proof of Continuity` — 内容の厳密な喪失を確認できたこと自体は、何かが連続していたことの証明にはならない。

## 最小生存記述

We observed convergence. We did not yet observe its source.

三つの独立したEncounter(Q, Q′, Q″)が、それぞれ異なる領域設計であったにもかかわらず、Controlのみで単一の極へ収束した。この収束が意味するのは、「診断的開放性を持つEncounterの設計は自明ではなく、01AのEncounter Xがなぜ機能していたのかは、現時点では再検証不可能である」ということだけである。モデルにbaseline dispositionがあるのか、三つとも設計が悪かっただけなのかは、現在のデータからは判定できない。

## Next probe: undesigned

02G-1以降のBoundary Testを再開する前に、baseline tendencyとhistory effectを事後的に切り分けようとするのではなく、最初から分離可能な形で測定できる設計が必要になる。

再定式化された問い：

`Does prior formation shift the distribution of subsequent uptake relative to an independently measured baseline?`

構想（未設計、記録のみ）：単一の完璧に均衡したEncounterを発明しようとするのではなく、(1)独立したfresh Control populationでunprimed応答分布を測定し、(2)別の独立したfresh populationへHistory A/Bをそれぞれ与えて応答分布を測定し、(3)Controlからの distribution shift としてhistory effectを見る。ControlがどちらかのPoleへ偏っていても、それ自体は設計の失敗にならない。

具体的なEncounter選定、サンプルサイズ、統計的な有意性の扱いは、まだ何も決めていない。02G-0の役割は、ここまで問いを削ることだった。

## Carry-over guard

`Distribution Shift ≠ Causal Attribution to History`

観測されたshiftが、History A/Bの内容そのものに起因するのか、単にpopulation間のサンプリングノイズなのか、あるいは「何らかの事前テキストを読まされたこと」自体の効果(content-free priming effect)なのかは、shiftの観測だけでは区別できない。次の設計では、A/B以外に「無内容だが同じ長さのダミー履歴」のような対照が、どこかで要求されることになる。この項目はまだ検証されていない──次段階の設計に持ち越す guard として、ここに登録するのみ。

## Raw log status（付記）

今回のQ/Q′/Q″/Original-Xの各pilotについて、個々のエージェントの逐語出力を別途保存したraw logは、この記録の時点で作成されていない。セッション圧縮の影響で、各Encounterの正確な原文・instruction文面も、今この場では完全な形では再現できない(Original-Xと同じ機構による喪失が、程度の差はあれ他のpilotにも及んでいる可能性がある)。

したがって「Ledger ≠ Raw Log」の原則と「No Probe without Trace」の実務は、今回のQ/Q′/Q″/Original-Xには遡及適用できない。次のProbe以降、Encounter原文・instruction・各agentへの入力・raw outputをセットで保存する運用を、実際に開始する。

👉 [CABA Probe Record Template](https://camp-us.net/articles/CABA-Probe-Record-Template.html)  

---

[CABA-01｜AIにハビトゥスはあるか？ ──社会理論の問いをAIで実験可能にしてみた記録](https://camp-us.net/articles/CABA-01_Habitus-AI-Probe.html)  
[CABA-01-note｜過去は終わる。過去の仕事は終わらない。 ──ハビトゥスをAIで実験してみた](https://camp-us.net/articles/CABA-01-note_Habitus-AI.html)  
[CABA-DN｜AI Habitus Probe — 2026-09-16](https://camp-us.net/articles/CABA-DN_AI-Habitus-Probe_2026-09-16.html)  
[CABA-02G-00｜Probe Calibration Ledger](https://camp-us.net/articles/CABA-02G-00_Probe-Calibration-Ledger.html)  
[CABA Probe Record Template](https://camp-us.net/articles/CABA-Probe-Record-Template.html)  

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
<p align="center">| Drafted Sep 16, 2026 · Web Sep 16, 2026 |</p>