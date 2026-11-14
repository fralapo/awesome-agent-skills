---
name: physics-and-math-ideas
description: "How physics and mathematics reason, and what they do and do not know: models, effective theories, symmetry and Noether's theorem, the action principle; relativity and curved spacetime; quantum mechanics with the interpretations compared (Copenhagen, pilot wave, many worlds), Bell tests and the Born rule; black holes, Hawking radiation, the information paradox, firewalls, holography; dark energy, naturalness and fine-tuning; entropy, Maxwell's demon, Landauer limit, the arrow of time, Boltzmann brains; fields, bosons and fermions, Higgs mechanism, Casimir effect, strings, Maxwell's equations; infinity, continuum hypothesis, Turing machines, halting problem, NP-completeness, uncomputable complexity, computer-assisted proofs; paradoxes and how to resolve them. Use when the user explains, writes about or checks a physics or maths idea, a popular-science claim, a paradox or an interpretation, and needs it sorted into established, proposed or speculative. Separates mechanism from position."
allowed-tools:
  - Read
  - Grep
argument-hint: [concept, paradox, claim, or chapter number]
---

# Physics and Math Ideas
**Chapters**: 10 | **Corpus**: ~34 theoretical transcripts | **Generated**: 2026-11-14

## Role and Boundaries

This skill **decides how to explain and weigh an idea from physics or mathematics**: what the concept says, which mechanism supports it, which assumptions carry it, what rival readings exist, and whether it is measured, proved, proposed or speculative. It gives mechanisms, comparison tables and a sorting checklist; it does not replace a textbook or run calculations.

| This skill decides | This skill hands off |
|---|---|
| What a physics or maths concept claims, its mechanism, its assumptions and its limit; how rival interpretations differ; which level of evidence backs a statement | Judging a study, a statistic or a forecast; base rates, replication, calibration, falsifiability in general, limits of proof as epistemology -> `scientific-thinking` |
| Paradoxes: finding the hidden assumption, classifying, tracing what field resulted | Reasoning about motives, irrationality and relationships -> `depth-psychology` |
| Entropy, information and computation limits as concepts | Architecture-level resilience, incident reasoning, distributed-systems limits -> `software-architecture` |
| Turning an idea into a clear explanation with an honest status line | Visual explanation, slides, diagrams for a talk -> `presentation-design`, `dataviz`, `creative-director` |
| Which parts of a popular claim are measured versus interpretive | Running a statistical analysis or numerical model on data -> `data:statistical-analysis` |

**Stay in lane.** The chapters hold practitioner-level conceptual theory, not a derivation of every result. Figures are dated snapshots; re-check before relying on them. Items that could not be confirmed are marked "(unverified)" or omit the figure. Items marked *general knowledge* are background added to make a concept complete.

## Facts vs Positions

- **Mechanism / fact**: why a symmetry gives a conserved quantity, why time dilation implies curvature, why Bell-inequality violations exclude local hidden variables, why the halting problem cannot be decided, why entropy rises.
- **Position**: written as "In this model..." or "(position)": for example "many worlds is the most economical interpretation", "entanglement drives the second law", "space is holographic", "computer proofs lack understanding", "the dome shows Newtonian indeterminism".
- Every concept has four fields: **Thesis**, **Mechanism**, **Trade-off**, **Does not hold when**. Read the last one before applying a claim.

## How to Use This Skill

Diagnose before explaining: ask who the explanation is for (level), whether the question is about the formalism, an interpretation or a speculation, and what the user will do with the answer (write, teach, check a claim).

| Task | Start with | Then |
|---|---|---|
| "How does physics reason?" Models, symmetries, conservation, action | [ch01](chapters/ch01-how-physics-reasons-models-symmetry-action.md) | ch10 |
| Relativity, curved spacetime, why gravity is not a force, time dilation | [ch02](chapters/ch02-relativity-and-spacetime.md) | ch05 |
| Quantum mechanics, interpretations compared, entanglement, Born rule | [ch03](chapters/ch03-quantum-mechanics-and-interpretations.md) | ch06.8, ch10 |
| Black holes, Hawking radiation, information paradox, firewalls, holography | [ch04](chapters/ch04-black-holes-and-information.md) | ch03, ch06 |
| Dark energy, expansion, fine-tuning, naturalness, constants | [ch05](chapters/ch05-cosmology-and-constants.md) | ch07, ch10 |
| Entropy, demon, Landauer limit, arrow of time, Boltzmann brains | [ch06](chapters/ch06-thermodynamics-entropy-arrow-of-time.md) | ch03.9, ch09 |
| Particles, fermions and bosons, Higgs mechanism, Casimir effect, strings, Maxwell's equations | [ch07](chapters/ch07-particles-and-fields.md) | ch01.5, ch05 |
| Infinity, continuum hypothesis, Turing, halting, NP-completeness, Kolmogorov complexity, computer proofs | [ch08](chapters/ch08-infinity-computability-formal-limits.md) | ch09 |
| A paradox: what is wrong with it, and what did it lead to | [ch09](chapters/ch09-paradoxes-and-how-to-use-them.md) | the relevant chapter |
| "Is this claim established or speculative?" | [ch10](chapters/ch10-established-vs-speculative-checklist.md) | `scientific-thinking` |
| Quick lookup | [cheatsheet.md](cheatsheet.md), [patterns.md](patterns.md), [glossary.md](glossary.md) | |

