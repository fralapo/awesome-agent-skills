# Chapter 08: Infinity, Computability and the Limits of Formal Systems

## Core Idea
In this model there are **provable limits** that are not about lack of cleverness: infinities come in different sizes, some questions cannot be settled by the standard axioms, some programs cannot be analysed by any general algorithm, and some natural problems are believed (not proved) to need exponential work. The skill is to say which of these three kinds of limit a claim is about: *impossible in principle* (proved), *independent of the axioms* (proved), or *merely unsolved* (open).

Fields: **Thesis**, **Mechanism**, **Trade-off**, **Does not hold when**. **(position)** = contested; *general knowledge* = background knowledge.

## 8.1 Size by pairing: countable infinity
- **Thesis**: two sets are the same size if their elements can be paired one to one with none left over; this definition, not "more elements", is what works for infinite sets.
- **Mechanism**: natural numbers pair with squares (1 with 1, 2 with 4, 3 with 9), with even numbers, with integers, and with fractions. All these are **countably infinite** (listable). Strange but consistent: a part can be as large as the whole.
- **Trade-off**: rigorous but violates the "part is smaller than whole" intuition.
- **Does not hold when**: the set is finite, where intuition and definition agree.

## 8.2 Different sizes of infinity: the diagonal argument
- **Thesis**: the real numbers are uncountable; there are more of them than natural numbers.
- **Mechanism**: assume a list of all reals; construct a number that differs from the n-th entry in its n-th digit; it is missing from the list, a contradiction. So no pairing exists. Hence there are infinitely many sizes of infinity (general knowledge); the smallest is aleph-null (naturals). Number hierarchy used: natural, integer, rational, irrational, algebraic, transcendental (pi and e are transcendental), all inside the reals.
- **Trade-off**: a powerful general proof technique (also used for halting, 8.6).
- **Does not hold when**: asked to construct a specific listing; the proof is by contradiction only.

## 8.3 The continuum hypothesis: independent of the standard axioms
- **Thesis**: "no size of infinity lies between the naturals and the reals" can neither be proved nor refuted from the standard axioms of set theory (ZFC).
- **Mechanism**: *consistency with ZFC*: build the **constructible universe**, the minimal universe containing only what the axioms force to exist; in it the hypothesis holds, so it cannot be disproved. *Unprovability*: build a larger universe by adding many new reals, using **forcing**, a method that assigns abstract likelihoods to every question about a random real and so describes a universe satisfying every axiom with probability one while violating the hypothesis; there the constructible reals sit strictly between the two sizes. Hence the statement is **independent**. "Provable" means true in *all* models of the theory; the colour of buildings is independent of the law that buildings are rectangular prisms.
- **Trade-off**: set theorists work with **many models**, not one mathematical universe.
- **Does not hold when**: it is read as "the answer is unknowable forever". Whether new axioms could settle it is an **open debate (position)**; the debate raises more questions than answers.

## 8.4 The programme to formalise mathematics and its three demands
- **Thesis**: a formal system (symbols manipulated by fixed rules, like chess) was supposed to be consistent, complete and decidable.
- **Mechanism**: consistency = no contradiction provable; completeness = every true statement provable; decidability = a mechanical procedure decides any statement. The programme was a reaction to the paradoxes that shook set theory (ch09.5). Two limits followed: any axiom set that is strong enough is incomplete (true statements it cannot prove), and it cannot prove its own consistency. The third demand fell to the halting problem (8.6).
- **Trade-off**: formalisation gives exactness; completeness is unobtainable.
- **Does not hold when**: the system is too weak to express arithmetic (limits then do not apply, *general knowledge*).

## 8.5 Turing machines: defining "effective procedure"
- **Thesis**: an effective procedure is anything a person could do mechanically with no insight, and a very simple machine models all of it.
- **Mechanism**: abstract the human computer: read, write and erase one symbol at a time on a tape (infinite), keep a small internal "state", stop when done. A state table says: in state S reading symbol X, write Y, move left or right, go to state S'. Example: pair each zero with a one, cross them off, accept if none are left over. It can do everything a modern computer can. A **non-deterministic** machine may branch among instructions. **Universality**: one machine can run any other machine's program; this "programmability" is why general computers displaced special-purpose devices, and it enables programs running programs.
- **Trade-off**: simple model, strong claim; the equivalence with "all computers" is a thesis supported by every proposed model.
- **Does not hold when**: asked about hypothetical hypercomputation; the model is about mechanical procedure.

