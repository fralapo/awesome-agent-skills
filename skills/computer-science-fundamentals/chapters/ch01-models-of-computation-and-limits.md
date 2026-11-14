# Chapter 1: Models of Computation and Their Limits

## Core Idea
A model of computation says what a machine may do in one step; what can be computed, how fast it can be computed and what can never be decided are properties of the model, not of a particular computer. In this model the useful habits are: know that very different devices compute the same things, know which questions no program can answer, and know which questions are answerable but hopeless at scale, so that heuristics are chosen on purpose and not by surprise.

## 1.1 The Turing machine as the reference model
- **Thesis**: an unbounded tape of symbols, a head that reads, writes and moves, and a finite table of rules is enough to compute anything a physical computer computes; no device found so far computes more.
- **Mechanism**: a machine holds a current state; given the symbol under the head, the rule table says which symbol to write, whether to move left or right, and which state comes next. A set of "cards" (one per state) is a program. A computer's CPU, registers and memory are an engineering version of the same idea with a finite, addressable tape.
- **Trade-off**: the model is a tool for proofs, not for performance; moving a head along a tape is a terrible cost model for real hardware.
- **Does not hold when**: you reason about speed, memory hierarchy or parallelism; use a cost model for the actual machine (ch4). The statement "nothing computes more" is an observation about all models proposed so far, not a theorem (position).

## 1.2 Counter machines: a much poorer machine that is just as powerful
- **Thesis**: a machine with no tape, only a few counters that can be incremented, decremented and tested for zero, can simulate a Turing machine; so power does not come from rich operations but from unbounded storage plus conditional looping.
- **Mechanism**: you may not look inside a counter, only ask "is it empty?". Small programs build everything else: reset (decrement until empty); add counter B into A (loop: take one from B, put one into A, until B is empty, which destroys B); copy (move through a temporary counter, then move back). To simulate a tape, store the part left of the head as one number, the part right of the head as another, and the symbol under the head in a third. Moving the head is doubling one counter (and adding the symbol) and halving another (the remainder becomes the new symbol); reading a symbol means draining a counter into a temporary one and testing; writing means reset then add. Encoding several counters in one number (for example with prime factorisation) reduces the number of counters; the full construction is not detailed here (unverified).
- **Trade-off**: each simulated step costs many counter steps; the point is expressiveness, not speed.
- **Does not hold when**: you need an efficient program; the simulation is exponentially slower than direct code.

## 1.3 Undecidability and the halting question
- **Thesis**: some well-posed questions about programs have no algorithm that always answers; "will this program stop?" is the standard one.
- **Mechanism**: a program can stop, loop forever or run without bound; there is no general procedure that tells which. Detecting a repeating pattern works for simple machines (a one-state machine that writes ones forever is obviously looping), but a machine may use a huge amount of tape, come back and overwrite it, and cycle with a period too long to notice. Proof technique: diagonalisation (see 1.5).
- **Trade-off**: practical tools must give up completeness or soundness: they time out, restrict the language, or answer "unknown".
- **Does not hold when**: the programs are restricted (a language without unbounded loops, a finite-state machine); then termination and equivalence become decidable.

## 1.4 The busy beaver game: fastest-growing "function" you can define
- **Thesis**: the question "what is the largest number of ones a halting machine of size n can leave on its tape?" has a definite answer for each n, yet no algorithm can compute it, and it outgrows every computable function.
- **Mechanism**: a machine of n cards has, per card, two cases (symbol read), each with a symbol to write, a direction and a next card (including "halt"). The count of machines of size n is (4(n+1))^(2n): 64 for one card, 20,736 for two (figures as stated). For one card the best score is 1. For four cards the best score stated is 13, found by enumerating and by proving most non-halting cases looping; a few rogue machines needed human arguments. For five cards the answer was still unknown when the figures were stated; for six a lower bound is stated around 10^10,500 (dated claim; later results may have changed it, check before quoting). Growth: eventually larger than the Ackermann function, because it exceeds every computable function.
- **Trade-off**: the game is useless as a tool and valuable as an illustration: "a perfectly innocent question" can hide undecidability.
- **Does not hold when**: you want a practical algorithm; nothing here helps compute anything.

