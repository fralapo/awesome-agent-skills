# AI and Machine Learning Concepts: Cheatsheet

Figures are dated reported values or rules of thumb; they are dated snapshots, so re-test. "Position" = judgment, not fact. Chapter references in brackets.

## Where to Start
| Situation | First move |
|---|---|
| Someone asks "how does it learn?" | Cost function, gradient, step downhill; backprop is the efficient gradient [ch04] |
| "Why is the model confident and wrong?" | Narrow training world, no abstain incentive, plausible-text objective [ch05, ch10] |
| A score looks too good | Check setup, contamination, item errors, ceiling [ch09] |
| A headline claims a breakthrough | Nine questions: human-designed task? general or specialised? hardest failure? other metrics? [ch09] |
| Answer needs exact arithmetic or long procedure | Give a tool; do not trust unaided generation [ch08, ch10] |
| Which model for my task? | Test on your own items; domain post-training breaks rankings [ch09] |

## Maths in One Line Each
| Idea | Plain meaning | Chapter |
|---|---|---|
| Matrix | Machine that moves every vector; columns = where basis vectors land | ch01 |
| Dot product | Alignment score | ch01, ch07 |
| Eigenvector | Direction only stretched by the map | ch01 |
| Derivative | Output change per tiny input change | ch01 |
| Chain rule | Multiply sensitivities along a path; add parallel paths | ch01, ch04 |
| Gradient | Vector of all sensitivities; negative = downhill | ch01, ch04 |
| Bayes' rule | Posterior proportional to prior times likelihood | ch02 |
| Binomial | Count of successes in n independent trials | ch02 |
| Central limit theorem | Sums tend to Gaussian; error of mean ~ 1 over square root of n | ch02 |
| Convolution | Flip, slide, overlap-weight; adds random variables; blurs | ch02, ch06 |
| Information | Minus log2 p bits | ch03 |
| Entropy | Average information; lossless compression limit | ch03 |
| Cross-entropy | Average code length with the wrong model; training loss | ch03 |

## Training Signals and What They Teach
| Signal | Teaches | Typical failure |
|---|---|---|
| Next-token prediction | Language, facts, patterns | Plausible falsehood, patchy recall [ch08, ch10] |
| Human preference | Helpful style | Flattery, confident tone [ch08, ch10] |
| Outcome reward (verified answer) | Reach right answers | Lucky or gamed solutions [ch08, ch10] |
| Process reward (per step) | Good working | Costly labels, subjective steps [ch08] |
| Self-generated chains + checker | Scalable reasoning where checkable | Open-ended tasks without grader [ch08] |

## Regularisation and Generalisation
| Tool | Effect | Watch for |
|---|---|---|
| Held-out test | Honest score | Leakage via tuning [ch05] |
| L1 | Sparse weights | Too strong underfits [ch05] |
| L2 | Smaller weights | Same [ch05] |
| Early stopping, dropout, augmentation | Less memorisation | Tuning on test [ch05] |
| Pruning under accuracy budget | Smaller, faster | Rare behaviours lost [ch05] |

## Architecture Picks
| Data | Reach for | Why |
|---|---|---|
| Tables | Boosted trees | Strong, inspectable [ch04] |
| Images, local structure | Convolutions | Shared local detectors [ch06] |
| Compressed representation | Autoencoder | Bottleneck code [ch06] |
| Text, long-range relations | Transformer | Content-based routing [ch07] |
| Expensive physics | Learned surrogate | Fast inference, weaker guarantees [ch06, ch12] |

## Test-Time Levers
| Lever | Gain | Cost |
|---|---|---|
| Reason before answering | Better on multi-step tasks | Tokens, latency [ch08] |
| Sample many, majority vote | Higher accuracy | Linear in samples [ch08] |
| Rank samples with a step-level judge | Highest in the reported study | Needs a trained judge [ch08] |
| Tools / code | Exact results | Sandbox, latency [ch08] |
| Longer context | Domain material in prompt | Quadratic attention cost, recall limits [ch07] |

## Headline Checklist (ch09, 9.9)
1. Task human-written with known answers, or open research?
2. A lead over rivals, and have rivals reported?
3. Specialised system or general model?
4. Which hardest item failed?
5. Hallucination, refusal and honesty metrics moved the same way?
6. Released product or internal model?
7. Does the jump generalise to other tasks or only to this family?
8. Who announces and why now?
9. Base rate of such claims proving durable?

## Safety Reading Rules (ch11)
- Distinguish lab-constructed scenarios from observed deployments.
- Distinguish developer reports from independent replication.
- Alignment, monitoring, containment: three layers; each weakens differently.
- A reasoning trace is evidence, not a guarantee.

## Estimation Numbers Seen (as reported at the time; re-check)
| Item | Value | Chapter |
|---|---|---|
| Small digit-classifier parameters | ~13,000 | ch04 |
| Large language model of the earlier generation | ~175 billion parameters; ~2/3 in feed-forward blocks | ch07 |
| Rating with few reviews, fair estimate | Add one good, one bad review (rule of succession) | ch02 |
| Hamming block | 247 data + 9 redundancy bits in 256 | ch03 |
| Process-reward study (math subset) | ~42% base to ~78% (as reported) | ch08 |
| Monte Carlo error | falls like 1 over square root of samples | ch12 |
