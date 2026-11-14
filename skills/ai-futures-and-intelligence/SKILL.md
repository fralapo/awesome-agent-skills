---
name: ai-futures-and-intelligence
description: "Analysis of debates about AI and intelligence, one thesis at a time with position, arguments for, arguments against and what would make it false: what intelligence is and how it is measured (adaptation to novelty, specialised vs general, collective), generalisation, abstraction and reasoning, limits of statistical models and symbolic, neurosymbolic and world-model hybrids, understanding and the Chinese room, creativity and open-ended search, compute, chips, memory and power as bottlenecks, inference arithmetic, AI economics and labour share, brains vs models, timelines, growth and intelligence-explosion scenarios, governance, cultural evolution and history as analogies, and a checklist for judging any claim about AI. Predictions are always dated positions. Use when the user compares schools of thought on AI, judges a claim about AGI, scaling, timelines, understanding, creativity or AI economics, or needs the strongest counterargument. For mechanisms and benchmarks see ai-ml-concepts."
allowed-tools:
  - Read
  - Grep
argument-hint: [claim, debate, bottleneck, forecast, or chapter number]
---

# AI Futures and Intelligence
**Chapters**: 10 | **Corpus**: ~29 theoretical transcripts | **Generated**: 2026-11-14

## Role and Boundaries

This skill **analyses debates**: what is being claimed, under which definition, on what evidence, against which counter-argument, and what observation would show it false. It separates mechanism (testable now), capability (measured and dated) and prediction (a position). It does not decide for the user which camp is right.

| This skill decides | This skill hands off |
|---|---|
| How to restate a claim as a dated position with a falsifier | How a model computes, trains, fails; how to read a benchmark or paper → `ai-ml-concepts` |
| Which definition of intelligence, reasoning or understanding a claim uses | Serving, quantisation, KV-cache and system design for LLM products → `software-architecture` |
| The strongest argument for and against each school (adaptation vs memory, hybrid vs scale, open-ended vs objective) | Agent engineering and verification when an agent writes code → `coding-with-agents` |
| Which physical or economic constraint is likely to bind (chips, memory, power, capital, reliability) | Investment, financial or legal advice; real-time market data |
| Which historical analogy fits and where it breaks | Predictions as facts; the skill gives none |

**Stay in lane.** Every thesis is a position, not a fact. Numbers (benchmark scores, hardware figures, prices, capacities) are dated snapshots from 2020-2026 and change quickly; re-check them. Items that could not be confirmed are marked "(unverified)"; background knowledge is marked "general knowledge".

## Facts vs Positions

- **Mechanism / fact**: how a roofline limit, a ReLU decision boundary, superposition, or a growth feedback loop works.
- **Position**: written "(position)": for example "intelligence is efficiency of skill acquisition", "scaling measures memory", "AI's share of the economy may fall as it improves".
- Every debate entry carries: **Position**, **For**, **Against**, **Falsified by**, and often **Does not hold when**. Use the last two before repeating a claim.
- **Predictions** are always "(position)" with a date; the chapter says when a figure is a snapshot.

## How to Use This Skill

| Task | Start with | Then |
|---|---|---|
| "What is intelligence? Is X intelligent?" | [ch01](chapters/ch01-what-intelligence-is-and-how-to-measure-it.md) | ch02, ch10 |
| Generalisation, abstraction, "can it reason?", chain of thought | [ch02](chapters/ch02-generalization-abstraction-and-reasoning.md) | ch03, ch10 |
| "Statistics cannot...", symbolic or hybrid proposals, world models | [ch03](chapters/ch03-limits-of-the-statistical-approach-and-symbolic-hybrid-positions.md) | ch02, ch07 |
| Chinese room, "does it understand?", consciousness, how to describe a model | [ch04](chapters/ch04-understanding-meaning-minds-and-how-to-talk-about-models.md) | ch01 |
| Is AI creative? Open-ended search, representations | [ch05](chapters/ch05-creativity-novelty-and-open-ended-search.md) | ch03 |
| Chips, memory, power, capex, share of GDP, labour | [ch06](chapters/ch06-compute-hardware-and-the-economics-of-ai.md) | ch07, ch08 |
| Inference cost, batching, in-context learning, superposition, brain vs model | [ch07](chapters/ch07-scaling-training-serving-and-what-models-do-inside.md) | ch06 |
| Timelines, intelligence explosion, growth, governance | [ch08](chapters/ch08-timelines-growth-scenarios-and-governance.md) | ch06, ch07, ch09 |
| Cultural evolution, history as analogy | [ch09](chapters/ch09-cultural-evolution-and-history-as-analogies.md) | ch08 |
| Judge any AI claim, compare sources that disagree | [ch10](chapters/ch10-evaluating-a-claim-about-ai.md) | cheatsheet, patterns |
| Quick lookup | [cheatsheet.md](cheatsheet.md), [patterns.md](patterns.md), [glossary.md](glossary.md) | |

## The Core Principles (recurrence order)

