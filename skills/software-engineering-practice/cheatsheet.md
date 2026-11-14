# Software Engineering Practice: Cheatsheet

Figures are rules of thumb or approximate values; re-test. "Position" = practitioner judgment, not evidence. Chapter references in brackets.

## Where to Start
| Situation | First move |
|---|---|
| Fear of releasing | Pipeline that tries to falsify every commit; measure cycle time [ch01] |
| Branches live for days | Integrate at least daily; toggles for unfinished work [ch02] |
| Do not know what to test | Test list, simplest useful case, problem not solution [ch03] |
| Test hard to write | Design signal: extract, separate, humble object [ch03, ch04] |
| Tests flaky | Detect, quarantine with expiry, fix, never auto-retry [ch04] |
| Everything depends on everything | Name the kind of coupling; pick design or feedback [ch05] |
| Over- or under-engineering | YAGNI plus modularity from day one [ch06] |
| Measuring improvement | Hypothesis plus 2-3 balanced metrics [ch08] |
| Agent output untrusted | Examples, test list, predicted TDD, gates [ch09] |
| Many parameters | Parameter object for orchestration; plain values for helpers [ch10] |
| Flags and branches pile up | One policy per rule, composed; config-driven switches [ch10] |
| Primitives with hidden rules | Value object validated at construction [ch10] |
| Third-party SDK everywhere | Boundary with own results and errors [ch11] |
| Duplicated code | Remove duplicated rules; keep cheap look-alikes; no flag-driven merges [ch11] |
| Inheritance tangle | Compose; small interfaces; data for variations [ch11] |
| Error handling clutter | Fail fast; catch only where you can recover [ch12] |
| Slow benchmark claim | Real conditions, medians, prefer built-ins [ch13] |
| Motivation or burnout | Feeling versus action; look for causes, not holidays [ch14] |

## CD in One Table
| Stage | Question | Tests | Target |
|---|---|---|---|
| Commit | Did I break something obvious? | Narrow, fast, no I/O | under about 5 min, about 80% of mistakes |
| Acceptance | Does it do what users need, deployably? | User-centred, production-like env | no more work after pass |
| Other | Fast, scalable, secure, resilient enough? | Specialised | releasability decided |
| Production | Get it to users safely | Canary, blue-green, observability | business decides timing |

## TDD Phases
| Phase | Mindset | Do | Do not |
|---|---|---|---|
| Red | Specification, consumer of the API | Predict failure, see it | Add back doors |
| Green | Tactical | Smallest step, hard-code if needed | Design cleverly |
| Refactor | Strategic | Improve tests and code | Skip it |

## Five Kinds of Coupling
| Kind | Smell |
|---|---|
| Operational | Cannot start without the provider |
| Developmental | Must change together |
| Semantic | Shared meaning, no code link |
| Functional | Same problem solved several ways |
| Incidental | Together for no reason |

Danger zone: strongly coupled + slow feedback (more than a day). Survivable: decoupled, or coupled with fast feedback. Rule: tighten the stable, loosen the uncertain.

## Test Suite Scorecard
Fast | Cheap | Predictive of production | Supports design change. Trade speed, cost and predictiveness explicitly.

## Five Causes of Unreliable Tests
Environment | Test data and isolation | Versions | Resources | System behaviour (randomness, concurrency). If still intermittent, it is a real defect.

## SPACE Dimensions
Satisfaction | Performance | Activity | Communication | Efficiency and flow. Use 2-3, in tension, from different dimensions. Never lines of code.

## DORA Four
Deployment frequency | Lead time | Change failure rate | Time to restore. Indirect indicators; signal, not action; no value measure.

## Code-Level Coupling
Global | Data | Stamp | Content | Structural | Temporal. Every fix trades one for a milder one; measure how far a change propagates (ch05.9, ch10.7).

## Abstraction Rule
Abstract when the pieces mean the same and change for the same reason; prefer duplication to the wrong abstraction; the pattern appears after the analysis (ch11).

## Do Not
- Call a CI server on a branch continuous integration.
- Rerun failures until green.
- Test after the fact and call it TDD.
- Use delivery metrics as individual targets.
- Drift into strong coupling with slow feedback.
- Remove duplication with a function full of flags.
- Return a provider's objects or errors from a wrapper.
- Catch everything just in case.
- Trust a micro-benchmark as production performance.
