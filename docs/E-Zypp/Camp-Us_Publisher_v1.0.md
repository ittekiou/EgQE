# Camp-Us Publisher 制作プレイブック v1.0
## note連載 → EPUB → KDPペーパーバック、フル工程まとめ

第一号『Homo editus』制作で確立した工程。次回作からはこの手順をなぞればいい。

---

## 0｜前提：マスター原稿の作法

- 章＝`#`（h1）、節＝`##`（h2）、小見出し＝`###`（h3）を厳密に守る。**`#`は必ず改ページ扱いになる**ので、節を`#`にすると意図しない大量改ページが起きる（今回VI・VII・補論で実際に発生したバグ）。着手前に必ず全見出しレベルを監査する：

```bash
grep -n "^# \|^## \|^### " master.md
```

- LaTeX記法（`\boxed{}`、`\rightarrow`、下付き文字など）は、EPUB/PDFどちらでもレンダリング崩れの元。**執筆時点でUnicode矢印（→ ↓ ↕ ≠ ⇌）か、それも怪しければASCII（`-->`、`<->`）に寄せておく**。今回、⇌が一部リーダーで文字化けした実例あり。迷ったらASCII優先。
- 図解・対応表を空白文字の位置合わせで表現しない。**リフロー環境（EPUB／紙どちらも）では空白の量が保証されない**。縦積みの箇条書きに変える。

---

## 1｜EPUB制作

### 1-1. 変換
```bash
pandoc master.md -o book.epub \
  --toc --toc-depth=2 \
  --metadata lang=ja \
  --epub-title-page=false \
  --resource-path=.:images
```

### 1-2. 必須チェックリスト
- [ ] LaTeX残骸なし：`grep -l '\\\\' EPUB/text/*.xhtml`（展開後）
- [ ] 全角スペースでの位置調整が残っていないか
- [ ] 章の見出しレベルが全章で統一されているか（太字指定の有無も含め、目次の表示崩れに直結する）
- [ ] 画像はPNGでなくJPEG圧縮（quality 85前後）でファイルサイズを落とす。写真調の絵はPNGだと不必要に重い
- [ ] 改ページを狙って入れたい箇所は`<div style="page-break-before: always;"></div>`のraw HTMLで明示

### 1-3. 検証
Kindle Previewer 3で必ず実機（タブレット/スマホ表示）を目視。特に：
- 記号のフォント代替（〼のような意図しないグリフ置換）
- 目次の太字が全章で揃っているか
- 図解のインデントが端末で崩れていないか

---

## 2｜KDPペーパーバック制作（PDF）

### 2-1. 環境
```bash
pip install weasyprint --break-system-packages
apt-get install -y ghostscript
```
WeasyPrintでCSS Paged Mediaを使い、127×188mmのような小型判型・左右ミラー余白・ノンブルを精密に組む。日本語はNoto Serif CJK JPが標準搭載されていることを確認しておく。

### 2-2. 既知の制約と回避策
**WeasyPrintは文書途中でのページカウンター（`page`）リセットに対応していない。** `counter-reset: page 1`をどの要素に置いても効かない（実験で3パターン確認済み）。

回避策：**前付け／本文／奥付を別々のHTMLとして独立レンダリングし、`pypdf`で結合する。** 独立文書はそれぞれ自分のページ1から始まるので、リセット不要で正しいノンブルになる。

```python
from pypdf import PdfWriter, PdfReader
writer = PdfWriter()
for fname in ['front.pdf', 'toc.pdf', 'blank.pdf', 'main.pdf', 'colophon.pdf']:
    reader = PdfReader(fname)
    for page in reader.pages:
        writer.add_page(page)
writer.metadata = {}  # KDPはメタデータ持ち込み禁止
with open('final.pdf', 'wb') as f:
    writer.write(f)
```

### 2-3. 綴じ側ミラー余白（`@page :left` / `:right`）
```css
@page :right {
  margin-left: 16mm;   /* 外側 */
  margin-right: 20mm;  /* 綴じ側 */
  @bottom-right { content: counter(page); }
}
@page :left {
  margin-left: 20mm;
  margin-right: 16mm;
  @bottom-left { content: counter(page); }
}
```
**前付けページ数を偶数にしておくこと。** 本文の1ページ目が右ページ（recto）から始まるようにするため。奇数だと本文の綴じ位置が丸ごとズレる。

### 2-4. 目次（実ページ番号入り）
本文PDFを先に確定させ、`pdfplumber`で各章見出しが何ページ目にあるかを自動抽出してから目次を組む。
```python
import pdfplumber
with pdfplumber.open('main.pdf') as pdf:
    for i, page in enumerate(pdf.pages, start=1):
        text = page.extract_text() or ""
        # 章タイトルとのマッチングでページ番号を取得
```

