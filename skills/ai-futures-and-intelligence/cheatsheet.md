# AI Futures and Intelligence: Cheatsheet

Figures are dated snapshots (2020-2026); re-check. "(position)" = judgment, not fact. Chapter references in brackets.

## Rival Definitions of Intelligence [ch01]
| Definition | Measure | Main objection |
|---|---|---|
| Efficiency of turning experience into new skill (position) | Skill per unit of new experience, given prior knowledge | Hard to compute; priors chosen by the tester |
| Specialised adaptations of an organism (position) | Task suite in an environment | May understate broad problem-solving |
| Collective: humans, markets, machines (position) | System outcomes and incentives | Understates single-system integration |
| Task skill | Exam or benchmark score | Preparation can buy it |

## Two Kinds of Abstraction [ch02]
| | Geometric (type 1) | Structural (type 2) |
|---|---|---|
| Compares by | Distance, templates | Exact structure, sub-graphs |
| Good at | Perception, intuition, pattern completion | Rules, proofs, exact procedures |
| Needs | Dense samples on a manifold | Combinatorial search or symbols |
| Typical system | Deep network | Program synthesis, symbolic reasoner |
| Real thinking | Both, stacked | |

## Evidence That Separates Rival Readings [ch02, ch10]
| Reading | Predicts | Test |
|---|---|---|
| Memorised templates | Collapse on fresh variants, renaming | Templated variants |
| Interpolation | Fails far outside training range | Extrapolation test |
| Learned rule (intension) | Transfers when a parameter changes | Parameter-change test |
| Real reasoning with verifier | Verified accuracy scales with search | Verifier test |

## Positions on Statistical Limits [ch03]
| Position | For | Against | Falsifier |
|---|---|---|---|
| Models are interpolative databases of functions | Style transfer, template failures | Retrieval vs reasoning blur at scale | Discrete algorithm learned and applied off-range |
| Scaling measures memory | Novelty-resistant tests flat in compute | Capability rises with scale and search | Novelty-resistant benchmark scaling with compute alone |
| Must derive, cannot learn | Complexity bounds not in samples | Derivations are in the data; search works | Verified novel proofs unexplained by seen lemmas |
| Hybrid is needed | Efficiency, explainability | Interface cost, brittleness of hand symbols | Pure learner matches hybrids |
| World model plus planning | Differentiable planning | Not shown at scale | Planner without state model reaches long horizon |

## Understanding and Minds [ch04]
| Question | Test type | Reply to expect |
|---|---|---|
| Does it understand? | Functional vs experiential | Systems reply, grounding reply |
| Is it conscious? | Architecture, substrate | Counterfactual structure objection |
| How to describe it? | Predictive accuracy of the description | Simulator vs single-character |

## Creativity [ch05]
| Approach | Strength | Risk |
|---|---|---|
| Objective optimisation | Scales; solves well-shaped problems | Deceptive paths; entangled representations |
| Novelty search, quality-diversity | Stepping stones, diverse niches | Needs a notion of interesting |
| Human-selected open-ended search | Good internal structure | Human taste is unmodelled |

## Bottlenecks (snapshot 2026) [ch06]
| Constraint | Lead time | Note |
|---|---|---|
| Data centre construction | Under a year (some about 8 months) | Short lead |
| Power purchase, turbines | Years ahead deposits | Contested "binding" claim |
| Chip fab | 2-3 years | Long lead |
| Lithography tools | Long | Late adoption cost a rival years |
| High-bandwidth memory | Capacity and wafer-area limited | About 4x wafer area per bit (position) |
| Packaging | Short | Earlier bottleneck |

## Inference Cost Model [ch07]
| Term | Meaning |
|---|---|
| Compute time | batch x active parameters / chip throughput |
| Memory time | (total weights + batch x context x bytes per token) / bandwidth |
| Step time | At least the larger of the two |
| Batching | Shares weight fetch; large effect on cost |
| Capacity per chip | (total weights + batch x context x bytes) / (expert width x pipeline depth) |

## Timeline Inputs [ch08]
| Input | Position and its counter |
|---|---|
| Compute needed | Wide prior across orders of magnitude / may not be the binding input |
| Growth loop | AI reopens people-ideas-resources loop / complementary inputs bind |
| Automation | Partial automation at scale can accelerate / slowest component governs |
| Physical build-out | Robot doubling in months / supply chains, energy |
| Long timelines (general knowledge) | Missing capabilities, diffusion lags / may arrive sooner |

## Analogy Fit [ch09]
| Case | Used for | Breaks when |
|---|---|---|
| Collective brain | Capability depends on connectedness | AI distils culture directly |
| Plague and climate shock | Tail events reshape outcomes | Risk is endogenous |
| Wartime weapon program | Race acceleration, dual use | AI is diffuse and commercial |
| Unstable succession | Governance of concentrated power | Mechanism differs |

## Claim Evaluation (six fields) [ch10]
Statement, definition, evidence, counter, falsifier, date. Missing falsifier: treat as a slogan.

## Common Traps
| Trap | Fix |
|---|---|
| Skill taken for generalisation | Ask how much was pre-loaded |
| Fluency taken for soundness | Add a verifier or test |
| Same output taken for same inside | Inspect representation |
| "Share" read as "size" | State which |
| Undated number | Date it or drop it |
| Analogy used as proof | List relations and breakpoints |

## Work, Learning, Information, Rights [ch11]
| Question | Position and evidence type | Falsifier |
|---|---|---|
| Will models replace jobs? | Tasks, not occupations; usage data from one product; gap between feasible and used | Multi-year hiring and wage data in exposed jobs |
| Does AI harm learning? | Free answers help practice, may hurt unaided exams; guided tutors avoid harm (one study) | Long-term unaided assessments |
| Chatbot as main source | More trust, less checking | Measured checking behaviour |
| Who sets limits on use? | Supplier terms vs state authority (open) | Durable legal framework |
| Age check | Mechanism can limit data; harm reduction unproven | Exposure and leakage measured |
| Training data and likeness | Compensation by output resemblance proposed; attribution unsolved | Working licensing market |
