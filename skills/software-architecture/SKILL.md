---
name: software-architecture
description: "System design and architecture reasoning for software engineers: scoping, estimates; consistency, replication, quorums, consensus, two-phase commit; time, clocks, ordering, linearizability, fencing tokens; availability, cascades, load shedding; storage engines, database internals, choosing a database; sharding, hashing; caching, eviction, Bloom filters and other probabilistic structures; TCP/TLS/HTTP, proxies, timeouts; OS kernel cost; queues, logs, exactly-once, stream processing; real systems and post-mortems as trade-off studies (leaderless stores, Spanner-style SQL, blob stores); case studies; domain modeling, boundaries, modular monolith; events, outbox, CQRS; sagas, idempotency; RAG, agents, LLM serving and quantization. Use when the user designs, reviews or debugs a distributed system, picks a database, cache, transport or messaging style, plans for failure or scale, or analyses an incident. Separates facts from positions and says when each rule stops applying."
allowed-tools:
  - Read
  - Grep
argument-hint: [system, problem, trade-off, or chapter number]
---

# Software Architecture
**Chapters**: 25 | **Corpus**: ~126 theoretical transcripts | **Generated**: 2026-11-14

## Role and Boundaries

This skill **decides how to reason about a system's design**: which requirement matters, which number to estimate, which mechanism fits an access pattern, what a design costs, and when a rule stops applying. It gives mechanisms, decision tables and checklists; the user owns the product and the final choice.

| This skill decides | This skill hands off |
|---|---|
| Scope, assumptions, estimates, access pattern, trade-offs, failure and overload plans | Writing, reviewing and testing the code an agent produces, and how LLMs behave while coding → `coding-with-agents` |
| Consistency level, replication, sharding, caching, transport, queue and pipeline shape | Interface, flows, hierarchy and microcopy of the product → `ux-ui-expert` |
| RAG pipeline stages, agent loop, tool design and guardrail placement (architecture level); memory arithmetic and quantization when serving a model | Running the workshop that agrees requirements and priorities → `workshop-facilitation` |
| Boundaries, module and service ownership, coupling, when to use events, workflow and external-call safety (as positions with counter-cases) | Writing the domain code itself → language- or framework-specific skills |
| Clocks, ordering, fencing, linearizability, Raft and two-phase commit; how a published system places its coordination | Language- or framework-specific code, cloud-vendor configuration, compliance and legal advice → specialist skills or professionals |

**Stay in lane.** This skill does not invent benchmarks or vendor figures. Numbers in the chapters are the ones stated at the time and are dated snapshots (scales, limits and prices change); re-check before relying on them. Where the source was unclear, the chapter says "unverified" instead of guessing.

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
| Kernel cost, page faults, processes vs threads, huge pages, lock stalls | [ch12](chapters/ch12-operating-system-and-kernel-cost.md) | ch14, ch15 |
| Latency with idle CPU, TCP/TLS/HTTP version, ports, sockets, listener design | [ch13](chapters/ch13-networking-and-protocols.md) | ch16, ch15 |
| Slow queries, bloat, locks, WAL, indexes ignored, distributed transactions | [ch14](chapters/ch14-database-internals-and-transactions.md) | ch04, ch02 |
| Outage review, "could this happen to us?", recovery path | [ch15](chapters/ch15-postmortems-and-lessons-from-real-incidents.md) | ch03 |
| Proxy, timeouts, balancer choice, gateway, discovery, OAuth | [ch16](chapters/ch16-proxies-timeouts-and-gateways.md) | ch13, ch06 |
| Model a domain, CRUD vs commands, aggregates, DDD scope | [ch17](chapters/ch17-domain-modeling-and-pragmatic-ddd.md) | ch18, ch19 |
| Module or service boundaries, modular monolith, coupling, interfaces, multi-tenancy | [ch18](chapters/ch18-boundaries-modular-monolith-and-coupling.md) | ch17, ch16 |
| Events, outbox, CQRS, event sourcing, stale reads after a write | [ch19](chapters/ch19-event-driven-architecture-and-messaging-patterns.md) | ch07, ch02 |
| Saga, third-party payment calls, duplicates, reservation, batch job replacement | [ch20](chapters/ch20-workflows-sagas-and-external-systems.md) | ch19, ch14 |
| Clocks, last-write-wins losses, fencing token, linearizability, Raft, commit wait | [ch21](chapters/ch21-time-ordering-and-coordination.md) | ch02, ch23 |
| Dynamo-style leaderless and wide-column stores, hot partitions of a managed service, file system master, lock service, wide-column store | [ch22](chapters/ch22-real-systems-ii-leaderless-wide-column-and-coordination.md) | ch05, ch21 |
| Entity-group consensus, multi-row transactions on a weak store, globally distributed SQL, cloud-native SQL, blob store | [ch23](chapters/ch23-real-systems-iii-transactional-and-cloud-native-stacks.md) | ch21, ch14 |
| Bloom filter, distinct counts, LRU/LFU eviction, scan-resistant cache, hash table growth | [ch24](chapters/ch24-probabilistic-and-cache-data-structures.md) | ch06, ch04 |
| Serving an LLM: weight memory, quantization, KV cache | [ch25](chapters/ch25-serving-llms-memory-and-quantization.md) | ch10 |
| Pick a database; Bitcask-style store; inverted index; log replication; exactly-once; stream processing | ch04 4.15-4.17, ch07 7.17-7.19 | ch22, ch23 |
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
10. **Count the hidden hops.** Connections, kernel transitions, locks and recovery paths cost more than the diagram shows; ask what the system depends on to recover.
11. **AI components are probabilistic.** Ground, evaluate, enforce limits in code, and use the smallest mechanism (call, RAG, agent) that fits.
12. **Boundaries are ownership, not deployment (position).** Choose logical boundaries, then communication, then deployment; decoupling moves complexity, it does not remove it.
13. **The party that owns the truth is the source of truth.** Across a network boundary make steps repeatable, bound reservations in time, and reconcile instead of guessing.
14. **A clock is an interval, and any actor can be stale.** Order with logical time or majority agreement, and let the resource reject stale holders with tokens.
15. **Spend precision only where it pays.** Approximate answers (filters, sampled eviction, quantized weights) cut memory by large factors; keep a source of truth that corrects them.

