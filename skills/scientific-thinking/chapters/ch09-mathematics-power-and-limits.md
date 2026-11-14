# Chapter 09: Mathematics: Power and Limits

## Core Idea
In this model, mathematics gives two things that must not be confused: **proof** (certainty within a formal system) and **model-building** (tools that predict and simulate). Both have limits: some true statements are unprovable, some questions are undecidable, and a heuristic that matches the data to high precision is still not a proof. At the same time, mathematical ideas born from abstract disputes have produced practical tools.

## 9.1 Heuristic evidence versus proof
- **Thesis**: a formula can match reality extremely well and still leave the claim unproven.
- **Mechanism**: for twin primes (primes two apart, like 11 and 13), a probabilistic argument based on the density of primes predicts how many should exist up to a limit; by 10^12 the estimate was off by about 0.001%, and enormous twin primes (hundreds of thousands of digits) have been found. Yet it is not known whether there are infinitely many. The estimate assumes primes behave as if independent, which they do not. As a leading mathematician put it, there could in principle be a vast conspiracy in which each number refuses to be prime if its neighbour is.
- **Trade-off**: heuristics guide research and bets; proofs end arguments.
- **Does not hold when**: the claim is only needed in practice, where strong heuristic evidence may be enough (cryptography relies on unproved assumptions).

## 9.2 Trade-offs inside a proof attack: main term versus error
- **Thesis**: much of analysis is a fight between the main term you think is true and error terms you must show are smaller.
- **Mechanism**: a sieve counts primes by removing multiples and then adding back overlaps (inclusion-exclusion). Applied to pairs two apart, the number of rounding errors multiplies faster than the main term grows, so the error swamps the signal. The fix is to sieve with fewer primes, which controls the error but lets in survivors that are not prime but have few prime factors. So the provable result was "infinitely many pairs two apart each having at most a few prime factors", a weaker statement. This is a general pattern: weakening the claim to make it provable.
- **Trade-off**: partial results can be far from the goal.
- **Does not hold when**: a new idea changes the structure of the error.

## 9.3 Bounded gaps: the value of not knowing it is impossible
- **Thesis**: a barrier believed to be fundamental may be an artefact of one method.
- **Mechanism**: an averaging method that slides a "stencil" over the number line and weights positions could show primes come arbitrarily close relative to the average gap, but it hit a ceiling because the supporting distribution theorem only works for step sizes up to the square root of the range. A workshop of experts concluded breaking through was effectively impossible. An unknown mathematician, working alone and not at the meeting, found a way to beat the half-exponent barrier by a tiny margin and proved a bounded gap of 70 million. Soon after, an independent method showed the half was a red herring altogether and got the gap down to 600, then a collaborative online project reached 246. Under a stronger unproven conjecture the gap would be 12, then 6. Once the first proof existed, progress was rapid, much as the four-minute mile was broken repeatedly shortly after the first time.
- **Trade-off**: isolation can free a mind from received wisdom but also from help; most isolated claims are wrong.
- **Does not hold when**: you treat the story as a recipe: the proof was fully checked by experts, which is what separated it from the many incorrect claims such journals receive.
- **Position**: not knowing something is "impossible" can pay; so can a mathematical culture that evaluates arguments on content rather than pedigree.

## 9.4 Sizes of infinity and the diagonal argument
- **Thesis**: not all infinite sets are the same size.
- **Mechanism**: assume you could list every real number between 0 and 1 against 1, 2, 3, and so on. Build a new number whose first digit differs from the first number's first digit, whose second differs from the second number's second digit, and so on. It differs from every number on the list, so the list was incomplete. Therefore real numbers are uncountable, a bigger infinity than the counting numbers. The method (diagonalisation) recurs in later limit results.
- **Trade-off**: the result was rejected by many mathematicians when published.
- **Does not hold when**: you apply finite intuitions (the whole is bigger than the part) to infinite sets.

## 9.5 Self-reference and paradox
- **Thesis**: systems that can talk about themselves generate contradictions unless restricted.
- **Mechanism**: the set of all sets that do not contain themselves contains itself if and only if it does not; a village barber who shaves exactly those who do not shave themselves cannot exist. The repair was to restrict what counts as a set, so that "the set of all sets" is not a set. The cost of that repair is that self-reference came back in other forms.
- **Trade-off**: restriction removes paradoxes but also expressive power.
- **Does not hold when**: you are in an informal setting where self-reference is harmless.

