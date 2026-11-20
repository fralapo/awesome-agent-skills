# Chapter 13: Return Distribution, Anomalies and Market Regimes

> Educational concepts for reading returns, not investment advice and not a forecast. No market call is made. Macro forecasting belongs to `economics-finance`; this chapter covers only what a trader needs to know about regimes and their effect on rules. Figures are illustrative.

## Core Idea
In this model, a return series is a sample with a shape: it is skewed, it is noisy, and its average is carried by a few observations. Most "edges" are patterns found in such samples. The useful questions are: what is the distribution of outcomes, how much of the signal is noise at the sample size available, does the pattern survive costs and publication, and which regime must hold for a rule to work. Each question has a mechanical answer, and most reported patterns fail at least one of them.

## 13.1 Returns are skewed and concentrated
- **Thesis**: in long-run samples of individual shares, a small minority of companies accounts for most of the wealth created, and the typical (median) company underperforms the index over long holding periods.
- **Mechanism**: returns are bounded below at -100% but not above, so the distribution is right-skewed. The mean of a skewed sample sits above its median. Published long-run studies of listed companies in several markets find that a small share of names produces most of the aggregate gain, while the median stock's lifetime return is below that of the market (general knowledge; re-check the study). A portfolio of a few randomly chosen names can beat the index in a short window by chance, but the result says nothing about selection ability.
- **Trade-off**: a concentrated portfolio can gain from the rare winner and lose from the common outcome. A diversified portfolio reduces the chance of holding no winner and also reduces the chance of holding the biggest one.
- **Does not hold when**: the selection rule was fixed in advance, tested out of sample and shown to capture the right-tail names reliably. Few rules meet that test.

## 13.2 Small samples cannot show skill
- **Thesis**: the noise in a short record is larger than most reported edges.
- **Mechanism**: for an asset with annual volatility `s`, one year's return has a standard deviation of about `s`. The excess return of a strategy against a benchmark has a tracking error that can be large even when the strategy is slightly better on average. A rough test: `t = mean excess return / (tracking error / sqrt(years))`. Illustration: an excess return of 2% a year with a tracking error of 6% a year, over five years, gives `t = 2 / (6 / sqrt 5)` = 0.75, far below the conventional threshold of about 2. A two-year record of a strong result can thus be indistinguishable from chance.
- **Trade-off**: short records are all that most traders have; the honest response is to report the uncertainty, not to act as if the record were long.
- **Does not hold when**: the mechanism is large and measured directly (a contract rule, a fee), not inferred from returns. See ch08 for the test of a rule and `scientific-thinking` for multiple testing.

## 13.3 Anomalies: definition, decay and capacity
- **Thesis**: an anomaly is a return pattern that a baseline model (usually the market, or market plus a few known factors) does not explain. Most anomalies are found in samples that later shrink.
- **Mechanism**: several categories have been documented in the literature: calendar effects, size, price momentum, value, and low volatility (factor detail is in `investing-and-financial-history` ch02). Three forces reduce an anomaly's usable return: (1) publication, after which traders crowd in and the effect often weakens (mixed evidence, general knowledge); (2) costs, which include spreads and market impact (12.1) and taxes, and which are largest in small and illiquid names; (3) capacity, since the excess return scales down as more capital chases the same mispricing.
- **Trade-off**: a diversified set of documented anomalies reduces the dependence on one pattern, but each carries its own long periods of underperformance and its own costs.
- **Position**: a mechanical flow (for example, a forced index rebalance, 12.7) can persist as long as the rule that creates it exists, so some anomalies are durable for structural reasons. The rival view is that any anomaly visible enough to trade will be arbitraged, so only the structural ones survive.
- **Does not hold when**: the net return after realistic costs and capacity is not positive. Test net, not gross.

## 13.4 Multiples and regimes: where the return comes from
- **Thesis**: a share's return can be split into earnings growth, dividends and the change in the multiple paid for those earnings. Long periods of good earnings can produce weak prices if the multiple falls.
- **Mechanism**: approximately, price return = earnings growth + change in the price-to-earnings multiple (dividends are added separately to get total return). Illustration: earnings double over a decade (about 7% a year) while the multiple halves from 20 to 10. The price change is about 2 x 0.5 = 1, a flat price over ten years, with no dividend. Multiples move with sentiment and with interest rates: a high multiple is a claim on low discount rates and on continued growth, and both can change. High valuations are weak predictors of one-year returns and somewhat more informative over a decade (position: the size of that relation is contested).
- **Trade-off**: a high multiple can persist for years, which makes a bet against it costly in the meantime. A low multiple can fall further.
- **Does not hold when**: the discount rate and growth expectations are stable for the whole horizon. Fair-value methods are in ch09.

## 13.5 Rate regimes and their effect on rules
- **Thesis**: a rule's results depend on the regime, and regimes are defined mainly by the level and direction of interest rates, inflation and volatility.
- **Mechanism**: bond prices move inversely to yields; for a small change in yield, the price change is approximately `-duration x change in yield`. A bond with a duration of 7 loses about 7% for a 1 percentage point rise in its yield. A long-duration holding is therefore a rate bet, whatever its name. An inverted yield curve (short rates above long rates) has preceded many recessions, but its timing is noisy and it is a signal about expectations, not a timing rule (position: its informational value is debated). Negative policy rates pushed some banks to pass costs to deposits; a liquidity mismatch, meaning short-term liabilities against illiquid assets, makes a bank vulnerable to runs whenever rates or confidence change, and the same mismatch appears in venues that lend against illiquid assets (crypto-assets ch05).
- **Trade-off**: a regime label gives context; it becomes a source of error when it is applied after the fact to explain a move. Labels must be written before the test and must be observable without hindsight.
- **Position**: whether rate regimes should condition a trend or a breakout rule is contested. The rival view is that the regime is visible only in hindsight, so conditioning adds fitted parameters with no proven gain.
- **Does not hold when**: the rule is not rate-sensitive (a short holding period in a liquid asset with no leverage and no funding cost).

## 13.6 Regime-conditioned rules: a checklist
1. Write the regime definition (for example, a rate level, a volatility percentile) before looking at results.
2. Check that it is observable at the time of the decision, not only afterwards.
3. Test the rule separately in each regime, net of costs, and count the trades in each.
4. Check whether the regime label itself changed the result, or whether a single episode drives the difference.
5. State which regime would make the rule stop working, and what the rule does then (stop trading, reduce size, or switch to another rule written for that regime).

## Common mistakes
- Reading a skewed sample's average as the typical outcome.
- Treating a two-year record as evidence of skill.
- Reporting an anomaly gross of costs and capacity.
- Applying a regime label after the move it is meant to explain.
- Assuming a high multiple is a timing signal rather than a statement about expectations.

## Links
- ch05 (rule families and their regimes), ch06 (sizing, correlation and drawdown), ch08 (testing rules, costs and claims), ch09 (valuation and fair value), ch12 (impact and flows); `investing-and-financial-history` ch02, ch07, ch13 (factors, funds, backtest statistics); `economics-finance` (rates, inflation, central banks); `scientific-thinking` (multiple testing and evidence).
