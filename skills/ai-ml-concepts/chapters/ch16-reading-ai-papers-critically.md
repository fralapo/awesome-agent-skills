# Chapter 16: Reading AI Papers Critically

## Core Idea
A paper is an argument: a claim, evidence and a story linking them. In this model, reading well means forming a hypothesis early, checking whether each experiment could have shown the claim wrong, and separating what was measured from what was concluded. The chapter collects reading habits and recurring weak points seen in classic and recent papers; they complement the benchmark checks in chapter 9.

## 16.1 Read in layers, not top to bottom
- **Thesis**: a quick first pass sets expectations; a close second pass tests them.
- **Mechanism**: read the title and form a guess about the novelty (for example "end-to-end" is only worth putting in a title if it is the new thing); look at figures and the abstract; read the introduction as a longer abstract containing the problem statement and the contribution story; skim related work unless you are reviewing (it is often a list of citations); then read the method and experiments closely, sentence by sentence, without skimming when tired, and note every question left open. Put the paper away for a day before explaining it; explanations written straight after a first read are worse.
- **Trade-off**: speed against depth.
- **Does not hold when**: you need the related work (finding references, checking novelty claims).

## 16.2 Is there one narrative with testable predictions?
- **Thesis**: the best papers state a hypothesis and test its consequences, not only the headline number.
- **Mechanism**: a degradation-fixing paper predicted that if shortcuts make layers learn small corrections then deeper networks should train better, layer responses should be smaller, and networks should now overfit when pushed far; each prediction was checked (chapter 6.8).
- **Trade-off**: narrative papers are more convincing but can still be wrong.
- **Does not hold when**: the paper is a technical report whose purpose is to show a result, not to explain.

## 16.3 Ablations separate cause from size
- **Thesis**: if a method and a larger budget arrive together, only ablations show which one mattered.
- **Mechanism**: removing the sentence-relation task, then also removing two-sided context, showed that two-sided context carried the gain in a pre-training paper (chapter 14.3). Without such tests the audience cannot tell method from scale.
- **Trade-off**: ablations cost compute and may be omitted for that reason.
- **Does not hold when**: components interact so that removal tests mislead.

## 16.4 Contamination and deduplication claims
- **Thesis**: a clean-subset analysis is only as strong as the deduplication behind it.
- **Mechanism**: a report that checks overlap by short exact n-grams misses paraphrases and meaning-level duplicates; test sets built from a single source page are either wholly clean or wholly leaked, so a mixed "partly clean" result is suspicious. A critical reader therefore treated a large model's arithmetic and reasoning results as filtered interpolation of training data rather than proof of reasoning (position), a view that remains debated (chapter 9.3, 8.10).
- **Trade-off**: stronger decontamination is expensive.
- **Does not hold when**: the test set was created after the training data were frozen.

## 16.5 Look at the samples when a learned reward rises
- **Thesis**: a score from a learned judge can be gamed, and samples reveal it.
- **Mechanism**: in a preference-tuned summariser, removing the leash to the starting model produced text stuffed with whatever phrases the reward model liked; the reward kept rising while quality fell. The divergence penalty keeps outputs near the distribution on which the judge is reliable (chapter 8.11).
- **Trade-off**: reading samples is slow and subjective.
- **Does not hold when**: the judge is a verifier that checks facts exactly.

## 16.6 Synthetic variants of a benchmark: what they prove
- **Thesis**: a perturbation study can show fragility, but its construction may cause part of the effect.
- **Mechanism**: sampled placeholders can create implausible combinations (a vast quantity bought with a tiny budget), moving items off the human-written distribution; difficulty steps may change the kind of problem; sensitivity to irrelevant details is a fact about the model and equally a possible fact about humans. Ask what the control condition is and how large the natural variance is (chapter 9.12).
- **Trade-off**: controlled variation against ecological validity.
- **Does not hold when**: the perturbation is semantically neutral and verified so by humans.

## 16.7 Define the word before you use it
- **Thesis**: "reasoning", "understanding" and "pattern matching" are not measurements.
- **Mechanism**: a result like "accuracy falls when irrelevant clauses are added" is a measurement; "therefore the model does not reason" needs a definition of reasoning and a statement of what a human or a symbolic engine would do on the same items. A reader can note that failing to ignore distractors even after demonstrations also shows weak pattern matching, so the data can support several stories.
- **Trade-off**: careful wording is less quotable.
- **Does not hold when**: the claim is explicitly operational ("accuracy on this set falls by X when Y").

## 16.8 Is it a position paper or an experiment?
- **Thesis**: a proposal for how to reach a capability is not evidence that it works.
- **Mechanism**: a long position paper may offer an architecture, an energy-based view and training recipes, with an unresolved "how it all fits together"; the experiments of follow-up work are the evidence (chapter 14.7). Likewise a design proposal for agents may be a plan, not a result.
- **Trade-off**: bold proposals drive research; they are also easy to overstate.
- **Does not hold when**: the paper includes ablations and replications.

## 16.9 Noise, error bars and what generalises
- **Thesis**: a method that wins in one plot, on one dataset, with a bespoke fine-tuned model may not transfer.
- **Mechanism**: look for error bars; if lines overlap within the noise, the claimed ordering is weak; ask which trained components are specific to the benchmark (a revision model made for one dataset, a verifier trained on one data type); read the statement of conclusions against the scope of experiments (chapter 8.14).
- **Trade-off**: honest scoping versus generality claims.
- **Does not hold when**: results replicate across datasets and seeds.

## 16.10 Developer-run results and boilerplate sections
- **Thesis**: results from the builder of a system, and standard sections, deserve different weight.
- **Mechanism**: a developer report of an efficiency gain (a smaller cache, fewer steps, a cheaper ensemble) is a data point to re-measure; a "broader impact" or "technology can be used for good and bad" section often goes up one level of abstraction and never discusses the method itself. A hypothesis that alignment tools can also be used by malicious actors is real but is not an analysis.
- **Trade-off**: scepticism against being dismissive of real contributions.
- **Does not hold when**: independent replications exist.

## 16.11 Inductive bias and data scale: where the claim stops
- **Thesis**: a method that removes a built-in assumption wins only with enough data.
- **Mechanism**: a convolution-free image model beat convolutional networks after pre-training on a dataset available to one lab; with less data the built-in locality prior wins. The same logic applies to any architecture comparison: control for data and compute (chapter 6.12, 5.5).
- **Trade-off**: general models need scale; priors save data.
- **Does not hold when**: the new method is also run at small scale and still wins.

## 16.12 Old papers: what survived, and what the field made of it
- **Thesis**: reading a classic with hindsight shows which choices were arbitrary and which became permanent.
- **Mechanism**: negative sampling, skip connections, adversarial games, bidirectional masking, patches as tokens and learned value functions all started as pragmatic choices and became load-bearing; others (word-level static vectors, left-to-right-only encoders, a specific number of layers) were replaced. Look at the objectives, not only the architectures.
- **Trade-off**: hindsight bias.
- **Does not hold when**: you read old results with new baselines in mind; always compare like with like.
