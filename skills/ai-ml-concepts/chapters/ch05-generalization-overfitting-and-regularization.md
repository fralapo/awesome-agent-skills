# Chapter 5: Generalization, Overfitting and Regularization

## Core Idea
Good training results prove little; the question is performance on data the model has not seen. In this model, generalization is a budget: capacity, data, inductive bias and regularization compete, and the evaluation must be separated from the training so that the budget is measured honestly.

## 5.1 Train, validation, test
- **Thesis**: a model should be judged on data it never touched during fitting or tuning.
- **Mechanism**: train set updates the weights; a validation set steers choices (architecture, stopping); a final test set is used once. If test items leak into training or selection, scores become optimistic (chapter 9 on contamination).
- **Trade-off**: holding data out costs data; small sets give noisy estimates.
- **Does not hold when**: the deployment distribution differs from the test distribution; the test score then only bounds in-distribution behaviour.

## 5.2 Overfitting as memorising the textbook
- **Thesis**: a model that fits the training examples too closely learns their noise and quirks instead of the concept.
- **Mechanism**: with a classifier drawn on a plane, an overfitted boundary wiggles around individual points. The exam analogy: practising exercises by memorising their answers gives full marks only if the exam repeats the textbook. A sufficiently large network can fit even randomly assigned labels.
- **Trade-off**: bigger models fit complex truths and memorise more easily.
- **Does not hold when**: the "test" is itself drawn from the training material, in which case overfitting is rewarded and goes unnoticed.

## 5.3 Regularization: prefer simpler models
- **Thesis**: add a penalty or constraint that favours simple solutions, so extra capacity is not spent on noise.
- **Mechanism**: a penalty on the sum of absolute weights (L1) pushes many weights to exactly zero; on squared weights (L2) shrinks all weights smoothly. Other tools: early stopping, dropout, data augmentation, smaller models. The strength is a dial: too weak leaves overfitting, too strong underfits ("as simple as possible but not simpler").
- **Trade-off**: more bias, less variance; the right setting is found by validation, not by principle.
- **Does not hold when**: the data is plentiful and diverse enough that the problem is not variance-limited.

## 5.4 Pruning and compression of networks
- **Thesis**: trained networks are redundant, so many units can be removed with small loss, giving faster and smaller models.
- **Mechanism**: remove filters or weights under an explicit accuracy-loss budget rather than just dropping the weakest responses; reported results for an image network showed about a quarter of filters removable for a few tenths of a percent loss, and more than three quarters for around three percent (as reported at the time, one study). Sometimes a pruned network even does better on a task.
- **Trade-off**: size and latency against accuracy; the best trade-off depends on the device.
- **Does not hold when**: the removed capacity held rare but important behaviour that the aggregate accuracy metric does not show.

## 5.5 Inductive bias: what the model assumes before seeing data
- **Thesis**: a learner with no assumptions has to test an enormous number of hypotheses; assumptions cut data needs but narrow the problems it can solve.
- **Mechanism**: convolutional layers assume locality and translation structure; sequence models assume order matters; a simulator-based prior assumes physical laws. Slow learning in a generic reinforcement learner is attributed to tiny incremental updates and weak bias; adding episodic memory (reuse stored experiences) and learning how to learn are proposed remedies, linked to hypotheses about brains.
- **Trade-off**: general learners reuse across tasks but need more data; specialised ones are sample-efficient and brittle.
- **Does not hold when**: the bias is wrong for the domain.

## 5.6 Representation: warping the space until a line separates
- **Thesis**: depth works because each layer re-represents the data so that the final decision is easy.
- **Mechanism**: a problem that cannot be separated by a straight line in the raw space may become separable after smooth warping (stretching without tearing); more layers mean more degrees of freedom to untangle complicated shapes (spirals, bull's-eyes), and the hidden layers build features from simple to composite.
- **Trade-off**: expressiveness against interpretability and optimisation difficulty.
- **Does not hold when**: the data is so tangled or the sample so small that no warping can be learned reliably.

## 5.7 Data quality over architecture
- **Thesis**: reported evidence suggests that curated data shifts the whole performance curve more than architectural tweaks do.
- **Mechanism**: different architectures often show the same scaling slope with different offsets; claims from practitioners describe very large effective-compute gains from crafting data digestible for the model, versus single-digit gains from optimiser or architecture changes.
- **Trade-off**: curation costs human and compute effort and can bake in biases.
- **Does not hold when**: data is scarce in a domain, where augmentation, synthetic data or architecture priors matter more.

## 5.8 Confident nonsense and out-of-distribution inputs
- **Thesis**: a model trained to be confident inside its narrow world has no reason to be unsure outside it.
- **Mechanism**: a digit classifier shown random noise may output a confident digit, because its cost never rewarded saying "none of the above"; it recognises digits but cannot draw them.
- **Trade-off**: adding an abstain option or calibration costs accuracy or data.
- **Does not hold when**: the deployment inputs are guaranteed to stay in-distribution.
