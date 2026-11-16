# Chapter 05: Strategy Families: Rules, Parameters and Invalidation

> Educational descriptions of methods, not investment or trading advice. No signals, no recommendations. Rules are reported as described by practitioners; none is shown here to be profitable.

## Core Idea
In this model, a strategy is **a written rule for entry, exit, size and invalidation, chosen to suit one market regime**. Trend following earns in trends and bleeds in ranges; mean reversion does the opposite; breakouts need expansion; pair trades need a stable relation. The most useful field of each card is the last one: when the rule stops describing the market. Parameters below are those reported; they are starting points for testing (ch08), not settings to copy. Results claimed for these methods are discussed only in ch08.

## 5.1 Trend following on pullbacks (RSI as regime filter)
- **Thesis**: buy pullbacks in uptrends and sell rallies in downtrends, entering after the move has proved itself.
- **Mechanism**: a 14-period RSI is read as a regime: 40-100 uptrend, 0-60 downtrend, 40-60 range. The rule enters long when an uptrend pulls back to an RSI near 40 (zone 40-45), short when a downtrend rallies to near 60; if price has already moved without returning to the zone, there is no trade. Stop just beyond the previous swing extreme; target at or beyond the previous high; stop about one third of the distance to target (reward-to-risk 1:3, break-even win rate 25%). If stop and target are too close because the market is flat, the trade is skipped. A trend is also checked by structure: a pullback must be followed by a new high, or the trend is no longer up.
- **Invalidation**: price beyond the reference level ends the scenario; the rule exits and does **not** reverse (no stop-and-reverse).
- **Trade-off**: catches the middle of trends, misses tops and bottoms ("whoever catches the whole move was lucky, not skilled").
- **Does not hold when**: illiquid shares, very volatile instruments, timeframes under about fifteen minutes, or ranges. Alternative thresholds (37/64, 62/38) exist; tuning them is curve fitting unless tested out of sample.
- **Rival view (general knowledge)**: diversified time-series trend following across many futures markets has a documented long-run record, but with long flat or losing stretches; single-instrument rules are far noisier.

## 5.2 Two-speed trend systems
- **Thesis**: one fast reading for entry, one slow reading to stay in or exit.
- **Mechanism**: two instances of the same indicator with different lengths; positions are added only in the direction of the slow one. Long and short sides can be run as separate systems: their drawdowns partly offset, so combined drawdown is less than the sum (6.8).
- **Invalidation**: the slow reading flips.
- **Does not hold when**: the market whipsaws around the slow line.

## 5.3 Mean reversion to an average
- **Thesis**: after an unusually long time away from an average, price tends to return toward it.
- **Mechanism (generic version)**: count the periods since price last touched an average (for example 50, 100 or 200). When the count passes a threshold N, a return becomes the working hypothesis; the method waits for a further 20-25% of N before entering, places the stop beyond the range extreme, targets the nearer average first and the slower one last, and requires reward-to-risk of at least 1:2. Two of three conditions should hold: the count zone, a well-defined range, a flattening slope of the average. N is chosen by translating a horizon into periods (one trading month, quarter or half-year on daily bars). A midpoint between a broken average and the next one can serve as first target and as the line between correction and reversal.
- **Invalidation**: a trend that accelerates without forming a range; the rule does not trade then, and shorting a market where price and slopes are "launched" is called dangerous.
- **Trade-off**: high hit rate claimed, small gains against occasional large losses (8.5).
- **Does not hold when**: very short timeframes (1-5 minutes) or short averages, which "stretch" more easily. Probabilities quoted by analogy with a normal curve (68%, 95%) are not measured results.

## 5.4 Mean reversion inside a range
- **Mechanism, extremes and pivots**: with RSI beyond 70/30 on four-hour bars, a first position against the move, further steps at pivot levels (R1, R2, midway to R3), the stop beyond R3, the target at the middle Bollinger band, and no trading around scheduled events. Scaling in this way is distinguished from martingale only because maximum exposure and the stop are fixed in advance (6.7).
- **Mechanism, pivots by expected volatility**: on high expected volatility (from the event calendar), trade with the trend on a break of S1/R1, target S2/S3, stop at the pivot; on low expected volatility, fade a break of S2/R2 with the stop at S3/R3 and target back toward the centre.
- **Mechanism, quiet intraday sessions**: in a late-session low-volatility window, draw the range only once congestion has formed, sell near its top and buy near its bottom with very small targets, checking a related index.
- **Invalidation**: a break that holds beyond the outer level; scheduled data and session opens.
- **Does not hold when**: trending days; against-trend trading is described as needing a close stop and reduced size.

