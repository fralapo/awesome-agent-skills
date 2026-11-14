# Chapter 21: Time, Ordering and Coordination in Distributed Systems

## Core Idea
Machines do not share a clock, a memory or a reliable view of each other. In this model every "who wrote first", "who is the leader" and "is this lock still mine" question must be answered by something that survives clock error, process pauses and message loss: logical order, majority agreement, and tokens that let the storage side reject stale actors. Wall-clock time is a hint with an error bar, not a fact. Figures below are dated snapshots.

## 21.1 A wall clock is an interval, not a point
- **Thesis**: no machine knows the exact current time; it can only bound it.
- **Mechanism**: most computers periodically ask a time server for the time, then count elapsed time with a quartz oscillator until the next sync. The reply travels over a network with arbitrary delay, so it is already old on arrival; the oscillator drifts (a dated snapshot: about 17 s per day at 200 µs/s of drift without sync). A device you do not own can also have its clock set by its user. The honest representation of "now" is an earliest and a latest bound, and the bound widens between synchronisations.
- **Trade-off**: tight bounds need specialised hardware and frequent sync (see 21.11); loose bounds force you to avoid time-based decisions.
- **Does not hold when**: the order of events does not matter (log lines for humans), or the error is far below the gap between the events you compare.

## 21.2 Measure duration with a monotonic clock
- **Thesis**: the time-of-day clock can jump; elapsed time must come from a counter that only moves forward.
- **Mechanism**: a sync can step the time-of-day clock backwards or forwards, and leap seconds (minutes of 59 or 61 seconds) are ignored or mishandled, so a subtraction of two readings may be negative or wrong. A monotonic clock is a counter that only increases and is meaningful only on one machine, for differences.
- **Trade-off**: monotonic readings cannot be compared across machines or persisted as dates.
- **Does not hold when**: you need a calendar timestamp for display or audit (use the time-of-day clock for that and monotonic for timeouts).

## 21.3 Last-write-wins on timestamps silently drops data
- **Thesis**: ordering concurrent writes by wall-clock time without coordination loses the write with the "older" clock, with no trace.
- **Mechanism**: two writers on two servers with skewed clocks; the write that really happened later carries the smaller timestamp, so every replica keeps the other one and discards it. A client that writes a nanosecond after another overwrites it as if it never happened. Several widely used key-value stores resolve conflicts this way because it needs no read-before-write and no coordination, and they advise keeping servers as well synchronised as possible.
- **Trade-off**: constant space per key and maximum write throughput, in exchange for lost updates under clock error or true concurrency.
- **Does not hold when**: writes to a key are rare, idempotent or from one writer, or losing one of two near-simultaneous writes is acceptable (a "last seen" field).

## 21.4 Logical timestamps: scalar clocks versus version vectors
- **Thesis**: logical clocks give order without physical time; the two families differ in what they can tell you.
- **Mechanism**: a *scalar logical clock* is a pair (counter, node id). Each node keeps the highest counter it has seen, increments on every write, and on seeing a higher counter jumps to it; ties break by an arbitrary but fixed order of node ids. The result is a **total order** consistent with causality, in constant space. A *version vector* keeps one counter per replica; comparing two vectors tells you whether one write happened after the other or whether they are **concurrent**, which allows keeping siblings or merging, but the size grows with the number of replicas.
- **Trade-off**: the scalar clock cannot distinguish "caused by" from "concurrent" (it picks a winner and one write is lost); the vector can, at linear space. Neither orders operations *in real time*: both settle the order after the fact.
- **Does not hold when**: a single leader assigns log positions (the log already is a total order).

## 21.5 Linearizability is per object; serializability is about transactions
- **Thesis**: strong consistency of a single object (every read sees the latest completed write, as if there were one copy) is a different guarantee from isolation across several operations.
- **Mechanism**: linearizability says nothing about two multi-write transactions interleaving; those can still race and leave a weird state even if each object always shows its latest value. It is exactly what you need when "there must be exactly one of something": the holder of a lock, the leader, a unique username. If the replicas of a lock are not linearizable, a stale replica can say the old holder still owns it; two replicas can each accept the same username.
- **Trade-off**: large performance cost, because every replica must see the same order of operations in step.
- **Does not hold when**: a weaker guarantee satisfies the need. Causal consistency (if A happened before B, nobody reads B without being able to read A) is often enough and far cheaper (position: avoid linearizability when you can).

