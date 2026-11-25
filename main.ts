// Entrypoint for the 25 November news-image entry.
//
// The front page is rendered ahead of time by draw_frontpage.py and shipped
// in this repository as entry.png. This file only puts that finished image
// where the grader looks for it. It uses nothing but Node's standard library,
// so it runs the same way in the grader's sandbox as it does here.
import { copyFileSync, existsSync, mkdirSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const sourceDir = dirname(fileURLToPath(import.meta.url));
const targetDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const source = join(sourceDir, "entry.png");
const target = join(targetDir, "entry.png");

if (!existsSync(source)) {
  throw new Error("entry.png is missing from the entry");
}
// A PNG must open with its eight-byte signature; refuse anything else
// rather than handing the grader a file it cannot read.
const magic = readFileSync(source, { flag: "r" }).subarray(0, 8);
const pngSignature = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
if (!magic.equals(pngSignature)) {
  throw new Error("entry.png does not start with a PNG signature");
}
mkdirSync(targetDir, { recursive: true });
copyFileSync(source, target);
console.log(`front page copied to ${target}`);
