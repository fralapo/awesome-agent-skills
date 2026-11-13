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
