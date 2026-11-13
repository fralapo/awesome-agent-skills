---
name: software-architecture
description: "System design and architecture reasoning for software engineers: how a senior scopes a problem, estimates load and picks components; consistency, replication, quorums, consensus and split brain; high availability, cascading failures, load shedding, thundering herds and cold caches; storage engines (B+ tree, log-structured merge, SQL vs NoSQL, key-value data modelling); sharding, consistent hashing, hot keys and geohash location indexes; look-aside caches, CDN and load balancing; real-time messaging, queues and async pipelines; studies of a cluster manager, managed key-value store, global authorization, social-graph store and cache fleet; case studies of chat, delivery matching and short video; RAG pipelines and agent loops. Use when the user designs, reviews or debugs a distributed system, picks a database, cache or transport, plans for failure or scale, explains a trade-off, or architects an LLM, RAG or agentic feature. Separates facts from positions and says when each rule stops applying."
allowed-tools:
  - Read
  - Grep
argument-hint: [system, problem, trade-off, or chapter number]
---

# Software Architecture
**Chapters**: 11 | **Corpus**: ~16 theoretical transcripts | **Generated**: 2026-11-13

## Role and Boundaries

This skill **decides how to reason about a system's design**: which requirement matters, which number to estimate, which mechanism fits an access pattern, what a design costs, and when a rule stops applying. It gives mechanisms, decision tables and checklists; the user owns the product and the final choice.

| This skill decides | This skill hands off |
|---|---|
| Scope, assumptions, estimates, access pattern, trade-offs, failure and overload plans | Writing, reviewing and testing the code an agent produces, and how LLMs behave while coding → `coding-with-agents` |
| Consistency level, replication, sharding, caching, transport, queue and pipeline shape | Interface, flows, hierarchy and microcopy of the product → `ux-ui-expert` |
| RAG pipeline stages, agent loop, tool design and guardrail placement (architecture level) | Running the workshop that agrees requirements and priorities → `workshop-facilitation` |
| How to read a published system description as a trade-off study | Language- or framework-specific code, cloud-vendor configuration, compliance and legal advice → specialist skills or professionals |

**Stay in lane.** This skill does not invent benchmarks or vendor figures. Numbers in the chapters are the ones stated in the material and are dated snapshots (scales, limits and prices change); re-check before relying on them. Where the source was unclear, the chapter says "unclear in source" instead of guessing.

## Facts vs Positions

- **Mechanism / fact**: how a quorum, a log-structured merge tree, a consistent-hash ring, a token bucket or a re-ranker works.
- **Position**: written as "In this model..." or "(position)": for example "sharding multiplies fan-out, so replicate the cache", "chunk by hand with a domain expert", "prompt rules are advice, not enforcement", "effort moves upstream when code is cheap".
- Every concept in the chapters has four fields: **Thesis**, **Mechanism**, **Trade-off**, **Does not hold when**. Use the last one before recommending: if the limit applies, drop the rule.

## How to Use This Skill

Diagnose before prescribing: ask for the product, the scale (users, requests, data), the read:write ratio, the acceptable staleness and downtime, the team's existing tools and the budget.

| Task | Start with | Then |
|---|---|---|
| Design a system from a vague brief | [ch01](chapters/ch01-senior-method-requirements-estimation.md) (scope, estimate) | ch09 (worked cases), cheatsheet |
| "Consistent or available?", copies disagree, quorum, split brain | [ch02](chapters/ch02-consistency-replication-consensus.md) | ch08 (store studies) |
| Outage, cascade, overload, sale or viral spike, cold cache, migration | [ch03](chapters/ch03-availability-failure-overload.md) | ch06 (caches), ch05 |
| Choose or model a database; slow writes; SQL vs NoSQL | [ch04](chapters/ch04-storage-engines-and-data-models.md) | ch05 |
| Shard key, hot shard, ring, nearby-search | [ch05](chapters/ch05-partitioning-hashing-geospatial.md) | ch04, ch06 |
| Cache, CDN, balancer, rate limit | [ch06](chapters/ch06-caching-traffic-and-delivery.md) | ch03 |
| Chat, push, queues, upload pipelines | [ch07](chapters/ch07-messaging-realtime-pipelines.md) | ch09 |
| "How did a large system solve this?" | [ch08](chapters/ch08-real-systems-as-trade-off-studies.md) | the matching chapter |
| Full practice designs (chat, delivery, short video) | [ch09](chapters/ch09-case-studies-chat-delivery-video.md) | ch01, ch07 |
| RAG quality, chunking, re-ranking, vector search | [ch10](chapters/ch10-llm-systems-and-retrieval.md) | ch11 |
| Agent loop, tools, guardrails, tool protocol, memory | [ch11](chapters/ch11-agentic-systems.md) | ch10 |
| Quick lookup | [cheatsheet.md](cheatsheet.md), [patterns.md](patterns.md), [glossary.md](glossary.md) | |

