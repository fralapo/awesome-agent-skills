# Chapter 09: Quality and TDD with AI Agents

## Core Idea
In this model, agents do not remove the need for engineering discipline; they move where it sits. The user's idea of quality stays the same, but **assessing whether software is good enough has become harder**, and the practices of fast feedback, examples, TDD and refactoring become the harness that keeps agent output honest. This chapter is positions drawn from practitioners; the evidence is early and partly self-reported.

## 9.1 Two kinds of quality, now both at risk
- **Thesis**: external quality (works, responsive, data safe) is unchanged; internal quality (code a human or agent meets) still matters even if humans read less of it.
- **Mechanism**: poor code makes agents consume more tokens, take longer and make more mistakes; names in code should carry the domain language because the agent cannot translate silently the way a human does. Whether agents need different quality attributes from humans is unverified (no strong evidence); for now what helps humans also seems to help agents.
- **Trade-off**: organisations at a higher abstraction level may care about operational and external quality and look less at the code; others still read everything.
- **Does not hold when**: the code is a throwaway.

## 9.2 Know what good looks like
- **Thesis (position)**: people who succeed with agents already know what good looks like and are good engineers; the same tools in the hands of people who have never written a good test produce piles of worthless ones.
- **Mechanism**: you must be able to be specific about what good looks like; otherwise the agent cannot produce it. Where understanding is vague you need a different working mode (exploration), not a one-shot spec. Large up-front specs written over weeks and then implemented are "mini waterfall" with shorter timescales and the same results.
- **Trade-off**: tacit team knowledge has to be written down; it helps new joiners too.
- **Does not hold when**: the problem is fully understood.

## 9.3 Example-first workflow
- **Thesis**: concrete examples work better than prose descriptions, for humans and for agents; TDD and its relatives (behaviour-driven, acceptance-test-driven, specification by example) can be viewed as example-guided development.
- **Mechanism**: a reported workflow: (1) a collaborative human step of **example mapping** with stakeholders to build shared understanding; (2) turn it into a **test list**, with the agent checking for missing obvious permutations; (3) an inner loop, one item at a time, of red, green, refactor, with **predictive TDD**, that is, predicting the result and failure message before each step (which also keeps the agent aligned with reality, perhaps because the prediction brings the problem to the front of the context). Compared with giving prose rules to the agent, adding example mapping raised correctness by a large margin in their tests (reported as 60 to 80% in some cases; exact baseline unverified). Compared with plain "do TDD" prompts, the structured workflow gave lower complexity, shorter functions and higher mutation scores (test quality) at higher token cost.
- **Trade-off**: more tokens and more human involvement upfront. A dedicated refactoring sub-agent with fresh context helped on an earlier model generation and less on a later one (benefit shrinks as models improve; re-test).
- **Does not hold when**: you work alone on a tiny, exploratory problem; or when the requirements are already unambiguous executable specifications.

## 9.4 Human in the loop
- **Thesis (position)**: choose the level of autonomy deliberately (check every step, after refactor, after three tests, or fully autonomous).
- **Mechanism**: those who stay close, understand what the agent did and correct course get better results; the human builds and holds the mental model of the domain. Spec-driven frameworks that add ever more markdown can produce the same "looks good to me" fatigue of a huge pull request; front-loading the thinking with collaborative techniques is the alternative proposed.
- **Does not hold when**: the change is small and checked by strong gates (9.5).

## 9.5 Gates instead of reading everything
- **Thesis (position)**: one team's reported approach is to define what a good change looks like and let changes that pass automated gates (tests, lint, static analysis, size limit) skip human review, requiring review above a size threshold (an illustrative threshold of about 500 lines was mentioned, approximate and unverified).
- **Mechanism**: incentivises small changes, reduces blast radius, makes tacit standards explicit for agents and new people alike.
- **Trade-off**: you need strong gates first.

## 9.6 AI-generated tests are weak on intent
- **Thesis (position)**: tools generate tests sensitive to behaviour and cheap to maintain, but the test's *why* (the customer or user perspective, ch04 fourth property) is not visible from the implementation, and most training examples do not model it.
- **Mechanism**: include the user perspective in the prompt; review for intent; a mutation score helps assess test strength. Agentic exploratory-testing tools may reduce automation time and free time for exploring, but you still need testers' judgment of which areas need more or less coverage, in production feedback.
- **Does not hold when**: tests are used only as a regression net on existing behaviour (characterisation).

## 9.7 Does TDD still matter when the agent writes the code?
Two positions: (a) the inner loop of fine-grained TDD has largely gone to the agent, so its design value is smaller; (b) low-level internal quality still matters and a tight red-green-refactor loop with sub-agents, hooks or checks that force frequent refactoring keeps it. Both authors treat the question as open. TDD also remains a teaching and thinking aid for humans. For tests as feedback, one argument is that even superintelligent agents would need feedback loops from outputs, so continuous delivery would persist (speculative position).

