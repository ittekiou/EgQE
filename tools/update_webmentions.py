#!/usr/bin/env python3
"""camp-us.net に届いた Webmention を webmention.io から仕入れて、箱の JSON に足していく。

使い方: python3 tools/update_webmentions.py docs/rack/webmentions.json [docs/rack/webmentions-hide.txt]
- 鍵は環境変数 WEBMENTION_IO_TOKEN（GitHub の Secrets に入れる）。なければ何もしない。
- 前の記録は消さない（痕跡は残す）。wm-id ごとに足すか、新しい内容で上書きする。
- hide ファイルに書いた送り元の URL（1行に1つ）は、記録は残したまま hidden: true にする（表示から外す）。
- 中身が変わったときだけ書き出す（変わらなければ、コミットも出ない）。
Only the standard library is used.
"""
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone

DOMAIN = os.environ.get("WEBMENTION_DOMAIN", "camp-us.net")
API = "https://webmention.io/api/mentions.jf2"
PER_PAGE, MAX_PAGES = 100, 50
KEEP = ("wm-id", "wm-property", "wm-source", "wm-target", "wm-received", "url", "name", "published")


def fetch_all(token):
    out = []
    for page in range(MAX_PAGES):
        q = urllib.parse.urlencode({"domain": DOMAIN, "token": token, "per-page": PER_PAGE, "page": page})
        req = urllib.request.Request(f"{API}?{q}", headers={"User-Agent": "camp-us.net webmention keeper"})
        with urllib.request.urlopen(req, timeout=30) as r:
            children = json.load(r).get("children") or []
        out.extend(children)
        if len(children) < PER_PAGE:
            break
    return out


def slim(m):
    """表示に要るものだけを残す（本文や顔写真は持たない）。"""
    s = {k: m[k] for k in KEEP if m.get(k) not in (None, "")}
    a = m.get("author") or {}
    if a.get("name") or a.get("url"):
        s["author"] = {k: a[k] for k in ("name", "url") if a.get(k)}
    return s


def main():
    path = sys.argv[1]
    hide_path = sys.argv[2] if len(sys.argv) > 2 else None
    token = os.environ.get("WEBMENTION_IO_TOKEN", "")
    if not token:
        print("WEBMENTION_IO_TOKEN がないので、何もしない")
        return 0
    try:
        old = json.load(open(path, encoding="utf-8"))
    except (OSError, ValueError):
        old = {"domain": DOMAIN, "items": []}
    hide = set()
    if hide_path and os.path.exists(hide_path):
        hide = {l.strip() for l in open(hide_path, encoding="utf-8") if l.strip() and not l.startswith("#")}

    items = {str(m.get("wm-id")): dict(m) for m in old.get("items", []) if m.get("wm-id") is not None}
    fetched = fetch_all(token)
    for m in fetched:
        if m.get("wm-id") is None:
            continue
        items[str(m["wm-id"])] = slim(m)
    for m in items.values():
        if m.get("wm-source") in hide or m.get("url") in hide:
            m["hidden"] = True
        else:
            m.pop("hidden", None)

    new_items = sorted(items.values(), key=lambda m: m.get("wm-received", ""), reverse=True)
    if new_items == old.get("items"):
        print(f"変わりなし（{len(new_items)}件、今回の仕入れ {len(fetched)}件）")
        return 0
    out = {"domain": DOMAIN, "updated": datetime.now(timezone.utc).isoformat(timespec="seconds"), "items": new_items}
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"{len(new_items)}件を記録（今回の仕入れ {len(fetched)}件）-> {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
