# Chapter 9: Evaluating Models: Benchmarks, Their Defects and How to Read a Headline

## Core Idea
A benchmark number is a measurement of a model under one setup on one set of items; it is evidence, not a verdict. In this model, evaluate a claim by asking what was measured, how the setup shaped the number, whether the items were seen in training, whether the items themselves are correct, and what the result does and does not demonstrate.

## 9.1 What a score is
- **Thesis**: a score is a function of the model, the prompt format, the grader, the sampling method and the item set.
- **Mechanism**: changing any of these moves the number. A well-known multiple-choice knowledge test was reported to rise by roughly two points (from the mid-80s to the high-80s percent, as reported at the time) simply by letting the model reason before answering and by majority vote over several samples, rather than forcing an immediate single-letter answer.
- **Trade-off**: tuned setups reveal capability; standard setups allow comparison.
- **Does not hold when**: the comparison mixes setups (one model with a scratchpad, another without).

## 9.2 Format shortcuts and encoding effects
- **Thesis**: models exploit any regularity that raises the score, including ones the designers did not intend.
- **Mechanism**: in multiple choice, an option such as "zero" can flag a trick question; moving to open-ended answers with a blind grader against a hidden reference reduced one private common-sense benchmark by about fifteen to twenty points (reported by its maintainer), yet scores stayed well above chance. In an abstract grid-puzzle test, changing colour numbers to other symbols lowered accuracy, because numbers allowed accidental arithmetic patterns.
- **Trade-off**: harder formats are closer to real use but noisier and slower to grade.
- **Does not hold when**: the multiple-choice cues are absent by design.

## 9.3 Contamination and memorisation
- **Thesis**: when benchmark items and answers appear in training data, the score may measure recall.
- **Mechanism**: problems and solutions circulate online; filtering training data against the test is imperfect (near-duplicates and paraphrases slip through). Hence the value of private or newly written items, held-out dates, and tests whose answers cannot have been seen. Even private sets are exposed once they are used repeatedly through an API.
- **Trade-off**: fresh tests are costly to create and eventually become stale.
- **Does not hold when**: the model's training data is verifiably disjoint from the test.

