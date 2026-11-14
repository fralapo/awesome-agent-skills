# Chapter 07: Messaging, Real-Time Delivery and Pipelines

## Core Idea
Two patterns carry most "move data between parties" designs: a **persistent connection plus a routing layer** for interactive messages, and an **accept-fast, process-later pipeline** for heavy work. In this model both use a durable record before acknowledging, retries with idempotency, and decoupled stages that scale separately.

## 7.1 Push needs more than request/response
- **Thesis**: request/response cannot push from server to client, so interactive products need another transport.
- **Mechanism**: options are long polling (client keeps asking; not real-time, repeated headers, many connections cycling), server-sent events (persistent, one-way server to client, plus ordinary POST for the other direction), WebSocket (persistent, bidirectional, no client/server asymmetry), and peer-to-peer/UDP-style streams (low latency, may lose or reorder, needs authentication first). Chat needs bidirectional low latency: WebSocket. Delivery tracking is watched occasionally and tolerates loss: server-sent events or even simple refresh are enough.
- **Trade-off**: each connection holds memory and a port/file descriptor; a server can hold only a limited number, so you need many servers behind a balancer. The exact connection limit in the source is unclear.
- **Does not hold when**: updates are rare or the client is rarely open (use notifications).

## 7.2 Dumb gateway, smart session service
- **Thesis**: the box that holds connections should do almost nothing else.
- **Mechanism**: the gateway terminates the external protocol and forwards messages in an internal, lighter protocol (security is handled at the edge). A **session service** stores "user X is connected to gateway Y"; a message for user B is routed to the session service, which finds B's gateway and pushes through it. Keeping this mapping in the gateways would waste connection memory and duplicate transient data. Message parsing moves to a separate parser stage using an internal serialisation format so the gateway can stay unparsed.
- **Trade-off**: hops and services.
- **Does not hold when**: very small deployments.

## 7.3 Delivery status as three acknowledgements
- **Thesis**: "sent", "delivered", "read" are three different events from three different places.
- **Mechanism**: **sent**: the server has durably stored the message in a chat store and will keep retrying until the recipient gets it; it replies to the sender immediately. **Delivered**: the recipient's device acknowledges to its gateway, which tells the session service, which routes a receipt back to the sender's gateway. **Read**: the same path when the chat is opened. Group delivered/read receipts are costly because every member must answer; many products skip them.
- **Trade-off**: more messages; receipts are deprioritised under load (ch03).
- **Does not hold when**: receipts are a compliance requirement.

## 7.4 Presence and last-seen
- **Thesis**: store a timestamp, not a conversation.
- **Mechanism**: every user-initiated action updates a per-user last-seen row via a small service; the requester reads that row instead of asking the user's device. If last activity is within a threshold (for example ten to twenty seconds) show "online"; otherwise show the time. Messages initiated by the app itself (polling, receipts) carry a flag and are not counted as activity.
- **Trade-off**: slightly stale status.
- **Does not hold when**: privacy settings change what may be shown.

## 7.5 Group fan-out
- **Thesis**: keep membership in its own service and cap the group size.
- **Mechanism**: the session service asks the group service for member ids, looks up their connections (cached) and pushes to each. Group-to-member mapping is spread over servers by consistent hashing on the group id. Group size is capped (a few hundred) so fan-out is bounded.
- **Trade-off**: product limit; group service availability matters.
- **Does not hold when**: broadcast to millions (use batching or pull).

## 7.6 Durable queues, retries and idempotency
- **Thesis**: put a queue between steps that can fail; let the queue retry.
- **Mechanism**: a message queue redelivers after a configurable delay and a configurable number of attempts; after the last failure it reports failure so the failure reaches the client ("could not send"). Receivers must handle duplicates, so each message has an id and operations are idempotent.
- **Trade-off**: a queue adds latency and operational cost; duplicates must be handled.
- **Does not hold when**: operations are synchronous and cheap to redo.

