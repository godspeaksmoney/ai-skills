---
name: mauboussin-research
description: Apply Michael J. Mauboussin's 183-paper Research archive. Use it to answer and cite questions about the research, to analyze a business as an investment (1–100 score, five-star rating, one-page executive summary), or to review new or revised papers for the library.
---

# Mauboussin research

The archive is in `references/`. Each of the 183 entries has a study note. The [archive index](references/archive-index.md) locates papers by title, year, coauthor or tag. The [research synthesis](references/research-synthesis.md) maps analytical methods to the papers. The [manifest](references/manifest.json) records sources, review status and coverage limits. Credit Mauboussin and his coauthors, link to the primary source, and write paraphrases rather than quotations.

## Answer a question about the research

1. Find the paper or papers in the archive index, then read their notes.
2. Answer from the notes and cite each one by its three-digit ID linked to the note (`references/notes/...#paper-NNN`) together with the source PDF link. Where the edition matters, compare editions (see the end of the synthesis) and say how they differ.
3. If a note's *Access* line shows a partial capture and the answer depends on unread sections, say so, or read the primary source.

## Analyze a business as an investment

Follow [business analysis](references/business-analysis.md):

1. Date the analysis. Verify the security and the price: the official close, or two timestamped sources that agree.
2. Verify changing facts in filings and with regulators. Label each one as reported, management view, proposed rule, enacted rule or assumption.
3. Trace the business from customers through incremental returns to cash flow and fade. Take the outside view.
4. Build bear, base and bull scenarios with probabilities. Solve for one operating assumption implied by the price, then stress-test.
5. Score with the [rubric](references/scoring.md) (`python3 scripts/score.py G1 … G6`). The weights, grades and probabilities are the skill's or the analyst's choices. The methods are attributed to papers.
6. Deliver the score, stars and a one-page summary following the [template](references/executive-summary-template.md). Put calculations and sources in a supporting analysis. `scripts/scenario_dcf.py` provides a generic scenario DCF with an implied-growth solve.

The [Indian Energy Exchange example](references/iex-executive-summary.md) shows the expected output: 60/100 · ★★★☆☆, dated 20 November 2026. It is historical. Refresh the filings, rules and price before treating it as a current view.

## Review new or revised research

Follow [intake](references/intake.md): reconcile the live Research tab (`python3 scripts/research_intake.py`), study each verified addition or revision, update the notes, manifest, index and synthesis, run `scripts/validate.py` and `scripts/privacy_scan.py`, then follow [publishing](references/publishing.md). Keep existing IDs. Keep failed or partial reviews visible in `pending` or `follow_up`.

The scripts use only the Python 3 standard library. Everything else works from the included notes without them.
