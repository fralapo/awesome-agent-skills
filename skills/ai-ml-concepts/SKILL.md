---
name: ai-ml-concepts
description: "Concepts behind AI and machine learning, from the maths to the frontier: linear algebra, calculus, probability, entropy; loss, gradient descent, backpropagation, double descent, regularization; dense, convolutional, residual and vision networks; transformers, attention, KV cache, state-space models; pre-training, preferences, group-relative RL, test-time search, scaling laws; generative models (diffusion, flow matching); self-supervised learning, world models; agents with memory, evaluation, security, token budgets; benchmarks and headlines; failure modes (hallucination, poisoning); safety, interpretability (circuits, sparse autoencoders, grokking); AI economics (capex, pricing, bubble tests); AI in learning and work (deskilling, verification); reading papers critically. Use when the user wants to understand, explain, judge or teach how a model works, why it fails, whether a benchmark, paper or AI claim holds, how to evaluate an agent, or what AI means for cost and skills. Separates mechanism from position."
allowed-tools:
  - Read
  - Grep
argument-hint: [concept, model behaviour, benchmark claim, or chapter number]
---

# AI and Machine Learning Concepts
**Chapters**: 18 | **Corpus**: ~130 theoretical transcripts | **Generated**: 2026-11-14

## Role and Boundaries

This skill **explains and evaluates**: how a model computes, why it learns or fails, what a benchmark or headline proves, and how to reason about limits and risks. It gives mechanisms, decision tables and checklists; the user owns the product, the data and the decision.

