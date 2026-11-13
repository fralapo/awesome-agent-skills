# Chapter 04: Test Design, the Pyramid and Reliable Tests

## Core Idea
A test suite is judged by properties, not by labels: is it fast, cheap, predictive of production success and supportive of design change? And a test is only useful if it passes or fails **for the right reasons, deterministically**. In this model most unreliability has five known causes, all fixable.

## 4.1 Testability and design
- **Thesis (position)**: every testability problem has an underlying design problem; fix the design and testing gets easy.
- **Mechanism**: examples: a private method you want to test is often an abstraction waiting to be extracted; having to change many tests for one change signals duplication or coupling; code that is hard to test against a framework signals poor separation between framework and domain; a long test set-up signals too many dependencies. Writing a test is writing a program to understand a program; if that is hard, the program is hard to understand.
- **Trade-off**: people conclude "testing is hard" when they test code never designed to be tested.
- **Does not hold when**: the difficulty comes from the environment (slow I/O) rather than structure; then isolate the boundary.
- **Also**: the simplest way to make architecture testable and reproducible is to keep host-environment definition, code and tests together under version control (4.7).

## 4.2 The Test Pyramid and its problem
- **Thesis**: the pyramid says most tests should be fast and cheap, few slow and expensive; its labels (unit, service, UI) are ambiguous.
- **Mechanism**: it assumes test granularity correlates with speed and cost, which is not necessarily true: some unit tests are hopelessly slow and some end-to-end tests fast enough to support refactoring. "Unit test" historically meant a manual test performed by another group in a V-model process; "service test" is often misread as any integration test, whereas its defining feature was being written from the customer perspective. Drawing speed and cost as axes (not layers) moves the conversation from "which type" to "is it fast and cheap enough".
- **Trade-off**: the pyramid is still a useful default (fast tests majority, slow ones added only when needed).
- **Does not hold when**: your architecture makes broad tests cheap, or your small tests are slow.

## 4.3 Test deciderata: four macro properties
In this model a suite should be:
1. **Fast** (to run).
2. **Cheap** (to write and maintain).
3. **Predictive of deployment success**: finds the bugs that would appear in production. UI-driven tests are slow and flaky but find interesting bugs, which is why we tolerate them; running the GUI is not the same as running the whole system, so ask which risk each test addresses and whether a cheaper route covers it.
4. **Supportive of ongoing design change**: tests written first drive design and document intent; after-the-fact tests tend to be coarse and mock-heavy, brittle under refactoring and costly. They also act as documentation of *why* the code exists, from the user's or customer's perspective.
- **Trade-off**: you trade the three of speed, cost and predictiveness explicitly.
- **Does not hold when**: you only have a handful of tests; fix reliability first.

## 4.4 Why flaky tests are expensive
- **Thesis**: a test that sometimes passes and sometimes fails under the same circumstances erodes trust in all tests, then in quality, then morale.
- **Mechanism**: teams learn to ignore failures, so real failures hide behind "that one is flaky". Teams often cannot even list which tests are flaky.
- **Trade-off**: fixing takes real time; leaving them costs more.

## 4.5 Handling flaky tests: process
1. **Find them**: automated retries to classify (pass once, fail twice = flaky) or cross-build comparison of the same test; do not rely on feel.
2. **Stop poisoning the suite**: quarantine to a separate build or time-boxed ignore tag; delete tests whose purpose nobody understands and schedule a rewrite.
3. **Fix them**: root-cause; schedule it (a backlog card, a fixed time slot, team swarming to find common causes) rather than "later".
4. **Inherently flaky tests** (external services, databases, heavy dependency graphs) run elsewhere; do not make every test depend on them. Break big end-to-end tests into smaller, controllable ones using stubs and harnesses.
- **Does not hold when**: the "flakiness" is a genuine race condition in production code, in which case the test has found a real defect.

## 4.6 Do not "retry until green"
- **Thesis (position)**: automatically rerunning failed tests is a mistake.
- **Mechanism**: the test has shown it lies at least once; passing on retry says nothing about whether the failure was real. Use tests as falsification: one deterministic failure is definitive proof, passing is not proof. Manual regression testing is also rejected: people are poor at precise repetition; machines excel (manual exploratory testing is fine).

## 4.7 The five causes of unreliable tests
| Cause | Remedy |
|---|---|
| **Environment** (unstable configuration, changing OS, disk, database location) | Control the environment: infrastructure as code in version control, test in an accurate clone of production, trigger the pipeline on any repo change; for software on environments you do not control, state supported targets and sample them |
| **Test data / isolation** (shared writable data, order dependency) | Atomic, isolated tests that can run in any order, in parallel, repeatedly. Use functional isolation (each test creates its own account, product, game with unique names) and temporal isolation; no shared writable data between tests. Isolation can be at the scope of whole system copies, but a shared system with fine-grained isolation is usually more efficient |
| **Versions** (version of system under test vs version of tests; versions of components of a larger system) | Keep tests with the code they test; version the environment definition too; for several teams' components define "releasable" at the scope of an independently deployable unit; if teams are not truly decoupled, integrate and test them together at least daily (CI) with a manifest of exactly which versions work together |
| **Resources** (overused disk, memory, CPU in test environments) | Automate and version-control so capacity can be added easily |
| **Behaviour of the system itself** (randomness, concurrency) | Control time and randomness in tests (time travel tests), isolate concurrency architecturally (event-based actor-style systems are highly deterministic), and in tests wait for a result for each invocation before the next instruction to remove race conditions |
After removing all five, any remaining intermittency points at a real problem in the system under test, which is exactly what the test exists to find.

## 4.8 Speed of feedback as a design lever
Reducing a nightly build to under an hour moved one organisation from very few fully green builds over years to at least one a day (reported anecdote). Test distribution and predictive test selection speed suites, but only work when tests are well separated. Quality cannot be inspected in afterwards; it has to be built in where the code is written.

## Cross-references
Chapter 03 for TDD itself; chapter 05 for what testability says about coupling; `coding-with-agents` for AI-generated tests (ch09 here).
