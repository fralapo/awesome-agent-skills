# Chapter 3: Limits of the Statistical Approach, and Symbolic and Hybrid Positions

## Core Idea
Two questions are easy to confuse. (1) *What do statistical models of language actually compute?* (2) *Can that computation, extended by scale and tooling, reach general intelligence?* In this model the first has partial mechanistic answers and the second is a contested prediction. This chapter gives each camp's thesis with arguments for, against and falsifiers. Predictions are written "(position)" and dated to 2020-2025.

## 3.1 "Interpolative database" (position)
- **Position**: a language model is best understood as storing *programs*, not facts: many small vector functions (style transfer, translation of a pattern, completion rules) held as points on a manifold. Prompting selects and interpolates between them. It is memorisation of functions, not just of content.
- **Mechanism**: next-token training under a fixed parameter budget forces compression. The cheapest compression is to learn reusable functions (once English is modelled, a new author is mostly a style-transfer function). Because the functions are continuous vector functions, they can be summed and interpolated; this is not conditional logic.
- **For**: explains style transfer, in-context pattern completion, and failures when the task needs a function that is not among those stored.
- **Against**: if the stored functions are rich enough, "retrieval" and "reasoning" stop being separable; interpretability work shows models do more than look up (a point both camps accept: nobody serious says retrieval alone). A clean characterisation of what else they do is still missing.
- **Falsified by**: a mechanistic demonstration of an algorithm learned from a few examples that works far outside the training range and is implemented as a discrete procedure inside the network.

## 3.2 Scaling laws measure memory, not intelligence (position)
- **Position**: the observed relation (performance grows roughly with the logarithm of training compute) is real, but exam-style benchmarks are memorisation games, so more parameters, data and compute buy more memory and hence higher scores, orthogonal to generalisation power.
- **For**: high-scoring methods on novelty-resistant tests did not need much training compute, and some used none (search programs that were not trained).
- **Against**: the sharpest counter is that capability on hard held-out tasks has kept rising with scale and with test-time compute, so the "orthogonal" claim needs a benchmark that is novelty-resistant and still scales; see ch06-ch08 for the economic stakes.
- **Falsified by**: a novelty-resistant benchmark whose score rises smoothly and predictably with training compute alone, with no extra search.
- **Does not hold when**: the user-facing task is itself memory-heavy (look-up, summarisation, translation); there scaling is exactly right.

## 3.3 Autoregression, surface matching and unpatched failures (mechanism + position)
- **Mechanism**: a model trained to produce what plausibly follows will emit a likely continuation without necessarily parsing the specifics of the question. Cases: a famous riddle answered by its canonical form when numbers have changed; a canonical puzzle answered for an absurd variation.
- **Position**: these limits are inherent to parametric curve-fitting with the same architecture, so they have not gone away since the first transformer models; fixes by human feedback are special-casing, so the failure class persists.
- **Against**: rates of this failure class fall with scale and with reasoning-style training; "no progress since day one" is an overstatement in this model unless measured on fresh variants.
- **Falsified by**: a steadily improving score on freshly generated adversarial variants that nobody could have patched.

## 3.4 What cannot be learned from data (position)
- **Position**: most knowledge that matters cannot be learned from examples; it must be derived. Example: show an algorithm millions of unsorted lists paired with sorted lists; no learner discovers from this that sorting costs about n log n, which is deduced.
- **Mechanism**: learning is statistical induction over a sample; derivations about all inputs (complexity bounds, mathematical truths) are not statistical regularities of a sample.
- **For**: a short argument that matches the idea that a mathematical claim holds for all cases, not on average.
- **Counter**: a language model can write the derivation because derivations are in its data, and tree-based representations of formulas are being used to discover new mathematics by search; so statistical regularities do exist in analytical text. The camp replies that in factual and analytical domains you are not allowed to approximate: approximating a decision with a probability is fine for recognising objects, not for a proof.
- **Falsified by**: a trained model producing correct proofs of novel, verified theorems at a rate unexplained by recombination of seen lemmas (and passing an independent check).
- **Does not hold when**: a verifier is in the loop; then an unreliable generator can still produce guaranteed results (ch02 2.6).

