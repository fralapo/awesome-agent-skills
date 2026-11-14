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

## Cross-references
`coding-with-agents` for working loop, context and reviewing agent output; `software-architecture` for agent architecture; chapter 03 for the TDD loop; chapter 04 for test properties.
