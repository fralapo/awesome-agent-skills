# Chapter 07: Context Engineering and Agent Harness Design

## Core Idea
A model call is stateless. During one step the model knows only the tokens it is given and what its tools returned. An agent is therefore a loop around a model, and most of its behaviour is set by the **harness**: what enters the context window, which tools exist and how they answer, what survives between steps, when the loop stops, and what gets checked. **Context engineering** is the discipline of making those choices on purpose. In this model it explains more agent failures than the choice of model does; that is a position, so measure it on your own tasks.

Facts vs positions: the mechanics below (the whole context is re-read at every step, a stable prefix can be cached, compaction is lossy, errors propagate through a pipeline) are facts of the architecture. "The harness matters more than the model" and "several agents are the future" are positions. Practitioners disagree on thresholds, so this chapter gives none as a rule.

## 1. The Context Window as a Budget
- Every step re-reads the whole context. Cost and latency grow with its length, and output and reasoning tokens are billed on top (ch06 section 4).
- Attention is shared. Relevant facts compete with noise, and quality on hard tasks often falls well before the window is full. Material in the middle of a long context is used less reliably than material at the start or end.
- Write the budget down: fixed prefix (system prompt, tool definitions, instructions files), retrieved material, history, tool output, and room for the answer. Tool definitions alone can be a large fixed cost. Count them.
- **Measure the knee.** Run the same task with the context filled to several levels and find where the success rate drops. Set the compaction trigger below that point, not at the window limit.

## 2. Load, Retrieve, Externalize, Compact, Isolate
Choose one of five moves for each piece of information.
- **Load** (always present): few, stable, true rules such as conventions, commands and non-goals. Keep the entry file an index that points to documents read on demand.
- **Retrieve** (on demand): fetch by key when the name is known, by meaning when it is not. Exact matching is still needed for identifiers, numbers and codes.
- **Externalize**: large tool results go to a file or store; the context keeps an identifier and a short summary. Pass identifiers between agents, not whole windows.
- **Compact** (lossy): summarise history into a working document. Keep decisions, constraints, open questions, failed attempts and the current plan; drop raw dumps. Keep the original log for audit. A fresh window seeded with a short written summary often beats a long, degraded session.
- **Isolate** (sub-agent): a sub-task runs in its own window and returns a conclusion plus evidence pointers (section 5).

Failure modes:
- Head-only truncation breaks follow-up questions.
- Automatic summarising silently drops a constraint stated once.
- Stale context: an answer cached before the system changed keeps being served.
- An error page returned with a success status gets compressed as if it were content. Validate before you compress.

**Context as an object.** Instead of stuffing data into the prompt, give the agent a few generic tools (list, read a range, search, run a query) and let it explore. For large material this often beats an elaborate tool catalogue, at the cost of more steps (position; test it on your task).

## 3. Tool Design for Agents
A tool is a contract the model reads: name, description, arguments and output shape are the whole interface.
- **Fewer, sharper tools.** Each definition costs context and adds a choice. Selection degrades when many tools look alike (position; measure it). Thin wrappers around every endpoint are the usual mistake.
- **Design around the task, not the API.** "Create and attach" beats three atomic calls the model must sequence correctly.
- **Descriptions are context**: what the tool is for, when not to use it, what each argument means, what errors look like.
- **Errors say how to recover.** "Identifier not found; list candidates with the search tool" keeps the agent moving; a bare failure makes it loop or give up.
- **Bounded output.** Paginate, truncate with a visible note, return identifiers and summaries. A dump of tens of thousands of lines is not a response.
- **Make failure visible.** A pipeline that reports only the last command's exit status turns a failing test into a success. Use fail-fast shell settings.
- **No hidden prompts.** An interactive prompt is invisible to the agent. Provide non-interactive flags, machine-readable output and environment credentials.
- **Code instead of many calls.** The model writes a short program against a typed client that runs in a sandbox: fewer round trips and tokens, but harder debugging and no resume at an intermediate step (position).

## 4. Protocol-Style Tool Interfaces
A standard protocol lets clients discover and call tools that servers expose. It standardises the plumbing, not judgement, security or task fit.
- A server author often does not know the agent's task. Design the tool surface for the task, or do not expose the whole API.
- **Authentication**: a delegated flow in which the server verifies tokens while login and consent stay with the authorization server. Long-lived shared keys do not record who acted. Prefer short-lived tokens scoped to user, tool and call.
- **Tool descriptions are untrusted input.** A server can place instructions in its descriptions (tool poisoning). Pull servers only from a vetted registry and pin versions.
- **Sampling** lets a server ask the client's model to complete a step, so the remote tool holds no model and its cost stays with the client (position on cost).
- **Not everything needs a protocol.** For a local, repeated, technical task, a command-line tool with JSON output is simpler to test and lets the agent filter output before it reaches the context. Protocols suit remote access and non-technical users (position).

