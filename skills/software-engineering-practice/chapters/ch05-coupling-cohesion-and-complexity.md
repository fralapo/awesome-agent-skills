# Chapter 05: Coupling, Cohesion and Managing Complexity

## Core Idea
In this model the ability to change software is the defining characteristic of its quality, and **coupling is the main thing that decides how expensive change is**. Coupling cannot be removed; the discipline is to choose, name and manage it.

## 5.1 Why change is the quality measure
- **Thesis (position)**: if you cannot change the code, the only way to get correctness, performance and security is to be perfect first time.
- **Mechanism**: so the working definition of quality is "the software works, and it can be changed easily and safely". That is supported by five properties used to prefer one design to another: modularity, cohesion, separation of concerns, abstraction (information hiding) and appropriately managed coupling (preferring loose).
- **Trade-off**: a design aimed at changeability can look like over-engineering if applied to hypothetical futures (ch06).
- **Does not hold when**: the code is a throwaway; the cost of change does not matter.

## 5.2 Coupling is not simply bad
- **Thesis**: a system with no coupling is not a system; the goal is deliberate coupling.
- **Mechanism**: strong coupling is fine when the thing coupled to is stable (the language of a mature query standard) and dangerous when it is unstable (this week's database schema). The harm comes from coupling that is **unstable, unintended or invisible**. Another way to see it: the connections between modules are the assumptions modules make about each other.
- **Trade-off**: tight coupling is acceptable early when abstractions are not yet known, or in high-performance systems that avoid translation layers, provided you protect it (5.5).
- **Does not hold when**: the coupling crosses team boundaries or release cycles.

## 5.3 Five kinds of coupling
| Kind | Meaning | Example / remedy |
|---|---|---|
| **Operational** | Consumer cannot run without the provider | App will not start without its database; one flaky shared service drags down everything. Remedy: graceful degradation, resilient design |
| **Developmental** | Two components must be changed together | Shared code or platform releases force lockstep; worsens super-linearly with size. Remedy: stable APIs, independent release, fewer shared libraries |
| **Semantic** | Components share a concept (what a customer or an amount of money means) and must agree on it | No code dependency, so tooling will not warn you. Trade against developmental coupling consciously |
| **Functional** | Different parts solve the same problem in different ways | Two implementations of a discount rule drift apart; seven data-mapping mechanisms evolved by accident in one project and took a cost audit to justify removing six |
| **Incidental** | Things change together for no good reason | A module reaching across the system for a value; two systems on one fan. Remedy: resilience; buys nothing |
All five are hidden assumptions in one part about another. Real solutions score on several kinds at once.

## 5.4 Moving coupling instead of removing it
- **Thesis**: you don't eliminate coupling, you move it to where you can manage it.
- **Mechanism**: comparing three ways of talking to a data store: direct SQL (strong operational and developmental coupling to a schema that changes), a REST-style API owned by the data team (still strongly coupled operationally, but the owning team can change internals as long as the API holds, so organisational boundary moves to a stable place) and event-driven messaging (weak operational and developmental coupling; coupling concentrated in message semantics, translated at the edges). An API's real purpose is an insulation layer.
- **Trade-off**: every option buys one kind of freedom with another kind of cost.
- **Does not hold when**: the schema is stable; then a database boundary between teams is less harmful than usual.

## 5.5 Two tools: design and speed of feedback
- **Thesis**: you cope with coupling either by decoupling through design, or by fast feedback on whether changes are safe.
- **Mechanism**: a 2x2. Decoupled + fast feedback: excellent. Decoupled + slow feedback: fine (independent services). Coupled + fast feedback: fine (CI doing its job). **Coupled + slow feedback: the danger zone**, the classic big ball of mud, which teams usually drift into by accident, for example treating a coupled system as independent services while sharing state, schemas and concepts. In this model "poor feedback on releasability" means more than a day.
- **Trade-off**: decoupling by design needs sophisticated design skill; fast feedback needs investment in CI (ch02).
- **Does not hold when**: you have neither; then you are already in the zone and must pick one deliberately.

## 5.6 Design techniques
Hide information behind APIs; treat boundaries (modules, services, teams) as guarded places; translate foreign data at the edge and validate it; **announce, don't command** (events instead of instructions); be parsimonious in what you consume and generous in what you produce (each field read is accepted coupling); design messages from the consumer's perspective; adding a field is easy, removing one is a breaking change. Rule: **tighten what is stable, loosen what is uncertain**. Start a new system with CI even if you plan to split it later, because boundaries are learned.

## 5.7 Symptoms of coupling
Slow builds (build time as a physical measure of coupling; one extreme example compiled the whole system seven times for one outcome); long test set-up; tests that break on renaming an internal class; teams blocked on each other; lockstep platform releases; long parameter lists (a position: nervous above four parameters, refuse more than six). Fix test set-up by reducing coupling, not by sharing the set-up. A hard-to-write test is coupling made visible before production (ch03).

## 5.8 Organisation is coupling too
- **Thesis**: an organisation that designs a system produces a design copying its communication structure (Conway's law).
- **Mechanism**: specialist silos (business, UX, back end, test, operations) make a chain of coupled hand-offs that every feature must pass. Small autonomous teams, small changes, modular seams, cohesion and abstraction are all coupling management, as are the five principles for managing complexity. Teams can cope with a system as coupled as their slowest dependency.
- **Trade-off**: autonomy is not a purity test; teams still need contact points as interfaces change.
- **Does not hold when**: the problem is small enough for one team.

## Cross-references
Chapter 06 for design vs architecture; chapter 08 for cognitive load as the human face of the same problem; `software-architecture` for service boundaries, messaging and resilience mechanics.
