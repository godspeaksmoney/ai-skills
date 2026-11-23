# Scoring rubric

The six weights, the grade scale, the valuation bands and the star mapping are **choices made by this skill**, not Mauboussin's. The analytical methods behind each dimension come from the papers cited, and the scenario probabilities are the analyst's judgment. Say so in every output.

## Dimensions and weights

| # | Dimension | Weight | What earns a high grade | Methods |
|---|---|---|---|---|
| 1 | Current economics | 20 | ROIC well above the cost of capital on a consistent definition (intangibles and excess cash handled); cash conversion | [028](notes/notes-001-061.md#paper-028), [027](notes/notes-001-061.md#paper-027), [033](notes/notes-001-061.md#paper-033) |
| 2 | Durability of competitive advantage | 25 | Long, evidenced CAP; stable share; customer value the business can capture; low threat of disruption or regulatory change | [012](notes/notes-001-061.md#paper-012), [004](notes/notes-001-061.md#paper-004), [029](notes/notes-001-061.md#paper-029), [100](notes/notes-062-122.md#paper-100) |
| 3 | Profitable reinvestment | 15 | Room to reinvest at incremental returns above the cost of capital; maintenance spending separated from growth spending | [045](notes/notes-001-061.md#paper-045), [035](notes/notes-001-061.md#paper-035), [182](notes/notes-123-183.md#paper-182) |
| 4 | Capital allocation and governance | 10 | Value-based M&A, buybacks and dividends; SBC counted; aligned incentives; minority-holder protection | [007](notes/notes-001-061.md#paper-007), [092](notes/notes-062-122.md#paper-092), [023](notes/notes-001-061.md#paper-023) |
| 5 | Financial resilience | 10 | Little leverage, liquidity, few contingent claims; survives the bear case | [009](notes/notes-001-061.md#paper-009), [052](notes/notes-001-061.md#paper-052), [113](notes/notes-062-122.md#paper-113) |
| 6 | Expectations and valuation at the observed price | 20 | Probability-weighted value well above the dated price; plausible market-implied hurdle | [104](notes/notes-062-122.md#paper-104), [002](notes/notes-001-061.md#paper-002), [010](notes/notes-001-061.md#paper-010) |

## Grades

Grade each dimension from 0 to 5 in half-point steps. **0** materially adverse · **1** weak · **2** below average · **3** adequate or mixed-positive · **4** strong · **5** exceptional, with sustained evidence. For every grade, list the evidence, the counterevidence, and what would move the grade by half a point.

## Score

`weighted points = weight × grade / 5`. Sum the unrounded points, round half up to an integer, and show at least 1. `scripts/score.py` does this calculation.

| Score | Stars |
|---|---|
| 1–20 | ★☆☆☆☆ |
| 21–40 | ★★☆☆☆ |
| 41–60 | ★★★☆☆ |
| 61–80 | ★★★★☆ |
| 81–100 | ★★★★★ |

## Valuation starting grade (dimension 6)

Value gap = probability-weighted value per share ÷ price − 1.

| Gap | Starting grade |
|---|---|
| below −35% | 0 |
| −35% to below −15% | 1 |
| −15% to below −5% | 2 |
| −5% to below +10% | 3 |
| +10% to below +25% | 4 |
| +25% or more | 5 |

You may move the starting grade by up to one point for downside asymmetry (the bear-case loss relative to the bull-case gain) or for weak evidence. Document any adjustment.

## Near-threshold rule

If a ±0.5 change in any single grade would cross a star boundary, report a plausible score range and star range next to the headline. Example: 60 · ★★★☆☆ (plausible 58–63, ★★★–★★★★).

## Confidence and provisional ratings

Rate confidence as high, medium or low, based on how reliable the evidence is, how reasonable people's views vary, and how sensitive the result is to new information ([024](notes/notes-001-061.md#paper-024)). Mark the rating **provisional** when a material input is unverified, such as a missing filing, an unconfirmed price, or a rule still in draft.
