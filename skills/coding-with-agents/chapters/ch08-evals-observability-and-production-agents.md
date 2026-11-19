# Chapter 08: Evals, Observability and Production Agents

## Core Idea
An agent is a non-deterministic product. Without an evaluation set every change is a guess; without traces, failures are invisible; without bounded permissions, the first unlucky run becomes the incident. Most of this is established engineering practice adapted to stochastic output. Judge-based evaluation is contested, so the rules below are the conservative version.

Facts vs positions: judges need calibration against labelled human cases (a method fact); "evals are the real intellectual property of an AI product" is a position.

## 1. Designing the Eval from the Outcome
- Start from the failure that matters: a wrong refund, a leaked record, an unnecessary escalation. Generic scores (groundedness, a one-to-ten rating) rarely say what to fix.
- Prefer **binary, task-specific criteria** with a short reason. Numeric scores tend to collapse onto a few values.
- Climb a ladder: deterministic checks first (format, query runs, tests pass), then a rubric judge only for what code cannot check, then human review of a sample.
- **Grade each stage.** Tool choice, arguments, use of results and the final state fail differently. A parsing error at step two shows up as a wrong answer at step nine.
- **Test the not-do.** Cases where the agent must refuse, escalate or leave a disclaimer untouched matter as much as cases where it acts.
- **A score of 100% means the eval is too easy.** Raise the difficulty until some cases fail.

## 2. Datasets
- Start with a few dozen real or realistic cases, labelled by someone who knows the domain. Write down what "good" means before labelling.
- Grow the set from production: each incident becomes a regression case, and failures are kept.
- Keep a development set you look at and a held-out set you touch rarely. Tuning against the exact test items is leakage.
- Simulated users are polite by default. Add frustrated, indecisive and adversarial personas, and measure the gap to real traffic.

## 3. Repeated Runs and Reliability
- One run is an anecdote. Run each case several times and report the distribution.
- **pass@k** (at least one of k attempts succeeds) measures capability with retries. **pass^k** (all k succeed) measures what a user meets every time. Use pass@k only where a failed attempt is cheap and detectable.
- **Reliability compounds over steps.** Illustration: if each of 100 steps succeeds independently with probability 0.99, the run succeeds about 37% of the time (0.99^100). This is arithmetic, not a measurement, and it is why a shorter path matters as much as better steps.
- Record inputs and outputs so a changed part can be replayed, and report sample sizes beside every figure.

## 4. LLM Judges: Calibration and Pitfalls
- **Calibrate before use.** Humans label a sample, you measure agreement with them, and you revise the rubric until disagreements are understood. A judge's agreement with its own repeated answers is not validation.
- Known biases: judges favour answers from their own model family, longer answers, and one position in pairwise comparison. Mitigate with a judge from another family, randomised order, and binary criteria with a reason. Pairwise comparison is often more reliable than absolute scores (a common practice position).
- Agreement near 100% with humans is a warning sign: the dataset may be too easy or the judge too lenient.
- Judges are affordable offline and on samples, not on every production request. Online, prefer deterministic signals or small classifiers.
- **Verifiers can be gamed.** An agent that can read or edit its checker can learn to pass it: editing tests, copying answers from history, special-casing inputs. Keep judges, tests and scorers outside the agent's write scope.

Contested: some hold judges are the only scalable option; others that they cannot be trusted. Use them only with calibration and a human sample.

## 5. Regression Tracking
- A release is a combination of model version, prompt, tools, harness and data. Changing any element reruns the evaluation.
- Report per category (intent, risk class, language). A stable mean can hide the collapse of one critical intent.
- Track cost and latency beside quality. Improving one axis often worsens another.
- Release gate: no regressions on critical cases, and no drop beyond a threshold fixed before the change. Raise the floor: users remember the worst cases.
- Keep a sanity set never used for tuning; hill-climbing an eval overfits it. Providers can change a model behind a stable name, so rerun when the version changes.

## 6. Tracing and Observability
- Record each run as a tree: model calls (input, output, tokens, latency), tool calls (arguments, result, status), retries, sub-agents, decisions and cost, tagged by run, user and function.
- The trace is the source of truth. A final message claiming success while a tool call lacked a required field is visible only in the trace. Inspect tool selection and results, not only the final answer.
- Keep full payloads briefly, summaries longer, and redact personal and secret data before storage.
- Implicit feedback (abandonment, re-asking, escalation) is abundant but noisy; check it against labels before trusting it.
- **Cluster failures by cause, not symptom.** Deterministic signals (an error code, a timed-out tool, a repeated phrase) direct investigation better than asking a model to find anomalies.

## 7. Failure Taxonomy
Use categories to triage. Each has a detection signal and a place where the fix belongs.

| Category | Typical signal | Fix where |
|---|---|---|
| Misread intent | answer addresses another goal | prompt, examples, clarifying question |
| Retrieval | wrong, missing or contradictory documents | index, metadata, chunking |
| Tool choice or arguments | wrong tool, missing required field | tool description, schema validation |
| Planning | skipped steps, loops | plan artifact, step budget |
| State | stale memory, outdated cached answer | write gate, invalidation |
| Silent partial completion | "done" with half the work | completion checks in code |
| Policy | action outside permission | permission layer, not the prompt |
| Infrastructure | timeouts, rate limits, retry storms | harness, budgets |
| Human-facing | tone, flattery, over-refusal | rubric, examples |

