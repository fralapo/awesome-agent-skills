# Chapter 05: Partitioning, Hashing and Geospatial Indexes

## Core Idea
Splitting data across nodes is easy; splitting it **so that the common request touches few nodes and no node becomes hot** is the design work. In this model the shard key follows the access pattern, hashing spreads load, a ring limits rebalancing, and for physical space a prefix-sortable cell code turns "nearby" into an ordinary range query.

## 5.1 Sharding limits the blast radius
- **Thesis**: with sharding, a node failure harms only its key range.
- **Mechanism**: node A owns users 0-100, B 100-200, C 200-300 (wrapping around). When C fails, only users 200-300 are affected; a replica of C is promoted by a coordinator (data kept in sync with an agreement protocol).
- **Trade-off**: cross-shard queries and transactions become hard.
- **Does not hold when**: the working set fits one machine.

## 5.2 The shard key follows the access pattern
- **Thesis**: choose the key by the lookup you perform 99% of the time.
- **Mechanism**: authorization data is read by object ("who can see this document?") so the object id is the key and all relations of that object (viewer, editor, owner) live in the same shard, rather than splitting by relation. The graph store keys an edge by its source node so "all friends of X" is one shard. The key is hashed to a number that maps to a node.
- **Trade-off**: other lookups (by destination) need an inverse record elsewhere.
- **Does not hold when**: the key has very skewed popularity (5.6).

## 5.3 Consistent hashing and the ring
- **Thesis**: place keys and nodes on the same circle, so adding or removing a node moves only a small part of the data.
- **Mechanism**: hash the key, walk clockwise to the next node. Replicas are placed on the following nodes: with replication 2, a key owned by node 2 also lives on node 3; a key owned by 5 also lives on 1. Any replica can answer reads; if one misses a write, another still has it. A uniform hash gives an even load; a bad hash (for example one that maps half the keys to the same value) overloads one node even when the cluster is large. A second level of hashing inside a hot node is possible but is a patch.
- **Trade-off**: ring metadata must be distributed; replica placement across failure domains needs care.
- **Does not hold when**: ranges must stay ordered for range queries (then use range partitioning).

## 5.4 Failure of one node moves only its share
- **Thesis**: spreading a failed node's range thinly over the ring avoids a herd on one survivor.
- **Mechanism**: with a consistent hashing layout the rebalance is minimal; replicas allow service to continue while partitions move. For rebuildable in-memory data, replication is optional because the index can be rebuilt from the database and live clients.
- **Trade-off**: rebuilding takes time during which requests miss.
- **Does not hold when**: data cannot be rebuilt.

## 5.5 Replicate or shard a cache? Follow the request shape
- **Thesis**: if one user-facing request needs hundreds of keys, sharding the cache multiplies the fan-out; replicating the cache keeps each request on one node.
- **Mechanism**: key-range shards store only popular keys within each range. A page load that needs many keys from many shards creates a multi-node query for every page. Adding full replicas lets each request be answered by one replica, and the total capacity scales with replicas.
- **Trade-off**: replicas hold duplicate data (fewer unique keys fit) and invalidation must reach all copies.
- **Does not hold when**: requests ask for a single key, or the dataset does not fit one node.

## 5.6 Hot keys and hot shards
- **Thesis**: no static partition survives a viral item; detect it and change the path.
- **Mechanism**: a popular person's post may have millions of likes. Splitting by source plus edge type spreads likes, comments and shares but often is not enough. Adding more read replicas does not help when the data **per key** exceeds one shard: an LRU cache would thrash, evicting entries to refill them. The practical response is to let the hot shard's requests go straight to the database instead of through the cache.
- **Trade-off**: database load on the hot path.
- **Does not hold when**: the hot item is small and fits a replicated cache.

## 5.7 Fan-out limits are a design lever
- **Thesis**: capping the number of recipients is cheaper than engineering for unbounded fan-out.
- **Mechanism**: chat groups capped at a few hundred members keep message fan-out manageable; some products cap groups slightly higher. Celebrity-scale posts need batching or pull instead.
- **Trade-off**: product limit.
- **Does not hold when**: the product needs broadcast (then batch and pull).

## 5.8 Routing table: coordinator or gossip
- **Thesis**: someone must know which node owns which partition.
- **Mechanism**: options are a coordination service (consistent but adds a hop), a load balancer holding the map locally, or gossip among nodes (fast, eventually consistent; a request sent to any node is forwarded to the owner). If clients re-send data every few seconds, brief staleness is repaired by itself.
- **Trade-off**: consistency of the map versus latency.
- **Does not hold when**: ownership errors cause correctness problems (use the coordination service).

