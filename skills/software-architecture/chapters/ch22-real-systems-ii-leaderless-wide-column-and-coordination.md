# Chapter 22: Real Systems II: Leaderless Stores, Wide-Column Stores, File Systems and Lock Services

## Core Idea
Continues the method of ch08: read each published system as **constraint -> decision -> accepted cost**, and copy the decision, not the product. This chapter covers the leaderless key-value family and its descendants, a hot-partition story from a managed service, a large-file store with a single metadata master, a lock service built on consensus, and a wide-column store layered on top of them. Figures are dated snapshots; "(unverified)" marks gaps.

## 22.1 Leaderless key-value store: availability over consistency
- **Problem**: shopping carts, sessions, preferences and catalogue entries need always-on reads and writes, with primary-key access only, small values, no joins and no multi-row transactions; the single-leader, semi-synchronous relational setup of the time stopped accepting writes when the synchronous replica or the leader's data centre failed.
- **Key decisions**:
  - Design principles: incremental scalability (add nodes with a button), **symmetry** (every node does the same job, no metadata master), heterogeneity (work proportional to hardware). Latency target stated at the 99.9th percentile, because a page fans out to about 150 services and the slowest straggler sets the page time (dated figure); beyond the 99.9th percentile effort has diminishing returns.
  - Keys on a consistent-hash ring with several random tokens per node (ch05 5.3, 5.13); the **preference list** is the first N distinct nodes clockwise, ideally across data centres; every node knows the ring through gossip.
  - Tunable quorum: N replicas, W acknowledgements for a write, R replies for a read, with W + R > N for overlap; a small W or R lowers latency (you wait for fewer stragglers) at the cost of durability or freshness (ch02 2.7).
  - Conflict detection with **version vectors**: a write must be coordinated by a node in the preference list so it can increment its own counter; one coordinator for all writes would kill availability and symmetry. A common optimisation: after a read, coordinate the next write at the replica that answered fastest with fresh data, so conflicts are less likely. Concurrent versions are kept as **siblings**; *syntactic* reconciliation merges automatically (mergeable data), *semantic* reconciliation hands both to application logic. Reported: for the cart service 99.94% of requests saw a single version.
  - **Sloppy quorum with hinted handoff**: if preference-list nodes do not answer, walk further clockwise and write to the next available node, which stores the data apart with a hint and hands it back when the owner returns. Writes stay available; the overlap guarantee of the quorum is gone, conflicts become likelier.
  - Repair: **read repair** (the read coordinator sees a stale replica and pushes the newest value) and **anti-entropy** with hash trees: compare root hashes of two replicas, descend only into differing subtrees, reconcile the differing rows.
  - Ring weakness noted: adding a node removes a range from each of several neighbours, forcing them to rebuild their hash trees and scan their local store to find what to send, which is costly (see the fix in 22.3).
- **Accepted costs**: possible conflicts and siblings; clients or applications must merge; version vectors grow with the preference list; availability bought with weaker guarantees.
- **Lessons**: choose availability explicitly, make the quorum a per-use-case knob, and keep every node identical.
- **Does not generalise when**: you need transactions, uniqueness or ad-hoc queries (ch02, ch14).

## 22.2 A wide-column descendant versus the leaderless original: what changed and why
- **Problem**: keep the leaderless, quorum-based wide-column model but cut write cost and operational friction.
- **Key decisions**:
  - **Timestamps instead of version vectors**: a client never reads before writing, so write throughput is highest and the protocol is simple; the cost is last-write-wins loss (21.3). Stores in this family accept it for availability and write rate.
  - Data model: partition key plus sort key within a partition; atomicity only at row level in the studied version; a multi-replica write is not applied in the same order everywhere, so the store is not linearizable.
  - Reads: quorum or closest replica (stale possible), with read repair; writes acknowledged synchronously by a quorum or asynchronously (details unverified).
  - Storage: log-structured merge trees and immutable sorted files (ch04 4.4).
  - Partitioning: nodes may **move along the ring** in small steps to relieve loaded neighbours, transferring data with kernel-level zero-copy; parallel transfer from several replicas was listed as future work (dated).
  - **Replication policies**: rack-unaware (next nodes on the ring), rack-aware (spread across racks) and data-centre-aware (spread across nearby data centres), because adjacent ring nodes may share a failure domain. Choosing placement is done by an elected leader through a coordination service, a deliberate departure from full symmetry: a single decision-maker simplifies reasoning even though it makes failover relevant (position of the designers).
  - Membership by **gossip** over UDP with non-blocking I/O; failure detection with a **probabilistic accrual detector**: instead of a binary up/down it computes a suspicion level from observed heartbeat arrival and a tunable threshold; reported detection time about 15 s against about 2 minutes for a fixed-timeout detector in the same cluster (dated).
  - Sloppy quorums are used, as in the original; new nodes find the cluster through seed nodes (hard-coded or kept in the coordination service).
