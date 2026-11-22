// news-image-20261121 — copies the generated poster (entry.png) to the
// make.fun output directory. Node 22 standard library only.
import { copyFileSync, existsSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const src = join(here, "entry.png");

if (!existsSync(src)) {
  console.error("entry.png not found next to main.ts");
  process.exit(1);
}

const size = statSync(src).size;
const ONE_MIB = 1024 * 1024;
if (size > ONE_MIB) {
  console.error(`entry.png is ${size} bytes, over the 1 MiB limit`);
  process.exit(1);
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
const dest = join(outDir, "entry.png");
copyFileSync(src, dest);
console.log(`wrote ${dest} (${size} bytes)`);
