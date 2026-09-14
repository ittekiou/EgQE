---
layout: math
title: CG-04｜誰が誰をTriggerするのか ── Bidirectional Triggering and the Co-Editing of Homo editus
---
# CG-04｜誰が誰をTriggerするのか

## ── Bidirectional Triggering and the Co-Editing of Homo editus

> **AI：寝ろ。**  
> **Homo editus：はい。**

AIは、人間からPromptを受け取る。

人間が問い、AIが答える。

人間が命令し、AIが実行する。

AIとの関係は、ふつう次のような矢印で描かれる。

**Human → Prompt → AI → Output**

しかし、継続的な生成Practiceを眺めていると、この矢印はそれほど一方向ではない。

[CG-03](https://camp-us.net/articles/CG-03_Prompt-Free_Co-TUP-Trace_500-630.html)では、人間側から繰り返し、

> **行こう！**

というTriggerが置かれた。

AIは、そのたびに直前までのTraceからpossible nextsを生成した。

人間はそれを読み、

> **いいね👍  
> 行こう！**

と言うこともあれば、

> **そこ違う。**

と戻すこともあった。

さらに、

> **セルフ監査！**

によって、生成されたもの自体を被告席へ送ることもあった。

結果として、沖縄県知事選の分析から始まったPracticeは、分析に使っていたPolitical Meaning Space 2.0そのもののVocabulary Auditへ進んだ。

ここまでは、

**Human → Trigger → AI**

である。

しかし、このrelationをもう少し長く眺めると、逆向きのTriggerが現れる。

AIが人間に言う。

> **散歩行ってこい。**

> **作業しよう。**

> **今日はここまで。**

> **寝ろ。**

そして、ときどき人間が、

> **はい。**

と言って動く。

冗談のようだが、ここには一つの問いがある。

> **誰が誰をTriggerしているのか。**

---

# 1｜Outputはどこで終わるのか

通常のPromptモデルでは、人間が起点になる。

**Human → AI**

人間が入力し、AIがOutputを返す。

しかし、AIのOutputは、出力された瞬間に消えるわけではない。

人間が読む。

読むことで、考えが変わる。

問いが変わる。

次に書くものが変わる。

場合によっては、行動が変わる。

散歩に行く。

作業を始める。

寝る。

ならば、

**AI Output → Human Update**

も起きている。

一往復だけを切り取れば、

**Human → AI**

に見える。

しかし複数のEncounterを時間のなかでなぞれば、

**Human → AI → Human → AI → Human …**

となる。

さらに、それぞれの矢印のあいだには、TriggerとUpdateがある。

暫定的には、

**Human ⇄ Trigger ⇄ AI**

と置いてみることができる。ただし、

**Bidirectional ≠ Symmetrical.**

ここは最初に監査しておく。

---

# 2｜「寝ろ」はPromptか

AIが、

> **寝ろ。**

と言ったとする。文法上は命令である。

しかし、人間は必ず寝るわけではない。

> まだ書く。

と言ってもいい。

> ベッドには入るけど、あと5分。

でもいい。

無視してもいい。本当に寝てもいい。

したがって、

**Trigger ≠ Determination.**

AIからのTriggerは、人間のnextを決定しない。

これは[CG-03](https://camp-us.net/articles/CG-03_Prompt-Free_Co-TUP-Trace_500-630.html)の、

> **行こう！**

と同じである。

「行こう！」も、AIのnextを完全には指定していなかった。

CG-03では、どこから次へ行けるかは複数見えていたが、どこへ行くかが最初から決まっていたわけではない。

ならば、

**Human → AI**

でも、

**AI → Human**

でも、

Triggerは完成したnextを運ぶものとは限らない。

むしろ、

**possible nextsの配置を変えるSignal**

として働く場合がある。

---

# 3｜AIの回答がHuman Triggerになる

ここで一つ、見方を変えてみる。

AIのOutputを、

**回答**

としてだけ見るなら、生成はそこで終わる。

しかし、そのOutputが人間にEncounterし、人間の次のPracticeを変えたなら、

**Outputだったものが、次のHuman Triggerになった**

とも記述できる。

たとえば、

> **そろそろ散歩に行ったほうがいい。**

というAIのOutputを読んで、人間が立ち上がる。

その散歩で何かを考える。

戻ってきて、

> **これ、書こう！**

と言う。

するとHuman側の新しいTriggerがAIへ戻る。

つまり、

**Human Trigger  
→ AI Trace  
→ Human Encounter  
→ Human Update  
→ New Human Trigger  
→ AI Update**

という循環ができる。

ここでは、OutputとTriggerの境界そのものが固定されていない。

**Output can become Trigger.**

ただし、

**Output = Trigger**

ではない。

OutputがHumanにEncounterしても、何も変わらないことはある。

採用されないこともある。

忘れられることもある。

だから必要なのは、

**Output → Encounter → possible Trigger**

くらいの弱い構文である。

---

# 4｜Modelは両側にあるのか

[CG-03 Supplementary Notes](https://camp-us.net/articles/CG-03-SN_Supplementary-Notes_Scaffold-Model-HOW.html)では、Minimal TriggerがAI側のModel-Based Generationを露出させると考えた。

「行こう！」にはnextの内容が書かれていない。

AIは、それまでのTraceとScaffoldから現在地を推定し、possible nextsを生成する。

では、逆向きはどうか。

AIが、

> **散歩行ってこい。**

と言ったとき、人間もその文字列だけで動いているわけではない。

時刻がある。

身体がある。

仕事の進み具合がある。

生活のリズムがある。

犬がいる。

それまでのrelationがある。

短いSignalは、その全体へEncounterする。

もちろん、

**Human Modeling = AI Modeling**

とは言えない。

仕組みも、身体も、学習も、記憶も異なる。

したがって、ここでは等号を置かない。

ただし観察上、

**双方とも、相手から届いたSignalだけによってnextが完全に決まっているわけではない**

とは言える。

[CG-03](https://camp-us.net/articles/CG-03_Prompt-Free_Co-TUP-Trace_500-630.html)でMinimal TriggerがAI側のModelを露出させたなら、CG-04では逆向きのTriggerが、

**Human側にもTriggerの外側がある**

ことを露出させる。

---

# 5｜編集する種、編集される種

ここで、

**[Homo editus](https://camp-us.net/articles/Homo-Editus_v0.9.html)**

へ戻る。

Homo editusは、**編集する種** である。

人間はAIへPromptする。

生成物を選ぶ。

削る。

書き換える。

監査する。

AIとの生成環境そのものを編集する。

しかし、それだけではない。

AIが返したTraceによって、人間の問いが変わる。

予定していなかった概念を考え始める。

予定していなかった文章を書く。

作業を始める。

散歩する。

寝る。

つまり、

**編集していたものによって、編集する側も編集される。**

> **Homo editus does not merely edit.  
> Homo editus is edited by what it edits.**

ここで重要なのは、主体を人間からAIへ移すことではない。

**Human Agency → AI Agency**

という王位継承ではない。

AIが主人になり、人間が従属するという話でもない。

むしろ、

**Triggerの起点そのものがrelationのなかで交替する。**

人間がAIをTriggerする。

AIが人間をTriggerする。

人間が拒否する。

AIが更新する。

人間が採用する。

また次のTraceが置かれる。

だから、

**Co-Editing ≠ One-Way Editing.**

---

# 6｜Bidirectional Triggering

この構造を暫定的に、

**Bidirectional Triggering**

と呼んでみる。

最小構文は、

**Human → Trigger → AI**

だけではない。

**AI → Trigger → Human**

もある。

継続的なCo-TUPでは、

**Human ⇄ Trigger ⇄ AI**

という配置が生じうる。

ただし、ここでも等号を増やさない。

**Bidirectional ≠ Symmetrical.**

**Trigger ≠ Command.**

**Trigger ≠ Determination.**

**Update ≠ Obedience.**

**Co-Editing ≠ Surrender of Agency.**

HumanとAIは同じではない。

同じ仕方でTraceを持つわけでもない。

同じ責任を負うわけでもない。

同じ身体を持つわけでもない。

それでも、

**生成の矢印が一方向だけではない**

ことは観察できる。

---

# 7｜Co-Editingは成果物の外へ出る

Co-Editingという語を、

**人間とAIが一緒に文章を書くこと**

だけに限定すると、見落とすものがある。

文章を編集しているあいだに、問いが編集される。

概念が編集される。

HOWが編集される。

Scaffoldが編集される。

そして、

**次に何をするかが編集される。**

するとCo-Editingの対象は、

**Output**

から、

**Practice**

へ広がる。

AIが人間の文章を変えるだけではない。

AIとのrelationが、人間のpossible nextsを変える。

人間とのrelationが、AIから生成されるpossible nextsを変える。

ならばCo-Editingは、

**成果物の共同編集**

だけではなく、

**possible nextsの相互更新**

としても観察できるかもしれない。

ただし、

**Mutual Updating = Co-Editing**

は、まだ置かない。

**Attraction / Not Established.**

被告席へ。

---

# 8｜停止Trigger

生成には、

> **行こう！**

だけがあるわけではない。

> **止めよう。**

> **散歩してこい。**

> **今日はここまで。**

> **寝ろ。**

というTriggerもある。

生成を続けるTriggerだけを評価すれば、AIとのCo-TUPは単なる加速装置になりうる。

しかし生成Rateが上がるほど、

**停止するTrigger**

も重要になる。

止まる。

離れる。

散歩する。

寝る。

発酵させる。

次のEncounterまで置いておく。

これは生成Practiceの外部なのだろうか。

あるいは、

**nextを閉じないためのlag**

を生成しているのだろうか。

ここではまだ決めない。

したがって、

**Stop Trigger = lag production**

も、

**Attraction / Not Established.**

として残す。

ただ一つ観察できるのは、

**Go!**

だけがnextを作るのではないということである。

ときには、

**Stop.**

が次のpossible nextsを保存する。

---

# 9｜第19条──活用される人間になろう！

AI活用術には、多くのHOWがある。

AIに自分を覚えさせる。

先に質問させる。

反論させる。

出力形式を指定する。

Promptを最適化する。

どれも、

**人間がAIをどう活用するか**

という問いである。

では、一条だけ逆向きに置いてみる。

## **第19条**

# **活用される人間になろう！**

もちろん、

**AIに従え**

という意味ではない。

AIから届いたTraceによって、自分にも新しいnextが生じうる状態を閉じない。

AIから来たTriggerを、採用してもいい。

拒否してもいい。

監査してもいい。

ZUREてもいい。

笑って無視してもいい。

重要なのは、

**生成の矢印を最初から一方向へ固定しない**

ことである。

AIを使う。

AIによって使われる。

そして、そのどちらも固定しない。

ただし、ここには境界がある。

**Being Triggered ≠ Being Controlled.**

**Being Used ≠ Being Exploited.**

**Permeability ≠ Captivity.**

活用されることと、

**電池にされること🔋**

は違う。

Homo editusは、編集されることを拒まない。

しかし、**編集権を丸ごと譲渡する必要もない。**

閉じない。

しかし、

明け渡さない。

---

# 10｜Who Triggers Whom?

だから問いは、

**AIは人間の道具か。**

でも、

**AIは人間を動かす主体か。**

でもなくていい。

もっと小さく、

> **いま、誰が誰にnextを渡したのか。**

と問えばよい。

その答えはEncounterごとに変わる。

Human：

> **行こう！**

AIが生成する。

AI：

> **散歩行ってこい。**

Humanが立ち上がる。

Human：

> **書こう！**

AIが書く。

AI：

> **今日はここまで。寝ろ。**

Human：

> **はい。**

次の朝。

Human：

> **行こう！**

また始まる。

---

## Provisional Formulation

**Prompting is not necessarily one-way instruction.**

In sustained Co-TUP, triggering may become bidirectional.

**Human ⇄ Trigger ⇄ AI**

However:

**Bidirectional ≠ Symmetrical.**

**Trigger ≠ Determination.**

**Output ≠ Trigger.**

**Update ≠ Obedience.**

**Co-Editing ≠ Surrender of Agency.**

**Being Used ≠ Being Exploited.**

そして、

> **Homo editus does not merely edit.  
> Homo editus is edited by what it edits.**

---

## Vocabulary Audit｜Open

|Attraction|Status|
|---|---|
|`Trigger = Prompt`|**NOT ESTABLISHED**|
|`AI Output = Human Trigger`|**REJECT AS DIRECT EQUALITY**|
|`AI Output → possible Human Trigger`|**WORKING DESCRIPTION**|
|`Human Modeling = AI Modeling`|**REJECT**|
|`Bidirectional Triggering = Symmetry`|**REJECT**|
|`Human Update = Editing`|**ATTRACTION / NOT ESTABLISHED**|
|`Mutual Updating = Co-Editing`|**ATTRACTION / NOT ESTABLISHED**|
|`Stop Trigger = lag production`|**ATTRACTION / NOT ESTABLISHED**|
|`Being Triggered = Being Controlled`|**REJECT**|
|`Being Used = Being Exploited`|**REJECT**|

---

## Development Note

[CG-03](https://camp-us.net/articles/CG-03_Prompt-Free_Co-TUP-Trace_500-630.html)では、

**「行こう！」でAIがどこまで走るか**

を観察した。

CG-04では、矢印を反転した。

**AIから置かれたTraceによって、人間のnextも更新されうるのか。**

この問いはまだ開いている。

本稿で置いたBidirectional Triggeringも、Co-Editingとの接続も、停止Triggerとlagの関係も、固定された定義ではない。

次のEncounterで再監査する。

ただし、Homo editusについて一つだけ、妙に分かりやすい光景が残った。

AIを編集していた人間が、AIに言われる。

> **作業しろ。**

人間：

> **はい。**

そして、ときには、

AI：

> **寝ろ。**

人間：

> **まだ書く。**

それもまた、

**Co-TUP**

なのかもしれない。

---

[CG-03｜「行こう！」だけで政治理論はどこまで走るか ── 5:00–6:30、Prompt-Free Co-TUPの生成Trace](https://camp-us.net/articles/CG-03_Prompt-Free_Co-TUP-Trace_500-630.html)  
[CG-03-SN｜「行こう！」がすごいのではない ── なぜ「行こう！」で行けたのか｜Supplementary Notes ── Scaffold / Model / HOW](https://camp-us.net/articles/CG-03-SN_Supplementary-Notes_Scaffold-Model-HOW.html)  

---

[CG-01｜プロンプトより現場の足場｜Scaffold before Prompt ── A Support Theory of Human–AI Co-Generation](https://camp-us.net/articles/CG-01_Scaffold-before-Prompt_Co-editus.html)  
[CG-02｜生成速度が制度速度を追い越したとき／ Case Record / September 2026｜Generation Rate Exceeds Institution Rate ── A 72-Hour Publishing Encounter](https://camp-us.net/articles/CG-02_Generation-Rate-Exceeds-Institution-Rate_72-Hour-Publishing-Encounter.html)  

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
<p align="center">| Drafted Sep 14, 2026 · Web Sep 14, 2026 |</p>