---
name: scientific-thinking
description: "Reasoning about evidence and uncertainty: falsifiability, phantom entities, how well a theory is tested; statistics (regression to the mean, p-values, multiple comparisons) and Bayes; cognitive ease, motivated reasoning, post-truth; calibration and real expertise; why research and headlines fail (replication, p-hacking, animal-to-human translation); prediction, chaos, randomness, markets; game theory and voting; limits of mathematics (undecidability, P versus NP, computer-assisted proof); infinity and paradoxes; emergence and complex systems; intuition, illusions, categories; far scenarios (simulation, Great Filter, collapse, automation) with caveats; everyday physics paradoxes; discoveries; wellbeing, IQ, learning; a claim checklist. Use when the user must judge a study, statistic, forecast or headline, reason under uncertainty, or explain a counterintuitive result. Hands off theoretical physics to physics-and-math-ideas."
allowed-tools:
  - Read
  - Grep
argument-hint: [claim, study, statistic, forecast, or chapter number]
---

# Scientific Thinking
**Chapters**: 17 | **Generated**: 2026-11-14

## Role and Boundaries

This skill **decides how to evaluate and reason about evidence**: whether a result is likely to be true, whether a number means what it seems to mean, how much confidence a forecast or expert deserves, which mistakes a given kind of situation invites, and how to design a test that could prove you wrong. It gives mechanisms, decision tables and a checklist; the user owns the domain knowledge and the decision.

| This skill decides | This skill hands off |
|---|---|
| Is this claim supported; what would falsify it; base-rate and Bayes checks; statistical red flags; calibration; expert validity; replication risk; headline skepticism; game-theoretic and voting structure; limits of proof and prediction | Running real statistical analysis on a dataset, choosing and coding tests -> `data:statistical-analysis`, `data:validate-data` |
| Systematic reading and scoring of a body of literature | `ecc:scientific-thinking-literature-review`, `ecc:scientific-thinking-scholar-evaluation` |
| Reasoning about irrationality, motives and relationships | `depth-psychology` |
| Persuasion, framing, story-led communication | `public-speaking-persuasion`, `marketing-mba` |
| UX research design and sample sizes for product work | `ux-ui-expert` |
| Architecture-level resilience, incident reasoning | `software-architecture` |
| Theoretical physics and advanced mathematics themselves (Standard Model, relativity, quantum computing, number theory) | `physics-and-math-ideas` |

**Stay in lane.** The chapters hold practitioner-level theory not a literature review. Figures are dated and context-bound, and several rest on studies that have been challenged. Where a finding is contested in the literature the text says "contested" and gives the reason. Where a point is unclear the text says "unclear".

## Facts vs Positions

- **Mechanism / fact**: how repetition creates a feeling of truth, why selecting extremes guarantees regression, why a rare-disease test yields mostly false positives, why a ranked voting rule cannot satisfy five reasonable conditions at once, why a halting-style question cannot be decided in general.
- **Position**: written as "In this model..." or "(position)": for example "ask forecasters for probabilities and keep score", "treat surprising unreplicated results as probably wrong", "prefer a simple repeatable formula to unaided expert judgment when the environment is noisy", "give up expecting a single best strategy".
- Every concept in the chapters has fields **Thesis**, **Mechanism**, **Trade-off**, **Does not hold when**. Read the last one before applying the rule.

## How to Use This Skill

Diagnose before prescribing: ask what the claim is, who made it and why, what the data are (sample, comparison group, measurement), whether the situation gives fast and valid feedback, and what would change the person's mind.

