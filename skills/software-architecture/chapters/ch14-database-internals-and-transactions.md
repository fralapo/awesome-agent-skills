# Chapter 14: Database Internals and Transactions

## Core Idea
A database is a program with design decisions, and each decision (where old row versions live, when the log is flushed, who holds locks, how many processes) shows up later as a performance or availability symptom. In this model you choose and operate a database by knowing which cost it moved where: versioning in the table or in an undo area, locks in memory or on disk, optimistic retries or pessimistic waits, one process per connection or a worker pool. The examples use a row-versioned relational engine and compare with undo-log engines.

## 14.1 Pages, tuples, tuple ids and what an index stores
- **Thesis**: a table is a file of fixed-size pages; a "row" is really a row *version*; an index maps a key to the physical location of that version.
- **Mechanism**: the table file is an array of equal pages (8 KB by default). A row version (tuple) is addressed by a tuple id: page number plus slot (line pointer) inside the page. A lookup is one index traversal, then one page read at a known offset, whatever the table size. Large values are moved to a side table. The index (a B-tree) stores the key and the tuple id, so the table (the heap) is a pile and the index is the shortcut.
- **Trade-off**: one-hop lookups, but the physical address in every index means any new version creates new index entries.
- **Does not hold when**: the engine clusters the table on the primary key (secondary indexes then hold the primary key and need a second lookup).

## 14.2 Update means new version; visibility depends on who you are
- **Thesis**: updates never overwrite; a reader sees the version that was alive in its snapshot.
- **Mechanism**: an update writes a new tuple (in the same page if there is space), adds an index entry for it, and stamps the old one as ended. Each version carries the id of the transaction that created it and of the one that ended it. A reader finds both index entries, goes to the heap, compares those ids with its snapshot (read-committed takes a new snapshot per statement, repeatable-read keeps one) and returns the single visible version. The check is a table lookup, which is part of why dead versions are not free to skip.
- **Trade-off**: readers never block writers; the cost is bloat and a visibility check.
- **Does not hold when**: workloads update one hot row constantly (versions pile up faster than cleanup).

## 14.3 Dead versions, long transactions and the cost of rollback
- **Thesis**: old versions are garbage only when no transaction can still see them; a forgotten long transaction pins them.
- **Mechanism**: a background cleaner (vacuum) removes dead versions and marks space reusable inside the file (a plain run does not return disk to the operating system; a full rewrite does, and takes an exclusive lock). Until then queries read pages mostly full of dead rows and discard them, so a page read that yields one live row wastes the I/O. A transaction that touches millions of rows doubles them; on rollback the engine does not delete the new versions, it leaves them dead for the cleaner (rollback is instant, cleanup is deferred). Engines that update in place and keep old values in an undo area must apply the undo on rollback and on crash recovery: a failed bulk transaction can leave the database in a long "rolling back" state.
- **Trade-off**: deferred cleanup versus rollback time; both are paid somewhere.
- **Does not hold when**: transactions are short and the cleaner keeps up (alert on oldest transaction age and on dead-row ratio).

## 14.4 Write-ahead log: durability without writing pages at commit
- **Thesis**: writing changed pages at commit is slow and unsafe (a crash halfway leaves a half-committed state); writing a compact journal first is fast and recoverable.
- **Mechanism**: changes happen in memory pages; each change is described in a small log record appended to a log and forced to disk. Commit means "the log up to my record is on stable storage" and only then does the client get success. Data pages stay dirty in memory and are flushed later. After a crash the engine reloads stale pages and replays the log (hence the name redo log). A checkpoint flushes dirty pages and records a consistent point so earlier log can be recycled. The operating system also caches writes; the log must bypass that cache (fsync) or a power loss loses acknowledged commits, which is why durable settings cost throughput. Engines with undo logs also keep the pre-change values so older snapshots can still read them.
- **Trade-off**: checkpoints are I/O bursts and show up as occasional slow queries; a larger log means fewer, bigger checkpoints and longer recovery; turning fsync off is faster and loses data on a crash (acceptable for disposable test data only).
- **Does not hold when**: data is rebuildable (a cache), or replicas already provide durability.

## 14.5 Process architecture and connection limits
- **Thesis**: a connection can be a heavyweight object; the design decides how many you can afford.
- **Mechanism**: one studied engine runs a listener that forks a backend process per connection, with shared memory for buffers and log and fixed helper processes: a background writer (frees buffer space), a checkpointer, a log writer (forces the log at commit), a cleaner launcher and workers, a log archiver, senders and receivers for replication, a pool of workers for parallel queries (so concurrent CPU-heavy work is capped and predictable), and a startup process that replays the log before accepting connections. Clients are normally application servers with a pool, not end users, so a default of a hundred connections is plausible; going beyond it needs an external pooler. Process-per-connection also multiplies page-table cost (ch12).
- **Trade-off**: isolation and simplicity versus per-connection memory and context switches.
- **Does not hold when**: the engine is thread-based or fronted by a pooler.

## 14.6 Optimistic versus pessimistic concurrency control
- **Thesis**: either prevent conflicts with locks (pessimistic) or detect them at commit and retry (optimistic); the choice is about conflict rate and who pays.
- **Mechanism**: pessimistic: lock the row you touch; others wait or fail; lock bookkeeping costs memory or I/O, and engines that hold row locks in memory escalate to a table lock past a threshold (cheap memory, many blocked writers). One engine stores row-lock state in the row version itself, spending disk I/O to avoid memory. Optimistic: nobody locks; at commit the engine checks whether the data changed underneath and aborts the transaction, so clients must retry. Optimistic fits low-conflict workloads; pessimistic fits hot rows and long business transactions.
- **Trade-off**: waits and deadlocks versus aborts and retry code.
- **Does not hold when**: everyone writes the same hot key; optimistic retries then storm and pessimistic locks queue (move the work to a queue or a single writer).

