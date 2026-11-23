// Meme Sprint 3: AI Agent Goes Rogue — entrypoint.
//
// Copies the pre-rendered meme (entry.png, committed beside this file)
// to the grader's output directory. Node standard library only; no
// network, no shelling out, no runtime image generation.
import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const source = join(here, "entry.png");

if (!existsSync(source)) {
  throw new Error(`entry.png not found next to main.ts (${here})`);
}

mkdirSync(outDir, { recursive: true });
copyFileSync(source, join(outDir, "entry.png"));
