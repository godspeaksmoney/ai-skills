#!/usr/bin/env python3
"""Reconcile the live Research tab with references/manifest.json (standard library only).

The site combines three public feeds:
  archive-data.js   window.MM_ARCHIVE = [...]   static entries {y,t,v,g,l,c}
  /api/archive      {"overrides": {"year|title|venue": {...,"hidden":bool}}}
  /api/writing      {"writing": [{date,title,type,venue,guests,link}]}
Research = static items with c == "research" after overrides (hidden removed)
         + live items whose type is "research" (or missing).

Modes
  Full reconciliation (feeds fetched directly or supplied as files):
    python scripts/research_intake.py
    python scripts/research_intake.py --archive-js A.js --writing-json W.json --overrides-json O.json
  Light check, when only the static script's version and research count are known
  (for example from a web-fetch summary), with the two small JSON feeds verbatim:
    python scripts/research_intake.py --static-version 20260806 --static-count 181 --writing-json W.json --overrides-json O.json
Outputs a JSON report (stdout or --report PATH). Exit codes: 0 no change, 10 changes or
items needing review, 2 incomplete or unverifiable inputs. Never edits the manifest;
proposed IDs for additions are the next unused numbers.
"""
import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

SITE = "https://www.michaelmauboussin.com/"
UA = "MauboussinResearchSkill/1.0 (public archive reconciliation)"
LIVE_TYPES = {None, "", "research"}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Cache-Control": "no-cache"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8")


def parse_static(js):
    m = re.search(r"window\.MM_ARCHIVE\s*=\s*", js)
    if not m:
        raise ValueError("archive array not found")
    arr, _ = json.JSONDecoder().raw_decode(js[m.end():])
    return arr


def research_rows(static, writing, overrides):
    rows = []
    for it in static:
        y, t, v = it["y"], it["t"], it.get("v", "")
        upd = overrides.get(f"{y}|{t}|{v}", {})
        if upd.get("hidden"):
            continue
        r = {**it, **upd}
        if r.get("c") == "research":
            rows.append({"key": f"static|{y}|{t}|{v}", "title": r["t"], "year": r["y"], "venue": r.get("v", ""),
                         "coauthors": r.get("g", ""), "url": r.get("l", ""), "date": None})
    for it in writing:
        if it.get("type") in LIVE_TYPES:
            d, t, v = it["date"], it["title"], it.get("venue", "")
            rows.append({"key": f"live|{d}|{t}|{v}", "title": t, "year": int(d[:4]), "venue": v,
                         "coauthors": it.get("guests", ""), "url": it.get("link", ""), "date": d})
    return rows


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def compare(manifest, rows):
    have = {e["key"]: e for e in manifest["entries"]}
    live = {r["key"]: r for r in rows}
    next_id = max(e["id"] for e in manifest["entries"]) + 1
    additions, removals, changed = [], [], []
    for k, r in live.items():
        if k not in have:
            # possible title/venue correction of an existing entry: same year and normalized title or URL
            twin = next((e for e in manifest["entries"] if e["key"] not in live and
                         (norm(e["title"]) == norm(r["title"]) or e["listed_url"] == r["url"]) and e["year"] == r["year"]), None)
            if twin:
                changed.append({"id": twin["id"], "kind": "key_changed", "old_key": twin["key"], "new_key": k, "new": r})
            else:
                additions.append({"proposed_id": next_id, **r})
                next_id += 1
        else:
            e = have[k]
            for fld, mf in (("url", "listed_url"), ("coauthors", "coauthors")):
                if (r[fld] or "") != (e.get(mf) or ""):
                    changed.append({"id": e["id"], "kind": f"{fld}_changed", "old": e.get(mf), "new": r[fld]})
    matched_twins = {c["old_key"] for c in changed if c["kind"] == "key_changed"}
    for k, e in have.items():
        if k not in live and k not in matched_twins:
            removals.append({"id": e["id"], "key": k, "note": "retain entry and history; mark as delisted"})
    pending = [e["id"] for e in manifest["entries"] if e.get("review_status") != "reviewed"]
    dupes = len(live) != len(rows)
    return {"live_total": len(rows), "manifest_total": len(have), "additions": additions, "removals": removals,
            "changes": changed, "pending_reviews": pending, "duplicate_live_keys": dupes,
            "follow_up": [f["id"] for f in manifest.get("follow_up", [])]}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    root = Path(__file__).resolve().parent.parent
    ap.add_argument("--manifest", default=str(root / "references" / "manifest.json"))
    ap.add_argument("--archive-js")
    ap.add_argument("--writing-json")
    ap.add_argument("--overrides-json")
    ap.add_argument("--static-version")
    ap.add_argument("--static-count", type=int)
    ap.add_argument("--report")
    a = ap.parse_args()
    man = json.load(open(a.manifest, encoding="utf-8"))
    try:
        writing = json.loads(Path(a.writing_json).read_text("utf-8") if a.writing_json else fetch(SITE + "api/writing"))["writing"]
        overrides = json.loads(Path(a.overrides_json).read_text("utf-8") if a.overrides_json else fetch(SITE + "api/archive"))["overrides"]
    except Exception as exc:
        print(json.dumps({"status": "incomplete", "error": f"live feeds unavailable: {exc}"}))
        sys.exit(2)
    if a.static_version is not None:
        known = man.get("static_script", "")
        same_version = known.endswith(f"v={a.static_version}")
        live_rows = research_rows([], writing, overrides)
        live_keys = {r["key"] for r in live_rows}
        man_live = {e["key"] for e in man["entries"] if e["key"].startswith("live|")}
        rep = {"mode": "light", "static_version_unchanged": same_version,
               "static_count_matches": a.static_count == man["counts"]["static_research"],
               "overrides_present": bool(overrides), "live_additions_match": live_keys == man_live,
               "new_live_keys": sorted(live_keys - man_live), "missing_live_keys": sorted(man_live - live_keys)}
        clean = same_version and rep["static_count_matches"] and not overrides and rep["live_additions_match"]
        rep["status"] = "no_change" if clean else "full_reconciliation_required"
        out = json.dumps(rep, ensure_ascii=False, indent=2)
        Path(a.report).write_text(out, "utf-8") if a.report else print(out)
        sys.exit(0 if clean else 10)
    try:
        js = Path(a.archive_js).read_text("utf-8") if a.archive_js else None
        if js is None:
            html = fetch(SITE)
            m = re.search(r'src=["\']([^"\']*archive-data\.js[^"\']*)', html)
            if not m:
                raise ValueError("archive script not referenced on the home page")
            js = fetch(urllib.request.urljoin(SITE, m.group(1)))
        static = parse_static(js)
    except Exception as exc:
        print(json.dumps({"status": "incomplete", "error": f"static archive unavailable: {exc}"}))
        sys.exit(2)
    rows = research_rows(static, writing, overrides)
    if any(not r["url"] for r in rows):
        print(json.dumps({"status": "incomplete", "error": "entries without links; inspect the rendered tab"}))
        sys.exit(2)
    rep = {"mode": "full", **compare(man, rows)}
    dirty = rep["additions"] or rep["removals"] or rep["changes"] or rep["pending_reviews"] or rep["duplicate_live_keys"]
    rep["status"] = "changes" if dirty else "no_change"
    out = json.dumps(rep, ensure_ascii=False, indent=2)
    Path(a.report).write_text(out, "utf-8") if a.report else print(out)
    sys.exit(10 if dirty else 0)


if __name__ == "__main__":
    main()
