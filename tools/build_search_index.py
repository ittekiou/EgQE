#!/usr/bin/env python3
"""EgQE内検索の索引づくり（GitHub Actions で Jekyll の前に実行する）

usage: python3 tools/build_search_index.py [DOCS_DIR]

DOCS_DIR（既定 docs）以下の .md を読み、本文を数個のファイルに分けて
DOCS_DIR/assets/search/ に書き出す。Jekyll はこれを静的ファイルとしてそのまま公開する。
索引はビルドのたびに作り直すので、リポジトリには入れない（.gitignore 済み）。
"""
import os, re, sys, json, datetime

DOCS = sys.argv[1] if len(sys.argv) > 1 else 'docs'
OUT = os.path.join(DOCS, 'assets', 'search')
SHARD_BYTES = 2_500_000
JST = datetime.timezone(datetime.timedelta(hours=9))
FM = re.compile(r'\A---\s*\n(.*?)\n---\s*\n', re.S)

pages = []
for root, dirs, files in os.walk(DOCS):
    # Jekyll と同じく、_ や . で始まるフォルダは公開されないので除く
    dirs[:] = sorted(d for d in dirs if not d.startswith(('_', '.')))
    for f in sorted(files):
        if not f.endswith('.md') or f.startswith(('_', '.')):
            continue
        path = os.path.join(root, f)
        text = open(path, encoding='utf-8', errors='replace').read()
        title = None
        m = FM.match(text)
        if m:
            fm = m.group(1)
            if re.search(r'^published:\s*false\s*$', fm, re.M):
                continue
            t = re.search(r'^title:\s*(.+?)\s*$', fm, re.M)
            if t:
                title = t.group(1).strip('\'"')
            text = text[m.end():]
        if not title:
            h = re.search(r'^#{1,2}\s+(.+?)\s*#*\s*$', text, re.M)
            title = h.group(1) if h else f[:-3]
        rel = os.path.relpath(path, DOCS).replace(os.sep, '/')
        url = '/' + rel[:-3] + '.html'
        pages.append([url, title, text.strip()])

os.makedirs(OUT, exist_ok=True)
shards, cur, size = [], [], 0
for p in pages:
    b = len(p[2].encode('utf-8'))
    if cur and size + b > SHARD_BYTES:
        shards.append(cur); cur, size = [], 0
    cur.append(p); size += b
if cur:
    shards.append(cur)

for i, rows in enumerate(shards):
    with open(os.path.join(OUT, f'egqe-{i}.js'), 'w', encoding='utf-8') as fh:
        fh.write(f'EGQE_SHARD({i},' + json.dumps(rows, ensure_ascii=False, separators=(',', ':')) + ');\n')
manifest = {
    'shards': len(shards),
    'pages': len(pages),
    'generated': datetime.datetime.now(JST).strftime('%Y-%m-%d %H:%M'),
}
with open(os.path.join(OUT, 'manifest.js'), 'w', encoding='utf-8') as fh:
    fh.write('EGQE_MANIFEST=' + json.dumps(manifest) + ';\n')
print(f'{len(pages)} pages -> {len(shards)} shards in {OUT}')
