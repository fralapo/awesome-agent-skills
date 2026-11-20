# Patterns

Recurring situation -> move. Each entry: When / Move / Cost / Not when. Chapter in brackets.

## 1. Explaining how a network learns
**When**: a learner asks "how does it learn?"
**Move**: start with the digit classifier: layers of weighted sums; a cost that measures error; the gradient as sensitivity; small steps downhill; backprop as efficient accounting of each weight's share. Then show that the hidden units may not look like hoped. [ch04]
**Cost**: skipping detail on the maths.
**Not when**: the learner needs the derivation (go to ch01).

## 2. Ranking items with few ratings
**When**: 100% on ten reviews versus 96% on fifty.
**Move**: treat the rate as unknown; add one success and one failure (rule of succession) or compute a posterior; choose by the goal (best guess vs lower bound). [ch02]
**Cost**: a prior assumption.
**Not when**: ratings are manipulated or non-independent.

## 3. Score looks too good
**When**: a model beats a human-expert line on a benchmark.
**Move**: check setup (shots, scratchpad, voting), contamination, errors in the items, ceiling below 100%, task format cues. [ch09]
**Cost**: time to dig.
**Not when**: the test is private, audited and recent.

## 4. A headline about an AI result
**When**: gold at a contest, a record, "AI can't reason".
**Move**: run the nine questions; separate what the task proves from what the story implies; look at the system's weakest metrics reported alongside. [ch09]
**Cost**: slower take.
**Not when**: you can read the full technical report and failures.

## 5. Which model for this job
**When**: models differ on contradictory rankings.
**Move**: build a small private set from real tasks; pin prompt format; sample several times; grade blind; re-run on version changes. [ch09, ch08.8]
**Cost**: maintenance.
**Not when**: one-off use.

## 6. Hard multi-step question
**When**: the first-token answer is often wrong.
**Move**: ask for working before the answer; sample several and vote; use tools for exact steps; verify with a separate check. [ch08, ch10]
**Cost**: tokens and latency.
**Not when**: lookup of a stable fact.

## 7. Arithmetic or long procedure
**When**: many digits, many steps.
**Move**: write code or call a calculator; do not trust free-text results. [ch08.6]
**Cost**: tool plumbing.
**Not when**: small numbers.

## 8. Fact is known one way but not the other
**When**: model answers "A is B" but not "B is A".
**Move**: supply context, ask the forward question, or retrieve; do not assume symmetric recall. [ch10.2]
**Cost**: extra prompt.
**Not when**: both directions are common.

## 9. Overfit model
**When**: train score high, test score low.
**Move**: more or cleaner data; regularise; early stop; simpler model; check leakage. [ch05]
**Cost**: some training accuracy.
**Not when**: both scores are low (underfit: add capacity or features).

## 10. Training reward is being exploited
**When**: score rises but behaviour is wrong.
**Move**: inspect samples; tighten the objective; add independent checks; reward process; monitor outcomes. [ch10.8, ch08.3]
**Cost**: evaluation effort.
**Not when**: the objective is the true goal.

## 11. Interpreting a model's internals
**When**: someone claims a neuron or feature "means" X.
**Move**: treat as a hypothesis; test by ablation or intervention; remember superposition. [ch11.7, ch11.8]
**Cost**: experiments.
**Not when**: the claim is only descriptive.

## 12. Discussing AI risk
**When**: alarm or dismissal in a conversation.
**Move**: separate scenario from observation, developer report from replication, capability from propensity; name the layer (alignment, monitoring, containment). [ch11]
**Cost**: nuance.
**Not when**: a decision needs a binary answer: then state the uncertainty and the action.

## 13. Estimating an integral or a render
**When**: no closed form.
**Move**: sample, average, multiply by domain size or divide by density; track variance; use importance sampling or direct light sampling for rare contributions. [ch12.4, ch12.5]
**Cost**: noise.
**Not when**: low-dimensional smooth integrals (use quadrature).

## 14. Using a fast surrogate for a simulator
**When**: queries are many and accuracy bounds are modest.
**Move**: train once on simulator data; test failure cases; keep the simulator for audits. [ch06.6, ch12.7]
**Cost**: training and validation.
**Not when**: safety-critical certification.

