# Chapter 2: Generalisation, Abstraction and Reasoning

## Core Idea
In this model, generalisation is what separates a capability from a lookup, and abstraction is the engine that produces it. The debate is over *what kind* of abstraction current systems form: smooth, distance-based abstractions (interpolation) or discrete, structure-based ones (composition). Reasoning is then discussed as a mix of both. Each section marks positions and counter-positions; mechanisms are separated from interpretation. Basic learning theory is in `ai-ml-concepts` ch05; this chapter is the debate layer above it.

## 2.1 A spectrum of generalisation (position)
- **Position**: generalisation comes in levels. (a) None: a fixed task with no novelty (a chess engine). (b) Local: adaptation within a known domain of tasks (recognising cats in new poses and lighting). (c) Broad: adaptation to unknown unknowns inside a known but wide domain. (d) Extreme: open-ended adaptation across domains, as general intelligence would require.
- **Mechanism**: most machine learning sits at (b); the question is whether very large language models have reached (c) because the task is specified at test time in the prompt.
- **Against the position**: critics of the position say that what the model "knows" at test time was acquired in training, so the prompt only selects among learned functions; defenders say the number of selectable functions is so large that (b) and (c) blur.
- **Falsified by**: a model that, on tasks provably outside its training distribution and unfamiliar in structure, adapts with a handful of examples at human-like efficiency.

## 2.2 The few-atoms-of-meaning hypothesis (position)
- **Position**: the world looks infinitely novel but is made of repetitions and compositions of a few "atoms of meaning". Intelligence mines experience for those atoms (abstractions) and recombines them to model new situations.
- **Mechanism**: two cooperating processes. *Abstraction generation* distils experience into reusable building blocks (patterns, templates, programs, representations). *Synthesis* assembles blocks on the fly into a model of the current situation. Together: learn blocks slowly, compose them quickly.
- **For**: it explains why analogies work, why few examples suffice for humans, and why compositionality matters.
- **Against**: a philosopher's objection is that this is a Platonic picture: a messy world of appearances over a neat, decomposable reality. Science often justifies mathematical representations this way even when they depart from known facts of the concrete system. Models are useful idealisations, not necessarily the real structure.
- **Falsified by**: a domain where no small library of reusable blocks reaches good prediction, or where the best blocks keep growing with each new case.
- **Does not hold when**: the domain is genuinely irregular (one-off historical events, ephemeral social facts).

## 2.3 Two ways to compare things: geometry and structure (position)
- **Position**: all abstraction is born from analogy, and there are two ways to compare two things. (1) By *distance*: points in a space, similarity as closeness, abstractions as templates or cluster centres; this yields perception, intuition and "type 1" thinking and is what deep learning does well. (2) By *exact structure*: sub-graph matching, identical or contained structure; this yields discrete, step-by-step reasoning and "type 2" thinking, which is what program synthesis and symbolic systems do.
- **Mechanism**: real thinking stacks both. A person checking a proof writes discrete steps but is guided by interpolative intuition about where to go; a person looking at an object does compositional matching hidden inside perception. A person solving a puzzle examines two to four hypotheses out of hundreds of thousands; intuition prunes, discrete evaluation checks.
- **Trade-off**: geometric abstraction is cheap, smooth and needs dense samples; structural abstraction is exact, data-efficient and costs combinatorial search.
- **Against the dichotomy**: it may be an artefact; a sufficiently large network could implement both inside one continuous substrate. In this model that is an open question.
- **Falsified by**: a purely continuous model that robustly learns discrete algorithms (sorting, arithmetic of arbitrary length) from examples and applies them off-distribution.

## 2.4 Interpolation versus extrapolation (mechanism + position)
- **Mechanism**: natural data is said to lie on low-dimensional manifolds in embedding space; a classifier untangles manifolds. Neural networks generalise by interpolating on a learnable manifold; where the target is discrete or has jumps, no smooth learnable manifold exists and gradient descent falls back on memorising. The manifold also has to be densely covered by examples.
- **A geometric picture (position)**: a network of piecewise-linear units carves the input space into polyhedra with flat hyperplanes; any smooth behaviour arises from many pieces. Each region is a local linear rule. The number of addressable regions grows exponentially with units, which explains storage capacity, and the same picture explains why extending a pattern beyond the region covered by examples is not guaranteed. Smooth non-linearity usually enters through human feature engineering done before the data reaches the network, so "no feature engineering needed" is overstated.
- **Counter**: scale changes what counts as "outside the data"; with enough diverse data, many practical inputs are inside the hull; and deep networks do compose layers, so the picture undersells structure that is learned in depth.
- **Does not hold when**: the question is about training with strong inductive bias (convolutions, symmetries), where the extrapolation is built in by design.

