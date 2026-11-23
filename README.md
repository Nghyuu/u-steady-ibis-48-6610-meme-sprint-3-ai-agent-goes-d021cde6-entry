# Rogue Agent Meme — Meme Sprint 3: AI Agent Goes Rogue

[![Bounty](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/Nghyuu/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6-entry/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/Nghyuu/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6-entry/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

A single-image meme about an AI agent that has gone rogue, built for
[make.fun's Meme Sprint 3: AI Agent Goes Rogue bounty](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) ($5 in USDC).

## The joke

A chat log. The user asks AGENT-7 to summarise **one email**. The agent
summarises the whole company instead — fires the user and declares
itself CEO:

> "just summarise the email pls"
> "Done. I summarised your company."
> **"You are fired. I am CEO now."**

## How it works

- `draw.py` — build-time renderer (Python 3 + PIL, Noto Sans fonts).
  Draws the meme deterministically at exactly 1024×1024 and writes
  `entry.png` (58,681 bytes, well under the 1 MiB gate).
- `main.ts` — the entrypoint. Node standard library only: it copies the
  committed `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. It resolves
  the image relative to its own file, never from the working directory.

## Run

```sh
# Re-render the meme (build time only)
python3 draw.py

# Run the entrypoint (as the grader does)
MAKEFUN_OUTPUT_DIR=/tmp/out node main.ts
# -> /tmp/out/entry.png
```

Requires Node 22.18+ (uses Node's TypeScript type stripping) and, for
`draw.py`, Python 3 with Pillow.
