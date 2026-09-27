# JEV API reference (via OpenRouter)

Source: OpenRouter's Jev community docs (openrouter.ai/docs/guides/community/jev, jev-tutorial, and the typesafe/jev-1.13 model page), fetched 2026-09-27. TypeSafe has not published an official architecture paper — this is OpenRouter's documentation of the hosted model, not a spec TypeSafe wrote themselves.

## Endpoint

```
POST https://openrouter.ai/api/alpha/decisions
Authorization: Bearer $OPENROUTER_API_KEY
Content-Type: application/json
```

A second, TypeSafe-SDK-compatible surface exists at `https://openrouter.ai/api/v1/systemone` — same auth, same billing. Prefer `/api/alpha/decisions` (Decisions API) unless you're porting code already written against TypeSafe's own SDK.

Model IDs: `typesafe/jev-1.13` (pinned) or `~typesafe/jev-latest` (alias, moves under you — pin the version for anything reproducible).

## Pricing

- Input: $0.042 / million tokens
- Output: $0 (JEV emits no output tokens by design — it reads logits, doesn't generate)
- Context window: ~32,000 tokens for `state` + all `questions` combined. This is much smaller than local clones like Rizzo Flow (1M) — batch carefully, don't dump entire files as state without checking size.

## Request shape

```json
{
  "model": "typesafe/jev-1.13",
  "state": "My invoice shows duplicate charges for Pro plan.",
  "questions": {
    "team": {
      "type": "choice",
      "instructions": "Which team should handle this?",
      "criteria": {
        "billing": "Charges and refunds",
        "technical": "Bugs and outages",
        "account": "Login and profile"
      }
    }
  }
}
```

- `state`: string, or an object/array of structured fields — whatever text/JSON the model needs to see. Counts against the 32k context.
- Optional: `session_id`, `user` (both ≤256 chars), `trace` (`trace_id`, `span_name`…), `provider` (OpenRouter routing prefs). Not needed for normal use.
- `noul.criteria` is documented as required (`true` + `false`) but verified live that omitting it still works — include it when the boundary is fuzzy.

Not this API: `typesafe/jev-router` is a separate chat-completions model that picks an external LLM and answers the prompt itself (tested: routed to a Gemini model, ~$0.003/call). Useless inside Claude Code.
- `questions`: an object keyed by whatever name you want (becomes the key in the response's `answers`). Multiple questions in one request run in parallel against the same cached `state` — always batch instead of making N calls.

### Question types

**`noul`** — boolean-shaped. (Yes, spelled `noul`, not `bool` — this is TypeSafe's own name for the primitive; expect it, don't "fix" it to `boolean` in a raw request or the API will reject the field.)
```json
{
  "type": "noul",
  "instructions": "Is the customer reporting a software defect?",
  "criteria": {
    "true": "The customer describes broken or unexpected product behavior.",
    "false": "The customer is asking a question or requesting a feature."
  }
}
```
Response: `"noul": 0.96` — probability the proposition is true. `criteria` is optional but improves calibration; give it when the true/false boundary is fuzzy.

**`choice`** — pick one of N named options.
```json
{
  "type": "choice",
  "instructions": "Which one of these options?",
  "criteria": {
    "billing": "Charges and refunds",
    "technical": "Bugs and outages",
    "other": "Anything else"
  }
}
```
Response: chosen key, plus `probabilities` (map of every option → probability) and `confidence`. Community reports suggest up to ~255 options are structurally supported, but this isn't in OpenRouter's docs — don't rely on more than a few dozen without testing.

**`score`** — ordered scale, returned as a probability-weighted continuous position (not just the nearest label).
```json
{
  "type": "score",
  "instructions": "How urgent is this ticket?",
  "criteria": [
    "Can wait for the next release",
    "Should be fixed this week",
    "Blocking revenue right now"
  ]
}
```
Response: `"score": 1.99` (position on the 0..N-1 scale, e.g. between "should be fixed this week" and "blocking revenue") plus `probabilities` per level, a `legend` mapping index → your label, and `confidence`.

Verified live 2026-09-27: `noul` responses contain only `noul` (no `confidence` field); `choice` and `score` include `confidence`.

## Response shape

```json
{
  "model": "typesafe/jev-1.13-20260917",
  "answers": {
    "team": {
      "type": "choice",
      "choice": "billing",
      "probabilities": {"technical": 0, "account": 0, "billing": 1},
      "confidence": 1
    }
  },
  "usage": {"input_tokens": 357, "output_tokens": 38, "cost": 0.000014994},
  "id": "gen-dec-...",
  "provider": "TypeSafe"
}
```

`usage.output_tokens` being nonzero in this example is billing-internal bookkeeping, not billed cost — output is $0 regardless (see pricing above). Always check `usage.cost` if tracking spend.

## Calibration and known failure modes (don't skip this)

Independent testers (not TypeSafe's own marketing) found:

- **"Zero hallucinations" is a marketing claim, not a technical fact.** JEV cannot invent an option outside your `criteria` — that's the real guarantee — but it absolutely can pick the *wrong* option from your list with high confidence. It is a calibrated statistical classifier, not an oracle.
- **Add an explicit "I don't know" / "insufficient evidence" option** to `choice` and `score` criteria whenever the state might not contain the answer (e.g. asking about a fact the model can't know). Without it, JEV was observed picking a wrong answer with 70-90%+ confidence on questions it had no basis to answer (e.g. guessing a person's age from an unrelated bio). With the option added, it correctly abstains ~90% of the time on genuinely unanswerable questions.
- **Confidence is a probability, not certainty** — rerunning the identical request can shift confidence a few points (e.g. 96% → 98% → 95%) run to run. Don't treat a single confidence value as exact; treat values near a decision boundary (e.g. 45-55% on a binary) as "uncertain" and escalate to a human or a full LLM call rather than trusting the raw threshold.
- **Order/position bias in `choice`**: when testing or generating training-adjacent prompts, vary the order of options — some open reimplementations found the model biased toward earlier-listed options when the state was ambiguous.

## Practical integration notes for Claude Code

- Batch every question about one `state` into a single request (parallel answers, one round trip, one input-token charge).
- For loops over many items (e.g. classifying 500 files), call once per item but keep `state` minimal — only the fields JEV needs, not the whole file — to stay well under 32k tokens and keep cost near-zero.
- Pin `typesafe/jev-1.13` for anything you want reproducible; `~typesafe/jev-latest` can change model version under you.
- Missing/invalid `OPENROUTER_API_KEY` → the API returns an auth error (401/403 depending on OpenRouter's gateway) — surface it clearly, don't silently fall back to guessing.
