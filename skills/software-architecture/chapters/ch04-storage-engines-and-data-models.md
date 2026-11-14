# Chapter 04: Storage Engines and Data Models

## Core Idea
A database is a data structure with a durability layer. In this model you choose the structure by the access pattern (all-fields reads, range reads, many small writes), then choose the model (relational vs document vs key-value) by how data is read and how it changes, and you keep the **log of changes** as the common backbone for replication, indexes and recovery.

## 4.1 The traditional engine is a B+ tree
- **Thesis**: insert and search are logarithmic, which is good for balanced workloads.
- **Mechanism**: every SQL insert or select maps to an insert or search in the tree and each request is acknowledged. Many small writes mean many round trips, headers and I/O calls.
- **Trade-off**: balanced reads and writes, but random in-place updates cost I/O.
- **Does not hold when**: writes dominate and can be batched or appended.

## 4.2 Batch writes first
- **Thesis**: condense many small writes into one block to cut acknowledgements, headers and I/O calls.
- **Mechanism**: the server buffers records in memory and sends one write.
- **Trade-off**: memory held in the server and a durability window for buffered records; cap the number of buffered blocks before flushing.
- **Does not hold when**: each write must be durable immediately.

## 4.3 The log is the fastest write, the slowest read
- **Thesis**: appending is constant time; searching a log is linear.
- **Mechanism**: write by appending to the end. For reads, sort and index the data off the write path.
- **Trade-off**: you must build a second, read-friendly representation.
- **Does not hold when**: data volume is small enough to scan.

## 4.4 Log-structured merge storage
- **Thesis**: combine fast appends with sorted, searchable files built in the background.
- **Mechanism**: buffer writes in memory in append order; when a threshold is reached, flush them as one sorted, immutable file (a **sorted string table**). Searching one file is a binary search; searching many files costs one binary search per file, so reads get slower as files accumulate. Merge files in the background like merge sort (two pointers, take the smaller key), producing bigger sorted files (6 + 6 -> 12, 12 + 12 -> 24): this is **compaction**. A per-file **bloom filter** says "definitely not here" (no false negatives, some false positives) so most files are skipped without a read; bigger merged files need bigger filters to keep false positives low. Updates simply add a newer record for the key (resolved by timestamp); deletes add a **tombstone** that hides older versions until compaction removes them.
- **Trade-off**: fast sequential writes, extra disk space until compaction, background I/O, slower worst-case reads, deleted data lingering.
- **Does not hold when**: workload is read-heavy with many in-place updates (B+ tree territory).

## 4.5 Relational vs document store
- **Thesis**: NoSQL wins when data is read and written together as one blob, schemas change, and scale-out is expected; it loses when you need relations, constraints and ad-hoc joins.
- **Mechanism**: a relational row split into foreign-key tables needs a join to rebuild a user; a document keeps the nested address inside the record, so one read returns everything. Adding a field is free in a document store; in a relational table a new column needs locks, which is expensive. Document stores often partition horizontally by design and are built for aggregations.
- **Trade-off**: weak transaction guarantees, no implicit relations or foreign-key checks, joins are manual, reading one field means reading the whole block.
- **Does not hold when**: financial transactions, many updates, relational queries, or small apps with no scale problem. Large relational deployments exist and are fine; scale alone does not demand NoSQL. (Counter-example in 4.7: a managed NoSQL store with transactions.)

## 4.6 Choose a store per kind of data
- **Thesis**: one product commonly needs three stores, matched to the data.
- **Mechanism**: in the short-video design: an object store for the video files (immutable, read by millions, tied to a CDN); a relational database for user data (relations, ACID, reuse by many services); a key-value or document store for video metadata (flexible, changing fields, no joins, very high read rate, horizontal scale).
- **Trade-off**: three stores to operate.
- **Does not hold when**: scale and variety are small.

## 4.7 Managed key-value data model
- **Thesis**: force callers to think in keys and access patterns; denormalise instead of joining.
- **Mechanism**: a **partition key** is hashed to find the partition; an optional **sort key** orders items inside it for range queries. Together they are the primary key. A **local secondary index** reuses the partition key with another sort field in the same partition (strongly consistent). A **global secondary index** has a different partition key and is a full copy of the table fed from the change stream (eventually consistent). Model one table per application, with composite keys for different patterns (user plus post, comment plus post). The limits on the number of indexes in the source are unclear (swapped, in all likelihood); check current limits.
- **Trade-off**: storage duplication and consistency lag in global indexes; no joins.
- **Does not hold when**: access patterns are unknown or ad-hoc analytics dominate.