| Task | Start with | Then |
|---|---|---|
| "Is this claim / study / headline believable?" | [ch12](chapters/ch12-evaluating-a-claim-checklist.md) | ch06, ch02 |
| What makes a claim scientific; falsifiability; consensus vs speculation | [ch01](chapters/ch01-method-falsifiability-and-evidence.md) | ch06, ch09 |
| Odd statistic, "it improved after we intervened", p-value, correlation | [ch02](chapters/ch02-statistics-and-inference.md) | ch03, ch06 |
| Test or screening result, updating beliefs, risk appetite | [ch03](chapters/ch03-probability-bayes-and-risk.md) | ch02, ch05 |
| Why people believe false things, polarisation, repetition, stories | [ch04](chapters/ch04-cognition-belief-and-post-truth.md) | ch05, ch12 |
| Overconfidence, when to trust an expert, forecasting | [ch05](chapters/ch05-confidence-calibration-and-expertise.md) | ch07, ch03 |
| Replication crisis, p-hacking, science news, forensic evidence in court | [ch06](chapters/ch06-how-research-and-reporting-fail.md) | ch02, ch12 |
| Forecasting, chaos, markets, randomness | [ch07](chapters/ch07-prediction-chaos-and-markets.md) | ch05, ch03 |
| Cooperation, strategy, voting systems, paradoxes of rational choice | [ch08](chapters/ch08-games-and-collective-choice.md) | ch03 |
| What proof can and cannot do; conjectures; Markov chains and simulation | [ch09](chapters/ch09-mathematics-power-and-limits.md) | ch01, ch07 |
| How discoveries happen, credit, prizes, dual use | [ch10](chapters/ch10-discoveries-credit-and-prizes.md) | ch01, ch09 |
| Happiness, income, IQ, learning styles, how learning works | [ch11](chapters/ch11-wellbeing-intelligence-and-learning.md) | ch02, ch04 |
| Why intuition fails, time perception, imagery differences, colour, what counts as an object | [ch13](chapters/ch13-intuition-illusions-and-categories.md) | ch04, ch14 |
| Infinity, supertasks, paradoxes of geometry, dimension, fractals, fluid equations | [ch14](chapters/ch14-infinity-paradox-and-strange-objects.md) | ch09, ch13 |
| Emergence, ant colonies, free will by layers, life and entropy, evolution, intelligence, power laws, universality | [ch15](chapters/ch15-emergence-and-complex-systems.md) | ch07, ch13 |
| Simulation argument, Great Filter, far future, collapse, automation, ageing, time as a block | [ch16](chapters/ch16-reasoning-about-far-scenarios.md) | ch03, ch12 |
| Everyday physics paradoxes: pressure, weight, springs, spools, siphons, resonance, decay | [ch17](chapters/ch17-everyday-phenomena-and-basic-physics.md) | ch01, ch13 |
| Quick lookup | [cheatsheet.md](cheatsheet.md), [patterns.md](patterns.md), [glossary.md](glossary.md) | |

## The Core Principles (recurrence order)

1. **Try to falsify, not to confirm.** A claim that forbids nothing explains nothing; look for the observation that would embarrass it.
2. **Feeling true is not evidence.** Familiarity, fluency, vividness and group identity all produce certainty without support.
3. **Start from the base rate.** The prior is the hardest and most neglected term; a precise test on a rare event still gives mostly false alarms.
4. **Extremes regress.** Selecting the best or worst and then observing again will show "change" with no cause; use a comparison group.
5. **Many chances make false positives.** Every extra measure, subgroup, stopping rule or analytic choice raises the odds of a spurious finding.
6. **Surprising results are the least likely to be true and the most likely to be reported.** Wait for independent replication.
7. **Confidence is not accuracy.** Calibrate by keeping score; confident people are rewarded whether or not they are right.
8. **Expertise needs a learnable world.** Valid regularities, many repetitions, timely feedback and deliberate practice; otherwise "experts" are story-tellers.
9. **Deterministic is not predictable.** Sensitive dependence limits the horizon; predict distributions and structure, not trajectories.
10. **Incentives shape output.** Funding, publication, press and clicks select for bold claims; read the chain, not just the claim.
11. **Rational individuals can make irrational groups, and the reverse.** Check the level at which a strategy or rule is being judged.
12. **Proof has limits; ignorance can be productive.** Some truths are unprovable, and not knowing a problem is "impossible" sometimes helps.
13. **Intuition has a trained range.** Outside everyday sizes, durations and minds, name the assumption that fails and reason from definitions and counts.
14. **Find the conflated quantity.** Paradoxes of everyday physics usually merge two terms (force and pressure, series and parallel); check energy and limiting cases.
15. **Conclusions of far scenarios are conditional.** Write the assumptions, mark which are testable, and keep the conditions in the summary.
16. **Whole-level properties are real.** Emergent behaviour comes from local rules and feedback; explain it at the right layer.

## Chapter Index

