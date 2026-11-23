#!/usr/bin/env python3
"""Validate archive coverage and internal links before calling the library complete or publishing.

Checks: unique IDs and keys; counts reconcile; one note anchor per reviewed entry; every
manifest note link resolves; every relative Markdown link in SKILL.md and references resolves
(including #anchors); pending and follow-up items are traceable; SKILL.md frontmatter is valid.
Exit 0 when all checks pass, 1 otherwise. Standard library only.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def anchors(path):
    return set(re.findall(r'<a id="([^"]+)"></a>', path.read_text("utf-8")))


def main():
    errs = []
    man = json.loads((ROOT / "references" / "manifest.json").read_text("utf-8"))
    ents = man["entries"]
    ids = [e["id"] for e in ents]
    keys = [e["key"] for e in ents]
    if len(set(ids)) != len(ids):
        errs.append("duplicate IDs")
    if len(set(keys)) != len(keys):
        errs.append("duplicate keys")
    c = man["counts"]
    if c["static_research"] + c["live_research"] != c["total"] or c["total"] != len(ents):
        errs.append(f"count mismatch: {c} vs {len(ents)} entries")
    reviewed = [e for e in ents if e["review_status"] == "reviewed"]
    if c["reviewed"] != len(reviewed) or c["pending"] != len(ents) - len(reviewed):
        errs.append("reviewed/pending counts do not match entries")
    pending_ids = {p["id"] if isinstance(p, dict) else p for p in man.get("pending", [])}
    for e in ents:
        if e["review_status"] != "reviewed" and e["id"] not in pending_ids:
            errs.append(f"{e['id']}: unreviewed but not listed in pending")
    seen = {}
    for e in reviewed:
        f, _, a = e["note"].partition("#")
        p = ROOT / "references" / f
        if not p.exists():
            errs.append(f"{e['id']}: note file missing {f}")
            continue
        seen.setdefault(f, anchors(p))
        if a not in seen[f]:
            errs.append(f"{e['id']}: anchor #{a} missing in {f}")
    all_anchor_ids = [a for f in seen for a in seen[f]]
    if len(all_anchor_ids) != len(set(all_anchor_ids)) or len(all_anchor_ids) != len(reviewed):
        errs.append(f"note anchors ({len(all_anchor_ids)}) do not match reviewed entries ({len(reviewed)}) one-to-one")
    md_files = [ROOT / "SKILL.md", ROOT / "README.md"] + sorted((ROOT / "references").rglob("*.md"))
    for md in md_files:
        if not md.exists():
            continue
        for link in re.findall(r"\]\(([^)\s]+)\)", md.read_text("utf-8")):
            if re.match(r"[a-z]+:", link) or link.startswith("#"):
                continue
            f, _, a = link.partition("#")
            target = (md.parent / f).resolve()
            if not target.exists():
                errs.append(f"{md.relative_to(ROOT)}: broken link {link}")
            elif a and target.suffix == ".md":
                if a not in anchors(target) and a not in {re.sub(r"[^a-z0-9 -]", "", h.lower()).replace(" ", "-")
                                                          for h in re.findall(r"^#+ (.+)$", target.read_text("utf-8"), re.M)}:
                    errs.append(f"{md.relative_to(ROOT)}: missing anchor {link}")
    sk = (ROOT / "SKILL.md").read_text("utf-8")
    fm = re.match(r"^---\nname: ([a-z0-9-]+)\ndescription: (.+?)\n---\n", sk, re.S)
    if not fm or fm.group(1) != ROOT.name:
        errs.append("SKILL.md frontmatter must start with name matching the folder and a description")
    elif len(fm.group(2)) > 1024:
        errs.append("description longer than 1024 characters")
    print(json.dumps({"entries": len(ents), "reviewed": len(reviewed), "pending": len(ents) - len(reviewed),
                      "follow_up": len(man.get("follow_up", [])),
                      "follow_up_meaning": "reviewed entries whose capture was partial; re-read when convenient (see manifest follow_up)",
                      "errors": errs}, indent=2))
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