## 9.6 Incompleteness
- **Thesis**: in any consistent formal system strong enough to do basic arithmetic, there are true statements that cannot be proven within it; and such a system cannot prove its own consistency.
- **Mechanism**: assign every symbol a number, then every statement and every proof a unique number (via prime factorisation), so statements about proofs become statements about numbers. Construct a statement that says, in effect, "the statement with this number has no proof", and arrange that the number is its own. If it were false, a proof would exist and the system would prove something false (inconsistent); if it is true, the system contains a true statement with no proof (incomplete). The second theorem says the system cannot certify its own freedom from contradiction.
- **Trade-off**: formal systems lose the dream of capturing all truth; mathematicians continue to work with systems that are very likely consistent.
- **Does not hold when**: the system is too weak to express arithmetic (then it can be complete), or you move to a stronger system, which has its own unprovable statements.
- **Position**: "truth" and "provability" are different. This does not show that any specific famous conjecture is unprovable; it only shows that some statements, unknown to us, are.

## 9.7 Computation, halting and undecidability
- **Thesis**: there is no general algorithm that decides, for every program and input, whether the program will stop.
- **Mechanism**: define an idealised machine with an unbounded tape, a read/write head and a table of rules; anything computable can be done on it. Assume a perfect halting-checker exists, and make a program that does the opposite of what the checker predicts about the program itself: if the checker says it halts, loop; if it says it loops, halt. Contradiction, so the checker cannot exist. Therefore no algorithm can decide, in general, whether a statement follows from the axioms.
- **Trade-off**: you can still run a program and see; the problem is a guarantee of an answer in finite time.
- **Does not hold when**: you restrict to limited classes of programs or accept a "don't know" answer.

## 9.8 Undecidability in the wild
- **Thesis**: any system rich enough to simulate computation inherits its own version of the halting problem.
- **Mechanism**: a simple cellular automaton (cells alive or dead, two rules) can simulate a general computer, so whether a given pattern grows forever is undecidable. The same for whether tiles with coloured edges can cover the plane, and for whether a quantum many-body system has an energy gap (proved in 2015 to be undecidable in general). Many ordinary tools are computation-complete: programming languages, spreadsheets, slide software, card games. The consequence is that exact long-term prediction of a rich enough system by a general method is impossible; you simulate and see.
- **Trade-off**: the property is powerful and dangerous at once.
- **Does not hold when**: a particular instance is easy; undecidability concerns the general case.

## 9.9 Probability with dependence: Markov chains
- **Thesis**: you can do probability with dependent events if the next step depends only on the current state.
- **Mechanism**: the earlier approach to probability required independent events, and some argued that if a social statistic converges (stable counts of marriages, crimes), the underlying decisions must be independent, hence free. A counter-demonstration used the sequence of vowels and consonants in a long text: letters are clearly dependent (a vowel is less likely to follow a vowel than chance predicts), yet the ratio converges to a stable value. A chain of states with transition probabilities reproduces it. Convergence does not prove independence, so it cannot demonstrate free will. The idea of a memoryless process lets a complex history be replaced by the present state.
- **Trade-off**: the Markov assumption can fail; a language model that conditions on more context predicts text better.
- **Does not hold when**: feedback loops and long memory dominate (climate with water-vapour feedback, a model trained on its own output, which collapses into repetition).

## 9.10 Simulation: the Monte Carlo method
- **Thesis**: when a system is too complex to solve, sample it many times.
- **Mechanism**: estimating the chance of winning a card game by playing hundreds of games instead of enumerating about 8 x 10^67 deals. For particles in a nuclear core, each particle's path depends on its position and energy, so independent sampling is not enough; a chain of dependent steps is run many times, the average number of new events per event is recorded, and the distribution tells you whether a chain reaction dies, sustains or grows. The same family of ideas gives modern text generation, link-based ranking of web pages and weather ensembles.
- **Trade-off**: results are statistical, with error that falls slowly as samples grow.
- **Does not hold when**: the model is wrong; sampling a wrong model gives precise wrong answers.

## 9.11 Link-based ranking as a Markov chain
- **Thesis**: importance can be defined as how much time a random surfer spends on a page.
- **Mechanism**: treat pages as states and links as transitions; each link is an endorsement, and endorsements from highly endorsed pages count more, while a page with many outgoing links gives each a smaller share. Running the chain until the time fractions settle ranks pages. Creating many pages that link to yours does not help because those pages have no endorsements. A damping rule (jump to a random page about 15% of the time) prevents getting stuck. The method beat keyword counting, which was easy to game.
- **Trade-off**: once a ranking is valuable, people game it.
- **Does not hold when**: the graph is manipulated at scale.

## 9.12 Shuffling
- **Thesis**: randomness takes more mixing than intuition suggests, and less than a naive guess for a good shuffle.
- **Mechanism**: treat each arrangement as a state and each shuffle as a step. About seven well-made riffle shuffles bring a 52-card deck close to uniformly random; a sloppier method needs thousands.
- **Trade-off**: "random enough" depends on the use.
- **Does not hold when**: a method has structure that preserves part of the order.