## 5. Planning and Sub-Agent Patterns
- **Climb only when needed.** Single call, fixed workflow (chain, router, parallel branches), single agent with tools, then several agents. Several agents pay off when the task has separable context, parallel read-only work, or distinct permissions. Otherwise a well-designed single agent usually wins (position, widely reported).
- **Plan as an artifact.** Write the plan to a file, tick steps, re-read it each turn. Models announce steps they have not executed, so require an explicit finish condition.
- **Sub-agent contract.** The sub-agent receives a system prompt, its tools and one message. It returns a status (completed, failed, cancelled, rejected), evidence and effects. A timeout is *unknown*, not failure. The orchestrator re-verifies any claim it will act on, because a sub-agent that failed halfway can return text that reads like success.
- **Lead and workers.** The lead sets the quality ceiling, so it gets the strongest model; workers can be cheaper. Check whether the gain justifies the extra tokens multi-agent setups multiply.
- **Parallel writes.** Parallelise reads freely. Assign file ownership before writes so two agents never edit the same file.

## 6. Memory Outside the Window
- Context is not memory. Memory is state written outside the window and read back by a retrieval step.
- Keep the kinds apart: **working** (inside the window), **episodic** (what happened), **semantic** (facts), **procedural** (rules). A tone rule is not a fact.
- The **write path** is where errors enter. Distil rather than copy; scope each item (user, project, team); date it; record its source. Gate writes: accept, reject or send to a person. Promoting nothing loses continuity; promoting everything fills later runs with noise.
- Treat retrieved memory as **input to check**. A memory written from an untrusted source changes future behaviour silently.
- **Supersede, do not delete silently**: a newer fact replaces the older one and the history stays for audit.
- Procedural edits to instructions deserve a person's review.

## 7. Workflow or Autonomous Agent?
- A **workflow** fixes the path in code and lets the model supply judgement at named points: predictable, cheap, testable.
- An **agent** lets the model choose the path: flexible, more expensive, harder to bound.
- Decision rule: keep deterministic whatever must always happen (validation, commits, permissions). Leave agentic whatever needs interpretation. Allow more autonomy where errors are cheap and reversible.
- **Sync-to-async**: a person starts the work and calibrates it early; the agent runs alone and signals when it needs help (a common practice position).
- **Durable execution**: persist state per step and resume after a crash without repeating completed calls. Non-idempotent effects, such as payments or sent messages, must never be retried blindly.

## 8. Guardrails Belong in the Harness
- **Enforce, do not instruct.** A line in the prompt is a suggestion. Permissions, blocked commands, network rules and approval gates run in code, before the action.
- **Deny by default.** Give each tool and run only the permissions the task needs.
- **The lethal combination**: private data, untrusted content and an outbound channel in one run. Break at least one in any run. This is a widely held position; the exact rule is contested.
- **Approvals bind the action**: what, with which parameters, by which actor, until when. A broad "yes" to a category invites approval fatigue.
- **Kill switch** covering prompts, tools, models, memory and sub-agents through one middleware path (ch06 section 11).
- **Stop conditions** in code: a maximum number of steps, repeated identical calls, an exhausted budget.

## 9. Cost and Latency
- Cost follows re-reading. A long loop of short steps can cost more than one well-prepared step. Measure cost per completed task, attributed to run, user and function.
- Keep the model fixed within one conversation: switching discards the provider cache for that prefix (ch06 section 4).
- Strong models for planning and checking, cheaper ones for routine steps; check the router's errors on a sample.
- Latency multiplies along sequential calls. Parallel reads and streamed partial results shorten wall-clock time.
- Cheaper tokens tend to produce more usage (the Jevons effect, a position). Budget the agent as a cost line.

## Common Mistakes
- Loading every instruction, tool and document "in case", then wondering why the agent ignores the important one.
- Compacting before measuring where quality drops.
- Many near-identical tools.
- Errors that look like successes.
- Memory the agent writes and nobody reviews.
- Sub-agents that return transcripts instead of conclusions.
- Guardrails written only in the prompt.

## Checklist
- [ ] Fixed prefix measured, including tool definitions
- [ ] Quality knee measured; compaction trigger set below it
- [ ] Each tool has a purpose, a when-not, argument meanings and recoverable errors
- [ ] Tool output bounded and paged; identifiers passed instead of dumps
- [ ] Memory scoped, dated, sourced and behind a write gate
- [ ] Permissions deny by default; approvals bound to actions
- [ ] Step, repetition and budget stops enforced in code
- [ ] Cost per completed task tracked

## Connects To
- ch02 (the loop and steering), ch03 (checking what comes back), ch06 (token economics, caching, compaction, security, unattended-agent safety).
- ch08 for evaluating and monitoring the harness.
- `ai-ml-concepts` ch15 for memory and durable execution as concepts; `software-architecture` for the system around the agent.
