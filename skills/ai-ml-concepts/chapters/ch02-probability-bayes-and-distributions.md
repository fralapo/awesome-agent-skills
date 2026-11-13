# Chapter 2: Probability, Bayes' Rule and Distributions

## Core Idea
Learning from data is reasoning under uncertainty. In this model, the useful probability toolkit is small: conditioning, Bayes' rule for updating, the binomial for counts, the central limit theorem for sums, and convolution for adding random variables. Each has a standard misuse worth naming.

## 2.1 Conditioning and the "and" rule
- **Thesis**: the chance of two events together is the chance of the first times the chance of the second given the first; it equals the product of the separate chances only for independent events.
- **Mechanism**: write the joint probability both ways (A then B given A; B then A given B); the two expressions are equal. That identity is Bayes' rule.
- **Trade-off**: dice and coins teach independence, so intuition from games misleads in the real world where events are correlated (relatives, repeated measurements of one subject, adjacent tokens in text).
- **Does not hold when**: you cannot estimate the conditional term; then the formula is correct and unusable.

## 2.2 Bayes' rule as updating beliefs
- **Thesis**: a posterior belief is the prior belief reweighted by how well each hypothesis predicts the evidence.
- **Mechanism**: posterior is proportional to prior times likelihood, then normalised. The classic trap is the screening-test paradox: when the condition is rare, even an accurate test yields mostly false positives, because the prior dominates. Work in natural frequencies (count people in each group) to avoid base-rate neglect.
- **Trade-off**: the answer is only as good as the prior and the likelihood model; an arbitrary prior can be disguised as a result.
- **Does not hold when**: the hypothesis space is poorly specified or evidence is not independent given the hypothesis (a common simplification).

## 2.3 A rating is not a rate: uncertainty about the long-run frequency
- **Thesis**: with few observations, the observed fraction is a weak estimate of the underlying success rate; a good decision accounts for how much data stands behind it.
- **Mechanism**: model each seller as having a hidden success rate; observed good and bad outcomes follow a binomial distribution given that rate. Treat the rate itself as unknown with a distribution over it ("probability of probabilities"), update by Bayes' rule. With a flat prior, the posterior mean has a simple form: pretend one extra good and one extra bad outcome were seen (the rule of succession). A perfect score on ten reviews then ranks below a slightly lower score on fifty; as data grows the pull of the prior fades.
- **Trade-off**: the answer depends on the goal (maximise the chance of a good experience, or be confident the rate exceeds a threshold, or explore); different goals give different rankings.
- **Does not hold when**: the rate drifts over time, reviews are fake or not independent, or a flat prior is unreasonable for the domain.

## 2.4 The binomial distribution
- **Thesis**: the number of successes in n independent trials with the same success rate has an exact formula.
- **Mechanism**: the probability of exactly k successes is the number of ways to choose which trials succeed, times the success rate to the k, times the failure rate to the n minus k. Simulating by random draws gives the same picture and is a good sanity check for any formula.
- **Trade-off**: tractable and exact; assumes independence and a constant rate.
- **Does not hold when**: trials influence each other or the rate changes.

## 2.5 The central limit theorem and the Gaussian
- **Thesis**: sums (and averages) of many independent contributions look Gaussian whatever the shape of the individual contributions, as long as variances are finite.
- **Mechanism**: the distribution of a sum is the convolution of the individual distributions; repeated convolution smooths any shape toward a bell curve whose width grows with the square root of the count. Consequences: errors of averages shrink like one over the square root of the sample size; adding two independent Gaussians gives a Gaussian with variances added.
- **Trade-off**: justifies Gaussian noise models and confidence intervals; convergence can be slow in the tails.
- **Does not hold when**: contributions are heavy-tailed (infinite variance), strongly dependent, or few; then rare extremes dominate and the bell curve underestimates risk.

## 2.6 Convolution: how to add random variables
- **Thesis**: the distribution of X plus Y is the convolution of their distributions; the same operation blurs images, adds echo to audio and powers convolutional layers.
- **Mechanism**: flip one function, slide it over the other, and at each offset take the overlap-weighted sum. Two ways to see it: as a grid of all pairs (x, y) summed along diagonals where x plus y is constant, and as a sliding window of weighted averages. The convolution of two boxes is a triangle, which already shows that it is not addition.
- **Trade-off**: a shared kernel gives translation-equivariance and few parameters (chapter 6); locality limits what one layer sees.
- **Does not hold when**: the effect depends on absolute position (then positional information must be added).

## 2.7 Reading statistics in practice
- **Thesis**: most statistical errors are about what was sampled and how, not about arithmetic.
- **Mechanism**: ask who or what is in the sample, whether the test set is separate from training, how many independent observations there are (not how many rows), and what decision the number feeds. A simulation is a cheap way to check a formula or to see how often a "surprising" result appears by chance.
- **Trade-off**: more care costs time; skipping it costs credibility.
- **Does not hold when**: the sample is the whole population and the question is descriptive.