## 9.13 Busy beaver: a bounded slice of the halting problem
- **Thesis**: a game that asks "what is the longest a small program can run before stopping" turns undecidability into a concrete ladder of hard problems.
- **Mechanism**: for a fixed number of rules there is a finite group of tape machines; run each from a blank tape; some stop quickly, some never. The number of steps of the longest that does stop is the busy beaver value for that size. Values are known for the smallest sizes (1, 6, 21 and 107 steps for one to four rules) and the next size was settled by a large online collaboration of amateurs, faster than expected. To prove a value, every machine in the group must be classified as halting or not, and some machines behave like unsolved mathematical conjectures. In general knowledge, the values grow faster than any computable function, which is why only a few are known.
- **Trade-off**: the game gives measurable progress on an undecidable question; each new size is enormously harder.
- **Does not hold when**: you only need to know if one specific program halts, which can be easy.

## 9.14 Finding versus checking: P versus NP
- **Thesis**: it is unknown whether every problem whose solution can be checked quickly can also be solved quickly.
- **Mechanism**: complexity theory studies how the time or memory needed grows with problem size. A puzzle that is hard to solve but easy to verify (factoring, scheduling, route planning, logic puzzles with many branching choices) is the typical case. If checking were as easy as finding, many hard problems would be quickly solvable, with large consequences: some forms of encryption would fail, and many optimisation tasks would become easy. Nobody has a proof either way; many specialists expect the two to differ (position, general knowledge).
- **Trade-off**: working algorithms exist for many instances; the theory concerns worst cases and growth.
- **Does not hold when**: a particular instance has special structure that makes it easy.

## 9.15 Cryptography runs on assumed hardness
- **Thesis**: secure communication rests on problems that are hard on average, not just in the worst case, and none is proven hard.
- **Mechanism**: a five-way classification of possible worlds ranges from one where every problem is easy (no cryptography), through worlds where hard instances exist but are rare, or are hard but uselessly so, to a world with minimal cryptographic tools, to one where shared secrets can be established between strangers, which is how current systems work. As far as is known, we live in the last, but that depends on a small number of long-standing methods whose hardness is assumed. Cryptographers are, unusually, hoping that problems are hard.
- **Trade-off**: practical security relies on assumptions that have survived scrutiny, which is empirical, not a proof.
- **Does not hold when**: a new algorithm or computing model changes the cost; quantum computers are the best-known candidate for factoring-based schemes (general knowledge).

## 9.16 Computer-assisted proof
- **Thesis**: a proof that depends on exhaustive machine checking changes what "proof" means without making the result false.
- **Mechanism**: the claim that any map can be coloured with four colours so that neighbours differ was posed in the 19th century; maps are turned into graphs (regions as points, shared borders as lines). A first accepted proof contained an error that was found years later (general knowledge); the eventual proof reduced the problem to a large but finite list of configurations checked by computer, the first major proof to depend heavily on one. This raised a long debate about whether a proof no human can fully read counts, and about what mathematicians do. The related practical problems are the same: timetables, frequency assignment, seating plans.
- **Trade-off**: machine checking is reliable for what it checks and is not human-surveyable; independent re-implementation helps.
- **Does not hold when**: the program or specification is wrong.

## 9.17 Conditional mathematics: results that assume an unproven statement
- **Thesis**: an unproven hypothesis can carry large amounts of mathematics and practice, and the discipline records which results depend on it.
- **Mechanism**: prime numbers seem to appear at random, but their counting follows a very good approximate law, and the finer deviations are tied to an unproven hypothesis about the zeros of a particular function. Many theorems in areas from cryptography to quantum physics are conditional on it: if it were false, those results would fall. It has resisted proof for over 150 years. This differs from the heuristic evidence in 9.1: here a whole network of derived results is built over a single unproven statement.
- **Trade-off**: conditional theorems are useful and risk collapse together.
- **Does not hold when**: a result has an unconditional proof.

## 9.18 Quantum computing changes the rules of probability, not the clock speed
- **Thesis**: a quantum computer is a different kind of device, not a faster supercomputer, and its advantage is specific.
- **Mechanism**: it was proposed because simulating quantum systems on classical machines grows exponentially expensive with the number of particles. Quantum mechanics replaces probabilities with amplitudes, which can add and cancel; algorithms arrange for wrong answers to cancel. Devices are fragile and need isolation near absolute zero.
- **Trade-off**: large speed-ups are known only for some problems.
- **Does not hold when**: the task has no amplitude structure to exploit; a classical machine remains the right tool.
- **Handoff**: for quantum theory proper, see `physics-and-math-ideas`.

## Cross-references
Chapter 01 for theory as compression; chapter 07 for chaos; chapter 02 and 03 for probability in practice. Chapter 14 for infinity, measure, dimension and fluid equations; chapter 15 for universality and complex systems; chapter 16 for far scenarios.
