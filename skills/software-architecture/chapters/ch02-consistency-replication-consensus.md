# Chapter 02: Consistency, Replication and Consensus

## Core Idea
Copies of data protect against loss and spread reads, but every copy creates a question: which copy is right, and who may write? In this model the answer is chosen **per operation and per use case**, and anything not provable under failure is repaired by a background process rather than a distributed transaction.

## 2.1 A single database is a single point of failure
- **Thesis**: any single box in the request path (database, load balancer) is a business-stopping risk; the simplest cure is a copy.
- **Mechanism**: keep a copy on different hardware, so one hardware fault does not take both.
- **Trade-off**: you now manage two states.
- **Does not hold when**: the data is cheap to rebuild (an in-memory index repopulated from a store and from live clients).

## 2.2 Asynchronous vs synchronous copies
- **Thesis**: asynchronous copies are cheap but can lose the latest transactions on a crash; synchronous copies lose nothing but cost latency and coupling.
- **Mechanism**: the primary applies a command (for example "add 100 to account 1") and sends the same command to the replica, which replays commands in the same serial order, reaching the same state. Async: the primary does not wait. Sync: the primary waits for the replica to acknowledge before reporting success.
- **Trade-off**: async lag means stale reads and possible loss at failover; sync means writes slow down or stop if the replica is unreachable.
- **Does not hold when**: you can accept bounded inconsistency (async) or bounded latency (sync); choose by which loss the business can bear.

## 2.3 Single writer, many readers
- **Thesis**: the node that accepts writes is the primary; any copy that accepts writes is a primary too.
- **Mechanism**: replicas refuse writes; they scale read traffic, serve analytics that do not need real time, and can be promoted if the primary dies (the switch is fast and is offered by managed database services). Dozens of replicas are acceptable when freshness does not matter (a comment appearing a moment late).
- **Trade-off**: write capacity does not scale with replicas; promotion needs a decision-maker (see 2.9).
- **Does not hold when**: writes themselves are the bottleneck (shard instead, ch05).

## 2.4 Two writers and the split-brain problem
- **Thesis**: two primaries look resilient but fail dangerously when only the link between them breaks.
- **Mechanism**: each side believes the other is dead and accepts writes. Example: balance 120; one side accepts a withdrawal of 100, the other one of 50; both succeed and the account goes negative.
- **Trade-off**: multi-writer gives write availability and some write load spreading, at the cost of conflict handling.
- **Does not hold when**: operations commute or conflicts can be merged automatically.

## 2.5 A third node as arbiter; majority
- **Thesis (simplified model)**: a third node can detect divergence, assuming the node and a link do not fail at the same time.
- **Mechanism**: a write moves state S0 to SX on node A and is propagated to the arbiter C. If B tries to move S0 to SY, C sees B's previous state is not its own and tells B to roll back and catch up to SX; the client retries on the new state. A write counts as committed only after the others have committed it.
- **Trade-off**: extra node and extra round trips; the "two failures never coincide" assumption is only an assumption. Real designs generalise this to majority agreement.
- **Does not hold when**: partitions can cut the arbiter off as well; then the minority side must refuse writes.

## 2.6 Distributed transaction options
- **Thesis**: coordinating many nodes costs time; choose the weakest protocol the business accepts.
- **Mechanism**: two-phase commit is popular but slow; three-phase commit exists (details unclear in source). Multi-version concurrency control keeps several versions of a record so readers choose isolation (older version for dirty reads, stronger isolation up to serializable at higher cost). A **saga** is a long transaction broken into small steps with compensation: reserve funds on an order, charge on completion; for a long phone call, reserve a little each minute and settle at the end.
- **Trade-off**: stronger isolation = slower; sagas allow intermediate states to be visible and need compensating actions.
- **Does not hold when**: the operation fits one node or one partition (then a local transaction is enough).

