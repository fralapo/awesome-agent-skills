# Chapter 03: Availability, Failure and Overload

## Core Idea
Availability is bought with redundancy, but redundancy adds parts that can fail. In this model the discipline is: pick the availability the business needs, remove single points of failure layer by layer, and design explicitly for the failures that come from **load redistribution** (cascades, herds, cold caches), because those take down systems that had redundancy.

## 3.1 Choose the number of nines for the organisation
- **Thesis**: reliability targets scale with size and stakes; chasing the top level too early wastes money and adds complexity.
- **Mechanism**: a startup can live with two to three nines and scheduled downtime; a mid-sized company aims for roughly an hour of downtime a year; mature platforms aim at five to six nines (minutes per year, often invisible to users who just refresh). Systems where a few seconds of outage is unacceptable (medical devices, positioning, unmanned aircraft) aim at zero downtime. The authorization system studied here targets about five nines (the source states about ten minutes of downtime a year) because without it every product is down.
- **Trade-off**: each extra nine costs redundancy, monitoring and engineering time.
- **Does not hold when**: a downtime has a legal or safety consequence that makes the target non-negotiable.

## 3.2 Five principles for high availability
- **Thesis**: availability is mostly judgment about what to give up.
- **Mechanism**:
  1. Simplicity over perfection: many applications need neither zero downtime nor instantaneous data equality between copies; a planned outage or an eventually consistent fallback (cache serving requests) can be invisible.
  2. Downtime over loss: sacrificing availability briefly is better than losing user data.
  3. Fewer moving parts: every extra redundancy layer (primary, replica, failover, backup) is also a part that can fail.
  4. Practise failure: deliberately kill an instance, then a whole region, in production-like conditions, to prove recovery. Suited to medium and large organisations; small ones can take this benefit from the cloud provider.
  5. Incident reports and root-cause analysis: write why it happened (for example repeated "why" questions) and fix the cause, not the symptom; most valuable where context is lost across teams.
- **Trade-off**: practising failure risks real outages; reports cost time.
- **Does not hold when**: the team is too small to run drills; rely on managed redundancy.

## 3.3 Redundancy at every layer
- **Thesis**: walk the request path and give each hop an alternative.
- **Mechanism**: network (a backup route when a router fails; route cost and latency matter), compute (several servers, retry on another, load balancing that can add/remove servers dynamically, regional preference with fall-back to another region), database (a replica kept consistent with the primary and promoted on fault; the same replica can also serve reads; a clustered NoSQL store is the larger-scale option but is usually eventually consistent and operationally heavier), cache (a miss or outage falls back to the database at higher latency and cost; the cache can be restarted, cleared and rebuilt).
- **Trade-off**: each fallback must be tested, and the fallback path must survive the load of the primary path.
- **Does not hold when**: the fallback is untested - it is then a hope, not redundancy.

## 3.4 Live migration playbook
- **Thesis**: a risky move (moving a database from one continent to another to cut latency for most users) becomes safe through rehearsal and a simple final step.
- **Mechanism**: rehearse on a staging copy; bulk-copy the production data while production keeps running (the two copies now differ by the recent window); announce a downtime window in advance (banner countdown and email); choose a time good for users and the team (users inactive, team awake); open a "war room" channel; then, in the window, run one plain query to copy the differential records and switch the pointer; delete the old database to save cost. Rejected as unnecessary: triggers, log-based change capture, managed migration services.
- **Trade-off**: a short visible downtime.
- **Does not hold when**: downtime is not allowed; then use continuous change capture and a dual-write or cut-over strategy.

## 3.5 Cascading failure: redistributed load kills the next server
- **Thesis**: when one server dies, its share lands on the survivors; if they have no headroom they die in sequence, faster each time.
- **Mechanism**: with four servers each carrying a quarter of the range, losing one hands roughly a third more to each survivor; an already-tight server fails, its range moves again, and the remaining ones may carry several times their original load. It is a race: bring a replacement before the next one falls.
- **Trade-off**: headroom costs money; a smart balancer only buys time.
- **Does not hold when**: capacity is elastic and provisioned faster than the failure spreads.

