import { createHash } from "node:crypto";
import { readFile, realpath } from "node:fs/promises";
import { isAbsolute, relative, resolve, sep } from "node:path";
import { pathToFileURL } from "node:url";

async function within(root, file) {
  if (isAbsolute(file)) throw new Error("Manifest paths must be relative.");
  const target = await realpath(resolve(root, file));
  const offset = relative(root, target);
  if (offset === ".." || offset.startsWith(".." + sep) || isAbsolute(offset)) {
    throw new Error("A manifest path is outside the selected archive.");
  }
  return target;
}

function hash(bytes) {
  return createHash("sha256").update(bytes).digest("hex");
}

export async function checkArchive(directory, sourceDirectory) {
  const root = await realpath(directory);
  const sourceRoot = sourceDirectory ? await realpath(sourceDirectory) : undefined;
  const manifest = JSON.parse((await readFile(resolve(root, "manifest.json"), "utf8")).replace(/^\uFEFF/, ""));
  if (!Array.isArray(manifest.issues) || !manifest.issues.length) throw new Error("The archive contains no reviewed issues.");
  const seen = new Set();
  let pages = 0;
  for (const issue of manifest.issues) {
    if (!/^\d{4}-(0[1-9]|1[0-2])$/.test(issue.id) || seen.has(issue.id)) {
      throw new Error("Invalid or duplicate issue identity.");
    }
    seen.add(issue.id);
    if (!Number.isInteger(issue.pdf_pages) || issue.pdf_pages < 1 || issue.covered_pages !== issue.pdf_pages) {
      throw new Error("Incomplete recorded coverage for " + issue.id);
    }
    const bytes = await readFile(await within(root, issue.notes));
    if (hash(bytes) !== issue.notes_sha256) throw new Error("Note hash mismatch for " + issue.id);
    const note = bytes.toString("utf8").replace(/^\uFEFF/, "");
    const sections = [...note.matchAll(/^## PDF p\. (\d+)[\t ]*\r?\n([\s\S]*?)(?=^## PDF p\. |(?![\s\S]))/gm)];
    if (sections.length !== issue.pdf_pages) throw new Error("Missing page sections for " + issue.id);
    sections.forEach(([, number, content], index) => {
      if (Number(number) !== index + 1 || !content.trim()) throw new Error("Invalid page sequence for " + issue.id);
    });
    if (sourceRoot) {
      const original = await readFile(await within(sourceRoot, issue.source));
      if (hash(original) !== issue.sha256) throw new Error("Original PDF hash mismatch for " + issue.id);
    }
    pages += issue.pdf_pages;
  }
  return { issues: seen.size, pages, originalPdfsChecked: Boolean(sourceRoot) };
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  const [, , archive, originals] = process.argv;
  if (!archive) {
    console.error("Usage: node scripts/check-archive.mjs <research-directory> [originals-root]");
    process.exitCode = 1;
  } else {
    try {
      console.log(JSON.stringify(await checkArchive(archive, originals)));
    } catch (error) {
      console.error(error.message);
      process.exitCode = 1;
    }
  }
}
