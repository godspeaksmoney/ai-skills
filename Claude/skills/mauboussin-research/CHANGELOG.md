# Changelog

## 2026-11-23 — Claude edition 1.0.0

- First Claude edition.
- **Live reconciliation.** The Research tab was reconciled with the live site on 23 Nov 2026: 183 entries (181 static plus 2 live additions), no overrides and no hidden entries. The listing is identical to the 20 Nov 2026 snapshot: keys, links and coauthors hash to the same value.
- **Source identity.** 167 PDFs were confirmed byte-identical to the snapshot by SHA-256. The 16 Morgan Stanley PDFs were read but not re-hashed.
- **Study notes.** 183 original notes, each written from its primary PDF. 151 papers were captured in full; 32 long papers were captured partially and are listed in the manifest's `follow_up` for a deeper re-read.
- **References.** Searchable archive index with tags and edition families; method synthesis covering competitive advantage and fade through decision quality; scoring rubric; business-analysis workflow; summary template; intake and publishing procedures.
- **Example.** A dated Indian Energy Exchange example: 60/100 · ★★★☆☆, analysis date 20 Nov 2026, price ₹115.17.
- **Scripts.** Standard-library scripts: `score.py`, `scenario_dcf.py`, `research_intake.py`, `validate.py`, `privacy_scan.py`.
