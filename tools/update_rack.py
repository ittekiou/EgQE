#!/usr/bin/env python3
"""Living RACK の新着を更新する。

rack.json の各マガジンについて、マガジンURL + "/rss" を読み、
最新3件の記事と最終更新日時（latest / latest_at）を書き込む。

手で書いた項目（title / description / cover / shelf / order）はそのまま使う。
空になっている項目だけ、ここで埋める：
  - title, description … RSS のマガジン名と説明から
  - cover              … マガジンのページの og:image から
RSS が読めないマガジン（非公開など）は hidden にして、ページに出さない。

使い方:  python3 update_rack.py rack.json
"""
import html
import json
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from datetime import datetime, timezone, timedelta

JST = timezone(timedelta(hours=9))
MEDIA = "{http://search.yahoo.com/mrss/}"
UA = "LivingRACK/0.2 (+https://camp-us.net/rack/)"
KEEP = 5          # 一冊あたり残す新着の数（ページでは入荷中だけ5件、ほかは3件）
PAUSE = 1.0       # 一回ごとの待ち時間（秒）。noteに負担をかけない
DESC_MAX = 80     # 説明文を自動で入れるときの最大文字数


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def to_iso(pub):
    try:
        return parsedate_to_datetime(pub).astimezone(JST).isoformat()
    except Exception:
        return None


def first_sentence(text):
    text = re.sub(r"<[^>]+>", " ", html.unescape(text or ""))
    text = re.sub(r"\s+", " ", text).strip()
    m = re.search(r"^(.+?[。！？!?])", text)
    s = m.group(1) if m else text
    return s if len(s) <= DESC_MAX else s[:DESC_MAX - 1] + "…"


def read_feed(mag_url):
    root = ET.fromstring(fetch(mag_url.rstrip("/") + "/rss"))
    ch = root.find("channel")
    info = {
        "title": (ch.findtext("title") or "").strip() if ch is not None else "",
        "description": first_sentence(ch.findtext("description")) if ch is not None else "",
    }
    items = []
    for it in root.iter("item"):
        thumb = it.find(f"{MEDIA}thumbnail")
        items.append({
            "title": (it.findtext("title") or "").strip(),
            "url": (it.findtext("link") or "").strip(),
            "date": to_iso(it.findtext("pubDate") or ""),
            "thumb": (thumb.text or "").strip() if thumb is not None and thumb.text else "",
        })
    items = [i for i in items if i["url"]]
    items.sort(key=lambda i: i["date"] or "", reverse=True)
    return info, items


def read_cover(mag_url):
    page = fetch(mag_url).decode("utf-8", "replace")
    m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)', page) \
        or re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image', page)
    return html.unescape(m.group(1)) if m else ""


def main(path):
    with open(path, encoding="utf-8") as f:
        rack = json.load(f)

    for m in rack["magazines"]:
        m.setdefault("url", f"https://note.com/takahashihajime/m/{m['id']}")
        try:
            info, items = read_feed(m["url"])
        except urllib.error.HTTPError as e:
            if e.code in (403, 404):        # 非公開・削除など
                m["hidden"] = True
            print(f"skip {m['id']}: {e}", file=sys.stderr)
            time.sleep(PAUSE)
            continue
        except Exception as e:              # 一冊失敗しても、ほかは続ける
            print(f"skip {m['id']}: {e}", file=sys.stderr)
            time.sleep(PAUSE)
            continue
        m.pop("hidden", None)
        if not m.get("title"):
            m["title"] = info["title"]
        if not m.get("description"):
            m["description"] = info["description"]
        m["latest"] = items[:KEEP]
        m["latest_at"] = items[0]["date"] if items else None
        time.sleep(PAUSE)

        if not m.get("cover"):
            try:
                m["cover"] = read_cover(m["url"])
            except Exception as e:
                print(f"no cover {m['id']}: {e}", file=sys.stderr)
            time.sleep(PAUSE)
        print(f"ok {m['id']}: {m['title'][:30]}")

    rack["updated"] = datetime.now(JST).replace(microsecond=0).isoformat()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rack, f, ensure_ascii=False, indent=2)
        f.write("\n")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "rack.json")