1. [Method, falsifiability and evidence](chapters/ch01-method-falsifiability-and-evidence.md)
2. [Statistics and inference](chapters/ch02-statistics-and-inference.md)
3. [Probability, Bayes and risk](chapters/ch03-probability-bayes-and-risk.md)
4. [Cognition, belief and post-truth](chapters/ch04-cognition-belief-and-post-truth.md)
5. [Confidence, calibration and expertise](chapters/ch05-confidence-calibration-and-expertise.md)
6. [How research and reporting fail](chapters/ch06-how-research-and-reporting-fail.md)
7. [Prediction, chaos and markets](chapters/ch07-prediction-chaos-and-markets.md)
8. [Games and collective choice](chapters/ch08-games-and-collective-choice.md)
9. [Mathematics: power and limits](chapters/ch09-mathematics-power-and-limits.md)
10. [Discoveries, credit and prizes](chapters/ch10-discoveries-credit-and-prizes.md)
11. [Wellbeing, intelligence and learning](chapters/ch11-wellbeing-intelligence-and-learning.md)
12. [Evaluating a claim: checklist and worked cases](chapters/ch12-evaluating-a-claim-checklist.md)
13. [Intuition, illusions and the categories we impose](chapters/ch13-intuition-illusions-and-categories.md)
14. [Infinity, paradox and strange mathematical objects](chapters/ch14-infinity-paradox-and-strange-objects.md)
15. [Emergence and complex systems](chapters/ch15-emergence-and-complex-systems.md)
16. [Reasoning about far-off scenarios, with caveats](chapters/ch16-reasoning-about-far-scenarios.md)
17. [Explaining everyday phenomena with basic physics](chapters/ch17-everyday-phenomena-and-basic-physics.md)

## Topic Index

- **80/20 rule, Zipf's law, heavy tails** -> ch15
- **Aphantasia, imagery, colour perception** -> ch13
- **Automation, collapse, ageing, far-future arguments** -> ch16
- **Brachistochrone, supertasks, Banach-Tarski, napkin ring** -> ch14
- **Busy beaver, P versus NP, four-colour proof, cryptography worlds** -> ch09
- **Eclipses, randomness of coins** -> ch07
- **Emergence, ant colonies, entropy and life, evolution** -> ch15
- **Great Filter, simulation argument, block universe, information paradox** -> ch16
- **Hydrostatic paradox, spool, lever, siphon, spring, resonance** -> ch17
- **Phantom entities, how well tested** -> ch01
- **Power pose, animal models ("in mice")** -> ch06
- **Time perception, periodisation, objects and boundaries** -> ch13

- **Adaptive strategies, tournaments** -> ch08
- **Approval voting, ranked choice, spoiler effect** -> ch08
- **Base rate, prior, posterior** -> ch03
- **Bounded gaps, conjectures, heuristics vs proof** -> ch09
- **Calibration, overconfidence, Dunning-Kruger effect** -> ch05
- **Chaos, logistic map, ensemble forecast** -> ch07
- **Climate misconceptions as a worked case** -> ch12
- **Cognitive ease, illusion of truth** -> ch04
- **Contextual bias, forensic techniques** -> ch06
- **Efficient markets, random walk, hedging** -> ch07
- **Flynn effect, IQ, heritability** -> ch11
- **Incompleteness, halting problem** -> ch09
- **Learning styles, multimedia effect** -> ch11
- **Loss aversion, repeated bets** -> ch03
- **Markov chain, Monte Carlo** -> ch09
- **Motivated numeracy, polarisation** -> ch04
- **Newcomb's problem, pre-commitment** -> ch08
- **p-hacking, replication, registered reports** -> ch06
- **Regression to the mean** -> ch02
- **Science headlines, hype** -> ch06
- **Story vs statistics, anecdotes** -> ch04
- **Wellbeing studies, income and happiness** -> ch11

## Related Skills

- `data:statistical-analysis`, `data:validate-data`: running and checking real analyses.
- `ecc:scientific-thinking-literature-review`, `ecc:scientific-thinking-scholar-evaluation`: systematic reading and scoring of papers.
- `depth-psychology`: motives, relationships and self-deception beyond cognitive bias.
- `public-speaking-persuasion`: how stories and framing move audiences (the other side of ch04).
- `software-architecture`: failure analysis and incident reasoning in systems.
- `physics-and-math-ideas`: theoretical physics and advanced mathematics themselves (this skill covers the reasoning around them).

## Scope & Limits

Practical theory about the scientific method, statistics, probability, cognitive science, research practice, forecasting, game theory, voting, the foundations and curiosities of mathematics (infinity, paradox, complexity), emergence, far-scenario reasoning, everyday physics explanations, the history of discoveries, and studies of wellbeing, intelligence and learning. Not covered: formal statistical derivations, domain-specific methods (clinical trial regulation, epidemiology), laboratory technique, and legal doctrine. Many findings are single studies or contested syntheses; the skill gives no medical, legal, financial or policy guarantee.