## 21.6 Total order broadcast and linearizable storage are two faces of one problem
- **Thesis**: to act as one copy, every replica must apply the same operations in the same order without loss; that is a consensus problem.
- **Mechanism**: *total order broadcast* delivers every message to every node, none lost, all in the same order (it does not say when). Writes go through that log; a uniqueness check is then deterministic: the first claim in the log wins, later ones are rejected. A read must also be placed in the log (or otherwise ordered against it) before the replica answers, or it may be stale. Conversely, linearizable storage with an atomic counter can order operations, so each can be built from the other. With one leader and no partitioning, the write-ahead log is the order; with several leaders or none, you need the retroactive clocks above, which cannot reject a duplicate in the moment (both usernames look accepted until the order is computed and one is rolled back).
- **Trade-off**: the order is paid in network round trips and in availability.
- **Does not hold when**: operations commute (counters, sets with merge) and can be reconciled later.

## 21.7 Process pauses make a leader or lock holder wrong without knowing it
- **Thesis**: a node can be correct, well-intentioned and still act on a belief that is no longer true.
- **Mechanism**: a process can be suspended at any instruction: a stop-the-world garbage collection (seconds), a virtual machine migrating hosts, a laptop lid closing. A lock service hands out a **lease** with an expiry. The holder is paused past the expiry, another client obtains the lock and writes, then the first wakes up, still believing it holds the lease, and writes too: corruption. The mirror case: the rest of the cluster, hearing nothing from a paused leader, elects another; the old one resumes and now two leaders exist (split brain). A check of the lease before the write is not enough, because the pause can happen between the check and the write.
- **Trade-off**: shorter leases give faster failover and more false suspicions.
- **Does not hold when**: the protected resource is itself idempotent for repeated writes, or the holder's work can be redone safely.

## 21.8 Fencing tokens: let the resource reject the stale holder
- **Thesis**: only a majority decision is trustworthy, but a single node cannot know it lost; so make the protected resource enforce the decision.
- **Mechanism**: every time consensus (or a lock service) grants leadership or a lock, it issues a **monotonically increasing token**. The client sends the token with every write. The storage remembers the highest token it has seen and rejects any lower one. If the first holder (token 33) wakes after the second (token 34) has written, its write is refused. A consensus term number plays the same role.
- **Trade-off**: the resource must understand tokens and keep one number; a resource that cannot (an external system you do not own) cannot be fenced this way.
- **Does not hold when**: the resource cannot compare tokens; then rely on short leases with large safety margins plus idempotent operations, and accept residual risk.

## 21.9 Raft in one page
- **Thesis**: a replicated log, built from leader election and majority acknowledgement, gives total order broadcast and survives minority failures; it was designed to be understandable.
- **Mechanism**: every node is a follower, candidate or leader; time is divided into numbered **terms** with at most one leader per term. Followers expect heartbeats; on silence beyond a **randomised timeout** (randomised so that not everybody stands at once and splits the vote) a follower becomes a candidate, increments its term, votes for itself and requests votes. A node votes if the candidate's term is not behind, it has not voted in that term, and the candidate's log is at least as up to date as its own. A majority of votes makes a leader; a node that sees a higher term steps down, even a leader. The leader appends client operations to its log, sends each follower the suffix it believes the follower lacks plus the term of the entry just before it. Invariant: if two logs have the same term at the same index, they are identical up to that index. If the check fails the follower reports it and the leader retries with a shorter prefix until the logs match, then overwrites the divergent tail. An entry is **committed** once a majority has stored it; only then is it applied to the state machine and acknowledged.
- **Trade-off**: every write costs a round trip to a majority; throughput is bounded by the leader; the cluster is unavailable without a majority.
- **Does not hold when**: the operation spans several independent partitions (a majority per partition is not "all partitions"); use atomic commit across them (21.10), with consensus replicating each partition.

