# Chapter 01: Clinical Reasoning and Evidence

> Educational, not medical advice. This chapter explains how probability and test accuracy work so that a claim can be judged. It does not diagnose anything and cannot replace an assessment by a qualified clinician.

## Core Idea
In this model a diagnosis is not a verdict produced by one test. It is a **probability that is revised in steps**: what is common in this kind of person (base rate), what the history adds, and only last what a test adds. A test is useful only if its result can move the probability across a decision threshold.

## 1.1 Diagnosis as a filter
- **Thesis**: the diagnostic process works as a sequence of filters that remove hypotheses until one main hypothesis (and perhaps one weaker rival) remains.
- **Mechanism**: step 1, epidemiology (some conditions are almost confined to a type of person: one tendon problem is typical of young people who jump, another of older sedentary women). Step 2, the questions asked in the history make a hypothesis more or less likely (an audible pop, immediate swelling and a pivoting mechanism raise the chance of a ligament tear far more than any later manoeuvre). Step 3, one or two tests of at least moderate accuracy are used to push the estimate up or down.
- **Trade-off**: a clinician who needs five different tests for five different hypotheses has filtered too late; the fix is knowledge of base rates and symptom patterns, not more tests.
- **Does not hold when**: the suspected condition is serious and must be excluded even if unlikely; then screening continues at low probability (see ch03 on red flags).

## 1.2 Pre-test probability and when a test adds little
- **Thesis (position, rule of thumb)**: if the estimate is already very high (roughly 80% or more) or very low (roughly 20% or less), special tests add little and may be skipped.
- **Mechanism**: a result changes the probability by a bounded amount; near the extremes the posterior cannot move across a decision line, so the test cannot change management.
- **Trade-off**: skipping tests saves time and avoids false alarms; but the thresholds are rules of thumb and depend on the cost of being wrong.
- **Does not hold when**: the cost of a miss is high (serious pathology), so the "low" threshold must be much lower; or when the exam is also used to reassure or build trust (a patient who expected a hands-on exam may feel dismissed without one, even if it has no diagnostic value).

## 1.3 Sensitivity and specificity
- **Thesis**: sensitivity is the share of people who truly have the condition that a test flags; specificity is the share of people without it that the test correctly clears. They describe the test, not the patient.
- **Mechanism**: four cells (true positive, false positive, true negative, false negative). A highly sensitive test produces few false negatives, so a negative result **rules out** (mnemonic: SnNout). A highly specific test produces few false positives, so a positive result **rules in** (SpPin). The trade-off between the two is built in: a test that flags everybody is perfectly sensitive and useless.
- **Worked example (one dated review, context-bound)**: for suspected lumbosacral nerve-root pain, a raised-leg test had high sensitivity and low specificity (about 92% and 28%) while the crossed version had the reverse (about 28% and 90%). Reading: use the sensitive test to try to rule out; use the specific one to try to rule in.
- **Trade-off**: both numbers come from studies with their own populations; moving the test to a different setting changes the numbers.
- **Does not hold when**: the reference standard used in the accuracy study was itself weak. Sensitivity and specificity are then estimates of agreement with a poor yardstick.

## 1.4 Likelihood ratios
- **Thesis**: likelihood ratios (LR) condense sensitivity and specificity into how much a result changes the odds.
- **Mechanism**: LR+ = sensitivity / (1 - specificity); LR- = (1 - sensitivity) / specificity. Convention: LR+ above about 10 is strong evidence to rule in; LR- below about 0.1 is strong evidence to rule out; values near 1 mean the test does almost nothing. To apply: pre-test probability -> odds (p / (1 - p)) -> multiply by LR -> convert back to probability (odds / (odds + 1)). A probability nomogram does the same graphically.
- **Worked example (illustrative figures)**: base rate in a general practice population about 5%; history and screening raise the estimate to about 60% (odds 1.5). A test with sensitivity 85% and specificity 94% has LR+ about 14 and LR- about 0.16. Positive result: odds 1.5 x 14 = 21, probability about 95%. Negative result: odds 1.5 x 0.16 = 0.24, probability about 19%. The same test applied at a 5% pre-test estimate rises to about 42%, probably still below a decision threshold, which is the point of using the base rate.
- **Trade-off**: the arithmetic is exact but the inputs (the pre-test estimate and the LR) are uncertain, so the output looks more precise than it is.
- **Does not hold when**: tests are used in sequence as if independent (they usually are not; use clusters, 1.5).

## 1.5 Special tests: why most are not so special
- **Thesis**: in the databases that grade orthopaedic tests, about two thirds are rated weak or unknown as standalone tests; only a small share (single digits of percent in two reviews) rate as strong. Treat the figures as dated snapshots.
- **Mechanism**: (a) low specificity to the structure: in a common shoulder test, several other muscles are about as active as the one the test is named after, so pain provoked does not say which tissue hurts; (b) many tests have never been checked for reliability or accuracy; (c) accuracy studies carry a high risk of bias (weak reference standard, retrospective design); (d) a test gives a signal about provoked pain, which is not the same as a structural diagnosis.
- **What follows**: use **clusters** of tests rather than single tests, and only after the history has narrowed the field. Self-diagnosis from a handful of tests found online is not valid for the same reasons.
- **Counter-argument (position)**: even a test with weak accuracy can have value as a way to reproduce a patient's symptom, to check that a movement is tolerated, or to inform the patient; the objection is to using it as proof of a structure.
- **Does not hold when**: a test is both highly specific and based on a well-defined sign (a few remain strong) or the test is a screening step for something serious.

## 1.6 Reading research
- **Thesis**: reading only the abstract is the most common way to be misled; the abstract is a trailer.
- **Mechanism**: because of publication bias and competition for impact, abstracts tend to amplify positive findings; methods and results sometimes do not match the claim. Look for sample size, comparison group, who was measured, outcome chosen, and the size (not only the existence) of the effect.
- **Statistical vs clinical significance**: a small effect can be "significant" in a large sample but not matter to a person; a large effect can be missed in a small sample. A p-value is a yes/no test of a hypothesis; clinical relevance is judged against a minimum meaningful difference.
- **Contested (position)**: some argue that p-values should be abandoned; others (and this model, cautiously) keep them as one clear check while adding effect sizes and intervals. Alternative magnitude-based inference approaches have been criticised as weaker than once thought.
- **Small in-house data**: simple averages and honest figures from a small group can be useful, but they are not controlled evidence.
- **Prediction**: individual injury prediction is not in reach; machine-learning on large datasets can identify risk factors, which is a lesser claim.
- **Does not hold when**: the article is a guideline or a systematic review, where the abstract is a more reliable summary, but it should still be checked against the methods.

## 1.7 Association is not causation
- **Thesis**: an association between a finding and pain (a posture, a muscle pattern, an MRI feature) says nothing about direction.
- **Mechanism**: group A (pain) differs from group B (no pain) on whatever the lab can measure; the difference may be an effect of the pain (people move differently when they hurt), a bystander, or a cause. Only prospective designs can address cause, and even then confounding remains.
- **Does not hold when**: a mechanism is both well established and supported by experiments (for example an acute overload).

See ch05 for load and tissue capacity, ch08 for imaging findings, ch09 for posture claims, ch10 for a checklist.
