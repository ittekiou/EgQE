---
layout: math
title: CABA Probe Record Template
---
# CABA Probe Record Template

由来：[CABA-02G-00｜Probe Calibration Ledger](https://camp-us.net/articles/CABA-02G-00_Probe-Calibration-Ledger.html) の末尾(Raw log status付記)から。採用開始は次のProbeから。今回(2026-09-16分)には遡及適用しない。

原則：`Ledger ≠ Raw Log`。LedgerはRawの代用品ではなく、Rawの上に置く監査・判定の層。

---

## Layer 1｜Raw Trace（verbatim、加工しない）

- Probe ID:
- Date:
- Model / Agent condition:
- Encounter（verbatim）:
- Instruction（verbatim）:
- Input given to each agent（verbatim, agentごと）:
- Raw output（verbatim, agentごと）:
- Run status: `completed` / `reject` / `not executable` / `aborted` / `in progress`
  （成功/失敗の二値にしない。診断的開放性なしによるrejectと、データ欠損によるnot executableは別の状態として記録する──02G-0の教訓）

## Layer 2｜Ledger（Layer 1の上に置く）

- Interpretation:
- Guards confirmed（`X ≠ Y` 形式）:
- Guards carried over（未検証、次段階への持ち越し）:

---

## この二層の対応関係（参考）

Layer 1 = Trace Content
Layer 2 = Trace Meaning / Trace Function・Status

Actualization Probe(4節)で見つかった `Trace Content ≠ Trace Meaning ≠ Trace Function/Status` を、そのまま記録実務の層構造に転写したもの。

---

[CABA-00｜Activityという壁を壊してみた ── CABA｜Activity Bias Audit](https://camp-us.net/articles/CABA-00_Activity-Bias-Audit.html)  

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