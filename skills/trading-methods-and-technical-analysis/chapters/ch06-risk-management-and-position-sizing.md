# Chapter 06: Risk Management and Position Sizing

> Educational concepts, not investment or trading advice. Worked examples use round illustrative numbers. Regulatory limits are dated snapshots to re-check.

## Core Idea
In this model, risk management is **arithmetic decided before the trade**: where the idea is wrong (stop), what a win is worth (target), how much of the account is lost if wrong (risk per trade), and therefore how large the position is. Analysis chooses the trade; sizing decides whether a run of errors is survivable. Most account failures described by practitioners are sizing failures, not analysis failures.

## 6.1 Reward-to-risk and the break-even win rate
- **Thesis**: the win rate needed to break even depends only on the ratio of average win to average loss.
- **Mechanism**: with reward `R` per unit of risk, break-even win rate = `1 / (1 + R)`. At 1:1 it is 50%; at 1:2, 33%; at 1:3, 25%; at 1:5, about 17%. The reverse also holds: risking 2 to gain 0.5 (R = 0.25) needs an 80% win rate, so a 66% win rate loses about 0.35 per trade (`0.66 x 0.5 - 0.34 x 2`). "Almost always hitting target but losing money" comes from small targets and wide stops: eight wins of 1 and two losses of 5 net -2. Expectancy per trade = `p x average win - (1 - p) x average loss`; costs are subtracted from every trade.
- **Trade-off**: high-ratio methods lose most of the time and test patience; high-hit-rate methods hide rare large losses (8.5).
- **Does not hold when**: wins and losses are not the planned sizes (gaps, slippage, moved stops).

## 6.2 Where the stop goes
- **Thesis**: the stop marks the price at which the trade idea is wrong, not an amount one is willing to lose.
- **Mechanism**: beyond the swing extreme, beyond a level band, or beyond the signal candle (ch03). A **closing stop** acts only if a candle closes beyond the level, which avoids intraday spikes; it is paired with an **emergency stop** in the platform (about 2 x ATR further) for gaps and abrupt moves. An abrupt removal of a currency floor by a central bank is the standard reminder that a stop must always be in the market. With a weekly resistance, some wait for the weekly close or close half the position on the daily signal.
- **Does not hold when**: the stop is placed where it "feels affordable" and then the size is fitted to it backwards (6.4).

## 6.3 ATR-based stops and targets
- **Mechanism**: stop about 2 x ATR(14) and target about 6 x ATR gives 1:3. Because ATR scales with timeframe and instrument, the same rule adapts automatically: a pair moving about 70 points a day would carry a 140-point daily stop, much less on hourly bars. Alternatives: stop at one third of the distance to target; if the stop sits under the lows, the target at least three times as far. Some intraday methods use stop 2 x ATR and target equal to the stop (1:1).
- **Does not hold when**: volatility shifts abruptly and ATR lags.

## 6.4 Sizing: the correct order
- **Thesis**: choose the trade, then stop and target, then size; never the lot first.
- **Mechanism**: size = (account x risk %) / (stop distance x value per point per unit). Example: account 10,000, risk 2% = 200; stop 25 points on a currency pair where one standard lot is worth 10 per point; size = 200 / (25 x 10) = 0.8 lots. Same risk of 300: with a 10-point stop, 3 standard lots; with a 100-point stop, 3 mini lots (1 per point). For shares: shares = risk amount / (entry - stop). For barrier certificates the same logic is restated in ch10 (10.4).
- **Trade-off**: fixed-percentage risk shrinks positions after losses and grows them after gains, which slows ruin and recovery alike.
- **Does not hold when**: the stop cannot be honoured (illiquid instrument, gap risk), so the real risk exceeds the computed one.

## 6.5 How much to risk per trade (snapshot of practice)
- Reported ranges: 1-2% per trade, up to 3% for aggressive accounts; 1.5% in some methods; 2-3% in others. One view calls the fixed 2% rule too rigid and prefers a fixed amount in money; another allows 5-6% for traders who keep only a small balance at the broker and withdraw profits. These are **practitioner conventions, inconsistent between practitioners**, not optimised values.
- **Arithmetic of streaks**: after ten consecutive losses, cumulative loss is about 10% at 1% risk (`1 - 0.99^10`), 18% at 2%, 40% at 5%, 89% at 20%. A method with a 40% win rate has about a 0.6% chance (`0.6^10`) of ten losses in a row starting at any given trade, but over 500 trades the longest losing run is typically around twelve (general knowledge: longest run grows with the log of the number of trials).
- **Before major events** (central-bank decisions, labour-market releases), size is reduced to keep the same money at risk under wider expected moves, or no new positions are opened.

## 6.6 Leverage is notional, not a multiplier
- **Thesis**: profit and loss follow the notional value controlled, not the margin posted.
- **Mechanism**: leverage = 100 / margin %: 0.25% margin is 400:1; 3.33% is 30:1. A 1% move on 100,000 notional is 1,000, which is a third of a 3,000 account. A mini contract reduces exposure, not leverage. Effective leverage falls only by reducing size. The spread is a certain cost that shifts the odds against random trading, more so with close stops and targets. European retail limits at the time of the material (snapshot, re-check): 30:1 on major currency pairs, 20:1 on major indices. A reported regulatory statistic says a large majority of retail accounts in contracts for difference lose money; figures differ by publisher and period (ch10, 10.9).
- **Does not hold when**: the product caps loss at the capital invested (ch10, barrier certificates), though even then the notional sets the risk.