- **Accepted costs**: clobbered writes, a coordination-service dependency for topology, weaker consistency.
- **Lessons**: drop machinery you can afford to lose (version vectors), and centralise only the decisions that are hard to make symmetrically.
- **Does not generalise when**: lost updates are unacceptable; use a conflict-free data type, a single leader, or consensus per key range.

## 22.3 A managed key-value service versus the leaderless original
- **Problem**: offer the model as a multi-tenant service with provisioned throughput, strong reads on demand and no operator burden, without exposing hot partitions to customers.
- **Key decisions**:
  - Unlike the paper store, each partition has a **leader with consensus-based replication** (a leader and two followers, quorum of two), leader leases so the leader can serve strongly consistent reads alone, eventually consistent reads from followers; storage nodes keep a B-tree and a write-ahead log on SSD across availability zones; request routers, a metadata service, an auto-admin component for health and replica replacement.
  - **Hot-partition evolution**, each step fixing the previous one's defect:
    1. *Equal split of provisioned throughput*: easy placement (a node checks its local capacity) but a hot key's share shrinks after every split, so customers over-provisioned (load dilution).
    2. *Bursting*: unused capacity is banked in token buckets (a few minutes of burst), at partition and node level; writes drain the buckets of every replica written; useless for sustained skew.
    3. *Adaptive capacity*: a controller reshapes per-partition limits within the table's total; reactive, since it waits for throttling.
    4. *Global admission control*: sharded, in-memory controllers hand tokens to request routers in proportion to observed load per partition; state is ephemeral and rebuilt in seconds; routers must refresh tokens regularly.
  - Storage nodes watch their own load (a threshold such as 80%) and ask the admin component to **move** partitions elsewhere (never two replicas of one partition on one node). A partition hot because of **one key or one key range** is not split (splitting helps nothing); other partitions are moved off the node. Splits are placed by observed load, not equal provisioned throughput.
- **Accepted costs**: more components, a token-accounting layer, extra data movement.
- **Lessons**: meter at the edge, move rather than split for single-key heat, and keep control-plane state rebuildable. See ch04 4.8 and ch05 5.6.
- **Does not generalise when**: you run your own single-tenant cluster with uniform keys.

## 22.4 Large-file store with a single in-memory master
- **Problem**: store huge files cheaply on commodity machines that fail daily, mostly sequential reads and appends.
- **Key decisions**:
  - Files split into fixed large **chunks** (64 MB, stated): little metadata per file, long-lived connections for sequential access, few master lookups, little fragmentation because files are huge.
  - **One master** keeps file-to-chunk and chunk-to-server maps in memory (small records per chunk, prefix-compressed names), so it is fast; chunk servers hold the data on ordinary local file systems and the OS cache. Default three replicas, re-created elsewhere if one is lost; the master heartbeats chunk servers.
  - **Operation log**: all metadata changes go to a log replicated synchronously (in the original), replayed on restart; checkpoints of the in-memory state are taken in the background from rotated, immutable log files so recovery is checkpoint plus tail. **Chunk locations are not logged**: on startup the master asks every chunk server what it holds.
  - Reads: ask the master (it may return the next chunks too), cache the answer with a TTL, read from any replica; a stale replica can miss only recent appends.
  - **Writes separate data flow from ordering**: the client pushes data to the closest replica, which **pipelines** it to the next closest, so the network is used fully and the data is buffered in memory; then the **primary** (a replica holding a time-limited **chunk lease**, 60 s initial, extended through heartbeats) picks one order for concurrent writes and tells the secondaries to apply in that order. Without the primary's order, two clients writing in opposite directions leave replicas disagreeing.
  - A write that fails on some replicas is retried by the client; a replica found stale by heartbeat comparison is replaced.
  - Each chunk has its own primary, so ordering holds within a chunk, not across chunks; how multi-chunk writes are reconciled is unverified (consistency is relaxed by design).
