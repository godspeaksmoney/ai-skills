"""List Oaktree's dated individual memo entries. A saved index can be used offline."""

import argparse
import json
import re
from datetime import date, datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen

INDEX = "https://www.oaktreecapital.com/insights/memos"


class MemoIndex(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.section = None
        self.date = None
        self.capture = None
        self.buffer = []
        self.rows = []
        self.url = None
        self.years = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {"button", "time"} and self.date is not None:
            raise ValueError(f"Dated entry has no recognized individual link: {self.date}")
        if tag == "button":
            self.capture = tag
            self.buffer = []
            self.section = self.date = None
        elif tag == "time" and self.section:
            self.date = None
            self.capture = tag
            self.buffer = []
        elif tag == "a" and self.section and "oc-title-link" in attrs.get("class", "").split():
            href = attrs["href"].strip()
            if href.lower().startswith("javascript:"):
                match = re.search(r"[\x22'](https?://[^\x22']+)[\x22']\s*\)\s*;?\s*$", href)
                if not match:
                    raise ValueError(f"Unrecognized memo link: {href}")
                href = match.group(1)
            self.url = urljoin(INDEX, href)
            self.capture = tag
            self.buffer = []

    def handle_data(self, data):
        if self.capture:
            self.buffer.append(data)

    def handle_endtag(self, tag):
        if tag != self.capture:
            return
        value = " ".join("".join(self.buffer).split())
        self.capture = None
        if tag == "button" and re.fullmatch(r"[12]\d{3}", value):
            self.section = int(value)
            self.years.add(self.section)
        elif tag == "time":
            self.date = datetime.strptime(value, "%b %d, %Y").date()
        elif tag == "a":
            if not self.date or self.date.year != self.section or not value:
                raise ValueError(f"Missing or inconsistent date/title: {value} ({self.section})")
            target = urlsplit(self.url)
            if target.scheme != "https" or target.hostname not in {"oaktreecapital.com", "www.oaktreecapital.com"}:
                raise ValueError(f"Review changed publication host: {self.url}")
            self.rows.append(dict(date=self.date.isoformat(), title=value, url=self.url))
            self.date = None


def parse_index(html):
    parser = MemoIndex()
    parser.feed(html)
    parser.close()
    keys = {(r["date"], r["title"]) for r in parser.rows}
    covered = {int(r["date"][:4]) for r in parser.rows}
    if parser.date is not None or not parser.rows or covered != parser.years or len(keys) != len(parser.rows):
        raise ValueError("Incomplete or ambiguous dated inventory; inspect the publisher index.")
    return sorted(parser.rows, key=lambda r: (r["date"], r["title"]))


def compare(candidate, baseline):
    old = {(row["date"], row["title"]): row for row in baseline}
    new = {(row["date"], row["title"]): row for row in candidate}
    return {
        "listed": len(new),
        "added": [new[key] for key in sorted(new.keys() - old.keys())],
        "changed_links": [
            {"before": old[key], "after": new[key]} for key in sorted(new.keys() & old.keys())
            if old[key]["url"] != new[key]["url"]
        ],
        "no_longer_listed": [old[key] for key in sorted(old.keys() - new.keys())],
    }


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--html", type=Path, help="Saved publisher index, otherwise fetch live")
    cli.add_argument("--compare", type=Path, help="Report changes against an existing inventory")
    cli.add_argument("--as-of", type=date.fromisoformat, help="Include entries dated on or before YYYY-MM-DD")
    args = cli.parse_args()
    if args.html:
        raw = args.html.read_bytes()
    else:
        with urlopen(Request(INDEX, headers={"User-Agent": "Memo research inventory/1.0"}), timeout=45) as response:
            raw = response.read()
    rows = parse_index(raw.decode("utf-8-sig"))
    rows = [r for r in rows if not args.as_of or r["date"] <= args.as_of.isoformat()]
    result = compare(rows, json.loads(args.compare.read_text(encoding="utf-8-sig"))) if args.compare else rows
    print(json.dumps(result, ensure_ascii=True, indent=2))
