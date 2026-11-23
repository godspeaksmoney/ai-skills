# Scoring and valuation

## Score out of 100

Grade each dimension from 0 to 5 in half-point increments. Apply the same anchors across companies. A 0 reflects demonstrable failure, 1 very weak, 2 weak, 3 adequate or mixed, 4 strong, and 5 exceptional with repeatable evidence and a credible stress test. Give a short rationale and evidence confidence for each. Assign 2.5 to a dimension where missing evidence prevents a fair ordinary assessment, flag it as unverified, and calculate the range if it moved from 1 to 4. For critical missing information about solvency, accounting or the central business mechanism, label the entire score provisional and show which facts would resolve it.

| Dimension | Points | What to assess |
| --- | ---: | --- |
| Economics of the moat | 25 | Repeat customer value, evidenced competitive advantage, durability and threats to its mechanism |
| Owner earnings and capital efficiency | 20 | Normalized cash economics, unit economics, maintenance investment, return on average and incremental capital |
| Capital allocation and reinvestment | 15 | Incremental opportunity and observed returns, dividends, acquisitions, dilution and buybacks in terms of value per share |
| Management and stewardship | 10 | Execution, candor, incentives, independent oversight and succession |
| Financial resilience | 15 | Cash actually available to owners, obligations and liquidity under adverse operating scenarios |
| Price and margin of safety | 15 | Current price relative to intrinsic value across plausible scenarios and strength of the valuation evidence |

Keep moat erosion in moat and its consequences in the cash flows. The resilience grade asks whether the balance sheet can absorb the resulting cash-flow stress. Avoid duplicating penalties through discretionary adjustments.

Compute each contribution as weight × grade ÷ 5. Sum unrounded contributions, round once to the nearest integer with half points rounded up, and floor at 1. Use [the scoring script](../scripts/score.py) with grades in table order for an independent check. For example, run `python -X utf8 scripts/score.py 2.5 4.5 3.5 3.5 4.5 1` from the skill directory.

| Score | Stars | Reading |
| --- | --- | --- |
| 85–100 | ★★★★★ | Exceptional |
| 70–84 | ★★★★☆ | Strong |
| 55–69 | ★★★☆☆ | Mixed |
| 40–54 | ★★☆☆☆ | Weak |
| 1–39 | ★☆☆☆☆ | Very weak |

The price anchors use a conservative central value and the downside case. Grade 0 when the price substantially exceeds even a generous case with little support for implied assumptions. Grade 1 when price is clearly above base and near or above upside. Grade 2 when price is near base or has only a small discount and still exposes capital to substantial downside. Grade 3 when a meaningful discount to base offers some cushion, with downside still material. Grade 4 when price is near or below a well-supported downside value or has a substantial discount to a tightly supported base. Grade 5 when price is materially below a conservatively estimated downside value and thesis uncertainty is low. If a meaningful dated price is unavailable, use 2.5 provisionally and show how price can move the score across the full 0–5 range.

## Owner economics and intrinsic value

- Review three to five years where possible. Use comparable periods and consolidated statements, label attributable figures, and explain any period with changes in business perimeter or accounting. Measure operating return on average invested capital and incremental NOPAT per change in operating capital where the denominator is meaningful. If net operating capital is near zero, negative, or distorted by contra balances, disclose it and use unit economics, cash conversion and return per share alongside reported ROE.
- Start with normalized earnings attributable to owners. Add genuine noncash accounting charges, subtract sustainable maintenance capex and incremental working capital necessary to maintain competitive position and unit volume. Include stock compensation as an economic cost and handle lease cash payments consistently. Distinguish the simple CFO less total capex proxy from normalized owner earnings and quantify the uncertain adjustments. Compare the estimates against cash flow over a cycle.
- Model growth investment if it is needed to deliver forecast growth. For banks and insurers, adapt the measure to earnings distributable after provisioning and required regulatory capital. Examine insurance float's cost, duration and tail liabilities. For clearinghouses and exchanges, exclude or offset customer margin, settlement assets and restricted funds when estimating surplus capital.
- Reconcile which operating, financing and associate flows are in the forecast. Use a consistent equity or enterprise discount rate and bridge. Separately value only assets whose earnings were excluded from the cash-flow stream. Show the assumptions for growth, permanent change in earnings, terminal value and net cash or debt, and report sensitivity to material drivers. Include price and quote date, value per diluted share and margin of safety defined as (base value − price) ÷ base value. Call the range conditional and distinguish evidence from estimates.
- Use a specific contrary case. For regulated or platform businesses ask who controls prices, clearing, access, settlement, and the right to earn returns. Model regulatory changes through unit volume, realized fees and operating leverage. See Berkshire’s utility discussion in the 2010, 2023 and 2025 letters, and the competitive advantage discussion in 1991 and 2007.