## 9.4 Errors inside benchmarks
- **Thesis**: a benchmark is itself a human artefact with mistakes, and differences between top models may be smaller than the benchmark's error rate.
- **Mechanism**: independent re-grading found questions with missing statements (the answer options referred to statements that were never pasted), factual errors, wrong keys and wrong sources, in subjects such as ethics, psychology, economics, law and accounting; at least dozens and plausibly hundreds of items were affected, enough to move scores by up to about two percent (as claimed by the re-graders, reviewed with some of the test's authors). Automatic exact-match grading would silently mark many unusual answers wrong. Leaderboards separating models by a tenth of a percent are measuring noise.
- **Trade-off**: human grading is slow and expensive.
- **Does not hold when**: items are verified by experts and the answer key is audited.

## 9.5 Saturation and the end of general ranking
- **Thesis**: once top models are near the ceiling or near the label-noise floor, the benchmark no longer discriminates.
- **Mechanism**: a score above the "human expert" line on a test with errors cannot be interpreted; the ceiling is below 100 percent.
- **Trade-off**: harder replacement tests are needed regularly.
- **Does not hold when**: models are still far from the ceiling.

## 9.6 Domain specialisation and the "vibe era"
- **Thesis**: with large post-training in specific domains, a model that wins one benchmark may lose another, so a single "best model" ranking is unstable.
- **Mechanism**: a newer model from a family can score lower on a chess-puzzle test than its predecessor while winning coding tests; a model that tops puzzle and science benchmarks can trail on broad tests of expert office tasks. Users' experience then depends on how close their task is to the post-training domains, which is why impressions on social media contradict each other.
- **Trade-off**: personal evaluation on your own tasks is the best predictor but takes work.
- **Does not hold when**: the model is a general-purpose system trained evenly, as earlier generations roughly were.

## 9.7 Best case versus worst case: hallucination metrics
- **Thesis**: a model's strongest answers say little about its weakest; hallucination is a property of the worst moments.
- **Mechanism**: useful indexes split incorrect answers into hallucinated answers and abstentions, and penalise wrong answers; two models with similar accuracy differ in whether they admit ignorance. A system can improve at its best and get worse at its worst in the same release (for example, a higher rate of fabricated outputs, or a weaker refusal of risky actions, reported together with a strong headline result).
- **Trade-off**: more abstention lowers coverage.
- **Does not hold when**: every answer is checked anyway and wrong answers are cheap.

## 9.8 Expert-judged task studies
- **Thesis**: tests of professional deliverables, graded by experts against human experts, are closer to work than exam questions but have their own caveats.
- **Mechanism**: tasks written by practitioners with years of experience; a win rate is the share of comparisons in which a grader prefers the model output. Reported patterns: win rates depend on file type (documents, slides, spreadsheets); a weaker model can slow experts down because reviewing costs time; a stronger one can speed them up; a lab publishing results where a rival model ranks first is a credibility signal.
- **Trade-off**: the "quality bar" is set by human graders who may miss subtle errors; self-reported productivity can diverge from measured productivity (a controlled study of developers found people believed they were faster while measured time went up).
- **Does not hold when**: tasks are long-horizon, require follow-up, or involve accountability.

## 9.9 Reading a headline: nine questions
- **Thesis**: before accepting "AI achieves X", check what X proves and what it does not.
- **Mechanism**: (1) Is the test human-designed with known answers, or research with unknown answers? A gold-level result on competition problems shows strength on problems experts wrote; research is about problems nobody knows how to solve. (2) Is it a lead over rivals, and have rivals reported? (3) Was a specialised system used, or general training? A general model matching a specialised one is the news. (4) Which hardest item failed? (5) Do other measurements of the same system (hallucination, refusals, honesty about tool use) move in the wrong direction? (6) Is the result from a released product or an internal model? (7) Does the jump generalise to different tasks or only to this family? (8) Who benefits from the announcement and when was it timed? (9) What is the base rate of such claims proving durable?
- **Trade-off**: skepticism costs time and can slide into denial; the symmetric error (dismissing a real advance) is as costly.
- **Does not hold when**: you can inspect the full method, data and failures yourself.

## 9.10 Reading "AI cannot reason" headlines
- **Thesis**: a failure on a puzzle at high complexity does not by itself show absence of reasoning.
- **Mechanism**: language models are probabilistic, not pre-programmed algorithms; they fail at exact long computation without tools, which has been known for years. In one widely shared study, accuracy on puzzles with growing numbers of pieces collapsed, but critics noted that the required output exceeded the model's token limit, that the models sometimes responded with the algorithm rather than the move list, and that thinking models still outperformed non-thinking ones at equal budgets. The balanced reading: models do not run exact procedures reliably, and they do solve many reasoning problems; both statements are true.
- **Trade-off**: design the test to separate reasoning from execution, length and format.
- **Does not hold when**: the puzzle is within the output budget and the tools are matched to the question.

## 9.11 Practical evaluation recipe
- **Thesis**: build a small private evaluation tied to your decisions.
- **Mechanism**: collect real tasks; write the correct answers and the failure cases in advance; fix the prompt format; run several samples; grade blind (human or a separate model checked against humans); report intervals; re-run when the model version changes; keep items out of public view.
- **Trade-off**: maintenance effort.
- **Does not hold when**: the use case is one-off.

## 9.12 Templated variants: testing robustness and contamination at once
- **Thesis**: turning each benchmark item into a template with placeholders (names, numbers, ranges) lets you measure how fragile a score is, but the template itself can add confounds.
- **Mechanism**: sample many variants of the same problem. In one study changing only names barely changed accuracy while changing numbers lowered it and widened the spread across variants; adding clauses made problems harder in steps (one fewer condition, one more, two more) and accuracy fell with each; appending an irrelevant clause that seems relevant caused large drops even after several demonstrations of ignoring such clauses. The authors concluded the models pattern-match rather than reason and that the original set was probably contaminated.
- **Trade-off**: exposes brittleness and memorisation; synthetic sampling can generate implausible scenarios (a huge number of items for a small purchase) that lie outside the human-written distribution models know, so part of the drop may reflect distribution shift; "two clauses harder" can mean a different kind of problem rather than twice as hard; and humans would also fail under time pressure on the hardest variants (position of a critical reader).
- **Does not hold when**: used as a verdict on "reasoning" without defining it (chapter 9.10, 16.7).

## 9.13 Error analysis: count the categories, read off the ceiling
- **Thesis**: before spending months on a fix, tally what the errors actually are.
- **Mechanism**: take about a hundred misclassified development examples and put them in a spreadsheet with a column per suspected cause (for example one animal confused for another, blurry images, filters), adding columns as new causes appear. If a cause accounts for 5 percent of errors, perfect handling lowers a 10 percent error to 9.5 percent (a ceiling); if it accounts for 50 percent, the ceiling is 5 percent. A few hours of counting can decide where to invest.
- **Trade-off**: cheap and decisive against a small sample and subjective categories; it gives priorities, not a formula.
- **Does not hold when**: errors interact (fixing one exposes another) or the labels themselves are wrong, which needs a separate check.

## 9.14 One number for iteration, several numbers for constraints
- **Thesis**: day-to-day model comparison needs a single real-valued metric; secondary needs become constraints.
- **Mechanism**: precision (of items called positive, how many are) and recall (of true positives, how many were found) trade off, so two models can each win on one; a combination such as the harmonic mean (F1) allows an immediate ranking, and an average across regions turns four error numbers into one. Dozens of experiments can then be sorted quickly.
- **Trade-off**: speed against hiding what matters; choose the single metric to reflect the real goal and add hard thresholds (latency, per-group floor) as constraints.
- **Does not hold when**: the single number is optimised until the model overfits it (chapter 15.10).

## 9.15 Reliability metrics: pass-at-k versus pass-to-the-k
- **Thesis**: "can it ever solve this?" and "does it solve this every time?" are different questions with different metrics.
- **Mechanism**: pass-at-k counts a task as solved if any of k attempts succeeds, which measures capability with retries and rises with k. Pass-to-the-k counts it only if all k attempts succeed, which measures reliability and falls as k grows. If one attempt succeeds with probability p, all k succeed with probability p to the power k, so a model at 90% per attempt is at about 59% over five required successes (arithmetic, not a measured result). Agentic tasks are repeated in production, so the second metric is the one customers feel. Accuracy tends to improve faster than reliability.
- **Trade-off**: the strict metric needs many runs per task and punishes rare failures heavily.
- **Does not hold when**: a verifier picks the winner among attempts and a failed attempt costs nothing.

## 9.16 Comparing models fairly: setup, effort, cost and judges
- **Thesis**: a leaderboard row is a setup, not a model; compare cost to reach a result, not list price.
- **Mechanism**: tables mix different numbers of attempts, example shots and reasoning effort ("table crimes"); more effort does not always help (a medium setting sometimes matches or beats the maximum); two models with the same list price can use very different numbers of reasoning tokens, so cost per solved task is the figure to compare. Arenas (people choose between two anonymous answers, scores computed like chess ratings) are closer to real preferences but less controlled than fixed datasets; model judges favour outputs in their own style. Fixing errors in a dataset has reordered published rankings. A third-party evaluator is a reasonable prior; a small private benchmark of your real task (define task and metric, build new realistic items, run through one API gateway with automatic or judged grading, analyse errors, cost and time, iterate) is better, and cheap (a reported order of magnitude: tens of dollars).
- **Trade-off**: private benchmarks cost effort and go stale with each model version.
- **Does not hold when**: the choice is low-stakes and reversible.
