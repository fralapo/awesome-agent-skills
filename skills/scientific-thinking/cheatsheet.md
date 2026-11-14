# Scientific Thinking: Cheatsheet

Figures are rules of thumb or values from the chapters; many come from single or contested studies. "Position" = practitioner judgment, not evidence. Chapter references in brackets.

## Where to Start
| Situation | First move |
|---|---|
| A claim sounds too good or too surprising | State it with a number; ask what would falsify it; wait for independent replication [ch01, ch06] |
| "It improved after we acted" | Is it an extreme case? Regression to the mean; need a comparison group [ch02] |
| Test result or alarm | Base rate first; count per 1,000 people [ch03] |
| Study with p just under 0.05 | How many outcomes/analyses were possible? Pre-registered? Effect size? [ch02, ch06] |
| Confident expert | Valid environment? Feedback? Scored track record? [ch05] |
| Headline about a breakthrough | Check data in the paper, size of jump, other labs [ch06] |
| Group arguing with identity stakes | Concrete local policy, not labels; do not assume more data persuades [ch04] |
| Forecast far ahead of a chaotic system | Ranges and ensembles; compare with the historical average [ch07] |
| Strategy in a repeated interaction | Nice, forgiving, retaliatory, clear; add a little generosity if there is noise [ch08] |
| Choosing a voting rule | Name which fairness property you give up [ch08] |
| "Mathematics proves it can't be done" | Exact theorem and conditions [ch09, ch12] |
| Using IQ, a style test, or a happiness result | Effect size, sample, causation, misuse history [ch11] |
| A result that "feels wrong" in a strange domain | In the trained range? Reason from definitions and a small count [ch13] |
| Infinity or geometry paradox | Which finite assumption fails; consistent vs realisable vs useful [ch14] |
| Collective behaviour from simple parts | Local rule plus feedback; explain at the right layer [ch15] |
| Far scenario (simulation, filter, collapse, automation) | List assumptions, mark testable, state conditionally, use base rates [ch16] |
| Everyday physics "paradox" | Find the conflated quantity; check energy and a limiting case [ch17] |
| "Worked in mice" | Does the model reproduce the mechanism? Human data? [ch06] |

## Statistics in One Table
| Idea | One line | Number/example |
|---|---|---|
| Regression to the mean | Extremes drift back; no cause needed | Top 10 scorers on a luck test fall to 50 |
| p-value | P(data this extreme given no effect), not P(hypothesis) | 0.05 is a convention |
| Multiple comparisons | More tries, more false positives | Four flexible tactics together push false positives above 60% |
| Published false share | Depends on prior, power, bias | 1,000 hypotheses, 10% true, 80% power: 80 true vs 45 false positives |
| Correlation squared | Variance explained | r = 0.2 is about 4% |
| Proportions | Compare ratios within rows | Largest cell misleads |

## Bayes in One Table (disease 0.1%, sensitivity 99%, false-positive 1%)
| Step | Count per 1,000 |
|---|---|
| Truly ill | 1 (flagged) |
| Healthy flagged | about 10 |
| Probability ill given positive | about 1 in 11 (9%) |
| After a second independent positive | about 91% |

## Calibration and Expertise
| Fact | Value |
|---|---|
| 90% certain, actually right | about 75% (classic quizzes) |
| Economists: stated vs actual confidence | about 53% vs 23% |
| Four conditions for real expertise | valid environment; many repetitions; timely feedback; deliberate practice |
| Active funds failing to beat the market | about 80% over 10 years, up to 90% over longer periods |
| Simple formula vs interviewers (one study) | formula beat 11 of 14 |

## Chaos and Prediction
| Item | Value |
|---|---|
| Logistic map | stable 1 to 3; period doubling after 3; chaos near 3.57; window of 3 near 3.83 |
| Doubling ratio | about 4.669 (universal) |
| Weather | by about day 8 worse than climatology (as stated); use ensembles |
| Solar system | chaotic on a time scale of about 4 million years |

## Games and Voting
| Item | Value |
|---|---|
| Dilemma payoffs | mutual cooperation 3 each; defect vs cooperate 5 and 0; mutual defection 1 each |
| Winning traits | nice, forgiving, retaliatory, clear |
| Noise fix | about 10% generosity |
| Ranked-ballot impossibility | unanimity, no dictator, unrestricted domain, transitivity, independence of irrelevant alternatives |
| Escapes | rated/approval ballots; single-peaked preferences (median voter) |

## Intelligence and Learning (contested)
| Item | Value |
|---|---|
| IQ scale | mean 100, SD 15; 68% in 85 to 115 |
| Associations | brain size about 0.33; school results 0.5 to 0.8; income about 0.2 |
| Heritability range | about 40 to 70% (within-population estimate) |
| Flynn effect | about 2 to 3 points per decade |
| Learning-style matching | no credible support; multimodal and active learning help everyone |

## Infinity and Strange Objects [ch14]
| Item | Value |
|---|---|
| Countable infinities | counting numbers, evens, odds, fractions all pair one to one; infinity plus one is the same size |
| Bigger infinity | power set of any set (2^n members for n members); diagonal construction |
| Cardinal vs ordinal | size vs order position; a later ordinal is not a larger amount |
| Supertask | converging (halving distances) fine; oscillating (lamp) has no defined end state |
| Equal cross-sections | equal volumes; napkin rings of equal height have equal volume |
| Least time | cycloid, not the straight line |
| Zero area | can still have positive dimension |

## Emergence and Heavy Tails [ch15]
| Item | Value |
|---|---|
| Zipf's law | frequency proportional to 1/rank; straight line on log-log |
| 80/20 | rule of thumb (position), not a law |
| Local rule + feedback | ant job switching by encounter counts; no planner |
| Evolution | random variation, non-random selection |
| Entropy | total never decreases; life exports heat and waste |

## Far Scenarios [ch16]
| Item | Value |
|---|---|
| Simulation argument | five assumptions; premise on motives is weakest |
| Great Filter | behind us (lucky) or ahead (bad); finding simple life elsewhere is bad news in this model |
| Collapse | common; worst recorded global drop about a tenth of population, recovered in about two centuries |
| Automation | test whether the job-creating mechanism still works at scale |
| Time | moving present, frozen block, growing block: all interpretations |

## Everyday Physics [ch17]
| Item | Value |
|---|---|
| Hydrostatic | pressure depends on height above, not volume |
| Siphon/straw | about 10.3 m ideal; about 10.07 m with water vapour pressure at room temperature |
| Series vs parallel springs | cutting a joining rope can raise the load |
| Exponential decay | doubling the start adds one half-life, not twice the time |
| Equator | apparent weight about half a percent lower |
| Debug rule | conflated quantity, limiting case, energy, control, measured gap |

## Red Flags in Science News
Single group; no replication; surprising; jump far above previous record; data inside the paper contradict headline; press release stronger than abstract; conclusion flatters a group.

## Do Not
- Do not read "99% accurate" as "99% likely".
- Do not credit an intervention applied to an extreme case without a control.
- Do not trust a feeling of obviousness for something repeated often.
- Do not quote the "Mount Stupid" curve as data.
- Do not treat "democracy is impossible" or "math is broken" headlines as literal.
- Do not assume one best strategy in a game; check the opponents.
- Do not read "in mice" as "in people".
- Do not drop the conditions of a far-scenario argument in the summary.
- Do not treat "80/20" as an exact law or a shared mechanism.
- Do not answer "after infinitely many steps" without a limit rule.