## 3.5 Knowledge representation as the missing piece (position)
- **Position**: "knowledge representation is the dark matter of AI". Knowledge is an ontology: moving from specific instances to concepts, with many instances per concept, and knowledge models that can operate on concepts. A concept ("banana") is more than a manifold that classifies images of it.
- **For**: explains explainability, reuse and extension; arguments from the frame problem (an autonomous agent must decide what does not change) and from adversarial examples.
- **Against**: hand-built ontologies were brittle (expert systems relied on tacit common sense never written down); learned representations scale where hand-built ones did not.
- **Hybrid position**: combine deep learning with knowledge structures and symbolic reasoning to improve efficiency, explainability, extensibility and reasoning. Judgement: the hybrid is likely to be right in engineering terms (components with different guarantees), but the open issue is the interface: who builds and maintains the symbols.
- **Falsified by**: a purely learned system that matches the hybrids on efficiency and explainability for the same tasks (this is the pure-scale prediction).

## 3.6 Neurosymbolic models: algebraic generalisation (position)
- **Position**: systems need variables and operations over them (a class of "universally quantified one-to-one mappings"), so that a rule learned for some instances transfers to any instance regardless of the training space. Hybrid systems with explicit symbols and learned perception give this.
- **For**: infant studies and simple controlled tasks show abstract rule generalisation that standard networks fail when examples are outside the training range.
- **Against**: scaled language models now pass many such tests; whether this is variable binding or broad coverage is unresolved.
- **Falsified by**: a standard network trained on a bounded numeric range that continues a rule across arbitrarily different encodings.
- **Does not hold when**: the application tolerates local errors; then the benefit of symbols (exact guarantees) may not justify their cost.

## 3.7 The Turing-complete question (position)
- **Mechanism (fact)**: a fixed-context autoregressive language model with no external memory is not Turing-complete in the technical sense; allowed to write and run programs, or to use an unbounded scratchpad, it can be.
- **Position A**: therefore it has practical limits on whole classes of problems (long exact procedures).
- **Position B**: practically, large contexts and tool use remove the limit that matters; "potentially infinite memory" is the same idealisation as for a real computer.
- **Falsified by**: a class of useful, long procedures (verified) that tool-using models fail at systematically while a simple program solves them.
- **Note**: programs drawn uniformly from the space of programs are mostly invalid or useless; a representation in which most programs are useful would be a major finding (unverified whether such work exists).

## 3.8 Compression as a general principle (position, counter-position)
- **Position**: next-token prediction instils induction principles (a preference for simple, compressible explanations), so a text-trained model can transfer to unfamiliar sequence problems: zero-shot time-series forecasting, and generation of crystal structures after fine-tuning on atoms written as text, in some cases better than purpose-built models. Compressible representations include symmetries (for instance rotation invariance), learned quickly under text pre-training.
- **For**: shows transfer is real, not only memorisation of text.
- **Against**: different problems are often truly different, not projections of one underlying reality (a shared-representation hypothesis may hold in some cases and not others); benchmark gains on a few tasks are a poor basis for universal claims.
- **Falsified by**: failure of text pre-training to help on tasks with the same formal structure but no textual analogue.
- **Use**: when a general model beats a specialist, check whether the specialist had a modern training recipe.

## 3.9 World models and planning: a hybrid built from continuous parts (position)
- **Position**: continuous, differentiable components are right for perception and for a learned *world model* (predict the next state of the relevant part of the world, in an abstract representation, not pixels or tokens) and a learned cost estimate; discrete search is then used on top (model-predictive planning). Humans are poor at discrete search (otherwise we would beat engines at chess and Go), so differentiable guidance is the part we are good at.
- **Mechanism**: actor-critic methods learn a differentiable value estimate so that gradients flow; a differentiable world model lets you optimise a sequence of actions by gradient descent at inference time, and learn a policy from it.
- **For**: it unifies planning with learning and avoids spending a token budget on every step of a plan.
- **Against**: world models learned from real-world data have not matched this promise at scale (unverified; treat as a prediction); autoregressive systems with tools are catching up on many planning tasks.
- **Falsified by**: a system without an explicit predictive state model reaching reliable long-horizon planning in open environments.
- **See also**: self-supervised and world-model methods in `ai-ml-concepts` ch14.

## 3.10 "Approximate retrieval plus a verifier" (position)
- **Position**: language models are fast candidate generators with no guarantees; the right architecture pairs them with external verifiers or solvers (generate, check, critique, repeat). The model is a flexible source of guesses, the verifier supplies soundness.
- **For**: works in code, planning with a checkable plan, and formal tasks.
- **Against**: verification is hard outside formal domains; a model verifying itself inherits its errors.
- **Falsified by**: a model that can reliably self-verify in domains with no external checker.

## Checklist for this chapter
1. Is the claim about what a model *does* (mechanism) or about what it *will be able to do* (prediction)?
2. Which camp's falsifier has actually been tried?
3. Is the proposed hybrid's interface specified: who writes and updates the symbols?
4. Does a verifier exist for this task? If yes, generator reliability matters less.