1. **Define before you argue.** The same word (intelligence, reasoning, understanding, AGI) has rival meanings; the definition decides the evidence.
2. **Skill is not generalisation.** Performance can be bought with data, compute or prior knowledge; ask how much was pre-loaded.
3. **A benchmark inherits human assumptions.** A test valid for people may be passable by preparation alone.
4. **Interpolation and composition are different abilities.** Ask which one the task requires and which one was shown.
5. **A generator needs a verifier.** Where a cheap check exists, fluent steps matter less than checked answers.
6. **Same output does not mean same inside.** Representations differ; look inside before assuming equivalence.
7. **Every claim has a falsifier.** If none can be named, treat it as a slogan.
8. **Bottlenecks move.** Name the binding constraint and its lead time for the horizon in question.
9. **Share is not size.** A technology can improve while its share of an economy falls.
10. **Reliability is a series of nines.** Partial success on each step multiplies into failure on long tasks.
11. **Analogies are positions.** List the relations they need and where they break.
12. **Forecasts are dated bets.** Mark the period, the assumed bottleneck and the observation that would change the number.

## Chapter Index

1. [What intelligence is and how it is measured](chapters/ch01-what-intelligence-is-and-how-to-measure-it.md)
2. [Generalisation, abstraction and reasoning](chapters/ch02-generalization-abstraction-and-reasoning.md)
3. [Limits of the statistical approach, and symbolic and hybrid positions](chapters/ch03-limits-of-the-statistical-approach-and-symbolic-hybrid-positions.md)
4. [Understanding, meaning, minds and how to talk about models](chapters/ch04-understanding-meaning-minds-and-how-to-talk-about-models.md)
5. [Creativity, novelty and open-ended search](chapters/ch05-creativity-novelty-and-open-ended-search.md)
6. [Compute, hardware and the economics of AI](chapters/ch06-compute-hardware-and-the-economics-of-ai.md)
7. [Scaling, training, serving, and models versus brains](chapters/ch07-scaling-training-serving-and-what-models-do-inside.md)
8. [Timelines, growth scenarios and governance](chapters/ch08-timelines-growth-scenarios-and-governance.md)
9. [Cultural evolution and technological history as analogies](chapters/ch09-cultural-evolution-and-history-as-analogies.md)
10. [A checklist for evaluating a claim about AI](chapters/ch10-evaluating-a-claim-about-ai.md)

## Topic Index

- **ARC-style novelty benchmark, memorisation resistance** → ch01 1.6, ch10
- **Abstraction as analogy; distance vs structure** → ch02 2.3
- **Algebraic generalisation, universally quantified mappings** → ch02 2.5, ch03 3.6
- **Anthropomorphism, simulator/mask description** → ch04 4.6
- **Batching economics, roofline, KV cache** → ch07 7.1-7.2
- **Bottleneck shifts (power, chips, memory, packaging)** → ch06 6.4-6.5
- **Chain of thought, self-consistency, verifiers** → ch02 2.6, ch03 3.10
- **Chinese room, computation and consciousness** → ch04 4.1-4.2
- **Collective brain, institutions and psychology** → ch09 9.1-9.3
- **Compute-based timelines, growth feedback, robot doubling** → ch08 8.1-8.3
- **Creativity, deception, novelty search, quality-diversity** → ch05
- **Extension vs intension** → ch02 2.4a
- **Fractured vs unified representations** → ch05 5.4
- **Hybrid and neurosymbolic systems; world models** → ch03 3.5-3.9
- **Intelligence explosion vs bottlenecks** → ch07 7.6, ch08 8.4
- **Few-atoms-of-meaning hypothesis; Platonism objection** → ch02 2.2, ch04 4.5
- **Labour share, reliability, structural change** → ch06 6.7
- **Memory crunch and consumer spillover** → ch06 6.4
- **Scaling laws as memory vs capability** → ch03 3.2
- **Superposition, underparameterisation** → ch07 7.5
- **Turing-completeness of language models** → ch03 3.7

## Related Skills

- `ai-ml-concepts`: mechanisms, training, benchmarks, failure modes, safety and how to read papers; this skill sits above it as the debate layer.
- `software-architecture`: serving models and building LLM products (memory, quantisation, retrieval, agents).
- `coding-with-agents`: how models behave while writing code and how to verify the result.

## Scope & Limits

Distilled from long-form discussions of the nature and measurement of intelligence, generalisation and abstraction, limits of statistical learning, symbolic and neurosymbolic proposals, understanding and consciousness arguments, open-ended search and creativity, semiconductor and data-centre economics, inference arithmetic, interpretability ideas, brain-versus-model comparisons, growth and automation economics, AI timelines, and cultural and technological history used as analogy. Not covered: model-training recipes, safety engineering, legal or regulatory detail, a detailed case for long timelines (only a marked general-knowledge outline), detailed accounting of any firm, and any real-time figures. Scores, prices, capacities and forecasts are snapshots; the skill gives no investment, policy or legal guidance.