- **Accepted costs**: a metadata ceiling on the master, relaxed consistency, clients must cope with duplicates and gaps.
- **Lessons**: keep the master off the data path, make metadata rebuildable from the nodes, separate bulk transfer from ordering.
- **Does not generalise when**: files are small and many, or applications need strict consistency (later systems moved the master's log to consensus).

## 22.5 Lock service on consensus: coarse locks, consistent caching, tokens
- **Problem**: application teams need leader election, configuration and naming with strong consistency, without each implementing consensus; the number of application instances should scale independently of the number of consensus nodes (a quorum over 99 nodes is slow).
- **Key decisions**:
  - A **cell** of five replicas, one master serving all reads and writes; data model of small files (size capped, 256 KB stated, because clients abused it) in a path namespace; **advisory** locks (you may read a file without holding its lock, useful for debugging); **ephemeral** nodes that live while the client holds the handle.
  - **Coarse-grained** locks (held for hours or days: primary election) are the use case; a failover of 5 to 30 s is tolerable there.
  - **Consistent client caching**: before a write completes, the master invalidates every client's cached copy and waits for acknowledgement, so no client reads stale data; this removes the dilemma of DNS-style TTLs (long TTL: wrong address for long; short TTL: overload) at the cost of a heavier write.
  - Every lock carries a **sequence number** to be checked by the resource (fencing, ch21 21.8). Because many services cannot be changed to check tokens, a **lock delay** exists: after a lock is released, nobody can take it for up to about a minute, assuming a delayed packet dies by then.
  - **Fine-grained coordination built from a coarse lock**: one server takes a coarse lock for a numbered *epoch* and issues its own sequence (epoch.counter) from memory; a standby watches the lock; when it takes over with the next epoch, the database rejects late packets from the lower epoch.
  - Cells sit on different racks; state is backed up to a file system in another data centre so a recovering lock service does not depend on a store that depends on itself; clients find cells through DNS.
- **Accepted costs**: a hard dependency on a small cell, write-heavy invalidation, poor fit for high-rate sequencing.
- **Lessons**: sell a lock and file interface rather than a consensus library, and layer fine-grained uses on coarse locks with epochs.
- **Does not generalise when**: you need a high-rate sequencer directly on the service.

## 22.6 Wide-column store on a file system and a lock service
- **Problem**: one table abstraction for crawl data, user data and analytics with row-level atomicity, versioned cells and sorted ranges.
- **Key decisions**:
  - **Data model**: row key, column families (a family groups columns of one type, which helps compression), column keys inside a family, and a **timestamp** per cell for versions (supplied by the client or the system). Sorted by row key; rows are **range-partitioned** into **tablets**; each tablet server holds tens to a thousand tablets and splits a tablet that grows too big.
  - Layers: tablets' files are immutable sorted tables with a block index (64 KB blocks) stored in the distributed file system, together with the write-ahead logs; the lock service elects the single master, registers live tablet servers (each takes a lock on its own name) and seeds the root of the location tree.
  - **Locating a tablet without the master**: a lock-service entry points to a **root tablet** (never split), which lists the **metadata tablets**, which list user tablets and their files; clients cache aggressively and walk back up when an entry is stale.
  - **Master startup**: take the master lock, list live servers from the lock service, ask servers what they serve (servers are the truth about assignments), then assign whatever is unassigned, starting with the root.
  - **Failure handling**: if the master stops hearing from a server it deletes that server's lock, which both proves the server is out and stops it rejoining; the server shuts itself down when it cannot hold its lock; its tablets are reassigned. A master that loses its lock-service session kills itself; existing tablets keep being served meanwhile.
  - **Write path**: append to the commit log (replicated in the file system, so it is slow), then the in-memory sorted table; when it is large it is flushed to an immutable file (**minor compaction**), which also truncates the log to replay; background **major compaction** merges files, newest wins, tombstones dropped.
- **Accepted costs**: single-row atomicity only; commit-log latency; a heavy stack of dependencies. A multi-row transaction layer on top is the subject of ch23 23.2.
- **Lessons**: split metadata (small, strongly consistent) from data (large, immutable), make servers the source of truth for assignments, and use a lock-service entry as the single bootstrap pointer.
- **Does not generalise when**: you need cross-row transactions inside the store itself, or your data fits one relational node.
