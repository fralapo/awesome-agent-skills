# Chapter 02: Statistics and Inference

## Core Idea
In this model, statistics is the discipline of **not being fooled by chance and by your own selection of what to look at**. Most numerical mistakes come from a few mechanisms: extremes regress, tests are run many times, correlation is read as cause, and a percentage is read without its denominator.

## 2.1 Regression to the mean
- **Thesis**: when an outcome is partly skill and partly luck, an extreme result is followed, on average, by a less extreme one, with no cause needed.
- **Mechanism**: imagine many people guessing true/false questions on a subject none of them knows. Scores cluster around 50% with random spread. Take the top group and test again: they fall back toward 50%. Take the bottom group: they rise. Nothing "evened out"; the extreme scores were extremes partly by luck, and luck does not repeat. With a real skill component the regression is smaller but still present. It differs from the gambler's fallacy: a fair coin does not "owe" you heads; rather, extreme runs are diluted by ordinary outcomes that are far more common.
- **Trade-off**: ignoring it makes any intervention aimed at extreme cases look effective.
- **Does not hold when**: the measurement is almost pure skill and almost noise-free, or you sample the whole population rather than the extremes. The effect is then small.

## 2.2 Why feedback gets misread
- **Thesis**: regression makes harsh feedback look useful and praise look harmful.
- **Mechanism**: in a classic story, flight instructors observed that after a very poor manoeuvre a reprimand was followed by improvement, while after an excellent manoeuvre praise was followed by a worse one. They concluded that criticism works and praise backfires. But the poor performance was partly bad luck and the excellent one partly good luck, so the next attempt would be closer to average either way. Controlled studies of feedback generally point the other way (positive feedback tends to be more effective than negative), although effects depend on the task, the person and the culture.
- **Trade-off**: a manager or teacher who learns from raw experience is systematically rewarded for being harsh.
- **Does not hold when**: a randomized comparison of feedback styles shows a real difference; then trust that, not the sequence of single cases.

## 2.3 Control groups drawn from the same population
- **Thesis**: any intervention applied to a selected extreme needs a comparison group selected the same way.
- **Mechanism**: a drug tried on the people with the worst blood pressure will show improvement at the second measurement even if inert, because stress, diet and measurement noise were all against them the first time. A speed camera placed where the previous year had many accidents will see accidents fall anyway, while sites with few accidents drift up, so the network total may not change. The comparison group, treated the same way except for the intervention, shows how much of the change was regression.
- **Trade-off**: control groups cost time and sample; sometimes ethics or logistics limit them.
- **Does not hold when**: the effect is so large and fast that no reasonable amount of regression could produce it.

## 2.4 What a p-value says and does not say
- **Thesis**: a p-value is the probability of data at least this extreme if the null hypothesis were true; it is not the probability that the hypothesis is true.
- **Mechanism**: a study found people could guess an image position slightly better than chance for one category (a 53% hit rate against 50%) with p around 0.01, and it appeared in a respected journal. The conventional threshold of 0.05 was an arbitrary convention. A significant p-value says the data would be surprising under "no effect"; whether "no effect" or "a real effect" is more plausible depends on prior plausibility (ch03) and on how many comparisons were tried (2.5). An astonishing claim with a small p-value still deserves doubt.
- **Trade-off**: the threshold gives a simple publication rule at the price of encouraging threshold-chasing.
- **Does not hold when**: used as one of several pieces of evidence, with effect size, intervals, pre-registration and replication; then it is useful.

## 2.5 Multiple comparisons and flexible analysis
- **Thesis**: the more things you measure or try, the more likely something crosses the significance bar by chance.
- **Mechanism**: a small study with a handful of people per group and many measured outcomes (weight, cholesterol, sleep quality, well-being and more) will usually show some "significant" difference. A deliberately rigged demonstration (the experiment was run as described but designed to maximise false positives) made precisely that point and was widely reported as a chocolate-diet finding. Related tricks include stopping data collection once p dips below 0.05, adding a second outcome variable, controlling for a covariate, or dropping a group; combining several of these can push the false positive rate above 60% even with the nominal 5% threshold. Give the same dataset to 29 analysis teams and conclusions ranged from no effect to about three times the odds, depending on defensible choices.
- **Trade-off**: some flexibility is legitimate because real data are messy; the cure is to declare the analysis plan in advance or treat results as exploratory.
- **Does not hold when**: the analysis is pre-specified, corrected for the number of tests, and confirmed on fresh data.

## 2.6 Correlation, variance explained and practical size
- **Thesis**: the correlation coefficient measures how tightly two variables move together; its square is the share of variance one explains.
- **Mechanism**: a coefficient near 0.5 means about a quarter of the variation is shared; 0.2 means about 4%. Coefficients of 0.2 to 0.8 appear in the intelligence-and-outcomes literature (ch11), and the same number can be impressive in one context (a large population-level health effect) and negligible for predicting an individual. A relationship can also be real but small, or large but caused by a third factor. Always ask about the variance left unexplained.
- **Trade-off**: reporting only correlation loses information about slope and shape; reporting only slope hides noise.
- **Does not hold when**: relationships are non-linear or restricted to a range; a single coefficient can mislead.

## 2.7 Proportional reasoning: read the table, not the largest cell
- **Thesis**: a two-by-two table must be read in proportions.
- **Mechanism**: in a fictional skin-cream trial, the largest number was in the "cream and improved" cell, suggesting benefit. But among cream users about three times as many improved as worsened, while among non-users about five times as many improved as worsened, so the cream did worse than nothing. The quick answer is to compare raw counts; the correct one is to compare ratios within each row. The same structure appears in any treatment-versus-control report where group sizes differ.
- **Trade-off**: proportional reasoning needs a few seconds of effort; that effort is the fix.
- **Does not hold when**: the groups are of identical size, in which case counts and proportions agree.

## 2.8 Reading a result requires the denominator and the comparison
- **Thesis**: a statistic is meaningful only with its base population and its comparison.
- **Mechanism**: two agencies reported opposite crime trends in the same period because one counted only reported incidents including fatal crimes and the other used a survey that includes unreported but excludes fatal ones. Different definitions answer different questions. Similarly, "headline rate went up" may reflect better measurement.
- **Trade-off**: checking definitions takes time; most disputes between numbers are definitional.
- **Does not hold when**: both sources use the same documented method.

## Cross-references
Chapter 03 adds base rates and updating. Chapter 06 covers how these errors reach print. Chapter 12 turns them into a checklist.
