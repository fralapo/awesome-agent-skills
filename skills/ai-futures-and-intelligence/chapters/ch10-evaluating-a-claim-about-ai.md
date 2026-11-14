# Chapter 10: A Checklist for Evaluating a Claim About AI

## Core Idea
Most claims about AI are arguments with an unstated definition, an unstated measurement and an unstated time horizon. In this model, evaluating a claim means rewriting it as a *position*: statement, definition used, evidence offered, strongest counter-argument, what would make it false, and the date it was made. If you cannot fill all six fields, the claim is a slogan, not a finding. For benchmark and paper mechanics see `ai-ml-concepts` ch09 and ch16; this chapter adds the debate layer.

## 10.1 The six-field rewrite
| Field | Question | Failure sign |
|---|---|---|
| Statement | What exactly is asserted, for which system, task and population? | "AI can" with no system or task |
| Definition | Which meaning of intelligence, understanding, reasoning, AGI? | Word flips between senses |
| Evidence | A measurement, a mechanism, an analogy, or an intuition? | Evidence is an anecdote or a headline |
| Counter | What is the best opposing argument, in its own terms? | Only a caricature is answered |
| Falsifier | What observation would change the claimant's mind? | "Nothing could" |
| Date | When was it true, and what has changed since? | Undated figures or forecasts |

## 10.2 Questions by claim type
- **"The model is intelligent / generalises / reasons."** Which level of generalisation (ch02 2.1)? Could preparation (memorised templates, contamination) explain it? Does it survive renaming, rephrasing and changed parameters (ch02 2.7)? Is there a verifier, or only plausible-looking steps (ch02 2.6)? Is the score driven by memory capacity or by test-time search (ch03 3.2)?
- **"The model does not understand / cannot think."** Is the argument functional (tested failures) or philosophical (the Chinese room, grounding)? Does it survive the systems and grounding replies (ch04 4.1)? Does it predict something observable that the opposite view does not?
- **"Statistical models cannot do X."** Is X something that must be derived (ch03 3.4) or something verified by search? Is there a hybrid already doing X? Is the claim about the architecture or about current training?
- **"Scaling will (not) get us there."** Which input scales: parameters, data, compute at training, compute at inference? Is there a novelty-resistant benchmark that scales (ch03 3.2)? What is the bottleneck in the horizon (ch06 6.5)?
- **"The model is creative."** Is novelty measured against the training set or against what could have been aimed for? Is there an archive of stepping stones (ch05 5.5)? How much did a human selector contribute?
- **"The economy will do Y."** Share or size? Which tasks are complements? What reliability is needed? What do the elasticities look like (ch06 6.7)? Is the forecast aggregated, or one person's view?
- **"AGI by year Z."** Which missing capability is assumed to arrive? Which constraint is assumed away (ch08 8.9)? What does the date rest on?
- **"This is like [historical case]."** List the relations the analogy needs and where AI reverses one (ch09 9.8).

## 10.3 Separate three things that are often merged
1. *Mechanism*: what the system computes (testable now).
2. *Capability*: what it can do on a task (measurable, dated).
3. *Prediction*: what it will do or cause (a position; needs a date and a falsifier).
Do not let evidence for the first stand in for the third.

## 10.4 Tests that discriminate between rival readings
- **Variants test**: generate fresh, templated variants of a benchmark; memorisation collapses, real procedure does not.
- **Extrapolation test**: train or condition on a bounded range, test far outside it (lengths, magnitudes, new tokens).
- **Parameter-change test**: change a defining constant of the task; see whether anything learned transfers.
- **Verifier test**: if the output can be checked mechanically, measure verified accuracy, not fluency.
- **Representation test**: when two systems give the same outputs, inspect the internals before assuming equivalence.
- **Arithmetic test**: convert the economic or compute claim into gigawatts, chips, dollars and years.
- **Counterfactual-date test**: ask what would have to be seen within two years if the claim were true.

## 10.5 Dating and decay
- Mark every figure and forecast with the period of the claim; hardware prices, benchmark scores, capacity and model capabilities decay in months.
- When a source's number conflicts with another (for example, the share of capital spending on memory), report the range and say "unverified".
- A prediction without an end date is not testable.

## 10.6 Using sources that disagree
- Present each camp's thesis in its strongest form, then arguments for, arguments against and falsifier.
- Do not average positions; identify the premise on which they differ (definition, measurement, bottleneck, time horizon).
- Say what you do not know ("unverified", "general knowledge").

## 10.7 A short template for an answer
1. Restate the claim as a position, dated.
2. State the definition used.
3. Give the strongest argument for and against.
4. Name the falsifier.
5. Say which camp the evidence currently favours, how strongly, and why; mark anything not established as general knowledge.

## Checklist for this chapter
1. Can the claim be written in the six fields?
2. Is each part mechanism, capability or prediction?
3. Is there a test that separates the rival readings?
4. Are all figures dated and all forecasts "(position)"?
