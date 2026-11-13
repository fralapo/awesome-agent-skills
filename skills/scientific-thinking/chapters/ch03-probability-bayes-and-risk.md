# Chapter 03: Probability, Bayes and Risk

## Core Idea
In this model, probability is a **language for updating beliefs under uncertainty** and for choosing under risk. Its two most useful lessons are that a prior matters as much as a test, and that evaluating a gamble one at a time can reverse the decision you would make across many repetitions.

## 3.1 Bayes' theorem and the base rate
- **Thesis**: the probability of a hypothesis given evidence depends on the prior probability, not only on the accuracy of the test.
- **Mechanism**: take a disease affecting 0.1% of people, with a test that catches 99% of cases and falsely flags 1% of healthy people. Test 1,000 people: about one is truly ill and is flagged; about ten healthy people are also flagged. A positive result then means about one chance in eleven, roughly 9%, not 99%. The formula is: posterior = prior x P(evidence given hypothesis) / P(evidence), where the denominator combines true and false positives. The intuitive answer confuses "the test is 99% accurate" with "99% of positives are real".
- **Trade-off**: the prior is often the hardest input and sometimes a guess; honest use shows how the conclusion changes across plausible priors.
- **Does not hold when**: the person tested was not drawn at random from the base population (for example they have symptoms or a risk factor); then the relevant prior is higher.

## 3.2 Repeated updating
- **Thesis**: Bayes' rule is meant to be applied repeatedly; each result becomes the next prior.
- **Mechanism**: a second, independent positive test moves the 9% to about 91%, still below the test's quoted accuracy. The original thought experiment was a repeated one: learning where a hidden object lies by being told, again and again, whether new random throws land to its left or right, narrowing without ever reaching certainty. The same logic filters spam: words in a message update the probability that it is junk.
- **Trade-off**: repeated updating assumes the pieces of evidence are independent; correlated tests (the same lab, the same biological confounder) count as less than separate ones.
- **Does not hold when**: evidence is not independent or the model of how it is generated is wrong.

## 3.3 Extreme priors cannot be moved
- **Thesis**: a prior of exactly 0 or 1 makes a person immune to evidence.
- **Mechanism**: if one person assigns 100% and another 0% to a proposition, no amount of data changes either of them. Debate between such positions is pointless as an attempt at persuasion. Practical use: when someone says "nothing could change my mind", you have found a prior of 0 or 1; do not expect evidence to work, and do not call the exchange a discussion of evidence.
- **Trade-off**: allowing yourself non-extreme priors feels less decisive.
- **Does not hold when**: the proposition is logically necessary or impossible.

## 3.4 The opposite trap: learning that nothing can change
- **Thesis**: updating on a history in which you never tried the alternative locks in a false certainty.
- **Mechanism**: a person who has seen the same discouraging outcome many times can internalise a near-zero prior that things could be different, like someone who sees the sun rise every day and becomes sure of the world's regularity. Outcomes, however, often depend on your own actions. If you never try something, you collect no data on it; the prior stays at zero because the evidence never arrives. A sound Bayesian therefore treats experimentation as how evidence is produced.
- **Trade-off**: experiments cost something and can fail.
- **Does not hold when**: the cost of an experiment is catastrophic or irreversible.

## 3.5 Expected value and loss aversion
- **Thesis**: people weigh a loss roughly twice as heavily as an equal gain, so they refuse positive-expectation bets.
- **Mechanism**: offered a coin flip that costs 10 if wrong and pays 10 if right, most decline (zero expected value). Even when the payoff for a win rises to 15 or 20 against a 10 loss, many still decline because the possible loss looms larger than the gain. Weight varies by person; some would want 100 against 10.
- **Trade-off**: loss aversion protects against ruin and keeps people from overconfident gambling, but costs money on genuinely favourable bets.
- **Does not hold when**: the loss would be ruinous (it cannot be absorbed) or the odds are not what is claimed; then declining is rational.

## 3.6 Repetition and aggregation
- **Thesis**: judged as one of a series, a favourable bet becomes safe.
- **Mechanism**: the same flip with a 20 gain and 10 loss repeated 100 times has an expected net gain of about 500 and roughly a one-in-2,300 chance of losing money at all, so even someone who weights losses twice as heavily should accept the series. The paradox is that the same person rejects the single bet. The remedy is to ask: "if I face this type of decision often, what policy do I want?" and to treat each choice as one draw from a portfolio.
- **Trade-off**: policy thinking assumes independence and enough repetitions; if each bet can wipe you out, the series never happens.
- **Does not hold when**: bets are correlated, stakes are large relative to your resources, or you cannot afford variance in the short run.

## 3.7 Substituting an easy question for a hard one
- **Thesis**: when the real question is hard, people answer a related easy one.
- **Mechanism**: ask someone how happy they are overall and the answer correlates weakly with how many dates they had last month; ask about dates first and the correlation jumps sharply, because the easy question has been substituted for the hard one. The same occurs with probability: "how likely is the disease?" is replaced by "how accurate is the test?". Name the hard question explicitly before answering.
- **Trade-off**: substitution is fast and often good enough.
- **Does not hold when**: the easy question really is a valid proxy for the hard one.

## Cross-references
Chapter 02 supplies significance and base-rate neglect in data; chapter 05 adds calibration; chapter 08 treats decisions where your choice interacts with others.