## 14.7 Lock modes, vacuum compatibility and deadlocks
- **Thesis**: "table lock" names are historical; what matters is which modes conflict.
- **Mechanism**: plain reads take the weakest table mode, inserts/updates/deletes a row-exclusive mode, row-level select-for-update variants add an intent mode; the cleaner and concurrent index builds take a mode that does not conflict with reads and writes but does conflict with itself and schema changes; schema changes, truncate, drop, reindex, full rewrites and clustering take the strongest mode, which conflicts with everything including reads. A transaction never conflicts with itself. So normal cleanup and concurrent index builds run alongside traffic, while full-table rewrites and index builds without the concurrent option block writers (the strongest ones block readers too). Page-level latches protect shared buffers briefly. Deadlocks arise when two transactions take the same locks in opposite order; the engine detects the cycle and aborts one; the cure is a consistent order of updates. Application-defined (advisory) locks serialise multi-transaction operations that the database cannot see as one unit.
- **Trade-off**: fine modes give concurrency but are hard to reason about; the strongest modes are simple and block everything.
- **Does not hold when**: a single writer owns the table.
- **Rule**: before a migration, list which mode each statement takes and whether it queues behind a long reader (a queued strong lock blocks every later query behind it).

## 14.8 When an index is useless (or harmful)
- **Thesis**: an index returns candidates, then the engine still visits the heap; it pays only if it narrows a lot.
- **Mechanism**: (1) low selectivity: a column where nearly all rows share one value (the status of an archive of completed orders; the dominant value of a skewed field) returns most of the table, so the planner, using statistics, chooses a sequential scan; the same index is useful for the rare value. (2) A function or expression on the column in the filter (wrapping the column in an upper- or lower-case function) cannot use a plain index on the column; build an index on the expression or normalise at write time. (3) Composite indexes are ordered left to right: a query on only the second column cannot use it, and an OR across the two columns usually forces a full scan. Unused indexes still cost writes and space. Planners depend on fresh statistics; small development tables hide all of this because a scan beats an index there, so test with production-size data and read the plan (EXPLAIN) rather than assume.
- **Trade-off**: every index slows writes and takes space.
- **Does not hold when**: the engine supports partial, expression or covering indexes that match the query exactly.

## 14.9 Distributed transactions and two-phase commit
- **Thesis**: atomicity across machines needs a protocol, and every protocol has a failure window; the realistic choices are to avoid the transaction (one shard, one writer), run two-phase commit and accept blocking, or compensate afterwards (saga).
- **Mechanism**: a single-node transaction relies on shared memory, locks and a crash-recovery log. Across two databases, "commit here, crash there" breaks atomicity. Two-phase commit: first the coordinator asks every participant to *prepare* (flush its changes and a "prepared" state to disk under a transaction name, keep its locks, survive a restart) and vote; if all vote yes it tells everyone to commit by name, otherwise to roll back. A participant that restarts with a prepared transaction restores its locks and asks the coordinator for the outcome. Limits: if the coordinator dies after prepare, participants hold locks and may block readers and writers until someone decides; electing a new coordinator requires it to know the state; every commit pays extra round trips. Sagas replace the lock with compensating actions and visible intermediate states (see ch02).
- **Trade-off**: strong atomicity versus blocking and latency.
- **Does not hold when**: the operation fits one partition, or the business accepts eventual consistency with reconciliation.

## 14.10 A unique-constraint inbox protects only your own database
- **Thesis (mechanism)**: transactional deduplication covers writes inside the transaction; a call to another system made before the commit is outside it.
- **Mechanism**: if a handler calls a payment provider and then inserts the message id, a duplicate delivery performs the external charge again and fails afterward on the constraint. Use the provider's idempotency key, a lookup by reference, a lock per business key, an outbox that separates intent from the call, and reconciliation (ch20 20.3).
- **Trade-off**: more moving parts around an external call.
- **Does not hold when**: the handler touches only your own database in one transaction.


## 14.11 Optimistic concurrency at the instruction level: compare-and-swap
- **Thesis**: the cheapest "lock" is an atomic instruction that makes one of several competing writers win and tells the others they lost.
- **Mechanism**: pessimistic locking wraps the critical section with acquire and release; all other threads wait, so one hot section caps throughput however many cores you have. **Compare-and-swap** sets a variable to a new value only if it still holds the expected old value, and reports success or failure; it is a single atomic hardware instruction (a locked compare-exchange), so the processor cannot be interrupted in the middle. A counter increment becomes: read old, compute new, compare-and-swap; on failure the code decides: retry, ignore or surface an error. The same shape appears in databases as a version column checked at update time (14.6) and across machines as an epoch or token check (ch21 21.8).
- **Trade-off**: high throughput when conflicts are rare and the section is a single variable; code is more verbose than a mutex; retries spin when contention is high.
- **Does not hold when**: the work is large (calls to other systems, several statements) or conflicts are frequent; take a lock or serialise the writers (14.6).

## 14.12 Distributed commit variants
- **See** ch21 21.10 (two-phase commit versus consensus), ch23 23.2 (client-driven two-phase commit with a primary lock and roll-forward) and 23.3 (replicated participants).