## 7.7 Accept fast, process later
- **Thesis**: decouple ingest rate from processing rate so a flood only grows a queue.
- **Mechanism**: the upload endpoint authenticates, stores or queues, and returns an "accepted" status (202) immediately; workers consume at their own pace. The queue absorbs spikes (holidays); users cannot be rate-limited at the entry because creators decide how much they upload.
- **Trade-off**: results appear later (a minute or minutes); status tracking is needed.
- **Does not hold when**: the user needs the result in the same call.

## 7.8 The processing pipeline as a task matrix
- **Thesis**: turn one big job into many independent small tasks, so adding a format is adding a column.
- **Mechanism**: stage 1 validates (length cap, content checks); stage 2 splits long files into chunks (a very short clip is one chunk and skips this); stage 3 fans out tasks for each format x resolution; stage 4 recombines, replicates across regions and publishes. Workers listen for task events. This is the common pattern for any heavy transformation (large text files too).
- **Trade-off**: scheduling overhead; many output files per input (storage multiplied).
- **Does not hold when**: output is a single cheap transformation.

## 7.9 Upload transport
- **Thesis**: a chunked secure upload over TCP is reliable and ordered, which suffices for recorded files.
- **Mechanism**: split the file into chunks; the connection retransmits missing ones. File-transfer protocols exist; the source leaves the comparison unclear.
- **Trade-off**: a live capture would need a different design.
- **Does not hold when**: you stream live.

## 7.10 Change streams
- **Thesis**: expose the database log as a stream and let others build on it.
- **Mechanism**: streams feed secondary indexes, search, backups, notifications and subscriptions to changes for a given object; they are eventually consistent and off the hot path (ch04 4.10).
- **Trade-off**: lag.
- **Does not hold when**: consumers need synchronous guarantees.

## 7.11 Bulk sends and batches
- **Thesis**: scheduled sends to all users must be chunked.
- **Mechanism**: send to the first thousand users in minute one, the next thousand in minute two; tune chunk size to the urgency. Add jitter to popular-publisher notifications (ch03 3.8).
- **Trade-off**: delayed delivery for later chunks.
- **Does not hold when**: delivery time is contractual.

## 7.12 The distributed log (Kafka-style) as a decoupling backbone
- **Thesis**: an append-only partitioned log decouples producers from consumers, absorbs spikes and allows replay; the price is operational complexity and weak ordering.
- **Mechanism**: topics hold partitions (append-only files) on brokers; a message has key, value, timestamp and headers; the key picks the partition and preserves order for equal keys; no key spreads load. A broker is usually limited by network before disk or CPU. Consumers record how far they have read as an offset; committing early risks loss on crash, committing late risks duplicates. A consumer group shares partitions so each message is processed by one member; if a member dies, partitions are reassigned (rebalance). Delivery: at most once, at least once, or exactly once (hardest and slowest). Durability: each partition has a leader and followers (commonly three replicas); waiting for all in-sync replicas is safest and slowest. Uses: replay for debugging and recovery, event sourcing (state = replay of events, with a full audit trail), regional partitioning of location updates.
- **Trade-off**: favours throughput over latency (batching adds delay), only per-partition order, heavy to operate.
- **Does not hold when**: you need request-response or global order (use a plain queue or a single partition).

## 7.13 Inbox pattern, hybrid transport and heartbeats
- **Thesis**: keep sending cheap and stateless, and use the persistent channel only for receiving; guarantee delivery with a per-user inbox that clears on acknowledgement.
- **Mechanism**: send by ordinary HTTP (easy to scale), receive over WebSocket. A message to an online user goes server to server directly (a presence service maps users to servers) and then to the device; an offline user's message waits in an inbox for a limited time and triggers a push notification through the platform push service; the inbox entry is removed only after the device's acknowledgement, and an unacknowledged one is retried; on reconnect the inbox is drained in order. Group delivery fans out to online members and stores for the rest (bounded group size). Presence uses heartbeats: the client pings about every 30 seconds, the server marks it offline after about 60 seconds without one, which smooths brief tunnel-like disconnections; a connection that looks open is not proof of an active user. Scaling: connection count is the first limit, then the inbox store (shard by user id), then regional deployment with cross-region routing.
- **Trade-off**: inbox storage and retries; ordering across servers needs ids or logical clocks.
- **Does not hold when**: messages are stored forever centrally (then the inbox is the history).

