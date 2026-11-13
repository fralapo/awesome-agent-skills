# Chapter 18: Boundaries, Modular Monoliths, Coupling and Dependencies

## Core Idea
A boundary is a statement about **ownership** (behavior, rules, lifecycle, meaning, authority), not about processes or databases. In this model coupling and cohesion are the two quantities to manage; named architectural styles are mental models for managing coupling, not blueprints. Much of this chapter is **position**; where a mechanism exists it is stated, and each section ends with the case where the opposite choice is right.

## 18.1 Logical and physical boundaries are separate decisions
- **Thesis (position)**: a module and a service should both be logical boundaries; deployment shape is chosen afterwards.
- **Mechanism**: ownership is about who owns the data, the invariants, the lifecycle and the concept. One logical boundary may be several deployables (a web API plus a background worker), several repositories (front end and back end) or share a database instance with another boundary while owning its own schema. Two microservices with a shared model are not isolated; one deployable with schema-owning modules can be. Decide in this order: logical boundaries, then how they communicate (synchronous or asynchronous), then how they are deployed. Teams that start from "must deploy independently" end up forcing events or network calls everywhere.
- **Trade-off**: logical boundaries inside one process rely on discipline or tooling; physical boundaries enforce isolation and independent scaling at a price in network hops and operations.
- **Does not hold when**: independent scaling, failure isolation, compliance or team autonomy really requires a separate process; then the physical split follows the logical one.

## 18.2 One word, several concepts; avoid entity services
- **Thesis (position)**: when two areas use the same word, check whether they mean the same thing; usually they do not.
- **Mechanism**: a vehicle in compliance (registration, insurance, maintenance) is a different concept from a vehicle in dispatch (availability, drivers, trailer capacity); an employee in HR (compensation, onboarding) is a user in IT (authentication, roles); a patient is a clinical record in one context and a billing account in another. The test: different language and different reasons to change. A single shared model couples them, so a change for one reason ripples into all. Keep ownership separate and integrate deliberately: each boundary has its own internal model and exposes only what others need. Shared identity (the same id) links them without a shared god object.
- **Trade-off**: some data is duplicated, and integration must be designed.
- **Does not hold when**: the data really is the same everywhere and changes for one reason (country codes, currency lists) or the system is small enough that one concept is honest.

## 18.3 Cohesion by capability, not by data or by layer
- **Thesis (position)**: group by what the system does (business functions); data follows behavior.
- **Mechanism**: functional cohesion relates things by task; informational cohesion relates them by shared data and tends to produce an entity service (a "product service" that sales, purchasing, warehouse and catalog all call). Behaviors drive data: sales owns price and availability, purchasing cost, warehouse stock adjustments, catalog names and descriptions. A service is then the authority over a set of capabilities and the data behind them. The same applies at code level: organize by feature (add to cart, check out) instead of by technical layer (all controllers, all models). Each boundary or feature can then choose its own style: a rich domain model in the core, transaction scripts in a supporting area.
- **Trade-off**: a team convention for structure is easier to keep uniform with layers; cross-feature reuse needs conscious effort.
- **Does not hold when**: the application is small CRUD where layers map one to one with features and cost nothing.

## 18.4 Coupling is the root question: volatility and blast radius
- **Thesis (position)**: hexagonal, clean and onion variants all say the same thing: point dependencies toward a stable core and isolate volatile concerns behind adapters; which diagram you pick matters little.
- **Mechanism**: the core (business logic) should not depend on things likely to change: web framework, database, cloud SDKs, external APIs, message brokers. Ask how many places depend on the thing, how likely it is to change, and how much a change would hurt. A single use of a stable SDK inside one handler needs no abstraction; hundreds of usages of a volatile dependency do. A "port" is just a contract (often an interface) and an "adapter" its implementation. Cohesion is the other half: coupling cannot be judged without asking what belongs together.
- **Trade-off**: every isolation layer is indirection to read, test and maintain.
- **Does not hold when**: a team wants one shared template for consistency across many services, or a regulated environment demands the separation; accept the cost knowingly. In a CRUD app the full template is overhead.

## 18.5 The cost of indirection
- **Thesis (position)**: an interface with one implementation, derived from that implementation, adds noise and no seam.
- **Mechanism**: at runtime an interface says nothing about behavior (the implementation is chosen by wiring and may be wrapped by decorators for retry or logging). A real seam appears when there are several implementations or a measured need to isolate. Symptoms of excess: query handlers that only delegate to a service that only runs one query; mapping an object from layer to layer; a dropped cancellation token because the thin abstraction did not carry it. A query is specialized by design; hiding a specialized query behind a generic read service hides nothing, because the coupling count is unchanged. Do not abstract in order to avoid depending on a library you use in a dozen places; abstract when usages number in the hundreds or the dependency is volatile.
- **Trade-off**: skipping the abstraction means a later change touches every usage; swapping is easier with a seam.
- **Does not hold when**: you choose the implementation per customer at runtime (payment provider per tenant), need a test seam around slow or external calls, or want a cross-cutting pipeline behavior on every handler.

