"""Reconcile every dated research note, its title and direct source with the inventory."""

import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

REFS = Path(__file__).resolve().parents[1] / "references"
HEADER = re.compile(r"^### (\d{4}-\d{2}-\d{2}) (?:·|—|–|-) (.+?)\s*$", re.MULTILINE)
LINK = re.compile(r"\]\((https://(?:www\.)?oaktreecapital\.com/[^\s]+)\)")

def identity(date, title, url):
    return date, " ".join(title.split()), unquote(url)

def verify(refs):
    with (refs / "inventory.json").open(encoding="utf-8-sig") as stream:
        expected = Counter(identity(r["date"], r["title"], r["url"]) for r in json.load(stream))
    observed = Counter()
    problems = []
    for name in ("early.md", "middle.md", "late.md"):
        body = (refs / name).read_text(encoding="utf-8-sig")
        headings = list(HEADER.finditer(body))
        for i, heading in enumerate(headings):
            end = headings[i+1].start() if i+1 < len(headings) else len(body)
            passage = body[heading.end():end]
            sources = LINK.findall(passage)
            if len(sources) != 1:
                problems.append(f"{name} {heading[1]}: expected one individual source link")
                continue
            observed[identity(heading[1], heading[2], sources[0])] += 1
    for label, difference in (("Missing or mismatched", expected - observed),
                              ("Extra or mismatched", observed - expected)):
        problems.extend(f"{label}: {date} {title} ({count})" for (date, title, _), count in difference.items())
    for key, count in expected.items():
        if count > 1:
            problems.append(f"Duplicate inventory row: {key[0]} {key[1]}")
    if not expected:
        problems.append("Empty inventory")
    return sum(observed.values()), problems

if __name__ == "__main__":
    count, problems = verify(REFS)
    if problems:
        sys.exit("\n".join(problems))
    print(f"Verified {count} individual memo notes against their inventory dates, titles and source URLs.")
