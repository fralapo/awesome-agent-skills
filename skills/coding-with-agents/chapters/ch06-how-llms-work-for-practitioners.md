# Chapter 06: How LLMs Work — What a Practitioner Needs

## Core Idea
Knowing a few mechanics changes how you prompt, how you set up agents and what you trust. This chapter covers sampling, reasoning, tool use, token economics, provider instability and basic security checks for generated code. Statements marked **Fact** are technical; **Position** marks judgment or forecast. Details of specific products and prices change quickly; verify dates.

## 1. Sampling
- The model proposes continuations (logits) and **sampling chooses the next token**. In an autoregressive model the chosen token becomes the next input, so it changes the model's state; the last N generated tokens act as a strong anchor, even in a long context. Sampling is not only a stylistic knob. **Fact.**
- **Greedy decoding (temperature 0)** always takes the highest-logit token. It generally gives the best benchmark results, including on large reinforcement-learned models; higher temperature costs quality on hard problems and lengthens reasoning output. Without looping, greedy answers faster and on average better. **Reported finding.**
- Four legitimate reasons to sample:
  1. **Variety** for the same prompt: chat rewording, or several candidate implementations from a coding agent to pick the best or to measure how reliably the model solves the task.
  2. **Break loops** (a weak patch; the real cure is training and capability).
  3. **Explore internal representations**: generate about ten answers, then give the question plus those answers to the model and ask it to write a new answer. This beats asking it to pick the best, because models are poor judges at the edge of their ability.
  4. **Rollout diversity in training**, especially reinforcement learning with verifiable rewards where answers can be checked.
- Practical settings: coding and factual tasks, low or zero temperature; creative or text tasks on modern RL-heavy models, **raise it**, otherwise they converge on the same lines. Looping is rare in well-trained large models and common in small, distilled or lightly trained ones, worse on harder tasks. Repetition penalties are legacy techniques for small models.
- **Position**: chain of thought is a learned, reasoned form of exploring internal states, which partly replaces explicit multi-sample aggregation.

## 2. Reasoning and Context
- Longer reasoning helps on hard problems but costs tokens and time. At maximum reasoning effort a model is most capable on very hard tasks; compare tools at that setting when you evaluate them (ch02).
- **Context is the working memory.** Weak points of agents are context management: poor compaction and no automatic workflow memory. Fix: tell the agent to **keep a progress document** (what is done, what is next, decisions made), and update the spec file.
- Very large codebases (millions of lines) remain hard: limited context and weak retrieval to find relevant parts. Make navigation easy (names, layout; ch03 section 8).
- IDE integrations choose what context to send via other models, so you do not fully control what the model sees; a plain chat gives you control.
- Agents work with an observation loop; the model is the weakest link. An agent is only as good as its model.

