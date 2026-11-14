# Patterns

Recurring situation -> move. Each entry: When / Move / Cost / Not when. Chapter in brackets.

## 1. Vague design brief
**When**: "design X" with no numbers.
**Move**: scope a small feature set; state assumptions; estimate users, rate, storage, read:write; name the dominant constraint; then pick components. [ch01]
**Cost**: time before drawing.
**Not when**: the numbers are already known.

## 2. Reads far exceed writes
**When**: ratio about 100:1 or more.
**Move**: one write path per key range, many read replicas, caches, precomputation, eventual reads. [ch01, ch06, ch08]
**Cost**: stale reads and invalidation machinery.
**Not when**: write-heavy.

## 3. Primary database is a single point of failure
**When**: one database serves everything.
**Move**: add a replica on separate hardware; async if loss of the last transactions is tolerable, sync if not; promote on failure; use the replica for reads. [ch02, ch03]
**Cost**: lag or latency; failover decisions.
**Not when**: data is cheap to rebuild.

## 4. Two writers
**When**: tempted by multi-leader for write availability.
**Move**: avoid unless operations merge; otherwise single leader, or require majority acknowledgement. [ch02]
**Cost**: lower write availability under partition.
**Not when**: conflict-free data.

## 5. Replica missed a write
**When**: reads return "not found" right after creating something.
**Move**: read with quorum (majority of replicas, latest timestamp wins); for the writer, route via the primary. [ch02]
**Cost**: slower reads; a second failure still errs.
**Not when**: stale reads are fine.

## 6. Two shards must change together
**When**: edge + inverse edge, or two entities.
**Move**: write in a fixed order with retries; background job repairs leftovers. [ch02]
**Cost**: brief inconsistency.
**Not when**: harm from the intermediate state.

## 7. Long business workflow
**When**: reserve then settle (orders, metered use).
**Move**: saga: small steps with compensation. [ch02]
**Cost**: intermediate states visible.
**Not when**: one-node transaction suffices.

## 8. Plan availability by size
**When**: setting a target.
**Move**: choose nines for the organisation; remove single points layer by layer (network, servers, database, cache); monitor. [ch03]
**Cost**: money, complexity.
**Not when**: safety domains need more.

## 9. Moving a database
**When**: relocating data to cut latency.
**Move**: rehearse on staging; bulk copy; announce window; war room; one differential query; switch pointer. [ch03]
**Cost**: short planned downtime.
**Not when**: no downtime is allowed.

## 10. A server died and survivors are dying
**When**: cascade risk.
**Move**: headroom, bounded queue per server, reject with temporary/permanent errors, client back-off, serve some users. [ch03]
**Cost**: some failed requests.
**Not when**: elastic capacity arrives first.

## 11. Planned or viral spike
**When**: sale or going viral.
**Move**: pre-scale known events; autoscale uncertain; rate limit viral; cache responses. [ch03]
**Cost**: spend.
**Not when**: traffic is flat.

## 12. Scheduled mass send
**When**: notify everyone at midnight.
**Move**: chunk over minutes; jitter for popular-publisher follow-ups. [ch03, ch07]
**Cost**: later chunks delayed.
**Not when**: delivery time is contractual.

## 13. Cache may go cold
**When**: backend sized for a 99%+ hit rate.
**Move**: constant work (clients keep querying the backend), or warm before use; overflow pool for failures. [ch03, ch06]
**Cost**: steady extra load, spare nodes.
**Not when**: backend can absorb the full miss load.

## 14. Deploys cause outages
**When**: changes ship to every instance at once.
**Move**: roll out in small batches and watch. [ch03]
**Cost**: slower rollout.
**Not when**: breaking schema changes force a parallel switch.

## 15. Metadata counters under load
**When**: views and likes hit the database.
**Move**: serve approximations interpolated from history. [ch03, ch06]
**Cost**: visible mismatch.
**Not when**: money or legal counts.

## 16. Write-heavy store
**When**: many small inserts.
**Move**: batch, append to a log, flush sorted files, compact in background, bloom filter per file. [ch04]
**Cost**: space amplification, background I/O.
**Not when**: read-heavy updates.

## 17. SQL or NoSQL?
**When**: choosing a database.
**Move**: relations, transactions, ad-hoc joins -> relational; data read whole, flexible fields, key access, scale-out -> document/key-value. Model keys by access pattern; denormalise. [ch04]
**Cost**: joins and constraints vanish in NoSQL.
**Not when**: small scale (either works).