## Chapter Index

1. [Senior method: requirements, estimates, reasoning](chapters/ch01-senior-method-requirements-estimation.md)
2. [Consistency, replication and consensus](chapters/ch02-consistency-replication-consensus.md)
3. [Availability, failure and overload](chapters/ch03-availability-failure-overload.md)
4. [Storage engines and data models](chapters/ch04-storage-engines-and-data-models.md)
5. [Partitioning, hashing and geospatial indexes](chapters/ch05-partitioning-hashing-geospatial.md)
6. [Caching, traffic shaping and delivery](chapters/ch06-caching-traffic-and-delivery.md)
7. [Messaging, real-time delivery and pipelines](chapters/ch07-messaging-realtime-pipelines.md)
8. [Real systems as trade-off studies](chapters/ch08-real-systems-as-trade-off-studies.md)
9. [Case studies: chat, delivery, video, short links, rate limiter](chapters/ch09-case-studies-chat-delivery-video.md)
10. [LLM systems and retrieval-augmented generation](chapters/ch10-llm-systems-and-retrieval.md)
11. [Agentic systems](chapters/ch11-agentic-systems.md)
12. [Operating system and the cost of the kernel](chapters/ch12-operating-system-and-kernel-cost.md)
13. [Networking and protocols](chapters/ch13-networking-and-protocols.md)
14. [Database internals and transactions](chapters/ch14-database-internals-and-transactions.md)
15. [Post-mortems and lessons from real incidents](chapters/ch15-postmortems-and-lessons-from-real-incidents.md)
16. [Proxies, timeouts, load balancing and gateways](chapters/ch16-proxies-timeouts-and-gateways.md)
17. [Domain modeling and pragmatic DDD](chapters/ch17-domain-modeling-and-pragmatic-ddd.md)
18. [Boundaries, modular monoliths, coupling and dependencies](chapters/ch18-boundaries-modular-monolith-and-coupling.md)
19. [Event-driven architecture and messaging patterns](chapters/ch19-event-driven-architecture-and-messaging-patterns.md)
20. [Workflows, sagas and calls to external systems](chapters/ch20-workflows-sagas-and-external-systems.md)
21. [Time, ordering and coordination in distributed systems](chapters/ch21-time-ordering-and-coordination.md)
22. [Real systems II: leaderless stores, wide-column stores, file systems and lock services](chapters/ch22-real-systems-ii-leaderless-wide-column-and-coordination.md)
23. [Real systems III: transactional stores, cloud-native SQL and blob storage](chapters/ch23-real-systems-iii-transactional-and-cloud-native-stacks.md)
24. [Probabilistic and cache data structures](chapters/ch24-probabilistic-and-cache-data-structures.md)
25. [Serving LLMs: memory and quantization](chapters/ch25-serving-llms-memory-and-quantization.md)

## Topic Index

