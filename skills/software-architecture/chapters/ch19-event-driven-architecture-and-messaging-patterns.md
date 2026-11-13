# Chapter 19: Event-Driven Architecture and Messaging Patterns

## Core Idea
"Event" names at least four different ideas, and most pain comes from mixing them or from using events where a plain call or a transaction fits. In this model events are worth their cost when independent responsibilities must react to a business fact, and each use needs its own rules. This chapter separates the uses, then covers the mechanisms (outbox, CQRS read side, event sourcing, consistency by context). Interpretations are **position**; mechanisms are marked as such. Every section states when the plain alternative is better.

## 19.1 Four things called "event"
- **Thesis (position)**: event sourcing, event-carried state transfer, notification and workflow events are different tools; conflating them multiplies complexity.
- **Mechanism**:

| Use | What it is | Visible outside the boundary? |
|---|---|---|
| Event sourcing | The facts that persist state; state is derived and transient | No: an implementation detail of one boundary |
| Event-carried state transfer | Events that copy data to other services, often per entity or per property | Yes: a data-distribution mechanism |
| Notification (domain or integration event) | A business fact others may react to | Domain events are internal; integration events are the contract |
| Workflow event/command | A step in a long-running process | Yes, between participants |

  Tools blur this: a messaging library, a log, a change-capture tool and an event-store database each do some of it, so one tool seems to justify all uses. Ask a team that says "we are event-driven" which of the four they mean.
- **Trade-off**: more vocabulary to learn.
- **Does not hold when**: the system is small and uses one of them in one place; the distinction costs more than it saves.

## 19.2 Events as notification: when they pay
- **Thesis (position)**: use events when independent concerns must react to something that already happened; not because a broker is fashionable or for scaling.
- **Mechanism**: after a delivery completes, the decision has been made; sending a text, calling a partner webhook and pushing a notification are separate responsibilities that were not part of the decision and can run on their own timeline. The publisher does not know whether there are zero, one or many consumers. A **command** is imperative, has one handler and an owner; an **event** is past tense, has one publisher and any number of consumers. Using a queue for commands does not make a system event-driven. A low-risk start: inside a monolith, publish "order placed" and consume it for e-mail, SMS and webhooks.
- **Trade-off**: temporal decoupling brings retries, duplicates, ordering and hidden behavior (ch18 18.6).
- **Does not hold when**: the work is request-response CRUD (validate, save, return), or the step must succeed or fail atomically with the main change; then a direct call or a local transaction is simpler. Scaling out consumers (competing consumers) is a side benefit, not the reason.

## 19.3 Loose coupling is about time; the three half-truths
- **Thesis (position)**: events remove temporal coupling, not coupling.
- **Mechanism**:
  - **Coupling**: the consumer must know the topic and the event's shape; changing the shape needs versioning or a new event. The dependency direction flips, it does not vanish.
  - **Scaling**: adding consumers moves the bottleneck to the database, the cache or a rate-limited third party; check what downstream can scale.
  - **Complexity and debugging**: a chain of synchronous calls across services is just as hard to trace. The root cause is a workflow that snakes through many boundaries. Boundaries are handoffs: one boundary finishes its workflow and hands off to the next (dispatch delivers, billing invoices); a single giant cross-boundary workflow means the boundaries are wrong.
  - **Ordering**: out-of-order delivery is mostly self-inflicted by CRUD events ("delete" before "create" propagates data, not workflow). With workflow events, a policy (a gatekeeper that records which preconditions have arrived and acts when all have) handles any arrival order, for example creating a label only once both "billed" and "placed" were received.
- **Trade-off**: policies add state per process.
- **Does not hold when**: you need strict global order or immediate answers; use a log with one partition or a synchronous call.

## 19.4 Events are a public API
- **Thesis (position)**: database model, domain model and integration model are three different things; only the last is a contract.
- **Mechanism**: exposing the schema through a JSON resource freezes the schema; publishing every internal domain event does the same to the domain. Publish a **summary** that other boundaries care about ("order dispatched" instead of carrier assigned, instructions sent, ETA computed, shipper notified). The same concept can exist as both a domain and an integration event with different schemas (an internal reason code must not leak and bind consumers to your internals). Thin events (ids only) push consumers to call back synchronously, which returns the state **now**, not at the time of the event, possibly minutes apart; fat events leak internals. Decide by what consumers need to understand and react. For evolution: add or remove properties compatibly; when the concept itself differs (order not used versus cancelled before dispatch), publish a **new** event rather than overload one.
- **Trade-off**: a mapping step and a deliberate contract to maintain.
- **Does not hold when**: one team owns publisher and consumers and the event is stable; or a fat event carries data to a reporting store where freshness at event time does not matter.