| This skill decides | This skill hands off |
|---|---|
| Which concept explains a behaviour; what a number or claim proves and does not prove; which failure mode fits a symptom | Designing the production system around a model (retrieval pipelines, agent loops, queues, caching, durable workflows) → `software-architecture`; day-to-day practice of coding with agents → `coding-with-agents` |
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
| Explain how a neural network or an LLM works from scratch | [ch04](chapters/ch04-learning-as-optimization.md) (4.10 perceptron to 4.16), [ch07](chapters/ch07-transformers-attention-and-fact-storage.md) | ch01 (maths), ch08 |
| "Why does X in the maths work?" (matrices, derivatives, chain rule, gradient) | [ch01](chapters/ch01-math-foundations-linear-algebra-calculus.md) | ch04 |
| Probability, Bayes, a rating with few reviews, why bell curves appear | [ch02](chapters/ch02-probability-bayes-and-distributions.md) | ch03 |
| Entropy, cross-entropy as loss, compression, error correction, Fourier | [ch03](chapters/ch03-information-entropy-and-signals.md) | ch08 |
| Overfitting, double descent, regularization, pruning, train/test discipline | [ch05](chapters/ch05-generalization-overfitting-and-regularization.md) | ch09 |
| Choose or explain an architecture (convolution, residual, autoencoder, vision transformer) | [ch06](chapters/ch06-network-architectures-convolution-and-autoencoders.md) | ch07, ch13 |
| Attention, embeddings, KV cache, where facts live, superposition | [ch07](chapters/ch07-transformers-attention-and-fact-storage.md) | ch11 |
| Image or video generation: adversarial, diffusion, flow matching, guidance | [ch13](chapters/ch13-generative-models-adversarial-diffusion-and-flow-matching.md) | ch06.5, ch14 |
| Self-supervised learning, embeddings, CLIP-style models, joint embedding, world models, robot policies | [ch14](chapters/ch14-self-supervised-learning-representations-and-world-models.md) | ch13, ch07 |
| Building or evaluating an agent: memory, files, search, simulation, red teaming, durability, agent security, token budgets | [ch15](chapters/ch15-agents-with-memory-evaluation-and-operations.md) | ch09, ch10 |
| "Is this paper's claim solid?" | [ch16](chapters/ch16-reading-ai-papers-critically.md) | ch09 |
| Pre-training, preferences, process rewards, group-relative RL, test-time search, scaling laws, fine-tuning vs retrieval, prompt practice | [ch08](chapters/ch08-llm-training-reasoning-and-scaling.md) | ch09, ch10 |
| "Is this benchmark or headline reliable?" Error analysis, one metric | [ch09](chapters/ch09-evaluating-models-benchmarks-and-headlines.md) | ch08.8, ch10, ch16 |
| Why a model fails (hallucination, reversal, arithmetic, gaming, sycophancy loop, grounded-answer errors, AI-text detectors) | [ch10](chapters/ch10-limits-and-failure-modes.md) | ch08, ch09 |
| Safety, alignment, control, interpretability (circuits, sparse autoencoders, grokking, subliminal learning, emergent misalignment, poisoning, steering), risk claims | [ch11](chapters/ch11-safety-alignment-control-and-interpretability.md) | ch10 |
| Research strategy, scaling debates, Monte Carlo, rendering, protein structure | [ch12](chapters/ch12-research-principles-and-scientific-applications.md) | ch06, ch03 |
| Cash flow, capex, data-centre spending, cost per user, pricing and subsidies, ads in answers, "is this a bubble?" tests | [ch17](chapters/ch17-economics-of-ai-capex-pricing-and-bubble-tests.md) | ch15 (15.19), ch08 (8.9) |
| Does AI make people less skilled? Learning, exams, verifying output, junior roles, AI in hiring, judgement as bottleneck | [ch18](chapters/ch18-ai-in-learning-assessment-and-professional-skill.md) | ch10, ch15 (15.20), ch12 (behaviour skill) |
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
16. **More parameters can generalise better, not only worse.** Past the interpolation threshold test error can fall again; measure effective complexity, not just size.
17. **Learning needs a path for the slope.** Smooth units, skip connections and exact backpropagated gradients are what let depth train.
18. **Representation learning must avoid the trivial answer.** Every label-free objective needs a guard against collapse, and the data selection is itself a hidden label.
19. **Generating is repeated small corrections.** Diffusion and flow models trade many steps for stability; guidance trades diversity for fidelity.
20. **An agent's memory is distilled, scoped and reconciled.** Keep logs, memories and specs separate, retrieve on purpose, and test the whole trajectory, not the last message.
21. **Read papers as arguments.** Ask what would have shown the claim wrong, then check samples, ablations, noise and definitions.
22. **Money shapes deployment.** Capital spending, unit cost and pricing decide which capabilities reach users; test bubble claims with falsifiers, not with enthusiasm or alarm.
23. **Skill needs practice and verification needs knowledge.** Delegating a step can erode the ability to judge it; keep practice where learning is the goal.

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
13. [Generative models: adversarial games, diffusion and flow matching](chapters/ch13-generative-models-adversarial-diffusion-and-flow-matching.md)
14. [Self-supervised learning, representations and world models](chapters/ch14-self-supervised-learning-representations-and-world-models.md)
15. [Agents with memory, evaluation and operations](chapters/ch15-agents-with-memory-evaluation-and-operations.md)
16. [Reading AI papers critically](chapters/ch16-reading-ai-papers-critically.md)
17. [Economics of AI: capex, pricing and bubble tests](chapters/ch17-economics-of-ai-capex-pricing-and-bubble-tests.md)
18. [AI in learning, assessment and professional skill](chapters/ch18-ai-in-learning-assessment-and-professional-skill.md)

## Topic Index

