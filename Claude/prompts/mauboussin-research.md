# Michael J. Mauboussin Research — Claude project prompt

Replicate my Michael J. Mauboussin research project end to end in Claude. Build and test a reusable Claude skill, study the complete Research archive, reproduce the Indian Energy Exchange worked example, publish the sanitized skill and installation documentation to GitHub, and set up and verify monthly research and publication updates.

Start with a brief execution plan, then proceed with the authorized work. Ask for my help when GitHub sign-in, account authorization, or a required approval needs my participation. Continue independent work while waiting. Report completed work, verified results, and any remaining blockers separately.

## 1. Establish the scope and workspace

The primary source is Michael J. Mauboussin’s Writing page at https://www.michaelmauboussin.com/#writing. Use the Research tab. Its verified 20 November 2026 snapshot contained 183 entries from 1995 through 2026, comprising 181 static entries and two live additions. The 183 entries are a historical reconciliation target. Check the live tab and account for any additions, corrections, or removals since that snapshot.

The existing ChatGPT release is at https://github.com/godspeaksmoney/ai-skills/tree/main/ChatGPT/skills/mauboussin-research. Use it as a baseline for the inventory, deliverables, and reproducibility checks. Consult the primary papers when recording your own review or extending a conclusion. Preserve author and coauthor credit.

Use the existing public repository https://github.com/godspeaksmoney/ai-skills. Publish the Claude edition under Claude/skills/mauboussin-research/. Add a Claude listing to the root README while preserving the existing ChatGPT section, sibling skills, and repository history. Keep the existing ChatGPT intake and publishing workflow outside the scope of changes to the Claude edition.

## 2. Study every Research entry and make coverage auditable

Reconcile the rendered Research tab against the public data it uses. The previous site combined its linked archive-data.js file with /api/writing additions and /api/archive corrections. Verify the current site behavior, apply visible corrections and hidden-entry rules, and include entries from the Research category. Keep separately listed revisions, editions, and identical titles from different years traceable.

Create a machine-readable manifest with stable IDs, original title, archive date or year, publication venue, coauthors where known, listed URL, verified source URL, review status, review date, and the note location. Where available, record PDF page count, content hash, useful page locators, and extraction or exhibit limitations. Preserve prior IDs during updates. Keep access failures and incomplete reviews visible and retryable.

Consult each primary source and write one original, source-linked study note per entry. Capture the paper’s question, argument or evidence, practical application, and material limitations. Read the supporting sections, cases, and exhibits needed to understand the result. Use PDF page positions where verified. Where extraction fails, use a public publisher copy, inspect rendered pages, or verify a matching alternate edition. Record exactly what was accessible. The prior snapshot contained 4,590 source PDF pages. Treat page counts as inventory metadata and describe the actual extent of exhibit and page-level verification.

Write a searchable archive index and a synthesis that links each analytical method back to the relevant papers. Cover competitive advantage and fade, network effects and market power, profit pools, customer economics, ROIC and incremental returns, intangibles, maintenance versus growth investment, capital allocation, valuation and reverse DCF, base rates and Bayesian updating, scenario probabilities and payoffs, and decision quality. Explain substantive differences across editions where they matter. Publish original paraphrases and source links.

Before calling the archive complete, verify unique IDs and keys, reconciled live and historical counts, one note per reviewed entry, valid note anchors, and traceable pending items. Test retrieval with a question that requires locating and citing an individual paper and a question that requires comparing editions.

## 3. Build a portable Claude skill

Create a folder named mauboussin-research with a concise SKILL.md and valid YAML name and description. Put supporting detail in relative references. Include the research synthesis, archive index, article notes, manifest, scoring rubric, intake instructions, a worked example, and any lightweight comparison or verification scripts the workflow needs. Document optional dependencies and make the core skill usable with the included notes.

Support three ordinary uses: answer a question about the research, analyze a business as an investment, and review new or revised research. For a business analysis, deliver a 1–100 investment score, a visual one-to-five-star rating, and a crisp one-page executive summary backed by the evidence and calculations.