## 2.4a Extension versus intension (mechanism)
- **Thesis**: a model can learn the *values* of a function (the extension) without the *rule* that generates them (the intension).
- **Mechanism**: a transform whose matrix of coefficients is known can be learned by optimising a random matrix against the true values; the optimiser converges to the right numbers, yet nothing it learned helps if one parameter of the formula changes by one, because the generating rule was never represented. This is the case for "fish versus how to fish".
- **Use**: when someone says a network "learned" a procedure, ask whether the result transfers when a defining parameter changes.
- **Does not hold when**: the network is trained on the family of parameters, in which case transfer is exactly what is learned.

## 2.5 Abstraction as extrapolation beyond the training space (position)
- **Position**: the cleanest test of abstraction is a one-to-one mapping learned on some inputs and applied outside their range: identity on even numbers then odd numbers; "add a suffix" to a new stem; recognising a pattern like A-B-A versus A-A-B over entirely new tokens. Infants as young as seven months generalise such patterns to new items, an effect that has replicated.
- **Mechanism**: a universally quantified mapping (every input gets its own output by the same rule) is trivial for a variable-based system and hard for a system that only encodes the training distribution.
- **For**: it isolates abstraction from memory, using simple, controlled cases.
- **Against**: large networks do succeed on many such tests when the training data covers enough variety; and humans also fail some abstract tasks.
- **Falsified by**: a network trained only on a bounded range that reliably continues the rule far beyond it, with no hard-coded variables.

## 2.6 Reasoning and chain of thought: what is and is not claimed
- **Thesis (position)**: an autoregressive model produces candidate completions quickly with no guarantee of correctness; "reasoning" claims need a verifier, a soundness argument or a search procedure, not only fluent steps.
- **Mechanism**: ways of spending more inference compute: (1) a generic prompt that asks for step-by-step output; (2) task-specific human-written exemplars (chain of thought); (3) generate many candidates and pick by majority or self-consistency; (4) add an external verifier or solver; (5) train the model with reinforcement learning on generated solution traces, so the intermediate tokens become "what to tell myself to raise the chance of the right answer", analogous to a game-playing agent whose board is the context and whose move is a token. Synthetic traces from solvers replace human-written ones.
- **For**: these methods reliably raise accuracy on verifiable tasks.
- **Against**: step-by-step text imitates the form of human derivations, may be unfaithful to what drives the answer, and helps less as problems grow beyond the length and structure of the exemplars. In this model, improvement from extra tokens does not imply a sound procedure.
- **Falsified by**: accuracy that stays flat or degrades when problem size grows along a dimension the traces did not cover, or intermediate steps that can be altered without changing the answer.
- **Does not hold when**: the domain has a cheap verifier (code with tests, formal proofs); there search plus verification gives guarantees regardless of whether the generator "reasons".

## 2.7 Brittleness to phrasing (mechanism)
- **Thesis**: robust understanding should survive renaming and rephrasing that a human would accept.
- **Mechanism**: models answer well-known trick questions by matching the surface (a famous riddle answered "they weigh the same" even when the numbers differ; a changed probability-puzzle variant answered with the canonical solution). Such cases were fixed by special-casing, but new instances are easy to find. Changing variable names or numbers in a formula can break performance.
- **Position on prompt engineering**: "you just need to query it right" implies that for every working query there is an equivalent human-readable rephrasing that fails; if so, this looks more like pattern matching than robust understanding.
- **Counter**: robustness has improved with scale and training; some brittleness is shared by people (framing effects).
- **Falsified by**: a battery of meaning-preserving rewrites, renamings and numeric variations with no drop in accuracy.
- **Related**: templated variants as a test are in `ai-ml-concepts` ch09.

## 2.8 Non-zero reasoning: a "fractal" picture (position)
- **Position**: models do something between retrieval and sound reasoning, inconsistently: sometimes memorised procedure, sometimes composition, sometimes something not yet characterised. Both "stochastic parrot" and "already general" are too simple.
- **Practical use**: describe observed behaviour by task and condition rather than by a single label.

## Checklist for this chapter
1. Is the claim about interpolation, composition, or both?
2. What would a controlled extrapolation test look like for this claim?
3. Is the "reasoning" verifiable, or only plausible-looking?
4. Does the result survive renaming, rephrasing and changed parameters?
