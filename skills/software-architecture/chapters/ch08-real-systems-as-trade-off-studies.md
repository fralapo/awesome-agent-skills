# Chapter 08: Real Systems as Trade-Off Studies

## Core Idea
Published system descriptions are most useful as **worked examples of constraint -> decision -> accepted cost**. In this model each study is read with the same questions: what was the load shape, what was given up, and what would break if the requirement changed. Numbers below are as stated in the source and are dated snapshots.

## 8.1 Cluster manager (Borg-style)
- **Problem**: run and heal processes across many data centers; developers should only supply code.
- **Key decisions**:
  - Jobs have priority bands (monitoring, production, batch, free); higher bands preempt lower, and production does not preempt production, which avoids eviction chains (ch03 3.11).
  - Constraints (OS, region) are optional; most users specify none.
  - Isolation is by Linux containers, not VMs (VMs too slow): a root jail for security, resource groups (cgroups) for CPU/memory/storage limits; polite stop signal first, forceful kill later.
  - A **cell** of about ten thousand machines has one master; five in-memory replicas with leader election; state in a consistent store. If the master dies, running tasks continue, only new placement stops.
  - Placement is bin packing: best fit packs tightly but is slow and risky when tasks underestimate needs; first fit is fast but wastes capacity; the system uses a **hybrid** that fits snugly while leaving headroom.
  - A naming service maps task instances to addresses; a job's task states (pending, running, stopped) and health are in the store.
  - Scale tricks: cache machine scores and configuration, group applications into classes (IO-, memory-, CPU-heavy) to avoid recomputation, prefer machines that already hold the needed packages (reported start time from about 25 s to 5 s).
  - Logs stay local and are rotated; metrics go to a time-series store and an analytical SQL system for capacity decisions.
- **Accepted costs**: a central master (mitigated by replication), poor tag/query language compared with its open-source descendant, constraint-solving left to a heuristic.
- **Lessons**: separate control from data plane; use priority and non-preemption rules; cache decision inputs.
- **Does not generalise when**: you have tens of machines (use an off-the-shelf orchestrator).

## 8.2 Managed key-value store (Dynamo-style)
- **Problem**: a fully managed NoSQL service for millions of customers with predictable performance, even with burst and transactions.
- **Key decisions**:
  - Request routers are separate from storage, in the same availability zone as the primary when possible.
  - A distributed metadata cache knows which storage node holds which key; its hit rate is about 99.7%, which makes it the dangerous component (ch03 3.9); clients keep querying the backing store regardless to keep load constant.
  - Writes go to the leader, then two replicas; leader election uses a Paxos variant; some replicas hold only logs.
  - The log streams to object storage and to a stream service for backups, indexes and change capture; global secondary indexes are eventually consistent copies built from the stream.
  - Transactions are offered with a serializable isolation level; strong and eventual reads are both available.
  - Throughput is metered in capacity units with a token bucket (five-minute burst) and admission across replicas (ch04 4.8).
  - The replication protocol is formally verified (tool name unclear in source).
- **Accepted costs**: consistency lag in global indexes; data duplicated; no joins; extra constant load for stability.
- **Lessons**: culture of predictability over peak speed; hide complexity behind a simple key model.
- **Does not generalise when**: the application needs ad-hoc relational queries.

## 8.3 Global authorization (Zanzibar-style)
- **Problem**: answer "may user U do R on object O?" for billions of users and trillions of objects, within tens of milliseconds, with about five-nines availability; over 99% of operations are reads.
- **Key decisions**:
  - A uniform data model of relation tuples: object, relation, user-or-group (for example "document D, editor, group G"); groups nest; the check walks incoming edges to the object and expands groups. Permissions form a hierarchy (owner implies editor implies viewer).
  - Read API with optional fields (source, relation, destination, timestamp) covers "does the relation exist", "all relations", "who can access this", "what can this user access"; the write API is just add/remove a tuple.
  - Consistency by timestamp (ch02 2.10).
  - The store is a globally consistent database holding per-namespace configuration (rules such as maximum editors), tuples and a change log.
  - The serving layer is an in-memory cache sharded by consistent hashing on the **object id**; recent hot lists in memory, the rest durable.
  - A watch service streams changes to listeners; snapshots cut recovery time; an indexing service precomputes group set operations (membership with exclusions) from snapshots plus the change stream.
- **Accepted costs**: several moving parts; precomputed indexes lag a little; clients carry timestamps.
- **Lessons**: model first (a graph written as tuples), shard by the access path, cache in layers, and push set arithmetic out of the hot path.
- **Does not generalise when**: permissions are few and static (a table suffices).

## 8.4 Social-graph store (TAO-style)
- **Problem**: serve more than a billion reads per second on a social graph of petabytes, 99.8% reads, with low latency and easy use.
- **Key decisions**:
  - A data model of **objects** (nodes) and **associations** (typed, timestamped edges); actions map to edges, repeatable entities to objects; each edge has an inverse stored on the other node's shard.
  - No new storage engine: an API layer over a cache fleet backed by a sharded relational database; on a miss or write the layer goes to the database.
  - Minimal API: create/read/update/delete an association; get edges by source and type with limit, time window and paging; count by source and type. Everything else is excluded to protect performance.
  - Shard an edge by its **source id** so a list is local; shard an object by its id; ids are hashed into ranges.
  - Two tiers: a primary shard tier per key range that receives writes and a larger tier of read replicas; reads go to the nearest replica; writes are forwarded through the replica to the primary (ch02 2.11); the database change stream is shipped by a change-capture wrapper to update caches. This cuts write amplification from "all replicas" to "a few primaries".
  - Edge and inverse are written in sequence; leftovers are repaired by a background job (ch02 2.12).
  - Hot shards: route by source plus type; if still too hot, query the database directly (ch05 5.6).
- **Accepted costs**: temporary dangling edges, minimal feature set, replica staleness.
- **Lessons**: build on mastered infrastructure; restrict the API; separate read scale from write path.
- **Does not generalise when**: you need arbitrary graph traversals.

## 8.5 Look-aside cache fleet (memcache-style)
- **Problem**: let hundreds of engineers share one cache that serves a page needing hundreds of keys within about 10 ms.
- **Key decisions**: look-aside with delete-on-write (ch06 6.1); a client library with batching and compression; TCP for sets, UDP for gets; replicate rather than shard to scale (ch05 5.5); client-side sliding windows to throttle; a spare overflow pool; one write region with log-driven invalidation via a daemon that adds cache deletes to the database log; a small number of write nodes and many read nodes.
- **Accepted costs**: stale reads at the margin; some read errors from UDP; duplicated data.
- **Lessons**: choose consistency per path; make the shared platform pleasant to use.
- **Does not generalise when**: a single cache node meets demand.

## 8.6 How to apply a study
- **Thesis**: map your constraints to the studies, copy the **decision**, not the product.
- **Mechanism**: write down your read:write ratio, key access path, latency target, availability target and consistency tolerance; find the study with the closest answers; list its accepted costs and check each is acceptable to you.
- **Trade-off**: studies are from large scales; at small scale the same decisions may be over-engineering.
- **Does not hold when**: your domain differs (batch analytics, interactive analysis, time-series monitoring and tracing were not covered in this material).
