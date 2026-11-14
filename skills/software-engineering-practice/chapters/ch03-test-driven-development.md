# Chapter 03: Test-Driven Development

## Core Idea
In this model, test-driven development (TDD) is first a **design discipline** and only second a source of regression tests. Writing the test first makes you the first user of your own code, so design problems surface immediately. Its value depends on writing the test *before* the code.

## 3.1 The loop
- **Thesis**: TDD is a small repeatable process, not "write tests".
- **Mechanism**: think about the problem and write a **test list** (small behaviours, kept dynamic: add and cross off items). Take one item: write the test, *predict how it will fail*, run it and see exactly that failure (red); write the minimum code to pass, committing any design sin you like (green); refactor tests and code while green; pick the next item. You are always either all-green or have exactly one failing test, and you know which.
- **Trade-off**: small steps feel slow at first; the feedback every few minutes is the payoff.
- **Does not hold when**: you cannot define an expected result up front (see 3.9).

## 3.2 Three mindsets
- **Thesis**: each phase needs a different way of thinking; most newcomers get one wrong.
- **Mechanism**:
  - **Red**: specify behavioural intent as clearly as possible; design the public interface from the consumer's side; do not compromise encapsulation or add back doors. Name tests as "should ..." to stay in behaviour rather than after-the-fact testing. Check the test can fail at all (a test that still passes when the code is removed tests nothing).
  - **Green**: be tactical. Smallest, simplest steps back to a stable passing state, even naive code or hard-coded returns. Consciously suspend design thinking.
  - **Refactor**: now think strategically about separation of concerns and expressiveness, in both tests and code, while the passing tests protect you.
- **Trade-off**: skipping refactor (the stage most people miss) leaves the design to rot.
- **Does not hold when**: no experienced person is available and the team has no feedback; start with a short kata.

## 3.3 Design feedback is the main benefit
- **Thesis (position)**: TDD gives the fastest, most visceral feedback on design quality available; a test that is hard to write is the code telling you its design is wrong.
- **Mechanism**: the pressure to keep tests simple pushes toward testable code, and testable code is by definition modular, cohesive, separated, with clear abstraction and loose coupling. Writing the test is designing the interface; the implementation step is tactical; refactoring designs the inside. A related claim: TDD teaches design, since every difficulty in TDD is a design difficulty.
- **Trade-off**: it exposes how good or bad your design is, which can feel uncomfortable; learning good design is a lifetime's work, while the core mechanics of TDD take weeks.
- **Does not hold when**: you already design testable code by habit; then the incremental design pressure matters less (experienced practitioners report adapting the practice).

## 3.4 Test first vs test after
- **Thesis (position)**: tests written after the code lose more than half the value; unit testing afterwards is better than none but not TDD.
- **Mechanism**: after-the-fact tests are tightly coupled to the chosen implementation, so changing code fails tests and changing tests weakens them; code and tests "concrete together". You also lose the design feedback and the chance to specify before solving. Adding a failing check after the fact to "see it fail" only confirms the test can fail.
- **Trade-off**: test-first needs a different habit (specify what you want before how).
- **Does not hold when**: you are characterising legacy code (use approval tests, 3.8).

## 3.5 Test the problem, not the solution
- **Thesis**: a common beginner mistake is imagining the solution in order to test it.
- **Mechanism**: describe the problem as an executable specification and ignore the solution. Start with the simplest useful case, for example adding whole-number fractions before proper fractions. Use that first test to explore the shape of the interface. Pick each next test to advance the design (not a repeat of what passed already), moving to more complex cases step by step (add denominators, then common denominators). Two of something is as good as many for testing a loop; if you worry about huge sizes, specify the limit as its own test. Test that recursion terminates.
- **Trade-off**: thinking one or two steps ahead is allowed ("keep your brain engaged") but over-designing ahead is the beginner bear trap.
- **Does not hold when**: the unit is trivial; do not wrap library behaviour in tests.

