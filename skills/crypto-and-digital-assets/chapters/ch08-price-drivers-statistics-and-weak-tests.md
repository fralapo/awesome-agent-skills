# Chapter 08: Price Drivers, Statistics and Why the Tests Are Weak

> Educational concepts, not investment, tax or legal advice. No price forecasts. Figures are illustrative, dated and sample-dependent.

## Core Idea
In this model, crypto-asset price history is **short, trending and dominated by a handful of episodes**, which makes most claims about cycles, supply effects and strategies fragile. This chapter shows how to test a claim, which common claims fail naive tests, and why even a "significant" result can be unusable. It teaches method, not outcomes.

## 8.1 Three cycles do not prove a cycle
- **Thesis**: three or four events cannot establish a causal link between supply halvings and price booms.
- **Mechanism**: if booms recur every 2 to 4 years and halvings every four, a boom shortly after a halving is likely by chance (both periodic, like Christmas following a birthday without being caused by it). A formal test: define a boom precisely (steeper than exponential and above the previous high), split history into five-month blocks (27 blocks, 9 between halvings), and count how many of five booms fall in the three blocks right after a halving. In one analysis 3 of 5 did, with a chance probability around 0.04%, but two booms fall outside the window and a sample of three events is fragile. A self-fulfilling prophecy remains possible: if enough people act on the pattern, it can appear.
- **Does not hold when**: used as a trading rule; sample size dominates.

## 8.2 Spurious correlation
- **Thesis**: two trending series correlate even without causation.
- **Mechanism**: supply and price correlate at about +0.65 (+0.89 with the log of price) simply because both rise with time. Add time as a regressor and the supply coefficient becomes small and negative: about -0.012 per unit issued, which with 900 units a day is about -11 a day against about +37 a day from time. In a log model one year of issuance costs about -8% while one year of time adds about +183% in the sample. Variables that embed price (dollar volume, market capitalisation) must be excluded. Regression limits include multicollinearity and absurd extrapolation outside the sample.
- **Does not hold when**: supply changes are large and abrupt. For altcoins the test should price in the main asset to remove the market-wide factor; results are inconsistent. The clear case in which supply explosion kills price is a collapsed algorithmic stablecoin's sister token (ch07).

## 8.3 Sign flips and unstable relations
A test of price against policy-rate changes produces correlations from +56% to -49% depending on the subperiod, and about -2% on daily changes. **Sign flips mean there is no stable law.** Asking "does X drive price?" needs the same answer across independent periods.

## 8.4 Non-overlapping windows and similarity
Compare non-overlapping 365-day windows of daily returns by the sum of squared differences (lower is more similar). The most similar pairs are not the famous bull runs; two famous cycles are about five times farther apart than the best pair. Each cycle also has its own fashion (token offerings in one, collectibles in another) that outlives the peak and hurts latecomers. Past cycles are not templates.

## 8.5 Waiting for a dip vs investing at once
- **Thesis**: for an asset with positive expected drift, waiting has a cost that usually exceeds the benefit.
- **Mechanism**: a backtest on equities: buy-and-hold about 13.9% annualised; buy only after a 30% drawdown about 12.8%; buy at -30% and sell at the prior high about 5.6% (exiting forfeits the big climbs). A one-year lockout keeps strategies comparable. Thresholds of 10% and 50% behave similarly; at 50% many stocks never trigger. On a highly volatile asset the dip entry triggers almost at once, but the sell-at-previous-high variant still underperforms. A loss and a missed gain are equivalent until the loss reaches 100%.
- **Trade-off**: regret avoidance versus expected return; staged entry in thirds or periodic investing lowers regret at a small expected cost.
- **Does not hold when**: the asset has no positive drift or the sample suffers survivorship bias (ch13 of `investing-and-financial-history`).

## 8.6 Rebalancing and the asset that goes to zero
- **Thesis**: rebalancing sells winners and buys losers, which helps under mean reversion and hurts under trends.
- **Mechanism**: daily rebalancing of pairs and triples of crypto-assets without fees gave sometimes better, sometimes worse results than buy-and-hold. The tail risk: an asset collapsing toward zero is bought repeatedly with proceeds from healthy assets, draining the whole portfolio (a three-way 33% split with a collapsing sister token fell from about 0.66 and 8 units of the two healthy assets to about 0.14 and 2). Rebalancing with new contributions avoids taxes.
- **Does not hold when**: assets are cyclical and bounded below; in one position, weights are kept relative to money originally invested, like not shifting capital from a winning business to a losing one.

## 8.7 Leverage, drawdown and liquidation
- **Thesis**: leverage is judged by maximum drawdown, not average return.
- **Mechanism**: over one-year windows of a volatile asset: average maximum drawdown about 23%, a quarter of windows about 45%, one in ten about 54%, one in twenty about 60%, worst case about -80%. With 50% LTV a 23% drop forces selling a quarter of collateral; a 54% drop leaves less than the starting capital. Leveraged funds that rebalance daily lose from volatility: +10% then -10% gives -1%, and at leverage 2 the factor 1 - x^2 becomes 1 - 4x^2; they also pay a funding rate and higher fees. Log returns add over time (+10% then +10% is +21%), are closer to normal for statistics, but fail for portfolios: a -100% asset has log return minus infinity, while +300% on another offsets it in money terms.
- **Does not hold when**: collateral is stable, the loan is small and thresholds are far away.

## 8.8 Hedging volatile assets
- **Thesis**: hedging a high-drift, high-volatility asset typically costs more than it protects.
- **Mechanism**: a margin short with collateral taken from the asset itself: at 10x leverage collateral is 10% of notional and the position is liquidated after a ~10% rise; estimated foregone gains are ~11% (10x), ~28% (5x), ~43% (3x). Liquidation probability for 10x rises from about 4% over a day to above 50% over six months. A 180-day at-the-money put paid ~9% on average but cost ~21 to 22%; adding opportunity cost (~15%) gives about -27% against doing nothing; longer maturities are worse. Protection also requires predicting the length of the downturn.
- **Does not hold when**: an asset is stable and cheap to insure, or there is genuine information about an imminent drop.

## 8.9 Concentration and diversification caveat
Diversification reduces risk only if added assets are not more volatile than the base: a low-correlation, high-volatility asset can raise portfolio volatility. A handful of well-chosen assets may diversify as well as a broad index in-sample, but many random 100-stock subsets of an index also beat it by luck; these facts say nothing about selection ability.

## 8.10 Other price drivers (concepts)
| Driver | Mechanism | Evidence quality |
|---|---|---|
| Liquidity and risk appetite | Money available for high-risk assets | Moderate, mixed |
| Regulatory news | Access changes | Event-based, short term |
| Adoption narratives | Expected future use | Weak, self-referential |
| Leverage and liquidations | Forced selling in falls | Mechanical, observable |
| Retail attention (search interest, lay press) | FOMO | Pro-cyclical (position: contrarian indicator) |
| Supply schedule | Issuance changes | Small direct effect (ch02, 2.7) |

## Common mistakes
- Quoting a correlation with no control for time.
- Presenting a pattern from three events as law.
- Judging leverage by returns rather than drawdown.
- Using chart patterns (channels, ratio levels, "rainbows") as evidence: they are arbitrary and fit afterward.

## Links
- ch02 issuance; ch07 leverage mechanics; `investing-and-financial-history` ch08, ch12-ch13; `scientific-thinking` (statistics).
