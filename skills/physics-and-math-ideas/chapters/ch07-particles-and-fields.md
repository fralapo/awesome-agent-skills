# Chapter 07: Particles, Fields, Forces and Electromagnetism

## Core Idea
In this model particles are the quantised vibrations of fields, forces come from gauge symmetries (ch01.5), and the shape of a field's energy landscape decides whether symmetry is visible or hidden. The chapter also holds the counting rules that divide particles into two families and the delicate handling of infinities in field calculations.

Fields: **Thesis**, **Mechanism**, **Trade-off**, **Does not hold when**. *General knowledge* and **(position)** are marked.

## 7.1 Quantum fields and particles
- **Thesis**: a quantum field is the fabric that can vibrate at each point; its quantised vibrations are the particles.
- **Mechanism**: like a drum's vibrational modes, but every point of space can wiggle, twist and oscillate; the wiggles come in discrete packets that can move around. Light is a vibration of the electromagnetic field (and a wave in it); fundamental particles are waves in their own fields. A field's energy-versus-strength shape (potential) and its kinetic term form a Lagrangian (ch01.6); the standard model is the sum of such terms.
- **Trade-off**: unified language; abstract.
- **Does not hold when**: gravity: it is not part of the standard model (ch02, ch04, 7.5).

## 7.2 Fermions and bosons from counting
- **Thesis**: whether particles may share a state changes the statistics, which changes the matter that results.
- **Mechanism**: for distinguishable particles the most probable energy distribution is the Maxwell-Boltzmann one (ch06.1). For *indistinguishable* particles, swapping labels is not a new microstate, so the count is wrong unless corrected. Counting correctly gives **Bose-Einstein statistics**: unlimited particles per energy state; a "minus one" in the formula makes little difference at ordinary energies but a huge one at very low energy, where many particles pile into the lowest state (a **Bose-Einstein condensate**: superfluidity, superconductivity-type behaviour). If a state can hold only one particle, **Fermi-Dirac statistics** apply. Spin links to the family: integer spin gives bosons (force carriers such as the photon), half-integer spin gives fermions (electrons, protons, neutrons, most matter). Composites of fermions can be bosons (a helium-4 atom).
- **Trade-off**: one counting rule explains why matter has structure (fermions refuse to overlap) and why condensates exist (bosons can).
- **Does not hold when**: the "refusal to share" is read as a force; it is a statistical/quantum rule. The deep reason (spin-statistics) is not derived here.

## 7.3 Spontaneous symmetry breaking and the mass of the weak bosons
- **Thesis**: a symmetric law can have an asymmetric lowest-energy state; this hides a gauge symmetry and gives massive gauge bosons without breaking the law's form.
- **Mechanism**: the weak force from SU(2) symmetry predicts three massless carriers, but the real carriers are heavy; a massive gauge boson seems to break gauge symmetry (and a massless-gauge-boson theorem seems to forbid mass). Also, the charges of weak isospin and hypercharge are tied to electric charge, which separate U(1) and SU(2) cannot explain; combining them (U(1) x SU(2)) gives photon-like and weak-like fields that are still massless and unlinked. Idea: **spontaneous symmetry breaking**. Magnets: above a temperature, random motion wins and no direction is preferred; when cold, all align, although the equations have no preferred direction. Ball and landscape: a symmetric valley; change the sign of the mass term and the valley becomes a "Mexican hat" with a hilltop; the field rolls to a random point on the brim. The shape of the potential keeps the symmetry, the state chosen does not.
- **Trade-off**: explains massive carriers while keeping the symmetric laws; this is the **Higgs mechanism** (the finishing steps, in which the gauge field absorbs the extra degree of freedom and becomes massive, are omitted here; *general knowledge*).
- **Does not hold when**: used to say that "the Higgs gives everything mass": it gives mass to the weak bosons and (in the standard model) to the fundamental fermions, not to most of the mass of ordinary matter (*general knowledge*).
- **Measurement note**: a decade-long measurement of the mass of the W boson reported a value about 0.1% heavier than expected; it was described as a tantalising hint of deeper physics. Not confirmed by later measurements (as of 2024); treat as unconfirmed (dated).

