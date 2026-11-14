# Chapter 04: Diversification and Asset Allocation

> Educational concepts and history, not investment advice or a forecast.

## Core Idea
In this model, the risk of a portfolio is not the average risk of its parts but the way they **move together**. Spreading across imperfectly related assets lowers risk without lowering expected return, which is why it is called the only free lunch. Allocation is then a decision about how much market risk to hold, constrained by what you can bear and what you need.

## 4.1 How diversification works
- **Thesis**: combining assets whose outcomes are not identical reduces the chance of a bad total outcome.
- **Mechanism, intuition**: if each of three holdings has a one-in-three chance of losing everything, an all-in investor loses everything one time in three; an investor who splits across the three loses everything only if all three fail, one time in 27 (if independent). The result depends on **correlation**: near-zero correlations diversify well, correlations near one barely help. Formal portfolio theory (published 1952) shows risk depends on covariances; the market portfolio of all assets is the mean-variance optimal one under the standard equilibrium model.
- **Mechanism, practice**: spread across industries (banks and property respond differently to interest rates), company sizes, countries, and asset classes (stocks, bonds).
- **Trade-off**: you always hold the best *and* the worst performers; you give up the unrepeatable chance of owning only the winner.
- **Does not hold when**: correlations jump toward one in a crisis (general knowledge, and also observed for stocks in downturns); or the "different" assets share a hidden factor such as leverage or liquidity.

## 4.2 Idiosyncratic risk and how many stocks are enough
- **Thesis**: much single-stock risk is removable; the "20 to 30 stocks" rule is outdated.
- **Mechanism**: company-specific risk is diversified away as holdings increase, leaving market risk. The older rule of thumb was based on dated research and on average volatility; more recent work implies you need many more stocks to be well diversified in terms of the risk of lagging the market, because of skew (ch03). The exact figure is unverified; the safe statement is "far more than 30 if the goal is to avoid missing the winners".
- **Trade-off**: holding the whole market is the extreme, with the lowest idiosyncratic risk and lowest cost.
- **Does not hold when**: the goal is an intentional bet and you accept the risk.

## 4.3 International diversification
- **Thesis**: excluding foreign stocks is a concentration bet on one country.
- **Mechanism**: under the standard model, every investor should hold the world market portfolio. In hindsight one market outperformed (about 2% a year over foreign developed markets for 1980-2020 and over a century), yet part of this was a rise in valuation (ch02, 2.8) and arguably luck and learning; you cannot choose in advance which market will win, and chasing recent winners is a documented retail mistake. **Economic growth does not equal stock returns**: expected growth is already in prices, so owning the most robust economy is not a riskless edge.
- **Trade-off (position)**: home bias gives currency familiarity, tax and cost simplicity, and lower fees; the case for full global diversification is theoretical plus empirical for most (not all) countries.
- **Does not hold when**: currency costs, taxes or legal limits dominate.

## 4.4 Asset allocation as a risk-profile problem
- **Thesis**: the stock-bond split should come from your **risk profile** (ch01, 1.5), not from a rule or the latest return.
- **Mechanism**: ability to take risk sets a ceiling (can you ride it out without selling?), need sets a floor (what return reaches the goal?), tolerance sets the portfolio you will actually keep. Behaviour often dominates: investors buy high and sell low, and a plan with a smaller drawdown that you keep beats a larger one you abandon.
- **Mechanism, measurement**: psychometric questionnaires give a relative ranking; risk tolerance in a large sample was close to normally distributed. A firm may map a high score to a high equity share, but only if ability allows (this is a firm practice, not a law).
- **Mechanism, learning**: risk composure is revealed by living through a decline. Some practitioners advise being relatively conservative until you have lived through a crash (position, and not endorsed by all).
- **Trade-off**: more bonds lower expected return and drawdown depth; more stocks raise both.
- **Does not hold when**: your liabilities, tax situation or pensions change the effective asset mix.

## 4.5 When the market drops
- **Thesis (general knowledge)**: a decline is the cost of the premium, not a malfunction.
- **Mechanism**: the realised premium arrives unevenly; declines are what make the long-run average positive. The decision test is whether the allocation still matches your risk profile; if it does, a fall changes the price paid for expected returns, not the plan. Rebalancing toward targets is a way to commit in advance (ch11).
- **Does not hold when**: the fall reveals that your tolerance or ability was lower than assumed; then the allocation was wrong at the start.

## 4.6 Concentration risk: the founder's and the manager's case
- **Thesis**: concentration in your own business or fund is correlated risk twice over.
- **Mechanism**: a partner who held about 80% of savings in the fund also owned a management company worth more than all financial assets; the effective exposure to the same outcome was closer to 90%, and a modest fund loss could have wiped out the management company. Expected-utility analysis, widely taught in decision theory, would have advised a smaller stake even though the expected return was attractive. Investors want skin in the game, but not all-in.
- **Trade-off**: controlling shareholders also hold concentrated positions to keep voting control.
- **Does not hold when**: signalling and control outweigh variance reduction for you, knowingly.