## 4.8 Provisioned throughput and the token bucket
- **Thesis**: users pay for capacity units; fair throttling and burst credit make capacity usable.
- **Mechanism**: one read unit is a 4 KB read per second, one write unit is a 1 KB write per second; many customers share a node, so a customer exceeding their units is throttled without hurting others. Unused units accumulate in a token bucket (five minutes of credit): a customer provisioning 200 read units can burst to 60,000 reads (200 x 300 s) for lunch-hour spikes. Admission is controlled globally across the three replicas, so one replica can serve more than its share if the total stays within the provision.
- **Trade-off**: placement must leave room for bursts.
- **Does not hold when**: traffic is flat and predictable.

## 4.9 Leader with tree, followers with log only
- **Thesis**: replicas need durability, not necessarily a query-ready view.
- **Mechanism**: the leader keeps a sorted tree for reads; some replicas keep only the replicated log, which is enough for durability and cuts the work per write. Reading from a log-only replica can be linear.
- **Trade-off**: faster writes versus slower recovery and unusable reads on those replicas.
- **Does not hold when**: every replica must serve reads.

## 4.10 The change log as backbone
- **Thesis**: one ordered log of changes feeds replication, backups, derived indexes, notifications and recovery.
- **Mechanism**: the storage layer streams its log to object storage (backups), to a stream service (customers consuming changes, index builders) and to replicas. A crashed node picks up from the log; a background job creates **snapshots** so recovery starts from a recent snapshot plus later changes rather than from the beginning of time. A watch service pushes selected changes to listeners, off the hot path.
- **Trade-off**: derived views are eventually consistent.
- **Does not hold when**: derived data must be read-your-write consistent.

## 4.11 Immutable files make recovery and flush simple
- **Thesis**: never mutate a written file; add new ones and merge later.
- **Mechanism**: since sorted files are immutable, flushing is quick and safe, duplicates are harmless because of timestamps, and space is reclaimed in batch.
- **Trade-off**: space amplification between compactions.
- **Does not hold when**: storage is scarce and compaction is costly.

## 4.12 Treat aggregates as a first-class goal
- **Thesis (source claim)**: document and NoSQL stores are built to compute aggregates such as averages and totals over large data.
- **Mechanism**: the mechanism is partitioned storage scanning many records; details beyond this are unverified.
- **Trade-off**: column-wise reads are more efficient in a column layout than in whole-record blocks.
- **Does not hold when**: workload needs fast columnar scans across few fields (use a column-oriented store).

## 4.13 In-memory data-structure server (Redis-style)
- **Thesis**: a single-threaded server holding rich structures in RAM is fast and predictable; durability is a configuration choice, not a given.
- **Mechanism**: commands run one at a time, so each is atomic (an increment cannot interleave) and there are no locks, but one slow command blocks every client; throughput comes from pipelining many commands per round trip and from small commands. Values are strings, lists, hashes, sets, sorted sets (ordered by score: leaderboards, top-N, rank lookups in logarithmic time) and streams. Durability options: none (pure cache; rebuild from the database), replicas (survive a node loss, double the memory), periodic snapshots (restart warm, lose writes since the last one), append-only log with a flush each second (lose at most about a second) or each command (safer, much slower). Scaling: replicas for reads, then client-side sharding by hash (consistent hashing for dynamic sets; each node independent, a failure just misses for its keys), and a built-in cluster only when its guarantees are needed (operationally heavier). Expire keys by time-to-live or evict by policy when memory is full. A forked snapshot writer only reads, so copy-on-write (ch12 12.5) makes it cheap unless the parent keeps writing.
- **Trade-off**: speed and simple semantics versus RAM cost and durability work.
- **Does not hold when**: data must survive a crash without loss and is large (use a durable database as the source of truth, ch06 6.1).

## 4.14 B-tree versus log-structured on flash: write amplification and read cost
- **Thesis**: an in-place update on a solid-state drive is really a write elsewhere, an invalidation and a later erase, so many small updates amplify; log-structured engines turn updates into appends and pay at read and compaction time.
- **Mechanism**: flash cannot overwrite; the controller writes new data, invalidates the old and later erases whole blocks, moving still-valid pages first (garbage collection), so one logical update can cost several physical writes; page splits in a B-tree add more. A log-structured merge engine writes to a log and an in-memory table, flushes sorted immutable files, and treats updates and deletes as new records (deletes are markers called tombstones). The costs: reads may consult the memory table and many files (Bloom filters skip files that cannot hold the key), and background compaction must keep up or latency grows; heavily deleted partitions fill with tombstones that slow reads until compacted. A B-tree serves a freshly written hot page straight from the buffer pool, which suits read-after-write on hot keys; an engine that must go to files for just-written data suffers on hot partitions.
- **Trade-off**: write throughput and drive wear versus read amplification and compaction tuning.
- **Does not hold when**: workload is read-mostly with in-place updates on small data (a B-tree is simpler).