## 8.6 Undecidability: the halting problem
- **Thesis**: no program can decide, for every program and input, whether it halts.
- **Mechanism**: suppose a halt-checker exists. Build "reverser": run the checker on a program; if it says "halts", loop forever; if "loops", halt. Feed reverser to itself; either answer contradicts itself. So the checker cannot exist. Undecidability is the **flip side of universality**, not a defect. Practical reach: many "can I write a general tool that tells me whether..." tasks reduce to halting (do two programs do the same thing? does a program contain malware? Goldbach's conjecture can be phrased as "does this search program halt?").
- **Trade-off**: general analysis is impossible; specific cases and restricted languages can still be analysed.
- **Does not hold when**: restricted to classes of programs with bounded loops or a limited language; the theorem concerns unrestricted programs and all inputs.

## 8.7 Hard problems: NP-completeness
- **Thesis**: a large family of problems with very different faces is, in a precise sense, one problem in disguise; a fast algorithm for one would give a fast algorithm for all.
- **Mechanism**: **Clique** (find k mutually compatible items) by brute force grows exponentially: roughly seconds at 40 items, centuries at 80, longer than the stars at 160 (as stated, order of magnitude, hardware-dependent). **P** = solvable in polynomial time; **NP** = a proposed solution can be *checked* in polynomial time (a needle in a haystack: hard to find, easy to verify). **SAT**: can a Boolean formula be made true? Boolean formulas can express constraints about any object. The **Cook-Levin result**: a SAT formula can simulate a non-deterministic Turing machine, so SAT is **NP-complete**, and any problem in NP reduces to it. To prove a new problem NP-complete, reduce a known one to it, a routine first move for working computer scientists. Over a thousand problems share the property (scheduling, routes, folding, Rubik's cube and puzzle-game optimisation are cited examples); a one million dollar prize is attached to the question whether P equals NP.
- **Trade-off**: tells you when to stop hunting for an exact fast algorithm and switch to heuristics, approximations or restricted cases.
- **Does not hold when**: you treat it as proved hardness. It is **unproven** that no fast algorithm exists; typical-case instances are often easy. Exponential versus polynomial is a coarse distinction, though in practice it often decides what is feasible.

## 8.8 Uncomputable complexity: the algorithm for truth cannot exist
- **Thesis**: the shortest description of a string (its **Kolmogorov complexity**) is a natural measure of simplicity, and it is **uncomputable**.
- **Mechanism**: a string like "10 repeated 25 times" is compressible; the digits of a constant look random yet have a short rule. The scientific method can be viewed as data compression, with Occam's razor as a preference for short descriptions. A search program that tries all programs in length order would find the shortest generator, but it cannot be made to work: one can use it to write a short program that outputs "the first string not describable in fewer than m bits", a contradiction with that string's description length (the **Berry paradox** made precise).
- **Trade-off**: gives a formal meaning to simplicity; shows that no general "algorithm for truth" or optimal compressor exists.
- **Does not hold when**: you only want approximations; compression in practice (any particular compressor) is fine. The limit is for the perfect, general case.

## 8.9 What counts as a proof: computer-assisted proofs
- **Thesis (position)**: a proof checked by machine is valid, but critics argue mathematics aims at understanding, which such proofs do not give.
- **Mechanism**: the **four colour theorem** (four colours suffice for any map) took over a century. The reduction: replace map by planar graph (regions as vertices, borders as edges); the **five colour** version has a human-length proof using induction, contradiction and invariants. The four-colour proof shows that every graph must contain one of about 2,000 configurations with a certain colourable property, then a computer checked them (over a thousand hours). Objection: the proof tells you it is true, not why; mathematics's mission is understanding. Counter-view: expecting proofs to fit a human mind may be arrogant. Later: a Boolean-Pythagorean-triples result used about four CPU-years (a few days on many cores) and a 200 TB proof, compressed to 68 GB.
- **Trade-off**: reach versus insight, and trust in software and hardware.
- **Does not hold when**: the computation is itself verified by an independent checker; trust in the proof then rests on checking tools.

## 8.10 Limits you can state precisely
| Kind of limit | Example | Status |
|---|---|---|
| Not provable and not refutable from given axioms | Continuum hypothesis (from the standard axioms) | Proved independent |
| Not computable by any algorithm | Halting, perfect compression, program equivalence | Proved |
| Probably needs exponential time | NP-complete problems | **Unproven** (P vs NP open) |
| Needs a machine to check | Four colour theorem | Proved (computer-assisted) |
| Too large to try | Typing monkeys, brute-force search | Practical, not logical |
