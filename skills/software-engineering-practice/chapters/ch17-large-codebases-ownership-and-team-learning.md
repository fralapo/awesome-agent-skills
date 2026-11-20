# Chapter 17: Large Codebases, Ownership and Team Learning

## Core Idea
When many people change one body of code, the limiting factors are how fast a change is verified, who is allowed to approve it, how unfinished work is kept out of the way, and how the team understands what it already has. The practices here are mechanisms that make those factors manageable. Most of them are positions drawn from practitioner experience at large organisations, and they assume a working automated test and review setup, so check the "Does not hold when" line before copying a practice into a small project.

## 17.1 One repository: a trade-off with conditions
- **Thesis**: a single shared repository lets one change see and refactor every consumer, but it works only when verification is fast and automatic.
- **Mechanism**: with shared code in one place, a team can search all uses of an API, change them in one changelist and see failures immediately. Ownership is then recorded per directory: a change touching a directory needs approval from its owners, and submitting requires passing the automated checks for the parts it touches.
- **Trade-off**: a shared tree concentrates load on tooling and on the people who run it. Multiple repositories make boundaries explicit and local, but cross-repository refactors become slower and more coordinated.
- **Does not hold when**: the team cannot run the affected tests in minutes; then the advantage disappears and boundaries need to be made explicit, as covered in ch05.

## 17.2 Automate style so humans argue about substance
- **Thesis**: formatting and convention rules should be enforced by machines before review, so that review time goes to correctness, design and clarity.
- **Mechanism**: a pre-submit check that rejects style violations removes an entire class of comments and avoids personal disputes about layout. Where a language has idioms that differ from other languages, some organisations require a readability approval: a reviewer certified as proficient in that language's idioms must sign off before the code is accepted. This makes language expertise a checkable credential rather than a matter of opinion.
- **Trade-off**: readability approval adds a gate and a queue; if too few people hold it, it becomes the bottleneck.
- **Does not hold when**: the team is small and everyone knows the language well; the ceremony then costs more than it returns.

## 17.3 Unfinished work behind a switch
- **Thesis**: code that is not ready for users can be merged into the shared line if it is switched off, and turned on gradually while metrics are compared with and without it.
- **Mechanism**: a flag separates deployment from release. Turning the flag on for a small share of traffic and comparing metrics with a control group tells you whether the change helps, hurts or does nothing measurable. Such experiments need agreed metrics before they start, or the result will be read to fit the hopes of the team.
- **Trade-off**: every flag is a branch in the code that must be tested and eventually removed; flags left behind accumulate as debt.
- **Does not hold when**: the change alters data formats or schemas in ways a flag cannot isolate; then use a staged migration instead (ch02 and ch06 cover the relevant mechanisms).
- **Practice**: give each flag an owner and a removal date when it is created.

## 17.4 Legacy code: understand before changing
- **Thesis**: in mature systems most engineering effort goes to understanding and deciding, not to writing new code. A change without understanding is the most common source of regressions.
- **Mechanism**: characterisation tests (ch03) record current behaviour so that a refactor can be checked. Finding the person or record that explains a decision is often faster than reverse-engineering it. Deleting code that nobody can explain, after checking its use, reduces the surface that every future change must consider.
- **Software does not rot by itself (position)**: software usually becomes costly to change because its dependencies, platforms and interfaces move on, and the business keeps changing requirements. Replacing a working product for its own sake because it has "aged" is often a decision driven by incentives, not by a technical defect.
- **Trade-off**: characterisation tests can freeze bugs; document the known ones before pinning behaviour.
- **Does not hold when**: the code is short-lived or the team owns all of it and can rewrite it cheaply; then a rewrite may be simpler than understanding.

## 17.5 The first design is usually wrong (position)
- **Thesis (position)**: for a complex system, the first design idea is almost always incomplete. Design should be expected to change, with the cost of change kept low.
- **Mechanism**: the team learns the real constraints by building. Early in a project a few people can hold the whole design in their heads and move fast. That informal method stops working once the number of people and components grows beyond what a small group can keep in mind; practitioners often place that point around a handful of developers. The signal to add structure is the rising cost of coordination, not a size threshold.
- **Practice**: build a thin version that touches every part, then revise the design; write down the decisions that are hard to reverse and keep the rest flexible; add written contracts between parts when more than one team depends on them.
- **Trade-off**: heavy structure too early slows learning; no structure too late makes coordination expensive.
- **Does not hold when**: the problem is well known and the design is standard. Then reuse the known design and state its assumptions.

## 17.6 Learn by rebuilding small systems
- **Thesis (position)**: rebuilding a system you already use, in a reduced form, teaches more than reading about it. Choose projects where the answer is partly known, and apply an 80/20 rule: a small version that covers the important cases is enough.
- **Mechanism**: a rebuild forces decisions you would otherwise skip: data layout, error handling, concurrency, the order of steps. Chess engines and small interpreters are often used because they combine many such decisions in a limited scope.
- **Practice**: pick one language and learn it deeply before moving to frameworks; take on a framework only after you can explain what it does without it. Avoid hopping between new tools each month (the "shiny object" pattern): each switch resets the learning curve.
- **Trade-off**: small projects do not teach operations, scale or the social side of software; supplement them with real contributions.
- **Does not hold when**: your job requires a specific framework now. Then learn it for the job and return to fundamentals later.

## 17.7 Measuring prevents guesses from becoming debt
- **Thesis**: optimisation without measurement creates debt that shows up later as latency and quality problems; measurement is the cheapest way to prevent both.
- **Mechanism**: performance depends on memory layout and caches as well as on algorithmic complexity, so a structure that looks slower on paper may win on realistic inputs. Benchmarks that run on a developer machine with unrealistic data can mislead; see ch13 for the measurement discipline.
- **Practice**: profile on realistic data before optimising; keep the simplest version until the profile says otherwise.
- **Does not hold when**: the hot path is already proven by production profiling; then optimise there.

## Cross-references
- ch02 for integration frequency and feature toggles.
- ch05 for coupling and ownership boundaries.
- ch09 for review and verification of generated code; this chapter does not repeat that treatment.
- ch13 for tools, benchmarks and learning a second language.
- ch15 for how this work is judged in performance reviews.
