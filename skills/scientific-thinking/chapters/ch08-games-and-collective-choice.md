# Chapter 08: Games and Collective Choice

## Core Idea
In this model, outcomes depend on **the structure of the interaction**: who moves, how often, with what information, and what is rewarded. The same individually rational move can produce collective disaster in a one-shot game and cooperation in a repeated one; and no voting rule can satisfy all of a short list of reasonable fairness conditions at once.

## 8.1 The prisoner's dilemma
- **Thesis**: when each side gains by defecting whatever the other does, both defect and both lose.
- **Mechanism**: payoffs: both cooperate, 3 each; one defects while the other cooperates, 5 for the defector and 0 for the other; both defect, 1 each. Defecting is better against either move, so rational players end at 1 each when they could have had 3. An arms race fits this pattern: both sides spent enormous sums on arsenals that neither could use. Animals that groom each other face the same structure.
- **Trade-off**: formalising the game strips context (trust, institutions, communication).
- **Does not hold when**: interaction is repeated, communication or binding agreements exist, or payoffs differ so that cooperation dominates.

## 8.2 Repeated play and the tournament
- **Thesis**: with an indefinite future, a simple conditional strategy beats cleverness.
- **Mechanism**: in a computer tournament, strategies submitted by experts played many rounds against each other. The winner was the simplest: cooperate first, then copy the opponent's last move. The top performers shared four qualities: **nice** (never defect first), **forgiving** (retaliate once, then return to cooperation), **retaliatory** (do not be a pushover), **clear** (opponents can understand and trust it). Nasty strategies lost in the long run even though they could not lose a single match. A variant that only retaliated after two defections would have won the first round.
- **Trade-off**: the strategy can never beat its partner in a pairwise match; it wins by getting cooperation from many.
- **Does not hold when**: opponents are always-defect (the strategy loses), the number of rounds is known (backward induction leads to defection in the last round and then all the way back), or the stakes of one defection are catastrophic.

## 8.3 Uncertain end, noise and generosity
- **Thesis**: a known end destroys cooperation; noise destroys strict reciprocity.
- **Mechanism**: if the last round is known, defect there; knowing that, defect in the one before, and so on to round one. Randomising the number of rounds restores the incentive. When there is a small chance that a cooperative move is read as a defection, two strict reciprocators fall into alternating retaliation, then permanent mutual defection, earning about a third of the perfect-world score. Adding about 10% generosity (not retaliating one time in ten) breaks the echo. Real errors exist: a warning system once mistook sunlight on clouds for missiles.
- **Trade-off**: generosity invites some exploitation.
- **Does not hold when**: detection of defection is perfect.

## 8.4 No single best strategy; the ecology matters
- **Thesis**: a strategy's score depends on who else is playing.
- **Mechanism**: a strategy that won one tournament came 24th in a second with a different population; against only always-defect players it comes last. Letting successful strategies multiply and unsuccessful ones vanish (an ecological simulation) favoured nice strategies in the long run; a nasty strategy that preyed on forgiving ones first grew and then declined as its prey disappeared. A small cluster of reciprocators in a hostile population can accumulate enough from mutual cooperation to spread.
- **Trade-off**: simulation conclusions depend on the payoff matrix and the population.
- **Does not hold when**: you assume the tournament result generalises to any environment; later work varied payoffs, noise and mutation, and the winner changes, though the basic lessons of niceness, forgiveness and not being a pushover broadly hold.

## 8.5 Most of life is not zero-sum
- **Thesis**: you win by getting reward from the environment, not necessarily by beating the opponent.
- **Mechanism**: a reciprocal strategy never wins a head-to-head, and yet comes out ahead overall; an always-defect strategy never loses a match but scores poorly. In zero-sum games (chess, poker) your gain is their loss; in positive-sum interactions, the reward comes from outside. The practical question is: is there a win-win here, and how do we make cooperation checkable? Arms reduction was organised in small steps with mutual verification, which converts a one-shot dilemma into a repeated game.
- **Trade-off**: mixed cases exist; some contests are zero-sum.
- **Does not hold when**: resources are fixed and exclusive.

