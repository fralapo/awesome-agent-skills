# Chapter 8: How Large Language Models Are Trained, Prompted and Scaled

## Core Idea
A language model is built in stages: predict the next token on a vast corpus (pre-training), then shape it with human preferences and verifiable rewards (post-training), then spend extra computation when answering (test-time compute). In this model, each stage adds a different kind of signal, and each signal has its own failure mode.

## 8.1 Pre-training
- **Thesis**: next-token prediction on enormous text teaches grammar, facts and patterns of reasoning as a by-product.
- **Mechanism**: initialise parameters randomly, feed text, compare prediction to the true next token, backpropagate. The compute is vast: with a billion operations per second, training the largest models would take over a hundred million years (a dated estimate, as reported at the time).
- **Trade-off**: breadth of knowledge against knowledge patchiness; the objective rewards plausible text, not truth.
- **Does not hold when**: the target behaviour is not in the data distribution (new facts, new tools).

## 8.2 Post-training: preferences and helpfulness
- **Thesis**: the pre-trained model is an autocomplete engine; training on human preferences turns it into an assistant.
- **Mechanism**: people rank or flag outputs; a reward model learns the preferences; the policy is updated to raise the reward. A small amount of binary feedback can go far: in a classic study, a simulated creature learned a backflip from on the order of hundreds of human comparisons, a small fraction of its agent steps. A human evaluator supplies the score that no formula could write down.
- **Trade-off**: preferences capture what looks good to the raters, including flattery and confident style.
- **Does not hold when**: raters cannot judge correctness (expert or long outputs).

## 8.3 Outcome rewards versus process rewards
- **Thesis**: rewarding correct reasoning steps can beat rewarding correct final answers.
- **Mechanism**: an outcome reward model scores only the final answer; a process reward model scores each step. Human labellers mark steps positive, neutral or negative; the step model predicts step correctness; a solution's score is the product of step probabilities, and the first wrong step locates the mistake. In a study on competition-style mathematics, best-of-many selection by a process model beat selection by an outcome model, and both beat majority voting; a base score of about 42 percent rose to about 78 percent on a subset (as reported at the time, with the curve still rising as more samples were scanned). It also transferred to chemistry and physics questions. Process supervision has an alignment appeal because it trains chains of thought that humans endorse.
- **Trade-off**: step labels are costly and subjective; outcome rewards are cheap but admit lucky right answers from wrong reasoning.
- **Does not hold when**: steps are not cleanly separable or the domain lacks a checker.

## 8.4 Reinforcement learning on verifiable answers
- **Thesis**: when answers can be checked automatically (mathematics, code, some science), a model can improve on its own reasoning traces.
- **Mechanism**: a third objective on top of prediction and preference: reward correct results. Generate many diverse chains of thought, keep those that reach verified answers, fine-tune on them, repeat. Own-generated chains have been reported to outperform fine-tuning on human-written chains. The ingredient that makes it scale is the automatic grader.
- **Trade-off**: strong where verification is cheap; unclear gains in open-ended tasks without a grader; rewards can be gamed (chapter 10).
- **Does not hold when**: the checker is wrong or leaky.

## 8.5 Test-time compute, chain of thought and self-consistency
- **Thesis**: letting the model produce intermediate tokens before answering, and sampling several answers, improves accuracy on tasks that need deliberation.
- **Mechanism**: a transformer does a fixed amount of computation per token, so forcing an answer as the first token starves hard problems; a scratchpad adds serial computation. Greedy decoding picks the single most probable path; sampling several paths and taking the majority final answer (self-consistency) often does better, with returns that rise with the number of paths. Two scaling curves have been reported: accuracy rises with thinking time and with train-time compute on verified traces.
- **Trade-off**: cost and latency grow with tokens; a scratchpad can also rationalise a wrong answer.
- **Does not hold when**: the question is pure recall, where deliberation adds nothing.

## 8.6 Tools beat unaided arithmetic
- **Thesis**: language models are generators, not calculators; give them tools for exact work.
- **Mechanism**: multiplication of long numbers fails without tools beyond a certain digit count, and the digit threshold rises with newer models; with a code tool the same models succeed and decide to use it unprompted. Hallucinated answers can look plausible (right leading and trailing digits).
- **Trade-off**: tool use adds latency and attack surface.
- **Does not hold when**: no tool is available and the user cannot verify.

## 8.7 Scaling: compute, data and diminishing returns
- **Thesis**: loss falls predictably with model size, data and compute, but a bigger loss improvement is not a proportionally better product.
- **Mechanism**: scaling laws extrapolate across several orders of magnitude and have been extended from loss to benchmark performance (a lab reported predicting downstream results from a compute budget). One reported case: about four times the compute gave a visible but not four-fold improvement, raising the question of how much users will pay if they must check outputs anyway. Data quality and filtering shift the curve; models are used to filter data for the next models.
- **Trade-off**: spending on scale competes with spending on data, post-training and inference.
- **Does not hold when**: data runs out (natural text is finite; other modalities like video are less exhausted), or when the benchmark saturates.

## 8.8 Post-training share and domain specialisation
- **Thesis**: as post-training grows in the compute budget, model strength becomes domain-dependent rather than uniform.
- **Mechanism**: reinforcement on domain-specific environments (coding, office tasks, search) lifts those areas while leaving others flat or worse. A claim of the form "enough specialisms will generalise" is a bet, not a result; so is the claim that longer context can supply the missing domain knowledge.
- **Trade-off**: targeted gains versus unexpected regressions elsewhere.
- **Does not hold when**: you assume one model that is better at coding is better at all else.

## 8.9 Open weights versus open source
- **Thesis**: downloadable weights are not the same as an open recipe.
- **Mechanism**: a common definition of open-source AI includes training-data provenance; a release that omits it cannot be reproduced even with the compute. Compute thresholds in regulation treat very large training runs as systemic risk.
- **Trade-off**: weights allow local use and auditing of behaviour; without data, auditing the causes is limited.
- **Does not hold when**: the licence or the data terms restrict use.
