# Chapter 09: Paradoxes and How to Use Them

## Core Idea
In this model a paradox is a **diagnostic**: it marks a place where an assumption you did not know you were making has failed. The useful question is not "which side is right?" but "which hidden assumption produces the clash?" Many paradoxes later became whole fields (limits and calculus, set theory, relativity, computability, statistical mechanics).

Fields: **Thesis**, **Mechanism**, **Trade-off**, **Does not hold when**. **(position)** marks contested resolutions.

## 9.1 Three kinds of paradox
| Kind | Cause | What to do | Examples here |
|---|---|---|---|
| Apparent (veridical) | A hidden assumption about frames, geometry or intuition | Find the assumption; the paradox dissolves | Pole in the barn, muon lifetime, rolling wheel, spring-and-string weight, dark night sky |
| Foundational | The theory is inconsistent or too permissive | Change the axioms or the rules | Set of all sets that are not members of themselves, shortest-description paradox, infinite-vase |
| Open or contested | The resolution itself is disputed | Hold both readings, mark which is which | Ball on the dome, white shoes as evidence about black ravens, measurement problem |

## 9.2 Apparent paradoxes: relativity
- **Thesis**: when the same events are "both true and false" in two frames, the cause is the relativity of simultaneity.
- **Mechanism**: **Pole in the barn**: a 20 m pole at 90% of light speed contracts (to about 8.7 m as quoted) and fits a 10 m barn in the barn's frame; in the pole's frame the barn is contracted and the pole never fits. Both are right because "both ends are inside at the same time" is frame-dependent. **Muon paradox**: muons live about 2.2 microseconds, so should travel only about 660 m, yet many reach the ground from about 15 km up. In the ground frame time dilation extends their life; in the muon frame the atmosphere is length-contracted. Both give the same count.
- **Trade-off**: you must pick a frame for each calculation and not mix them.
- **Does not hold when**: the speeds are low; then the Newtonian answer is fine.

## 9.3 Apparent paradoxes: geometry, mechanics, cosmology
- **Rolling circle**: a small circle rolling inside a big one covers the same distance, so same circumference? The small one is not purely rolling; it is also dragged. The insight links to mapping all points of lines of different length one to one (ch08.1).
- **Spring-and-string weight**: with two springs linked, springs alone bear the whole weight; unlinking shares it among two pairs, so the springs shorten and the weight **rises** although slack strings seem to allow it to drop. Lesson: equilibria change when the load path changes; intuition about "slack" is unreliable.
- **Gabriel's horn**: infinite surface area, finite volume (the curve 1/x rotated about the axis). Lesson: area and volume diverge or converge independently.
- **Dark night sky**: if stars fill an infinite static universe every line of sight ends on a star. Resolution: finite speed of light and finite age (light from far galaxies has not arrived, some never will) and redshift of starlight by expansion.
- **Easy-hard inversion (robotics)**: things that are easy for humans (walking across a messy room, grasping) were hard for machines, while explicit-rule tasks (chess) were easy. Explanation offered: skills that feel simple are deeply rooted in unconscious processing refined by long evolution. Dated: AI and robotics have changed quickly since the examples were set (the example match was in 1997).
- **Trade-off**: each is a lesson on a hidden assumption: "same time", "same length", "static", "just rolling".
- **Does not hold when**: the setup is changed so the assumption is true.

## 9.4 Paradoxes that built calculus and the idea of limits
- **Thesis**: three ancient puzzles about infinite division pushed mathematicians to define limits rigorously.
- **Mechanism**: **Dichotomy**: before reaching the end you must reach halfway, then half of what is left, forever; infinitely many steps, so motion seems impossible. A **limit** shows an infinite sum can be finite (1/2 + 1/4 + 1/8 + ... = 1). **Widthless lines** (stacking lines of zero width to get area): sums of infinitely many zeros are not zero; the fix is the limit of strips whose width approaches zero (the integral). **Arrow at an instant**: motionless at each instant, yet moves; the **derivative** defines instantaneous velocity as the limit of average velocity over shrinking intervals. The Planck-scale hint that space may not be divisible without limit (ch03.1) does not rescue the paradox as stated.
- **Trade-off**: a precise tool for the infinite; no claim about whether physical space is continuous.
- **Does not hold when**: used to prove space is infinitely divisible; the mathematics is idealisation.

