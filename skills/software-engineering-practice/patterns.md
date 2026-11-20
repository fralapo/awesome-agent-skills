# Patterns

Recurring situation -> move. Each entry: When / Move / Cost / Not when. Chapter in brackets. Entries marked (position) are practitioner judgment, not evidence.

## 1. "We deploy often, are we doing continuous delivery?"
**When**: frequent releases but fear before each one.
**Move**: ask whether any commit could be released now and how long the verdict takes; measure cycle time from idea to users; build a pipeline that tries to falsify each commit. [ch01]
**Cost**: automation investment before the benefit.
**Not when**: the artefact cannot be produced repeatedly.

## 2. Slow or unclear feedback on a change
**When**: failures are found days or weeks later.
**Move**: commit stage in about five minutes catching about 80% of mistakes, developer-centred tests only; acceptance stage for the rest. [ch01]
**Cost**: tests must be narrow, no whole-app start, disk or network.
**Not when**: the system is tiny and everything already runs in seconds.

## 3. Manual regression testing
**When**: a test phase follows development.
**Move**: automate regression, keep manual testing for exploration. [ch01, ch04]
**Cost**: upfront automation.
**Not when**: one-off.

## 4. Long-lived feature branches
**When**: branches live for days or weeks.
**Move**: integrate into the shared line at least daily in small steps; use feature toggles, dark launching, branch by abstraction for unfinished work. [ch02]
**Cost**: change in working habits, less private progress.
**Not when**: you are the only committer, or the work shares nothing. (Position: feature branching can work but is not the best option.)

