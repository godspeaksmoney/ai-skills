import argparse
import concurrent.futures
import hashlib
import io
import json
import logging
import re
import sys
import time
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

SITE = "https://www.michaelmauboussin.com/"
AGENT = "ResearchArchiveReader/1.0 (public source review)"
TYPE_MAP = {"research": "research", "article": "written", "interview": "written",
            "video": "video", "podcast": "audio"}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": AGENT, "Cache-Control": "no-cache"})
    with urllib.request.urlopen(req, timeout=22) as response:
        return response.read(), response.geturl()


def source_key(origin, year_or_date, title, venue):
    return f"{origin}|{year_or_date}|{title}|{venue}"


def archive(root=None):
    def get(name, url):
        if root is not None:
            return (root / name).read_bytes()
        return fetch(url)[0]

    if root is None:
        html = fetch(SITE)[0].decode("utf-8")
        script = re.search(r'src=["\x27]([^"\x27]*archive-data\.js[^"\x27]*)', html)
        if not script:
            raise ValueError("The site no longer exposes the expected archive script.")
        static_url = urllib.parse.urljoin(SITE, script.group(1))
    else:
        static_url = SITE + "archive-data.js"

    raw = get("archive-data.js", static_url).decode("utf-8")
    match = re.search(r"window\.MM_ARCHIVE\s*=\s*", raw)
    if not match:
        raise ValueError("Could not locate the archive array.")
    static, _ = json.JSONDecoder().raw_decode(raw[match.end():])
    adds = json.loads(get("writing-live.json", SITE + "api/writing"))["writing"]
    overrides = json.loads(get("archive-live.json", SITE + "api/archive"))["overrides"]
    if not static or not isinstance(adds, list) or not isinstance(overrides, dict):
        raise ValueError("Incomplete archive feeds.")
    records = []
    for item in static:
        year, title, venue = item["y"], item["t"], item.get("v", "")
        update = overrides.get(f"{year}|{title}|{venue}", {})
        if update.get("hidden"):
            continue
        row = {**item, **update}
        if row["c"] == "research":
            records.append((source_key("static", year, title, venue), row))
    for item in adds:
        if TYPE_MAP.get(item.get("type"), "research") == "research":
            date, title, venue = item["date"], item["title"], item.get("venue", "")
            records.append((source_key("live", date, title, venue), {
                "t": title, "y": int(date[:4]), "v": venue, "g": item.get("guests", ""),
                "l": item.get("link", ""), "date": date}))
    result = [{"key": key, "title": row["t"], "year": row["y"], "venue": row.get("v", ""),
               "coauthors": row.get("g", ""), "url": row.get("l", ""), "date": row.get("date")}
              for key, row in records]
    if len({r["key"] for r in result}) != len(result) or any(not r["url"] for r in result):
        raise ValueError("Duplicate entry keys or missing URLs. Inspect the rendered Research tab.")
    return result


def write_json(path, value):
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)


def compare(current, baseline):
    old = {row["key"]: row for row in baseline}
    fields = ("title", "year", "venue", "coauthors", "url", "date")
    changes = {"new": [], "changed": [], "absent": [], "pending": []}
    now = {row["key"] for row in current}
    for row in current:
        prior = old.get(row["key"])
        if prior is None:
            changes["new"].append(row)
        elif any(row[key] != prior.get(key) for key in fields):
            changes["changed"].append({"previous": prior, "current": row})
        elif prior.get("review_status") != "reviewed":
            changes["pending"].append(prior)
    changes["absent"] = [row for row in baseline if row["key"] not in now]
    return changes


class ArticleHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.text = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("style", "script", "svg"):
            self.skip += 1
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.links.append(href)
        if tag in ("p", "h1", "h2", "h3", "li", "blockquote", "br"):
            self.text.append("\n")

    def handle_endtag(self, tag):
        if tag in ("style", "script", "svg") and self.skip:
            self.skip -= 1

    def handle_data(self, text):
        if not self.skip and text.strip():
            self.text.append(text.strip() + " ")


def read_document(url):
    from pypdf import PdfReader

    raw, resolved = fetch(url)
    if not raw.lstrip().startswith(b"%PDF-"):
        parsed = ArticleHTML()
        parsed.feed(raw.decode("utf-8", errors="replace"))
        candidates = list(dict.fromkeys(urllib.parse.urljoin(resolved, href) for href in parsed.links
                                        if urllib.parse.urlsplit(href).path.lower().endswith(".pdf")))
        if len(candidates) == 1:
            raw, resolved = fetch(candidates[0])
        else:
            return raw, resolved, None, ["".join(parsed.text)], candidates
    if not raw.lstrip().startswith(b"%PDF-"):
        raise ValueError("Linked document did not return a PDF.")
    reader = PdfReader(io.BytesIO(raw), strict=False)
    pages = [page.extract_text() or "" for page in reader.pages]
    return raw, resolved, len(pages), pages, []


def acquire(item, folder):
    number = item["id"]
    meta = folder / f"{number:03}.json"
    path = folder / f"{number:03}.txt"
    if meta.exists() and path.exists():
        cached = json.loads(meta.read_text(encoding="utf-8"))
        if cached.get("source_url") == item["url"] and cached.get("page_count"):
            return cached
    try:
        raw, resolved, count, pages, candidates = read_document(item["url"])
        path.write_text("\n".join(f"\n=== PDF PAGE {i} ===\n{page}" for i, page in enumerate(pages, 1)),
                        encoding="utf-8")
        data = {"id": number, "source_url": item["url"], "resolved_url": resolved,
                "page_count": count, "text_chars": sum(map(len, pages)),
                "low_text_pages": [i for i, page in enumerate(pages, 1) if len(page.strip()) < 100],
                "sha256": hashlib.sha256(raw).hexdigest(), "other_pdf_links": candidates}
    except Exception as exc:
        data = {"id": number, "source_url": item["url"], "error": str(exc)}
    write_json(meta, data)
    time.sleep(0.22)
    return data


def main():
    parser = argparse.ArgumentParser(description="Compare the author's Research tab with a review manifest.")
    parser.add_argument("--snapshot", type=Path, help="Use a saved copy of the three public feeds.")
    parser.add_argument("--baseline", type=Path, help="Load a prior manifest and report changes to stdout.")
    parser.add_argument("--inventory", type=Path, help="Save the current source inventory.")
    parser.add_argument("--extract-to", type=Path, help="Fetch and extract originals into a temporary folder.")
    parser.add_argument("--ids", type=int, nargs="+", help="With extraction, retrieve only these IDs.")
    options = parser.parse_args()
    records = archive(options.snapshot)
    print(f"Research entries: {len(records)}", file=sys.stderr)
    for number, item in enumerate(records, 1):
        item["id"] = number
    if options.inventory:
        write_json(options.inventory, records)
    if options.baseline:
        old = json.loads(options.baseline.read_text(encoding="utf-8"))
        print(json.dumps(compare(records, old["entries"]), ensure_ascii=False, indent=2))
    if options.extract_to:
        logging.getLogger("pypdf").setLevel(logging.ERROR)
        folder = options.extract_to
        folder.mkdir(parents=True, exist_ok=True)
        selected = [r for r in records if not options.ids or r["id"] in options.ids]
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
            futures = [pool.submit(acquire, record, folder) for record in selected]
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                print(result["id"], result.get("page_count") or result.get("error", "HTML"),
                      result.get("text_chars", ""), flush=True)


if __name__ == "__main__":
    main()