## 3.6 Practical habits
- **Backward comments**: write the test as comments first, starting with the assertion, then the action that triggers it, then the state needed (arrange); fill code after.
- **Given / when / then** structure; ideal test is about three lines and has one reason to fail. A test that cannot separate given from when signals several tests in one.
- **Finish a session on a failing test** as a bookmark; next time the next step is obvious.
- **Tests as the place for decisions**: writing down the paths and decisions as tests reduces the overload of keeping them in your head.
- **Less debugging**: fine-grained tests with a single reason to fail point at the cause.
- **Names matter**: when a test fails in a CI list, its name should hint at the broken area.

## 3.7 Self-testing code is the goal, TDD the best route
- **Thesis (position)**: the key output is code that can be told "test yourself" and reports green or not; TDD is the best-known way to get it and also helps design.
- **Mechanism**: in any new technology the first job is to establish the self-testing set-up. For hard-to-test parts (UI, remote calls) apply the **humble object** idea: move as much behaviour as possible into an easily testable object and keep the awkward one trivial.
- **Trade-off**: other routes exist but are generally less effective.
- **Does not hold when**: output is exploratory and has no expected value (a site-generation tool tested by diffing the whole output against a known-good build is a crude but valid regression test).

## 3.8 Approval tests and characterisation
- **Thesis**: approval tests pin down current behaviour; they are excellent for legacy code but are a different thing from canonical TDD.
- **Mechanism**: the act and arrange are defined, the assertion is the approved output. Used to drive development you iterate on one test until the diff looks right. In this model that does not drive design or verify intent up front, since the expected result derives from your solution.
- **Trade-off**: fast feedback and low effort vs weaker specification. Practitioners disagree whether it counts as TDD (position).
- **Does not hold when**: you can state the expected result before implementing.

## 3.9 Objections and answers
| Objection | Answer in this model |
|---|---|
| It limits creativity | Tests are tools like a ruler: they explore, not dictate |
| It works against design | It is itself a design approach |
| I cannot test before seeing the implementation | You only need the interface; but you must understand the context (an existing component may make the test far simpler) |
| It is hard to adopt | Mostly because people write tests after and call it TDD |
| There is no data | True: evidence for TDD specifically is thin and often from small student studies; the argument rests on engineering reasoning plus data for CI |
| Unit tests do not prove much | Correct: they show the code does what you meant; broader testing is still needed (ch01, ch04) |

## 3.10 Behaviour-driven roots
Behaviour-driven development began as a better way to teach TDD by focusing on words: tests specify what software should do, not test what it already does. A related framing calls it example-guided development (see ch09 for why this suits AI agents).

## 3.11 A conventional five-step framing and test hygiene
- **Thesis**: the cycle can be stated as five steps and a few hygiene rules protect it from decay.
- **Mechanism**: (1) write tests that pass only if the feature specification is met (this forces thinking about requirements and interface first); (2) run them and **confirm they fail**, which proves they test the new behaviour; (3) write the simplest code that passes, without polishing; (4) run the **whole** suite, old tests included; (5) refactor with the suite green. Repeat in small steps with frequent commits. Hygiene: do not share one mutable fixture between tests (each test builds its own state through set-up and tear-down, so one test cannot change another's result); do not test the standard library; compare with **fixed expected values**, never with a copy of the implementation inside the test (that only checks the copy against itself); money and other exact quantities need exact types, not floats, and floating comparisons need a tolerance.
- **Trade-off**: more code and upkeep. In an early-stage product that may be discarded, heavy testing can be wasted; coverage numbers make the trade-off explicit, so do not chase a percentage.
- **Watch for**: a **false sense of security** (many passing unit tests may reduce effort on integration and end-to-end checks, ch04); **blind spots** when one person writes both the tests and the code and misreads the specification the same way twice (position: separate the roles where a team allows, or pair on the specification).
- **Does not hold when**: exploring with no expected value (3.7).

