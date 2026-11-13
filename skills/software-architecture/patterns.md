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
