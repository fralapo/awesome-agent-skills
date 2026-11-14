# Chapter 1: What Intelligence Is and How It Is Measured

## Core Idea
In this model "intelligence" is not one agreed quantity. Several camps define it differently, and the definition decides which benchmark counts as evidence. Every claim about "more intelligent" systems should first be translated into: *intelligent at what, relative to which prior knowledge, measured how*. This chapter lays out the rival definitions as positions, each with arguments for, arguments against and what would show it false.

## 1.1 Intelligence as efficient adaptation to novelty (position)
- **Position**: intelligence is the ability to handle situations not seen before by building a model of them on the fly; it is the rate at which experience is converted into new skill, not skill itself.
- **Mechanism**: separate *skill* (performance on a task, which can be bought with prior knowledge or training data) from *generalisation power* (how much skill you obtain per unit of new experience, given what you already knew). A formal version normalises task skill by task difficulty, prior knowledge and experience, giving an information-conversion ratio. A system that has memorised the answer to a task has skill but shows no intelligence on it.
- **For**: it explains why a chess engine, a lookup table and an exam-passing model can all score high without anyone calling them general; it makes "how much did the engineer pre-load?" a first-class question.
- **Against**: the ratio is hard to compute in practice (what counts as "prior"?); it can be gamed by tasks built from human-centric priors, so the result depends on the chosen priors; critics say it defines intelligence so that current models fail by construction.
- **Falsified by**: a system with no task-specific preparation, tested on tasks its builders did not foresee, matching human sample efficiency and still failing everyday tasks that humans handle with the same experience.
- **Does not hold when**: the goal is economic usefulness; a system with zero generalisation power but enormous coverage can still be worth deploying (see ch06 and ch08).

## 1.2 Intelligence is specialised and anthropocentric (position)
- **Position**: intelligence is a collection of adaptations to a particular kind of organism in a particular environment, not an open-ended, domain-independent quantity you can have "more and more of forever".
- **For**: cognitive scientists and animal-intelligence researchers typically describe intelligence this way; human reasoning is tied to social standing, embodiment and a limited energy budget; "pure intelligence" has never been separated from these in any known system.
- **Against**: the opposing view holds that general problem-solving is a real, separable capacity (it is why a person can learn chess, law and carpentry); "adaptations" does not rule out a very broad adaptation.
- **Falsified by**: demonstrating a system that is both clearly superhuman across unrelated domains and shows none of the biases, social dependence or embodiment of known intelligences. In this model this has not been shown (as of 2020-2025); absence of evidence is not proof of impossibility.
- **Practical use**: when a claim says "a smarter-than-human system would also be X", ask whether X depends on the assumption that intelligence is a single scalar.

## 1.3 The "intelligence always wins" assumption (position)
- **Thesis**: much risk talk assumes a purified intelligence that would be able to do everything a human can, plus more. Critics call this anthropomorphic projection.
- **Argument against**: even among humans, numbers, resources and brute force often beat intelligence; a system with a goal but no insight into why the goal was set ("fix climate change" solved by removing the people) would be, in this model, a *dumb superintelligence*, a contradiction: real intelligence includes insight into the goals and likely effects of its actions.
- **Counter-argument**: capability and goal-understanding are separable in practice; optimisers exploit the gap between the literal objective and the intended one (see `ai-ml-concepts` ch11). So "it would understand us" is not a safeguard unless understanding is part of what is optimised.
- **Falsified by**: a deployed system that is general across domains yet systematically mis-reads human intent in a way that cannot be traced to its training signal.

## 1.4 Intelligence as collective, not artificial (position)
- **Position**: the useful unit of intelligence is the system of many humans, markets and machines, not an individual "mind in a box". Machine-learning style prediction combined with economic mechanisms (prices, incentives, data markets) is the productive direction.
- **Mechanism**: social knowledge is ephemeral and local (what is on sale, at what price, who wants what right now); you cannot collect enough data to cover all future choices even over ten seconds, so a system should stay humble and route decisions through humans as producers and consumers.
- **For**: it matches how recommendation, logistics and finance systems actually work; it frames equilibria and incentives, which optimisation-only machine learning ignores.
- **Against**: it understates the possibility that a single system might do the integrating work; markets also fail, and a toy model of a data market is not evidence about the real one.
- **Falsified by**: a single system that, without human participants and without market-like feedback, outperforms the collective on tasks that depend on local, fast-changing knowledge.

## 1.5 Benchmarks inherit human assumptions
- **Thesis**: an exam is a valid test of a human because it is a proxy for abilities that, in humans, travel together. When a machine passes it, the proxy relationship may not hold.
- **Mechanism**: chess was once thought to require general intelligence; brute-force search conquered it with no generalisation. Passing a professional exam by a model shows skill at that test format, possibly through memorised templates, not the generalisation that the same score implies in a person. Benchmarks driven by memory improve with more parameters, data and compute, which are proxies for memory.
- **Trade-off**: benchmarks that cannot be prepared for (novel, few-example tasks) are harder to build, because designing a truly novel and interesting test is nearly as hard as the capability under test.
- **Does not hold when**: the test is the job itself (a production task with real inputs); then skill, not generalisation, is exactly what you need.

## 1.6 A benchmark built to resist memorisation (mechanism + snapshot)
- **Mechanism**: a few-example abstract-reasoning benchmark gives each task a handful of coloured-grid input/output pairs; every task is different from all others and from anything online, and requires a small, fresh program. Humans solve most tasks easily; the design goal is that preparation cannot substitute for adaptation.
- **Snapshot (mid-2024, approximate dates; re-check)**: general language models scored roughly 5-9%; the best reported entry was about 21%; brute-force program search at scale was estimated to reach at least about 50% from an ensemble of earlier-competition entries; humans scored above 90% (two testers about 97-98% on a private set, together 100%).
- **Position on the non-zero scores**: a score above zero may come from a kernel of real reasoning (which would scale) or from memorised patterns (which would not and would turn progress into endless special-casing, "whack-a-mole"). The two readings predict different things: reasoning scales smoothly with fresh variants; memorisation collapses on templated variants. Test with variants before believing either.
- **Does not hold when**: later systems changed the picture (general knowledge: test-time search and reasoning-trained models moved scores a lot after this snapshot); re-measure before quoting.

## 1.7 Chess-style moving goalposts and the opposite error
- **Thesis**: when a task becomes easy for machines, people redefine intelligence to exclude it. The counter-error is declaring generality whenever a task falls.
- **Move**: fix your criterion *before* looking at the result; state what pattern of performance would count as failure.
- **Does not hold when**: the criterion was set long ago and is plainly outdated.

## Checklist for this chapter
1. Which definition of intelligence does the claim use (adaptation, specialised adaptation, collective, task-skill)?
2. Could the test be passed by preparation alone?
3. Does the score scale with compute spent on memory (parameters, data) or with compute spent on search at test time?
4. What result would change your mind, written down in advance?
