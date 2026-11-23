# Mauboussin Research

Analyze a listed business using Michael J. Mauboussin's research on competitive advantage, return on invested capital, capital allocation, base rates, and expectations investing. The skill produces an investment score from 1 to 100, a five-star visual rating, a one-page executive summary, and supporting analysis.

## Install in a Codex project

1. Download the GitHub repository with **Code → Download ZIP**, or clone it.
2. Find the folder at **ChatGPT/skills/mauboussin-research**. Copy that whole folder into your project at **.agents/skills/mauboussin-research**. Keep the scripts and references alongside the skill instructions.
3. Open the destination project in Codex and invoke the skill:

   > Use $mauboussin-research to assess Indian Energy Exchange Limited (NSE: IEX) at its latest verified closing price. Give me the 1–100 score, visual star rating, and one-page executive summary. Explain what the price implies and which facts would change the result.

If the skill does not appear in the selector, restart Codex. Other tools that support Agent Skills can use the same folder in their own skills directory. [OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills)

To update your installation, pull or download the latest repository version and copy the full skill folder again. Review the [changelog](CHANGELOG.md) if you have made local changes.

## How the analysis works

- Start with the issuer, date, and observed price. Use dated company, exchange, and regulator sources for facts that can change.
- Compare the firm's economics, moat, reinvestment opportunities, capital allocation, resilience, and valuation using the [rubric](references/scoring.md).
- Model downside, base, and upside cases and state the estimates and assumptions that drive the scores.
- See the [dated IEX worked example](references/iex-executive-summary.md) for the summary format. Its November 2026 assumptions illustrate a historical setup.

## Research coverage

The archive contains **183 reviewed entries** out of **183 indexed** as of **2026-11-20**. The [index](references/archive-index.md) links to a note and original source for each baseline entry. See the [manifest](references/manifest.json) for coverage limits and the [synthesis](references/research-synthesis.md) for methods by topic.

Company analysis can use the included notes directly. The optional [archive intake](references/intake.md) requires Python 3 and network access. Optional local PDF extraction also requires the pypdf package.

## Attribution and license

The skill is an independent implementation based on [Michael J. Mauboussin's Research archive](https://www.michaelmauboussin.com/#writing), including papers credited to his coauthors. The scoring rubric is an implementation choice. The [MIT license](LICENSE) applies to the original skill instructions, study notes, and code in this folder. Linked papers and publisher exhibits retain their respective rights.
