# Wealth Insight Research

Use your own Wealth Insight magazine archive to answer investment research questions, compare reporting across editions, and review new issues with original PDF-page citations.

## Install

Copy the complete **ChatGPT/skills/wealth-insight-research** folder into your project's **.agents/skills/wealth-insight-research** directory. Keep the supporting references and scripts with it.

Place your reviewed archive in the project's **Wealth Insight Research** directory, or tell Codex which archive and research paths to use. Keep an index, a manifest and one note file per issue. [The intake workflow](references/intake.md) explains the expected records and review steps.

Try this prompt in the destination project:

> Use $wealth-insight-research to compare how two issues discuss a company. Cite the issue and original PDF pages, preserve the dates, and identify any change in assumptions.

## Check a maintained archive

The optional checker requires Node.js. Run it from the skill directory:

```text
node scripts/check-archive.mjs "<research-directory>" ["<originals-root>"]
```

The research directory contains manifest.json, INDEX.md and corpus/YYYY-MM.md. Manifest issues contain id, source, pdf_pages, covered_pages, sha256, notes and notes_sha256. Source paths are relative to the originals root. Each note contains one ## PDF p. N section per one-based PDF page. The checker verifies recorded coverage and file hashes. The actual reading and visual verification are performed during issue intake.

## Maintained coverage

The originating study covers **8 issues and 588 PDF pages**, through **2026-11**, reviewed on **2026-11-17**. The [coverage record](references/coverage.json) tracks reviewed issue identities, page counts and note fingerprints. Actual coverage in your installation depends on the local files available.

The public package contains the reusable workflow, checker and coverage metadata. Keep your magazine copies and detailed research notes in your own archive.

## Updates and attribution

After a completed issue review or a validated skill edit, run the installed project's configured GitHub publishing step. Review the proposed diff, preserve concurrent edits, verify the published commit, and report an unsuccessful sync as pending. GitHub receives the reusable package and refreshed coverage record. See the [changelog](CHANGELOG.md).

This is an independent research workflow for Wealth Insight, published by Value Research. Magazine content remains subject to the publisher's rights. The [MIT license](LICENSE) covers the original instructions and checker in this folder. Publication does not grant rights to the magazine or the private study archive.
