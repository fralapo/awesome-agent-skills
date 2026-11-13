# Chapter 20: Workflows, Sagas and Calls to External Systems

## Core Idea
Business processes cross boundaries and third parties, and no transaction spans them. In this model the working answers are: coordinate with an explicit workflow, treat the party that owns the truth as the source of truth, make each step safe to repeat, bound reservations in time, schedule follow-ups instead of scanning, and prefer moving the decision to where the data lives over distributed consistency. Goal: **effectively once**, not exactly once. The mechanisms are generally accepted; the preferences are **position**.

## 20.1 Choreography or orchestration
- **Thesis (position)**: choose how a long-running process is coordinated by how much you need to see and control it.
- **Mechanism**: in choreography each service consumes events and publishes events without knowing it is part of a process (order placed, payment completed, label created); there is no central place that holds the workflow. In orchestration a coordinator (saga or process manager) holds the state of one process instance, sends commands, receives events and sets timeouts. Choreography keeps services independent; orchestration makes the process visible, testable and able to time out.
- **Trade-off**: choreography hides the whole flow (behavior is invisible, see ch18 18.6); orchestration adds a component that knows the steps.
- **Does not hold when**: the process is one handoff between two boundaries (choreography is enough), or it has many steps, timeouts and branches (orchestrate).

## 20.2 A saga coordinates; it is not the source of truth
- **Thesis (position)**: pair a saga with reconciliation against the system that owns the truth.
- **Mechanism**: the saga knows the step, the messages received and the next command. It cannot know whether a payment provider charged the card after a timeout. A **timeout means the saga stopped waiting, not that the step failed**, so no compensation is issued; instead it requests reconciliation: fetch the order, exit if it is already confirmed or cancelled, read the real status from the provider, then apply a safe action (provider says captured: record the capture and confirm the order; provider says failed: mark failed and cancel). Triggers for reconciliation: the saga's timeout, a user action ("check payment status"), or periodic polling for pending items older than a threshold. This replaces a mess of branching logic in the payment handler for every timeout, duplicate and unknown error.
- **Trade-off**: you need a query API (or ledger) on the provider; polling costs calls; the extra code path must be tested.
- **Does not hold when**: you own the truth in one database (a transaction suffices), or the provider offers only asynchronous callbacks you can trust and store (webhooks as input to the same reconciliation).

## 20.3 Idempotency ends at your network boundary
- **Thesis (mechanism)**: an inbox table with a unique message id makes your own state changes idempotent in one transaction; it cannot undo a call you already made to someone else.
- **Mechanism**: handler pseudo-order: call the payment gateway, then save the inbox row and state. A duplicate message (or a concurrent second request) calls the gateway again and fails only afterwards on the unique constraint: the customer is charged twice. Concurrency makes the bug easy to reproduce; it exists without it. Layered defenses:
  1. the provider's idempotency key, derived from the business operation and reused on retry (and offer the same in your own APIs);
  2. a lookup by reference id (order id) before acting; races remain unless the provider enforces uniqueness;
  3. serialize by a granular business key with a lock (row lock or a cache lock), accepting lower throughput; a timeout while holding the lock does not prove failure;
  4. separate the internal state from the external call: mark "payment pending" and write an outbox message in one transaction, let a dedicated handler call the provider with its own retries and timeouts; this improves state consistency but can still double charge;
  5. reconcile or compensate (void, refund) when the others did not prevent it.
- **Trade-off**: each layer costs complexity or throughput.
- **Does not hold when**: the provider's idempotent request support already covers the operation, or the call is harmless to repeat.

## 20.4 Reservation: a time-bound lock instead of a distributed transaction
- **Thesis (mechanism)**: when a guarantee must span services and time, reserve the resource for a limited period.
- **Mechanism**: a reservation has three behaviors: reserve, confirm (the business process finished, nobody else may use it) and expire (release after a timeout). Example: reserving a username at the start of a multi-step registration so another request cannot take it, and releasing it if registration is abandoned; a store holding an online order's last item aside for a week then returning it to the shelf; a card authorization that holds funds and is captured or voided. Implemented in process with a dictionary and a timer, or with messages and a delayed message for expiry. Compare two-phase commit (ch14 14.9): no cross-resource lock is held while participants prepare; the lock is a record with a lifetime.
- **Trade-off**: the reservation service is a single point of failure for whatever depends on it; coordination can deadlock; the lifetime must be chosen (too short cancels legitimate work, too long locks resources).
- **Does not hold when**: a single boundary has a unique constraint that covers the whole process.

## 20.5 Do you need a distributed transaction? Often you need a different boundary
- **Thesis (position)**: when two boundaries must stay consistent, first ask why they are separate.
- **Mechanism**: example: a subscription balance in payment and order statuses in ordering. After renewal, ordering calls payment synchronously to deduct for unpaid orders, then updates its own status; a failure between the two leaves the balance reduced and the orders unpaid. Options in rising quality: (1) replace the blocking call with messaging, getting retries, backoff and dead-letter queues, but the two stores are only eventually consistent; (2) use a reservation (authorize the amount, set a timeout, mark orders paid, complete or cancel); (3) **remove the need**: the order's payment status and amount belong to the boundary that decides payment, so payment records orders from an "order placed" event and settles them in its own transaction; ordering receives an event and shows the status. This happens in the first place because we think of one entity living in one service, and because the screen wants one service to show everything; compose the screen from several services instead.
- **Trade-off**: one boundary now owns more data; the other shows eventually consistent status.
- **Does not hold when**: the boundaries are truly independent with different authorities: then use the reservation or a saga.

## 20.6 Model the future instead of running batch jobs
- **Thesis (position)**: when something happens that implies a later action, schedule that action then, rather than scanning for it later.
- **Mechanism**: batch problems: a failure in the middle of a batch (partial refunds, inconsistent state), retry policy to design, and two sneaky growth problems: runtime creeping beyond the interval so runs overlap and duplicate work, and the "quiet hour" peak that grows into working hours until you shift it again. Splitting the batch into a kickstarter plus one message per item isolates failures but not concurrency or load. Alternative: at the moment of the fact (reservation created), send yourself a **delayed message** due at the expiry time. When it arrives, read the current state; if the order was picked up, exit; otherwise expire, refund and release. The same shape fits abandoned registrations (expire the attempt) and recurring updates (each message schedules the next one until delivery completes). Load spreads through the day and each item fails and retries alone. Visibility: the state of the system is in your data, not in the delayed messages; consumers must tolerate "nothing to do".
- **Trade-off**: delay semantics and limits are broker-specific (read the documentation); a very large number of items can cost more as messages than as one query; the broker still polls internally, but that concern is no longer yours.
- **Does not hold when**: the work is genuinely set-based (reporting, ETL, bulk recalculation), the number of events makes per-item messages too costly, or a condition spans many entities and cannot be evaluated per item.