## 5. "I merge trunk into my branch, so I do CI"
**When**: a CI server runs only on branches.
**Move**: measure the dark period (time since your changes met everyone else's) and shorten it; define CI as merging daily. [ch02]
**Cost**: confronting the definition.
**Not when**: the team agrees on a different goal.

## 6. A merge or integration "day"
**When**: scheduled painful integration.
**Move**: shrink the interval until integration is a non-event; integration tests across components run on every commit or at least daily. [ch02, ch04]
**Cost**: pipeline capacity.
**Not when**: components are truly independent and independently deployable.

## 7. Blank page in TDD
**When**: you do not know what to test first.
**Move**: write a test list; pick the simplest useful case; test the problem not the solution; write the test backwards in comments (assertion, action, set-up). [ch03]
**Cost**: slow start.
**Not when**: no expected output exists (use approval testing for characterisation).

## 8. Test is hard to write
**When**: long set-up, many mocks, private method wanted.
**Move**: treat it as a design signal; extract the abstraction, separate framework from domain code, humble-object the awkward edge. [ch03, ch04, ch05]
**Cost**: refactoring effort.
**Not when**: the awkwardness comes from slow environment I/O only.

## 9. Tests written after code
**When**: code first, tests later.
**Move**: for new code switch to test-first; for existing code use characterisation/approval tests, then refactor into testable shape. [ch03]
**Cost**: relearning the habit.
**Not when**: spike code that will be discarded.

## 10. Flaky test suite
**When**: tests pass on rerun.
**Move**: detect (retry classification or cross-build comparison), quarantine with an expiry, schedule fixing, delete untrusted tests; move inherently flaky ones to another build; never auto-retry to green. [ch04]
**Cost**: dedicated time.
**Not when**: the flakiness reveals a race in production code (then fix the product).

## 11. Order-dependent tests
**When**: one test changes data another reads.
**Move**: isolate functionally (create unique accounts, products, per test) and in time; no shared writable data. [ch04]
**Cost**: test infrastructure for unique naming.
**Not when**: read-only reference data.

## 12. Many teams, many versions, unclear releasability
**When**: independent small services still fail together.
**Move**: define releasability at the scope of an independently deployable unit; if not truly decoupled, test the combination daily with a manifest of working versions. [ch04, ch05]
**Cost**: shared pipeline effort.
**Not when**: genuinely independent contracts and consumer checks exist.

## 13. Reviewing the test suite
**When**: unsure what to add or remove.
**Move**: score the suite on fast, cheap, predictive of production, supportive of design change; for each slow test ask which risk it covers and whether a cheaper test covers it. [ch04]
**Cost**: an hour of analysis.
**Not when**: fewer than a handful of tests.

## 14. Strong coupling and slow feedback
**When**: services deployed separately but sharing state or schema.
**Move**: pick deliberately: decouple by design, or speed feedback (CI across the group), or both; never remain in the combination. [ch05]
**Cost**: design work or pipeline work.
**Not when**: already decoupled with fast feedback.

## 15. Naming a coupling problem
**When**: "everything depends on everything".
**Move**: classify as operational, developmental, semantic, functional or incidental; apply the remedy for that type; remember coupling moves, it does not vanish. [ch05]
**Cost**: analysis.
**Not when**: coupling is to something stable and understood.

## 16. Choosing between SQL, API and events across a team boundary
**When**: a consumer team depends on a data team.
**Move**: put the boundary where coupling is stable: API owned by the data team insulates schema change; events weaken operational and developmental coupling at the cost of semantic coupling. [ch05]
**Cost**: translation work.
**Not when**: schema is stable and teams are the same.

## 17. Fear of over-engineering vs big ball of mud
**When**: "YAGNI, do not design yet".
**Move**: build only what is needed now but with modularity, cohesion, separation, abstraction and managed coupling from day one; refactor early when a trivial separation keeps tests durable. [ch06]
**Cost**: small extra structure.
**Not when**: throwaway code.

## 18. Making decisions cheaper to reverse
**When**: architecture feels frozen.
**Move**: raise modularity, test quality and refactoring skill; replace review-board constraints with automated checks in the pipeline. [ch06]
**Cost**: sustained investment.
**Not when**: short-lived system.

## 19. Sequencing a big change
**When**: a large piece of work seems indivisible.
**Move**: ask how thin the slices can be and in what order; match feedback frequency to change frequency; try alternative orderings. [ch06]
**Cost**: planning thought, sometimes re-implementation for practice.
**Not when**: predicted value is nearly all the value and little will be learned (rare).

## 20. "Is software craft or engineering?"
**When**: debate about process vs skill.
**Move**: keep craft skill, add measurable constraints (properties of quality, tests, fast feedback) that rule out non-viable solutions. [ch07]
**Cost**: some discomfort with the word engineering.
**Not when**: output is purely aesthetic.

## 21. Speed vs safety argument
**When**: "we cannot go faster, it is safety-critical".
**Move**: work in small verifiable steps, design for failure, test extreme values, avoid giant functions; compare with survey evidence that speed and quality correlate positively (correlation only). [ch07]
**Cost**: skills and rigour.
**Not when**: regulation prescribes a process; comply and apply within.

## 22. Choosing productivity metrics
**When**: asked "how do we measure improvement?"
**Move**: state a hypothesis; choose two to three measures in tension across different SPACE dimensions; time-box; rotate as data improves; keep delivery metrics (DORA) for signal and the practice research for action. [ch08]
**Cost**: attention; imperfect data.
**Not when**: the measures will be used as individual targets.

## 23. Metrics reported to management
**When**: delivery metrics appear on executive dashboards.
**Move**: keep them as team diagnostics; present them as a balanced set with outcome measures; do not rank people. [ch08]
**Cost**: explaining.
**Not when**: management understands lean and agile.

## 24. Operations hand-offs and slow recovery
**When**: a separate operations team gets the first page for services it did not build.
**Move**: you build it, you run it for modern services: product team on call, alerts go to them first, compensate availability and call-outs, clarify accountability with funding; leave legacy services where they are. [ch08]
**Cost**: budget shifts, on-call disruption.
**Not when**: you cannot start properly; do it right or not yet.

## 25. Team is overloaded
**When**: slow delivery, incidents, burnout.
**Move**: diagnose drivers across composition, work clarity, environment and dependencies; remove avoidable load (approvals, dependency chains), add platform golden paths, accept justified temporary load for learning. [ch08]
**Cost**: honest diagnosis.
**Not when**: the load is the intrinsic hard problem the team wants.

## 26. Prose requirements fed to an agent
**When**: output is plausible but not what was wanted.
**Move**: do example mapping with stakeholders, derive a test list, run red-green-refactor with predicted failures, choose a human-in-the-loop level. [ch09]
**Cost**: tokens and upfront conversation.
**Not when**: spec is already executable.

## 27. Agent writes tests that merely echo the code
**When**: high test counts but weak value.
**Move**: provide the user perspective, review for intent, check mutation score, keep humans designing the important tests. [ch09, ch04]
**Cost**: review time.
**Not when**: characterisation.

## 28. Reducing human code review
**When**: review is a bottleneck.
**Move**: define gates (tests, static checks, size limit); require review above the limit; make good-change criteria explicit. [ch09]
**Cost**: building strong gates first.
**Not when**: gates are weak.

## 29. A group of values travels through many functions
**When**: every signature carries the same four or five arguments; adding an option touches them all.
**Move**: introduce an immutable parameter object that validates itself at construction and owns derived values; use it in high-level orchestration; pass plain values to small helpers. [ch10]
**Cost**: one more concept to name.
**Not when**: the helper needs one field (stamp coupling) or a split of responsibilities removes the need.

## 30. One function grows a flag or branch for every new rule
**When**: boolean flags interact in non-obvious ways; each requirement edits the same body.
**Move**: one policy per rule; compose them (list or pipeline); optionally build the list from configuration so rules switch on and off without conditionals. [ch10]
**Cost**: more code, more up-front thinking.
**Not when**: a throwaway script or a rule set that stays tiny.

## 31. Bare numbers and strings carry hidden rules
**When**: a price, discount or email is a primitive and every function re-validates it; units and ranges are ambiguous.
**Move**: value object, immutable, validated once at construction; behaviour lives with the data. [ch10, ch12]
**Cost**: more types and conversions at the edges.
**Not when**: the primitive has no rule or meaning.

## 32. A third-party SDK leaks through the codebase
**When**: provider objects, error classes and vocabulary appear in business logic.
**Move**: build a boundary: domain operations, your own result and error types, a fake for tests; avoid pass-through and god wrappers; expose behaviour callers need to know. [ch11]
**Cost**: a layer to maintain.
**Not when**: one call in one place with no change expected.

## 33. A small change breaks unrelated features
**When**: adding a field to one step breaks analytics and invoicing.
**Move**: split the workflow into phases; keep orchestration separate from domain rules; collect shared data in the owning record; stop reaching through object chains; place interfaces at the infrastructure edge; ask "how far does a change propagate?". [ch10, ch05]
**Cost**: refactoring effort.
**Not when**: a short script one person owns.

## 34. Removing duplication made the code harder to read
**When**: a merged "generic" function needs flags and a misleading name.
**Move**: undo; split by responsibility (filter versus normalise); remove duplicated rules, keep cheap similar loops; keep duplication that protects a boundary; abstract when meaning and reason to change match. [ch11]
**Cost**: some visible repetition.
**Not when**: the copies must stay in lockstep (a rule); remove that duplication.

## 35. Patterns and tiny classes outweigh the problem
**When**: a strategy hierarchy and factory for one string; a container and interface with a single implementation.
**Move**: replace with functions and a dictionary; group settings that change together; make the pipeline explicit; add an interface only where variation really is (typically provider-specific details); let the pattern emerge. [ch10, ch11, ch06]
**Cost**: unlearning the checklist.
**Not when**: many variants are certain.

## 36. Inheritance used for reuse
**When**: a class inherits two parents for one method each; subclasses per value or per feature combination; read-only subtype that fails on write.
**Move**: compose; model values as data; separate capability interfaces; keep inheritance for true is-a. [ch11]
**Cost**: wiring and delegation.
**Not when**: the subtype honours every guarantee of the parent.

## 37. Try-blocks wrap every line
**When**: nested handlers, catch-all clauses, errors printed and ignored.
**Move**: fail fast; catch only where you can recover; one top-level handler; scoped resources; a library exception hierarchy; specific messages; logs without secrets. [ch12]
**Cost**: crashes are visible; needs monitoring.
**Not when**: serious consequences or real-time constraints.

## 38. Return null or raise?
**When**: lookups and optional parameters leave callers to test for absence.
**Move**: by identifier, raise not-found; many results, empty list; optional parameters only when absence has meaning. [ch12, ch10]
**Cost**: exceptions in flow.
**Not when**: absence is an ordinary outcome.

## 39. Stuck on one tool, afraid of the hard task
**When**: only the comfortable editor and stack; avoiding tasks you might fail.
**Move**: become great at the tools in use; try a different one on purpose; recall solved problems; say yes to unfamiliar work with a pause rather than a reflex. [ch13, ch14] (position)
**Cost**: slower at first.
**Not when**: hard deadline or unsafe workload.

## 40. "My version is faster" from a micro-benchmark
**When**: a timing loop on a developer machine drives a decision.
**Move**: measure under real conditions with a clean state, many runs, medians then averages, and margins of error; prefer the platform's built-in where one exists. [ch13]
**Cost**: slow experiments.
**Not when**: the path is proven hot in your own profile; measure there.

## 41. Flat, unmotivated or burnt out
**When**: dread, avoidance, malaise.
**Move**: separate feeling from action for ordinary reluctance (start, momentum follows); for persistent dread look for causes: boredom, validation placed in the job, outside circumstances; a holiday alone treats the symptom; change environment or workload; seek help for health symptoms. [ch14, ch08] (position)
**Cost**: honest reflection.
**Not when**: symptoms point to a health issue; seek professional help.

## 42. Promotion case built on hours or feelings
**When**: a person expects promotion because they work long hours or feel ready.
**Move**: read the written level descriptions; collect dated evidence of decisions, designs, outcomes and people unblocked; ask the manager in writing what is missing for the next level. [ch15] (position)
**Cost**: documentation time.
**Not when**: the company has no published levels; then agree the expectations explicitly before the cycle.

## 43. Noisy interview loop
**When**: rounds disagree, or hires do not work out.
**Move**: a fixed rubric per round; independent scoring before discussion; questions tied to the job; a work sample where feasible; probe reasoning aloud rather than recall of a known trick. [ch15]
**Cost**: interviewer preparation and candidate time.
**Not when**: the job depends on one well-known technique; test that technique directly.

## 44. Freelance income thin despite a good rate
**When**: a full calendar and a small margin.
**Move**: track a month of billable and non-billable time; price from the gross week plus self-funded benefits and overhead; cap the share of revenue from any one client or channel; hold a cash buffer. [ch16] (position)
**Cost**: higher quotes; some price-sensitive clients lost.
**Not when**: the work is a fixed deliverable with known effort; price the project instead.

## 45. Startup plan with untested assumptions
**When**: the plan depends on claims nobody has checked with the people who have the problem.
**Move**: list the assumptions the plan needs; for each, the cheapest test that could prove it wrong; run interviews, a prototype and a request to pay in order of dependence; record the result. [ch16]
**Cost**: delay that can feel unproductive.
**Not when**: a regulatory or technical feasibility question must be answered first.

## 46. Shared code and flags with no owner
**When**: switches accumulate; a shared directory has unclear approval.
**Move**: owner and removal date per flag; code owners per directory; automated style checks so reviews discuss substance; readability approval only where language idioms matter and enough people hold it. [ch17] (position)
**Cost**: gates and bookkeeping.
**Not when**: a small team that knows the code and the language well.

## 47. Legacy code nobody wants to touch
**When**: changes cause regressions and the original authors have left.
**Move**: characterisation tests of current behaviour (record known bugs first); find who or which record explains a decision; delete code nobody can explain after checking its use; change in small steps. [ch17, ch03]
**Cost**: slower first changes.
**Not when**: the code is short-lived or cheaper to rewrite completely.