## 1.5 Incompleteness: a system that can talk about itself cannot settle everything
- **Thesis**: any consistent formal system that includes elementary arithmetic (addition and multiplication over the natural numbers) contains true statements it can neither prove nor refute, and it cannot prove its own consistency.
- **Mechanism**: (a) encode every formula as a natural number (obvious to a programmer: a formula is bytes, bytes are a number). (b) Encode "provable" as a predicate on those numbers, inside the system itself; arithmetic is rich enough to do this with heavy bookkeeping. (c) By diagonalisation (apply a predicate to its own code), build a sentence G that says, in effect, "my own code is not provable". If G were provable, the system would prove something false about provability and be inconsistent; if its negation were provable, likewise. So a consistent system proves neither. (d) The second theorem follows by formalising that argument one level up: the system cannot prove "false is not provable".
- **Trade-off**: adding G as a new axiom just produces a new system with a new unprovable sentence; completeness cannot be bought by adding axioms.
- **Does not hold when**: the system is weaker. Arithmetic without multiplication is complete (but cannot talk about itself); the theory of real numbers as a field and classical Euclidean geometry (points and lines) are complete. A common philosophical reading (that the theorem proves something about minds or about the universe) is not supported by the theorem (position).

## 1.6 Diagonalisation, a reusable technique
- **Thesis**: the same trick, feeding a thing its own description and flipping the answer, proves several different limits.
- **Mechanism**: it shows that no program decides halting, that the real numbers are more numerous than the natural numbers, and (in 1.5) that provability cannot be complete. Whenever a claim says "a general checker exists for all programs of kind X including itself", try diagonalisation first.
- **Trade-off**: it proves impossibility without telling you what to do instead.
- **Does not hold when**: the checker is not allowed to see itself (restricted classes again).

## 1.7 P, NP and what "hard" means
- **Thesis**: complexity classes separate problems whose solutions can be found in polynomial time (P) from problems whose solutions can at least be checked in polynomial time (NP); whether the two are the same is open.
- **Mechanism**: sorting names takes time roughly proportional to n or n log n: P. Boolean satisfiability, scheduling, the travelling-salesman problem over n cities (n-1 factorial routes; for 15 cities about 87 billion), and many puzzle problems are in NP: a proposed answer can be checked quickly, finding one seems to need exploring exponentially many cases. NP-complete problems are the hardest of NP: a polynomial algorithm for any one would give one for all, because each can be translated into any other. Satisfiability was the first problem shown to be NP-complete. Nobody has proved P = NP or P ≠ NP; most people believe they differ; known proof techniques run into barriers.
- **Trade-off**: because exact answers may be out of reach, real systems use heuristics that find good, not provably best, answers in reasonable time, trading optimality for time (see ch2 for annealing and search heuristics).
- **Does not hold when**: instances are small or structured; exact solvers for specific NP-hard problems routinely solve huge structured instances. "Easy to verify, hard to find" is also the backbone of public-key cryptography (multiplying two primes is easy, factoring the product is believed hard, but not proven hard); if P = NP were true with a practical algorithm, much of today's cryptography would be in trouble, which is a commonly stated consequence rather than a proof.

## 1.8 Growth rates: reading Big-O correctly
- **Thesis**: complexity notation describes how cost grows with input size, so scaling behaviour matters more than constants for large inputs.
- **Mechanism**: constant, logarithmic, linear, n log n, polynomial, exponential, factorial, and then faster-than-any-computable (busy beaver) form a ladder. Doubling the input adds one step in a logarithmic algorithm and doubles the cost of a linear one. Both time and memory (space) are measured.
- **Trade-off**: a better asymptotic class can lose to a simpler algorithm on small inputs or on hardware that likes the simpler access pattern (ch3, ch4).
- **Does not hold when**: the input is small, the constants dominate, or the cost is not the one measured (memory traffic, I/O).

See also: ch11 (how to reason about these limits in practice); `ai-ml-concepts` for learning-theoretic limits (generalisation, overfitting).
