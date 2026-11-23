# Mauboussin Research — Claude skill

A Claude skill built on the 183 entries in the Research tab of [Michael J. Mauboussin's archive](https://www.michaelmauboussin.com/#writing), reconciled with the live site on 23 November 2026.

## What it produces

- **Research answers** that cite individual papers through the [archive index](references/archive-index.md), with one original study note per paper, and comparisons between editions where they matter.
- **Investment analysis** of a business: a 1–100 score, a one-to-five-star rating, and a one-page executive summary backed by a scenario DCF, a market-implied hurdle and dated evidence. See the [Indian Energy Exchange example](references/iex-executive-summary.md) (60/100 · ★★★☆☆, dated 20 November 2026).
- **Library maintenance** for new or revised papers: reconcile the live list, study the additions, then update the notes, [manifest](references/manifest.json), index and [synthesis](references/research-synthesis.md).

## Install

Download or clone the **complete** `mauboussin-research` folder. The skill needs its `references/` and `scripts/` folders.

```bash
git clone --depth 1 https://github.com/godspeaksmoney/ai-skills.git
# the skill is at ai-skills/Claude/skills/mauboussin-research
```

**Claude Code (one project):** copy the folder to `.claude/skills/mauboussin-research` in that project.

```bash
mkdir -p .claude/skills
cp -R ai-skills/Claude/skills/mauboussin-research .claude/skills/
```

Invoke it with `/mauboussin-research`, or just ask. Claude also loads it automatically when a request matches. To make it available in every project, copy it to `~/.claude/skills/mauboussin-research` instead.

**Claude apps (custom skill upload):** download [`mauboussin-research.zip`](https://github.com/godspeaksmoney/ai-skills/raw/main/Claude/skills/mauboussin-research.zip) (stored next to the folder in the repository), or build it yourself from the folder above with `zip -r mauboussin-research.zip mauboussin-research`. The ZIP must contain the `mauboussin-research/` folder at its top level. In Claude, go to **Customize → Skills → + → Create skill → Upload a skill** and choose the ZIP. Uploaded skills require code execution to be enabled. On Team or Enterprise plans an owner may need to enable skills first.

## Requirements

- No dependencies for answering questions or analysing companies; the notes and references are self-contained.
- Python 3.9+ (standard library only) for `scripts/score.py`, `scenario_dcf.py`, `research_intake.py`, `validate.py` and `privacy_scan.py`.
- Web access for current prices, filings and regulatory records, and for monthly intake.

## Sample prompts

- "Using the Mauboussin research skill, explain how to estimate a competitive advantage period, and cite the 1997 and 2026 papers."
- "How do the two editions of the Base Rate Book sales-growth report differ?"
- "/mauboussin-research Analyze Costco as an investment as of today's close. Give me the score, stars and a one-page summary."
- "Check the Research tab for new papers and update the library."

## Updating

Pull the latest version and replace the whole folder (`git pull`, then copy again), or re-upload the new ZIP. The library is refreshed monthly. [CHANGELOG.md](CHANGELOG.md) lists the changes, and [intake](references/intake.md) describes the procedure.

## Attribution and license

All research belongs to Michael J. Mauboussin and his coauthors (including Dan Callahan, Darius Majd, Kristen Bartholdson, Alexander Schay, Bob Hiler, Stephen Kawaja and others credited in the manifest) and to their publishers. This skill contains original paraphrases and links to the primary sources. It does not reproduce the papers. The scoring weights, grades, scenario probabilities and the IEX example are the skill's own and are not attributable to the authors. The skill is not affiliated with or endorsed by the authors or their employers, and it is not investment advice.

The original skill material is released under the MIT License (see [LICENSE](LICENSE)). The license does not cover the linked research.
