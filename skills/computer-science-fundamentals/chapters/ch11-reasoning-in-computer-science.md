# Chapter 11: How to Reason in Computer Science

## Core Idea
The technical chapters share a small set of habits. In this model a good computer scientist (1) separates what is impossible, what is merely expensive and what is cheap, (2) names the operation that dominates the cost, (3) measures before believing, (4) asks what an adversary or an unlucky interleaving would do, and (5) states what each rule assumes so that the exit condition is visible.

## 11.1 Sort the question: impossible, intractable, tractable
- **Thesis**: the first move is to place the problem on the ladder from ch1.
- **Mechanism**: undecidable (no algorithm), believed intractable (exponential; NP-hard), polynomial but heavy, near-linear. For the first two, state the compromise (restrict the input, accept approximation, use heuristics, time-limit, or use a checker that may answer "unknown"). For the others, optimise.
- **Trade-off**: a clever heuristic is not a proof; label it as such.
- **Does not hold when**: the instance size is small enough for brute force.

## 11.2 Find the dominant operation and its machine cost
- **Thesis**: complexity classes tell you scaling; the machine tells you constants. Memory access, not arithmetic, usually dominates.
- **Mechanism**: ask how many times each step runs, whether the data is sorted, what the access pattern is, which cache level answers (ch4), how many system calls or network round trips happen (ch6, ch7). Convert to a rough number of cycles or nanoseconds and see which line dominates.
- **Trade-off**: a back-of-envelope model is only an order-of-magnitude guide.
- **Does not hold when**: contention, other tenants or an unusual input distribution change the picture.

## 11.3 Measure, because the same code behaves differently on different machines
- **Thesis**: an assumption about how a processor runs code is a hypothesis; the array-versus-list experiment gave opposite results on neighbouring generations of one processor family, and a benchmark chosen by someone else may not resemble your workload.
- **Mechanism**: write a small test on the real hardware with real data, repeat it, and compare. Beware of the compiler optimising away or restructuring your test (ch6).
- **Trade-off**: measurement takes time; it pays for decisions that are expensive to reverse.
- **Does not hold when**: the difference is too large to doubt (a linear scan of a hundred million items versus a lookup).

## 11.4 Amortise: precompute, sort once, specialise at compile time
- **Thesis**: shift work from the repeated path to the one-time path.
- **Mechanism**: sort once and search many times (ch2); compute a divisor's reciprocal at compile time (ch6); reuse a connection or a cached translation (ch4, ch7); memoise (ch2). The break-even is the number of repetitions.
- **Trade-off**: preparation cost, memory, staleness.
- **Does not hold when**: each input is used once.

## 11.5 Caches everywhere, and what they cost
- **Thesis**: a cache in front of a slow store is the most common performance move; it is also the most common source of inconsistency.
- **Mechanism**: CPU caches (ch4), translation caches, DNS caches (ch7), caches of memoised results; "almost every problem can be solved by adding another layer of caching" is a half-joke. Each cache adds a policy (what to evict), a freshness rule (when to refresh) and a coherence question (who else changed this).
- **Trade-off**: speed versus staleness and complexity.
- **Does not hold when**: access is genuinely random with no reuse; the cache only adds overhead.

## 11.6 Easy to verify, hard to find
- **Thesis**: asymmetry between checking and searching is a resource to exploit and a structural fact to respect.
- **Mechanism**: it underlies signatures and factoring (ch8), proof of work (ch9), NP (ch1), and the design principle of verifying received data cheaply before acting on it. If you can check an answer quickly, you can accept untrusted suggestions (including from heuristics or generated code) and verify them.
- **Trade-off**: a cheap check must be a complete check.
- **Does not hold when**: verification is as hard as the search.

## 11.7 Explore versus exploit
- **Thesis**: the same trade-off shows up whenever you decide under uncertainty.
- **Mechanism**: annealing temperature, the exploration bonus in tree search, bandits, random restarts (ch2). Explore early and widely, exploit as evidence accumulates; keep a little exploration to avoid being trapped.
- **Trade-off**: where the switch point lies depends on the cost of a bad trial.
- **Does not hold when**: a mistake is irreversible (then exploration must be simulated, not performed).

## 11.8 Adversaries and interleavings
- **Thesis**: concurrency bugs and security protocol attacks have the same shape: a combination of steps nobody pictured.
- **Mechanism**: for shared state, list the interleavings of check and act (ch5); for a protocol, list the roles a party can play and who could relay messages (ch9). Remove the problem by structure: indivisible steps, fixed lock order, idempotent actions, identity-bound messages.
- **Trade-off**: structural fixes constrain design.
- **Does not hold when**: the system is single-actor and trusted.

## 11.9 Know the layer below
- **Thesis**: abstractions are lies that help; when behaviour surprises, descend one layer.
- **Mechanism**: the pointer is a virtual address (ch4); a print call is a system call (ch6); a connection is a flow with a window (ch7); a "random" number may be a shift-register sequence (ch7, ch5); a "secure" operation may leak by its timing (ch8). Sort symptoms by layer before changing code.
- **Trade-off**: depth takes time; use it when the symptoms are inexplicable at the current layer.
- **Does not hold when**: the abstraction is airtight for your purpose.

## 11.10 Break symmetry, and make repeats harmless
- **Thesis**: identical deterministic parties retry in lockstep forever; a little asymmetry or real randomness ends it; and an operation that is safe to repeat tolerates retries.
- **Mechanism**: backoff with random jitter, ordering by an identifier, one party picking up the second utensil first (ch5); separate start and stop actions (ch5); retry-safe messages (see `software-architecture` ch20).
- **Trade-off**: randomness hurts reproducibility; seed and log it in tests.
- **Does not hold when**: the order is dictated by a protocol.

## 11.11 Hand-offs
- **Thesis**: this skill gives the fundamentals; others own the applied layers.
- **Mechanism**: distributed system design, consistency, caching in production, TLS and gateways: `software-architecture`. Neural networks, optimisation, transformers, diffusion: `ai-ml-concepts`. Writing and reviewing code with agents: `coding-with-agents`. Everyday engineering practice (tests, reviews, refactoring): `software-engineering-practice`. Interface design: `ux-ui-expert`.
- **Trade-off**: none.
- **Does not hold when**: the question really is about fundamentals only.
