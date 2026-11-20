---
name: software-engineering-practice
description: "Software engineering practice for developers and team leads: continuous delivery and pipelines, continuous integration versus feature branching, test-driven development, test design and flaky tests, coupling, cohesion and complexity, design versus architecture and YAGNI, craft versus engineering, productivity metrics (DORA, SPACE), ownership and cognitive load, quality with AI coding agents, function-level design, duplication, abstraction, patterns, composition over inheritance, error handling and failing fast, engineering culture, careers and levels, hiring and offers, freelancing and startups, large-codebase ownership, motivation and burnout. Use when the user sets up a pipeline or branching strategy, learns or teaches TDD, fixes flaky tests, untangles coupling, debates over-engineering or DRY, simplifies a class design, chooses inheritance or composition, decides on error handling, picks metrics, prepares for a promotion or interview, or plans freelance or startup work. Separates facts from positions."
allowed-tools:
  - Read
  - Grep
argument-hint: [practice, problem, or chapter number]
---

# Software Engineering Practice
**Chapters**: 17 | **Generated**: 2026-11-13

## Role and Boundaries

This skill **decides how to work and reason as a software engineer**: how to organise integration and delivery, how to design tests and drive code from them, how to name and manage coupling, how to design functions, modules and abstractions at code level (and when patterns and DRY make code worse), how to handle errors, how to keep decisions cheap to change, how to measure improvement without distorting it, how to put engineering discipline around agent-written code, and how engineers sustain learning, motivation and health. It gives mechanisms, decision tables and checklists; the team owns context and the final choice.

| This skill decides | This skill hands off |
|---|---|
| Pipeline stages, branching and integration frequency, test strategy, TDD habits, coupling analysis, design-versus-architecture reasoning, metrics choice, ownership model, cognitive load diagnosis | System design of distributed systems (consistency, sharding, caching, messaging, resilience mechanics) and agent/RAG architecture -> `software-architecture` |
| Engineering discipline around AI-written code (examples, test lists, gates) | Working loop with coding agents, context, prompts, reviewing and token cost -> `coding-with-agents` |
| Function-level design, duplication, composition, injection, error handling | Architecture-scale styles (layers, hexagonal, boundaries between services, resilience such as circuit breakers) -> `software-architecture` |
| Career, motivation and burnout reflections | Medical or psychological care; organisational overload -> ch08; legal, tax or contract interpretation (ch15-16 give mechanisms only) |
| How to reason about quality and measurement | Running the workshop that agrees priorities -> `workshop-facilitation`; interface and flows of the product -> `ux-ui-expert` |

**Stay in lane.** The chapters hold practitioner theory, not benchmarks; ch15-16 give no legal, tax or contract advice and no figures for thresholds or rates. Figures are dated, context-bound snapshots; many outcome claims come from survey research and show correlation, not controlled proof. Where a point is unverified, the text says "unverified".

## Facts vs Positions

- **Mechanism / fact**: how a deployment pipeline falsifies a release candidate, why diverging copies need reconciling, what the five causes of unreliable tests are.
- **Position**: written as "In this model..." or "(position)": for example "feature branching is not the best option", "tests written after the code lose most of the value", "do not auto-retry failed tests", "a hard test means a design problem", "craft is not enough without constraints".
- Every concept in the chapters has fields **Thesis**, **Mechanism**, **Trade-off**, **Does not hold when**. Read the last one before recommending: if the limit applies, drop the rule.

## How to Use This Skill

Diagnose before prescribing: ask about team size, release frequency, current branching, how long a commit takes to get a verdict, test reliability, how teams depend on each other, and who operates the software.

