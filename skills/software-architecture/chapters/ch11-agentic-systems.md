# Chapter 11: Agentic Systems

## Core Idea
An agent is a language model running **in a loop with tools and memory**, wrapped in code you control. In this model the model decides, the harness executes, and you stay accountable for limits, permissions and failure behaviour - because the model is neither deterministic nor safely self-limiting.

## 11.1 Why a plain model call is not enough
- **Thesis**: a model only outputs tokens; it cannot act.
- **Mechanism**: asked to "book my flight", a plain call can only suggest where to go; the user still does the work. An agent exposes **tools** (callable functions) so the model can ask the harness to run them: collect structured details through a form, search flights, book. The result goes back to the model, which decides the next step.
- **Trade-off**: autonomy means actions with side effects.
- **Does not hold when**: one retrieval plus an answer suffices (RAG).

## 11.2 Anatomy: model, harness, tools, memory
- **Thesis**: the model is the brain you do not control; the rest is yours.
- **Mechanism**: the **harness** is the agent code, the system prompt and behaviour rules, the tool set (own or external), and memory. Model plus harness equals the agent. The model chooses when to use a tool and fills in the arguments (for example converting currency pairs); the harness runs it, controls what memory to pass, and enforces limits.
- **Trade-off**: the more the model decides, the less predictable the path.
- **Does not hold when**: the workflow is fixed - then write plain code.

## 11.3 The loop (reason, act, observe)
- **Thesis**: the simplest effective single-agent pattern is a loop with a hard stop.
- **Mechanism**: send the model the user message, system prompt and tool definitions; if it returns tool calls, run them (possibly in parallel), append each result tagged with the **tool call id** (the id lets the model match results to calls, because the same tool may be called several times with different outcomes), and call the model again; stop when it returns no tool calls; also stop at a **maximum number of iterations** and report. Example: weather plus currency conversion in parallel in step one, hotel prices in step two, because the second step depends on the first.
- **Trade-off**: linear thinking; cost and latency grow with iterations; complex tasks need other patterns.
- **Does not hold when**: tasks need long planning or many specialists (other patterns exist; not covered).

## 11.4 Designing tools
- **Thesis**: a tool is an interface for a model, so describe it like one.
- **Mechanism**: state what it does, **when** to use it (triggers), what each parameter means, what it returns, and give example inputs (for example "USD", not "United States dollars"). Name tools after business tasks (change a seat, make a booking) rather than raw capabilities (update). In real code a decorator generates the description from the function. Every useful agent has tools.
- **Trade-off**: clear descriptions take effort; brittle if the underlying API changes.
- **Does not hold when**: the tool is one-shot and obvious.

## 11.5 Failure behaviour
- **Thesis**: when a tool fails, a model can quietly fall back on its general knowledge and answer confidently.
- **Mechanism**: in a demo where the price tool returned "not available" or an error, the model still answered a booking question from prior knowledge, even when the system prompt said not to guess. Retrying within the iteration limit happens, but eventual failure handling is yours: fall-backs in the prompt (try another provider), error results that the model cannot ignore, and checks outside the model.
- **Trade-off**: prompt rules reduce but do not eliminate it; stronger models follow rules better; weaker models need blunt instructions.
- **Does not hold when**: wrong answers are cheap.

## 11.6 Guardrails
- **Thesis**: guardrails written in the system prompt are advice, not enforcement.
- **Mechanism**: the prompt can refuse out-of-scope requests and prompt-injection attempts, and set limits such as a maximum fare; stronger models follow them better. Hard limits (spending caps, permission checks, authorization of payments by the user) must be enforced in code and in the external systems. Sandboxing limits the damage of mistakes.
- **Trade-off**: code limits are rigid.
- **Does not hold when**: nothing irreversible can happen.

## 11.7 Tool protocol (MCP-style) vs plain APIs
- **Thesis**: a tool protocol flips the maintenance burden to the provider.
- **Mechanism**: wrapping an API by hand is tedious and brittle - when the API changes, the caller's tool description breaks. With a tool-protocol server, the harness connects at startup, asks for the tool list and definitions, and receives a notification when a definition changes; no client library is compiled in. It differs from a plain API in being stateful (calls can be traced across a conversation) and discovered at run time. It carries **no intelligence**: choice of tool is the model's. Tool outputs are free-form text/JSON; there is no standard for response shape, and errors are just text.
- **Trade-off**: trust in third-party servers (same risk as any external API, plus the model's judgement); cost of **context**: the model is stateless, so tool definitions are sent in every call, and connecting many servers bloats the context even for unrelated requests.
- **Does not hold when**: you own both sides and the tool set is stable.

## 11.8 Memory and context engineering
- **Thesis**: memory is context you choose to carry; it improves answers and costs tokens.
- **Mechanism**: store earlier interactions, preferences and tool outcomes; the harness decides what to pass (and what not to, for sensitive data). Examples: remember a seat preference across months. Do not "train" the model for new information; add it to context (training or fine-tuning is rare).
- **Trade-off**: more tokens, higher latency, privacy exposure.
- **Does not hold when**: each interaction is independent.

## 11.9 Choosing between a plain call, RAG and an agent
- **Thesis**: pick the smallest mechanism that fits.
- **Mechanism**: single question over general knowledge -> plain call; needs private or fresh information -> RAG; needs to change something or to choose among data sources over several steps -> agent.
- **Trade-off**: agents are costlier and less predictable.
- **Does not hold when**: a deterministic workflow exists.

## 11.10 Evaluate agents
- **Thesis**: building an agent is easy; showing it works is the job.
- **Mechanism**: measure success on realistic cases and traces, use model judges for grounding, review traces for tool misuse, and watch cost and latency at scale. Models change quickly, so re-test on each change.
- **Trade-off**: evaluation takes as long as building.
- **Does not hold when**: you only prototype.
