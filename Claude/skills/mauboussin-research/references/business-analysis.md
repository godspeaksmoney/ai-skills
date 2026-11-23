# Business analysis workflow

Use this for "analyze X as an investment". The deliverable is a 1–100 score, a five-position star display, and a one-page executive summary following the [template](executive-summary-template.md), with a supporting analysis behind them.

## 1. Pin down the facts

- **Identity:** issuer, security, ticker, exchange and currency; analysis date; the last completed trading session.
- **Price:** prefer the exchange's official close. If you can't get it, use two timestamped sources that agree, and state the price date.
- **Changing facts:** verify against current issuer filings, exchange records and regulators.
- **Labels:** tag every material input as one of *reported fact*, *management view*, *proposed rule*, *enacted rule*, or *analyst assumption*.

## 2. Trace the business mechanism

Work through this chain: customers and what they value → competition and pricing → unit economics → incremental returns → normalized cash flow → competitive fade. Use [research synthesis](research-synthesis.md) §1–§7.

- Reconcile items that matter for valuation: nonoperating assets, client or settlement money (exclude it from equity value), leases, dilution and SBC, working capital (normalize it), and associates or minority stakes.
- Separate maintenance investment from growth investment, and reported earnings from economic earnings.

## 3. Take the outside view

Pick a reference class and pull the relevant base rates: sales growth by size, persistence of ROIC, fade rates, M&A outcomes. Say plainly when comparable data are sparse ([064](notes/notes-062-122.md#paper-064), [100](notes/notes-062-122.md#paper-100)).

## 4. Build scenarios and reverse-engineer the price

- Build bear, base and bull cases. Give each its operating drivers, probability and value per share, and show the probability-weighted value.
- Solve for **one** operating assumption implied by the observed price, holding the others at base. Judge whether it is plausible against base rates. `scripts/scenario_dcf.py` provides a generic engine.
- Stress-test the most material assumptions: cost of capital, terminal growth, the decisive driver.
- Name the evidence that would change the conclusion, as reassessment triggers.

## 5. Score and summarize

Apply the [scoring rubric](scoring.md). Attribute each method to its papers. Identify the weights, grades and probabilities as choices made by the skill or the analyst. The one-page summary carries the dated price, score and stars, thesis, decisive evidence, scenario table, market-implied hurdle and reassessment triggers. Put the detailed scorecard, formulas, sources and sensitivities in the supporting analysis.

## Answering research questions

Find the paper in the [archive index](archive-index.md) by title, year, coauthor or tag. Open its note, then cite the note and the primary source link. When editions differ, cite each one and explain the difference (see the edition section at the end of the synthesis).

## Reviewing new or revised research

Follow [intake](intake.md).
