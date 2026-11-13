# Chapter 01: The Senior Method - Requirements, Estimates, Reasoning

## Core Idea
In this model a senior designer is recognised less by knowing components than by the **order of work**: scope the problem, state assumptions out loud, estimate, derive the access pattern, and only then choose components. Every later chapter is a toolbox; this one says when to open it.

Each concept uses four fields: **Thesis** (the claim), **Mechanism** (how it works), **Trade-off** (what it costs), **Does not hold when** (the limit).

## 1.1 Scope the features before drawing boxes
- **Thesis**: a design question is too big to answer whole; the designer picks a small, explicit feature set and says what is out of scope.
- **Mechanism**: list candidate features (for a chat system: one-to-one messages, group messages, media, sent/delivered/read marks, online status, temporary vs permanent history), start with the ones already understood, and drop the rest in writing. For a delivery system: keep order placement, matching and live location; exclude payments, onboarding and restaurant setup (payments assumed to be an outside service).
- **Trade-off**: going deep on one slice loses the full-product view, but a shallow tour of everything yields nothing testable.
- **Does not hold when**: the requirement itself is the unknown (a discovery project); then the first deliverable is questions, not a design.

## 1.2 Assumptions are owned, not guessed silently
- **Thesis**: when the requester gives a vague number, the designer proposes one, states it, and carries it through the whole design.
- **Mechanism**: ask for daily active users, region (one country or global), creators-to-viewers ratio, upload length cap, orders per user per day. If the requester shrugs, pick a plausible figure and say "I will assume X".
- **Trade-off**: a wrong assumption propagates; stating it makes it cheap to correct.
- **Does not hold when**: real traffic data exists - use it instead of an assumption.

## 1.3 Non-functional requirements are a menu, not a binary
- **Thesis**: "consistent or available?" is the wrong first question. Ask, per feature, what delay or staleness is acceptable.
- **Mechanism**: write latency targets separately for each path (upload, time until visible to others, playback start); a delay of minutes between upload and visibility can be fine while upload acknowledgement must be fast. Separate "tolerate a region going down" from "100% uptime".
- **Trade-off**: per-feature choices mean several consistency levels in one system, which costs explanation and testing.
- **Does not hold when**: money or safety is involved (balances, authorization decisions); there the strongest guarantee is the default (see ch02).

## 1.4 Back-of-the-envelope estimates decide what is hard
- **Thesis**: the estimate tells which constraint dominates (storage, read rate, write rate, fan-out), so effort goes there.
- **Mechanism**: users x actions per day = events per day; events per day / 86,400 = average rate; multiply by object size for storage; multiply by derived copies. Worked examples in this model: 10 million active users with one order per day = 10 million orders per day; if one courier makes about 20 deliveries a day, that implies on the order of 500 thousand couriers; a user table of a few hundred bytes per user at 10 million users is only a few gigabytes, so size is not the problem and partitioning is for locality, not capacity. For short video: about 200 thousand uploads per day at about 1 MB each is about 200 GB of raw video per day, then multiplied by every stored format and resolution (the multiplier used in the source is unclear; the method is the point).
- **Trade-off**: estimates are crude; they only need the right order of magnitude.
- **Does not hold when**: the bottleneck is not volume but latency or correctness (a small table can still need consensus).

## 1.5 Read:write ratio sets the whole storage and cache shape
- **Thesis**: measure the ratio first; a ratio around 100:1 or more (reads 99% and above in the graph store and authorization examples) justifies replicas, caches, precomputation and eventual consistency for reads.
- **Mechanism**: compute creators vs consumers (for example 100 thousand creators vs 10 million viewers), then decide: few writers means a single write path per key range with many read replicas.
- **Trade-off**: heavy read optimisation makes writes slower or more complex (invalidation, propagation).
- **Does not hold when**: the system is write-heavy (ingest, logging, telemetry); then optimise the write path first (ch04 log-structured storage).

