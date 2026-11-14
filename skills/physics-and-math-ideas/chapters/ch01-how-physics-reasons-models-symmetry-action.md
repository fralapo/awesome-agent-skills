# Chapter 01: How Physics Reasons - Models, Symmetry, Action

## Core Idea
In this model physics is less a list of facts than a **style of argument**: build a model with few moving parts, ask what it leaves unchanged (symmetry), ask what it forbids, and let experiment choose between models that are each self-consistent. This chapter holds the reasoning moves that later chapters reuse.

Each concept uses four fields: **Thesis**, **Mechanism**, **Trade-off**, **Does not hold when**. Background knowledge is marked *general knowledge*; contested claims are marked **(position)**.

## 1.1 A theory is a layer: effective (IR) theories sit on deeper (UV) ones
- **Thesis**: most theories are coarse-grained descriptions valid over a limited range of scale or energy, not the bottom floor.
- **Mechanism**: the zoomed-out, low-energy, more emergent description is called the infrared (IR) theory; the deeper, short-distance one is the ultraviolet (UV) theory. The free parameters of the IR theory (the standard model has 19 that must be fixed by measurement) are not free in the UV theory: in principle they are calculable from it. Thermodynamics is the classic emergent layer: temperature and pressure belong to a room of molecules, not to one molecule.
- **Trade-off**: working in an IR theory is practical and accurate within its range, but it hides why its constants have their values.
- **Does not hold when**: the question is about the regime where the layer breaks down (singularities, the earliest universe); there the effective theory is silent or wrong.

## 1.2 Reductionism's default: the deep theory does not know about the shallow one
- **Thesis**: in the reductionist paradigm the UV theory is "blind" to the IR consequences that emerge from it, which is why a special-looking IR value is suspicious (see ch05 on naturalness).
- **Mechanism**: parameters at the bottom are set by some process (random, or a unique inevitable one); either way, nothing at the bottom is tuned *so that* a particular low-energy number comes out.
- **Trade-off**: gives a clear test for "this value looks arranged"; assumes the layer picture is right.
- **Does not hold when**: the layers are not cleanly separated (strong feedback between scales) or the deep theory is not reductionist.

## 1.3 Describe only what can be observed (observables-first)
- **Thesis**: when a picture of the unobservable interior (electron orbits) keeps failing, drop it and build the law only for what is measured.
- **Mechanism**: instead of formulas for a list of hidden states, write a formula for the frequency and intensity of the light emitted for every pair of initial and final state. A two-index table is a matrix, and matrices do not commute: x times y is not always y times x. That non-commutation became the engine of the uncertainty principle and of quantum randomness (ch03).
- **Trade-off**: powerful and honest about what is known, but the theory then "tells no story" about what happens between measurements, which many find unacceptable.
- **Does not hold when**: a model of the hidden layer makes extra, testable predictions; then refusing to model it throws information away (position).

## 1.4 Symmetry gives conservation (Noether's theorem)
- **Thesis**: for every continuous symmetry of the laws there is a conserved quantity. Conservation laws are consequences, not axioms.
- **Mechanism**: *continuous* means the equations of motion stay the same under any-size shift in a coordinate. Translation in space gives momentum; translation in time gives energy; rotation gives angular momentum. A perfectly flat road: momentum of colliding cars is conserved; a hilly road breaks the translation symmetry and the sum is not conserved. Discrete symmetries (mirror flip, 60-degree rotation) are not covered by the theorem.
- **Trade-off**: a very cheap way to solve problems ("cheat codes") and to explain why a law holds; it also tells you exactly when it fails.
- **Does not hold when**: the symmetry is absent. In general relativity space and time are dynamic, so time-translation symmetry is not generally available and energy is not conserved in the simple sense. Cosmological redshift loses photon energy; dark energy adds it. Energy conservation is then a special case valid where space is approximately unchanging. A bookkeeping quantity (the Landau-Lifshitz pseudotensor) restores a global balance by adding gravitational potential energy, but its use and interpretation are **contested**.