## 19.5 Don't blame events for bad boundaries
- **Thesis (position)**: reported failures of event-driven systems (hard debugging, stale screens, cost, rollback pain) mostly trace to misuse.
- **Mechanism**:
  - Events must be business facts (order submitted, inventory reserved, payment authorized), not "order created/updated".
  - "We cannot roll back" is a workflow-modeling problem: a shipping label created with a carrier or a payment that timed out cannot be rolled back in your database even in a monolith; you compensate or reconcile (ch20).
  - A user changing their own profile should see it immediately: handle it synchronously and publish events for the other concerns (CRM, analytics) asynchronously.
  - The broker is infrastructure like the database: give it high availability and a local outbox for when it is unreachable; do not remove synchronous fallbacks and then lose all functions when it is down.
  - Events do not require microservices, a cluster of brokers or six databases: they work between modules of one deployable.
  - Messaging cannot fix bad boundaries: choose logical boundaries first, then communication, then deployment (ch18 18.1).
- **Trade-off**: you must design the workflow instead of assuming a rollback.
- **Does not hold when**: all steps live in one boundary and one database; a transaction does the job.

## 19.6 Dual write and the outbox
- **Thesis (mechanism)**: saving state and publishing a message are two writes to two resources; failing between them leaves the state changed and the world uninformed.
- **Mechanism**: write the message to an outbox table in the same transaction as the state change. A relay (separate thread or process) reads unsent rows, publishes them to the broker, then marks or deletes them; a failure just retries. If the publish succeeds but marking fails, the message is published again, so delivery is at least once and consumers must be idempotent (ch20 20.3). Most messaging libraries implement this. It is not "for finance": it is for events that are facts other parts depend on (long-running processes, cache invalidation). Alternative: avoid the second write, as when the event store is the state.
- **Trade-off**: an extra table, relay latency, cleanup, duplicates.
- **Does not hold when**: events are best-effort metrics where loss is fine; or the stream is the source of truth.

## 19.7 CQRS is code paths, not read replicas
- **Thesis (position)**: command-query separation is about two responsibilities in code; scaling a database with replicas is a different matter.
- **Mechanism**: the command side changes state (often through an aggregate); the query side is free to be specialized: compose several sources, read a materialized view, use a different library or raw SQL, and avoid over-fetching because no consistency boundary is needed for reads. A materialized view or dedicated table updated in the same transaction stays consistent; updated asynchronously it adds eventual consistency (19.9). Both sides can use the same database and schema. Read replicas copy data and bring their own staleness. Do not abstract specialized queries behind generic read services (ch18 18.5); loading an aggregate for a read is waste.
- **Trade-off**: two paths to maintain; a framework for it tends to accumulate extension points; shared projection machinery (batching, prioritization) is the part worth reusing.
- **Does not hold when**: one model serves both sides without composition pain; then a single path is simpler.

## 19.8 Event sourcing in plain terms
- **Thesis (position)**: store facts, derive state; use it where history and domain language matter.
- **Mechanism**: a stream per aggregate (a warehouse item: received 30, received 5, shipped 6, count adjustment of minus 2, giving 27). Any shape can be derived by projections (SQL tables for analysts, documents), including the state at an earlier time. Anti-patterns: "CRUD-sourcing" (created, updated, updated; no domain language), using the stream as a broker for other services (their reads freeze your internals), and using it for analytics or scale reasons. Versioning: add or remove properties compatibly but do not rename; for a real change (one event becomes two) rewrite the whole store into a new store and flip to it at the end. A read model feeding a command is allowed if the command records the read-model version it used, so later processing can detect that more recent events would have changed the decision. In occasionally connected systems, writes must be accepted without seeing the latest state.
- **Trade-off**: projections to build, migration work for event changes, unfamiliar tooling, ad hoc queries need a read model.
- **Does not hold when**: the domain is CRUD with no valuable history; or a normal audit table is enough.

## 19.9 Eventual consistency depends on who reads
- **Thesis (position)**: staleness is harmless for other readers and reports; it hurts when the reader is the writer, when the read enforces a rule, or when the decision cannot be undone.
- **Mechanism**: a user saves, is sent to a list built from a projection or replica, and does not see the change. Remedies in order of preference:
  1. avoid the problem: read from the primary after a write that matters; do not return the user to a stale view (they already know what they entered; send them elsewhere); add the created id to the list locally;
  2. wait for the replication lag, or update the projection inside the command (adds write latency);
  3. return a log position or version at write; the read presents it and the projection says whether it has caught up, or when to retry;
  4. push the update (WebSocket) or poll.
  Business-rule reads are different: if a credit check reads a local copy updated by events, two concurrent orders can both pass. That is a boundary problem (the decision belongs where the data is), not a tooling problem. Eventual consistency fits reporting, analytics and views "as of" a time. The consistency here is linearized: the same ordered timeline, only your position differs, unlike multi-master stores where nodes can hold diverging histories.
- **Trade-off**: reads that must be fresh cost latency or primary load.
- **Does not hold when**: freshness is required everywhere and the cost is acceptable; then use strong reads (ch02 2.8).
