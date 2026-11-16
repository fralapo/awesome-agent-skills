# Chapter 08: Validation, Backtests and Claimed Results

> Educational concepts, not investment or trading advice. Claimed results below are anonymised illustrations of how claims are made; none is verified.

## Core Idea
In this model, a trading rule is **a hypothesis until it survives a test it could have failed**: fixed in advance, run on data it was not tuned on, net of all costs, with enough independent trades to separate skill from luck. Most results presented to sell a method fail at least one of these conditions. The general statistics of backtests (overlapping windows, survivorship, significance against effect size, overfitting) are in `investing-and-financial-history` ch13; this chapter applies them to trading rules and to the typical shape of claimed performance.

## 8.1 Declared versus verified
- **Thesis**: a result shown by the seller of a method, course, indicator or product is a claim, not evidence.
- **Mechanism**: claims seen in educational trading material, anonymised: a four-hour mean-reversion method reporting 313 trades in 13 months, 82% winners and +246% on a small account opened "as a test"; an automated system reporting +160% in a month with a 25% drawdown; a price-action trader reporting +67% risking 1.5% per trade; "from a few hundred to over ten thousand"; an annual top-30 fundamental-score portfolio reporting about 17% a year over two decades with a 30% maximum drawdown; a momentum index backtest reporting roughly double the broad index over ten years, published by the issuer of a product that had existed for about a month. Common features: one account or one period, no out-of-sample test, incomplete costs, no distribution of outcomes, and a commercial interest.
- **Trade-off**: dismissing every claim also dismisses honest work; the remedy is to ask for what a test needs (8.7), not to assume fraud.
- **Does not hold when**: results are audited, long, net of costs and published before the period they cover (rare).

## 8.2 How many trades are enough
- **Thesis**: short records cannot distinguish a small edge from luck.
- **Mechanism**: with a true 50% hit rate, the standard error of an observed rate over `n` trades is `sqrt(0.25 / n)`. To show a 55% rate is above 50% at about two standard errors needs roughly `(2 x 0.5 / 0.05)^2 = 400` independent trades. A month of results or a few dozen trades says almost nothing. Hit rate alone is not the test anyway: expectancy per trade, net of costs, is (6.1; `investing-and-financial-history` ch13, 13.4).
- **Does not hold when**: the edge is very large, which is itself a reason for suspicion.

## 8.3 Overfitting and parameter drift
- **Thesis**: the more parameters searched, the more the best result reflects noise.
- **Mechanism**: an optimisation over several thousand parameter combinations (one example tested 7,938) will always find a winner; its parameters are, in the practitioner's own words, "not to be reused". A system whose optimal range drifts from one window to the next (an average length moving from 21-25 to 22-27) shows that the past optimum is unstable. A system without any backtest "by choice", whose coefficients are said to stay valid for three to four weeks and are refreshed weekly, cannot be tested at all; its live equity is then the only evidence and is too short. Different data feeds between brokers can change the bars a pattern is computed on, so a pattern found on one feed may not exist on another.
- **Trade-off**: some re-estimation is legitimate when markets change; it must then be tested walk-forward (optimise on one window, trade the next, repeat).
- **Does not hold when**: the rule has few parameters, a stated mechanism, and was fixed before the test.

## 8.4 Confluence does not add probabilities
- **Thesis**: combining signals does not raise the hit rate by a fixed amount each.
- **Mechanism**: one heuristic adds about ten points to a 50% base for each agreeing element (trendline, seasonality, pattern) and claims 60-80% success. Probabilities do not add. If each of three signals alone gave 55% and they were truly independent, combining them by odds would give about 60% for two and 65% for three; correlated signals (all derived from the same price) add far less. Two horizons of the same seasonal statistic, or two oscillators, are close to one signal counted twice.
- **Does not hold when**: signals come from genuinely different information (price, positioning, fundamentals) and their joint value has been tested.

## 8.5 Hit rate, payoff and hidden tails
- **Thesis**: high win rates often come with rare large losses.
- **Mechanism**: mean-reversion and scaling-in methods win often by design: they take small profits and give the market room. A rule with a 90% hit rate and an average loss nine times the average win only breaks even before costs; at ten times it loses. Martingale-like averaging shows smooth equity until one move exceeds its tolerance. Only the full distribution of trade outcomes, including the worst, describes the risk (6.9).
- **Does not hold when**: the stop is fixed and honoured, so losses are bounded.

## 8.6 What academic evidence says (position)
- **In this model**: technical tools organise decisions and enforce discipline; their predictive value is modest and conditional.
- **Rival view, efficiency (general knowledge)**: weak-form efficiency predicts that past prices do not forecast returns net of costs; most professional managers do not beat cheap benchmarks after fees (`investing-and-financial-history` ch02, 2.6).
- **Rival view, data snooping (general knowledge)**: studies that found profitable moving-average and range-break rules on a century of index data later showed that the best rule from a large family is not significant once the search is accounted for, and that apparent profits faded in later periods and after costs.
- **Where some support exists (general knowledge)**: time-series trend following across many futures markets and cross-sectional momentum have long-run records in academic work, with long losing stretches, crash risk and high turnover; seasonal anomalies have often weakened after publication. These are portfolio-level effects, not support for single-chart signals.
- **Reading**: the honest summary is "small, unstable, cost-sensitive edges at best", not "it works" or "it never works".

## 8.7 Checklist for a trading-rule test
1. Was the rule written down, with every parameter, before looking at the test data?
2. How many rules or parameter sets were tried before this one?
3. Is there an out-of-sample or walk-forward period, and how does it compare?
4. Are spreads, commissions, financing (swaps) and slippage included at realistic levels?
5. How many independent trades, and what is expectancy per trade, not only hit rate?
6. What are the maximum drawdown, the longest losing streak and the worst trade?
7. Does it hold on other instruments and periods and with shifted start dates?
8. What is the benchmark (buy-and-hold of the same asset over the same period)?
9. Was the data feed the same one the rule would trade on?
10. Who produced the test, and do they sell the method, the product or the account?

## 8.8 Manual and paper testing
- **Thesis**: a manual walk-through is a sanity check, not a test.
- **Mechanism**: applying a rule bar by bar on past charts, or scanning markets with condition-based screeners, shows how often conditions occur and whether the rule is executable. A screener flags conditions at bar close or on the live bar (which repaints until the close); it is a list of candidates, not a backtest. Demo trading tests execution and psychology but not the edge.
- **Does not hold when**: the tester knows what happened next on the chart being studied.

## Common mistakes
- Reading a claimed return as a measured one.
- Judging a rule by its hit rate.
- Optimising, then "validating" on the same data.
- Counting correlated confirmations as independent.

## Links
- ch04 seasonal statistics, ch05 strategy cards, ch06 drawdown; `investing-and-financial-history` ch02, ch13; `scientific-thinking` for multiple testing and study design.