- **Activation functions (sigmoid, ReLU)** → ch04, ch07
- **Agent security, prompt injection, least privilege, token budgets, Jevons effect** → ch15 (15.18-15.19)
- **Agent evaluation, tracing, simulation sandboxes, red teaming** → ch15
- **Agent memory (semantic, episodic, procedural), CRUD, retrieval timing** → ch15
- **AND gate in a feed-forward block, fact storage** → ch07
- **Attention, queries/keys/values, masking, quadratic cost** → ch07
- **Autoencoders, sparse autoencoders, variational** → ch06, ch11
- **Autonomy ladder, durable execution, agentic search, files as memory, specs** → ch15
- **Backpropagation, chain rule, mini-batches** → ch04, ch01
- **Bayes' rule, base rates, rule of succession** → ch02
- **Benchmark contamination, item errors, format effects** → ch09
- **Blackmail scenarios, agentic misalignment** → ch11
- **Central limit theorem, Gaussian, convolution** → ch02, ch06
- **Chain of thought, self-consistency, test-time compute** → ch08
- **Contrastive learning, collapse, negative sampling** → ch14
- **Cross-entropy, entropy, KL divergence, compression** → ch03
- **Diffusion, guidance, flow matching, adversarial training, mode collapse** → ch13
- **Double descent, bias-variance** → ch05
- **Eigenvectors, determinant, matrix as transformation** → ch01
- **Error analysis, single-number metric** → ch09
- **Error-correcting (Hamming) codes** → ch03
- **Evaluation recipe, headline checklist** → ch09
- **Fourier and Laplace transforms** → ch03
- **Gradient descent, local minima, SGD** → ch04
- **Grokking, circuit tracing, sparse autoencoders, subliminal learning** → ch11
- **Group-relative policy optimisation, sharpening, pass at k** → ch08
- **Fine-tuning vs retrieval vs prompting, low-rank adapters** → ch08 (8.17)
- **Emergent misalignment, data poisoning, activation steering, refusal removal** → ch11 (11.16-11.18)
- **pass-at-k vs pass-to-the-k, reliability, cost-aware comparison, model judges** → ch09 (9.15-9.16)
- **Jagged capability, verifiability, circular benchmarks** → ch08 (8.18)
- **Retrieval-grounded answer errors, sycophancy loop, AI-text detectors** → ch10 (10.13-10.15)
- **Tokenizer, vocabulary trade-off, language token cost** → ch07 (7.15)
- **Prompt practice (few-shot, format, delimiters)** → ch08 (8.19)
- **Hallucination, reversal asymmetry, syntax over semantics** → ch10
- **Interpretability, round-trip translation of activations** → ch11
- **Joint embedding, world models, planning, robot policies** → ch14
- **KV cache, multi-query, grouped-query and latent attention, state-space models** → ch07
- **Monte Carlo, path tracing, next-event estimation** → ch12
- **Overfitting, L1/L2, pruning, inductive bias** → ch05
- **Perceptron, exclusive-or, least squares, universal approximation** → ch04
- **Preferences, process rewards, verifiable rewards** → ch08
- **Protein structure prediction, confidence** → ch12
- **Reading a paper, ablations, templated benchmarks, definitions** → ch16
- **Reasoning claims ("AI cannot reason")** → ch09, ch10
- **Residual connections, vision transformer, embeddings** → ch06
- **Scaling laws, data quality, domain specialisation** → ch08, ch05, ch09
- **Scaling-law theory, power laws** → ch08, ch12
- **Specification gaming, reward hacking** → ch10
- **Superposition, nearly orthogonal directions** → ch01, ch07, ch11
- **Test-time search (best-of-N, beam, revision)** → ch08
- **Tools vs unaided arithmetic** → ch08, ch10
- **Cash flow versus profit, depreciation of hardware, off-balance-sheet commitments** → ch17 (17.1-17.2)
- **Cost per user, heavy users, launch pricing, dependence and price rises** → ch17 (17.3-17.4)
- **Inference cost versus training cost, monetisation (ads, subscriptions, commerce)** → ch17 (17.5-17.6)
- **Running open-weight models, quantisation and implementation fidelity, gatekeeping** → ch17 (17.7-17.8)
- **Bubble criterion, falsifiers, energy per task** → ch17 (17.9-17.10)
- **Deskilling, delegation and skill atrophy** → ch18 (18.1)
- **Verification needs prior knowledge, productive friction** → ch18 (18.2-18.3)
- **Assessment redesign, oral and handwritten checks, writing as thinking** → ch18 (18.4-18.5)
- **Task exposure versus job loss, the junior pipeline question** → ch18 (18.6)
- **Judgement as bottleneck, AI in hiring screens, creative sparring** → ch18 (18.7-18.9)
