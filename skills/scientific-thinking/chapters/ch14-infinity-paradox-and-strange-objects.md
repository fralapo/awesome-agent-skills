# Chapter 14: Infinity, Paradox and Strange Mathematical Objects

## Core Idea
In this model, the paradoxes of infinity and geometry are not tricks: each one exposes a specific assumption that holds for finite or everyday objects and fails beyond them (the part is smaller than the whole, shortest means fastest, an object with no area is nothing, a finished sequence has a last step). The skill is to name the assumption that fails, and to keep three questions apart: is it **logically consistent**, is it **physically realisable**, and is it **useful**. Chapter 09 covers proof, undecidability and computation; this chapter covers infinity, measure, shape and dimension.

## 14.1 Sizes of infinity by matching
- **Thesis**: two collections are the same size if their members can be paired one to one, and for unending collections this overturns the "part is smaller" rule.
- **Mechanism**: the counting numbers, the even numbers, the odd numbers and the fractions can all be paired with each other, so they share the smallest infinite size. A fully booked hotel with unending rooms can always take another guest by moving every guest one room along, or a countably infinite busload by moving each guest to twice their room number; removing a guest can be absorbed in the other direction. The same trick removes one point from a circle: the countable set of points marked along it can be shifted to fill the hole. Infinity is a size, not a number on the line: infinity plus one, or divided by two, is the same size.
- **Trade-off**: matching gives a clean definition of "same size" but gives up the intuition of proportion.
- **Does not hold when**: the collection is finite; then the part really is smaller.

## 14.2 Size and order are different things
- **Thesis**: for infinite collections, "how many" and "in what order" separate.
- **Mechanism**: the amount of members is a cardinal number; the arrangement is captured by an ordinal number, the label you need after using every counting number in sequence. Adding a line after an endless sequence of lines does not change how many lines there are, but it changes the order type, so the new arrangement needs a label beyond the first infinite ordinal. A larger ordinal is not a larger amount.
- **Trade-off**: the extra machinery is needed only when order matters.
- **Does not hold when**: collections are finite, where size and order coincide.
- **Use**: in a "name the biggest number" contest, state whether you mean a size or a position.

## 14.3 Bigger infinities: the power set
- **Thesis**: you can always manufacture an infinity larger than the one you have.
- **Mechanism**: the power set of a set is the set of all its subsets (it has 2^n members for n members). Take any attempted pairing of the counting numbers with their subsets; build a new subset that disagrees with the first subset on membership of the first number, with the second on the second, and so on. It differs from every listed subset, so no pairing is complete. Repeating the construction gives an unending ladder of ever larger infinities. The real numbers form a bigger infinity than the counting numbers by the same diagonal idea (ch09, section 9.4).
- **Trade-off**: the construction proves existence of larger sizes, not their physical meaning.
- **Does not hold when**: the question is about anything countable or measurable in the physical world; no known physical quantity needs an uncountable collection.

## 14.4 Infinity as a completed thing
- **Thesis**: accepting infinity as a finished object, not just an endless process, is a choice that opened a new field and met long resistance.
- **Mechanism**: the older view allowed only "potential" infinity: a sequence can be continued without end, but you never have all of it at once. Constructing the number line so that every limit is a number (for instance by defining a real number as the cut or gap it fills) treats the whole line as a completed totality, and infinity then lives inside every interval. Resistance was philosophical before it was technical.
- **Trade-off**: the completed view is powerful and unlocks the ladder of sizes, but it licenses objects that cannot be constructed step by step.
- **Does not hold when**: you work in a framework that rejects completed infinities on principle; it then gives a different, weaker mathematics.
- **Position**: popular origin stories of foundational results are often cleaner than the record (see ch10).

## 14.5 Supertasks: infinitely many steps in finite time
- **Thesis**: an unending list of tasks can be consistent with a finite duration, but its end state may be undefined.
- **Mechanism**: if each step takes half as long as the previous one, the total time is finite while there is no last step. Some such sequences converge: halving a solid again and again and stacking the halves gives finite volume and unbounded height and surface area (a cake you can eat but not frost). Others oscillate: a lamp switched on and off at ever shorter intervals is neither on nor off at the end, because every "on" is followed by an "off" and vice versa; layers of alternating colour give no top colour. The state at the limit is not determined by the steps; it requires an additional rule.
- **Trade-off**: a physical smallest length or time would end the sequence, but then the truth of a mathematical statement would depend on contingent physics, which some find unsatisfying.
- **Does not hold when**: the steps converge to a limit and you only ask about that limit.
- **Use**: reasoning about "after infinitely many steps" needs an explicit limit rule; otherwise the question has no answer.

## 14.6 Rearranging a solid into two (Banach–Tarski)
- **Thesis**: a ball can be split into a few pieces and reassembled by rotation and translation into two balls of the same size, so "volume" cannot be assigned to every set of points.
- **Mechanism**: name each point on the surface by the sequence of allowed rotations that reaches it from a starting point, excluding sequences that undo one another; this partitions the surface into a few classes defined by the last rotation. One class, rotated, turns out to cover three of the classes together; the structure is the same as a dictionary of all possible words: strip the first letter from the "a" volume and you obtain the whole dictionary again. The few left-over points (fixed by every rotation) are handled separately. In this model, the construction depends on choosing representatives from infinitely many classes without a rule (the axiom of choice, general knowledge) and the pieces are not measurable; they cannot be made of "stuff" with a volume.
- **Trade-off**: the result shows why measure theory restricts which sets count; the cost of removing the paradox is giving up either the axiom or the idea that every set has a volume.
- **Does not hold when**: you work with physical matter: real objects are finite collections of atoms, and the pieces cannot be cut out.
- **Position**: the result is a consequence of axioms, not a prediction about the world.

