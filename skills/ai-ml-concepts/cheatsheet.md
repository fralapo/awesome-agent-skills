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
| Training error rises as the network gets deeper | Add skip connections; it is degradation, not overfitting [ch06.8] |
| Test error falls again with a bigger model | Double descent: effective complexity, not parameter count [ch05.9] |
| Need many label-free features | Pick an objective plus an anti-collapse guard [ch14] |
| Agent works in demo, fails in use | Trace whole runs; bucket failures; test model, harness and task set [ch15.10] |
| A paper claims an advance | Ablations, samples, error bars, definitions [ch16] |

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

## Generative Families (ch13)
| Family | Trains | Sampling | Typical risk |
|---|---|---|---|
| Adversarial pair | Generator versus discriminator | One pass | Mode collapse, unstable training |
| Denoising diffusion | Predict noise at random step | Many small steps (about 25 with a deterministic sampler, thousands originally, as reported) | Cost per sample |
| Flow matching | Regress a velocity field to a per-sample path | Integrate an ODE; straight paths need few steps | Path choice, less mature tooling |
| Guidance | Classifier gradient on noisy images | Weight raises fidelity | Lower diversity |

## Label-Free Objectives and Their Guards (ch14)
| Objective | Guard against collapse | Cost |
|---|---|---|
| Skip-gram with negative sampling | Random negatives | Sampling noise |
| Masked bidirectional prediction | Reconstruction of real tokens | Needs fine-tuning |
| Image-text contrastive | In-batch negatives | Huge pair sets, prompt sensitivity |
| Moving-average teacher | Centering plus sharpening, stop-gradient | Needs augmentations |
| Joint-embedding predictive | Variance and decorrelation regularisers | Needs decoder only for inspection |

## Agent Building Blocks (ch15)
| Need | Mechanism | Watch for |
|---|---|---|
| Facts, past cases, rules | Semantic, episodic, procedural memory | Unreconciled conflicts [15.4] |
| Durable simple memory | Files plus a short skill document | No transactions [15.7] |
| Multi-document questions | Agentic search loop | Latency [15.8] |
| Intent across sessions | Constitution plus feature specs | Spec versioning [15.9] |
| Pre-production confidence | Simulation, red teaming, script validators | False confidence [15.12-15.14] |
| Crash recovery | Workflow plus retryable activities | Non-idempotent side effects [15.16] |

## Paper-Reading Checklist (ch16)
1. What would have shown the claim wrong? 2. Do ablations separate method from scale? 3. How was contamination checked? 4. Do samples agree with the rising score? 5. Error bars and scope? 6. Are key words defined? 7. Position paper or experiment? 8. Who ran the result?

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
| Pick the method by difficulty and budget | Compute-optimal allocation | Needs a difficulty estimate [ch08.14] |
| Share or compress keys and values | Smaller cache, faster decoding | Some head specialisation lost [ch07.13] |

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
| Group-relative RL | Advantage = (reward minus group mean) over group standard deviation; no value network | ch08 |
| Cache per token, three schemes | about 4 MB, about 500 KB, about 70 KB (one reported config) | ch07 |
| Scaling exponent, language | about 0.095 in magnitude; implied intrinsic dimension at least about 42 vs about 100 measured | ch08 |
| Plain 74-layer vs 8-layer net | worse; skip connections lifted one toy net from under 40% to about 73% | ch06 |
| Error ceiling | If a cause is 5% of errors, perfect fix takes 10% error to 9.5% | ch09 |
| Zero-shot image-text classifier | Competitive with a supervised ResNet-50 linear probe on 16 sets (as reported) | ch14 |
