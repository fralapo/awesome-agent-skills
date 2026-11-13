# Chapter 06: Design, Architecture and Incremental Design

## Core Idea
Design and architecture are the same kind of thinking (decisions that map needs onto software) at different scales. In this model **architecture is the set of design decisions that are expensive to change**, so the practical aim is to keep that set small by staying modular, well tested and skilled at refactoring.

## 6.1 Design versus architecture
- **Thesis**: there is a sliding scale between design (cheap to change) and architecture (expensive to change); skill transfers between the two.
- **Mechanism**: architecture-end decisions (monolith or distributed, cloud platform, data and transactions); design-end decisions (arguments of a method, shape of a conditional). Both identify abstractions, understand context and trade off. The difference is the scale of impact and breadth of context. Where the dividing point sits moves; in legacy code, even a method's argument list can become an architectural decision because unknown clients depend on it.
- **Trade-off**: pushing the point towards "cheap" requires investment in the three factors below.
- **Does not hold when**: you treat architecture as a title or role; it is a property of decisions.

## 6.2 Three factors that keep decisions reversible
1. **Modularity** (good abstractions and API design, with cohesion, separation of concerns, loose coupling): reason about change inside a module and minimise blast radius.
2. **Automated tests**: even if you cannot reason about the impact of a change, good tests show which behaviour it changed. Slow, flaky or mock-heavy tests get in the way.
3. **Refactoring skill**: change structure without changing behaviour using known techniques, smell recognition and deterministic tools. This is also what lets a team say "yes" to an unexpected, valuable request.
- **Trade-off**: each costs ongoing investment.
- **Does not hold when**: the system is short-lived.

## 6.3 Incremental design versus big upfront design
- **Thesis (position)**: agile does not mean stop designing; coding is design, so you design continuously, in small steps. Both big upfront design and naive flailing are wrong.
- **Mechanism**: a middle path: build a rough mental model while the problem is explained (think of a fuzzy ball with sticks and levers), sketch it informally in minutes to hours (a few days for a broad overview of a big project, at most), then validate with tests and code. Hold commitment lightly: understanding of the problem and the first solution are both probably wrong, so do not commit solidly to the first idea. Look for the simplest thing that works, but note there are two kinds of simple, simple-stupid and simple-smart.
- **Trade-off**: the line between them is partly art.
- **Does not hold when**: the problem is trivial and well-known.

## 6.4 YAGNI done well
- **Thesis**: "you aren't going to need it" targets over-engineering (scalability for millions when three users show up), not design.
- **Mechanism**: a naive reading ("my code is simple so any design will do") lets everything pile into one class. Instead adopt heuristics from day one: keep modular, cohesive, separated, abstract, coupling managed. Leave doors open without building the room behind them: you do not predict the detailed future, you make the code easy to change so you can revisit it. Some early abstractions will be trivial or wrong and get deleted; that is part of evolutionary design. Splitting a small class early may strictly violate YAGNI but keeps tests durable and options open.
- **Trade-off**: you accept small unneeded structure for lower risk of expensive rework.
- **Does not hold when**: separation costs more than the entire rework it might avoid (a throwaway tool).

## 6.5 Design through refactoring and the design in mind
- **Mechanism**: at every stage keep a guiding structure that tells you where behaviour should live, even before an obvious place exists. New ideas change the model, which may force a pause on architecture. Divisions between architecture, design and code are blurred; all should be iterative and incremental.
- **Marker of quality**: if we are afraid to change it, the design is poor; if we can change it radically without fear, it is good.

## 6.6 The succession problem
- **Thesis (position)**: all development is incremental, but feedback often is not; the hard question is how thin the slices are and in what order you eat them.
- **Mechanism**: size the feedback loop to match the change loop (a new line every ten seconds suggests feedback every ten seconds as the ideal). Many sequences produce the same result; consciously shaping the *unfolding* of the program, not only its final structure, gives more options. Practise by re-implementing the same exercise with different test orders to learn which test teaches most. Question to ask: why can't we release today's change today, and what stands in the way?
- **Trade-off**: finding the sequence that maximises learning can be hard, and is rarely discussed.
- **Does not hold when**: the predicted value is nearly all the value and little will be learned (then big chunks are fine); in the material's view this is rarely the case, because revealed value can exceed predicted value by orders of magnitude.

## 6.7 Options and reversibility
Every line of code creates or collapses future options. Deleting a bad attempt quickly (a few minutes of work) is better than defending it. Technology and delivery practices have made once-hard changes cheaper (for example a hosting-region move reported as a few lines of infrastructure code). Constraints that used to be review boards can be run as automated checks in the pipeline (fitness functions).

## Cross-references
`software-architecture` for the architecture decisions themselves. Chapter 05 for coupling vocabulary; chapter 03 for design driven by tests.