## 1.6 The access pattern chooses keys, shards and cache layout
- **Thesis**: "no perfect cache, only caches designed for a problem." Observe how data is requested, then lay it out for that.
- **Mechanism**: if every request needs all edges of one source, store those edges together and route by source id; if every page needs hundreds of small keys, replicate the cache rather than shard it (ch05, ch06).
- **Trade-off**: a layout tuned to one pattern makes other patterns slow (finding all edges by destination needs an extra inverse record).
- **Does not hold when**: access patterns are unknown or changing; then keep the layout simple and measure.

## 1.7 Reuse the organisation's strengths; ease of use drives adoption
- **Thesis**: a platform component succeeds when people adopt it, and adoption follows ease of use and fit with existing operational skill.
- **Mechanism**: the graph store was built as a thin API over an existing cache and relational database the organisation already mastered, instead of a new in-memory graph database. A client library hides requests, retries, batching and compression, so callers import it rather than hand-build calls; a minimal API (add edge, get edges with limit/time window/paging, count) keeps the production path fast and the learning curve short.
- **Trade-off**: reuse inherits the old components' limits; a minimal API refuses feature requests.
- **Does not hold when**: no existing component meets a hard requirement (here: nothing existed at the required scale for in-memory graph queries, so something had to be built).

## 1.8 Decouple, and keep the edge dumb
- **Thesis**: scarce resources (connections, memory) should not also hold business state.
- **Mechanism**: a gateway only holds connections and forwards raw messages; a session service knows who is connected where; a group service knows who is in which group; parsing happens in a separate stage. Each can be scaled and failed independently.
- **Trade-off**: more network hops and more services to run.
- **Does not hold when**: scale is small; a single service is cheaper to build and reason about.

## 1.9 Simplicity beats perfection; boring and predictable beats clever
- **Thesis**: choose the simplest mechanism that meets the stated requirement, and prefer low variance of behaviour to peak speed.
- **Mechanism**: a one-minute migration done with one plain query in a planned window beat a streaming pipeline; a managed database service with predictable latency beats a fast but erratic one; fewer moving parts means fewer failure combinations.
- **Trade-off**: simple solutions may have visible downtime or limits; they are chosen because the requirement allows them.
- **Does not hold when**: the requirement explicitly rules out downtime or data loss (ch03 high-stakes domains).

## 1.10 Build vs buy vs rent
- **Thesis**: before building, ask whether an off-the-shelf or open-source piece exists, and compare its service level to the requirement.
- **Mechanism**: for a CDN, an outside provider is rational for most; building one is rational only at a scale where control, flexibility and reliability pay for the effort. Compare the vendor's stated availability to the target. For geospatial lookups, check whether the database already has a geospatial extension before building indexes.
- **Trade-off**: renting couples you to a vendor's SLA and cost curve.
- **Does not hold when**: cost at scale or a hard control requirement flips the economics.

## 1.11 Cost estimate early
- **Thesis**: design reviews improve when cost appears in the first minutes, because it prunes options.
- **Mechanism**: after the storage and traffic estimate, state a monthly order of magnitude for storage, transfer and compute; revisit it when adding derived copies or replication.
- **Trade-off**: cloud prices change; treat any figure as a dated snapshot.
- **Does not hold when**: cost is not a constraint of the exercise.

## 1.12 Admit gaps precisely
- **Thesis**: saying "I have only used X; I would check the difference to Y" is better than guessing, and the weak spots found in review are usually the protocols and numbers the designer skipped.
- **Mechanism**: pick the transport (upload and download protocols, push mechanism) early; being hesitant there is what reviewers probe.
- **Trade-off**: honesty costs a little in confidence signalling.
- **Does not hold when**: the gap is in the core of the design, then close it before presenting.

## 1.13 Positions on relevance in the age of code generation
- **Thesis (position)**: when code is cheap to produce, the scarce skills move upstream: design, trade-off decisions, judging whether output is good, and measuring that a claim is true.
- **Mechanism**: learn the basic vocabulary of LLM systems, apply it to a real project, and keep the habit of tests and measurement for claims ("the bridge cannot fall"). Experience supplies the context that tools lack.
- **Trade-off**: a forecast, not a fact.
- **Does not hold when**: the work is purely mechanical and already specified.
