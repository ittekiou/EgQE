OK、完璧なスタートです 👍  
**ここからは一切むずかしいことはしません。**  
私が「打つ文字」をそのまま真似してください。

---

# 🧭 Step 1｜作業用フォルダを作る

まず、**論文専用フォルダ**を作ります。  
今いる場所は `~`（ホームディレクトリ）なので、そのままでOK。

👇 **これをそのままコピーして Enter**

```bash
mkdir Z0_Golden_Bridge
```

成功すると、**何も表示されません**（それで正常）。

---

## 確認（任意）

```bash
ls
```

一覧に  
`Z0_Golden_Bridge`  
が見えたらOK。

---

# 🧭 Step 2｜作業フォルダに移動する

👇 **次にこれ**

```bash
cd Z0_Golden_Bridge
```

確認：

```bash
pwd
```

表示がこうなっていれば正解👇

```
/Users/takahashihajime/Z0_Golden_Bridge
```

---

# 🧭 Step 3｜paper.tex を作る（超重要）

いよいよ **LaTeX原稿を置く**ところです。

👇 **これを打って Enter**

```bash
nano paper.tex
```

すると、**黒い画面の編集画面**になります。

---

## ✍️ ここでやること

1. さきほど私が渡した  
    **LaTeX完成版全文**を  
    👉 **そのまま全部コピー**
    
2. nano画面に **ペースト**
    

（Macなら

- 右クリック → ペースト
    
- または ⌘V ）
    

---

## 💾 保存して出る方法（nanoの作法）

nanoはここが最初の山ですが、**順番通り押すだけ**。

1. **Ctrl + O**（保存）
    
2. Enter（ファイル名 paper.tex のまま）
    
3. **Ctrl + X**（終了）
    

👉 ターミナルに戻れば成功。

---

# 🧭 Step 4｜図ファイルを置く（次）

次は **Z0_Golden_Bridge.svg** をこのフォルダに入れます。

やり方は2通り：

### 方法A（いちばん簡単）

- Finderで  
    `Z0_Golden_Bridge.svg`
    
- それを  
    **Z0_Golden_Bridge フォルダにドラッグ**
    

### 方法B（もしDownloadsにあるなら）

```bash
mv ~/Downloads/Z0_Golden_Bridge.svg .
```

---

## 確認

```bash
ls
```

こうなっていればOK：

```
paper.tex
Z0_Golden_Bridge.svg
```

---

# 🧭 Step 5｜コンパイル（いよいよ！）

👇 **これを打つ**

```bash
pdflatex paper.tex
```

しばらく文字が流れますが、  
最後の方に👇が出れば成功：

```
Output written on paper.pdf (4 pages).
```

---

## 念のため2回目

```bash
pdflatex paper.tex
```

---

# 🧭 Step 6｜PDFを開いて確認

👇

```bash
open paper.pdf
```

### チェックポイント

-  **4ページ**
    
-  図がちゃんと出ている
    
-  文字化けなし
    

---

## 🚨 もしエラーが出たら

そのまま **エラーメッセージを全部コピペして貼ってください**。  
100%その場で直します。

---

## 🎯 今の地点まとめ

あなたはいま：

- ✅ ターミナル起動
    
- ⏭ フォルダ作成 → tex作成 → コンパイル直前
    

**完全に正しい道**にいます。

---

### 次の合図

👉 **Step 1 を実行したら、そのまま結果を貼ってください。**

```
mkdir Z0_Golden_Bridge
```

進みましょう。  
**ここから先は一本道です。**