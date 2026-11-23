# Berkshire Hathaway Business Analysis — Claude project prompt

Replicate my Berkshire Hathaway Business Analysis project end to end in Claude. Study the full annual shareholder-letter archive, build and test a reusable skill, reproduce the dated Indian Energy Exchange analysis, publish a sanitized Claude edition to GitHub, and configure automatic research and publication updates.

Start with a short plan, then proceed. Ask for my help when account authorization or a required approval needs my participation. Continue independent work while waiting.

## 1. Study and reconcile the Berkshire archive

Use Berkshire’s official sources:

- Warren Buffett’s annual letters: https://www.berkshirehathaway.com/letters/letters.html
- Greg Abel’s annual letters: https://www.berkshirehathaway.com/letters/gealetters.html
- Annual reports: https://www.berkshirehathaway.com/reports.html

The original baseline is 49 annual letters for reporting years 1977–2025, comprising 21 official HTML documents and 28 official PDFs totaling 571 PDF pages. Buffett authored the main 1977–2024 letters. Abel authored the 2025 letter. Preserve Charlie Munger’s attribution for the retrospective included in the 2014 material. Check both letter indices and the latest annual report for subsequent additions or changes. Count one reporting-year letter once when the standalone letter and annual report reproduce the same text.

Use the existing public skill as a baseline and cross-check:
https://github.com/godspeaksmoney/ai-skills/tree/main/ChatGPT/skills/berkshire-business-analysis

Consult the original source for each year. Record one original, decision-relevant note per annual letter. Capture the principle, business example, how it affects an investment decision, and material limitations. Use HTML section names or one-based PDF page positions where verified. Read substantive exhibits, tables, appendices, and footnotes where they change the interpretation. Check image-only or poorly extracted pages visually when they contain relevant evidence. The original review flagged and inspected PDF page 22 of the 2010 letter.

Maintain a manifest keyed by reporting year with the official URL, format, author where useful, retrieval or review status, and page count, source hash, or extraction limitations where verified. Preserve previous years and meaningful revisions. Record blocked or partial entries precisely and keep them eligible for retry. Reconcile the manifest, yearly note headings, and official URLs before claiming coverage.

Add a thematic index covering owner earnings, durable competitive advantages, incremental returns and retained earnings, capital allocation, acquisitions, buybacks and dilution, stewardship and incentives, insurance float and tail risk, financial resilience, intrinsic value, and margin of safety. Test retrieval with one question about a specific letter and one that compares how a principle was applied across years.

## 2. Build the Claude skill and scoring workflow

Name the skill berkshire-business-analysis. Include SKILL.md with valid YAML frontmatter, the annual notes and manifest, scoring and valuation guidance, a one-page executive-summary template, intake instructions, a dated worked example, and a simple score calculator.

For a company, establish the issuer, security, currency, reporting periods, valuation date, and verified closing price. Prefer primary filings, exchange records, and regulators. Identify who pays, why they pay, and which observable advantage explains the economics. Examine what could erode that advantage. Review three to five years where possible, reconcile earnings to normalized owner earnings, and assess incremental returns, management stewardship, and balance-sheet resilience.

Estimate owner earnings from normalized earnings attributable to owners. Add genuine noncash charges and deduct maintenance investment and operating working capital needed to maintain the business. Treat stock compensation and leases consistently. Distinguish reported CFO less total capex from normalized owner earnings. Use sector-appropriate methods for banks and insurers. For exchanges, offset customer collateral and settlement assets against their obligations. Value nonoperating assets separately only when their earnings are excluded from the forecast.

Build downside, base, and upside equity valuations. Show assumptions, the cash-flow bridge, terminal value, and sensitivity. Define margin of safety as (base intrinsic value − price) / base intrinsic value. State what the market price requires and what would change the investment conclusion.

Use the original six dimensions and weights, in this order:

1. Economics of the moat — 25
2. Owner earnings and capital efficiency — 20
3. Capital allocation and reinvestment — 15
4. Management and stewardship — 10
5. Financial resilience — 15
6. Price and margin of safety — 15

Grade each from 0 to 5 in half-point increments. The anchors are 0 demonstrable failure, 1 very weak, 2 weak, 3 adequate or mixed, 4 strong, and 5 exceptional with repeatable evidence and a credible stress test. Explain the evidence, counterevidence, and confidence for each grade. Where ordinary evidence is insufficient, use 2.5 provisionally and show the range for grades 1–4. Treat critical gaps in solvency, accounting, or the business mechanism as grounds for a provisional overall result. If a dated price is unavailable, use a provisional 2.5 for price and show the full 0–5 impact.

Use weight × grade / 5 for each contribution. Sum before rounding, round half up once, and floor the result at 1. Use the Berkshire skill’s star bands:

- 1–39: ★☆☆☆☆
- 40–54: ★★☆☆☆
- 55–69: ★★★☆☆
- 70–84: ★★★★☆
- 85–100: ★★★★★

