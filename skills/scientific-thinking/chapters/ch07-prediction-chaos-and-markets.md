# Chapter 07: Prediction, Chaos and Markets

## Core Idea
In this model, **being deterministic does not make a system predictable**. Chaos, noise and feedback set horizons beyond which forecasts are no better than guesses. What can still be predicted is structure: ranges, attractors, distributions and the sign of change. In markets, the same logic means prices behave like random walks, and persistent edges are rare and shrink when discovered.

## 7.1 The determinist's promise and why it fails
- **Thesis**: if you knew every position and velocity you could, in principle, compute the future; in practice this fails for many systems.
- **Mechanism**: the thought experiment of an all-knowing calculator was inspired by the success of celestial mechanics, where eclipses can be predicted centuries ahead. The idea works for a pendulum, whose state can be drawn in a phase space of angle and velocity: a damped pendulum spirals into a fixed point, a frictionless one traces a closed loop, curves never cross because each state has one future. But add a third body to two orbiting bodies and no general solution exists.
- **Trade-off**: simple solvable systems are over-represented in teaching, which gives a false sense of generality.
- **Does not hold when**: the system is linear or weakly nonlinear and its state is well measured.

## 7.2 Sensitive dependence on initial conditions
- **Thesis**: in a chaotic system, tiny differences in the starting state grow exponentially.
- **Mechanism**: a weather model was re-run from mid-printout values rounded to three decimals instead of six; within a short time the new run diverged completely from the original. A three-variable toy model of convection shows the same behaviour: fully deterministic, never repeating, never settling, with nearby trajectories separating. The pair of connected pendulums and several magnet-coupled spinners are further examples. Even the solar system, seen as the model of order, is chaotic on a time scale of roughly four million years.
- **Trade-off**: knowing chaos is present tells you not to over-invest in precision of initial data.
- **Does not hold when**: the system is stable (all trajectories converge) or the horizon is short relative to the divergence time.

## 7.3 Forecast horizons and ensembles
- **Thesis**: forecast skill decays with horizon; at some point it is worse than simply quoting the historical average.
- **Mechanism**: studies of weather suggest that by about the eighth day, a long-range forecast is less accurate than climatology (the long-run average for that date). Modern practice therefore runs ensemble forecasts: many runs with perturbed starting conditions and model parameters, producing a spread whose width is itself information. The same logic applies to any prediction in a noisy system: report ranges, not a point.
- **Trade-off**: ensembles cost compute and make the message less crisp.
- **Does not hold when**: the audience needs a single decision; then convert the distribution into an action with stated probability.

## 7.4 Strange attractors: unpredictable paths, predictable shape
- **Thesis**: chaos has structure; trajectories wander over a bounded, geometrically complex set.
- **Mechanism**: in the convection model, nearly all starting conditions end up moving on the same butterfly-shaped set. Individual states cannot be forecast far ahead, but the collection of states has a shape. Practical use: ask what statistics of the system are stable (long-run frequency, bounds, typical transitions) even when the next value is not.
- **Trade-off**: summary statistics throw away the timing.
- **Does not hold when**: the system's rules change over time.

## 7.5 The logistic map: simple rule, complex behaviour
- **Thesis**: a very simple growth model with a negative feedback shows order, cycles and chaos as one parameter increases.
- **Mechanism**: next population = growth rate x population x (1 - population), with population as a fraction of the maximum. For growth rates below 1 the population dies out; between 1 and 3 it settles to a constant; just above 3 it alternates between two values, then four, eight and so on (period-doubling); at about 3.57 the behaviour is chaotic; inside the chaos there are windows of order (for example a three-cycle near 3.83). The doubling points converge at a fixed ratio of about 4.669 that holds for a whole family of single-hump functions, a universality property. The same sequence appears in a rolling fluid heated from below, in the flicker response of eyes, in the dripping of a tap as flow rate rises, and in the route to heart fibrillation in animals, where chaos theory was used to time corrective shocks.
- **Trade-off**: the equation is a caricature; real populations have many drivers.
- **Does not hold when**: delays, noise or many interacting variables dominate; then the clean diagram blurs. Experiments in controlled settings match better than wild populations.
- **Use**: it is a reminder that complex output does not need a complicated cause; and that regular boom-bust cycles can arise from internal dynamics without any external shock.

## 7.6 What chaos does to causal stories
- **Thesis**: the "butterfly effect" is about prediction limits, not about every choice mattering equally.
- **Mechanism**: it is true that small causes can amplify, which limits both forecasting and tracing a present state back to a single initial cause (a fog on both sides of the present). It is not true that all small decisions have large foreseeable consequences; in most systems small changes die out.
- **Trade-off**: popular use turns it into regret-or-fate narratives.
- **Does not hold when**: the system is dissipative and stable.

## 7.7 Information, randomness and free choice
- **Thesis**: information is order that can be compressed; maximally informative data look random.
- **Mechanism**: language is about 75% redundant, so it compresses; a perfectly ordered string carries no information; a random string cannot be compressed and carries the most. If the universe were deterministic from an initial state, its total information would be constant; the observed increase of entropy suggests new information is being generated, and the most natural candidate is quantum measurement, which is probabilistic. Chaotic amplification could then carry quantum events up to macroscopic scale.
- **Trade-off**: this is a speculative connection (offered as a speculation), and interpretations of quantum mechanics differ.
- **Does not hold when**: you adopt an interpretation without intrinsic randomness. Treat claims about free will as philosophy, not as a result.

