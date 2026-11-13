---
name: ai-ml-concepts
description: "Concepts behind AI and machine learning, from the maths to the frontier: linear algebra and calculus, probability and Bayes' rule, distributions, convolution, entropy, cross-entropy and compression, error-correcting codes; loss, gradient descent, backpropagation, overfitting and regularization; dense, convolutional and autoencoder networks; transformers, attention, how facts are stored, superposition; pre-training, preferences, process rewards, reasoning, scaling; evaluating models and benchmarks (contamination, errors, how to read a headline); failure modes; safety, control and interpretability; rendering, Monte Carlo, learned simulators and protein structure. Use when the user wants to understand, explain, judge or teach how a model works, why it fails, whether a benchmark or AI claim holds, or how AI applies to science. Separates mechanism from position and says when each claim stops applying."
allowed-tools:
  - Read
  - Grep
argument-hint: [concept, model behaviour, benchmark claim, or chapter number]
---

# AI and Machine Learning Concepts
**Chapters**: 12 | **Corpus**: ~69 theoretical topics | **Generated**: 2026-11-13

## Role and Boundaries

This skill **explains and evaluates**: how a model computes, why it learns or fails, what a benchmark or headline proves, and how to reason about limits and risks. It gives mechanisms, decision tables and checklists; the user owns the product, the data and the decision.

| This skill decides | This skill hands off |
|---|---|
| Which concept explains a behaviour; what a number or claim proves and does not prove; which failure mode fits a symptom | Designing the production system around a model (retrieval pipelines, agent loops, queues, caching) → `software-architecture` |
| Whether an evaluation is sound (setup, contamination, item errors, best case vs worst case) | Writing, reviewing and testing code produced with agents → `coding-with-agents` |
| Safety, control and interpretability reasoning at the concept level | Legal, regulatory and compliance advice; clinical or biological protocols → specialist professionals |
| Teaching order and analogies for math and learning | Statistical analysis of a real dataset in code, charts → data skills; visual design of explanatory pages → design skills |

**Stay in lane.** This skill does not invent figures. Figures in the chapters are values reported at the time and are dated snapshots ("as reported at the time"); model families, leaderboards and prices change within months, so re-check before relying on them. Where a figure is a dated estimate or unclear, the chapter says so instead of guessing.

## Facts vs Positions

- **Mechanism / fact**: how matrix products, softmax, attention, backpropagation, cross-entropy or a Monte Carlo estimator work.
- **Reported result**: a number or finding from one study or one developer's report; useful, dated, not independently verified here.
- **Position**: written as "In this model..." or "(position)": for example "general methods that scale beat hand-built knowledge", "a benchmark is evidence, not a verdict", "tools beat unaided arithmetic".
- Every concept in the chapters has four fields: **Thesis**, **Mechanism**, **Trade-off**, **Does not hold when**. Use the last one before applying a rule: if the limit applies, drop the rule.

## How to Use This Skill

Diagnose before explaining: ask who the learner or decision-maker is, what they already know (derivatives? matrices? probability?), and what decision the explanation feeds.

| Task | Start with | Then |
|---|---|---|
| Explain how a neural network or an LLM works from scratch | [ch04](chapters/ch04-learning-as-optimization.md), [ch07](chapters/ch07-transformers-attention-and-fact-storage.md) | ch01 (maths), ch08 |
| "Why does X in the maths work?" (matrices, derivatives, chain rule, gradient) | [ch01](chapters/ch01-math-foundations-linear-algebra-calculus.md) | ch04 |
| Probability, Bayes, a rating with few reviews, why bell curves appear | [ch02](chapters/ch02-probability-bayes-and-distributions.md) | ch03 |
| Entropy, cross-entropy as loss, compression, error correction, Fourier | [ch03](chapters/ch03-information-entropy-and-signals.md) | ch08 |
| Overfitting, regularization, pruning, train/test discipline | [ch05](chapters/ch05-generalization-overfitting-and-regularization.md) | ch09 |
| Choose or explain an architecture (convolution, autoencoder, generator) | [ch06](chapters/ch06-network-architectures-convolution-and-autoencoders.md) | ch07 |
| Attention, embeddings, where facts live, superposition | [ch07](chapters/ch07-transformers-attention-and-fact-storage.md) | ch11 |
| Pre-training, preferences, process rewards, reasoning models, scaling | [ch08](chapters/ch08-llm-training-reasoning-and-scaling.md) | ch09, ch10 |
| "Is this benchmark or headline reliable?" | [ch09](chapters/ch09-evaluating-models-benchmarks-and-headlines.md) | ch08.8, ch10 |
| Why a model fails (hallucination, reversal, arithmetic, gaming) | [ch10](chapters/ch10-limits-and-failure-modes.md) | ch08, ch09 |
| Safety, alignment, control, interpretability, risk claims | [ch11](chapters/ch11-safety-alignment-control-and-interpretability.md) | ch10 |
| Research strategy, scaling debates, Monte Carlo, rendering, protein structure | [ch12](chapters/ch12-research-principles-and-scientific-applications.md) | ch06, ch03 |
| Quick lookup | [cheatsheet.md](cheatsheet.md), [patterns.md](patterns.md), [glossary.md](glossary.md) | |

