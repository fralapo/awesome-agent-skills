# Chapter 5: Creativity, Novelty and Open-Ended Search

## Core Idea
In this model, creativity is not output that looks novel but the process that *finds* stepping stones to places nobody could aim for. The debate is whether objective-driven optimisation (the basis of nearly all machine learning) can produce good internal structure, or whether open-ended, objective-free search produces better representations. Positions below are each followed by counter-arguments and falsifiers.

## 5.1 Deception in objective search (position)
- **Thesis**: for ambitious goals the path to the goal does not look like the goal, so searching by "get closer to the target" is deceptive.
- **Mechanism**: an experiment evolved images through human selection, with no fixed target. Later, the same underlying algorithm was asked to reach a specific found image by minimising similarity to it. It generally failed because the stepping stones towards the image do not resemble it (image matching is a bad heuristic). It succeeded only for simple targets, and then with networks about three times the size of the original discovery.
- **For**: explains why directly optimising for a distant goal gets stuck; recommends searching for interestingness and diversity.
- **Against (general knowledge)**: objective-driven optimisation scales spectacularly in practice (gradient descent with large networks has solved many "deceptive" problems); the demonstration is on small search spaces.
- **Falsified by**: a method that reliably reaches distant, complex targets through pure similarity or reward gradients, without larger or less efficient solutions.
- **Does not hold when**: the objective is well-shaped and the landscape smooth, where hill-climbing works.

## 5.2 Novelty search and quality-diversity (mechanism + position)
- **Mechanism**: instead of maximising an objective, reward behaviour that is *different* from what has been archived, and keep a map of high-quality solutions across a space of behaviours (quality-diversity). This illuminates many niches rather than one peak. Such algorithms are now used inside larger systems (for example algorithm-discovery pipelines whose core includes a quality-diversity archive).
- **Position**: interesting stepping stones are only recognisable in hindsight, so maintain a population of diverse "stepping stones" instead of following a single gradient.
- **Against**: unconstrained novelty can be arbitrary; you need a notion of "interesting", and defining it reintroduces an objective.
- **Falsified by**: failure of diversity-maintaining search to beat objective search on a suite of hard, deceptive tasks at equal compute.

## 5.3 Survival is a constraint, not an objective (position)
- **Position**: biological evolution is not an optimiser aimed at a target; survival is a binary constraint on the system, and everything interesting (flight, photosynthesis) arose as a by-product. Early genetic algorithms used selection as a crude optimiser, which gave the field the impression that evolution is a poor man's optimiser and is not a deep metaphor.
- **For**: explains open-ended diversity in nature.
- **Against**: evolution does behave like an optimiser at many scales (fitness gradients, adaptation); the "constraint" framing is a modelling choice.
- **Falsified by**: showing that evolving populations with only a survival constraint do not produce open-ended novelty, or that the novelty arises from implicit objectives.

## 5.4 Fractured versus unified internal representations (position + mechanism)
- **Position**: two networks can produce the *same output* (an image) and differ completely inside. A representation from open-ended search can be modular and compact: separate components for parts (a mouth that opens and closes, a smile dimension) and efficient reuse. One trained by gradient descent to reproduce the same output can be a "spaghetti" of entangled, redundant pieces, even though the behaviour is identical and the loss is zero.
- **Mechanism for judging**: for a single-image network every unit can be visualised, so the internal structure is visible; the difference is stark.
- **Implication (position)**: "it solved the task" is not the end of the story; *how* it solved it matters for extension, adaptation and creativity. Brute-force routes yield worse representations than serendipitous ones. Interpretability work that studies circuits in standard networks addresses a different question: it explains whatever structure is there, not whether better structure exists.
- **For**: existence proof that neural networks do not inevitably yield entangled representations; so entanglement is a property of the training process, not of networks.
- **Against**: the examples are small and the human selector was part of the process, so the difference may come from human guidance, not from the open-ended search; the result may not generalise to language-scale models; entangled representations may suffice for most uses.
- **Falsified by**: finding comparable modular structure in large models trained by gradient descent and showing it matters (or does not matter) for extension and adaptation; or showing that human-guided search yields no better representations on fresh tasks.
- **Does not hold when**: the downstream use is only the fixed task output.

## 5.5 Does AI create, or only recombine? (position)
- **Position**: current models are strong at interpolation within the space of what exists and weak at the creative step that opens a new space. Open-ended novelty needs stepping-stone accumulation, not only a recombination of existing components.
- **For**: models produce competent variations in style but rarely a new movement; diverse outputs often converge ("homogenised output", see `ai-ml-concepts` ch10).
- **Against**: new combinations can be creative in practice; many human creative acts are recombination too; in domains with verifiers (maths, code, search for algorithms), model-guided search has produced results people accepted as new.
- **Falsified by**: independent judges unable to distinguish model-originated and human-originated contributions that opened a new space; or evidence that new-space contributions had no archive-based stepping stones.
- **Practical use**: ask whether the system maintains an archive of diverse stepping stones and a notion of "interesting", or only optimises a single score.

## 5.6 Humans in the loop as part of the explanation
- **Thesis**: much of the quality of the open-ended results came from humans picking what interested them without a fixed target; that is itself an unmodelled "interestingness" function.
- **Move**: if you want to reproduce the effect, the key design question is how to automate the choice of "what is worth pursuing next" without collapsing it into a single objective.
- **Does not hold when**: a model of interestingness learned from human choices is good enough (an open question).

## Checklist for this chapter
1. Is the system optimising a target, or maintaining diverse stepping stones?
2. Same output, different inside: has anyone looked at the representation, not just the result?
3. Is novelty judged against what exists, or against what could have been aimed for?
4. How much of the creativity was supplied by a human selector?
