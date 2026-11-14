# Chapter 23: Real Systems III: Transactional Stores, Cloud-Native SQL and Blob Storage

## Core Idea
Same method as ch08 and ch22 (constraint -> decision -> accepted cost), applied to systems that add transactions or strong consistency to partitioned storage, to a relational engine rebuilt around its log, and to an exabyte-scale blob store that avoids consensus altogether. Time-based ordering mechanics are in ch21; here the focus is on how each design places its coordination. Figures are as stated and dated.

## 23.1 Strong consistency per partition with a replicated log per entity group
- **Problem**: application developers reason more easily and ship faster with strong consistency (a write is readable at once), and data must survive a data-centre outage.
- **Key decisions**:
  - The write-ahead log of each partition is replicated by a **consensus protocol across data centres**; one log per **entity group** (a partition of related data chosen by the application), because a single global log would make every write contend for the next slot.
  - Transactions are ACID **inside one entity group**. Data is denormalised so related rows sit together: child keys are the parent key concatenated with the child id (user, then message, then image), so a hierarchy is contiguous and a typical write touches one node.
  - Across groups: a distributed transaction (discouraged, writes may take seconds) or a **message queue**: commit locally, enqueue a message, apply on the other group atomically there; both effects eventually happen but are not isolated from other writers.
  - Replication: **any replica** can accept a write (no master failover); a write picks the next free log slot and proposes it to a majority; the commit also nominates the **next leader**, normally the replica closest to the writer (writes tend to repeat from one place), which has then already done its prepare step for the next slot, so a follow-up write is one round trip. A proposal number lets another replica take over if the nominated one is down.
  - **Local reads**: each replica has a **coordinator** process that records which entity groups the local replica is fully up to date for; a replica may serve a read locally only for such groups, otherwise it does a majority read. A write that fails on a replica must first mark that group as not locally readable there.
  - The coordinator itself must be reachable for writes to proceed; it holds locks in a lock service so that a failed one can be declared dead (details unverified), which matters because a data-centre failure takes the replica and its coordinator together.
- **Accepted costs**: write contention across leaders, cross-group operations are second-class, relies on several underlying services.
- **Lessons**: pick the partition by the application's transaction boundary; the nominated-next-leader trick turns two rounds into one for repeated writers.
- **Does not generalise when**: transactions routinely span many entity groups.

