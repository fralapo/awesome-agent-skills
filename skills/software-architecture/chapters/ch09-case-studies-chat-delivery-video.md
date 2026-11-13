# Chapter 09: Case Studies - Chat, Delivery Matching, Video, Links, Rate Limits

## Core Idea
Six worked designs (9.1-9.3 first, then 9.5-9.7 added later), each presented as: **requirements -> estimate -> key decision -> alternatives rejected -> cost accepted**. They reuse the mechanisms from earlier chapters; the point is the order of reasoning. A news-feed case is not part of this material; for it, apply ch06 (cache/fan-out), ch05 (fan-out limits, hot keys) and ch07 (batching).

## 9.1 Chat service (one-to-one, groups, receipts, last seen)
- **Requirements**: one-to-one messages; group messages (cap a few hundred); sent/delivered/read marks; last seen; history temporary or permanent (a policy question: privacy and storage vs compliance).
- **Core design**:
  1. Device connects to a gateway over a persistent connection (WebSocket).
  2. Gateway forwards unparsed messages; a parser converts to the internal format.
  3. A session service stores user-to-gateway mapping and routes.
  4. A durable chat store holds the message; the sender gets "sent".
  5. Delivery and read receipts return along the same path (ch07 7.3).
  6. A last-seen service records user-initiated activity (ch07 7.4).
  7. A group service resolves members; consistent hashing on group id (ch07 7.5).
  8. A queue retries failed group sends with idempotent message ids.
- **Alternatives rejected**: Long polling over plain request/response (not real-time); keeping connection mapping inside gateways (memory, coupling).
- **Cost accepted**: group receipts omitted; extra service hops.
- **Peaks**: drop last-seen and receipts first; never drop the send.
- **Does not apply when**: end-to-end encryption or multi-device sync dominates (not covered here).

## 9.2 Delivery matching with location
- **Requirements**: place an order; match a nearby courier; see each other's location. Excluded: payments, onboarding.
- **Estimate**: 10 million active users, 10 million orders a day, about 20 deliveries per courier per day, so about 500 thousand couriers; the user table is a few gigabytes, so the design problem is location, not size.
- **Core design**:
  1. A relational database holds users (replicated, single leader; failover coordinated by a consensus-based service). A wide-column NoSQL store (log-structured writes, leaderless replication) was an option but unnecessary unless create-account speed mattered.
  2. Restaurants are geohashed at onboarding; couriers send location every few seconds through an update service, which converts to a cell and writes to the right shard (removing the older entry).
  3. Geo-shards are in-memory sorted sets, one index per region; cells of a fixed size (for example a few kilometers) are mapped to servers by consistent hashing; the partition map is held by a coordination service or by gossip.
  4. Matching: query the restaurant's cell and its eight neighbours, filter by exact distance, rank with a scoring function; expand to larger cells if none found; give up after a configured distance.
  5. Matched couriers leave the pool; a real-time channel (WebSocket if bidirectional, server-sent events if one-way) carries locations; a balancer puts both parties on the same server.
  6. Courier entries expire by time-to-live.
- **Alternatives**: geospatial database extension (try first), quadtree, Hilbert curve; peer-to-peer or UDP location streaming (loss is tolerable).
- **Cost accepted**: slightly stale positions; no replicas for the in-memory index (rebuilt quickly); one job per courier at a time.
- **Does not apply when**: batching several orders per courier is a requirement.

## 9.3 Short-video upload and distribution
- **Requirements**: upload short videos (length capped), distribute to feeds worldwide; availability and fault tolerance over strict consistency; upload fast, visibility within minutes.
- **Estimate**: 10 million daily viewers, about 100 thousand creators, so about 100:1 reads to writes; about 200 thousand uploads a day, about 1 MB each, multiplied by formats and resolutions (ch01 1.4).
- **Core design**:
  1. Upload service accepts and queues requests (202 accepted).
  2. Pipeline: validate and moderate; chunk if long; convert to each format and resolution in parallel by workers; recombine; store.
  3. Stores: object storage for files, relational for users, key-value/document for metadata (ch04 4.6).
  4. Replicate files across regions; front with a CDN (use a provider unless scale justifies a private one).
  5. A video-serving service picks the file by location, bandwidth and device, returns a metadata list (titles, thumbnails) from the metadata store, cached for hot videos; the device streams the file from the CDN.
  6. Upload as a chunked, secure transfer over TCP.