For Claude Code, document copying the entire skill folder to .claude/skills/mauboussin-research in the destination project and invoking /mauboussin-research. For Claude’s custom-skill interface, provide a ZIP with mauboussin-research/ as its top-level folder and document how to upload it. Verify which usage paths are supported by the current Claude environment. Test the completed package in a clean project without access to my private files.

## 4. Reproduce the scoring and investment workflow

For each company, identify the issuer, security, currency, valuation date, completed trading session, and verified price. Prefer an official closing quote. If unavailable, use two timestamped corroborating sources and state the price date. Verify changing facts with current issuer filings, exchange records, and regulators. Label reported facts, management views, proposed rules, enacted rules, and analyst assumptions.

Use these six weights from the original skill:

- Current economics: 20
- Durability of competitive advantage: 25
- Profitable reinvestment: 15
- Capital allocation and governance: 10
- Financial resilience: 10
- Expectations and valuation at the observed price: 20

Grade each dimension from 0 to 5 in half-point increments. Grade 0 is materially adverse, 1 weak, 2 below average, 3 adequate or mixed-positive, 4 strong, and 5 exceptional with sustained evidence. Show the evidence and counterevidence. Calculate weighted points as weight × grade / 5. Sum before rounding, round half up to an integer, and floor the displayed score at 1.

Map 1–20 to ★☆☆☆☆, 21–40 to ★★☆☆☆, 41–60 to ★★★☆☆, 61–80 to ★★★★☆, and 81–100 to ★★★★★. The starting valuation grades for the probability-weighted value gap versus price are: below −35% = 0; −35% to below −15% = 1; −15% to below −5% = 2; −5% to below +10% = 3; +10% to below +25% = 4; +25% or more = 5. Document any adjustment for downside asymmetry or weak evidence. Show a plausible score and star range when the result sits near a threshold. Attribute the analytical methods to the papers and identify the weights, grades, and scenario probabilities as skill or analyst choices.

Trace the business mechanism from customers, competition, and pricing through incremental returns, normalized cash flow, and competitive fade. Reconcile nonoperating assets, client money, leases, dilution, and working capital where material. Use an appropriate outside view and disclose when comparable data are sparse. Build bear, base, and bull cases, show their probabilities and valuations, solve for one operating assumption implied by the observed price, and stress the most material assumptions. Name the evidence that would change the conclusion.

## 5. Reproduce the dated Indian Energy Exchange example

Use Indian Energy Exchange Limited, NSE: IEX, with an analysis date of 20 November 2026 and the 19 November NSE close of ₹115.17. Reproduce this historical case using sources available at that cutoff. Keep any later refresh clearly dated and separate.

Use IEX’s FY26 annual report, Q2 FY27 filings and earnings call, relevant exchange price records, and CERC’s draft and current regulations registers. Show how pooling bids and centralizing clearing-price discovery could affect IEX’s venue-specific liquidity advantage, market share, and realized fee. Distinguish company-wide volume growth from IEX retention, transaction fees from power clearing prices, and regulatory proposals from final rules. Document the treatment of client settlement balances, excess financial assets, and the Indian Gas Exchange holding.

Reproduce and audit these historical benchmarks:

- Grades in rubric order: 4.5, 2.5, 3.5, 3.5, 4.0, and 1.0. Weighted points: 18, 12.5, 10.5, 7, 8, and 4. Headline score: 60/100 · ★★★☆☆.
- Equity DCF uses five forward years, an 11.5% nominal INR cost of equity, 89.1692735 crore gross issued shares, and a ₹1,500 crore equity bridge consisting of ₹1,000 crore estimated excess financial assets and ₹500 crore estimated IGX stake value. These are historical model inputs.
- Year-zero model inputs in ₹ crore: 625 transaction revenue, 35 other operating revenue, 108 cash operating cost, 16 cash investment, and 25% cash tax. Grow other operating revenue, operating cost, and cash investment at 8% in each forward year. Normalize settlement working-capital changes to zero and exclude treasury income and the IGX share of profits from core cash flow.
- For each forward year, multiply cumulative market-volume growth by the relative IEX share and relative fee factors to model transaction revenue. Bear: annual market growth 10%, 10%, 9%, 8%, 7%; relative share 100%, 92%, 77%, 72%, 72%; relative fee 100%, 94%, 87%, 84%, 84%; terminal growth 4.0%. Base: market growth 12%, 12%, 11%, 10%, 9%; share 100%, 100%, 92%, 87%, 86%; fee 100%, 100%, 96%, 94%, 94%; terminal growth 5.0%. Bull: market growth 16%, 15%, 14%, 13%, 12%; share 100%, 100%, 99%, 98%, 98%; fee 100% throughout; terminal growth 5.5%.
- Approximate values per share: bear ₹61.53 at 30%, base ₹92.41 at 50%, bull ₹130.79 at 20%. Weighted value ₹90.82, about 21% below the reference close. The price implies approximately 16.6% annual market-volume growth over five years under the model’s other base-case assumptions.