## 18. Many access patterns on a key-value table
**When**: need a second sort or lookup.
**Move**: local secondary index (same partition) or global secondary index (copy, eventual). [ch04]
**Cost**: duplication, lag.
**Not when**: one pattern.

## 19. Multi-tenant capacity
**When**: customers share nodes.
**Move**: provisioned units + token bucket with burst; admit globally across replicas. [ch04]
**Cost**: placement headroom.
**Not when**: single tenant.

## 20. Shard key choice
**When**: splitting data.
**Move**: key by the dominant lookup; keep related records together; hash it; consistent hashing; replicas on next nodes. [ch05]
**Cost**: other lookups need inverse records.
**Not when**: range queries needed (use ranges).

## 21. Cache for composite pages
**When**: a page needs hundreds of keys.
**Move**: replicate the cache; batch keys in the client library; look-aside with delete-on-write. [ch05, ch06]
**Cost**: duplicated data.
**Not when**: single-key reads.

## 22. Hot shard
**When**: one item gets huge traffic.
**Move**: split by source + type; if still hot, bypass the cache to the database. [ch05]
**Cost**: database load.
**Not when**: small hot item.

## 23. Nearby search
**When**: find points near a location.
**Move**: cell code (geohash), sorted index, query the cell and eight neighbours, filter exactly; map cells to nodes by consistent hashing; refresh positions every few seconds with TTL. [ch05, ch09]
**Cost**: constant-factor extra queries.
**Not when**: a database geo extension exists.

## 24. Push to clients
**When**: server-originated messages.
**Move**: WebSocket for bidirectional; server-sent events for one-way; dumb gateway + session service. [ch07]
**Cost**: connection memory.
**Not when**: rare updates.

## 25. Delivery receipts
**When**: sent/delivered/read.
**Move**: sent = durably stored; delivered = device ack through gateway and session; read = chat opened; skip group receipts; deprioritise under load. [ch07, ch03]
**Cost**: extra messages.
**Not when**: compliance demands receipts.

## 26. Heavy upload processing
**When**: transformation per upload.
**Move**: return 202, queue, validate, chunk, fan out format x resolution tasks, recombine, replicate, CDN. [ch07, ch09]
**Cost**: delay, storage multiplication.
**Not when**: one cheap transformation.

## 27. Build a platform component
**When**: many teams need a shared tool.
**Move**: build on mastered infrastructure; minimal API; client library; measure adoption. [ch01, ch08]
**Cost**: feature requests refused.
**Not when**: no existing base.

## 28. RAG answer quality is poor
**When**: wrong or irrelevant answers.
**Move**: read traces; fix parsing/chunking with a domain expert; retrieve more; re-rank; decompose; then evaluate with a judge. [ch10]
**Cost**: latency and tokens per step.
**Not when**: pipeline already works.

## 29. Agent loop
**When**: model must act or choose sources.
**Move**: tool descriptions with when/params/returns/examples; loop with iteration cap; tool-call ids; enforce limits in code; log traces. [ch11]
**Cost**: unpredictability, tokens.
**Not when**: fixed workflow.

## 30. Many connected tool servers
**When**: agent has dozens of tools.
**Move**: connect only what the task needs; remember definitions are resent each call. [ch11]
**Cost**: reduced convenience.
**Not when**: few tools.

## 31. Latency rises but CPU is idle
**When**: slow responses, no resource pressure.
**Move**: count connections per host, ports and file descriptors; look for a connection created per request; add a pool or multiplexing; set timeouts. [ch13, ch15]
**Cost**: pool tuning.
**Not when**: the delay is in a slow dependency (trace it).

## 32. Choose a protocol path
**When**: many small requests from browsers or mobile.
**Move**: HTTP/2 or HTTP/3 end to end; layer-4 balancer unless content routing is needed; TLS 1.3; check every proxy supports the version. [ch13, ch16]
**Cost**: UDP and proxy compatibility.
**Not when**: few large downloads.

## 33. Proxy timeouts
**When**: a reverse proxy or balancer fronts backends.
**Move**: set idle, whole-request, connect and per-endpoint response timeouts; shrink them along the chain; give uploads their own route. [ch16]
**Cost**: some slow legitimate calls fail.
**Not when**: the operation is async.

## 34. Cache failure modes
**When**: a hot key, missing keys or a restart sends load to the database.
**Move**: per-key lock or stale-while-refresh, placeholders or Bloom filter, jittered expiry, redundant cache, pre-warm, circuit breaker. [ch06]
**Cost**: extra parts.
**Not when**: the database absorbs the full load.