## 7.14 Saving state and publishing: the outbox
- **Thesis (mechanism)**: a database write and a broker publish are two resources; if the process fails between them the state changed and nobody was told.
- **Mechanism**: store the outgoing message in an outbox table inside the same transaction as the state change; a relay publishes unsent rows and marks them sent. If marking fails the message is sent again, so delivery is at least once and receivers need ids (7.6). Needed when other parts rely on the fact (workflow steps, cache invalidation); unnecessary for best-effort telemetry. Details: ch19 19.6.
- **Trade-off**: an extra table, relay latency, duplicates.
- **Does not hold when**: the log itself is the state, or loss is acceptable.

## 7.15 Delayed messages replace polling and batch scans
- **Thesis (position)**: when an event implies a later action (expiry, reminder, follow-up), schedule it at that moment with a delayed message.
- **Mechanism**: the broker holds the message until its due time; the consumer rereads the current state and exits if nothing is needed. Load spreads over the day instead of a nightly burst; each item retries independently. Delay limits and semantics differ between brokers. Details: ch20 20.6.
- **Trade-off**: one message per item; visibility lives in data, not in the broker.
- **Does not hold when**: processing is set-based or the volume of items makes per-item messages too expensive.

## 7.16 More consumers move the bottleneck; order is a design choice
- **Thesis (position)**: competing consumers raise throughput until the next constraint appears, and strict order is often unnecessary.
- **Mechanism**: adding consumer instances increases load on the database, cache or rate-limited third party behind them; check that downstream can scale. With several consumers even a first-in-first-out queue can process messages concurrently out of order; with workflow events a policy that records which preconditions have arrived makes order irrelevant. Details: ch19 19.3.
- **Trade-off**: a per-process state record for the policy.
- **Does not hold when**: order is a hard requirement; then use one partition or one consumer per key (7.12).


## 7.17 Log replication: in-sync replicas, commit and the failure window
- **Thesis**: a partitioned log stays durable if a message counts as committed only when every replica in a **dynamic in-sync set** holds it; the knobs decide how much loss you accept.
- **Mechanism**: each partition has one **leader** that takes all writes and serves all reads (extra replicas add durability, not throughput). Followers pull from the leader like consumers. The **in-sync replica set** is kept in a coordination service by a **controller** that heartbeats brokers; a replica that lags beyond a time bound or loses contact is removed and rejoins when it catches up. A message is **committed** (visible to consumers) only after every in-sync replica has it; on leader failure only an in-sync replica may take over, so it holds all committed data; uncommitted tail entries on a failed leader are overwritten after the new leader's **epoch** begins (a follower asking with an old epoch is told to go back to an earlier offset and overwrite). Producer acknowledgement levels: none (fire and forget), leader only, or all in-sync replicas; a **minimum in-sync size** setting refuses writes when the set has shrunk too far. If every in-sync replica is down you choose: wait for one of them (no loss, longer outage) or resume with whichever broker returns (shorter outage, possible loss). Brokers do not flush every message to disk before acknowledging, on the argument that disks fail too and replication is the durability (position; durability is then reduced by simultaneous crashes). Leaders are spread by a **preferred leader** per partition and moved back when the preferred broker returns; notifications are batched.
- **Versus a majority quorum**: a quorum is not held back by one slow node and needs only a majority alive; the in-sync approach is held back by its slowest member but evicts slow members dynamically and tolerates more failures (with five replicas, four can fail and one still serves). Both need overlap between the set that acknowledged and the set that can elect.
- **Trade-off**: durability versus latency, set per producer and per topic; batching makes the all-replica wait cheap per message.
- **Does not hold when**: the loss of a recent message is acceptable (logs, metrics) or all replicas fail together.

