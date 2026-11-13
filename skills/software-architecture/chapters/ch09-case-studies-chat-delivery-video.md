# Chapter 09: Case Studies - Chat, Delivery Matching, Short Video

## Core Idea
Three worked designs, each presented as: **requirements -> estimate -> key decision -> alternatives rejected -> cost accepted**. They reuse the mechanisms from earlier chapters; the point is the order of reasoning. A news-feed case is not part of this material; for it, apply ch06 (cache/fan-out), ch05 (fan-out limits, hot keys) and ch07 (batching).

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

## 9.4 Reasoning template distilled from the three cases
- **Thesis**: the same eight questions solve most new problems.
- **Mechanism**: (1) scope; (2) numbers; (3) read:write; (4) access path; (5) keys and shards; (6) transport; (7) failure and overload; (8) accepted costs. Then name what you would revisit if the numbers grew ten times.
- **Trade-off**: a template can hide problem-specific traps.
- **Does not hold when**: the problem is mostly algorithmic, not architectural.
