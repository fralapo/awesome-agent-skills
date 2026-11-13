# Chapter 17: Domain Modeling and Pragmatic DDD

## Core Idea
Model what the business does, not what the tables look like. In this model most of the material here is **position**, not mechanism: the choices are judgment calls about where behavior deserves explicit code. The recurring test is "what is the user trying to do?": maintain data (plain CRUD is the cheapest correct answer) or perform a business capability with rules and outcomes (capture the intent explicitly). Most systems need both, in different areas.

## 17.1 CRUD or task-driven: decide per area
- **Thesis (position)**: forcing CRUD onto behavior hides rules and intent; forcing commands onto plain data adds ceremony. Pick per boundary, not per system.
- **Mechanism**: when the data model, the stored record and the resource sent to the client are the same object, every business action collapses into "update some fields and change a status". The rules live only in the users' heads: nothing enforces that a bill-of-lading number must be present when freight is marked loaded, that a piece count may vary only within a tolerance, or that arriving must precede loading. A task-driven design names each capability (dispatch, arrive, load, depart, deliver, cancel), gives each its own input, validation and order rules, and produces a named outcome that downstream parts can react to. The screen then guides the user through the workflow instead of exposing an edit form. Reference data (a customer's contact details) has no behavior and needs no "change phone number" command.
- **Trade-off**: more types, handlers and screens per capability; tooling and frameworks favour CRUD, so it is faster to build and easier to hire for.
- **Does not hold when**: the area is pure reference data, or an external system owns the behavior and you only map its data (a CRM or accounting integration). There, CRUD wins; do not create "25 commands for one screen".

## 17.2 Intent is what a status change throws away
- **Thesis (position)**: a record shows what changed, not why; inferring the why later is guesswork.
- **Mechanism**: "cancel shipment" implemented as delete, soft delete or `status = cancelled` does not record who asked, why, or what kind of cancellation it was. The distinction can be commercially real: a vehicle that went to pick up goods that were not ready (a charge is owed to the carrier, the customer may be invoiced a fee, the vehicle is freed) differs from an order cancelled before dispatch (nothing owed). Consumers that must infer this from a generic "cancelled" event each invent their own rule. Capturing the intent at the moment of the action (a command with its reason and actor) lets the right fact be published (ch19 19.4).
- **Trade-off**: you must ask the question in the UI and in the model; some data collected will never be used.
- **Does not hold when**: no one downstream can act on the distinction and no audit need exists; keep the simple status.

## 17.3 Model rules, not relationships
- **Thesis (position)**: an aggregate exists to enforce a rule atomically; building an object graph of everything related to it is a trap.
- **Mechanism**: take "a group chat holds at most 100,000 members" with millions of messages and members. Loading every member into memory to check a count is modeling a relationship instead of the rule. Alternatives, each with a cost:
  1. keep only a member counter inside the aggregate (fast; membership must be tracked elsewhere and the counter can drift from it);
  2. enforce the limit in the application layer from a read-model count (flexible; the projection can be stale, so the limit can be overshot);
  3. a transaction script: open a transaction at a suitable isolation level, count with an index, optionally lock, insert, commit (simple and fast; rules scatter if the domain is rich);
  4. split by responsibility: a membership model enforces joining, the chat model handles messages (no single model has to hold everything).
  The guiding sentence: an aggregate can enforce a rule only if it has all the data needed to decide; enforce each rule where it can be done reliably and efficiently, not where it looks tidy.
- **Trade-off**: rules end up in more than one place; each option picks a different consistency level.
- **Does not hold when**: the collection is small and bounded (an order with a few lines): a normal aggregate with its children is natural, and hard limits on money need the strongly consistent options (1 or 3), not a stale projection.

## 17.4 What DDD is for
- **Thesis (position)**: DDD targets inherent business complexity (rules, processes, how people really work), not technical complexity that frameworks already cover.
- **Mechanism**: the strategic part comes first: build a conceptual model and a shared language with the business, one per context (a "claim" is a rich concept in claims processing, a payment line in finance, a pointer to a contract elsewhere). Classify areas as core, supporting or generic to decide where modeling effort pays. The tactical patterns (entities, value objects, aggregates, repositories) come after and depend on the language and framework; beginners over-focus on them. Sample applications are descriptive: they assume the domain is complex enough to justify the pattern, and copying them as prescriptions is the common error. A pattern only has value in the context of the problem it answers; working backwards from the pattern to a problem fails.
- **Trade-off**: time with domain experts; models must evolve with understanding.
- **Does not hold when**: the domain is mostly CRUD with simple rules: the cost of a domain model exceeds its return; use transaction scripts and keep DDD vocabulary for the few areas that deserve it.

## 17.5 Find boundaries from the process, not from the entities
- **Thesis (position)**: pivotal events and shifts in language mark candidate boundaries more reliably than the table list.
- **Mechanism**: model the end-to-end flow with representatives of each team (for example by laying out events on a wall), then look for handoffs (a contract is signed and sales becomes onboarding), changes in vocabulary, the actors and external systems involved, where value is created and where pain sits. Pain often originates upstream: a team that spends its time repairing data is being handed bad input. Start at the whole-flow level, then zoom into one boundary.
- **Trade-off**: workshops cost calendar time and need business experts; the result is a hypothesis.
- **Does not hold when**: one small team already knows the domain; a short conversation suffices.

## 17.6 Introducing a new model into legacy: extract, then experiment
- **Thesis (position)**: do not thread a new modeling approach through a big ball of mud; carve out a service behind an explicit contract and work inside it.
- **Mechanism**: define the boundary, extract that slice (the strangler idea: the old code calls the new through the contract, then the implementation behind the contract is replaced), and now you have a small area (ten use cases, not two thousand) where you can record meaningful business events, try event sourcing or a richer model, and show results the business understands. Even if the first boundary is wrong, the extraction adds value because dependencies became explicit.
- **Trade-off**: an interface to maintain between old and new; some duplication during the transition.
- **Does not hold when**: the legacy system is small enough to rewrite wholesale, or the slice cannot be separated from shared data without large coupling work.
