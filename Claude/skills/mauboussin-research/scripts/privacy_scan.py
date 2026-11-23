#!/usr/bin/env python3
"""Scan files destined for publication for private or identifying content.

Usage: python scripts/privacy_scan.py PATH [PATH ...] [--deny-file FILE]
Flags email addresses (except GitHub no-reply), phone numbers, tokens and keys, absolute local
paths, home-directory user names, private hosts and IPs, cloud-drive links, and any literal
strings listed in an optional deny file (one per line, for example personal names or internal
project names; keep that file out of the repository). Exit 0 when clean, 1 on findings.
"""
import argparse
import re
import sys
from pathlib import Path

PATTERNS = {
    "email": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    "phone": r"(?<![\d.])(?:\+?\d{1,3}[ -]?)?(?:\(\d{2,4}\)[ -]?)?\d{3,5}[ -]\d{3,5}(?:[ -]\d{2,5})?(?![\d.])",
    "github_token": r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b",
    "aws_key": r"\bAKIA[0-9A-Z]{16}\b",
    "private_key": r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    "generic_secret": r"(?i)\b(?:api[_-]?key|secret|token|password)\s*[:=]\s*['\"][^'\"]{8,}['\"]",
    "bearer": r"(?i)\bbearer\s+[A-Za-z0-9._-]{20,}",
    "windows_path": r"\b[A-Za-z]:\\(?:Users|Documents and Settings)\\[^\\\s]+",
    "unix_home": r"(?<![\w.])/(?:home|Users)/[A-Za-z0-9._-]+",
    "container_path": r"/mnt/(?:user-data|project-files)|/r[o]ot/|/t[m]p/",
    "private_ip": r"\b(?:10|127|192\.168|172\.(?:1[6-9]|2\d|3[01]))\.\d{1,3}\.\d{1,3}(?:\.\d{1,3})?\b",
    "loopback_host": r"\blocal[h]ost\b",
    "cloud_drive": r"(?i)(?:docs|drive)\.google\.com/|dropbox\.com/|onedrive\.live\.com|sharepoint\.com",
    "claude_session": r"claude\.ai/(?:code|chat|share)/",
}
ALLOW = [re.compile(p) for p in [r"noreply@anthropic\.com", r"[0-9]+\+?[A-Za-z0-9-]*@users\.noreply\.github\.com"]]
TEXT_EXT = {".md", ".py", ".json", ".txt", ".yml", ".yaml", ".toml", ".cfg", ""}


def scan_text(name, text, deny):
    hits = []
    for kind, pat in PATTERNS.items():
        for m in re.finditer(pat, text):
            s = m.group(0)
            if any(a.fullmatch(s) for a in ALLOW):
                continue
            if kind == "phone" and (re.fullmatch(r"\d{4}[ -]\d{2,4}", s) or not re.search(r"\d{3}[ -]\d{3}", s)):
                continue
            line = text.count("\n", 0, m.start()) + 1
            hits.append((name, line, kind, s[:60]))
    low = text.lower()
    for d in deny:
        i = low.find(d.lower())
        if i >= 0:
            hits.append((name, low.count("\n", 0, i) + 1, "deny_list", d))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--deny-file")
    a = ap.parse_args()
    deny = [l.strip() for l in Path(a.deny_file).read_text("utf-8").splitlines() if l.strip()] if a.deny_file else []
    hits = []
    for p in a.paths:
        for f in ([Path(p)] if Path(p).is_file() else sorted(Path(p).rglob("*"))):
            if not f.is_file():
                continue
            hits += scan_text(str(f), str(f), deny)  # filenames
            if f.suffix.lower() in TEXT_EXT:
                hits += scan_text(str(f), f.read_text("utf-8", errors="replace"), deny)
            elif f.suffix.lower() == ".zip":
                import zipfile
                with zipfile.ZipFile(f) as z:
                    for n in z.namelist():
                        hits += scan_text(f"{f}!{n}", n, deny)
                        if Path(n).suffix.lower() in TEXT_EXT and not n.endswith("/"):
                            hits += scan_text(f"{f}!{n}", z.read(n).decode("utf-8", "replace"), deny)
    for h in hits:
        print(f"{h[0]}:{h[1]}: {h[2]}: {h[3]}")
    print(f"{len(hits)} finding(s)")
    sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