## 23.2 Multi-row transactions layered on a single-row store (snapshot isolation + two-phase commit)
- **Problem**: incremental processing of a huge index (add a few pages without recomputing everything) needs atomic, serialisable multi-row updates, while the underlying store only guarantees single-row atomicity. The previous approach, chained batch jobs over the entire data set, is trivially consistent (each stage finishes before the next starts) but every update costs a full pass, so the index is staler on average.
- **Key decisions**:
  - A thin **client library** wraps the store; throughput matters, per-transaction latency does not (seconds are fine).
  - Every cell is versioned by timestamp; a transaction reads at its **start timestamp** (a consistent snapshot, avoiding the "half a transfer" read) and commits at a **commit timestamp**; both come from one central **timestamp oracle** that only needs to hand out increasing values (not consecutive ones), so it can batch.
  - **Two-phase commit executed by the client**: prepare = write a lock plus the tentative value in each row; the first lock written is the **primary**, every other lock points to it; commit = first convert the primary (commit point), then the others. If the transaction sees a committed write newer than its start, or any lock on a row it touches, it aborts (optimistic, abort-and-retry).
  - **Client failure** leaves locks; they are cleaned **lazily**: a later transaction that meets a lock looks at the primary. Everybody, including the cleaner, must *start* at the primary, so exactly one of "committed" or "removed" happens there. If the primary committed, the finder **rolls the transaction forward** by committing the remaining rows; if the primary was removed, it rolls back. This prevents the case where a paused client (a long garbage-collection pause) commits one row after another client has removed its lock on the other.
  - **Observers**: user code triggered by writes to a column, run as separate transactions that follow up with further writes (unlike database triggers, which share the writer's transaction).
- **Accepted costs**: slow transactions (several store round trips plus the oracle), a central oracle, lock debris until someone trips over it; suited to batch-like throughput, not user-facing latency.
- **Lessons**: put the commit point in one cell, and make every recovery action go through that cell.
- **Does not generalise when**: you need low-latency interactive transactions, or hot rows (optimistic aborts storm).

## 23.3 Globally distributed SQL on bounded clocks
- **Problem**: strongly consistent SQL across regions, with non-blocking consistent snapshot reads over many partitions.
- **Key decisions**:
  - Same skeleton as 23.1 (consensus group per partition, interleaved tables for locality) but **one leader per group**: several leaders were found to create lock contention in two-phase commit anyway, so one leader is simpler. The leader holds a **lease** extended by piggybacking on writes, and uses the single-vote rule (ch21 21.12).
  - Single-group write: prepare on followers, take locks, assign the commit timestamp from the clock interval, wait out the uncertainty, commit (ch21 21.11).
  - **Cross-group write**: a coordinator asks each group leader to prepare; each leader writes a *prepare* entry (with its timestamp and the **list of locks it holds**) into its own consensus log, so a leader failover does not lose the in-flight transaction or its locks; the coordinator then picks a commit timestamp above all prepare timestamps and each group logs the commit. Making each participant a replicated group removes the infinite-retry problem of plain two-phase commit.
  - Reads: see ch21 21.12 (safe time, key-level blocking by prepared transactions, snapshot at a chosen time).
  - Reported behaviour: very good performance when clock uncertainty is small (an assumed drift of about 200 microseconds per second, dated).
- **Accepted costs**: specialised time infrastructure, commit wait on every write, cross-group writes still need two-phase commit.
- **Lessons**: when order must match real time, buy small uncertainty; keep distributed commit state replicated.
- **Does not generalise when**: you cannot operate bounded-error clocks, or all transactions are single-partition (consensus plus a counter is enough).

## 23.4 A relational engine rebuilt around "the log is the database"
- **Problem**: hosted MySQL-style instances amplify writes: each transaction writes the log, data pages, metadata files, the replication log and a temporary double-write area (protection from torn pages), several in sequence, and cross-site replication stacks their latencies.
- **Key decisions**:
  - **Separate compute from storage**: one writer instance, read replicas with caches, and a storage fleet of ordinary servers with big SSDs (not an object store). Every change leaves the writer as **one stream of log records**; no data pages are written by the writer.
  - The storage layer **builds pages from the log in the background**, when idle (the reverse of the classic engine, where page writes track write volume); a read gets a page plus pending log applied.
  - **Quorums chosen for failure domains**: each 10 GB **segment** is stored six times, two copies in each of three availability zones; **write quorum 4, read quorum 3** (V = 6, W + R > V, and W > V/2 so two writes cannot succeed on disjoint sets, otherwise conflicting writes could both be acknowledged). The common 3-replica, quorum-2 setup is judged inadequate at scale: with 365 machines something fails every day, so a whole-zone outage plus one more fault is likely. This layout survives a zone loss plus one more failure for **reads** (writes need all four remaining nodes of the two surviving zones), and survives the loss of any two nodes or a whole zone for both.
  - Small segments bound **mean time to repair**: copying 10 GB over a fast link takes about 10 s (stated), far less than the mean time between failures, so double faults rarely overlap.
  - Because one writer sequences everything, each log record has a sequence number; storage nodes that miss records **backfill by gossip**; the writer tracks which node holds what, so ordinary reads go to **one up-to-date node without a quorum read**; the writer computes a **durable point** (the highest log position for which every partition has a write quorum, taking the lowest across partitions) and acknowledges commits only up to it; a transaction acknowledged at position 102 waits if 101 is not yet durable.
  - Related changes are grouped in **mini-transactions** applied atomically.
- **Accepted costs**: six-fold storage, a single writer, a proprietary storage tier.
- **Lessons**: reduce the number of synchronous writes on the critical path; place replicas by failure domain, not by count; shrink repair time to widen your tolerance.
- **Does not generalise when**: write volume exceeds one writer, or you need multi-writer SQL.

## 23.5 Blob store without consensus
- **Problem**: store exabytes of immutable user data durably (many nines) and cheaply, with strong consistency and simple operations.
- **Key decisions**:
  - Data is cut into 4 MB **blocks**, named by their content hash; a sharded relational **block index** maps hash to bucket and checksum. Identical content is stored once (a hit in the index means the block exists), and the checksum detects corrupted bits.
  - Blocks are **appended** into 1 GB **buckets** (the unit of replication, closed and immutable when full); a **volume** is a bucket's set of copies on different nodes. Recent blocks are accessed far more than old ones (temporal locality).
  - Three **zones** thousands of kilometres apart; inside a zone, **cells** of up to about 50 PB, because beyond that the single master becomes a bottleneck; to scale you add cells, not masters.
  - A cell has a **stateless master** (background only: creates buckets, tracks storage-node liveness, merges and garbage-collects sparse buckets, keeps the replication factor), many storage nodes (each about a petabyte), and a replication table. If the master dies, reads and writes continue; new buckets stop being created after a few minutes and writes shift to other cells.
  - **No consensus**: a put writes the block **synchronously to every node of the chosen volume**; any failure aborts that attempt and retries on another volume; the partial write is garbage-collected later.
  - **Re-replication commit point**: the master waits a while for a failed node to return (cheaper than reshuffling), then spreads its volumes across many nodes in the cell, planning from its single global view; each new copy is stored with the volume's **generation number plus one**; the move commits when the replication table atomically updates the node list and the generation number together; a new master that finds an uncommitted copy (lower generation in the table) simply redoes the move.
  - **Erasure coding** after a volume is closed (it needs immutable data): split the block into parts plus parity so one loss is tolerated at 1.5x storage instead of 2x for a second copy; variants differ in fault tolerance (the studied system used a local-reconstruction variant). Cold data across regions: store half-blocks plus parity rather than a full copy per region (the example gives 1.5x instead of 2x; details unverified).
  - Cost orientation: shingled-magnetic-recording disks for efficiency.
- **Accepted costs**: failed writes waste space until cleaned; the master is a planning bottleneck at cell scale (answered by cells); erasure-coded reads and repairs cost more I/O.
- **Lessons**: immutability simplifies replication, repair and coding; a generation number is a cheap commit point; scale by cloning cells.
- **Does not generalise when**: objects are mutable or small, or need cross-object transactions.

## 23.6 Choosing the coordination level, summarised
| Need | Placement of agreement | Example in this chapter |
|---|---|---|
| Strong writes, one transaction scope | Consensus log per partition | 23.1, 23.3 |
| Multi-row atomicity on a weak store | Commit point in one cell, client-driven 2PC | 23.2 |
| Durable writes with cheap reads | Quorum on a single sequenced log | 23.4 |
| Immutable data, simple operations | No consensus; generation number as commit point | 23.5 |
