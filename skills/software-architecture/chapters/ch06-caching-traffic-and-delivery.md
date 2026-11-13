# Chapter 06: Caching, Traffic Shaping and Delivery

## Core Idea
A cache is a bet on the access pattern. In this model the best caches are simple (look-aside), make invalidation idempotent (delete, do not update), protect themselves from overload and from cold starts, and are shipped with a client library that hides all the sharp edges.

## 6.1 Look-aside cache
- **Thesis**: keep the cache next to the database, not in front of it, and let the caller (via a library) fill it.
- **Mechanism**: read: ask the cache; on a miss read the database and set the cache. Write: update the database first, then **delete** the cache entry. Deleting is repeatable; if the delete fails you can retry as often as needed, and the next read repopulates. Setting a new value would require handling retries and concurrent updates.
- **Trade-off**: a read after a write pays a miss; a race can still leave stale data for a moment.
- **Does not hold when**: write-heavy keys where deletes cause constant misses.

## 6.2 The client library is part of the product
- **Thesis**: adoption goes up when the caller imports a library instead of using raw requests.
- **Mechanism**: the library builds requests, handles the look-aside logic, compresses, and **batches many keys into one request**; page loads that need hundreds of keys cost one round trip. Contract changes arrive as a library version bump.
- **Trade-off**: the platform team maintains a library per language.
- **Does not hold when**: only one caller exists.

## 6.3 Different transports for different operations
- **Thesis**: reliability is needed for writes, not necessarily for reads.
- **Mechanism**: sets go over TCP, which acknowledges and keeps order, so "set key to 1, then to 2" ends at 2. Gets go over UDP: no connection state per client (more memory for data, millions of clients), no head-of-line blocking, lower latency; if packets arrive out of order or are lost, the client treats it as an error and moves on. Over UDP two sets could be processed out of order, which is why sets avoid it.
- **Trade-off**: some reads fail and are retried or fetched from the database; kernel tuning for connection counts.
- **Does not hold when**: the network drops packets frequently.

## 6.4 Throttle at the client with a bounded queue
- **Thesis**: the cache must be protected from bursts by the callers.
- **Mechanism**: each client keeps a bounded window of in-flight requests; excess requests are dropped instead of queued. Too large a window means old requests wait and the end user retries anyway; too small drops everything on arrival (see ch03).
- **Trade-off**: dropped requests surface as errors upstream.
- **Does not hold when**: callers cannot tolerate errors.

## 6.5 Spare nodes for failures
- **Thesis**: a small overflow pool serves keys of failed nodes (ch03 3.10).
- **Mechanism**: about one percent of nodes are reserved; they talk to the same database; after a failure the client asks them.
- **Trade-off**: poor locality, idle capacity.
- **Does not hold when**: many nodes fail at once.

## 6.6 Cross-region invalidation without write fan-out
- **Thesis**: send writes to one primary database and invalidate caches through the database's own log, so a write does not fan out to hundreds of servers.
- **Mechanism**: a write hits one database in one region; its change log is tailed by a daemon that adds cache invalidation commands and ships the log to other regions, which replay it. Reads vastly outnumber writes (orders of magnitude), so only a few primary databases are needed and many read nodes. Without this, every write would update many databases and caches at once.
- **Trade-off**: read nodes are eventually consistent; brief staleness.
- **Does not hold when**: writes are as frequent as reads.

## 6.7 Multi-level lookup and precomputed set operations
- **Thesis**: serve the common case from memory and precompute what is expensive.
- **Mechanism**: keep recent, frequently used relations in memory and the rest in durable storage; complex group arithmetic (members of one group excluding another) is precomputed by a background indexing service from snapshots and updated by the change stream. A tiny fraction of requests reach the slowest path.
- **Trade-off**: index freshness versus latency, and an extra system.
- **Does not hold when**: queries are simple lookups.

## 6.8 The CDN
- **Thesis**: put copies of static content close to users; it cuts latency and removes a regional single point of failure.
- **Mechanism**: store files in object storage, replicate to regions, front with a CDN; edge caches keep popular files. The video-serving service chooses the right file variant by device, format, bandwidth and region and returns links; the device streams from the CDN. Use a provider unless scale justifies building one (ch01 1.10). Whether a provider offers an API to push or purge cache entries is unclear in source.
- **Trade-off**: vendor service levels and cost; purge control.
- **Does not hold when**: content is dynamic and personalised.

## 6.9 Request router and load balancing
- **Thesis**: separate "where does this request go?" from "where is the data?", while keeping them close.
- **Mechanism**: a router asks a metadata cache which storage node owns the key and forwards there, preferring the same availability zone as the primary; a load balancer spreads requests across servers, can add/remove servers dynamically and retry another server on failure. Local-first with fall-back to another region.
- **Trade-off**: extra hop; the router and its metadata cache are on the critical path (ch03 3.9).
- **Does not hold when**: a single server suffices.

## 6.10 Counters and metadata can be approximate
- **Thesis**: non-core numbers do not need to be exact.
- **Mechanism**: show views and likes interpolated from earlier values and the growth curve; refresh occasionally.
- **Trade-off**: users may see a number that differs from reality.
- **Does not hold when**: the number is money or a legal count.

## 6.11 Do not couple to another service's data casually
- **Thesis**: caching another service's data speeds you up but ties your correctness to theirs.
- **Mechanism**: caching a profile picture for an hour is harmless; caching an authentication outcome could let a changed-password attacker through.
- **Trade-off**: speed versus freshness and security.
- **Does not hold when**: the data is public or very slow-changing.

## 6.12 Three cache failure modes: stampede, penetration, avalanche
- **Thesis**: the cache protects the database only while it works; each failure mode sends the whole load to the database in a different way.
- **Mechanism**: **Stampede**: one hot entry expires and many requests recompute it at once. Mitigate with a per-key lock (others wait, get a not-found with client back-off, or are served a stale copy), with a separate refresher process, or with probabilistic early refresh (each request has a small, growing chance to refresh before expiry). **Penetration**: requests for keys that do not exist miss the cache and the database every time; cache a placeholder with a short time-to-live, or check a Bloom filter of existing keys first (a negative answer is definite; false positives only cost a miss). **Avalanche** (or crash): many different keys expire together, or the cache restarts empty or fails, and everything lands on the database; stagger expiry with random jitter, run a redundant cache cluster, pre-warm before taking traffic, and add a circuit breaker so the database is not buried while it recovers (users who refresh make it worse).
- **Trade-off**: locks and refreshers are extra parts; placeholders use memory.
- **Does not hold when**: the backing store can absorb the full miss load (ch03 3.9 constant work).

## 6.13 Balancing
- **See** ch16 16.4 for static and dynamic balancing algorithms and ch16 16.5 for request coalescing with hash routing.