## The Core Principles (recurrence order)

1. **A model is a function with adjustable numbers.** Learning is choosing them to make a cost small; everything else is detail.
2. **The gradient is the engine.** The chain rule makes it computable; smooth costs make it usable.
3. **Prediction is compression.** Lower cross-entropy is a better model of the data distribution, not necessarily a better assistant.
4. **Generalisation is the goal, training fit is the cost.** Hold data out; regularise; distrust a score you cannot separate from training.
5. **Structure in the architecture is a bet.** Convolutions bet on locality, attention bets on content-based routing; each bet has a price.
6. **Features overlap.** High dimensions allow many nearly independent directions, so neurons rarely map to single concepts.
7. **Signals shape behaviour.** Each training signal (next token, preference, verified answer, step label) teaches something and invites a matching failure.
8. **Process beats outcome where steps can be judged.** Rewarding good working locates mistakes; outcome rewards admit luck.
9. **Spend compute where it helps.** Thinking tokens, sampling, tools and retrieval beat forcing a first-token answer on hard questions.
10. **A benchmark is evidence, not a verdict.** Setup, contamination, item errors and the best case vs worst case decide what a number means.
11. **Specialisation breaks general rankings.** With heavy domain post-training, test on your own tasks.
12. **Optimisers exploit gaps.** What is written is optimised, not what is meant; monitor behaviour, not only objectives.
13. **Alignment, monitoring and containment are different layers.** Each weakens as autonomy and capability grow; report risks with calibrated language.
14. **Interpretation is a hypothesis.** Test it by intervention.
15. **Sampling estimates what cannot be solved exactly.** Know the variance, the missing-factor bugs and the rare-event blind spot.

## Chapter Index

1. [Math foundations: linear algebra and calculus](chapters/ch01-math-foundations-linear-algebra-calculus.md)
2. [Probability, Bayes' rule and distributions](chapters/ch02-probability-bayes-and-distributions.md)
3. [Information, entropy, compression and signals](chapters/ch03-information-entropy-and-signals.md)
4. [Learning as optimization](chapters/ch04-learning-as-optimization.md)
5. [Generalization, overfitting and regularization](chapters/ch05-generalization-overfitting-and-regularization.md)
6. [Network architectures: dense, convolutional, autoencoders, generators](chapters/ch06-network-architectures-convolution-and-autoencoders.md)
7. [Transformers, attention and how facts are stored](chapters/ch07-transformers-attention-and-fact-storage.md)
8. [How LLMs are trained, prompted and scaled](chapters/ch08-llm-training-reasoning-and-scaling.md)
9. [Evaluating models: benchmarks, defects, headlines](chapters/ch09-evaluating-models-benchmarks-and-headlines.md)
10. [Limits and failure modes](chapters/ch10-limits-and-failure-modes.md)
11. [Safety, alignment, control and interpretability](chapters/ch11-safety-alignment-control-and-interpretability.md)
12. [Research principles and scientific applications](chapters/ch12-research-principles-and-scientific-applications.md)

## Topic Index

- **Activation functions (sigmoid, ReLU)** → ch04, ch07
- **AND gate in a feed-forward block, fact storage** → ch07
- **Attention, queries/keys/values, masking, quadratic cost** → ch07
- **Autoencoders, sparse autoencoders, variational** → ch06, ch11
- **Backpropagation, chain rule, mini-batches** → ch04, ch01
- **Bayes' rule, base rates, rule of succession** → ch02
- **Benchmark contamination, item errors, format effects** → ch09
- **Blackmail scenarios, agentic misalignment** → ch11
- **Central limit theorem, Gaussian, convolution** → ch02, ch06
- **Chain of thought, self-consistency, test-time compute** → ch08
- **Cross-entropy, entropy, KL divergence, compression** → ch03
- **Eigenvectors, determinant, matrix as transformation** → ch01
- **Error-correcting (Hamming) codes** → ch03
- **Evaluation recipe, headline checklist** → ch09
- **Fourier and Laplace transforms** → ch03
- **Gradient descent, local minima, SGD** → ch04
- **Hallucination, reversal asymmetry, syntax over semantics** → ch10
- **Interpretability, round-trip translation of activations** → ch11
- **Monte Carlo, path tracing, next-event estimation** → ch12
- **Overfitting, L1/L2, pruning, inductive bias** → ch05
- **Preferences, process rewards, verifiable rewards** → ch08
- **Protein structure prediction, confidence** → ch12
- **Reasoning claims ("AI cannot reason")** → ch09, ch10
- **Scaling laws, data quality, domain specialisation** → ch08, ch05, ch09
- **Specification gaming, reward hacking** → ch10
- **Superposition, nearly orthogonal directions** → ch01, ch07, ch11
- **Tools vs unaided arithmetic** → ch08, ch10