## 35. Fan-in on hot reads
**When**: thousands of clients read the same item at once.
**Move**: coalesce identical requests in a data-access layer and route them by consistent hash of the entity. [ch16, ch05]
**Cost**: hot instance, in-flight state.
**Not when**: requests are personalised.

## 36. Database slows down over time
**When**: queries degrade, disk grows.
**Move**: find the oldest open transaction, check dead rows and cleaner progress, read the plan for index use, check lock queues. [ch14]
**Cost**: operational attention.
**Not when**: load simply grew (capacity).

## 37. Atomic change across systems
**When**: two databases or services must change together.
**Move**: keep it in one partition; otherwise two-phase commit if blocking is acceptable, or a saga with compensation. [ch14, ch02]
**Cost**: latency, blocking window, visible intermediate states.
**Not when**: eventual consistency with reconciliation is acceptable.

## 38. Self-inflicted overload
**When**: partial failure triggers retries, ejection and autoscaling.
**Move**: back-off with jitter and a retry budget, cap ejected fraction, rate-limit autoscaling, nodes join only when ready, stage restarts. [ch03, ch15]
**Cost**: slower reaction to real loss.
**Not when**: no automation exists.

## 39. Design the recovery path
**When**: reviewing a system or writing an incident follow-up.
**Move**: ask whether tooling, DNS, access and monitoring work when the primary network or identity is down; keep an out-of-band path and a rehearsed procedure. [ch15]
**Cost**: duplicate infrastructure.
**Not when**: outage cost is low.

## 40. Short links or ids
**When**: you need compact unique codes.
**Move**: counter encoded in base 62 (no collisions) or hash plus collision check; cache the read path; temporary redirects if counting clicks. [ch09]
**Cost**: a unique counter service; guessable codes.
**Not when**: random unguessable ids are required.

## 41. Rate limiter
**When**: protect an API.
**Move**: token bucket in a shared in-memory store, atomic update, enforced at a gateway; decide fail-open or closed. [ch09, ch04]
**Cost**: an extra hop and a dependency.
**Not when**: capacity is limited upstream.

## 42. Large uploads and playback
**When**: big media files.
**Move**: signed URL and chunked parallel upload to object storage; workflow graph for transcoding; adaptive streaming with manifests from a CDN. [ch09, ch07]
**Cost**: many derived files.
**Not when**: live streaming.

## 43. Platform upgrade or process model change
**When**: OS, kernel or runtime update; process-per-connection database.
**Move**: benchmark before and after, read default changes, use huge pages, pool connections, consider threads. [ch12, ch14]
**Cost**: benchmark time.
**Not when**: stateless, low-load services.

## 44. CRUD or capability
**When**: a screen edits a record, but the real activity is a workflow (dispatch, load, cancel).
**Move**: ask what the user is trying to do; keep reference data as CRUD; give each capability an explicit command with its rules and a named outcome; record reason and actor. (Position.) [ch17]
**Cost**: more types and screens.
**Not when**: no behavior exists, or an external system owns it.

## 45. Rule over a huge collection
**When**: an invariant such as a maximum member count, with millions of children.
**Move**: enforce the rule, not the relationship: counter in the aggregate, indexed count in a transaction script, a separate membership model, or an application-layer check on a projection (stale). [ch17]
**Cost**: rules in several places; stale option can overshoot.
**Not when**: the collection is small, or a strict limit needs a strongly consistent option.

## 46. Same word, two meanings
**When**: a shared model keeps breaking other modules on change.
**Move**: split by reason to change and language; each boundary owns its concept; link by id; integrate through a contract. (Position.) [ch18]
**Cost**: duplicated data and integration work.
**Not when**: the data is truly identical and changes for one reason.

## 47. Abstraction or direct dependency
**When**: deciding to hide a library, SDK or data access behind an interface.
**Move**: count usages and volatility; abstract hundreds of usages of a volatile dependency or when several implementations exist; use it directly in a handful of places. (Position.) [ch18]
**Cost**: indirection when abstracted; wider change when not.
**Not when**: a shared template or regulation requires the layer.

## 48. How far to decouple
**When**: a procedural flow (save, charge, e-mail) seems "too coupled".
**Move**: pick the step that the business needs: direct call, interface, queue, events; change user-facing wording to "accepted" when going asynchronous. [ch18]
**Cost**: complexity moves, not removed.
**Not when**: the flow is simple and must succeed or fail together.

