# Berkshire Hathaway Business Analysis

Apply the shareholder letters’ lessons about owner earnings, durable businesses, capital allocation, and valuation. The skill delivers a 1–100 investment score, a visual rating from one to five stars, and a one-page executive summary.

## Install in a Codex project

1. Clone this repository, or download it using **Code → Download ZIP** on GitHub.
2. Copy the entire folder **ChatGPT/skills/berkshire-business-analysis** into your project’s **.agents/skills** directory as **berkshire-business-analysis**. Keep the references and scripts with the skill.
3. Open the destination project in Codex and try this prompt.

   > Use $berkshire-business-analysis to assess a listed business at its latest verified closing price. Give me the one-page summary, 1–100 score, visual stars, and supporting assumptions. Identify what would change the rating.

If the skill does not appear in the selector, restart Codex. Other tools with Agent Skills support can use the full folder in their own skill directory. [OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills)

To update your installation, pull or download the latest repository version, review the [changelog](CHANGELOG.md), and copy the full folder again. Ordinary company analysis uses the included references directly. The optional score calculator uses Python 3. Run `python scripts/score.py --help` from the skill folder.

## How to use it

Assess the business as a long-term owner. Work through moat durability, normalized owner earnings, stewardship, capital allocation, resilience, and the margin of safety at the quoted price. The [dated Indian Energy Exchange example](references/iex-executive-summary.md) illustrates the report format and both ratings. Refresh filings, rules, and price before reassessing the company.

[Valuation and scoring guide](references/scoring.md) · [Executive summary template](references/executive-summary-template.md)

## Research coverage and attribution

This edition includes **49 annual letters covering reporting years 1977–2025**. [Year-by-year notes](references/letter-notes.md) and the [source inventory](references/letter-manifest.json) link each study to its publisher. Consult the individual source for context, material assumptions, and original wording. The [intake guide](references/intake.md) explains how the archive is maintained.

The skill is an independent implementation based on [Berkshire Hathaway shareholder letters](https://www.berkshirehathaway.com/) by Warren Buffett and Greg Abel. The scoring weights and stars belong to this skill. The [MIT license](LICENSE) covers the original skill instructions, notes, and code here. The linked publisher materials retain their respective rights.
