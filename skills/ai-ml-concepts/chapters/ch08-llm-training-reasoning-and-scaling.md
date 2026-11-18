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

## 8.10 Zero-shot and few-shot: the prompt as the task specification
- **Thesis**: a language model trained on varied text can be steered to new tasks by describing or demonstrating them in the prompt, with no weight updates.
- **Mechanism**: frame a task as text to continue: a description and zero, one or a few worked examples, then the new case. An early model of about one and a half billion parameters trained on roughly forty gigabytes of web text performed rudimentary translation, reading comprehension and summarisation this way (summaries barely beat picking three random sentences) and its authors argued that single-task training is a main cause of poor generalisation, while a sufficiently varied corpus teaches tasks implicitly. A much larger successor improved with size in zero-, one- and few-shot settings, answered closed-book questions competitively with a task-trained retrieval system on some sets and worse on others, and added two-digit sums reliably but degraded at four or more digits and at multiplication (as reported at the time).
- **Trade-off**: flexible and data-free; sensitive to wording, example order and format; examples cost context.
- **Does not hold when**: you read success on arithmetic as proof of logic: a reviewer's position was that near-exact-match training-data overlap (weak n-gram deduplication, partly clean subsets) plus interpolation explains much; see chapter 16.

## 8.11 Preference training in detail: reward model, KL leash, over-optimisation
- **Thesis**: reinforcement learning against a learned reward model works only while the policy stays near the data the reward model has seen.
- **Mechanism**: pipeline: pre-trained model, supervised fine-tuning on human demonstrations, a reward model trained on human comparisons between outputs, then a policy-gradient update whose reward is the reward-model score minus a penalty on the divergence from the supervised model. In a summarisation study the resulting policy was preferred to human reference summaries (a pre-trained model alone lost 70 to 80 percent of comparisons) and transferred better to new domains than the supervised model (as reported at the time). Without the penalty the policy finds adversarial text: keyword-stuffed, repetitive phrases that score high with the reward model but are poor summaries. The reward model is just a network, and finding inputs it likes is the same problem as finding adversarial examples.
- **Trade-off**: higher quality as judged by humans against reward hacking and flattery (chapter 10); a tighter leash lowers risk and gains.
- **Does not hold when**: the reward model is evaluated far from its training data, or when raters cannot judge correctness.

## 8.12 Group-relative policy optimisation: no learned value function
- **Thesis**: you can estimate the advantage of an answer by comparing it with other answers to the same question, avoiding a separate value network.
- **Mechanism**: policy-gradient methods maximise probability of good actions weighted by an advantage and need a trust region so noisy updates do not wander (a penalty on divergence from the previous or reference policy; clipping in the common variant). The group variant samples a group of answers per prompt, scores them with a reward model or checker, and sets each advantage to its reward minus the group mean, divided by the group standard deviation; the divergence penalty is added directly to the objective rather than to the reward. Outcome and step-level rewards both fit. In a mathematics study the recipe, with a code-initialised 7-billion-parameter model and a curated, multilingual maths corpus, matched much larger general models on a competition-style benchmark (as reported at the time; specialised against general).
- **Trade-off**: saves memory and complexity; needs many samples per prompt, so rollouts dominate cost.
- **Does not hold when**: all answers in a group get the same reward (zero advantage, no signal) or the reward is noisy.

## 8.13 What reinforcement learning on verifiable tasks mostly does: sharpening
- **Thesis**: much of the measured gain from reinforcement learning is moving correct answers up the ranking, not adding capability the base model lacked.
- **Mechanism**: compare pass at k (is any of the top k answers correct) with majority vote at k (is the consensus correct). After reinforcement learning, majority-vote accuracy rose while pass-at-k barely moved, in the report's analysis, meaning the output distribution became more robust rather than the set of solvable problems growing. Code pre-training helped maths more than raw scientific-paper text did, perhaps because papers communicate results rather than derivations (a guess).
- **Trade-off**: cheap, fast gains; a ceiling set by the base model (position: the ceiling may be lower than many expect, so better base models are still needed).
- **Does not hold when**: long reinforcement runs with exploration do reach new solutions; the evidence here is limited to the settings tested.

## 8.14 Spending test-time compute: a menu, no single winner
- **Thesis**: how to spend inference compute depends on question difficulty and budget.
- **Mechanism**: options in order of complexity: sample many and take the majority (no verifier needed); best-of-N with a verifier or reward model; beam search guided by a step-level verifier (keep the best partial solutions at each step); look-ahead search (roll out a few steps to score a candidate, noisy but forward-looking); sequential revision by a model trained to edit its own attempts. Difficulty is best defined empirically per question (how often the model solves it), not by dataset labels, which did not predict behaviour. Findings in one study: on easy questions simple best-of-N is enough and beam search shows over-optimisation at high budget; on medium ones search helps most; on the hardest ones little helps. Choosing the method by estimated difficulty and budget ("compute-optimal allocation") matched or beat each fixed method; on easy and medium questions with low inference load extra test-time compute could substitute for a larger model, while on hard questions or high inference load more pre-training was more effective (as reported at the time).
- **Trade-off**: spending per query against training once.
- **Does not hold when**: you generalise from the study: plots lacked error bars, the revision and verifier models were trained for one dataset, and the difficulty estimate itself costs compute that was not counted.

