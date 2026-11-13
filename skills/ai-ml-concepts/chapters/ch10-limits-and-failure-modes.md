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