## 4.15 Choosing a database by access pattern (one page)
- **Thesis**: choose from the data model, the write path and the failure behaviour you need, not from a product name; most engines are one of two index structures (B-tree, log-structured merge) plus a replication style.
- **Mechanism**:
  - **Relational** (B-tree, ACID): normalised rows, joins, multi-row transactions; best when correctness beats speed (money, status tables, schedulers); writes spanning tables on different machines need distributed commit (ch14 14.9), so keep related rows together or shard by the transaction boundary.
  - **Document store**: nested documents give locality when parts are read and written together; denormalised copies can drift apart.
  - **Wide-column, leaderless** (log-structured merge, quorum, timestamp conflict resolution): very high write throughput, tunable consistency, last-write-wins loss unless conflicts are mergeable (ch22 22.2); suits chat history keyed by conversation with timestamp as the sort key.
  - **Conflict-free data types** on a leaderless store: counters and sets that merge deterministically instead of clobbering.
  - **Wide-column on a distributed file system** (single leader, log-structured merge, described as column-wise storage; verify before relying on it): no write conflicts, slower writes, strong for scans of one column (large media metadata, image thumbnails stored by column); reads of a whole column are local and compress well.
  - **In-memory key-value store**: a hash map, no ordered index, poor for range queries; for hot, small, constantly updated data (caches, live driver locations).
  - Replication style: single leader (no conflicts, write ceiling), multi-leader and leaderless (more write capacity, conflicts), see ch02.
- **Trade-off**: each choice moves cost between write path, read path, consistency and operations.
- **Does not hold when**: your team already masters one engine and the workload fits it (ch01 principle 9); stay on it.

## 4.16 Log-structured hash store with an in-memory key directory
- **Thesis**: the simplest fast key-value store is an append-only set of files plus a complete in-memory index, with exactly one disk read per lookup.
- **Mechanism**: one **active** data file receives all writes; when it reaches a size limit it becomes immutable and a new one starts. Each record is `checksum, timestamp, key size, value size, key, value`; fixed-width headers let you read the header, then exactly the right number of bytes (a delimiter scan would be unsafe because the delimiter may appear in the value); a checksum mismatch after a crash means truncate the tail, since a partially written record cannot be trusted. A **key directory** in memory maps every key to file, offset and timestamp: it is a **dense** index (every key present), so a missing key is answered "absent" without touching disk, and a hit needs one random read. A delete appends a tombstone record and removes the key from the directory. Immutable files accumulate stale and deleted records, so a background **merge** rewrites live records (compaction, 4.4). Recovery rebuilds the directory by scanning the files.
- **Trade-off**: the entire key set must fit in memory; no range queries; merge I/O.
- **Does not hold when**: keys are too many for memory or ordered scans are needed (use a sorted-file engine, 4.4).

## 4.17 Inverted index
- **Thesis**: search over text is a set intersection of precomputed lists, not a scan of documents.
- **Mechanism**: a naive search checks every document for a word (linear). An **inverted index** maps each **term** to its **posting list** (document ids, kept sorted); the set of terms is the **dictionary**. Building: split text into tokens (on white space, with other strategies possible), lower-case, remove punctuation, **stem** (strip suffixes to a root; cheap and widely used) or **lemmatise** (map to a grammatical root; slower), drop **stop words** (very common words that do not discriminate). A posting entry can also hold the term's **position** (for proximity and ranking) and **offset** (for snippets and highlighting). A query "a and b" intersects two sorted lists in linear time; ranking happens afterwards. Optimisations: keep lists sorted, compress ids (delta and variable-length encoding), keep the top documents of each list in memory and the rest on disk (a tiered or "champion" list), index word pairs or triples for phrase queries.
- **Trade-off**: index size, build time and update cost against fast queries.
- **Does not hold when**: the corpus is tiny or queries are exact-key lookups.

## 4.18 Why B+ trees: a file of rows has linear operations
- **Thesis**: a plain file of rows costs linear time for find, update and delete, because rows are packed and a longer row cannot overwrite its neighbour; grouping rows into page-sized nodes keeps the index shallow.
- **Mechanism**: in a flat file, updating a row to a longer width means rewriting the file; finding a row needs a scan, though a range query is cheap once the first row is found. A B+ tree packs many rows into one node the size of a disk page (a 4 KB node holds about a hundred 40-byte rows), so a search touches a few pages and range scans follow leaf links. (Treated briefly here; see 4.1 for the engine view.)
- **Trade-off**: in-place page updates and splits against the append-only options in 4.3 and 4.4.
- **Does not hold when**: writes dominate and updates can be appends (4.4).