## 4.7 Rebalancing: when it actually matters
- **Thesis**: rebalancing controls risk; it does not raise expected return, and its benefit depends on the mix and on costs.
- **Mechanism**: selling what rose and buying what lagged restores target weights. The only source of extra return is mean reversion of relative prices ("volatility harvesting"): a loss `a` then a gain `b` compounds to `1 - a + b - ab`, and a 50/50 rebalance cuts the hidden `-ab` cost of oscillation to about a quarter per cycle. With +50% then -33.3% an unrebalanced asset returns to 100 while a 50/50 mix with a flat asset ends near 104. With swings of a few percent the effect is negligible.
- **Mechanism, evidence in this model**: on rolling 5-year windows, a stock-bond mix rebalanced yearly or never gave near-identical means, and monthly rebalancing was often slightly worse; in a diversified stock basket the gain was put at 0.5 to 1 point a year before taxes, and yearly rebalancing captured most of it at a twelfth of the transaction cost. For baskets of a few single stocks it trims the right tail (the winners).
- **Mechanism, practice**: where selling triggers tax or fees, steer new contributions and withdrawals toward the underweight sleeve instead. A rule of thumb in this model (position): act only when a weight has doubled with two assets, or tripled to quintupled with twenty.
- **Trade-off**: lower dispersion and a stable risk profile against costs and lower upside.
- **Does not hold when**: one asset has a runaway trend (continuing to sell it forfeits the gain) or is structurally dying (mechanical buying pours money into it).

## 4.8 Equal weight versus capitalisation weight (position)
- **Thesis**: capitalisation weighting is a convenience, not a proven optimum; equal weighting diversifies more but behaves very differently across periods.
- **Mechanism**: a cap-weighted index needs no rebalancing and embeds an automatic momentum tilt (it holds more of what grew); one country can reach 60-70% of a global index, so its variance dominates and the cross-market term barely counts. With two assets of equal variance, a 50/50 mix has variance no higher than 70/30, with equality only at correlation 1. Equal weight has the opposite tilts (smaller firms, lower volatility) and implicitly sells winners at every rebalance. Re-weighting by economic output is a third option (position), sitting between the two in backtests, with a short history.
- **Mechanism, evidence**: over rolling 7-10 year windows an equal-weight world index had returns near the cap-weighted one and lower terminal dispersion; sub-periods flip, with equal weight ahead after an equity peak and cap weight ahead in a decade of mega-cap leadership.
- **Rival view**: capitalisation weights aggregate everyone's information and need no maintenance; an equal-weight portfolio of small markets has turnover, liquidity limits and one-name collapses. Market value is not economic size.
- **Does not hold when**: samples include only present index members (survivorship, ch13) or a price index is compared with total-return ones.

## 4.9 Lump sum, staged entry and rule-based entry
- **Thesis**: if the money is already available and expected return is positive, investing at once is better in expectation; staging trades expected return for lower dispersion.
- **Mechanism**: uninvested cash earns less, so a plan of equal tranches has an average exposure near half the horizon; in a stylised 5% model the effective return on money paid in drops to about 3.6%. Starting a plan on every historical date, the staged mean was about half the lump-sum mean over 36-month windows, while the worst case improved by only a couple of points, because a crash hitting the first tranches is barely softened. Value averaging (invest the gap to a growing target) and drawdown ladders (deploy a buffer at fixed drops, each trigger firing once) cut dispersion by a third to a half and lower the mean; none beat lump sum on average in rising markets. Waiting for a fixed pullback below the recent peak trims both tails and usually lowers the mean; being near highs is the normal state of a rising market (ch13).
- **Trade-off**: behavioural ease of entry against lower expected result.
- **Does not hold when**: the investor only has a monthly flow (staging is then the only path), or markets are flat or fall through the window, where staged and ladder rules do better.

## 4.10 Factor ETFs and systematic active management (implementation; debate in ch03)
- **Thesis**: a factor can exist without a factor-tilted fund beating the plain one.
- **Mechanism**: factor funds tilt to value, small size, momentum, quality, minimum volatility or high dividend. Compared with the matching standard index on rolling 5-year windows, quality and momentum were the more robust in one 25-year sample, while value, small size and minimum volatility changed sign; minimum-volatility funds did lower volatility. Country and year explained more variation than the factor. In one 17-year euro sample a core-equity tilt fund trailed the world index by about half a point and a targeted-value fund trailed a small-cap index by about a point, gaps near costs; 17 years is short for factor claims. Judge any fund by rolling windows against the closest style benchmark, since for any index some fund beats it and the problem is choosing in advance.
- **Does not hold when**: the effect is a data bug or an artefact of overlapping windows (ch13).

