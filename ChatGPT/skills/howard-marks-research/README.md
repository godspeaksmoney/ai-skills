# Howard Marks Research

Apply Oaktree’s memos to price, risk, credit, cycles, and potential permanent loss. The skill delivers a 1–100 investment score, a visual rating from one to five stars, and a one-page executive summary.

## Install in a Codex project

1. Clone this repository, or download it using **Code → Download ZIP** on GitHub.
2. Copy the entire folder **ChatGPT/skills/howard-marks-research** into your project’s **.agents/skills** directory as **howard-marks-research**. Keep the references and scripts with the skill.
3. Open the destination project in Codex and try this prompt.

   > Use $howard-marks-research to assess a listed business at its latest verified closing price. Give me the one-page summary, 1–100 score, visual stars, and supporting assumptions. Identify what would change the rating.

If the skill does not appear in the selector, restart Codex. Other tools with Agent Skills support can use the full folder in their own skill directory. [OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills)

To update your installation, pull or download the latest repository version, review the [changelog](CHANGELOG.md), and copy the full folder again. Ordinary company analysis uses the included references directly. The optional archive inventory and note verifier use Python 3. Retrieving the live inventory also requires network access.

## How to use it

Start with the buyer’s implied expectations and the risks of permanent loss. Use second-level thinking, cycles, credit and liquidity evidence, and security-specific scenarios. The [dated Indian Energy Exchange example](references/iex-executive-summary.md) illustrates the report format and both ratings. Refresh filings, rules, and price before reassessing the company.

[Investment framework](references/framework.md) · [Scoring guide](references/scorecard.md)

## Research coverage and attribution

This edition includes **167 dated entries from 1990-10-12 through 2026-11-11**. [Memo coverage and period notes](references/coverage.md) and the [source inventory](references/inventory.json) link each study to its publisher. Consult the individual source for context, material assumptions, and original wording. The [intake guide](references/intake.md) explains how the archive is maintained.

The skill is an independent implementation based on [Oaktree’s memo archive](https://www.oaktreecapital.com/insights/memos) by Howard Marks and credited coauthors. The scoring weights and stars belong to this skill. The [MIT license](LICENSE) covers the original skill instructions, notes, and code here. The linked publisher materials retain their respective rights.