## 5.9 Geohash: nearby as a range query
- **Thesis**: encode a 2D area into a string where each longer string is a sub-cell of the shorter one, and a sorted index can answer "everything in this cell" as a key range.
- **Mechanism**: a cell like "qr42" splits into children "qr42a", "qr42b" and so on (not necessarily four children). All locations in a cell share the prefix, so a range between two keys covers the cell. In an in-memory store this is a sorted set; in a relational database an ordinary index. A public service can convert latitude and longitude into the code; do not build your own. The cell size is chosen from the search radius.
- **Trade-off**: points near a cell edge are near points in the neighbour cell; the lookup must scan neighbours.
- **Does not hold when**: you need exact road distances (see 5.10) or overlapping regions (use a tree for polygons).

## 5.10 Boundary and precision handling
- **Thesis**: query the surrounding cells, then filter exactly.
- **Mechanism**: query the centre cell plus its eight neighbours (nine disjoint range queries, executable in parallel) with a cell larger than the radius, then compute the exact straight-line distance for each candidate and drop out-of-range ones. For travel time use precomputed distances between popular tile pairs in a periodic batch job, or call a mapping service. A larger search radius means querying a bigger cell or more cells.
- **Trade-off**: constant-factor extra queries (nine) and a filtering step.
- **Does not hold when**: points are sparse and an exact radius query is cheap.

## 5.11 Other spatial structures
- **Thesis**: a 2D space is split either into smaller regions or traversed by a curve.
- **Mechanism**: quadtrees split regions recursively; a space-filling curve (Hilbert) maps 2D to 1D keeping nearness more faithfully; some systems use hexagonal cells. A geospatial extension of a relational database may already do this.
- **Trade-off**: complexity versus accuracy; details beyond these names are unverified.
- **Does not hold when**: a built-in extension is enough.

## 5.12 Location pool lifecycle
- **Thesis**: the live index holds only candidates that can take work now.
- **Mechanism**: couriers send their position every few seconds; the service converts to a cell, writes to the right shard and removes them from the old one; entries expire after a time-to-live (for example ten minutes without update means offline). When a courier is matched they leave the pool and a separate real-time channel starts. Stale-by-seconds data is fine because the food takes minutes to prepare.
- **Trade-off**: simplicity (one task at a time per courier) versus lost optimisations (queueing the next job).
- **Does not hold when**: matching latency is sub-second and positions must be exact.

## 5.13 Why modulo placement fails and how virtual nodes fix the ring
- **Thesis**: placing a key by hash modulo the number of servers is perfect until the number changes, then almost every key moves.
- **Mechanism**: with N servers, key placement is hash mod N; adding or removing one server changes N and remaps nearly all keys, causing a storm of cache misses or data moves. On a ring, servers and keys are hashed into the same space and each key goes to the first server clockwise; adding a server takes only the arc between it and its predecessor, removing one hands its arc to the next. Random points make arcs uneven (one server may take most keys, and after a removal a neighbour's arc doubles), so each server is hashed at many points (virtual nodes) and owns many small arcs; more virtual nodes give better balance at the cost of more metadata. Replication places copies on the next distinct servers clockwise. Used for data partitioning in key-value stores, for spreading content across edge servers and for pinning persistent connections to backends.
- **Trade-off**: balance versus metadata and lookup structure.
- **Does not hold when**: the node set is fixed (modulo is fine) or range queries need ordered partitions.

## 5.14 Spreading a hot key with a compound partition key
- **Thesis**: if the natural key concentrates events on one partition, add a second component that spreads them while keeping order where it matters.
- **Mechanism**: in a partitioned log, messages with the same key land on one partition and stay ordered; partitioning by a popular item makes one partition hot on release night. Use item id plus a hash of the user id: events for the item spread across partitions while each user's events stay ordered. Time-based partitions make retention easy but concentrate current writes. Global ordering means one partition, which removes parallelism (accept partial order).
- **Trade-off**: per-item aggregation now needs a merge across partitions.
- **Does not hold when**: per-key volume is small.

## 5.15 Sharding and partitioning: two words, one scaling path
- **Thesis**: vertical scaling hits a hardware ceiling; past it you split the data across machines.
- **Mechanism**: a single leader with read replicas absorbs growing read load, and a bigger machine absorbs growing writes, until the largest machine is reached (for example 1,500 writes per second wanted where one node tops out at 1,000). Splitting the data over two nodes at half each lets the pair serve more than either can alone, provided traffic is spread evenly. **Partition** is about the data (mutually exclusive subsets); **shard** is about the server holding one or more partitions (several partitions can live on one server, and one partition can move). A partitioning strategy decides the subsets (hash, range, ring, 5.3 and 5.13); uneven access breaks the arithmetic (5.6, 5.14).
- **Trade-off**: cross-shard queries and transactions become hard (ch14 14.9); operations multiply.
- **Does not hold when**: one node already meets the need with replicas.

## 5.16 Moving ring positions instead of adding nodes
- **See** ch22 22.2 for a store in which nodes shift their position on the ring in small steps to relieve a loaded neighbour, and for rack- and data-centre-aware placement.