## 49. Pain after adopting events
**When**: debugging, ordering, stale screens, cost complaints.
**Move**: check the boundaries and event naming first: business facts, not CRUD; user's own changes synchronous; policy for out-of-order workflow events; HA and outbox for the broker; events can run inside a monolith. (Position.) [ch19]
**Cost**: modeling and redesign effort.
**Not when**: the system is request-response CRUD that needs no events.

## 50. Publishing state and an event together
**When**: a state change must reliably announce a fact.
**Move**: outbox in the same transaction; relay publishes; idempotent consumers. [ch19, ch07]
**Cost**: table, relay latency, at-least-once duplicates.
**Not when**: best-effort telemetry, or the log is the state.

## 51. Event contract design
**When**: other boundaries consume your events.
**Move**: publish integration events as summaries, not the schema or every internal step; avoid leaking internal codes; include what consumers need to react; add a new event when the concept differs. (Position.) [ch19]
**Cost**: a mapping step.
**Not when**: one team, stable event; or a fat event feeding reports.

## 52. Stale screen after a save
**When**: the user does not see their own change.
**Move**: read the primary, route elsewhere, add the new id locally, wait for lag or update the projection in the command, or pass a log position; push or poll. [ch19, ch02]
**Cost**: latency or primary load.
**Not when**: the reader is someone else or a report.

## 53. Heavy read composition
**When**: queries join many sources at runtime.
**Move**: CQRS as separate read path: materialized view in the same transaction (consistent) or async projection; do not confuse with read replicas. [ch19]
**Cost**: two code paths; projection lag if async.
**Not when**: one model is enough.

## 54. Data needed from another boundary
**When**: a service wants another's data for display or for a decision.
**Move**: display: compose in the UI or build a purpose-shaped projection; decision: let the deciding boundary own the data it needs, from events. Do not copy the other schema. (Position.) [ch18]
**Cost**: eventual consistency, composition latency.
**Not when**: reporting into a warehouse (replicate freely).

## 55. Multi-tenant isolation choice
**When**: tenants share a system.
**Move**: list what to isolate (data, compute, deploy, schema changes, performance, failure); try per-tenant rate limits and pools before splitting; pool by tenant size; isolate for blast radius, compliance, dedicated capacity or safer rollouts. [ch18]
**Cost**: N times the operations when dedicated.
**Not when**: few similar tenants (shared is fine).

## 56. Double charge despite a unique constraint
**When**: a handler calls a payment or other external system and also dedupes messages.
**Move**: provider idempotency key; lookup by reference; lock per business key; pending state plus outbox; reconcile or compensate; aim at effectively once. [ch20, ch14]
**Cost**: throughput or complexity per layer.
**Not when**: the provider already guarantees idempotency for the call.

## 57. Pending forever with a third party
**When**: a timeout leaves an order "payment pending" though the provider charged.
**Move**: saga timeout triggers reconciliation: read the provider's truth, then confirm or cancel; also a user button and a polling fallback. [ch20]
**Cost**: provider query API, polling calls.
**Not when**: you own the truth in one database.

## 58. Guarantee across services over time
**When**: a unique name, last item or amount must be held during a multi-step process.
**Move**: reservation with reserve, confirm and expire; or move the data to the deciding boundary so one transaction suffices. [ch20, ch02]
**Cost**: reservation service is a dependency; choose lifetime.
**Not when**: one database constraint covers the process.

## 59. Nightly batch job
**When**: a scan finds items to expire, remind or refund.
**Move**: at the triggering event send a delayed message; on arrival re-read state and exit early if done; reschedule if recurring. (Position.) [ch20, ch07]
**Cost**: message per item; broker-specific delay limits.
**Not when**: set-based work (reporting, ETL) or enormous item counts.

## 60. Event sourcing in a legacy system
**When**: wanting history and domain events in an old code base.
**Move**: define a boundary, extract it as a service behind a contract, then experiment inside; do not weave it through the old code. (Position.) [ch17, ch19]
**Cost**: interface between old and new.
**Not when**: the system is small enough to rebuild, or has no value in history.

## 61. Last-write-wins is losing data
**When**: replicas resolve conflicts by wall-clock timestamp.
**Move**: accept it only for idempotent or single-writer keys; otherwise use version vectors with siblings, mergeable data types, or one leader per key range. [ch21, ch22]
**Cost**: read-before-write or merge logic.
**Not when**: losing one of two near-simultaneous writes is acceptable.

