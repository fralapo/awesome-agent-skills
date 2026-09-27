---
name: jev
description: Use the real JEV model (TypeSafe's System One decision model) via OpenRouter for fast, cheap, typed decisions — boolean/noul, choice, score — instead of burning a full LLM turn on classification, routing, filtering, or triage. Trigger whenever a task reduces to "yes/no", "pick one of N", or "rate on a scale" over some text/state: ticket routing, content moderation gates, file/document triage, resume screening, sentiment scoring, tool/skill selection, web-scrape link picking, context-pruning decisions, guardrail checks. NOT for text generation, summarization, free-form extraction, or multi-step reasoning — JEV can only answer with a boolean, one of a fixed list, or a number on a scale.
---

# JEV via OpenRouter

JEV is not a chatbot. It answers exactly one of three shapes: `noul` (boolean probability), `choice` (pick one option from a fixed list), `score` (position on an ordered scale). No output tokens, no free text. Model: `typesafe/jev-1.13` on OpenRouter, $0.042/M input tokens, output free, ~32k token context.

Use it as a **tool Claude Code calls**, not as a replacement for reasoning. The pattern: Claude (system 2) decides *what* to ask and *why*; JEV (system 1) answers *fast* and *cheap*.

## When to reach for it

- Routing: which subagent/skill/tool should handle this request
- Triage/classification: ticket severity, file type, invoice vs not-invoice, spam vs not
- Filtering a large batch: "which of these 500 files are candidates for X" (loop calls, or batch via multiple `questions` per state)
- Guardrail gate: does this input look like a prompt injection / policy violation, yes or no
- Scoring: urgency, sentiment, confidence, relevance, on a defined scale
- Pruning agent context: keep/drop a text block

If the task needs generated prose, code, or an answer outside a fixed set — don't use JEV, just answer directly.

## Setup

Requires `OPENROUTER_API_KEY` in the environment. Check first:

```
echo $OPENROUTER_API_KEY   # bash
$env:OPENROUTER_API_KEY    # powershell
```

If unset, ask the user for it before proceeding — never hardcode a key in scripts or commit it.

## How to call it

Use `scripts/jev_client.py` from this skill's folder (stdlib only, no deps, works from any cwd). Below, `<skill-dir>` means this skill's base directory — the one shown when the skill loads (plugin install: inside the plugin cache; manual install: `~/.claude/skills/jev`). Always use the absolute path.

If the base directory isn't shown or the script isn't there, find it instead of guessing (newest install wins):
```bash
ls -d ~/.claude/plugins/cache/*/*/*/skills/jev/scripts/jev_client.py ~/.claude/skills/jev/scripts/jev_client.py 2>/dev/null | sort -V | tail -1
```
```powershell
(Get-ChildItem "$HOME/.claude/plugins/cache","$HOME/.claude/skills" -Recurse -Filter jev_client.py -ErrorAction SilentlyContinue | Sort-Object LastWriteTime | Select-Object -Last 1).FullName
```

Three ways to call it:

**Inline, one-off:**
```bash
python "<skill-dir>/scripts/jev_client.py" --state "Customer: my Stripe connection keeps failing after 3 days" \
  --noul urgent="Is human intervention needed right now?" \
  --choice team="Which team handles this?:technical,billing,sales,other"
```

**From a JSON file or stdin** (preferred for anything with criteria descriptions or multiple questions — see `references/api.md` for the full schema):
```bash
python "<skill-dir>/scripts/jev_client.py" request.json
cat request.json | python "<skill-dir>/scripts/jev_client.py" -
```

**Bulk (many items, different states)** — write one request per line to a `.jsonl` file; runs in parallel (default 8 workers, `-w N` to change), prints one result per line in input order. A failed item prints `{"error": ...}` without stopping the rest. Transient 429/5xx/network errors retry automatically with backoff.
```bash
python "<skill-dir>/scripts/jev_client.py" items.jsonl -w 16
```
Measured: 12 tickets classified in ~1.6s wall total, $0.00018.

Write request files to the session scratchpad, not the user's project.

For Python-side batch loops, import it directly instead of shelling out per item:
```python
import sys; sys.path.insert(0, "<skill-dir>/scripts")
from jev_client import decide
decide(state, questions)  # returns parsed JSON dict, raises JevError
decide_many([{"state": s, "questions": q}, ...], workers=8)  # parallel, per-item {"error"} on failure
```

## Ready-made patterns

Read `references/patterns.md` for the exact request shape and how to act on each answer:

1. Rerank search/research results before fetching (fetch only the top few)
2. Pick the next element in browser automation (+ irreversibility check)
3. Review a diff before commit (plain rules first, then risk per hunk)
4. Triage failing tests / logs (real bug vs flaky vs environment…)
5. Verify citations after research (claim vs fetched source)
6. Screen external content for prompt injection / exfiltration
7. Triage PR review comments (must-fix / nit / question / outdated)
8. Find duplicates (pre-filtered pairs only)
9. Organize files into folders (propose, user confirms, never auto-move)

## Question-writing rules (from TypeSafe's official skill + cookbooks)

- One narrow judgment per question; put several independent questions about the same state in ONE request (13 batched ≈ 12× cheaper, 10× faster than 13 calls).
- Put structured context in `state` as named JSON fields and reference them in instructions with backticked paths, e.g. `ticket.messages[0].text`.
- Always include a no-match option (`none`/`unknown`) when nothing may fit. JEV can't pick a value you didn't list.
- Never ask JEV to count or do math: ask one `noul` per item and sum probabilities in code.
- For ranking with several criteria: ask each criterion as its own `score` once, apply weights in code — reweight later without re-calling.
- Don't use JEV for things code does exactly: known rules, lookups, arithmetic.

Always batch every question you need about the same `state` into ONE request — JEV answers all questions in parallel in a single call, which is both faster and cheaper than N separate calls.

## Reading the answer

- `noul` type → response has a probability 0–1 that the proposition is true. Don't hard-threshold at 0.5 for anything consequential; read `references/api.md` on calibration and adding an explicit "I don't know" option to `choice`/`score` criteria to avoid confident-but-wrong answers on out-of-distribution input.
- `choice` type → response has the chosen option plus a probability distribution over all options and a `confidence` score.
- `score` type → response has a probability-weighted position on the scale plus per-level probabilities.

Full field-level schema, request/response examples, and known limitations are in `references/api.md` — read it before hand-writing a raw request.

## What NOT to build

Don't reimplement a local model (that's what Rizzo Flow / SemIf / other open clones are for — different tool, different tradeoff: this skill talks to the real hosted JEV over the network). Don't add retries/caching/queueing beyond what `jev_client.py` already does unless the task actually needs it.