- **Cost accepted**: eventual visibility; many files per video; multi-copy storage; vendor dependence.
- **Review feedback pattern**: give cost estimates and the transport choice early.
- **Does not apply when**: live streaming or editing after upload is required (files are immutable here).

## 9.4 Reasoning template distilled from the cases
- **Thesis**: the same eight questions solve most new problems.
- **Mechanism**: (1) scope; (2) numbers; (3) read:write; (4) access path; (5) keys and shards; (6) transport; (7) failure and overload; (8) accepted costs. Then name what you would revisit if the numbers grew ten times.
- **Trade-off**: a template can hide problem-specific traps.
- **Does not hold when**: the problem is mostly algorithmic, not architectural.

## 9.5 URL shortener
- **Requirements and numbers**: 100 million new links per day is over a thousand writes per second; reads outnumber writes, so about ten thousand redirects per second; ten years is about 365 billion links, tens of terabytes for the mappings alone.
- **Design**: the short code uses 62 symbols (digits and both letter cases); 62^7 is about 3.5 trillion, comfortably more than 365 billion, so seven characters. Two ways to produce it: (a) hash the long URL and keep seven characters: simple but collides, needing a lookup and retry for each new link; (b) take the next number from a unique counter and encode it in base 62 (repeated division by 62, remainders read backwards): no collisions and no existence check, but the counter must be generated uniquely across servers and codes are guessable in order (add a permutation or random offset if enumeration matters). Redirect path: cache first, then database, then fill the cache; return a permanent redirect (the browser may skip the service next time, which hides later analytics and edits) or a temporary one if clicks must be counted. Scale: replicas for reads (about ten thousand lookups per second per database server), then shard by code. Extras: rate limiting, analytics, malicious-link blocking.
- **Does not apply when**: links must expire, be editable or counted per click (choose temporary redirects and an event stream).

## 9.6 Rate limiter
- **Requirements**: configurable rules (for example 100 per minute per user, different tiers), reject with 429 and headers showing remaining quota and reset time, check under a few milliseconds at the 95th percentile, highly available and shared by many servers.
- **Algorithms**: a fixed window counter is simplest but lets a user spend two windows' quotas around a boundary (200 requests in 20 seconds). The token bucket (capacity = burst size, refill rate = sustained rate) allows bursts after quiet periods without exceeding the average; sliding-window and leaky-bucket variants also exist. Placement: client side cannot be trusted; inside each service mixes limits with business logic; a middleware or gateway centralises policy (best default, ch16 16.6). State lives in a shared in-memory store (ch04 4.13), not the database (too slow) and not per server (limits multiply by server count). Two servers reading then writing a counter lose updates; make the read-check-decrement atomic with a server-side script. Open questions to settle: fail open or closed when the store is down, multi-region latency, hot keys from a few heavy users, live rule updates.
- **Does not apply when**: capacity limits are enforced by upstream providers, or the limit is global to one shared resource (then use admission control, ch04 4.8).

## 9.7 Video platform: direct uploads, a workflow graph and adaptive streaming
- **Requirements**: very large uploads (minutes of 4K video range from a couple of gigabytes compressed to tens of gigabytes uncompressed) that are resumable; playback that adapts when bandwidth falls from tens of megabits to a few.
- **Design**: (1) Upload: the API server issues a time-limited signed URL and the client sends chunks (a few megabytes each, each with a content hash, several in parallel) straight to object storage, so application servers do not carry gigabytes of pass-through traffic and a failed chunk is retried alone. (2) Processing: one upload becomes 15 to 20 files (resolutions from very small to 4K, several codecs trading bandwidth against device support, containers for compatibility). Model it as a directed acyclic graph: split at key frames (independently decodable frames every few seconds) into segments; segment, audio, thumbnail and subtitle tasks run in parallel on a worker farm; stages feed the next. (3) Streaming: the player reads a master manifest listing formats, then a media manifest per format listing segment URLs, measures download speed on recent segments and picks the next segment's quality; range requests allow seeking; segments are served from a CDN near the viewer. (4) Open topics: viral videos (metadata caching, hot rows), cost (transcode popular formats first, others on demand, tiering to cold storage), pipelining processing while the upload is still arriving.
- **Does not apply when**: live streaming (segments are produced in real time) or private files (skip the ladder).