## 62. A lock holder that was paused
**When**: a lease or lock protects a shared resource and a process can stall (garbage collection, migration).
**Move**: issue a monotonically increasing token with each grant; the resource rejects lower tokens. If it cannot check tokens, add a delay after release and keep operations idempotent. [ch21, ch22]
**Cost**: the resource keeps one number.
**Not when**: the work is safely repeatable.

## 63. Exactly one of something
**When**: unique name, leader, lock.
**Move**: linearizable store on a consensus log, or a single owner per key; weaker consistency cannot enforce uniqueness at write time. [ch21, ch02]
**Cost**: write latency, availability only with a majority.
**Not when**: a later rollback of a duplicate is acceptable.

## 64. Atomic write over partitions without a coordinator single point
**When**: two partitions must commit together.
**Move**: two-phase commit where each participant is a replicated group and the decision is logged first; or put the commit point in one cell and roll forward or back from it. [ch21 21.10, ch23]
**Cost**: extra round trips, locks held.
**Not when**: one partition holds the data or a saga fits.

## 65. Availability first, repair later
**When**: reads and writes must never refuse (carts, sessions).
**Move**: leaderless replicas, sloppy quorum with hinted handoff, read repair, background hash-tree comparison, siblings merged by the application. [ch22]
**Cost**: conflicts and stale reads.
**Not when**: money or uniqueness is involved.

## 66. Hot partition in a metered service
**When**: one key or range takes more than its share.
**Move**: bank unused capacity (bursting), let a controller rebalance limits, hand out tokens in proportion to observed load, move other partitions off the node; do not split a partition that is hot because of one key. [ch22 22.3]
**Cost**: accounting layer.
**Not when**: load is uniform.

## 67. Skip the lookup that cannot succeed
**When**: most queries hit absent keys or absent files.
**Move**: Bloom filter in front of the store or file; confirm "maybe" against the source of truth; rebuild larger when it fills. [ch24 24.2]
**Cost**: false positives, no deletion, rebuild for growth.
**Not when**: a false positive is harmful and unchecked.

## 68. A table scan wiped my cache
**When**: a one-off scan evicts hot pages.
**Move**: split the recency list into young and old; insert at the head of the old list; promote on re-reference. [ch24 24.7]
**Cost**: one more tuning knob.
**Not when**: scans are rare.

## 69. Eviction without a linked list
**When**: memory is better spent on data than on list pointers.
**Move**: coarse per-object clock, sample a few keys, keep the worst in a small sorted pool; for frequency use a logarithmic probabilistic counter with decay at access time. [ch24 24.4-24.5]
**Cost**: approximate choice.
**Not when**: exact order has business meaning.

## 70. Count distinct at scale
**When**: unique visitors or items in a stream.
**Move**: hash, record trailing-bit pattern in small registers, combine estimates; keep exact counts only where money or law needs them. [ch24 24.3]
**Cost**: a few percent error, no member list.
**Not when**: exact value required.

## 71. Exactly-once between two topics
**When**: read, process, write to another topic.
**Move**: idempotent producer, transactional id with epoch, atomic commit of outputs and input offsets; for external stores use an idempotent write instead. [ch07 7.18]
**Cost**: coordination latency.
**Not when**: the consumer is idempotent already.

## 72. Stream job that must survive a node loss
**When**: stateful operators over replayable inputs.
**Move**: checkpoint barriers injected into inputs, align at multi-input operators, durable snapshots, replay after the barrier; do not depend on cross-partition order; use event time with watermarks. [ch07 7.19]
**Cost**: alignment stalls, storage.
**Not when**: state can be recomputed cheaply from the log.

## 73. Replicas placed by count, not by failure domain
**When**: three replicas on three machines in one zone, or quorum sizes chosen only for overlap.
**Move**: spread across zones, make W more than half of N, size repair units small so repair is far faster than the next fault. [ch02 2.20, ch23 23.4]
**Cost**: more copies.
**Not when**: data is rebuildable.

## 74. Hosting a model with too little memory
**When**: weights plus cache do not fit.
**Move**: quantize weights offline to a lower bit width, quantize the cache, measure quality on your own task, keep the high-precision original as reference. [ch25]
**Cost**: some quality, a conversion step.
**Not when**: memory is not the bottleneck.

## 75. Immutable blocks, no consensus
**When**: storing huge immutable objects cheaply.
**Move**: content-hash naming, append-only buckets, synchronous write to every replica of a volume, retry on another volume after a failure, a generation number as the commit point, erasure coding once a bucket closes. [ch23 23.5]
**Cost**: wasted partial writes until cleaned.
**Not when**: objects are mutable or need transactions.