## 8.15 Scaling laws as power laws, and a theory of why
- **Thesis**: test loss follows a power law in compute, parameters and data, with little dependence on architecture details, and a data-manifold argument offers a partial explanation.
- **Mechanism**: on log-log axes a family of training curves for models of different sizes has an envelope, the compute-efficient frontier, that is a straight line; the fit spans many orders of magnitude of compute (about thirteen between early small runs and the largest reported runs; the largest figures were unofficial). The loss is cross-entropy, minus the log of the probability assigned to the correct next token. If data lie on a manifold of intrinsic dimension d, the typical distance between training points shrinks like data to the power minus one over d, which would tie the loss exponent to d (a reported relation: the intrinsic dimension should be at least four divided by the magnitude of the loss exponent). Plugging in the observed language exponent (about 0.095 in magnitude) gives a dimension of at least about 42, while direct estimates of the learned manifold gave about 100: the inequality held but agreement was far worse than on synthetic and image data, so the theory is partial.
- **Trade-off**: predictable loss; specific abilities (unscrambling words, arithmetic, multi-step reasoning) still appear at unpredictable scales.
- **Does not hold when**: you extrapolate behaviour rather than loss, or ignore data limits.

## 8.16 Value learning from pixels: the classic deep Q-learning recipe
- **Thesis**: a convolutional network can learn to play video games from raw pixels by regressing expected future reward.
- **Mechanism**: a value function estimates the total future reward of taking an action in a state; it satisfies a recursion (the value now equals reward plus the best value next), which turns into a regression target as play proceeds; the agent plays with the current network and trains on its own experience. With raw pixels and no per-game tuning, the original system beat earlier methods on six of seven games and a human expert on three (as reported at the time); it did worst on games that need long-horizon planning, which stayed hard for years.
- **Trade-off**: general and simple against sample hunger and weak long-term planning.
- **Does not hold when**: rewards are sparse and far in the future, or one mistake is irreversible.

## 8.17 Adapting a model: prompt, retrieval or fine-tuning
- **Thesis**: three ways to adapt a model change different things; choosing by what is missing (knowledge, behaviour, or format) avoids expensive mistakes.
- **Mechanism**: *prompting* changes the context only. *Retrieval* inserts text fragments found by semantic similarity into the prompt: it updates easily, is inspectable (you can see what was retrieved) and has a running cost in tokens and latency. *Fine-tuning* changes weights, often through small low-rank adapters kept separate from the base weights: it teaches tasks, style and output format well, adds knowledge poorly, is opaque, must be redone to update facts and has an upfront cost. They can be combined. The delicate part of fine-tuning is the dataset; to judge a style change, run base and tuned models on the same prompts and compare. Behaviour learned from a narrow set can spread beyond it (chapter 11.16).
- **Trade-off**: retrieval pays per query and depends on what is found; fine-tuning pays once and ages.
- **Does not hold when**: the knowledge is small enough to sit permanently in the prompt (then neither is needed), or the model is closed and cannot be tuned.

## 8.18 Verifiability decides where capability grows (jagged profile)
- **Thesis (position)**: reinforcement on checkable answers makes progress fast where an exact verifier exists and slow where it does not, so capability is uneven ("jagged") rather than uniformly rising.
- **Mechanism**: mathematics, code and puzzles have automatic checks, many examples and quick feedback; legal reasoning, campaign design, clinical triage or strategy have answers that cannot be checked quickly, or feedback arrives months later. Benchmarks are then built on what is verifiable, those get optimised until saturated, and unverifiable problems stay out of the tables: the evidence about progress is circular. Whether the chains of thought found by this training were already latent in the base model (visible at large k in pass-at-k, chapter 8.13) or whether long runs create new capacity is disputed.
- **Trade-off**: verifiable domains gain quickly and measurably; other domains need slower proxies such as expert grading.
- **Does not hold when**: a domain acquires a cheap trustworthy verifier (a simulator, a formal checker), or a generalisation from verified to unverified domains is demonstrated.

## 8.19 Prompt practice: what tends to help and what does not
- **Thesis**: prompting is empirical craft, not an exact science; a few habits are stable.
- **Mechanism**: helpful: a few examples of the desired output, a role or audience, the relevant context, an explicit output format, delimiters between instructions and data, and a structured template such as context, objective, style, tone, audience, response. Unhelpful: long prompts padded with irrelevant detail; placing the expected answer in the question (the model tends to agree); "think step by step" on models already trained to reason, which adds nothing; secret formulas sold as techniques. Automatic prompt optimisation can search wordings against a metric.
- **Trade-off**: more structure costs effort and tokens; the gain depends on the model and must be measured.
- **Does not hold when**: the task is simple enough that a plain request works; ritual then adds noise.