## 7.8 Markets as random walks
- **Thesis**: if prices already reflect available information, next price changes are unpredictable, like a coin flip, and a population of random walks yields a bell-shaped spread that widens with time.
- **Mechanism**: the argument is that if people could predict tomorrow's rise they would buy today, moving the price now and erasing the predictability. A ball falling through a board of pegs is the model: each peg is a 50/50 choice, no single path can be predicted, but the pile is a normal distribution that widens with more rows. The same mathematics describes heat spreading and the jiggling of microscopic particles in a liquid, which is evidence that atoms exist.
- **Trade-off**: pure randomness ignores drift (companies grow or fail) and ignores fat tails.
- **Does not hold when**: markets are inefficient or have identifiable patterns.
- **Contested**: whether markets are efficient. At least one long-lived data-driven fund earned returns far above the market average for decades using large amounts of data, hidden state models and many hired scientists; the author of a study of it concluded that the efficiency hypothesis can be rejected in the data. But such performance is very rare, hard to verify from outside, and if everyone found the patterns they would vanish, which pushes markets back toward randomness.

## 7.9 Option pricing and dynamic hedging
- **Thesis**: a derivative can be priced by constructing a portfolio that removes risk.
- **Mechanism**: a call option gives the right, not the obligation, to buy at a set price; a put gives the right to sell. Options limit downside to the premium, add leverage (bigger percentage gains and losses), and enable hedging. A hedger who sold an option holds a computed amount of the stock so that gains and losses offset, rebalancing as the price moves (dynamic hedging). If the hedged portfolio is riskless it must earn only the risk-free rate in an efficient market, which, combined with a random-walk-plus-drift model of prices, gives a differential equation whose solution is an explicit pricing formula. Once the formula was adopted, trading volume in listed options exploded and related markets grew to many multiples of the underlying securities.
- **Trade-off**: derivatives spread risk and add liquidity in normal times, but can move together in a crash and concentrate leverage.
- **Does not hold when**: price jumps, volatility changes, liquidity vanishes, or hedging cannot be done continuously; model assumptions fail under stress.
- **Use**: an early failure in applying math to money is a reminder that skill with equations does not remove exposure to crowd behaviour: a very accomplished calculator of planetary motion lost about a third of his wealth by buying into a bubble and averaging down.

## 7.10 What is predictable: eclipses and the three-body problem
- **Thesis**: some motions are predictable far ahead because they repeat, even when the underlying problem has no neat solution.
- **Mechanism**: long records of the Moon and Sun showed three nearly periodic cycles: the phase cycle (about 29.5 days), the cycle in which the Moon crosses the plane of the Sun's apparent path (about 27.2 days), and the cycle of its apparent size (about 27.5 days). After 6585 days and 8 hours (about 18 years, the saros) the three nearly realign, so an eclipse similar to an earlier one occurs. The cycle predicts roughly when, not where. Prediction to within a second or two, for centuries ahead, needs a model of the Earth, Moon and Sun with their gravitational pulls (the three-body problem, which has no general closed-form solution), solved numerically with accumulated corrections. In this model, the lesson is that empirical cycles can predict without mechanism, and that numerical models can predict a regular system well even when no formula exists.
- **Trade-off**: the cycle needs no theory but gives limited detail; the numerical model gives detail but needs good data and a correct model.
- **Does not hold when**: the system is chaotic over the horizon of interest (see 7.2 and 7.3); eclipse prediction works because the relevant motions are well behaved over centuries.

## 7.11 Randomness: ignorance, intrinsic chance and camouflage
- **Thesis**: a process can look random because of ignorance, because of intrinsic chance or because we have not found its pattern.
- **Mechanism**: a coin toss is deterministic: a machine can control it to land as desired. Practical biases exist: a coin thrown in a standard way tends to land with the face that was up at the start slightly more often (about 51% in one study), spinning a coin on its edge gives larger biases because of the weight distribution (a heavier side down, as often as 80% for some coins), and a thick enough coin occasionally lands on its edge (about once in several thousand throws for one coin). Dice are made to tolerances of a few micrometres, which can show as small biases. Intrinsic randomness is a different thing: quantum events such as the time of a particular radioactive decay cannot be predicted even with full knowledge, only their probabilities. A random process can generate readable patterns by chance, and is easier to rule out than to confirm.
- **Trade-off**: assuming randomness simplifies models; assuming determinism calls for the full state.
- **Does not hold when**: a "random" sequence has been designed; test it and use a certified generator.
- **Use**: to be fair with a coin, catch it in the hand instead of letting it bounce and spin.

## Cross-references
Chapter 05 for pundits and low-validity environments; chapter 09 for Markov chains and simulation; chapter 03 for risk. Chapter 13 for the everyday sense of "random"; chapter 16 for time, randomness and the future.