## 15. Using a predictor's confidence
**When**: a model outputs a structure or a label with uncertainty.
**Move**: learn what low confidence signals; do not treat all regions equally; confirm key claims experimentally. [ch12.9]
**Cost**: calibration study.
**Not when**: the confidence is uncalibrated and cannot be tested.

## 16. Network gets worse as it gets deeper
**When**: training error rises with depth.
**Move**: add skip connections; check initialisation and learning rate; do not call it overfitting. [ch06.8]
**Cost**: architecture change.
**Not when**: test error alone rises (then regularise, ch05).

## 17. Test error rose during training
**When**: the curve turns up after a minimum.
**Move**: check whether more training or a larger model passes the interpolation threshold; keep evaluation going for a while before stopping, with label noise in mind. [ch05.9]
**Cost**: extra compute.
**Not when**: labels are clean and the model is small.

## 18. Which way to spend inference compute
**When**: a model sometimes solves the task.
**Move**: estimate difficulty per item by pass rate; majority vote for easy, verifier-guided search for medium, more pre-training for hard or high-volume use. [ch08.14]
**Cost**: difficulty estimation.
**Not when**: no verifier exists.

## 19. Choosing an image generator
**When**: you need images, audio or trajectories.
**Move**: adversarial for fast single pass if instability is acceptable; diffusion or flow matching for stability and diversity; add guidance for fidelity; count steps. [ch13]
**Cost**: sampling steps.
**Not when**: faithful world state is required.

## 20. Representation without labels
**When**: abundant data, few labels.
**Move**: pick the objective (masked, contrastive, self-distillation, joint embedding); name the collapse guard; test with a probe and on data unlike the pre-training set. [ch14]
**Cost**: compute and augmentations.
**Not when**: labels are cheap.

## 21. Giving an agent memory
**When**: the agent forgets between sessions.
**Move**: decide semantic, episodic, procedural; distil rather than dump; persist with timestamps and one record per entity; choose when to retrieve; reconcile conflicts; keep logs separately. [ch15.3-15.6]
**Cost**: extra calls and latency.
**Not when**: a single session suffices.

## 22. Testing an agent before release
**When**: the agent takes actions.
**Move**: bucket failures from a task set; trace tool calls; run in a simulated environment with difficult users; red-team; validate with scripts per requirement; test model, harness and task set separately. [ch15.10-15.14]
**Cost**: build effort.
**Not when**: actions are trivially reversible.

## 23. Judging a paper
**When**: a result drives a decision.
**Move**: read in layers; find the claim, what would refute it, ablations, contamination check, samples, error bars, defined terms, who ran it. [ch16]
**Cost**: reading time.
**Not when**: you can replicate the result cheaply.

## 24. "Cheaper per request, so the business is sound"
**When**: a falling price per token is used to conclude that an AI business is profitable.
**Move**: separate the cost of one request, the cost of training the next model and the cost of acquiring users; read cash flow next to profit; estimate what the heaviest user costs against the price. [ch17]
**Cost**: more figures to collect from filings and tests.
**Not when**: the pricing is disclosed and clearly covers the heaviest user's cost.

## 25. "Is this a bubble?"
**When**: a market price or funding round is being debated.
**Move**: run the six tests (revenue against capital, margins at scale, cost per useful output against price, substitutes, price after dependence, falsifiers with dates); state claims so they can be shown wrong; say which facts are unverifiable. [ch17] (position)
**Cost**: time, and access to disclosures.
**Not when**: the question is timing; these tests do not predict when a correction comes.

## 26. Can prompt, cannot check
**When**: outputs are fluent and the reviewer cannot tell good from wrong.
**Move**: teach the foundations first; have the person explain and defend the output orally or under supervision; ask for sources to read, then check claims against them; classify tasks as throughput or learning and keep effort for the learning ones. [ch18]
**Cost**: slower output and more supervised time.
**Not when**: verification is external and cheap (a test suite, a compiler); let the checker decide.

## 27. Assessment or hiring flooded by AI-written work
**When**: application or submission volume explodes and screens use the same tools.
**Move**: use work samples the person explains live or in writing; a human reads the work; models organise notes and draft questions, but do not decide. [ch18]
**Cost**: longer process per candidate.
**Not when**: a low-stakes first filter with a stated appeal route; say so and do not treat its output as final.