## 7.18 Exactly-once inside a log system: three layers and their limits
- **Thesis**: exactly-once is delivery into the log plus atomic writes inside the log; it is not a promise about what your consumer does outside.
- **Mechanism**: default behaviour is **at least once** (a lost acknowledgement makes the producer retry and the broker append twice); **at most once** never retries (message may vanish); on the consumer side, committing the offset after processing gives at least once, committing before gives at most once. Layer 1, **idempotent producer**: the broker gives each producer an id; the producer numbers every batch per partition; the broker keeps recent sequence numbers per producer, drops a batch that repeats one and rejects one that skips ahead. It does not inspect payloads (two identical legitimate events are allowed). Layer 2, **zombie fencing**: the application supplies a logical **transactional id**; each time an instance registers under it the coordinator issues a higher **epoch**, and partitions reject writes carrying an older epoch, so a producer revived after a long pause is fenced (ch21 21.8). Instances sharing an id should read and write the same topics, otherwise partitions not registered with the new epoch still accept the zombie. Layer 3, **atomic multi-partition writes**: reading input, producing output and committing the input offsets are all writes to the log (offsets live in an internal topic), so one atomic commit makes "processed exactly once" hold for read-process-write cycles. The coordinator is chosen by hashing the transactional id to a partition of an internal transaction-state topic (the studied default: 50 partitions) and its leader; it logs the commit decision before propagating it (two-phase commit, ch21 21.10), and its log is itself replicated, so a coordinator takeover reads the decision.
- **Limits**: a write to an **external** database cannot be rolled back with the transaction; processing that is **non-deterministic** or calls external systems may differ on re-execution; a transaction is not an **atomic read** (a consumer of several topics cannot easily tell which messages belong together); delivery-exactly-once is not processing-exactly-once.
- **Trade-off**: coordination round trips, transaction-state storage and latency until commit.
- **Does not hold when**: the consumer is idempotent by design (an upsert by key); then at-least-once plus idempotency is cheaper (ch20).

## 7.19 Stream processing: checkpoints, barriers, time and watermarks
- **Thesis**: a stream job gets exactly-once **state updates** by snapshotting operator state at a consistent point of logical time and replaying from replayable inputs.
- **Mechanism**: a job is a directed acyclic graph of operators; a client compiles code into the graph, a **job manager** places operators on **task managers**, heartbeats them and triggers checkpoints; for its own availability the job manager keeps its state in a coordination service so a standby can take over, and checkpoints go to durable storage. **Barrier records** are injected into every input stream at an interval; an operator that sees a barrier snapshots its state, which reflects all events before the barrier and none after. An operator with several inputs **aligns**: it holds back events on an input that has already delivered its barrier until all inputs reach theirs (the operator still processes other inputs, but one input stalls). On failure the operator is rescheduled elsewhere, state is reloaded from the last checkpoint, and events after the barrier are replayed, so every input and every inter-operator stream must be **replayable** (a durable log, or a write-ahead log on the producing operator). The guarantee is that each event updates state exactly once, not that each event is handled once. Streams between operators come in **pipelined** form (batches flushed when a size threshold or a time threshold is reached: a larger size gives throughput, a smaller time bound gives latency) and **blocking** form (materialised, for bounded batch jobs, no back-pressure but the producer finishes first). Ordering holds inside a partition only; once data fans out across partitions and the network, do not depend on arrival order (write operators that do not require it). Three notions of time: **event time** (when the record was produced), **ingestion time** (when the system first saw it) and **processing time** (the operator's clock; inconsistent across machines). A **low watermark** at an operator says that no event with a lower event time can still arrive; watermarks are injected periodically and an operator with several inputs takes the minimum of its inputs. Iterative jobs add a **feedback stream** with control events that mark the end of an iteration. A batch job is a bounded stream; the older approach of a stream for approximate and a batch for exact results (two code paths) is what a unified engine tries to avoid.
- **Trade-off**: alignment delay and checkpoint storage against recovery time; larger buffers against latency.
- **Does not hold when**: inputs cannot be replayed, or an external sink is not idempotent or transactional.
