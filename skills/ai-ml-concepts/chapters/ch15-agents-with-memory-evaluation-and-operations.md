# Chapter 15: Agents with Memory, Evaluation and Operations

## Core Idea
A model call has no state; an agent is a loop of calls with tools, context and, if you build it, memory. This chapter treats the concepts behind building such a loop that remembers, can be tested and survives failure. In this model, three questions dominate: what is kept between steps and sessions (memory), how you know the agent works (evaluation), and how you keep it from causing harm or losing work (operations). Concrete product design belongs to `software-architecture`; practice of coding with agents belongs to `coding-with-agents`. Vendor claims are marked as such.

## 15.1 The autonomy ladder and the cost of error
- **Thesis**: risk grows with each step from answering to acting.
- **Mechanism**: a chatbot answers from knowledge; a co-pilot uses tools but waits for a human to send; an action agent sends the message, changes the database or pays. Impact rises with autonomy, and so does the cost of a mistake. High-value, high-cost-of-error workflows (underwriting, compliance review) are the hardest to adopt.
- **Trade-off**: value from autonomy against irreversibility.
- **Does not hold when**: actions are reversible and cheap; then more autonomy is affordable.

## 15.2 Agents are stateless; context is what you load
- **Thesis**: whatever the agent must know at the start of a session has to be written into its context or fetched.
- **Mechanism**: nothing persists between calls except the text supplied; long sessions suffer context decay, and very long contexts degrade reasoning on hard tasks ("context rot", a developer's report), so loading the right information matters more than loading all of it.
- **Trade-off**: more context, more cost and more distraction.
- **Does not hold when**: the task is short and self-contained.

## 15.3 Human memory types mapped to agent memory
- **Thesis**: borrowing the categories helps decide what to store and how.
- **Mechanism**: short-term and working memory is the recent conversation and intermediate results in the context window. Long-term memory splits into semantic (facts: weights plus external knowledge sources), episodic (past events: logged action sequences and outcomes, replayed as examples) and procedural (how to do things: system prompt and rules). Sensory memory has no direct counterpart in text-only agents.
- **Trade-off**: a clear design vocabulary against the risk of over-literal analogy.
- **Does not hold when**: a single store serves several purposes without distinguishing them; reconciliation then gets messy.

## 15.4 Creating, persisting and updating memories
- **Thesis**: a memory is a distilled insight, not a raw trace.
- **Mechanism**: raw material includes reasoning traces, tool results, conversations and environment feedback; the agent extracts what is reusable (character traits in a simulation, successful or failing action sequences, expert instructions, errors with their fixes) and writes it to an external store, because context memories vanish between sessions. Timing options: on every input, when the context nears full, every N turns, on a condition, or by the model's own judgement (models have decent intuition for when to create, retrieve and update). Each memory operation is an extra step with added latency. Records need timestamps for recency filtering, one source of truth per entity or procedure that is updated as facts change, and periodic reconciliation and compaction to avoid unbounded growth. Deletion and conflict rules (does the newer fact replace the older, or does the older remain as history?) are part of the design, and the answer depends on the prompt.
- **Trade-off**: distillation loses detail; keeping everything is a log, not a memory.
- **Does not hold when**: you need an audit trail: keep logs in addition and treat memory as the working summary.

## 15.5 Retrieving memories
- **Thesis**: retrieve at the right moment with the right method.
- **Mechanism**: when: before every action in a simulated world; at planning time for computer-use tasks; only on error for code generation; or leave it to the model. How: exact matching on keys such as entity names, vector search by meaning for similar situations or sequences, and combinations with keyword and pattern search. The difference from standard retrieval-augmented generation (RAG) is provenance: RAG searches a static corpus, memory is content added through interactions, which makes extraction and update the error-prone part.
- **Trade-off**: recall versus noise versus latency.
- **Does not hold when**: un-reconciled memories contradict each other: the agent then invents (an assistant inferred a wrong personality trait from a single query).

## 15.6 Three kinds of agent memory in one worked pattern
- **Thesis**: facts, examples and instructions can be updated by different mechanisms.
- **Mechanism**: in an email assistant: triage classifies each message (respond, notify, ignore) with a short reasoning field; semantic memory stores extracted facts about contacts and the user; episodic memory stores past cases as few-shot examples; procedural memory is the prompt itself, rewritten from feedback. Human feedback is the learning signal: marking a thread resolved leaves memory untouched; ignoring a message stores an "ignore" example; editing a proposed tool call lets a model infer what instruction change would have produced the edit; free-text feedback re-runs the task and, in the background, updates the instructions. Memory and prompt optimisation are two sides of one coin.
- **Trade-off**: few-shot examples suit classification and structured extraction; complex rules are better distilled into prompt text. Thread-scoped (short-term) and cross-thread (long-term) stores differ, and time-limited memories are less explored.
- **Does not hold when**: the model's in-context learning over very long example lists improves enough to replace distillation (a forecast).

## 15.7 Files as the memory primitive
- **Thesis**: a file system is a universal, durable, human-readable memory that models already know how to use.
- **Mechanism**: give an agent a directory, a shell and a short skill document (a few dozen lines) that points to sub-documents on how to handle each file; instruct it to inspect before assuming; if the same fact lives in two files, say explicitly that they must be kept in sync. Because people can read and edit the same files, the pattern doubles as human-in-the-loop review. Cloud file systems add durability, multiple users, versioning and permissions. The guiding principle is to ride the model's priors: prefer interfaces the model was trained on (files, shell, search) over bespoke schemas, and do not spend effort retraining behaviour at inference time.
- **Trade-off**: simple and inspectable against weak structure and concurrency control.
- **Does not hold when**: you need transactional guarantees or fast structured queries; a database is better.

## 15.8 Agentic search
- **Thesis**: retrieval works better as a loop in which a model issues queries, reads results and decides when to stop.
- **Mechanism**: the search agent has tools (hybrid dense plus sparse search, pattern search over full text, fetch a whole document) and may end its own loop; it handles multi-document and contradictory-document questions that a single retrieval pass cannot. The same loop decides where to write new information. Predictions from one vendor (positions): a steering layer that pushes or pulls context into the reasoning model, small and fast retrieval models, and continual learning realised at the context layer (adding knowledge to a store) rather than in weights.
- **Trade-off**: better answers against more calls and latency.
- **Does not hold when**: the question is a single lookup of a known item.

## 15.9 Specifications as the memory of a coding agent
- **Thesis**: for software work, written specifications carry decisions across stateless sessions.
- **Mechanism**: a project "constitution" records the mission, technology stack and roadmap; each feature gets a spec (plan, requirements, validation criteria), written in conversation with the agent, which asks questions and surfaces trade-offs; small edits to the spec steer large code changes (one sentence about the database choice can touch hundreds of lines). Work in branches with frequent commits, review the spec for wrong assumptions the agent filled in, validate with tests and a human in the loop, then re-plan: update the constitution in its own branch so versions of the spec can be tied to versions of the code (a practice still evolving). The approach also applies to existing code bases, and keeps the workflow independent of any one agent. The contrast is "vibe" coding that hopes the agent chooses right.
- **Trade-off**: more upfront thinking and review for better intent fidelity and maintainability.
- **Does not hold when**: you want a quick throwaway; specs then cost more than they save. Details of agent practice are in `coding-with-agents`.

## 15.10 Evaluating agents: neither leaderboard worship nor vibes
- **Thesis**: public scores are noisy signals, taste alone is unmeasured, and the truth is in your own task set.
- **Mechanism**: one camp trusts leaderboard numbers although neighbouring scores are not meaningfully different and releases can be tuned to a benchmark; the other trusts taste, which cannot be tracked. Heuristics: do not chase every release, wait for the dust to settle, then test; prefer evaluations close to your problem (a coding benchmark became saturated and was dropped from release notes); consider cost, since a model costing a fraction of another may suffice. Practice: run the evaluation, get a baseline, bucket the failures (for example 20 of 89 tasks looped on file reading or installation), fix the tool or harness, rerun. An agent evaluation tests three things at once: the model, the harness (scaffolding, tools) and whether the problem set matches yours; the same model can behave better in one harness. Isolated containers run in parallel avoid interference and shrink a multi-hour sequential run. Danger zone: once a number exists people optimise it (prompts fitted to the tasks), so hill-climb, then still pass a sanity check.
- **Trade-off**: effort against actionable direction.
- **Does not hold when**: the evaluation set leaks into the prompts or training.

## 15.11 Tracing, tool-use metrics and measured prompt changes
- **Thesis**: instrument runs so that errors invisible in the final answer are visible.
- **Mechanism**: record each run as spans (model calls, tool calls with arguments and results). Check tool selection (a simple question should not call a chart tool) and tool output (an agent reported a chart, but the trace showed a placeholder file name). Score with LLM judges and code checks, and test every change on a fixed evaluation set: in one demonstration, prompts rewritten by a model with examples raised accuracy from 68 to 84 to 88 percent while an automatic prompt optimiser mostly changed speed (a vendor claim; mileage varies).
- **Trade-off**: overhead against debuggability.
- **Does not hold when**: you read a single demonstration as typical.

## 15.12 Simulation sandboxes for action agents
- **Thesis**: an agent that acts in the world needs a safe copy of the world to fail in.
- **Mechanism**: agents operate in partially observable environments (hidden user intent, hidden system state): each action changes the state and returns a possibly delayed reward. A sandbox copies production's users, tools and services without consequences. Components: scenario generation (failure modes of each tool, out-of-scope requests, edge cases), simulated users (language models are trained to be polite; you need frustrated, incomprehensible or indecisive ones), simulated services, and evaluation, where a script with ground truth beats an LLM judge. The sandbox can also produce data to improve prompts or fine-tune. Testing in production is the alternative; its risks are lawsuits and deleted databases. Bias warning: the argument comes from a vendor of such sandboxes.
- **Trade-off**: realism and coverage cost effort; a poor simulation gives false confidence.
- **Does not hold when**: the real environment cannot be modelled (open-ended human behaviour), so staged rollout is still needed.

## 15.13 Red teaming and trajectory-level judgement
- **Thesis**: failures must be found offline, and many only appear across a whole trajectory.
- **Mechanism**: risks range from sophisticated attacks (prompt injection, jailbreaks, prompt leakage) to legitimate queries that expose hallucination, performance problems and off-topic replies, plus reputational incidents. Red teaming finds issues; blue teaming fixes them. Two examples of failures that final-text judging misses: a user growing frustrated while the agent keeps asking for a rephrase instead of escalating (visible only across turns), and a final message claiming success while the tool call had a missing required field (visible only in the tool inputs). Desired behaviours are written in natural language and turned into simulated multi-turn users plus judges; single-turn LLM-as-judge covers the simple cases.
- **Trade-off**: depth versus coverage.
- **Does not hold when**: you treat a clean red-team report as proof of security.

## 15.14 Deterministic validators versus model judges
- **Thesis**: code checks give confidence; a model judge is only as good as the judge.
- **Mechanism**: in a structured agent the plan has explicit steps, dependencies and checkpoints; each requirement gets its own validator and, if it fails, a fixer; success at following all requirements in one large prompt degrades quickly as constraints are added, so a specialised judge per constraint performs better than one judge for many. A static-analysis vendor argues that if a model writes code it should not be the only reviewer; deterministic scans (security patterns, data-flow taint, dependency licences) give consistent results, whereas a model asked to explain the same code three times may answer differently. Generated code can be more complex (more lines, more branching, more hidden bugs) than needed, and models differ in style; trust in generated code was reported to be low in a survey (as quoted).
- **Trade-off**: deterministic checks are narrow; model judges are broad but probabilistic.
- **Does not hold when**: the property cannot be written as code (tone, helpfulness); then judges with calibration and human review remain.

## 15.15 Accuracy, cost and latency as one optimisation
- **Thesis**: improving an agent means moving along a three-way frontier, not maximising one axis.
- **Mechanism**: levers: configuration (model, prompt, tools, harness, guardrails) and inference-time scaling (repeated runs, ensembles, repair loops). Different models solve different tasks, so an ensemble raises accuracy and, by mixing cheaper models, can lower cost and latency (in one company's report, the same accuracy as four runs of an expensive model at less than half the cost and about a fifth lower latency). Execution strategy matters: run all in parallel for speed or start with cheap ones and escalate for cost. The configuration space is practically infinite, so automatic search that learns per-model configurations, stops when a result is good enough ("anytime" generation) and predicts whether another cycle will help can beat months of hand tuning (vendor claim); the search policy only has to learn each new model's configuration, whereas a router or a distilled model must be rebuilt when models change (vendor claim).
- **Trade-off**: tuning effort and search cost against operating cost.
- **Does not hold when**: workload is small enough that a default configuration suffices.

## 15.16 Durable execution
- **Thesis**: a crashed agent should resume, not restart.
- **Mechanism**: split the agent into a workflow (orchestration logic, deterministic) and activities (model calls, tool calls, web searches: the failure-prone, retryable steps); a platform persists state, applies retries and timers, and resumes after a crash, so the user's context and progress survive. The code looks nearly the same as the non-durable version. Making an agent production-ready is harder than making it work.
- **Trade-off**: an extra runtime dependency against reliability.
- **Does not hold when**: sessions are very short or side effects are not idempotent (retrying a payment is dangerous).

## 15.17 Reading documents: parsing, grounding and its benchmarks
- **Thesis**: an agent's answers are only as good as the context extracted from its documents.
- **Mechanism**: complex PDFs and office files need layout-aware parsing (tables, figures), and citations that point to a region of a page need grounding with bounding boxes; calling a general vision model does not provide this. Document benchmarks are incomplete: one measures exact table syntax (too rigid and nearly saturated), another uses binary pass or fail on academic papers (a distribution unlike enterprise files). Orchestration choices: deterministic workflows for repeatable low-complexity processes, general agents prompted in plain language for the rest, with growing task horizons (a vendor claim of half an hour growing to hours).
- **Trade-off**: parsing cost against reduced hallucination and traceability.
- **Does not hold when**: documents are clean text.