## 7.4 Infinite sums, regularisation and the Casimir effect
- **Thesis**: the claim "1 + 2 + 3 + ... = -1/12" is false as an ordinary sum; the -1/12 is the finite part left after **regularisation**, and it has real, measured consequences.
- **Mechanism**: a convergent series (a half plus a quarter plus an eighth ... equals one) has a value; the natural numbers sum diverges. The Riemann zeta function, defined by the series for s greater than 1, can be analytically continued; at s = -1 it is -1/12. That is a regularised value, not the sum. **Casimir effect**: two conducting plates exclude modes of the quantum electromagnetic field; only modes with an integer number of half wavelengths fit. Total energy is a base energy times 1 + 2 + 3 + ..., infinite for both inside and outside, so introduce a cutoff (high-frequency modes stop noticing real metal) and compare: subtract the divergent part common to inside and outside. A finite remainder times the zero-point factor gives an energy that decreases as the plates approach, so an attractive force, which has been measured. In the realistic three-dimensional case (two polarisations, parallel momentum) the factor becomes 1/120 instead of -1/12. In **string theory** the same sum appears from closed-string modes and the cutoff feels less ad hoc because high-frequency modes are local and do not affect the global energy spectrum.
- **Trade-off**: infinities handled by subtraction work and match experiment; they are not proof that infinities are physical.
- **Does not hold when**: used outside regularisation (as arithmetic), or when it is claimed that the unobserved vacuum energy itself is real everywhere (the absolute value is not measurable; only differences are).

## 7.5 Strings (position: unconfirmed theory)
- **Thesis (position)**: one-dimensional strings whose vibration modes are particles could unify all forces with a single free parameter (tension or length scale) instead of 19.
- **Mechanism**: history: models of quark-bound states (mesons as strings of strong force) were replaced by another theory but contained a massless spin-2 mode, which looks like the graviton. Reinterpreting strings at the Planck scale makes them candidates for quantum gravity. Standing waves on a string give discrete frequencies; mass comes from length and tension; vibrational modes fix charge and spin. Strings can merge and split, giving interactions; because the graviton is a loop, not a point, interactions are smeared and avoid the explosion of infinities below the Planck length. The theory needs extra dimensions (nine of space plus time; one more for the unifying M-theory); they are "compactified" into tiny dimensions, and the shape of those dimensions sets the one free parameter. The number of possible shapes is estimated around 10^500 (landscape). Common answers to "what are strings made of" include nothing (fundamental) or a meaningless question.
- **Trade-off**: promise of a unified theory; the price is a huge landscape and a lack of a way to choose or test. It is widely seen as currently at an impasse (position).
- **Does not hold when**: described as established; no confirmed prediction exists so far.

## 7.6 Gauge forces, in one table
| Symmetry | Conserved/charge | Gauge field and carrier | Mass? |
|---|---|---|---|
| U(1) local phase | Electric charge | Electromagnetic field, photon | Massless |
| SU(2) abstract rotation | Weak isospin | Three weak carriers | Observed massive; needs symmetry breaking |
| Colour symmetry | Colour charge | Gluons (strong force between quarks) | See standard model (not detailed here) |

## 7.7 Maxwell's equations: four statements about two fields
- **Thesis**: all of classical electromagnetism is four equations: two say how electric and magnetic fields arise, two say how they behave when changing.
- **Mechanism**: (1) **Gauss's law for electric fields**: the flux of the electric field through any closed surface is proportional to the charge enclosed. A field is a region where you can feel a force; the electric field is a vector at every point; flux counts the component perpendicular to the surface (dot product with the unit normal). (2) *General knowledge*: the equivalent law for magnetic fields states there is no net flux, i.e. no isolated magnetic charge. (3) **Faraday's law**: a changing magnetic flux through a surface produces a circulating electric field around its boundary; if a conductor is present, current flows in the direction that opposes the change (Lenz's law). (4) **Ampere-Maxwell law**: a current *or* a changing electric flux produces a circulating magnetic field; the second term is the addition that makes the set symmetric (changing electric flux makes magnetic field, as changing magnetic flux makes electric field). *General knowledge*: that symmetry is what yields self-propagating electromagnetic waves at a fixed speed, which is light.
- **Trade-off**: enormous practical power (communication, power) from a compact set; the vector calculus hides intuition.
- **Does not hold when**: quantum effects dominate (quantum electrodynamics replaces it).

## Quick checks
- Is "mass" meant as rest mass of a fundamental particle or the mass of a composite?
- Is a divergent expression being treated as a value, or as a regularised difference?
- Does the string claim include a prediction that could fail?