## 8.6 Newcomb's problem
- **Thesis**: two valid lines of reasoning, one about evidence and one about causation, give opposite answers.
- **Mechanism**: a very accurate predictor fills an opaque box with a large sum only if it predicted you would take that box alone; a transparent box has a small sum. You choose one or both. Taking both dominates in every fixed state of the boxes (the contents are already set). Taking one has a higher expected return once you condition on the predictor's record: above roughly a 50% accuracy, the expected value of one-boxing exceeds that of two-boxing. Opinion in a large poll was close to evenly split, with a majority in the one-box camp online. Two decision theories: **evidential** (condition on what your choice indicates) and **causal** (consider only what your choice can cause).
- **Trade-off**: each theory has a case where it seems to fail: causal theory leaves you poorer, evidential theory seems to treat correlation as influence.
- **Does not hold when**: the predictor is not reliable or the problem is placed in a setting where your choice can truly influence the box (for example a predictor that looks into the future).
- **Position**: the problem is less about the right answer than about what it reveals about rationality and free will; the reputational, repeated and pre-commitment versions all push toward one-boxing.

## 8.7 Pre-commitment and credible threats
- **Thesis**: binding yourself to a worse option in some states can produce a better outcome overall.
- **Mechanism**: a deterrent works only if retaliation is credible; but once the attack has happened, retaliating is irrational (all lose). So societies create automatic or institutional commitments. In the game of chicken, visibly throwing away the steering wheel makes you unable to swerve and forces the other to. A fictional doomsday device that triggers automatically makes the threat credible, but only if the adversary knows it exists. A person who adopts rules that would have been good to commit to (the one-box rule) acts well even in cases where, in the moment, defecting would pay.
- **Trade-off**: commitments are dangerous if the circumstances were misjudged, or if the device is triggered by error.
- **Does not hold when**: you cannot make the commitment visible, or an error rate in the trigger is unacceptable.
- **Level confusion**: a rational society may be made of cooperators who, individually, are not maximising in each one-shot move; rationality at one level can differ from rationality at another.

## 8.8 Voting rules and their pathologies
- **Thesis**: every common method of counting votes has a failure mode.
- **Mechanism**:
  - *Plurality (first past the post)*: the most votes wins. Minority rule is common (in one legislature, a party holding a majority of seats had a majority of the vote in only 2 of 21 cases over a century). Similar candidates split the vote (spoiler effect), which pushes voters into voting strategically and drives systems toward two parties.
  - *Instant runoff (ranked choice)*: eliminate the weakest and redistribute. It reduces spoilers and in practice encourages cordial campaigns (candidates need second preferences), but it can fail monotonicity: a candidate can win by doing worse in the first round.
  - *Borda count*: points by rank. Irrelevant extra candidates can change the winner.
  - *Condorcet method*: pick the one who beats every rival head to head. It may not exist: with three options each preferred to another in a cycle (burgers beat pizza, pizza beats sushi, sushi beats burgers), there is no winner.
- **Trade-off**: simpler systems are easier to count and explain, more complex ones offer more fairness properties but harder to audit.
- **Does not hold when**: only two candidates run, in which case majority rule works.

## 8.9 The impossibility theorem
- **Thesis**: no ranked-ballot system with three or more options can satisfy five reasonable conditions at once.
- **Mechanism**: the conditions: *unanimity* (if everyone prefers A to B, so does the group); *no dictator* (no single voter decides regardless of the others); *unrestricted domain* (any set of rankings is allowed and yields a unique group ranking); *transitivity* (if A over B and B over C, then A over C); *independence of irrelevant alternatives* (the group's A-versus-B ranking depends only on how voters rank A versus B). The proof shows that you can find a pivotal voter whose switch changes the group ranking, and that this voter ends up deciding for the group: a dictator. The result says that every ranking-based rule gives something up.
- **Trade-off**: dropping a condition (usually independence of irrelevant alternatives) is the common path.
- **Does not hold when**: the voters' preferences are structured so a median voter exists, or the ballot is not a ranking.

## 8.10 Ways out
- **Thesis**: restricting the setting or changing the ballot escapes the theorem.
- **Mechanism**: if voters and candidates lie along one dimension (a left to right spectrum), the median voter's preference reflects the majority and cycles disappear. Rating or approval ballots (tick all you approve, or score each candidate) are not ordinal rankings, so the theorem does not apply. Approval voting was reported to raise turnout, reduce negative campaigning and remove spoilers, and is simple to count; it was used for centuries in some elections and is used for a major international post.
- **Trade-off**: approval ballots need voters to decide where to put a threshold, and limited real-world testing at scale exists; a different class of strategic-voting problems arises.
- **Does not hold when**: preferences are multidimensional and polarised; the single-peak guarantee fails.
- **Position**: "democracy is mathematically impossible" is a misreading; the theorem says a certain kind of ideal aggregator does not exist, not that voting is useless. Choose a method knowing which property you are sacrificing.

## Cross-references
Chapter 03 for decisions under risk; chapter 07 for ecological/evolutionary stories; chapter 09 for the structure of impossibility proofs.
