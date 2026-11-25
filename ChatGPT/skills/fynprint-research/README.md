# The Fynprint Research

A Codex skill for answering investment research questions from your own copies of *The Fynprint*. It helps trace an answer to an issue and PDF page, compare changing coverage across editions, and study new issues without losing incomplete updates.

This package contains reusable instructions. Supply your own authorized magazine PDFs and reading notes. The magazine archive, private research notes, hosted agent, credentials and scheduled task are separate from this package.

## Install in a Codex project

Download or clone this repository. Copy the entire `ChatGPT/skills/fynprint-research` folder into your project's `.agents/skills/` directory. Open the project in a new Codex chat and invoke `$fynprint-research`.

Keep your magazine archive and notes in a location Codex can access. Tell it where they are; there are no personal filesystem paths to configure in the skill.

## Try it

- `Use $fynprint-research to answer this question from my magazine archive. Cite the issue date and PDF pages, and identify anything that needs current verification.`
- `Use $fynprint-research to compare how two editions describe the same outbound fund. Check share class, fees, currency, tax basis and measurement dates before comparing returns.`
- `Use $fynprint-research to study the new issue I saved, including every chart and table. Update my reading notes and report which requested destinations have been verified.`

See the [intake procedure](references/intake.md) for complete-page review, durable progress records and retry verification. Scheduling and private Site connections require configuration for your own environment; installing the skill does not create either.

## Attribution and reuse

An independent research workflow for readers of [The Fynprint](https://thefynprint.com/). It is not affiliated with or endorsed by the publisher. Magazine text, artwork and other publisher materials belong to their respective rights holders.

The original skill instructions were written for this repository. The authors reserve rights in those materials. Publication of the workflow does not grant rights to reproduce or distribute magazine content.