## 6.7 Managing an open position
- **Break-even stop** after a given profit; a pending re-entry order at the same level is optional and a matter of risk tolerance.
- **Partial exits**: half at the first target, the rest with a stop in profit (for example, after 180 points, the stop moves to +90). Profit management should be consistent: always let run or always take, not chosen trade by trade.
- **Do not chase**: if the planned entry was a level, entering far beyond it ruins the ratio; buying after an already extended move is the same error.
- **Staged entry** is acceptable with small sizes and a final stop; adding only in the direction of the trade and only in profit is the opposite of martingale.
- **Martingale** (averaging down without a stop, doubling after losses) postpones losses until one wipes the account; automated systems promising very high returns often hide it.
- **Trailing stops** are often managed by hand, updated every day or two.
- **Time stop**: if the market does not do what was expected within a set period, one practice exits (or reverses).

## 6.8 Correlation between positions (thin coverage)
- **Thesis**: two positions on related instruments are closer to one bigger position than to two independent ones.
- **Mechanism (general knowledge)**: with two equal risks `r` and correlation `ρ`, combined risk is `r x sqrt(2 + 2ρ)`: at ρ = 1, two 1% risks are 2%; at ρ = 0, about 1.4%; at ρ = -1, zero. Long two currency pairs that share the same quote currency is largely one bet on that currency; coherent currency views (buy the expected strong one against the weakest) avoid hidden offsets. In liquidity shocks correlations jump toward one: positions that looked diversified fall together, and margin increases force deleveraging across assets.
- **Mechanism, combining systems**: separate long-only and short-only systems on the same market partly offset each other, so the combined drawdown is less than the sum of the two.
- **Mechanism, spreads**: a pair trade relies on correlation; closing one leg converts it into an outright position with much higher volatility (ch05, 5.6).
- **Does not hold when**: correlations are estimated on calm periods and assumed stable.

## 6.9 Drawdown and recovery
- **Thesis**: losses need larger percentage gains to recover.
- **Mechanism**: recovery needed after a drawdown `d` is `1 / (1 - d) - 1`: 10% needs 11.1%; 20% needs 25%; 33% needs 50%; 50% needs 100%. Capital needed for a system can be estimated from its historical maximum drawdown with a safety margin, since the worst historical drawdown is not the worst possible one (`investing-and-financial-history` ch12, ch13). On very small accounts, a normal drawdown (a quarter of the balance) pushes people to stop the system at the worst moment.
- **Does not hold when**: drawdown is measured only on closed trades while open losses are ignored.

## 6.10 Trading versus investing capital
One reported allocation keeps most capital invested for the long term and a small share for trading; a recurring warning is never to put the whole of one's wealth into active trading. These are personal frames, not rules.

## 6.11 Ergodicity, ruin and the Kelly fraction
- **Thesis**: the average outcome across many possible accounts is not the outcome a single account experiences. With repeated, multiplicative bets the path decides, and some sizes lead to ruin even when each bet has a positive expected value.
- **Mechanism**: betting the whole account on a coin with win probability `p` below 1 survives `n` rounds with probability `p^n`, which goes to zero as `n` grows. For a bet paying `b` per unit staked, with a fraction `f` of capital at risk, expected log growth per bet is `g(f) = p ln(1 + b f) + (1 - p) ln(1 - f)`. The Kelly fraction maximises it: `f* = (b p - (1 - p)) / b`, which at even money (`b = 1`) is `2p - 1`. Example: `p = 0.6` at even money gives `f* = 0.2`, with `g(0.2)` about +0.020 per bet; `g(0.5)` is about -0.034, so staking half the capital on a real edge destroys growth. Half of Kelly (0.1 here) gives about three quarters of the maximum growth, and much smaller drawdowns (general knowledge). Above `2 f*` the expected log growth is negative even with a true edge.
- **Leverage ruin threshold**: a position with leverage `L` is wiped out by an adverse move of about `1 / L` of the notional, before buffers and fees: 10x at -10%, 25x at -4%, 7x at -14.3%. Whatever the direction the analysis was right about, the position is gone at that move.
- **Trade-off**: Kelly needs `p` and `b`, which are estimated with error; full Kelly built on overestimated edges is too aggressive, so fractional Kelly is the usual response.
- **Position**: whether Kelly-style sizing is useful for discretionary trading at all is contested. The rival view is that edges are too uncertain for the formula to be used literally, so a fixed small risk per trade (6.5) is the safer frame.
- **Does not hold when**: outcomes are correlated (several bets are one bet, 6.8), losses are not bounded by a stop that is honoured, or `p` and `b` are unknown.

## Common mistakes
- Choosing the lot before the stop.
- Small targets and wide stops with a high hit rate.
- Treating two correlated trades as diversification.
- Moving the stop away when price approaches it.

## Links
- ch05 strategies, ch07 psychology, ch08 testing, ch10 leveraged products; `investing-and-financial-history` ch07 (margin, daily-reset leverage), ch12 (drawdown).
