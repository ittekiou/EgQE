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
    if url.startswith("file:"):                     # 爺さんが手で貼ったRSS（リポジトリの中のファイル）
        with open(url[5:], "rb") as f:
            data = f.read()
        # ブラウザから写すと先頭に「This XML file does not appear…」の一行が付くので、最初の < より前は捨てる
        return data[data.find(b"<"):].strip()
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/rss+xml, application/xml;q=0.9, text/html;q=0.8, */*;q=0.5"})
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


ROW_KEEP = 12     # 新刊・図書だより・声・映像の段に並べる数
ITUNES = "{http://www.itunes.com/dtds/podcast-1.0.dtd}"
ATOM = "{http://www.w3.org/2005/Atom}"
YT = "{http://www.youtube.com/xml/schemas/2015}"


def any_date(s):
    """RSS（RFC 822）でも Atom（ISO 8601）でも、日本時間のISOにする。"""
    s = (s or "").strip()
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(JST).isoformat()
    except ValueError:
        return to_iso(s)


def feed_url_of(row):
    """feed が "env:名前" なら、GitHub の Secrets から渡された環境変数を使う。
    （鍵の入ったURLを、公開の台帳に書かないため）"""
    f = row.get("feed") or ""
    if f.startswith("env:"):
        import os
        return os.environ.get(f[4:], "")
    return f


def item_image(it, fallback=""):
    enc = it.find("enclosure")
    if enc is not None and enc.get("url") and enc.get("type", "").startswith("image"):
        return enc.get("url")
    for th in it.iter(f"{MEDIA}thumbnail"):          # note / YouTube（media:group の中）
        u = th.get("url") or (th.text or "").strip()
        if u:
            return u
    im = it.find(f"{ITUNES}image")                  # ポッドキャスト
    if im is not None and im.get("href"):
        return im.get("href")
    CONTENT = "{http://purl.org/rss/1.0/modules/content/}encoded"
    for body in (it.findtext("description"), it.findtext(CONTENT)):   # Medium は本文（content:encoded）の中
        m = re.search(r'<img[^>]+src=["\']([^"\']+)', html.unescape(body or ""))
        if m:
            return html.unescape(m.group(1))
    return fallback


def read_row(feed_url, sort=True):
    """RSS（Are.na・Substack・LISTEN・stand.fm）でも Atom（YouTube）でも、「段」の中身を読む。
    Are.na の <source url>（Amazon の商品ページ）があれば、そちらをリンクにする。"""
    root = ET.fromstring(fetch(feed_url))
    out = []
    if root.tag == f"{ATOM}feed":                   # YouTube など
        for e in root.iter(f"{ATOM}entry"):
            link = ""
            for l in e.findall(f"{ATOM}link"):
                if l.get("rel", "alternate") == "alternate":
                    link = l.get("href", "")
            out.append({
                "title": (e.findtext(f"{ATOM}title") or "").strip(),
                "url": link,
                "image": item_image(e),
                "date": any_date(e.findtext(f"{ATOM}published") or e.findtext(f"{ATOM}updated")),
            })
    else:
        ch = root.find("channel")
        ch_img = ""
        if ch is not None:
            ci = ch.find(f"{ITUNES}image")
            ch_img = (ci.get("href") if ci is not None else "") or (ch.findtext("image/url") or "")
        for it in root.iter("item"):
            src = it.find("source")
            link = src.get("url") if src is not None and src.get("url") else (it.findtext("link") or "").strip()
            out.append({
                "title": (it.findtext("title") or "").strip(),
                "url": link,
                "image": item_image(it, ch_img),
                "date": any_date(it.findtext("pubDate")),
            })
    out = [x for x in out if x["title"]]
    if sort:
        out.sort(key=lambda x: x["date"] or "", reverse=True)
    return out[:ROW_KEEP]


SITE = "https://camp-us.net"


def read_whatsnew(path, keep=10):
    """camp-us.net の WhatsNew.md から、日付の見出し（###### 2026/10/26）の下にあるリンクを新しい順に拾う。
    見出しより上（目次・常設リンク）は読まない。"""
    out, date = [], None
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = re.match(r"^#{2,6}\s*(\d{4})/(\d{1,2})/(\d{1,2})\s*$", line)
            if m:
                y, mo, d = map(int, m.groups())
                date = datetime(y, mo, d, tzinfo=JST).isoformat()
                continue
            if not date:
                continue
            for t, u in re.findall(r"\[([^\]]+)\]\(([^)\s]+)\)", line):
                if u.startswith("/"):
                    u = SITE + u
                if u.endswith(".md"):
                    u = u[:-3] + ".html"
                out.append({"title": t.strip(), "url": u, "image": "", "date": date})
                if len(out) >= keep:
                    return out
    return out


def fill_group(grp, rid, sort=True):
    """feed が一本なら "feed"、いくつも混ぜるなら "feeds": [...]。
    一本でも取れたら items を入れ替え、全部だめなら前の中身のまま。"""
    # feeds の一つが ["A", "B"] のような並びなら、A がだめなときだけ B を試す（予備の住所）
    feeds = grp.get("feeds") or [grp.get("feed")]
    feeds = [f for f in feeds if f]
    if not feeds:
        return
    got, ok = [], 0
    for f in feeds:
        for url in [feed_url_of({"feed": x}) for x in (f if isinstance(f, list) else [f])]:
            if not url:
                continue
            try:
                got += read_row(url, sort)
                ok += 1
                print(f"ok row {rid}: {url[:60]}")
                time.sleep(PAUSE)
                break
            except Exception as e:
                print(f"skip row {rid}: {url[:60]}: {e}", file=sys.stderr)
                time.sleep(PAUSE)
    if ok:
        if len(feeds) > 1:
            got.sort(key=lambda x: x["date"] or "", reverse=True)
        grp["items"] = got[:grp.get("keep", ROW_KEEP)]


FEED_KEEP = 20    # 一本のRSSに載せる数（リーダー側は前の分を覚えているので、少なめでよい）
PAGE = SITE + "/rack/"
PR_NOTE = "新刊の項目にはAmazonアソシエイトリンクを含みます（PR）。"


def collect_entries(rack):
    """棚の中身を、RSSの一項目ずつに並べる。どの段・どの棚のものかの札を付けておく。
    雑誌は冊ごとではなく記事ごと（同じ日に同じ冊へ何本入っても取りこぼさない）。"""
    out = []

    def add(it, cat, tags, pr=False):
        if it.get("title") and it.get("url"):
            out.append({"date": it.get("date") or "", "title": it["title"], "url": it["url"],
                        "image": it.get("image") or it.get("thumb") or "",
                        "cat": cat, "tags": tags, "pr": pr})

    for row in rack.get("rows", []):
        name, rid = row.get("name", ""), row.get("id", "")
        pr = row.get("kind") == "book"              # 新刊の段はAmazonアソシエイトリンク
        for grp in (row.get("groups") or [row]):
            cat = name + ("｜" + grp["label"] if grp.get("label") and grp is not row else "")
            for it in grp.get("items", []):
                add(it, cat, {"row:" + rid}, pr)
    for m in rack.get("magazines", []):
        if m.get("hidden"):
            continue
        tags = {"row:magazines", "shelf:" + (m.get("shelf") or "")}
        for it in m.get("latest", []):
            add(it, "📬 雑誌｜" + (m.get("title") or ""), tags)
    return out


def write_feed(entries, out, title, desc, page=PAGE):
    """entries を新しい順に FEED_KEEP 件、RSS 2.0 で書き出す。同じURLは一つにまとめる。"""
    from xml.sax.saxutils import escape as esc
    from email.utils import format_datetime
    seen, items = set(), []
    for e in sorted(entries, key=lambda e: e["date"], reverse=True):
        if e["url"] not in seen:
            seen.add(e["url"])
            items.append(e)
    items = items[:FEED_KEEP]

    def rfc(d):
        try:
            return format_datetime(datetime.fromisoformat(d))
        except Exception:
            return ""

    name = out.replace("\\", "/").rsplit("/", 1)[-1]
    if any(e["pr"] for e in items):
        desc += PR_NOTE
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:media="http://search.yahoo.com/mrss/">',
        "<channel>",
        f"<title>{esc(title)}</title>",
        f"<link>{page}</link>",
        f'<atom:link href="{PAGE}{name}" rel="self" type="application/rss+xml"/>',
        f"<description>{esc(desc)}</description>",
        "<language>ja</language>",
        f"<lastBuildDate>{format_datetime(datetime.now(JST).replace(microsecond=0))}</lastBuildDate>",
    ]
    for e in items:
        d = esc(e["cat"]) + ("（PR）" if e["pr"] else "")
        if e["image"]:
            d += esc(f'<br><img src="{e["image"]}" alt="">')
        lines += ["<item>",
                  f"<title>{esc(e['title'])}</title>",
                  f"<link>{esc(e['url'])}</link>",
                  f'<guid isPermaLink="true">{esc(e["url"])}</guid>',
                  f"<category>{esc(e['cat'])}</category>",
                  f"<description>{d}</description>"]
        if rfc(e["date"]):
            lines.append(f"<pubDate>{rfc(e['date'])}</pubDate>")
        if e["image"]:
            lines.append(f'<media:thumbnail url="{esc(e["image"])}"/>')
        lines.append("</item>")
    lines += ["</channel>", "</rss>", ""]
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"feed: {len(items)} items -> {out}")


def write_feeds(rack, folder):
    """ぜんぶ（feed.xml）、段ごと（feed-books.xml など）、雑誌の棚ごと（feed-shelf-walk.xml など）。"""
    import os
    entries = collect_entries(rack)
    base = "Living RACKs｜SCREP -処-"
    motto = "束はあちこちに。表紙はここに。"
    write_feed(entries, os.path.join(folder, "feed.xml"), base,
               motto + "本・便り・聲・雑誌・紀要の新着。")
    for row in rack.get("rows", []) + [{"id": "magazines", "name": "📬 雑誌｜SCREP -処-"}]:
        sub = [e for e in entries if "row:" + row["id"] in e["tags"]]
        write_feed(sub, os.path.join(folder, f"feed-{row['id']}.xml"),
                   f"{base}｜{row['name']}", motto + row.get("note", ""))
    for sh in rack.get("shelves", []):
        sub = [e for e in entries if "shelf:" + sh["id"] in e["tags"]]
        write_feed(sub, os.path.join(folder, f"feed-shelf-{sh['id']}.xml"),
                   f"{base}｜{sh['name']}", motto + "noteマガジンの棚。" + sh.get("note", ""))


def main(path):
    with open(path, encoding="utf-8") as f:
        rack = json.load(f)

    # 新しいマガジン：docs/rack/feeds/magazines.txt に書かれた /m/ の URL のうち、台帳にない冊を足す
    # （棚は空のまま＝「まだ棚のないもの」。題名と表紙はこのあと自動で入る）
    txt = rack.get("magazine_list", "docs/rack/feeds/magazines.txt")
    try:
        with open(txt, encoding="utf-8") as f:
            listed = re.findall(r"/m/(m[0-9a-f]{12})", f.read())
        have = {m["id"] for m in rack["magazines"]}
        n = 0
        for mid in dict.fromkeys(listed):
            if mid not in have:
                rack["magazines"].append({"id": mid, "title": "", "cover": "", "description": "",
                                          "count": None, "shelf": "", "order": 900 + n,
                                          "latest_at": None, "latest": []})
                n += 1
        print(f"magazines.txt: {len(set(listed))} listed, {n} new")
    except FileNotFoundError:
        pass

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

    for row in rack.get("rows", []):
        # 段の中を仕切るときは "groups": [{label, feeds, keep}, ...]。仕切らないなら段そのものが一つの組
        src = row.get("source", "")
        if src.startswith("whatsnew:"):
            try:
                row["items"] = read_whatsnew(src[9:], row.get("keep", 10))
                print(f"ok row {row.get('id')}: {len(row['items'])}")
            except Exception as e:
                print(f"skip row {row.get('id')}: {e}", file=sys.stderr)
            continue
        for grp in (row.get("groups") or [row]):
            fill_group(grp, row.get("id"), row.get("sort", True))

    rack["updated"] = datetime.now(JST).replace(microsecond=0).isoformat()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rack, f, ensure_ascii=False, indent=2)
        f.write("\n")

    # 同じ中身を、RSSでも配る（rack.json の隣に feed.xml）
    import os
    try:
        write_feeds(rack, os.path.dirname(path) or ".")
    except Exception as e:
        print(f"no feed: {e}", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "rack.json")
