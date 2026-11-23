# Publishing the Claude edition

Use the same steps after a validated monthly intake and after validated manual changes. All writes go only to `Claude/skills/mauboussin-research/` and the Claude listing in the root `README.md`. Never touch the ChatGPT edition, the sibling skills, or the ChatGPT intake workflow.

1. **Prepare.** Clone or fetch the repository. Create a branch named `claude/mauboussin-research-YYYYMMDD` from the latest default branch. Record the base commit.
2. **Copy from an allowlist.** Copy only these into `Claude/skills/mauboussin-research/`: `SKILL.md`, `README.md`, `CHANGELOG.md`, `LICENSE`, `references/` (Markdown and `manifest.json`) and `scripts/*.py`. Exclude private runbooks, credentials, source PDFs, extracted text and detailed company models.
3. **Validate.** Run `python scripts/validate.py`, then `python scripts/privacy_scan.py Claude/skills/mauboussin-research README.md` with any private deny list. Then save the staged diff (`git diff --cached > staged.diff`), scan it with `python scripts/privacy_scan.py staged.diff`, and delete it.
4. **Detect overlapping edits.** Fetch again before pushing. If the default branch moved and touched the same paths, stop. Rebase only when the changes don't overlap, and rerun validation afterwards.
5. **Commit.** Use a GitHub no-reply author email and a message that summarises the intake. The changelog entry is included in the same commit.
6. **Merge according to repository protections.**
   - If the default branch accepts direct pushes from the authorized identity and checks pass, fast-forward merge.
   - If protections require a pull request or a review, open the pull request and report its URL. That review is the remaining manual step.
7. **Retry safely.** On any failure, leave the validated branch in place and record what failed. The next scheduled run detects unpublished validated changes, by comparing the branch with the default branch, and retries from step 4.
8. **Verify.** Confirm the public URLs and that the file set matches the allowlist.