## 3.6 Load shedding with a bounded queue
- **Thesis**: serving some users is better than serving none; refuse work you cannot finish.
- **Mechanism**: give each server a capacity (for example requests per second) and a bounded request queue; when the queue reaches capacity, reject the next request immediately with an error class: **temporary** (retry later: overloaded, slow database) or **permanent** (the request is wrong). Clients must back off and not hammer.
- **Trade-off**: some users see failures; badly behaved clients can still amplify load.
- **Does not hold when**: requests cannot be rejected cheaply (every rejection still costs parsing); put limits at the edge.

## 3.7 Queue length: not too long, not too short
- **Thesis**: sizing the waiting window is a user-experience decision.
- **Mechanism**: a long queue makes requests wait so long that clients time out and retry anyway (the waiting work is useless); a very short queue rejects on arrival and users retry immediately. Pick a middle value and, for old items, drop the stale ones.
- **Trade-off**: no value is right for all traffic.
- **Does not hold when**: requests have hard deadlines; then use deadline-aware dropping.

## 3.8 Thundering-herd sources and mitigations
- **Thesis**: spikes come from known and unknown events; use the cheapest lever matching the predictability.
- **Mechanism**: (a) predictable event (a sale): pre-scale; (b) uncertain: autoscale, accepting extra spend because more traffic usually means more revenue; (c) unpredictable viral spike: rate limiting; (d) scheduled bulk work (sending a message to every user at midnight): split into chunks over minutes; (e) a hot publisher notifying all followers: batch and add jitter; (f) metadata that need not be exact (view and like counts): serve approximations that are interpolated from recent history, saving many database queries; (g) cache identical responses; (h) deploy gradually in small batches (most outages happen during deploys), except for breaking changes that force simultaneous rollout; (i) cache authentication results only for low-stakes data.
- **Trade-off**: approximate counts and delayed bulk sends are visible to some users; cached authentication can accept a stale or revoked credential.
- **Does not hold when**: the delayed or approximate item is the core product (financial data, security decisions).

## 3.9 Cold cache and constant work
- **Thesis**: a cache that is almost always hit hides a latent outage: when it goes cold, the hit rate collapses and the backend sees a multiple of its normal load.
- **Mechanism**: in the studied store the metadata cache normally hits at about 99.7%; if it restarts empty, almost all requests take the slow path and effective capacity falls to a fraction. The countermeasure is "constant work": clients keep querying the backing store regardless of hit or miss so the backend load is steady and capacity is always sized for it, and scaling decisions are made on real load.
- **Trade-off**: extra load and cost in normal times, for predictability; the design goal is low variance.
- **Does not hold when**: the backend cannot absorb the constant extra load, or the cache can be warmed before use.

## 3.10 Spare overflow pool
- **Thesis**: a small spare pool absorbs the failures that cause most overload.
- **Mechanism**: roughly one percent of cache nodes are reserved as overflow ("gutter") nodes and take requests only when a regular node is failing or being replaced; they connect to the same database. Data locality is poor but it only needs to hold short-lived entries.
- **Trade-off**: idle capacity.
- **Does not hold when**: failures are not rare or correlated (a whole zone).

## 3.11 Priorities, preemption and avoiding eviction cascades
- **Thesis**: when resources run out, kill by priority, but protect the top tier from being killed to avoid a chain of evictions.
- **Mechanism**: in the cluster manager, monitoring and production tasks outrank batch and free tasks. A higher-priority task can evict a lower one; to prevent chains where the evicted task evicts another, production tasks are not preempted by other production tasks. If a machine runs out of a non-compressible resource (memory) it kills lowest priority first; for a temporary CPU or I/O squeeze it waits.
- **Trade-off**: batch work is unstable on busy machines.
- **Does not hold when**: all work has equal priority.

## 3.12 Control plane down, data plane up
- **Thesis**: separate the part that changes the system from the part that serves requests, so losing the first does not stop the second.
- **Mechanism**: if the cluster master dies, the per-machine agents keep their tasks running; only new placement stops. Keep the master replicated (five in-memory replicas with leader election) and its state in a consistent store.
- **Trade-off**: during the outage nothing new can be scheduled and failures are not healed.
- **Does not hold when**: the data plane needs the control plane on each request.

## 3.13 Degrade by importance during peaks
- **Thesis**: under heavy load, drop low-value work before core work.
- **Mechanism**: in a chat system during a festival, stop computing "last seen" and read/delivered receipts, but always acknowledge the send. Keep the rule written in advance.
- **Trade-off**: reduced features at the moment of highest attention.
- **Does not hold when**: the secondary feature is the main business.
