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