| Task | Start with | Then |
|---|---|---|
| "What is continuous delivery? Build a pipeline" | [ch01](chapters/ch01-continuous-delivery-foundations.md) | ch04 (reliable tests), ch02 |
| Branching strategy, merge pain, "do we do CI?" | [ch02](chapters/ch02-continuous-integration-vs-feature-branching.md) | ch05 (coupling), ch01 |
| Learn, teach or defend TDD | [ch03](chapters/ch03-test-driven-development.md) | ch04, ch06 |
| Flaky or slow tests, test strategy, pyramid debates | [ch04](chapters/ch04-test-design-and-reliable-tests.md) | ch03, ch01 |
| Everything depends on everything, hard to change | [ch05](chapters/ch05-coupling-cohesion-and-complexity.md) | ch06, ch02 |
| Over-engineering vs mess, "design vs architecture", YAGNI | [ch06](chapters/ch06-design-architecture-and-incremental-design.md) | ch05, ch03 |
| Craft vs engineering, what is quality, safety-critical talk | [ch07](chapters/ch07-engineering-craft-and-software-quality.md) | ch05, ch01 |
| DORA, SPACE, productivity, output-volume metrics, on-call, team overload | [ch08](chapters/ch08-productivity-metrics-ownership-and-cognitive-load.md) | ch01, ch05 |
| Quality, TDD, debt and review with AI agents | [ch09](chapters/ch09-quality-and-tdd-with-ai-agents.md) | ch03, ch04 |
| Too many parameters, flags, primitives, brittle functions, data threaded through steps | [ch10](chapters/ch10-function-and-module-level-design.md) | ch05, ch11 |
| DRY, wrong abstraction, patterns, third-party SDKs, inheritance vs composition, SOLID, injection | [ch11](chapters/ch11-duplication-abstraction-patterns-and-composition.md) | ch10, ch06 |
| Exceptions, fail fast, raise vs return nothing | [ch12](chapters/ch12-error-handling-and-failing-fast.md) | ch10 |
| Tools mastery, learning a language, benchmarks, internals | [ch13](chapters/ch13-engineering-culture-tools-and-benchmarks.md) | ch07 |
| First job, motivation, burnout | [ch14](chapters/ch14-career-motivation-and-sustainability.md) | ch08, ch13 |
| Levels, promotion, calibration, team moves, performance reviews | [ch15](chapters/ch15-careers-levels-hiring-and-offers.md) | ch08 (ownership), ch14 |
| Hiring from either side, interview design, CV signals, offers, contracts, layoffs | [ch15](chapters/ch15-careers-levels-hiring-and-offers.md) | ch14 (first job) |
| Freelance pricing, client concentration, startup validation, funding terms, exits | [ch16](chapters/ch16-independent-work-startups-and-business.md) | ch15, ch14 |
| Monorepo, code owners, readability approval, feature flags, legacy code, first design, learning by rebuilding | [ch17](chapters/ch17-large-codebases-ownership-and-team-learning.md) | ch05, ch09, ch13 |
| Quick lookup | [cheatsheet.md](cheatsheet.md), [patterns.md](patterns.md), [glossary.md](glossary.md) | |

## The Core Principles (recurrence order)

1. **Feedback is the engine.** Shorten the time from change to trustworthy verdict; software work is mostly learning.
2. **Try to falsify, not to prove.** A deterministic failure is proof; a pass is not.
3. **Work in small steps, integrated daily.** Divergence costs more the longer it runs.
4. **Tests specify behaviour and expose design.** A hard test is a design signal; write the test first.
5. **Tests must be trustworthy.** Flaky tests destroy the signal; remove the five causes.
6. **Ability to change is the quality measure.** Modularity, cohesion, separation, abstraction, managed coupling.
7. **Coupling moves; it is never removed.** Choose and name it; avoid strong coupling with slow feedback.
8. **Keep decisions cheap to reverse.** Design continuously; avoid both big upfront design and unstructured guessing.
9. **Measure to learn, not to rank.** Balanced indicators; delivery metrics are signal, not action; keep them with the team.
10. **Ownership and load shape results.** Teams that run what they build, with manageable cognitive load, improve faster.
11. **Agents need the harness more, not less.** Examples, tests, gates and human judgment of what good looks like.
12. **Abstract by meaning, not by look.** DRY is about duplicated knowledge; prefer duplication to the wrong abstraction; patterns appear after analysis.
13. **Make invalid states unrepresentable and fail early.** Validate once at construction; catch only where you can recover.
14. **Sustain the engineer.** Habits, tools and effort that compound slowly; feeling is not a plan; burnout has causes, not just fatigue.

## Chapter Index

