# Chapter 07: Engineering, Craft and the Meaning of Software Quality

## Core Idea
In this model software development is a design discipline whose production cost is near zero, so the right analogy is **one-off design engineering** (a vehicle designer), not a production line or bridge-building. Craft supplies skill; engineering adds constraints, measurement and accumulated guide rails. The position here is that "engineering is the stuff that works" (positions, not evidence).

## 7.1 Craft is necessary but not sufficient
- **Thesis (position)**: craft values (skill, responsibility, steady value, community) are good, but they are not unique to craft and need guidance on what "good" looks like.
- **Mechanism**: skill exists in engineering too; responsibility exists in engineering (with legal duty of care in many fields); steady accretion of value is how aviation became safe. Craft quality tends to be judged subjectively; engineering adds stronger constraints and measures that rule out non-viable solutions, and lets later practitioners stand on earlier ones. Compare a safety device whose specification is tolerances and tests with one made to taste.
- **Trade-off**: engineering vocabulary carries historical baggage (bureaucracy, heavyweight process).
- **Does not hold when**: the output is genuinely artistic or subjective (UX copy, visual taste); engineering constraints assist but do not replace judgment.

## 7.2 What "engineering" means here
- **Thesis**: the application of scientific rational thinking to practical problems within economic constraints.
- **Mechanism**: iterate, simulate and experiment in small steps, control the variables, measure, and discard what others found bad. Engineering is a set of guide rails, not a cookie cutter; it does not give fixed solutions. In software the practical parameters are modularity, cohesion, separation of concerns, abstraction and coupling.
- **Trade-off**: some outcomes remain subjective (usability); the point is to limit the subjective area.
- **Does not hold when**: "engineering" is used to justify heavyweight bureaucracy; that is a different thing.

## 7.3 Why the wrong analogies hurt
Production-line and civil-engineering thinking comes from domains where production is the hard problem. In software, coding, architecture and UI design are all design; pressing a button yields perfect copies at negligible cost. Designers of cars, phones or spacecraft iterate, simulate, experiment and take small steps because they do not have the answers. Another advantage over physical engineering: we can design for testability and determinism, and try things out cheaply.

## 7.4 A quality definition you can use
Order of priority: (1) it works; (2) it is easy and safe to change, because that is how performance, security and everything else improve when you learn more; (3) the properties that preserve changeability (modular, cohesive, separated, abstracted, loosely coupled). Test of a choice: imagine two versions of your system, one with the properties and one without (behaviour spread everywhere, changes break distant things); which would you add a feature to?
- **Internal vs external quality** : external is what users perceive (works, responsive, safe data); internal is what developers meet in code, and splits into operational quality and developer experience. The user's definition of quality has not changed with agents; how you assess it has (ch09).

## 7.5 Safety-critical work, speed and quality
- **Thesis (position)**: there is no trade-off between speed and quality; survey research supports this; slow process does not equal safe process.
- **Mechanism**: the first software engineers on a crewed-flight programme became obsessed with how things could go wrong, designed to fail safe, and kept the crew alive when overload alarms fired. The engineering mindset is: for any scale, how can this go wrong, and how do I mitigate or eliminate it. Contrast: a car-maker's runaway-acceleration case where reportedly expert review found enormous functions (stated as 10,000 lines), and an anecdote of a lighting switch changing engine behaviour in a car, showing a claimed separation of subsystems did not hold. Coverage by control-flow can be gamed; a data-driven defect can slip through.
- **Trade-off**: heavy compliance tends to rely on extra late-stage testing and traditional slowness, not necessarily better engineering. One survey statistic cited: having a change-approval board correlates negatively with quality, "worse software slower" (correlation, from survey data; treat as indicative).
- **Does not hold when**: a regulation mandates a specific process; satisfy it, but apply small verifiable steps within it.

## 7.6 Mindset for edge cases
Design for failure; evaluate likely and unlikely scenarios; decide what degrades gracefully for unanticipated ones. People mis-judge probabilities at scale (one in a million is frequent at millions of operations). Test extreme legal values (a maximum integer, not-a-number, and zero versus lost signal are different things). Domain models need to distinguish "nothing present" from "zero". Learning from failures at every scale is the education; most failures cascade from humble starts. The effort is different, not more; it is mostly a conversation or one test.

## 7.7 Skilled expertise still decides
Successful agent-assisted engineering was reported by already-skilled people who know what good looks like (ch09); the same holds for QA: a tool is easy to be impressed by unless you can judge test portfolios (more or less coverage where).

## Cross-references
Chapter 01 for the engineering process (pipeline), chapter 05 for the quality properties, chapter 08 for measurement.
Chapters 10 to 12 for function-level design and error handling; chapter 13 for tool mastery and benchmarks as craft habits.