## 9.5 Foundational paradoxes
- **Set of all sets that are not members of themselves**: in or out, both lead to contradiction; naive set theory is inconsistent. This uprooted foundations and motivated axiomatic set theory (ch08.4). The barber version: the barber shaves all and only those who do not shave themselves.
- **Shortest-description paradox**: "the smallest integer that cannot be described in fewer than fifteen words" is described in fourteen. Made rigorous it shows that perfect compression is uncomputable (ch08.8).
- **Part equals whole (squares versus naturals)**: dissolved by defining size via pairing (ch08.1).
- **Infinite vase (balls added and removed forever)**: how many balls are in the vase at noon? "Infinity times nine" says infinitely many; "every ball is eventually removed" says zero. Both come from treating an infinite process as if its limit were determined by counts alone; (*general knowledge*) the answer depends on the order in which balls are removed. This is a warning about informal infinite arguments.
- **Trade-off**: foundational repairs (axioms, definitions) restore consistency at some cost to intuition.
- **Does not hold when**: the "paradox" is only wordplay; test by asking whether a precise version remains.

## 9.6 Open or contested: the dome
- **Thesis (position)**: a frictionless ball resting at the apex of a particular dome can, under Newtonian equations, start moving at an arbitrary time with no cause; this is a challenge to determinism.
- **Mechanism**: Newtonian determinism is mathematically uniqueness of solutions to the differential equation given initial conditions. Uniqueness is guaranteed under conditions (Lipschitz continuity, in the existence-and-uniqueness theorem); the dome violates one (the slope of the force blows up in a controlled way at the apex), so the equation of motion has more than one solution: staying forever, or leaving at any excitation time. Time-reversal symmetry makes it plausible: a ball can be nudged to arrive at the apex and stop there, so reversed it can rest and then leave. The instantaneous form of the first law is not violated at any moment: zero force, zero acceleration, even at the excitation time. The excitation time is the *last* instant of rest; there is no *first* instant of motion, so there is nothing to look for as the "initial cause".
- **Positions**: (a) Newtonian mechanics is indeterministic after all; (b) the idealisation is illegitimate (real balls and domes are not perfect; quantum effects interfere); (c) Newtonian mechanics has several valid versions, not one. The matter has stayed unsettled through a decade of published argument and is a reminder that well-established theories can still surprise us. Not a claim about physical balls.
- **Trade-off**: shows exactly which mathematical condition carries determinism.
- **Does not hold when**: used to prove free will or a "fourth law of motion", both of which appear in the debate but remain speculative.

## 9.7 Open or contested: evidence for "all ravens are black"
- **Thesis**: "all ravens are black" is logically equivalent to "all non-black things are non-ravens", so a white shoe seems to confirm it.
- **Mechanism**: logically it does, but only extremely weakly; the common view is to ignore it in practice. Not resolved.
- **Trade-off**: shows the gap between formal confirmation and useful evidence (see `scientific-thinking`).
- **Does not hold when**: the population of non-black things is small and drawn at random (then the evidence is not negligible, *general knowledge*).

## 9.8 Reversibility paradox: microscopic reversibility versus the arrow
See ch06.7: the laws are time-reversible, so the arrow needs a low-entropy past. It is both an apparent paradox (equilibrium assumption) and an open question (why the start was special).

## 9.9 How to use a paradox: a procedure
1. **State both sides precisely** (as geometry, equations or definitions).
2. **List the assumptions** each side uses; mark which were not stated (frame, equilibrium, order of operations, closed system, idealisation).
3. **Find the clash**: which assumption cannot hold in both?
4. **Classify** with 9.1 (apparent, foundational, open).
5. **Ask what field the paradox grew into**: if it produced a definition (limit, cardinality, proper time), the definition is the real resolution.
6. **Say what it does not show**: a paradox in an idealised model is not necessarily a fact about the world.
- **Does not hold when**: the question is rhetorical; if no assumption can be named, the paradox may be a language trap.