## The Core Principles (recurrence order)

1. **Access pattern first.** Read:write ratio and how data is requested decide keys, shards, caches and APIs.
2. **Scope and estimate before components.** State assumptions; the estimate shows the dominant constraint.
3. **Choose consistency per operation**, not per system; repair what cannot be proved under failure.
4. **Redundancy adds parts.** Prefer fewer moving parts; plan for the failures that redistribute load (cascade, herd, cold cache).
5. **Reject early, degrade by importance.** Bounded queues, load shedding, priority tiers; never serve everyone badly.
6. **Log first.** Appends are cheap; one ordered change log feeds replicas, indexes, backups and recovery.
7. **Make retries safe.** Idempotent operations, delete-not-update invalidation, background repair of dangling state.
8. **Decouple the scarce thing.** Connection holders, caches and routers do little; business state lives elsewhere.
9. **Reuse what the team masters; keep platforms easy to use.** A thin, minimal API on proven parts beats a new engine.
10. **AI components are probabilistic.** Ground, evaluate, enforce limits in code, and use the smallest mechanism (call, RAG, agent) that fits.

## Chapter Index

1. [Senior method: requirements, estimates, reasoning](chapters/ch01-senior-method-requirements-estimation.md)
2. [Consistency, replication and consensus](chapters/ch02-consistency-replication-consensus.md)
3. [Availability, failure and overload](chapters/ch03-availability-failure-overload.md)
4. [Storage engines and data models](chapters/ch04-storage-engines-and-data-models.md)
5. [Partitioning, hashing and geospatial indexes](chapters/ch05-partitioning-hashing-geospatial.md)
6. [Caching, traffic shaping and delivery](chapters/ch06-caching-traffic-and-delivery.md)
7. [Messaging, real-time delivery and pipelines](chapters/ch07-messaging-realtime-pipelines.md)
8. [Real systems as trade-off studies](chapters/ch08-real-systems-as-trade-off-studies.md)
9. [Case studies: chat, delivery matching, short video](chapters/ch09-case-studies-chat-delivery-video.md)
10. [LLM systems and retrieval-augmented generation](chapters/ch10-llm-systems-and-retrieval.md)
11. [Agentic systems](chapters/ch11-agentic-systems.md)

## Topic Index

- **Agent loop, tools, tool protocol, memory** → ch11
- **Approximate counters, metadata staleness** → ch03, ch06
- **Bloom filter, compaction, tombstone** → ch04
- **Cache invalidation, look-aside, delete-on-write** → ch06
- **Cascading failure, load shedding, queue sizing** → ch03
- **Chunking, re-ranking, query rewriting** → ch10
- **Consistent hashing, hot shard, shard key** → ch05
- **Geohash, nearby search, location pool** → ch05, ch09
- **Idempotency and retries** → ch02, ch07
- **Leader election, Paxos-style, quorum** → ch02, ch08
- **Nines of availability, redundancy layers** → ch03
- **Read:write ratio, estimates** → ch01
- **Replication sync/async, split brain, saga** → ch02
- **SQL vs NoSQL, key-value modelling, token bucket** → ch04
- **WebSocket vs polling vs events, receipts, presence** → ch07

## Related Skills

- `coding-with-agents`: working method, verification and LLM mechanics when an agent writes the code of the system.
- `ux-ui-expert`: the interface and flows of the product built on the architecture.
- `workshop-facilitation`: facilitating the session that fixes scope, priorities and acceptance.

## Scope & Limits

Practical theory distilled from transcripts about distributed-systems design, studies of published systems and applied LLM architecture. Not covered: news-feed ranking in detail, batch-analytics and interactive-query engines, time-series monitoring, tracing, container orchestration internals beyond the cluster-manager study, and security or compliance engineering. Scale figures, vendor limits and model capabilities are snapshots and change quickly; the skill gives no legal, compliance or cost guarantee.