## 21.10 Two-phase commit versus consensus
- **Thesis**: atomic commit needs *every* participant to agree; consensus needs only a *majority*; they solve different problems.
- **Mechanism**: a coordinator asks all participants to *prepare*; a "yes" is a promise to commit whatever happens (crash, power loss) until told otherwise, and the participant keeps its locks. If all say yes, the coordinator logs the decision first and then tells everyone to commit; otherwise abort. Weak points: a participant down after prepare must be retried indefinitely; a coordinator that dies leaves participants "in doubt", holding locks (and with exclusive locks even readers wait), unable to abort alone because others may have committed; the coordinator is a single point of failure unless its decision is itself replicated. It is used where data is split: cross-partition writes, secondary indexes kept in step with the table, derived stores. A generic cross-vendor transaction interface cannot share lock information between engines and so blocks more than a protocol inside one engine, which can use optimistic snapshot-style isolation instead of long locks (position: internal two-phase commit is far more workable than the heterogeneous kind). See also ch14 14.9.
- **Trade-off**: atomicity across partitions versus blocking, latency and coordinator risk.
- **Does not hold when**: the data fits one partition, or a saga with compensation (ch20) is acceptable.

## 21.11 Bounded clock uncertainty and commit wait
- **Thesis**: if you can bound the clock error, you can get real-time-consistent order by *waiting out the uncertainty*.
- **Mechanism**: the clock API returns an interval (earliest, latest). A writer holding its locks picks the commit timestamp equal to the latest bound, then waits until that time is surely past before making the write visible. Any transaction that reads this write must start after it became visible, so its own commit timestamp is larger: causality and real-time order are respected (**external consistency**: if A commits before B starts, A's timestamp is lower). Two scalar logical clocks cannot guarantee this; they only keep causal order. The waiting time equals the uncertainty, so the design buys small bounds with hardware: time servers in each data centre fed by both satellite receivers and atomic or quartz references, because they fail differently, and a drift assumption in the order of hundreds of microseconds per second between syncs (stated figure, dated).
- **Trade-off**: every commit pays the uncertainty; the approach needs specialised infrastructure.
- **Does not hold when**: you cannot run bounded-error time infrastructure; use consensus-based ordering or accept weaker guarantees.

## 21.12 Snapshot reads, safe time and leases with a single vote
- **Thesis**: with commit timestamps, read-only work can use a consistent snapshot at a time T without locks, from any replica that is caught up for T.
- **Mechanism**: a replica may serve a snapshot at T if it has seen writes beyond T and has no in-progress prepared two-phase commit with a timestamp below T that touches the keys read (tracking the affected keys avoids blocking unrelated reads). The latest such T is the replica's **safe time**. To advance safe time without writes, the leader promises to the followers that any future write will be after a time M, below its lease end, and renews M periodically. A snapshot over several partitions either asks each for its last entry and takes the lowest common time (an extra round) or uses the current time and waits for slow partitions. Leader leases avoid a consensus write per renewal with a **single-vote rule**: a follower that voted for a leader will not vote for another until its local lease timeout expires, so lease periods of two leaders cannot overlap.
- **Trade-off**: an idle partition holds back snapshots unless it publishes a time; leases depend on clock rate being roughly right.
- **Does not hold when**: reads must reflect the very latest write (go to the leader) or the store has no commit timestamps.

## 21.13 Causal consistency as the cheap target (position)
- **Thesis**: most applications need "I never see an effect without its cause", not one global order.
- **Mechanism**: a dependent write (y set from x) must not be visible without the write it read. Logical clocks give this by carrying the highest counter the client has seen. Real-time external consistency adds "if A finished before B started, A is ordered first", which logical clocks alone do not give.
- **Trade-off**: weaker than linearizability; fine for feeds and comments, not for uniqueness or locks.
- **Does not hold when**: the invariant is "exactly one" (21.5).