## 14.7 Equal cross-sections, equal volumes
- **Thesis**: two solids with the same cross-sectional area at every height have the same volume.
- **Mechanism**: stack coins into a straight pile and shear it; the shape changes, the volume does not. Applied to a sphere with a cylinder bored through its centre (a napkin ring), at any height the ring's cross-section is the area of the sphere's circle minus the area of the cylinder's circle, and by the Pythagorean relation this depends only on the ring's height and the height at which you cut. So two napkin rings of the same height have the same volume, whatever the size of the sphere: a thinner ring from a big sphere exactly offsets a thicker ring from a small one.
- **Trade-off**: the principle is elegant for volumes but requires the cross-section comparison to hold at every level.
- **Does not hold when**: heights differ, or the hole is not cylindrical and centred.
- **Use**: "obviously bigger" claims about shapes can be checked by comparing cross-sections.

## 14.8 Shortest is not fastest: least-time paths
- **Thesis**: the straight line is the shortest route but not the quickest route for a body falling under gravity.
- **Mechanism**: steeper early travel gives higher speed sooner, which can outweigh a longer path. The solution was found by treating the fall as light moving through layers with changing speed: light always bends according to a law that makes its path the quickest, and with speed increasing continuously the quickest curve is a cycloid (the path traced by a point on a rolling circle). A first guess that a circular arc was best was wrong.
- **Trade-off**: the quickest path depends on the starting and ending points, and on friction being negligible.
- **Does not hold when**: friction, rolling resistance or air drag matter; the optimum changes.
- **Use**: when an "optimal" route is requested, state the quantity being optimised (distance, time, energy).

## 14.9 Zero area is not nothing: dimension
- **Thesis**: a set can have no area and still be large in a different sense, measured by dimension.
- **Mechanism**: two different objects are easy to confuse. (a) The area in which a needle can be turned through all directions can be made as small as you like, but not zero. (b) A Besicovitch set contains a line segment in every direction and can have area zero, but it does not allow the needle to be rotated continuously. Fractional dimension (the exponent in how the number of covering boxes grows as the boxes shrink) shows the set in (b) is not small in that other sense; the open question is whether the dimension can drop below that of the space itself in higher dimensions. A proof for the three-dimensional case was announced in 2025 (as reported; not independently checked here), and a tower of conjectures in harmonic analysis rests on the question.
- **Trade-off**: dimension gives a finer notion of size but not one number that fits all purposes.
- **Does not hold when**: you only need area or volume of nicely behaved shapes.

## 14.10 Simple rule, endless complexity: the Mandelbrot set
- **Thesis**: iterating a very simple map can produce a boundary of unlimited detail.
- **Mechanism**: take a quadratic rule on complex numbers, choose a parameter, iterate from a start and ask whether the sequence escapes to infinity or stays bounded. The set of parameters whose sequence stays bounded is the Mandelbrot set. Its boundary shows self-similarity and new features at every zoom. It is a map of the behaviour of a whole family of dynamical systems and is described as the first step towards understanding much more complicated systems; basic questions about it remain open.
- **Trade-off**: pictures suggest structure but proofs of the structure are rare.
- **Does not hold when**: you interpret the picture as evidence: a rendered image is finite and coloured by choice.

## 14.11 Topology: local flatness, global difference
- **Thesis**: spaces that look identical up close can differ globally; intuition about this fails most in four dimensions.
- **Mechanism**: a manifold looks like flat space on a small enough patch (the surface of a ball looks flat to an ant); only global invariants separate a sphere from other surfaces. In four dimensions there is much behaviour that differs from lower and higher dimensions, and results cannot be guessed. A related use of symmetry (the 17 ways a repeating plane pattern can be symmetric, also the possible symmetries of a layer of crystal) shows how counting symmetries classifies things that look unlimited.
- **Trade-off**: abstract classification is complete but far from picturable.
- **Does not hold when**: you only need local behaviour; then flat-space geometry is enough.

## 14.12 Fluid equations: working tools without a proof of good behaviour
- **Thesis**: an equation can be used productively for centuries while a basic mathematical question about it remains open.
- **Mechanism**: the equations of fluid motion add friction between layers (viscosity) to the older frictionless ones; they describe most real flows but exact solutions are out of reach because of turbulence, so predictions come from numerical simulation. What is not established is whether solutions always remain smooth, or whether they can develop singularities in finite time; it is one of the seven prize problems of the field. A recent computer-assisted resolution was reported; its extent and acceptance are unclear and should be checked before relying on it.
- **Trade-off**: practitioners can proceed without the proof but cannot rule out pathological cases.
- **Does not hold when**: the application depends on guaranteed regularity (some safety bounds).

## Cross-references
Chapter 09 for the diagonal argument, undecidability and computation; chapter 13 for intuition failures; chapter 15 for heavy tails, universality and emergence; chapter 10 for how foundational ideas are received; for theoretical-physics topics, hand off to `physics-and-math-ideas`.