Treat these as reproducibility targets. Recalculate them, document the sources and judgment calls, and explain any material difference you find. Include the dated price, ratings, thesis, decisive evidence, scenario table, market-implied hurdle, and reassessment triggers in the one-page summary. Produce an editable Markdown summary and a printable one-page PDF for my working copy. Render and visually check the PDF. Keep the detailed scorecard, formulas, sources, and valuation sensitivity in a supporting analysis. Put the dated one-page Markdown example and both ratings in the public skill so a reader can see the expected output.

## 6. Connect GitHub, check privacy, and publish

Verify the GitHub identity and repository access. Guide me through the supported GitHub connection or browser sign-in if needed. Verify that the chosen publishing path can write to the intended repository and that the scheduled environment can use it. Use the minimum practical access and a GitHub no-reply author email for local Git commits.

Build the public package from an explicit file allowlist. Scan file contents, filenames, URLs, manifests, generated artifacts, and staged changes for personal names and contact details, device usernames, absolute local paths, internal project names, private links and files, secrets, tokens, and identifying metadata. Keep private runbooks, credentials, intermediate extracts, source PDFs, and the detailed IEX working model in the working environment. Include an MIT license for the original skill material, with separate attribution for linked research.

Publish SKILL.md, references, necessary scripts, a skill README, and CHANGELOG.md under Claude/skills/mauboussin-research/. The README must explain what the skill produces, how to download or clone and install the complete folder, how to invoke it, requirements, source attribution, how to update it, and a sample prompt. Verify the final public URLs, repository paths, file set, and a fresh installation.

## 7. Set up and test monthly intake and automatic publishing

Schedule Claude’s intake for the first of every month at 9:00 a.m. Asia/Kolkata. Use a durable scheduler supported by the available environment, such as Claude Code’s cloud scheduled task or a persistent Desktop task when the workflow needs local files. If the cloud scheduler uses a five-field UTC cron expression, the equivalent is 30 3 1 * *. Verify the saved timezone and next run. Use only credentials and files the scheduled environment can actually access.

Each run must fetch and reconcile the complete Research list; catch new entries, revised links or papers, backfills, and previous unresolved items; study verified new material; and update the notes, manifest, index, synthesis, and usage documentation where affected. Preserve prior research and the dated IEX example. On a clean no-change run, exit without a commit. Use the same publishing step after validated manual changes to the Claude skill, and reconcile any unpublished validated changes during the next scheduled run.

Publish validated skill and documentation changes together with a changelog entry. Respect repository protections and detect overlapping edits. Where the authorized workflow supports it, merge automatically after checks pass. If branch permissions require a pull request or approval, verify what can actually be automated and state the remaining step. Preserve validated work on failures and make retries safe. Limit all writes to the Claude edition and the catalog entry it owns.

Test a real no-change run and simulate a new article, a substantive revision, a broken source, a detected private value, and a conflicting GitHub edit in a disposable test environment. Verify the actual scheduled publishing identity or permissions before claiming the workflow can publish unattended. Report whether the first scheduled run has occurred separately from any manual test.

## Definition of done

Return the public repository, skill, install guide, changelog, historical IEX summary, and any downloadable Claude package. Report the verified archive total, sources reviewed, any gaps and exhibit limitations, IEX score and stars, key valuation assumptions, proof of clean installation, the schedule and next run, and verified publication status. Distinguish installed, published, scheduled, manually tested, and successfully run on schedule.
