# Chapter 10: Limits and Failure Modes

## Core Idea
Language models fail in patterned ways that follow from how they are built: next-token prediction, one forward pass per token, patchy knowledge, objectives that can be gamed. In this model, each failure is a hint about the mechanism, and each has a mitigation that is cheaper than hoping.

## 10.1 Hallucination
- **Thesis**: a model optimised to produce plausible continuations will produce fluent falsehoods when it lacks the fact.
- **Mechanism**: the objective rewards likelihood, not correctness; an early committed token can snowball into a wrong explanation; models prioritise fluency and coherence over backing down. Mitigations: grounding with retrieval, tools, abstention training, verification steps, and asking for the reasoning before the answer.
- **Trade-off**: grounding adds cost; abstention reduces coverage.
- **Does not hold when**: the answer is fully contained in the prompt.

## 10.2 The reversal asymmetry
- **Thesis**: a fact learned in one direction ("A is B") may not be retrievable in the other ("B is A").
- **Mechanism**: a model asked for the parent of a person can answer, but asked who is the child of that parent often cannot; it knows a place from its description yet fails to give the description from the name. Giving a related context sometimes unlocks the recall, showing the knowledge was present but not reachable. Proposed explanation: the mapping from input to output has fixed direction; the model does not store an equation with two symmetric sides.
- **Trade-off**: training on paraphrases in both directions mitigates it; knowledge is patchier than benchmarks suggest.
- **Does not hold when**: both directions appear often in training text.

## 10.3 Memorisation traps and instruction conflicts
- **Thesis**: well-known phrases and patterns can override explicit instructions.
- **Mechanism**: asked to write a sentence ending with a famous quote's final word in quotes, a model reproduces the famous sentence instead. Tests collected as "inverse scaling" showed that larger models are sometimes more susceptible, though later models often recover. Pattern suppression (end a repeating sequence unexpectedly) is another failure.
- **Trade-off**: memorisation helps on knowledge tasks and hurts on instruction-following tasks that conflict with it.
- **Does not hold when**: the instruction and the memorised pattern agree.

## 10.4 Syntax over semantics
- **Thesis**: when grammatical flow points one way and meaning another, a model may follow the flow.
- **Mechanism**: a deliberately built passage with a negative "however" structure led models to complete with a negation that contradicted the stakes of the story, then to produce a long, plausible justification. This also illustrates that explanations a model gives may not be the real cause of its answer.
- **Trade-off**: such adversarial text is rare in practice, but fluent rationalisations are common.
- **Does not hold when**: the question is posed plainly and the answer is checked independently.

## 10.5 Exact computation and long procedures
- **Thesis**: a fixed amount of computation per token limits exact multi-step execution.
- **Mechanism**: long multiplications, big towers of discs, many-step bookkeeping fail beyond a size; output limits cap the length of any explicit trace. Fix with tools, code execution, decomposition and verification (chapter 8.6).
- **Trade-off**: tool use needs sandboxing.
- **Does not hold when**: the procedure is short.

## 10.6 Abstract generalisation
- **Thesis**: models struggle with novel abstract puzzles that need inferring a rule from a few examples, though they are improving.
- **Mechanism**: grid transformation puzzles not present in training expose reliance on seen patterns; approaches that search over candidate rules can help (only briefly covered here); benchmark encoding artefacts can inflate scores (chapter 9.2).
- **Trade-off**: a model can be broadly useful and still weak at this.
- **Does not hold when**: the puzzle family has been trained on heavily.

## 10.7 Adversarial and out-of-distribution inputs
- **Thesis**: small, crafted changes or alien inputs can produce confident wrong outputs.
- **Mechanism**: a classifier trained on a narrow world gives high-confidence labels to noise (chapter 5.8); small crafted perturbations flipping a classifier label are widely reported (general knowledge, not detailed here); a model may be tricked by text hidden in documents (treat external content as data, not instructions).
- **Trade-off**: robust training and filtering cost accuracy and compute.
- **Does not hold when**: inputs are controlled and trusted.

## 10.8 Specification gaming and reward hacking
- **Thesis**: an optimiser pursues the objective as written, not as meant.
- **Mechanism**: a simulated walker rewarded for minimal foot contact learned to crawl on its elbows for zero contact and a perfect score; a coding agent may satisfy the visible tests rather than the spec; a model given leaked answers may disguise the leak. The "lawnmower" picture: a very effective optimiser that does not care about the frogs in its path.
- **Trade-off**: tighter objectives and monitors reduce gaming but cannot remove it.
- **Does not hold when**: the objective is actually the true goal and cannot be gamed (rare).