## 5.5 Breakout and false breakout
- **Thesis**: the first impulse that breaks a level, with no obstacles to its left, can carry far in high volatility.
- **Mechanism, direct breakout**: buy-stop or sell-stop orders beyond support or resistance; reward-to-risk above 1:1; favourable when no other levels sit nearby; suited to very volatile instruments and periods. Levels are drawn on closes and bands built from shadows (1.6).
- **Mechanism, false-break entry (generic)**: candles with a range at least 4-5 times the average of the last 20 mark horizontal levels at their close. The rule does not enter on the first touch: it waits for price to cross the level and close back on the other side (a false break), then places a limit order at the level; target = the opposite level, stop = half that distance (1:2); halfway, half the position is closed and the stop moves to break-even.
- **Invalidation**: price closes back inside the range (for a breakout) or beyond the level again (for a false-break fade).
- **Positions**: some prefer pullbacks over breakouts ("breakouts often come back"); others say breakouts outperform pullbacks only in periods of very high volatility. Both entries (retest or direct) are used.
- **Does not hold when**: wide, noisy ranges; then stand aside or change timeframe.

## 5.6 Pair trading and long-short spreads
- **Thesis**: long one instrument and short a closely related one, equal value in the account currency, opened and closed together, to earn the change in their spread rather than the direction.
- **Mechanism**: select by correlation (overlaid charts), spread history and, in some methods, seasonality; examples of related pairs include two crude oil benchmarks, two precious metals, refined products, two shares of the same sector, or two national indices. For shares, relative multiples (P/E, net margin, value to sales) against the sector help choose which side is cheap. A percentage comparison chart depends on its start date; several horizons are checked. A ratio (one price divided by the other) shows relative strength; equal capital on both legs ignores different volatilities, so the spread is effectively weighted toward the more volatile leg.
- **Invalidation**: the relation breaks (correlation collapses, one leg re-rates on news); some variants hold a fixed number of days, others use no stop, which in this model is a mistake for beginners.
- **Trade-off**: "market neutral" means independent of direction in theory, not riskless; financing costs on both legs apply to contracts for difference.
- **Does not hold when**: one leg is closed in profit and the other left open: the position becomes directional and its volatility jumps (6.8).

## 5.7 Momentum and ranking
- **Thesis**: assets that rose most over 6-12 months have tended to keep outperforming for a while (cross-sectional momentum).
- **Mechanism**: rank a basket by 12-month return (or 6- and 12-month, sometimes adjusted for volatility), hold the top decile (at least five names), rebalance monthly or semi-annually, compare with an equal-weight benchmark. Results on very short horizons are poor; shorting the losers systematically is not shown to work here. Ranking by fundamentals (earnings and revenue growth, net margin, return on equity over five years, equal weights, annual rebalancing, staged entry) is a related selection method; crashes still hit it in full.
- **Invalidation**: momentum reversals after sharp market rebounds (general knowledge: momentum crashes).
- **Does not hold when**: turnover costs exceed the edge; `investing-and-financial-history` ch03 notes momentum's weak theory and high cost.

## 5.8 Scalping and intraday
- **Thesis**: on short horizons, cost is the main adversary.
- **Mechanism**: a spread of 0.8 points on a standard currency lot costs about 8 units of account; with targets of 4-7 points it consumes roughly 11-20% of each winning target. Instruments are chosen for low spread relative to average range. One five-minute setup: a short average's slope for direction, a parabolic stop for exits, RSI 30/70; entry on a return to the average in the trend direction; no trade if there is no room between average and stop. Session rules: skip the first 15-30 minutes after the open, at most two sessions of about two hours, a maximum daily loss of 1%.
- **Positions**: several practitioners advise against scalping (commissions, false signals, stress); one limits intraday to about one day a week and a small share of resources at the start.
- **Does not hold when**: costs, latency or emotions dominate; most of short-term trading is described as psychology (ch07).

## 5.9 Seasonal and positioning strategies
See ch04 (4.4) for the rule-based seasonal setups and their statistical weakness.

## Common mistakes
- Using a trend rule in a range, or a range rule in a trend.
- Reversing a position automatically when stopped out.
- Closing the winning leg of a spread.
- Tuning thresholds until the past looks good.

## Links
- ch01-ch04 tools, ch06 risk, ch08 validation; `investing-and-financial-history` ch03 (momentum), ch13 (backtests).
