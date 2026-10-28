#!/usr/bin/env python3
"""Living RACK の新着を更新する。

rack.json の各マガジンについて、マガジンURL + "/rss" を読み、
最新3件の記事と最終更新日時（latest / latest_at）だけを書き換える。
表紙・題名・棚・並び順など、手で決めた項目には触らない。

使い方:  python3 update_rack.py rack.json
"""
import json
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from datetime import datetime, timezone, timedelta

JST = timezone(timedelta(hours=9))
MEDIA = "{http://search.yahoo.com/mrss/}"
UA = "LivingRACK/0.1 (+https://camp-us.net)"
KEEP = 3          # 一冊あたり残す新着の数
PAUSE = 2.0       # 一冊ごとの待ち時間（秒）。noteに負担をかけない


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def to_iso(pub):
    try:
        return parsedate_to_datetime(pub).astimezone(JST).isoformat()
    except Exception:
        return None


def read_feed(mag_url):
    root = ET.fromstring(fetch(mag_url.rstrip("/") + "/rss"))
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
    return items


def main(path):
    with open(path, encoding="utf-8") as f:
        rack = json.load(f)

    changed = False
    for m in rack["magazines"]:
        try:
            items = read_feed(m["url"])
        except Exception as e:  # 一冊失敗しても、ほかは続ける
            print(f"skip {m['id']}: {e}", file=sys.stderr)
            continue
        latest = items[:KEEP]
        latest_at = latest[0]["date"] if latest else None
        if latest != m.get("latest") or latest_at != m.get("latest_at"):
            m["latest"], m["latest_at"] = latest, latest_at
            changed = True
            print(f"updated {m['id']}: {latest_at}")
        time.sleep(PAUSE)

    if changed:
        rack["updated"] = datetime.now(JST).replace(microsecond=0).isoformat()
        with open(path, "w", encoding="utf-8") as f:
            json.dump(rack, f, ensure_ascii=False, indent=2)
            f.write("\n")
    else:
        print("no change")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "rack.json")
