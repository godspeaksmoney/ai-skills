# Howard Marks Research — Claude project prompt

Replicate my Howard Marks Research project end to end in Claude. Study the complete dated Oaktree memo archive, build and test a reusable investment skill, reproduce the dated Indian Energy Exchange analysis, publish a sanitized Claude edition to GitHub, and configure automatic memo intake and publishing.

Start with a short plan, then proceed. Ask for my help when account authorization or a required approval needs my participation. Continue independent work while waiting.

## 1. Reconcile and study the Oaktree archive

Use the dated year sections of Oaktree’s official memo index:
https://www.oaktreecapital.com/insights/memos

The 20 November 2026 baseline contained 167 dated entries across 37 annual sections, with 130 individual PDFs and 37 dated memo pages. It ran from The Route to Performance, 12 October 1990, through A Layman Thinks About AI, 11 November 2026. The original reading volumes contained 50 entries for 1990–2006, 61 for 2007–2017, and 56 from 2018 through the baseline. Reconcile the live listing against this baseline and account for additions, corrections, removals, and backfills.

Use the existing public skill as a baseline and cross-check:
https://github.com/godspeaksmoney/ai-skills/tree/main/ChatGPT/skills/howard-marks-research

Follow the individual dated memo links, including older PDF links that may require a rendered page or parsing of public page data. Exclude the separate Compilations section. Study the signed introduction associated with the dated October 2025 anthology entry. Count translations, transcripts, audio, and alternate formats of the same dated memo once. Preserve coauthors, guest contributions, similarly titled but distinct memos, and any meaningful difference between the archive date and the printed or originally circulated date.

Consult each original memo, including substantive exhibits, appendices, and footnotes. Use page images or OCR when important PDF content is unavailable in extracted text. For each dated entry, write an original study note with the displayed date, title, direct Oaktree link, argument, evidence or case, investment application, and boundary condition. Record genuine access or coverage gaps. Preserve prior notes when links move or entries disappear.

Maintain a machine-readable inventory, coverage and year reconciliation, the period reading notes, and a reusable intellectual framework. Provide an inventory comparison tool and a note verifier where useful. Test dates, titles, direct links, and one-to-one correspondence between reviewed inventory entries and notes, including equivalent URL encodings. Document that detecting edits to a memo under an unchanged URL may require checking the individual publication. Test retrieval with a single-memo question and a question that compares how Marks’s views developed.

Synthesize second-level thinking, price versus value, permanent impairment, the limits of forecasting, cycles and the pendulum, market temperature, credit and liquidity, risk control, contrarian judgment, patience, and payoff asymmetry. Link the methods to relevant dated memos and show how they affect a real underwriting decision.

## 2. Build the Claude skill and investment scorecard

Name the skill howard-marks-research. Include a concise SKILL.md with YAML name and description, a framework, scorecard, coverage guide, dated notes, inventory, intake instructions, worked example, and any comparison or verification scripts. Use relative links and document optional dependencies. Support research questions, investment assessment at a specific price, and continuing memo intake.

For an investment, identify the security, reporting currency, valuation date, dated closing price, and horizon. Verify changing facts using issuer filings, exchange data, and regulators. Distinguish observed facts and enacted rules from management views, proposals, and analyst assumptions. Trace the economics through to the owner of the actual security. Establish a plausible permanent-loss case, an upside the market may underweight, and what the quote requires. Compare scenario payoffs over the same horizon and in the same units. Explain the appropriate hurdle or investable alternative, confidence, contrary evidence, and reassessment triggers. Assign scenario probabilities only when the evidence supports them.

Use the original five factors and maximum points:

1. Earning power — 20
2. Protection against permanent loss — 25
3. Price versus conservative value — 25
4. Cycle and expectations — 15
5. Payoff asymmetry — 15

Award integer points up to each ceiling. Anchor zero at a severe weakness, half credit at a mixed case, and full credit at a demonstrable strength that survives a demanding test. Explain deviations from the midpoint. Keep each fact attached to the economic question it answers. If price is unverified, use a clearly dated reference price or give conditional ratings at assumed prices. Sum points with a floor of 1 and ceiling of 100.

Use these bands: 1–20 ★☆☆☆☆; 21–40 ★★☆☆☆; 41–60 ★★★☆☆; 61–80 ★★★★☆; 81–100 ★★★★★. These are skill conventions. Explain that the score expresses prospective compensation for the risks of buying at the stated price. Output the numeric score, visual stars, and one-page executive brief first, with full arithmetic, assumptions, and source citations in supporting analysis.

## 3. Reproduce the dated IEX example

Analyze Indian Energy Exchange Limited, NSE: IEX, using the 20 November 2026 official NSE equity-series close of ₹113.15 and a three-year horizon. Use historical evidence available at that cutoff. Keep any later refresh separate.

