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

## 5.9 Double descent: error can fall again after the interpolation threshold
- **Thesis**: the textbook U-shaped test-error curve is the first half of the story; past the point where a model just fits the training data exactly, test error can drop again.
- **Mechanism**: with polynomial fits to noisy points, test error falls, rises as the model starts fitting noise, peaks where the model has just enough freedom to interpolate the data (only one fitting solution, extremely sensitive to the noise), then falls as many interpolating solutions appear and the solver picks the smoothest, smallest-norm one. The same shape has been seen for transformers and vision networks, both as a function of model size and as a function of training time: continuing after test error starts to rise can bring it back down, sometimes lower than before, and a small amount of label noise makes the bump more pronounced (as reported at the time). Stochastic gradient descent tends toward small-norm solutions under certain conditions.
- **Trade-off**: bigger models and longer training can generalise better, but early stopping on the first rise may cut off the second descent.
- **Does not hold when**: the setting is the toy one: in the polynomial example the effect depends on the basis in which the polynomial is written (a numerically stable orthogonal basis shows it, the plain monomial basis with minimum norm does not), so "number of parameters" is a poor proxy for complexity. Later textbooks treat double descent as consistent with the bias-variance idea once complexity is measured as effective flexibility (position).

## 5.10 Bias, variance and what can actually be measured
- **Thesis**: test error decomposes into bias squared, variance and irreducible noise, but computing bias requires knowing the true function.
- **Mechanism**: refit the same model class on many random samples of the same process; the average fit's distance from the truth is bias, the spread of fits is variance. A too-simple model has high bias; a flexible model fitted to few noisy points has high variance. Because the truth is unknown in real problems, the U-shaped curve is a conceptual tool, not a quantity you can plot.
- **Trade-off**: a clean vocabulary for diagnosing under- and overfitting against limited practical measurability.
- **Does not hold when**: models sit at or past the interpolation threshold (5.9), where variance and bias still decompose but the classic trade-off no longer predicts the shape.

## 5.11 First-generation anti-overfitting kit and data as a sample
- **Thesis**: the first very deep image classifier relied on augmentation, dropout and weight decay, and every dataset is a sample of a process, not the process.
- **Mechanism**: random shifts, flips and colour changes make the label independent of exact appearance; dropout switches off random units so no single pathway is required; weight decay penalises large weights. An observation such as "three hours of sleep and five of study gave a score of 75" is one draw: other variables and luck matter, so a model that reproduces it exactly has learned noise. A hold-out set tells which learned pattern survives.
- **Trade-off**: robustness against slower training and tuned hyperparameters.
- **Does not hold when**: the augmentation changes the label (flipping text, rotating digits that are rotation-sensitive).