## 4.11 Currency: hedging and listing
- **Thesis**: currency is a zero-sum pair; neither hedged nor unhedged is better a priori, and hedging has a recurring cost.
- **Mechanism**: returns multiply (+10% on the asset and -10% on the currency is -1%). A hedged share class holds the assets plus forwards; because the asset value changes daily the hedge is imperfect, and the slippage lands in performance. In one dated sample (data to 2024) the realised cost was a median of 1-2% a year against a visible expense gap under 0.2%, with yearly values from -4% to +4%, and hedged dollar bond funds gave up nearly their whole extra yield. The currency a fund is *quoted* in does not remove exposure: the same units listed in two currencies differ by small random amounts, against typical 12-month exchange-rate moves of about 8% (range -22% to +26%).
- **Does not hold when**: the currency is unstable, the horizon is short, or the pair carries almost no hedging cost.

## 4.12 The cost stack
- **Thesis**: the expense ratio is an estimate of explicit cost, not the whole cost.
- **Mechanism**: layers are the ongoing charge (a past estimate, not a promise), transaction costs inside the fund (about 0 to 0.3%, near zero for bond funds), broker commission, half the bid-ask spread (`(ask - bid)/mid`), tracking difference (cash drag, rebalances, sampling) and entry or exit fees. Tracking is noisy: monthly outliers of -3% to +6% around a mean near the stated cost, so a lump-sum buyer draws one noisy year in which a 0.05-point difference in expense ratio is invisible. Cost matters relative to expected return: 4% on an 8% expectation takes half; 2% on a 3% bond return takes two thirds. A rough ladder from costly to cheap in this model: wrapped life policies, managed accounts, guaranteed-capital products, complex certificates, unlisted funds, plain bonds, index funds. A mixed product that trails a mix of indices by its cost has shown its price.
- **Does not hold when**: the cost buys something real (a guarantee, access) and is valued knowingly.

## 4.13 Accumulating versus distributing (principle)
- **Thesis**: before tax the two are equivalent; a dividend is a sale of the asset.
- **Mechanism**: on the ex-date the price falls by about the dividend (a share at 17 paying 1 trades near 16); an accumulating fund reinvests inside. Overlapping charts for the two usually assume virtual reinvestment; without it a five-year index chart can read 57 against 80. Where income and gains are taxed alike at a flat rate, deferral lets the untaxed part compound, and selling units taxes only the gain fraction; where gains fall below cost, accumulating never pays. Distribution gives cash flow and may steady behaviour; high yields can mean the price has fallen (a dividend trap), and a payout above earnings is capital returned. Rules differ by country; see `personal-finance-italy` for one snapshot.
- **Does not hold when**: dividends and gains are taxed at different rates, or a low-basis position makes each sale mostly gain.

## 4.14 Allocation by wealth and time horizon
- **Thesis**: split wealth by the date each unit of money is needed, not by product.
- **Mechanism**: four buckets in this model (position): current spending; a reserve for unplanned shocks, sized from a list of last year's surprises plus the largest foreseeable one, less any reliable family backstop; spending known within 1-10 years, matched by instruments maturing on the date (ch06); and money not needed for 10+ years in diversified equities. Equities are then never the source of a scheduled payment. Fixed amounts, not percentages, suit the first three. A Monte Carlo of random expenses showed a buffer cutting dispersion of final wealth slightly at the cost of a small lower mean; for a single-asset holder it was clearly better, for a wealthy multi-asset holder it added little. Below roughly a few thousand units, fixed fees outweigh the gain of any product beyond a deposit.
- **Mechanism, large wealth**: legal, operational and sovereign risks outgrow market risk: accounts can be frozen, a fund issuer can suspend, illiquid property sells below its book value, tax instalments are large. Gold is not a safe asset in nominal terms (flat for about 25 years after 1980; down about a third in nine months in 2012-13, dated).
- **Mechanism, older investors**: age alone does not dictate prudence; horizon (remaining life expectancy at 70 is roughly 16-17 years, and heirs lengthen the horizon), care costs and the wish to leave assets do. See ch14.
- **Rival view**: the rule "the young should hold equities" is rejected in this model for people whose future needs are uncertain.
- **Does not hold when**: wealth is so large that no outflow forces a sale.

## Common mistakes
- Treating "diversified" as "many tickers" (check correlations and shared factors).
- Choosing an allocation from the last decade's results.
- Mistaking tolerance for ability.
- Rebalancing monthly, or into an asset that is failing.
- Counting a lower expense ratio as certain when tracking noise is larger.

## Links
- ch01 risk, ch03 concentration data, ch06 bonds, ch08 behaviour, ch11 decisions, ch12 maths, ch13 evidence, ch14 retirement.