## 1.5 Gauge symmetry: a redundancy that forces a force
- **Thesis**: if physics does not care about a local choice (the zero point of an angle, the phase of a quantum wave function), then a new field must exist to compensate, and that field is a force.
- **Mechanism**: demanding that the local phase of the wave function be unobservable forces a new field into the equation; its oscillations are the photon (U(1) symmetry, electromagnetism). The same trick with abstract two-component degrees of freedom (SU(2)) gives three carriers resembling the weak bosons; combining groups is how the standard model is organised (ch07). The conserved electric charge is the Noether partner of phase rotation.
- **Trade-off**: organises all non-gravitational interactions with one principle; the price is that the gauge bosons come out massless, which needed an extra mechanism (ch07).
- **Does not hold when**: used as proof that nature "had to" be this way. The symmetries are inputs of the model, and a different symmetry choice gives a different theory.

## 1.6 The action principle: nature takes stationary paths
- **Thesis**: the path of a system is the one for which a quantity called action does not change to first order under small variations of the path. "Least action" is the common name; **stationary action** is more exact because minima and maxima both count.
- **Mechanism**: a history of ideas. Light takes the shortest path in a uniform medium; replacing "least distance" with "least time" explains refraction. For matter, add up (kinetic energy minus potential energy) over time along a path: the real path is the one where that sum is stationary. The integrand is the **Lagrangian**; the Euler-Lagrange equations turn the principle into equations of motion. Forces and vectors disappear; only energies are needed.
- **Trade-off**: Lagrangian mechanics replaces hard vector bookkeeping with simple scalar functions and extends unchanged to relativity and quantum theory; but it is hard to say what action *is*.
- **Does not hold when**: asked as a fact about purpose. "Nature minimizes" is a compact summary of the equations, not an agent choosing.

## 1.7 Action across theories: proper time and the path integral
- **Thesis**: pushing the action principle into relativity and quantum theory sharpens what action means.
- **Mechanism**: in relativity the action becomes the integral of **proper time**, the time an object itself measures; free-fall paths are the ones extremising proper time, and Fermat's least time is the special case for massless light. In quantum mechanics a particle does not take one stationary path; it explores *all* paths, each weighted by a phase set by its quantum action. Phases cancel where the action varies fast and add where it is stationary, so the classical path emerges as the dominant one (path-integral formulation, equivalent to wave mechanics and matrix mechanics). The space being explored is **configuration space** (all possible trajectories allowed by constraints), which becomes configuration spacetime in relativity and a state space in quantum theory. Each quantum field has its own Lagrangian; summing them gives the standard model Lagrangian.
- **Trade-off**: unifying and predictive; but "action is more fundamental than energy, entropy or even time" is a **(position)**, not an established result.
- **Does not hold when**: quantised gravity, where it is open what plays the role of the spacetime path being summed over.

## 1.8 Two self-consistent pictures: let experiment decide
- **Thesis**: internal consistency does not pick a theory; agreement with measurement does.
- **Mechanism**: flat spacetime with gravity as an added force and curved spacetime without a gravitational force can both be made consistent. A measurement settles it (ch02): gravitational time dilation, however small, is impossible in flat spacetime. When two models agree on the data, prefer the simpler (Occam), but age is not a reason; a long-standing model deserves trust only to the extent it passed *additional* tests.
- **Trade-off**: waiting for decisive data can take decades.
- **Does not hold when**: the models make identical predictions in every accessible regime; then the choice is interpretive (ch03).

## 1.9 Modern cosmology-style inference: rule out the universes you are not in
- **Thesis**: when no observation measures a parameter directly, you learn by eliminating parameter sets inconsistent with several different observations.
- **Mechanism**: each probe (supernova distances, baryon acoustic oscillations, weak lensing, the cosmic microwave background) responds to a *combination* of parameters. Like finding two numbers from their sum and product, each probe leaves **degeneracies** and several together remove them. Probes must be checked for shared assumptions and shared data; this shared uncertainty is **covariance**, and ignoring it is like polling 100 people who read the same rumour.
- **Trade-off**: more probes shrink the allowed region, but combined results are only as independent as the probes are.
- **Does not hold when**: the probes share systematic errors (same calibration, same galaxies) that nobody modelled; the combined confidence is then overstated.

## 1.10 Constructor-style framing (position)
- **Thesis (position)**: instead of searching for the equation of one phenomenon, ask which tasks are possible or impossible and let that narrow the space of allowed laws.
- **Mechanism**: constraints from observation keep shrinking the set of candidate laws; the hope is convergence to one, or to an infinite family.
- **Trade-off**: a possible perspective shift; no confirmed new predictions exist so far (dated).
- **Does not hold when**: it is presented as a finished theory; it is generally treated as an unproven programme, and critics call it a reframing.