Rule: fix at the origin. A parsing error upstream is not a reasoning problem, and no prompt repairs a missing permission.

## 8. Human Oversight and Escalation
- **Autonomy ladder**: shadow mode (the agent proposes, people act, outcomes are compared), suggestion, approval per action, sampled review, then exceptions only. Move up only when measured agreement and error rates pass thresholds set in advance.
- Confidence thresholds decide between act, confirm and escalate. A model's self-reported confidence means nothing until measured against outcomes.
- **Automation bias**: after many correct outputs, reviewers approve by reflex. Sample agent-approved outcomes and show reviewers known errors now and then.
- Escalations should be rare and clear, carrying what was asked, what was tried and why the agent stopped.

Contested: some teams aim for full autonomy with exception handling; others hold that consequential decisions need a person throughout.

## 9. Security in Production
- Untrusted content (documents, pages, messages, tool descriptions, earlier memory) can carry instructions. The model does not solve prompt injection; limit the damage and verify authority in the systems the agent calls.
- Break the lethal combination (private data, untrusted input, outbound channel) for each run where possible.
- **Identity**: the agent has its own identity, separate from the person who started it, with short-lived tokens scoped to user and call. Shared API keys in environment variables are the weak pattern.
- **Secrets never enter the sandbox.** A proxy adds credentials to permitted requests; the agent sees placeholders. Egress is deny by default, and each run gets an ephemeral environment.
- **Isolation**: containers share a kernel; many teams prefer a micro-VM-class boundary for untrusted code (contested; choose by threat model). Vet, pin and scan skills, plugins and packages, since static scans miss natural-language injection.
- **Irreversible actions** (email, transfers, deletions) need a preview, a two-step commit, idempotency keys and approval. Test injected instructions in the eval set: a clean red-team report shows coverage, not safety.

## 10. Deployment and Infrastructure
- **Durable state**: persist state per step, resume after a crash without repeating model or tool calls, and replay logged steps when debugging.
- **Every wait has an end**: success, error, timeout, cancellation or a maximum number of attempts. Before retrying a timed-out action, read its state, and use idempotent operations.
- **Bounded retries** with backoff and a shared budget. Unbounded retries multiply cost.
- **Admission control**: for self-hosted inference, reject or defer work when capacity is full. Central gateways hold keys, budgets and provider fallback; a streamed answer cannot switch provider halfway.
- **Rollout**: shadow, then a small share of traffic, then full, with thresholds fixed in advance and a kill switch ready. Pin model, prompt, tools, data and harness together, with a release note for each combination.

## 11. Retrieval Quality
- Retrieval sets the ceiling. A strong model cannot use documents it never received; a sound pipeline with a modest model often beats the reverse (a common practice position).
- Fix in this order: structure-aware chunking, hybrid search (exact terms for identifiers, numbers and names; semantics for meaning), metadata filters; then reranking; then agentic loops. Evaluate end to end after each step.
- Measure recall at the depth you pass to the model. Passages in the middle are used less well, and distractors degrade answers, so remove stale and contradictory versions.
- Counts, dates and aggregations need a structured query, validated before it runs. Access filters apply before content enters the context; post-filtering loses recall.
- Numbers come from code: the model cites, code extracts and computes. Measure parsing on your own documents, since naive parsing flattens tables and invents figures.

## 12. Fine-Tuning or Prompting?
- **Order**: instructions and examples; retrieval for facts that change; tool design; an evaluation that shows the gap; then fine-tuning if behaviour, format or cost still fails.
- Fine-tuning suits behaviour, format, style, narrow skills and cost at volume. It is poor at adding current facts and can memorise documents without generalising. Each base-model change means curation and retraining again, with regression risk at every retrain.
- A small model fine-tuned on a narrow task can match a larger one on it; route easy cases there only when evals show equivalence. Data quality dominates: a small expert-verified set often beats a larger mixed one.

Contested: whether fine-tuning is the next step or a last resort. This chapter treats it as a last resort, triggered by a measured gap.

## Common Mistakes
- Judging a release by one run or one average.
- Accepting an eval score of 100%.
- Letting the agent edit its own tests.
- Trusting a judge without human labels.
- Treating a timeout as failure, or retrying a payment.

## Checklist
- [ ] Eval set built from real failures, with negative cases and a held-out split
- [ ] Deterministic checks first; judges calibrated against labelled humans
- [ ] Repeated runs; pass@k and pass^k reported by category
- [ ] Failure taxonomy used for triage; traces with cost per completed task
- [ ] Deny-by-default permissions; approvals bound to actions; kill switch
- [ ] Shadow mode and staged rollout, thresholds fixed before launch
- [ ] Every incident turned into a regression case

## Connects To
- ch07 (harness design), ch03 (verifying output), ch06 (token budgets and unattended-agent safety).
- `ai-ml-concepts` ch09 (benchmarks and reliability metrics) and ch15 (agent operations); `software-engineering-practice` ch09 for tests as the harness of agent-written code.