Give the 1–100 score, visual stars, and one-page executive summary first. Put the detailed scorecard, calculation, and sources in supporting analysis. Attribute the business principles to the letters and label the scoring weights and valuation inputs as conventions of this skill.

## 3. Reproduce the dated IEX example

Analyze Indian Energy Exchange Limited, NSE: IEX and BSE: 540750, as of 20 November 2026 using the 19 November official BSE close of ₹115.20. Reconcile the quote using ISIN INE022Q01020. Verify the FY26 annual report, H1 and Q2 FY27 filings, and CERC’s draft and current regulations as of that cutoff. Keep later information separate from the historical case.

Explain the asset-light exchange model, the value of concentrated liquidity and embedded customer workflows, and how CERC’s proposed shared price discovery could change IEX’s retention and fees. Separate transaction fees from the market price of electricity. Account for client settlement balances before estimating surplus liquidity, and treat the Indian Gas Exchange stake separately.

Reproduce and audit these historical benchmarks:

- Trailing core pretax income of ₹516.59 crore, after excluding other income and associate earnings. Apply a 25% normalized cash tax rate. Add ₹24.33 crore depreciation and amortization. Deduct ₹20 crore maintenance capex, ₹5 crore lease principal, and ₹7 crore for working capital and growth investment. Starting core owner earnings are approximately ₹380 crore.
- Use five forward years of equity cash flow, a 12.5% discount rate, 4.5% terminal growth, ₹1,000 crore estimated surplus assets, ₹200 crore assumed IGX stake value, and 89.0895 crore model shares. Explain these historical inputs and how they differ from any other share-count or balance-sheet convention.
- Grow core owner earnings by 6% in the downside case, 10% in the base case, and 14% in the upside case. Apply a permanent cut from year three onward of 42%, 20%, and 2%, respectively. Tie the cuts to coupled segment exposure and volume × fee retention. Treat the timing and retention rates as assumptions.
- Expected valuation benchmarks are ₹51.13 downside, ₹70.91 base, and ₹93.74 upside per share. The base margin of safety is approximately −62.5% at ₹115.20. The same base assumptions imply starting core owner earnings of roughly ₹673 crore at the quoted price. Show sensitivities to discount rate and coupling impact.
- Grades in rubric order: 2.5, 4.5, 3.5, 3.5, 4.5, 1.0. Contributions: 12.5, 18, 10.5, 7, 13.5, 3. Total 64.5 before rounding, yielding 65/100 · ★★★☆☆.

Recalculate the benchmarks and explain any material difference. Produce editable Markdown, a printable one-page PDF, and detailed supporting analysis for my working copy. Render and inspect the PDF. Include the dated one-page Markdown example with both ratings in the public skill.

## 4. Install, audit privacy, and publish to GitHub

Publish to the existing public repository https://github.com/godspeaksmoney/ai-skills under Claude/skills/berkshire-business-analysis/. Add or update the relevant listing in the root README while preserving its existing tool sections and sibling skills.

Verify my GitHub identity, repository access, and publishing permissions. Guide me through authorized sign-in if necessary. Use minimal access and GitHub’s no-reply author email for local Git commits.

Build the public package from an explicit list of approved files. Scan filenames, text, source links, manifests, staged changes, and document metadata for personal names and contact details, local paths, usernames, private project names or links, credentials, and tokens. Publish original notes, source links, necessary scripts, and the dated one-page Markdown example. Keep source documents, temporary extracts, the detailed IEX valuation, PDF, credentials, and private automation instructions in the working environment. Include an MIT license for original skill material and credit the linked rights holders.

Add a skill README and CHANGELOG.md. Document how to download the entire folder, copy it into .claude/skills/berkshire-business-analysis, and invoke /berkshire-business-analysis. Offer a ZIP with the skill folder at its root for Claude’s custom-skill upload where available. Include prerequisites, a sample prompt, scoring interpretation, source coverage, and update instructions. Test a fresh installation using only the public package.

## 5. Configure and verify automatic updates

Set a durable monthly intake for the first of each month at 10:00 a.m. Asia/Kolkata. If the scheduler uses five-field UTC cron, use 30 4 1 * *. Verify the timezone, saved schedule, next run, and publishing access from the scheduled environment. Preserve the existing ChatGPT automation.

On each run, check Buffett’s and Abel’s official letter indices and the latest annual report. Verify and study additions or substantive revisions. Update the note, manifest, coverage, method, and documentation as applicable. Reconcile pending items. Publish validated changes and a changelog entry in one commit, within the authorized Claude folder and catalog entry. Apply the same publishing step to validated manual skill updates. A clean no-change run creates no commit.

Respect branch protections and detect overlapping edits. Use automatic merge only where authorized and supported after validation. If approval or a pull request is required, report the exact remaining step. Preserve verified local work on failure and make retries safe. Test a live no-change run and simulate a new letter, source failure, private-data detection, and conflicting remote changes in a disposable environment.

Return the public links, tested install instructions, archive coverage and gaps, IEX score and one-page example, and the schedule and next run. Distinguish configured, manually tested, and successfully run on schedule.