### 2-5. KDP入稿仕様｜必須監査（公式ヘルプ「原稿ファイルの保存」準拠）

- [ ] 日本語原稿はPDFのみアップロード可
- [ ] PDF/X-1a推奨。ただし非対応でも審査時にAmazon側で除去処理される想定で、無理に追い込みすぎない（WeasyPrint＋Ghostscriptでの完全なPDF/X-1a準拠は今回未達成、標準RGB版を本命とした）
- [ ] 単ページPDF（見開き書き出し禁止）
- [ ] 全フォント埋め込み（`pdffonts file.pdf`で`emb: yes`確認。サブセット埋め込みは許容範囲）
- [ ] 画像300 DPI以上、ダウンサンプリング無効
- [ ] トンボ・トリムマーク・ブックマーク・コメント・非表示オブジェクト・注釈・プレースホルダー・**メタデータ**を含めない
- [ ] ファイルをロック・暗号化しない
- [ ] 線幅0.75pt/0.3mm以上
- [ ] 本文最低7pt（可読性優先で実際はもっと大きく——今回10pt採用）
- [ ] ページサイズ＝仕上がり判型と完全一致（裁ち落としなしの場合）
- [ ] **ページ番号の左右は横書きLTRなら奇数＝右／偶数＝左。ただし縦書きRTLの日本語原稿では逆転する**ので、本の組版方向を必ず確認してから左右ミラー設計をすること
- [ ] 冒頭・中間の連続白紙は5ページ未満、末尾は11ページ未満
- [ ] 総ページ数は偶数に（奇数ならKDPが自動調整するが、自分で末尾に白紙を足して制御したほうが安全）
- [ ] 新規ファイルとして都度生成する。**既存PDFの上書き保存を繰り返さない**（Amazon公式が明示的に警告している）

---

## 3｜表紙制作

### 3-1. テンプレートから正確な座標を読み取る
KDPが提供するテンプレートPNGを画素解析して、mm単位の正確な境界を得る。
```python
from PIL import Image
import numpy as np
img = Image.open('template.png').convert('RGB')
arr = np.array(img)
px_per_mm = arr.shape[1] / 全体幅mm
# 黄色（バーコード領域）、黒（トリムライン）のピクセル座標を抽出
```

今回の実測値（127×188mm、208ページ、砕木パルプ紙の場合）：
- 全体：272.77mm × 194.35mm（裁ち落とし込み）
- 表1／表4：各127mm、背：12.42mm
- 裁ち落とし：外周3.175mm
- バーコード欄：幅50.8mm×高さ30.5mm、表4の綴じ寄り下部

**ページ数が変われば背幅もバーコード位置も変わる。毎回テンプレートを取り直して実測すること。**

### 3-2. 構成の基本
- 表1：既存のアートワークをフルブリードで配置（裁ち落とし込みの領域全体を覆う）
- 背：縦組みで書名＋著者名。`transform: rotate(-90deg)`。**KDP最低基準は左右各1.6mm、79ページ以上必要**
- 表4：紹介文＋著者情報。バーコード欄は完全に無地のまま空けておく（KDPが自動生成）
- 全体をCMYKに変換：
```bash
gs -dBATCH -dNOPAUSE -dNOOUTERSAVE \
   -sColorConversionStrategy=CMYK \
   -sProcessColorModel=DeviceCMYK \
   -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 \
   -dPDFSETTINGS=/prepress \
   -sOutputFile=cover_cmyk.pdf cover.pdf
```

---

## 4｜最終監査（提出直前）

1. KDP印刷プレビューアーで全ページ目視——特に扉・目次・章の切れ目・巻末・表紙見開き
2. 総ページ数、目次のページ番号と実際のページが一致しているか
3. 表紙のガイド線が完全に消えているか（ガイドレイヤーごと非表示・削除）
4. 著者名・タイトル・ISBNが、本の詳細情報（KDP管理画面）とPDF内（表紙・扉・奥付）で完全一致しているか

---

## 5｜このプレイブックの前提となった技術スタック

- `pandoc` — Markdown → EPUB/HTML変換
- `weasyprint` — CSS Paged Media対応のHTML→PDF（判型・余白・ノンブル制御）
- `ghostscript` — CMYK変換、PDF/X-1a試行
- `pypdf` — PDF結合・メタデータ除去
- `pdfplumber` — 本文PDFからの章ページ番号自動抽出
- `PIL/numpy` — テンプレート画像のピクセル解析

すべてこの環境（bash_tool）で完結する。次回作は、この手順書の番号順になぞれば、初稿から入稿までの距離がかなり縮む。