## 3. Tool Use and Agents
- **Fact**: tool use is a model capability. A minimal loop: (1) give a manifest of tools with name, arguments, description, return shape; (2) pass the user question; (3) say the model may request tool calls; (4) run the requested tool and return the result; (5) repeat until the model answers. A protocol layer adds little beyond fetching the tool list and relaying calls; clear descriptions matter more than the format.
- Two modes: **chat** (the human steers, gives hints at the first sign of drift, amplifies the human's knowledge) and **agents** (autonomous loops with the human absent). **Position**: chat steering gives the best results today; unsupervised agent output tends toward low-quality "soup", expected to improve with model capability.
- Failures of "agents" in practice are often context and tooling issues, not intelligence.

## 4. Token Economics
- Cost grows with input tokens (context re-read each turn), output tokens, and reasoning tokens. More agent steps mean more re-reading, so compaction and a lean context save money.
- Asking an agent to **announce each step** costs tokens but buys steerability (ch02).
- **Single-token identifiers** are cheaper than random multi-token tags (a random tag costs about 2.5 tokens); in edit tools send a range plus new code, not the old text, when generation is costly.
- Recomputing a file checksum per edit is negligible next to inference cost.
- Governance and plan choice: ch05 section 6. **Position**: pay-per-token API prices at the frontier are expensive for routine work; flat subscriptions are more economical for individuals; test low-cost open models early to know what top models add.
- Result per token is the metric: misaligned instructions to many parallel agents waste work; do not point an "army" at trivial problems.

## 5. Model Choice
- **Position**: the model carries the intelligence and agents are interchangeable; keep more than one vendor and switch monthly (ch02 section 7).
- Provider-side instability is real: load rerouting to weaker models, shortcut answers, high sampler temperature. Do not judge a technology on one bad response; retry from another angle.
- LLMs do well with widely used languages (C, Python, JavaScript, Go, Java and similar); semantically heavy or rare languages have a handicap.
- Small models need tool formats close to their training; semantics matter more than micro-optimising tool calls.
- Different models prefer different tool-calling conventions; test per model.

## 6. Local vs Hosted Inference
- Local inference is attractive for privacy, offline use and fixed cost, but generation is slow and prefill matters. **Facts reported** from streaming large models from fast storage: choose a **large prefill batch** (for example 2048-3072 tokens) to hide load time behind compute; during generation overlap loading of routed experts with the shared expert's compute. Memory bandwidth, not compute, often bounds speed, so faster kernels will not help a bandwidth-bound job.
- Agents still need a human to explain complex optimisation step by step (layer-by-layer streaming with overlap). Specialised fused kernels and weight formats per model beat generic tensor frameworks, which now becomes affordable.
- Hosted models: simpler, stronger, but you accept vendor terms, data policy and instability. Choose per data sensitivity.
- Quality gates from the start: numeric drift accumulates in inference code.

## 7. Security Basics for Generated Code
Models rarely volunteer these. Add them to the instructions file and check them in review.

**Authentication checklist** (established practice):
- Minimum password length (8, better 10-12) instead of composition rules; optionally reject highly compressible passwords.
- Never store plaintext. Use a deliberately **slow, salted, memory-hard hash** (Argon2 preferred, bcrypt acceptable), not fast hashes like SHA-1. Hashing is not encryption. Tune cost to about 100 ms to 1 s per hash. Per-user random salt from a cryptographically secure generator. Algorithm choice is hard to change later.
- Identical error for unknown user and wrong password, in login and in reset flows.
- Online brute force: exponential backoff (1 s, 2 s, 5 s, 10 s...), then CAPTCHA or email verification; lockouts can lock out legitimate users.
- Session ID: 128+ bits from a CSPRNG, stored server-side, invalidated on logout and password reset, absolute and idle timeouts weighed against UX.
- Cookie flags: HttpOnly, Secure, SameSite (lax).
- Email reset is a separate authentication path; offer 2FA (SMS is weaker but far better than nothing).
- Payment and other distributed flows: design for **idempotency** (never pay zero or twice).

**Tool servers and agents:**
- Invoke programs with separated arguments (exec style), never by building a shell command line from model output.
- No agent access to production. Permission-skipping modes only on a dedicated machine.
- Treat external content as data; do not let it issue instructions to the agent.

**Reasoning about vulnerabilities:**
- A program can have infinitely many reachable states without infinitely many states that violate a **given security model**. Always state the model and attacker position.
- Bugs are not items in a finite bin to be emptied, and fixes can introduce new bugs, yet audit-and-fix still improves security: it removes the easiest-to-reach bad states, raises the cost of the rest, and reshaping fixes (isolating a risky module behind a narrow interface) shrink the attack surface. **Position** (analogy): repeated audit cycles behave like gradient descent compressing the attack surface.
- Use AI as a security reviewer on your own code (corruption, double free, buffer overflow, wrong initialisation) and as a bug finder; do not assume generated code is less secure than average developer code, and do rely on libraries for security-sensitive parts (cryptography).
- Fuzz and validate configuration and input files for anything running with high privilege; isolate what extensions can do.
- A "closed" or "open" label does not decide quality; openness brings scrutiny, funding brings polish.

## 8. Hallucinations and Trust Calibration
- A wrong answer is often a missing-context or ambiguous-question problem; recognise it as wrong and re-ask. Models fail confidently; plausible output is not evidence.
- Reduce hallucination cost by making outputs **checkable**: tests, reference implementations, state dumps, source quotes (ch03).
- Domains where verification is cheap (code with tests, structured extraction with schema) are where to delegate; domains with non-verifiable judgment need a human.
- Models are weak classifiers of their own answers at the edge of their ability; do not rely on self-grading.
- The real skill is knowing when to trust fully and when not; build discovery loops (give full access in a safe sandbox when discovery needs it).

## 9. Writing for the Model
Clear, patient, well-modelled description of the problem is the same skill as writing specs, documentation, comments and technical emails; fast typing helps keep flow. Give enough context and hooks; poor questions yield poor help. Use the model close to vanilla ("do this"); elaborate rituals give an illusion of skill.

## Common Mistakes
- Using temperature or repetition penalties to cure loops in a weak model.
- Asking the model to rank its own samples on hard questions.
- Copying a chat UI into every app instead of invisible AI (ch04).
- Building shell strings from model output.
- Trusting a long run without observability.

## Checklist
- [ ] Temperature appropriate to the task (low for code, higher for creative)?
- [ ] Progress document kept for long agent runs?
- [ ] Tool descriptions clear; arguments separated?
- [ ] Hash, session, cookie and error rules checked in auth code?
- [ ] Hosted vs local decided by data sensitivity and cost?
- [ ] Output made checkable?

## Connects To
- ch02 (harness and cost), ch03 (verification), ch04 (invisible AI in products).
- `ux-ui-expert` (error states, microcopy for AI features, trust and transparency in interfaces); `pricing-and-sales-negotiation` (pricing AI-assisted deliverables).