## 2.7 Quorum reads and writes
- **Thesis**: with replication factor N, requiring a majority to agree trades a little availability for much better correctness than "any replica".
- **Mechanism**: with N=3 and quorum 2, a read asks several replicas and returns the value with the latest timestamp. Failure case without quorum: the node that took the write crashes, another replica has not yet received it, answers "not found", and the application tells the user their new profile does not exist. If two of three have not yet received it, even quorum returns the wrong "not found" (rare, accepted). With quorum 3 of 3 a single down node fails every request.
- **Trade-off**: raising the quorum increases correctness and failure rate; lowering it does the opposite.
- **Does not hold when**: data is write-once or timestamps cannot order versions (clock issues).

## 2.8 Consistency selectable per request
- **Thesis**: a managed key-value store can offer both levels and let each call choose.
- **Mechanism**: all writes go to the key's leader, which persists and forwards to two replicas. A strongly consistent read is routed to the leader; an eventually consistent read may hit any replica and can return stale data or even a deleted item whose deletion marker has not yet arrived.
- **Trade-off**: eventual reads are cheaper and balance load; strong reads concentrate on the leader.
- **Does not hold when**: the caller cannot tolerate resurrected or stale data at all.

## 2.9 Leader election and coordination services
- **Thesis**: someone must decide who the leader is; use a proven agreement protocol rather than inventing one.
- **Mechanism**: the key-value store elects leaders with a Paxos variant; the cluster manager keeps five in-memory replicas of its master with election; configuration and process state sit in a lock service built on a consensus protocol. Coordination services (examples named: ZooKeeper-style, etcd-style) also trigger failover via heartbeats. Gossip between nodes is an alternative for membership, but is eventually consistent. Internals of the protocols are unclear in source.
- **Trade-off**: consensus is slow and has few nodes; gossip is fast but converges late.
- **Does not hold when**: you can re-derive state quickly after a node loss.

## 2.10 Timestamps as consistency tokens
- **Thesis**: a globally ordered timestamp lets clients ask for "at least as fresh as my write".
- **Mechanism**: the authorization store returns a timestamp with each write; a later read carrying a timestamp equal or greater than the write's will reflect it; a read with an older timestamp gets no guarantee. The timestamp comes from the underlying globally consistent database and is managed largely by the client.
- **Trade-off**: clients must carry tokens; the underlying store must supply ordered time.
- **Does not hold when**: there is no globally ordered clock.

## 2.11 Read-your-writes by routing
- **Thesis**: you can give a writer fresh reads without making all reads strong.
- **Mechanism**: clients talk to the nearest replica tier; writes are forwarded by that replica to the single primary shard, which persists to the database and returns through the same replica, so that replica is updated immediately. Other replicas learn by the change stream.
- **Trade-off**: other users see the write later; write latency includes an extra hop.
- **Does not hold when**: the same user switches replica tiers between write and read.

## 2.12 Dependent writes without a transaction
- **Thesis**: when one logical change touches two shards, order the writes and repair, instead of using a distributed transaction.
- **Mechanism**: an edge and its inverse live on different shards. Write the first edge, wait for success, then the inverse; if the second fails, leave a dangling edge and let a periodic job find and complete them. Retry the first indefinitely.
- **Trade-off**: temporary inconsistency (a post shows no like from a person who liked it).
- **Does not hold when**: the temporary state is harmful (money).

## 2.13 CAP is a per-feature decision, not a team slogan
- **Thesis**: a distributed cache or store usually chooses consistency in some paths and availability in others; arguing "perfectly consistent or perfectly available" is the wrong question.
- **Mechanism**: the cache in this model leans to high availability with eventual consistency, yet works hard to be as consistent as it can because stale replies degrade a social product. Decide per use case.
- **Trade-off**: mixed guarantees must be documented for callers.
- **Does not hold when**: regulation or money demand strict consistency globally.

## 2.14 Retries need idempotency
- **Thesis**: any retry (queue redelivery, client retry) can duplicate work, so operations should be safe to repeat.
- **Mechanism**: deleting a cache key is naturally repeatable; a "send message" needs an id so duplicates are dropped (details in the source are referenced, not given).
- **Trade-off**: ids and dedupe state to store.
- **Does not hold when**: the operation is already naturally idempotent.