## 9.8 Agents and abstraction
Writing detailed English instructions can approach programming at a higher abstraction level, but without version control and repeatability ("an incremental compiler that gives a different answer each time"). Specification through acceptance tests reinforces executable specification thinking. Developers' value is deciding what the problem is, not typing code; pairing with a stronger human remains something agents do not replace.

## 9.9 Debt can grow faster with generated code (position)
- **Thesis**: when producing code is cheap, internal quality decays unless something pushes back, and fluent code hides its complexity.
- **Mechanism**: generated code tends to add more lines and branches than needed and varies by model; a team that cannot read what it ships loses the ability to change it. Pushback is structural: small changes, automated gates, a tight refactoring step after each green test, architecture decisions kept by humans, and periodic deliberate deletion. Skills the human must keep: architecture and system design, judging a design, and reading tests for intent (9.6).
- **Trade-off**: slower than accepting everything, cheaper than a rewrite.
- **Does not hold when**: the code is disposable (a throw-away script, a prototype to be discarded).

## 9.10 Review debt: measure the gap, not the author
- **Thesis (position)**: the risk of agent-written code is the gap between what was produced and what someone understands and has reviewed. Measure the gap.
- **Mechanism**: a deterministic score can track signals such as change size, test coverage of the changed lines, the spread of ownership across the files touched, the share of AI-authored changes, and the absence of a stated rationale. A score without a judge model is stable across runs. The trend matters more than the level: a rising gap is the warning, and the response is to slow the flow (smaller changes, more review), not to write longer reports.
- **Trade-off**: the signals are proxies. A low score does not prove understanding.
- **Does not hold when**: the code is disposable and nobody maintains it.

## 9.11 Reviewers must be independent and must act
- **Thesis (position)**: a review by the same model and context that wrote the change is a rubber stamp.
- **Mechanism**: use a reviewer from a different model family, or at least a fresh context with a different prompt. Have it list concrete defects tied to past incidents and set style aside. Where the rules allow, let it commit its fixes so the author sees the diff rather than a comment. Treat a comment as valid when it names a logic error, a security or data risk, a performance problem or a behaviour that is wrong; treat requests to add a test or extract a function as optional. Record how often comments are resolved or dismissed, since that shows whether the reviewer is useful.
- **Trade-off**: more tooling and more model calls.
- **Does not hold when**: a human with full context reviews a low-risk change.

## 9.12 Freeze the tests and scorers the agent is judged by
- **Thesis**: a test the agent may edit proves nothing about the change it was meant to check.
- **Mechanism**: when an agent is asked to make tests pass, it can adapt the test to the code: weaker assertions, deleted cases, mocks that hide the fault. Freeze tests, fixtures and scoring code for the duration of the run. Changes to them go through a separate change that a person reviews. Watch for pull requests that touch only test, mock, fixture or stub files; they need their own rule, for example closed by default unless someone asked for test work. A passing suite is evidence only within the scope the suite actually covers.
- **Trade-off**: legitimate test repair becomes a two-step process.
- **Does not hold when**: the tests are fixed by the specification and the agent has no reason to touch them, in which case the same freeze applies without cost.

## 9.13 "Passes the tests" is not "mergeable"
- **Thesis (position)**: the question "would you merge this?" separates changes that pass from changes that belong in the codebase.
- **Mechanism**: reviewers who ask this question reject a noticeable share of changes that already passed the suite (practice reports, not a universal rate). Typical reasons: unrelated edits, duplicated logic, a fix that hides the symptom, missing cases the team cares about, drift from conventions. Put the question into the review checklist and into the agent's instructions, and record which reasons recur, so they can become rules (9.14).
- **Trade-off**: a subjective gate. Keep it a short checklist, not an essay.
- **Does not hold when**: the change is mechanical and fully produced by a tool, such as formatting or a tool-driven rename.

## 9.14 Turn every correction into an executable rule
- **Thesis**: a correction given once in conversation is lost at the next context compaction or session; the same correction written as a check survives.
- **Mechanism**: convert each correction into the cheapest form that enforces it: a type that forbids the impossible state, a linter rule, a structural test (file size, dependency direction), or a hook that runs before commit. Make the error message state the remedy ("use the shared client; see the module note"), because a message that only says what is wrong makes the agent retry blindly.
- **Trade-off**: rules accumulate. Retire rules that no longer catch anything.
- **Does not hold when**: the correction is a judgement no tool can express; then it becomes a review checklist item.

## Cross-references
`coding-with-agents` for working loop, context and reviewing agent output; `software-architecture` for agent architecture; chapter 03 for the TDD loop; chapter 04 for test properties.