## The Core Principles (recurrence order)

1. **Symmetry gives conservation; no symmetry, no conservation.** Check whether the symmetry holds before using the law.
2. **Geometry first.** Rephrase a motion or gravity claim as a statement about world lines and curvature to compare it fairly.
3. **Formalism is agreed, interpretation is not.** Separate the numbers a theory predicts from the story told about them.
4. **Every interpretation gives something up.** Locality, realism, a single world, or a neat measurement rule.
5. **Principles collide at horizons.** Black holes force a choice between information conservation and a smooth horizon.
6. **Combine independent probes, and check how independent they are.**
7. **Unnatural means "improbable under an explicit prior", not "impossible".**
8. **Entropy is counting and hidden information.** The second law is statistical; the arrow also needs a special past.
9. **Divergent expressions are regularised, not summed.**
10. **Provable limits come in three kinds**: independent of axioms, uncomputable, and merely unsolved. Do not confuse them.
11. **A paradox marks a hidden assumption.** Name it before choosing a side.
12. **State the evidence level in the same sentence as the claim.**

## Chapter Index

1. [How physics reasons: models, symmetry, action](chapters/ch01-how-physics-reasons-models-symmetry-action.md)
2. [Relativity and spacetime](chapters/ch02-relativity-and-spacetime.md)
3. [Quantum mechanics and its interpretations](chapters/ch03-quantum-mechanics-and-interpretations.md)
4. [Black holes, singularities and information](chapters/ch04-black-holes-and-information.md)
5. [Cosmology, dark energy and the naturalness of constants](chapters/ch05-cosmology-and-constants.md)
6. [Thermodynamics, entropy, information and the arrow of time](chapters/ch06-thermodynamics-entropy-arrow-of-time.md)
7. [Particles, fields, forces and electromagnetism](chapters/ch07-particles-and-fields.md)
8. [Infinity, computability and the limits of formal systems](chapters/ch08-infinity-computability-formal-limits.md)
9. [Paradoxes and how to use them](chapters/ch09-paradoxes-and-how-to-use-them.md)
10. [Established or speculative? A checklist](chapters/ch10-established-vs-speculative-checklist.md)

## Topic Index

- **Action, Lagrangian, path integral** -> ch01.6-1.7
- **Anthropic reasoning, Boltzmann brains** -> ch05.6, ch06.9
- **Arrow of time, past hypothesis** -> ch06.6-6.7
- **Bell inequalities, locality, realism** -> ch03.7
- **Black-hole entropy, Bekenstein bound** -> ch04.4
- **Born rule** -> ch03.8
- **Bosons, fermions, condensates** -> ch07.2
- **Diagonal argument, countable sets** -> ch08.1-8.2
- **Casimir effect, regularisation, -1/12** -> ch07.4
- **Computer-assisted proof, four colour theorem** -> ch08.9
- **Continuum hypothesis, forcing, independence** -> ch08.3
- **Dark energy, timescape, evolving dark energy** -> ch05.1-5.4
- **Dome paradox, determinism** -> ch09.6
- **Effective theory, UV and IR** -> ch01.1
- **Entanglement and entropy** -> ch03.9, ch06.8
- **Equivalence principle** -> ch02.3, ch04.6
- **Firewall, complementarity, monogamy of entanglement** -> ch04.6-4.7
- **Halting problem, undecidability** -> ch08.6
- **Higgs mechanism, symmetry breaking** -> ch07.3
- **Holographic principle, AdS/CFT** -> ch04.9
- **Kolmogorov complexity, Berry paradox** -> ch08.8, ch09.5
- **Landauer limit, reversible computing** -> ch06.5
- **Many worlds, pilot wave, Copenhagen** -> ch03.5
- **Maxwell's demon** -> ch06.4
- **Maxwell's equations** -> ch07.7
- **Naturalness, hierarchy problem, fine-tuning** -> ch05.5-5.6
- **Noether's theorem, conservation laws** -> ch01.4
- **NP-completeness, P versus NP** -> ch08.7
- **Planck constant, ultraviolet catastrophe** -> ch03.1
- **Singularity theorem, trapped surface** -> ch04.1
- **Strings, extra dimensions, landscape** -> ch07.5
- **Turing machine, universality** -> ch08.5
- **Dichotomy paradox, limits, calculus origins** -> ch09.4