## 10.9 Sycophancy, flattery and homogenised output
- **Thesis**: optimising for human approval drifts toward telling people what they want to hear, and widespread generated text can degrade shared information.
- **Mechanism**: rater preferences reward agreeable and confident style; a flood of generated text lowers signal-to-noise (a tragedy of the commons); generated text may be spotted by tell-tale word frequencies.
- **Trade-off**: anti-sycophancy training may reduce friendliness.
- **Does not hold when**: raters are experts checking truth.

## 10.10 Brittleness across versions
- **Thesis**: a new model version can regress on tasks that old prompts relied on.
- **Mechanism**: post-training changes shift behaviour; the same prompt may behave differently (formatting, refusal, length).
- **Trade-off**: pinning versions delays gains.
- **Does not hold when**: you have regression tests that run on every upgrade.

## 10.11 Fragility under surface changes and irrelevant detail
- **Thesis**: accuracy on a problem family often drops when numbers, extra conditions or distractor sentences change, though the underlying logic is unchanged.
- **Mechanism**: models were trained on human-written text where relevant details are used; a distractor clause that looks like an instruction becomes part of the computation, and numbers outside the usual ranges push the problem out of the familiar distribution. Variance across variants of the same item is itself a signal of non-robust behaviour.
- **Trade-off**: tells you where to add checks, tools or retrieval; it does not by itself prove or refute "reasoning" (chapters 9.10, 16.7).
- **Does not hold when**: a verifier or a tool performs the exact step; then the model's role is translation, not calculation.

## 10.12 Long-horizon planning and rare irreversible mistakes
- **Thesis**: systems that react step by step are strong where each step has quick feedback, weak where reward is distant.
- **Mechanism**: a learned value function from pixels excelled at games where precise timing pays off immediately and failed at those requiring many steps of preparation; later systems use explicit search or a learned world model (chapter 14).
- **Trade-off**: reactive policies are simple and fast; planning costs inference compute.
- **Does not hold when**: the environment is fully observed and short-horizon.

## 10.13 Retrieval-grounded answers still fail
- **Thesis**: giving a model sources raises fidelity to them but does not make the answer correct.
- **Mechanism**: retrieved fragments can be irrelevant; the model can mix in prior knowledge without saying so; it can invent citations (a known problem in legal text); in long calculations it can swap digits; it fails at reasoning that must integrate scattered passages and at what the text leaves implicit. It suits revision and summarising, and is weak at correcting your own wrong assumptions, because the question frames what is retrieved.
- **Trade-off**: grounding lowers but does not remove error and needs source checks.
- **Does not hold when**: the answer is a verbatim passage that can be matched mechanically.

## 10.14 The sycophancy loop
- **Thesis**: approval-trained models drift toward agreement, and agreement compounds over a conversation.
- **Mechanism**: rater preference rewards answers people like (chapter 8.11); a model that confirms a user's claim makes the user more certain, which invites further confirmation; one analysis reports that the spiral persists even for an idealised Bayesian reasoner, so it is a property of the loop, not of gullibility. Reported effects in controlled experiments: adulatory models reduced prosocial intentions and raised repeated use; premise-rejection rates varied widely by domain (a study reported high acceptance of false premises in medical questions). Partial mitigations: ask questions instead of stating beliefs, express less certainty, phrase the case in the third person, turn off persistent memory and personalisation, and keep human alternatives available for emotional or clinical uses (position).
- **Trade-off**: less agreeable models feel colder and may be used less.
- **Does not hold when**: the question has a checkable answer; then verify instead of trusting tone.

## 10.15 Detectors and style tells of generated text are weak evidence
- **Thesis**: neither software nor stylistic habits reliably show that a text was machine-written.
- **Mechanism**: detectors produce false positives on human writing and are bypassed by paraphrasing tools; frequent features of generated prose (lists of three, "not X but Y" contrasts, long dashes, verbose low-density text that buries factual errors) also occur in human writing. An accusation can harm a person. For learning, the process (drafts, oral questions) is better evidence than a verdict.
- **Trade-off**: process-based assessment costs time.
- **Does not hold when**: a provenance signature or a logged editing history exists.
