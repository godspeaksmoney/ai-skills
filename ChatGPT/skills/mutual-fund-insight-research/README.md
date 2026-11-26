# Mutual Fund Insight Research

Research a user-supplied Mutual Fund Insight archive, compare its coverage across issues, and study new issues with citations to original PDF pages.

## Install

Copy this entire folder from `ChatGPT/skills/mutual-fund-insight-research` into your project's `.agents/skills/mutual-fund-insight-research` directory. Keep the references and agent metadata together. Invoke it with:

> Use $mutual-fund-insight-research to compare what the supplied issues say about SIP returns, with issue and PDF page citations.

> Use $mutual-fund-insight-research to study this newly supplied issue cover to cover, update my archive, and report any unreadable pages.

Supply your own authorized PDFs and research library. If those sources are unavailable, the agent should explain what is missing. Update an installation by copying the latest complete folder and reviewing the [changelog](CHANGELOG.md).

## Included knowledge and coverage

The [research principles](references/research-principles.md) distill methods from the studied archive: cash-flow returns, exposure and allocation, active differentiation, factors, passive implementation, retirement assumptions, and source inconsistencies. The [intake procedure](references/intake.md) describes complete study and reliable updates.

The [coverage record](references/coverage.json) records the originating archive's reviewed issues and page counts. Revision fingerprints change when its private notes or synthesis change; they cannot be used to retrieve those notes. This package contains the reusable method and coverage metadata. Detailed reading notes, magazine PDFs, source extractions, private Site, credentials and scheduled task remain separate.

A copied skill needs its own authorized evidence to answer archive-specific questions. Installing it does not transfer the originating archive or create a Site, API access, scheduled job or GitHub connection.

## Updates and reuse

The originating installation checks for new user-saved issues monthly. Validated changes to the skill or its research trigger a checked GitHub sync; unsuccessful syncs remain pending for retry. Other installations can follow the [intake procedure](references/intake.md) with their own configured destinations.

This is an independent research workflow based on Mutual Fund Insight, published by Value Research. It is not affiliated with or endorsed by the publisher. Original publication material retains its respective rights. See [reuse terms](LICENSE).