Verify the NSE closing file, IEX’s FY26 and H1 FY27 consolidated results, the relevant earnings call and operating releases, and CERC’s draft and current regulation registers. Explain how shared clearing and a common price could weaken IEX’s venue-specific liquidity advantage. Assess customer integration, segment-level share retention, unit fees, operating leverage, and what the owner could lose even without a refinancing problem. Reconcile settlement and member balances against their corresponding claims.

Reproduce and audit these historical benchmarks:

- Trailing diluted EPS of ₹5.87, using FY26 ₹5.54 minus H1 FY26 ₹2.75 plus H1 FY27 ₹3.08. The quote is approximately 19.3× trailing EPS.
- Use ending wealth per share = year-three EPS × exit P/E + aggregate cash dividends. Measure annualized return as (ending wealth / reference price)^(1/3) − 1. Use nominal INR and state the historical convention of cash dividends held without reinvestment, before taxes and costs.
- Downside: ₹4.70 EPS, 14× exit, ₹8 cumulative dividends, ₹73.80 ending wealth, about −34.8% total return and −13.3% annualized.
- Base: ₹7.10 EPS, 18× exit, ₹10 cumulative dividends, ₹137.80 ending wealth, about +21.8% total return and +6.8% annualized.
- Upside: ₹8.30 EPS, 22× exit, ₹12 cumulative dividends, ₹194.60 ending wealth, about +72.0% total return and +19.8% annualized.
- At a 12% annual research hurdle, the central case supports a price of roughly ₹98.08. At ₹113.15, the same hurdle requires approximately ₹8.28 in year-three EPS given an 18× exit and ₹10 dividends. Use no probability weights for these historical scenarios.
- Factor scores in rubric order: 16/20, 13/25, 11/25, 8/15, and 8/15. Total 56/100 · ★★★☆☆. Historical conclusion: Watch at ₹113.15. Re-underwrite around ₹98 or after final coupling details and evidence of post-launch segment share and fee retention.

Recalculate the benchmarks and explain any material difference. Show which specific Marks memos changed the underwriting. Produce a dated Markdown summary, a printable one-page PDF, and detailed supporting analysis for my working copy. Render and inspect the PDF. Include the dated one-page Markdown example with both ratings in the public skill.

## 4. Install, audit privacy, and publish to GitHub

Publish to the existing public repository https://github.com/godspeaksmoney/ai-skills under Claude/skills/howard-marks-research/. Add or update its listing in the root README while preserving existing tool sections and sibling skills.

Verify my GitHub identity, repository access, and publishing permissions. Guide me through authorized sign-in if needed. Use minimal access and GitHub’s no-reply author email for local Git commits.

Build the public package from an explicit list of approved files. Scan filenames, text, URLs, manifests, staged changes, and document metadata for personal names and contact details, local paths, usernames, private project names or links, credentials, and tokens. Publish original notes and source links, the portable skill files, necessary scripts, and the short dated IEX example. Keep source PDFs, raw extracts, the detailed IEX case, PDF, credentials, and private operational instructions in the working environment. Include an MIT license for original skill material and credit Howard Marks, credited coauthors, and Oaktree.

Add a skill README and CHANGELOG.md. Explain how to download the entire folder, copy it into .claude/skills/howard-marks-research, invoke /howard-marks-research, and update the installed copy. Offer a ZIP with the skill folder as its root for Claude’s custom-skill interface where supported. Include prerequisites, a sample prompt, source coverage, and the meaning of the score and stars. Test a fresh installation using only the public package.

## 5. Configure and verify monthly memo intake and publishing

Set a durable monthly intake for the first of each month at 6:00 p.m. Asia/Kolkata, matching the existing Howard Marks cadence. If the scheduler uses five-field UTC cron, use 30 12 1 * *. Verify the timezone, saved schedule, next run, and publishing access from the scheduled environment. Preserve the existing ChatGPT automation and limit the Claude task’s writes to the Claude edition and its catalog entry.

On each run, reconcile the full dated Oaktree archive with the inventory, including older backfills, changed URLs, substantive revisions, and unresolved entries. Study additions from the originals. Update notes, inventory, coverage, framework, and documentation where affected. Preserve dated worked examples and historical research.

Publish validated skill and documentation changes in one commit with a changelog entry. Use the same publishing step for validated manual skill updates. A clean no-change run creates no commit. Check for overlapping remote edits and respect branch protection. Use automatic merge only where authorized and supported after validation. If a pull request or approval is required, identify the remaining step. Preserve verified work and make retries safe.

Test a live no-change run and simulate a new memo, a revised link, an inaccessible source, detected private data, and a conflicting GitHub edit in a disposable environment. Verify the scheduled environment’s access before claiming unattended publishing works.

Return the public links, tested installation instructions, archive count and gaps, IEX score and one-page example, and the schedule and next run. Distinguish configured, manually tested, and successfully run on schedule.