1. [Continuous delivery foundations](chapters/ch01-continuous-delivery-foundations.md)
2. [Continuous integration vs feature branching](chapters/ch02-continuous-integration-vs-feature-branching.md)
3. [Test-driven development](chapters/ch03-test-driven-development.md)
4. [Test design, the pyramid and reliable tests](chapters/ch04-test-design-and-reliable-tests.md)
5. [Coupling, cohesion and complexity](chapters/ch05-coupling-cohesion-and-complexity.md)
6. [Design, architecture and incremental design](chapters/ch06-design-architecture-and-incremental-design.md)
7. [Engineering, craft and software quality](chapters/ch07-engineering-craft-and-software-quality.md)
8. [Productivity metrics, ownership and cognitive load](chapters/ch08-productivity-metrics-ownership-and-cognitive-load.md)
9. [Quality and TDD with AI agents](chapters/ch09-quality-and-tdd-with-ai-agents.md)
10. [Function and module-level design](chapters/ch10-function-and-module-level-design.md)
11. [Duplication, abstraction, patterns and composition](chapters/ch11-duplication-abstraction-patterns-and-composition.md)
12. [Error handling and failing fast](chapters/ch12-error-handling-and-failing-fast.md)
13. [Engineering culture, tools, learning and benchmarks](chapters/ch13-engineering-culture-tools-and-benchmarks.md)
14. [Career, motivation and sustainability](chapters/ch14-career-motivation-and-sustainability.md)
15. [Careers, levels, hiring and offers](chapters/ch15-careers-levels-hiring-and-offers.md)
16. [Independent work, startups and building a business](chapters/ch16-independent-work-startups-and-business.md)
17. [Large codebases, ownership and team learning](chapters/ch17-large-codebases-ownership-and-team-learning.md)

## Topic Index

- **Acceptance tests, commit stage** -> ch01
- **Approval tests, characterisation** -> ch03
- **Branch by abstraction, feature toggles, dark launch** -> ch02
- **Benchmarks, micro-benchmarks** -> ch13
- **Burnout, motivation, first job** -> ch14
- **Cognitive load, platforms** -> ch08
- **Lines of code and token counts as metrics, verification bottleneck** -> ch08 (8.9)
- **Debt growth with generated code, deliberate deletion** -> ch09 (9.9)
- **Composition over inheritance, six OO mistakes** -> ch11
- **Connascence, Law of Demeter, stamp coupling** -> ch05, ch10
- **Custom exceptions, fail fast** -> ch12
- **DRY, duplication, wrong abstraction** -> ch11
- **Facade versus adapter, third-party SDKs** -> ch11
- **Parameter object, policies, value objects** -> ch10
- **SOLID, dependency injection, composition root** -> ch11
- **Conway's law** -> ch05
- **DORA, SPACE** -> ch08
- **Example mapping, predictive TDD** -> ch09
- **Flaky tests, isolation, determinism** -> ch04
- **Humble object, testability** -> ch03, ch04
- **Refactoring skill, reversible decisions** -> ch06
- **Safety-critical work, speed vs quality** -> ch07
- **Test pyramid, test deciderata** -> ch04
- **YAGNI, succession problem** -> ch06
- **You build it, you run it, on-call** -> ch08
- **Calibration, rating budgets, PIP, promotion case** -> ch15
- **Team matching, internal moves, visibility** -> ch15
- **Interview loops, structured interviews, work samples, CV screens** -> ch15
- **Offer comparison, equity risk, negotiation of package** -> ch15
- **Contracts: IP clauses, NDAs, declaring side projects** -> ch15
- **Layoffs, restructuring, hours versus impact** -> ch15
- **Freelance non-billable time, packages, cash buffer** -> ch16
- **Cash business versus equity business lens** -> ch16
- **Venture model, funding terms, primary versus secondary, earn-outs** -> ch16
- **Subscription versus one-off pricing software** -> ch16
- **Code owners, readability approval, pre-submit style checks** -> ch17
- **Feature flags as deployment switch, metric ramps** -> ch17
- **Legacy code, characterisation before change, dependency rot** -> ch17
- **First design is wrong, when informal coordination stops working** -> ch17
- **Rebuild a small system, 80/20, framework hopping** -> ch17

## Related Skills

- `software-architecture`: distributed-system design, architecture styles, resilience (circuit breakers), deployment independence, agent architecture.
- `coding-with-agents`: working method, context and reviewing when an agent writes code.
- `workshop-facilitation`: facilitating the sessions that agree scope, examples and acceptance criteria.

## Scope & Limits

Practical theory about continuous delivery, integration, testing, TDD, design (function level and incremental), abstraction and patterns, error handling, engineering culture and career, productivity measurement, team ownership and AI-assisted development. Not covered: tool-specific pipeline configuration, language-specific testing frameworks, security and compliance engineering, estimation and project management, medical or psychological advice. Chapters 10 to 12 use a Python-like language for examples; chapters 13 to 17 are practitioner opinion and personal experience, marked as positions (ch15-16 on careers and independent work are mechanisms, with no tax, legal or contract advice and no dated figures). Evidence for several claims is survey correlation or practitioner experience; AI-agent findings are early and model-dependent. The skill gives no legal, compliance or cost guarantee.