## 18.6 The decoupling spectrum: you move complexity, you do not remove it
- **Thesis (position)**: decoupling is not a goal or a maturity ladder; each step away from an in-process call buys something and costs something.
- **Mechanism**: the spectrum for "place order" (save, charge, reserve stock, e-mail, loyalty points):

| Step | Gain | Cost |
|---|---|---|
| Direct calls | One call stack, explicit order, easy to debug | Everything coupled, shared availability |
| Interfaces and injection | Seams, substitution, tests | Indirection; meaning only at runtime |
| Queue (temporal decoupling) | Producer and consumer need not be up together; scaling; absorbs spikes | Retries, duplicates, poison messages, dead-letter queues, outbox; call stack lost |
| Events, independent consumers | Fan-out, add consumers without touching the publisher | Invisible behavior; events become contracts to version |

  The semantic change at the queue step is the important one: "order accepted" is not "order completed". A declined card that used to show immediately must now be communicated later, so the UX changes with the architecture. Code that was procedural cannot simply be pushed through a queue.
- **Trade-off**: where complexity lives changes (code, wiring, time, contracts); it does not shrink.
- **Does not hold when**: the business really needs fan-out, independent availability or long-running processes; then the later steps pay for themselves.

## 18.7 What a modular monolith needs
- **Thesis (position)**: modular means logically separated; monolith only describes packaging, and the two are independent.
- **Mechanism**: modules own their schema; no other module reads it or joins across it; integration goes through a public API, a read model or projection, or events; one deployable can be scaled out as several identical instances behind a balancer; communication can still be asynchronous inside it (a module that publishes and consumes its own events for e-mail, SMS and webhooks is a good first step). When modules are defined only by folders while sharing a model, a change in one (an HR work status) still ripples into another (authentication).
- **Trade-off**: boundary violations are one import away; independent deployment, scaling and technology choices are given up.
- **Does not hold when**: teams need independent release cadence, or one module's load or failure profile must be isolated from the rest.

## 18.8 Needing data that another boundary owns
- **Thesis (position)**: first ask whether you need it for a read or for a decision; replicating tables everywhere is rarely the answer to either.
- **Mechanism**: for **queries** (show the customer name next to the invoice status), compose in the UI or a composing layer so each part comes from its owner, or build a purpose-shaped, denormalized projection from published events; the reader is rarely the writer, so stale is usually fine. For **decisions** (is this command valid?), a synchronous call also returns data that may be stale by the time you act, so it is not safer than a local copy. The strongest option: the boundary that must make the decision owns the data it needs, derived from other boundaries' events and shaped for its use. Replicating another boundary's schema, even through change data capture, keeps you coupled to its internals; translate to a published contract. Consolidating disparate data into a warehouse for reporting is a good use of replication.
- **Trade-off**: composition adds latency and a failure point; projections add eventual consistency and duplication.
- **Does not hold when**: the decision needs strongly consistent data from another boundary: then the boundary is wrong; merge the data into one owner (see ch20 20.5).

## 18.9 Multi-tenancy is isolation, not a database choice
- **Thesis (position)**: the question is what to isolate (data, compute, deployments, schema changes, performance, failures), not "shared or per-tenant database".
- **Mechanism**: whatever tenants share couples them. A shared database shares schema, migrations and performance; shared compute shares deployments, failures and noisy neighbours; shared caches, queues and regions share invalidation, backlog and residency. A shared schema keyed by tenant id works, but the id leaks into every query, report and message, and every migration must be backward compatible with the code still running (expand the schema, deploy, backfill, then contract). Each resource sits on a spectrum: shared, pooled (groups of tenants), dedicated; mix per resource. The trade is efficiency versus control. Try cheaper tools before splitting: per-tenant rate limits and per-tenant connection pools address noisy neighbours without separate compute. Tenants differ: pool small ones together and dedicate large ones as it becomes necessary. Isolate for smaller blast radius, compliance, dedicated capacity or safer rollouts (a tolerant tenant gets a version first).
- **Trade-off**: control costs N backups, migrations and upgrades; sharing costs coupling.
- **Does not hold when**: you have few, similar tenants and simple needs: one shared database is a sound, cheaper design. See ch04 for provisioned capacity per tenant.
