# Intake: new and revised research

Use this file monthly, or whenever someone asks for a review of a new or revised paper. The source is the Research tab of [Michael J. Mauboussin's archive](https://www.michaelmauboussin.com/#writing). Inclusion rules and the current counts are in the [manifest](manifest.json): `rules`, `counts` and `static_script`.

## 1. Reconcile the list

Either path is acceptable. Record which one you used.

- **Direct fetch (full):** from the skill folder, run `python scripts/research_intake.py`. It reads the home page, `archive-data.js`, `/api/archive` and `/api/writing`, applies overrides and hidden-entry rules, and compares the result with the manifest.
- **When the shell cannot reach the site:**
  1. Use a web-fetch tool to read `/api/writing` and `/api/archive` verbatim, and save them as JSON.
  2. From the home page, find the `archive-data.js?v=` version and the count of `c:"research"` items.
  3. Run the light check: `python scripts/research_intake.py --static-version V --static-count N --writing-json W.json --overrides-json O.json`.
  4. If the result is `no_change`, stop. Otherwise obtain the full static list, using a browser or a saved copy of `archive-data.js` passed with `--archive-js`, and rerun the full mode.

Exit codes: `0` means no change, `10` means there are changes or items to review, and `2` means the inputs were incomplete. Treat `2` as an intake issue to report. Never take it as "no change".

## 2. Classify each difference

| Report item | Action |
|---|---|
| `additions` | New entry. Assign the next unused ID (the script proposes one). Never reuse an ID. |
| `changes: url_changed` | Revised link. Confirm whether it is the same paper or a new edition. A changed URL alone is reconciled once identity is confirmed. Re-hash if possible. |
| `changes: key_changed` | Title, venue or year correction. Keep the ID and add a history entry. |
| `changes: coauthors_changed` | Update the credit and add a history entry. |
| `removals` | Keep the entry, its note and its history. Set `review_status` to `delisted` and record the date. |
| `pending_reviews`, `follow_up` | Retry the previously unresolved or partial reviews. |

A separately listed revision, a new edition, or an identical title from a different year is a **distinct entry** with its own ID and note. Cross-reference it in `edition_note`.

## 3. Study verified material

For each addition, revision or pending item:

1. Open the primary PDF, or a verifiable publisher copy. Read the summary, argument, cases, exhibits and conclusion needed to understand the result.
2. Write an original note in the next notes file under `<a id="paper-NNN"></a>`. Cover the question, the argument and evidence, the application, the limitations, the editions, and an *Access* line saying exactly what was read. Use one-based PDF page locators only where you verified them. Never copy passages from the paper.
3. If retrieval fails, set `review_status` to `pending`, add the entry to `pending` with the reason, and keep the listing data. Never mark an entry reviewed just because its title was seen.

## 4. Update the library

- **Manifest:** add or update the entry, then update `counts`, `history`, `reconciled_on` and `static_script`.
- **Index:** add the row and tags in [archive index](archive-index.md).
- **Synthesis:** update [research synthesis](research-synthesis.md) only when the paper adds to, extends or qualifies a method. Note material differences between editions.
- **Documentation:** update the README's usage text only if behaviour changed. Add a `CHANGELOG.md` entry.
- Keep the dated IEX example unchanged. Any refresh goes in a new, separately dated file.

## 5. Validate

1. Run `python scripts/validate.py`. It must exit 0, which confirms unique IDs and keys, reconciled counts, one anchor per reviewed entry, working links, and traceable pending items.
2. Run `python scripts/privacy_scan.py .` on the package. It must report 0 findings.
3. Test retrieval: answer one question that needs the new paper by citing its note and source link.

## 6. Publish

See [publishing](publishing.md). On a clean no-change run, make no file changes, no commit and no notification beyond the run log.