- **Accept queue, backlog, listener threading models** → ch13
- **Agent loop, tools, tool protocol, memory** → ch11
- **Approximate counters, metadata staleness** → ch03, ch06
- **Aggregate design, rules vs relationships, transaction script** → ch17
- **Batch jobs vs delayed messages, model the future** → ch20, ch07
- **CQRS vs read replicas, materialized views** → ch19
- **CRUD vs task-driven, intent** → ch17
- **Coupling, cohesion, interfaces, hexagonal/clean/onion** → ch18
- **Eventual consistency by context, read-your-writes** → ch19, ch02
- **Event kinds, events as public API, event sourcing** → ch19
- **Idempotent consumers, external-call double charge, reconciliation** → ch20, ch14
- **Logical vs physical boundaries, modular monolith, data from another service** → ch18
- **Multi-tenancy isolation** → ch18, ch04
- **Outbox, dual write** → ch19, ch07
- **Reservation pattern, saga, distributed transaction alternatives** → ch20, ch02, ch14
- **Base 62 short codes, redirect codes** → ch09
- **Bloom filter, compaction, tombstone, write amplification** → ch04
- **Cache invalidation, look-aside, delete-on-write** → ch06
- **Cache stampede, penetration, avalanche** → ch06
- **Cascading failure, load shedding, queue sizing, retry storms** → ch03, ch15
- **Chunking, re-ranking, query rewriting** → ch10
- **Consistent hashing, virtual nodes, hot shard, shard key** → ch05
- **Ephemeral port exhaustion, connection pooling** → ch13, ch15
- **Geohash, nearby search, location pool** → ch05, ch09
- **HTTP/1.1, HTTP/2, HTTP/3, TLS 1.3, slow start** → ch13
- **Idempotency and retries** → ch02, ch07
- **Indexes ignored, EXPLAIN, composite order** → ch14
- **Kafka-style log, offsets, consumer groups** → ch07
- **Latency orders of magnitude, estimation recipe** → ch01, ch12
- **Leader election, Paxos-style, quorum** → ch02, ch08
- **Locks, deadlocks, optimistic vs pessimistic** → ch14
- **Nines of availability, redundancy layers** → ch03
- **Page tables, TLB, page faults, huge pages** → ch12
- **Post-mortems (routing policy, DNS withdrawal, internal network, autoscaling)** → ch15
- **Proxy anatomy, timeouts, balancing algorithms, gateway, discovery, OAuth** → ch16
- **Rate limiter, token bucket** → ch09, ch04
- **Read:write ratio, estimates** → ch01
- **Redis-style in-memory server, persistence options** → ch04
- **Replication sync/async, split brain, two-phase commit** → ch02, ch14
- **Request coalescing** → ch16
- **SQL vs NoSQL, key-value modelling** → ch04
- **Write-ahead log, checkpoint, vacuum, versioned rows** → ch14
- **WebSocket vs polling vs events, inbox, receipts, presence** → ch07
- **Approximate counters, Morris-style log counter** → ch24
- **Bitcask-style log-structured hash store** → ch04 4.16
- **Bloom filter, cuckoo and counting variants** → ch24, ch04
- **CAP in practice, wide-area partitions** → ch02 2.19
- **Chubby-style lock service, coarse locks, consistent caching** → ch22
- **Clock skew, monotonic clock, last-write-wins loss** → ch21
- **Compare-and-swap, optimistic locking** → ch14 14.11
- **Distinct counting (HyperLogLog-style)** → ch24
- **Epoch, term, zombie producer, fencing token** → ch21, ch07 7.18
- **Eviction policies, approximate LRU, LFU, midpoint insertion** → ch24, ch06
- **Exactly-once in a log, idempotent producer, transactional id** → ch07 7.18
- **Flink-style checkpoints, barriers, watermarks, event time** → ch07 7.19
- **GFS-style large-file store, chunk lease** → ch22
- **Hash table doubling, probing, load factor** → ch24
- **Hot partitions in a managed service, bursting, adaptive capacity, admission control** → ch22
- **Inverted index, posting list, stemming** → ch04 4.17
- **Kafka-style in-sync replicas, committed messages** → ch07 7.17
- **Leaderless store, sloppy quorum, hinted handoff, read repair, anti-entropy** → ch22
- **Linearizability, total order broadcast, Raft** → ch21
- **Percolator-style transactions, primary lock, roll forward** → ch23
- **Quantization, scale factor, KV cache, weight memory** → ch25
- **Quorum W > N/2, zone-aware quorum placement, six-copy design** → ch02 2.20, ch23 23.4
- **Rate limiting reasons, external vs internal limiter** → ch06 6.14
- **Sharding vs partitioning terms** → ch05 5.15
- **Spanner-style commit wait, safe time, leader lease** → ch21, ch23
- **Wide-column store (tablet, root tablet, compaction)** → ch22

## Related Skills

- `coding-with-agents`: working method, verification and LLM mechanics when an agent writes the code of the system.
- `ux-ui-expert`: the interface and flows of the product built on the architecture.
- `workshop-facilitation`: facilitating the session that fixes scope, priorities and acceptance.

## Scope & Limits

Practical theory distilled from transcripts about distributed-systems design, operating-system, network and database internals, post-mortems of published outages, studies of published systems, applied LLM architecture, and opinion-led material on domain modeling, boundaries and event-driven design (marked as position, each with its counter-case), plus studies of published distributed databases, file systems, lock services and blob stores, clock and ordering theory, probabilistic and cache data structures, and the memory side of serving quantized language models. Not covered: GPU kernels, batching schedulers and attention variants for LLM serving, graph and time-series databases, framework- or language-specific implementation, API/REST design details, feature flags and deployment tooling, news-feed ranking in detail, batch-analytics and interactive-query engines, time-series monitoring, tracing, container orchestration internals beyond the cluster-manager study, routing-protocol internals beyond the incident lessons, cryptography mathematics, and security or compliance engineering. Scale figures, vendor limits and model capabilities are snapshots and change quickly; the skill gives no legal, compliance or cost guarantee.
