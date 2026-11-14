# Chapter 14: Retirement Saving and Decumulation

> Educational concepts, not investment, tax or legal advice.

## Core Idea
In this model, saving for retirement and spending in retirement are **different problems with different risks**. While saving, a bad draw can be absorbed by working longer, so the right tail of equity returns dominates. While withdrawing, a bad draw is irreversible, so the **left tail and the order of returns** dominate. Everything here is mechanism and sample-based illustration; rules, rates and thresholds of any country are dated snapshots and change often.

## 14.1 Accumulation: savings rate and real contributions
- **Thesis**: the savings rate dominates the outcome.
- **Mechanism**: the probability of reaching a target after `n` years of monthly saving rises with equity share and horizon; bond-only saving rarely reaches large targets in reasonable time. Model contributions in real terms (growing with inflation), since a fixed nominal contribution shrinks, and remember that taxes fall on nominal gains, so inflation raises the effective tax burden. Example: 1,000 real a month for 10 years at 7% nominal is about 121,000 contributed (real) and about 155,000 of real capital; halving the savings rate roughly doubles the time to a given target.
- **Does not hold when**: income is unstable or the saver cannot extend working life, in which case the accumulation risk is not "right-tail" at all.

## 14.2 Withdrawals depend on real net return
- **Thesis**: a portfolio funding spending lasts as long as its net return exceeds inflation by enough to cover the withdrawal rate.
- **Mechanism**: inflation is not a loss of capital but a rise in required spending: `W_t = W_0 (1+i)^t`, and `K_{t+1} = (K_t - W_t)(1 + r_net)`. Approximate survival condition: `r_net - i` must exceed the initial withdrawal rate with a margin that depends on horizon. Worked example: 700,000, spending 26,000 in today's money, 6% net, 3% inflation lasts to 100; at 5% inflation or 4% net it runs out near 88; at 20,000 spending it survives even 5-6% inflation. Small changes in either input flip the outcome.
- **Does not hold when**: spending is flexible (cut in bad years) or a guaranteed income begins mid-horizon.

## 14.3 Withdrawal rates are horizon-dependent
- **Thesis**: a fixed-percentage rule is calibrated to a horizon.
- **Mechanism**: a "4% rule" is calibrated for roughly 30 years; in this model (position), a 50-year horizon needs a much lower initial rate (about 2% or somewhat more), because more years expose the plan to a bad sequence and to cumulative inflation. Required capital is `spending / rate`, so halving the rate doubles the capital. In one sampled set with a 50% cost basis, 26,000 at 4% (650,000) ran out before 83 in about 30% of paths, while about 2.1% (1,200,000) had a risk near 5% by 90.
- **Rival view**: flexible spending, part-time income or a public pension in later years lower the needed capital substantially; the rule is a floor-case, not a plan.
- **Does not hold when**: part of the horizon is covered by guaranteed income or spending adapts.

## 14.4 Sequence-of-returns risk
- **Thesis**: for a retiree, the order of returns matters more than the average.
- **Mechanism**: withdrawals during a drawdown sell units cheaply and permanently shrink the base that must recover; early on capital is largest, so early losses are largest in absolute terms. In a simulated 50-year set, paths that ran out of money had average returns below 2% in the first 10 years; from year 30 on, the averages of both groups coincided. A constant-return model cannot show this. In accumulation, order does not matter for a single-sum horizon, and contributions even buy cheaply in a downturn.
- **Trade-off**: protecting the early years (cash buffer, ladder) lowers average growth.
- **Does not hold when**: the portfolio is so large relative to spending that no plausible sequence depletes it.

## 14.5 Decumulation strategies compared by their left tail
- **Thesis**: compare strategies by the worst quartile of years survived, not by the mean.

| Strategy | Range | Left tail | Note |
|---|---|---|---|
| Pure equity (accumulating or distributing) | widest | worst | highest mean (in one example 7 to 50 years, mean about 37) |
| Bond ladder | narrow | better | all outcomes in a band (about 20-28 years), low mean |
| 10-year ladder plus equity for the rest | medium | much better | equities not sold in the first decade (worst case about 7 to about 12 years) |
| Inflation-linked bonds | narrow | highest floor | real floor, lower mean |
| Fixed 60/40, rebalanced mechanically | medium | does not protect | keeps selling bonds to buy falling equities |
| Discretionary 60/40 (sell whichever rose) | medium | helps the tail | can lag in trending markets |
| Multi-year cash buffer | medium | raises the minimum slightly | lowers the mean |

- **Mechanism**: coupons and dividends are irregular, controlled by issuers and fully taxed; selling units gives control over timing and amount. A ladder with maturities at 2, 4 and 6 years gives known cash for known spending with no price risk if held to maturity, while a bond fund has no maturity and can lose when rates rise (ch06, 6.8).
- **Does not hold when**: capital is so large that every strategy survives, or the data window favours one asset.

## 14.6 Monte Carlo design for personal finance
- **Thesis**: resampling real history in blocks keeps structure that an i.i.d. draw destroys.
- **Mechanism**: annual equity returns show near-zero autocorrelation, so yearly blocks can be drawn at random; inflation is strongly autocorrelated (around 0.9 from one year to the next) and cannot be drawn year by year without smoothing; inflation and equity returns can be negatively correlated, so pair each sampled return with its contemporaneous inflation. A 12-month block bootstrap preserves intra-year dependence. Extending inflation back before the return data needs heuristics. Short histories (25 years) limit variety, a long inflation history from another monetary regime misrepresents a holder of foreign assets, and a sample containing an exceptional asset (a metal that rose strongly in the window) biases results.
- **Reading**: results are "in this sample", for example 88% survival at 100 years with 1,000,000; they are not forecasts (ch13).

## 14.7 Tax on withdrawals and the cost of switching
- **Thesis**: in a capital-gains regime the same capital supports different spending depending on how much of it is gain.
- **Mechanism**: each sale taxes only the gain portion: `tax = rate x (proceeds - proportional cost basis)`. With basis at half the market value, half of each sale is gain, so a 26% rate taxes about 13% of the proceeds (Italy, snapshot 2026). Tax deferral makes the effective after-tax return higher than the immediately taxed one (8% x 0.74 = 5.92% if taxed each year), but concentrates the bill when the money is needed. Switching all at once from an accumulation asset to an income structure realises the gain: with basis at half the value it costs about 13% of the portfolio; the true cost is the return lost on tax paid early, so a gradual switch using new contributions avoids it. 
- **Does not hold when**: the holding sits in a wrapper taxed yearly or exempt, or sales occur in a loss year.

## 14.8 Pension funds versus direct investment (general principles)
- **Thesis**: a tax-deductible contribution must be compared with the same pre-tax money invested outside, not with the refund.
- **Mechanism**: at marginal rate `m`, one unit of gross income becomes `1 - m` outside the wrapper and 1 inside; with `m = 40%`, contributing 5,000 reduces net pay by 3,000 while 5,000 enters the fund, whereas outside only 3,000 could be invested. The saving is deferral and reduction, not a gift. A fund usually wins at short and medium horizons, when a marginal rate is high, and when an employer matches (an instant return that nothing else replicates, about 100% on the matched part); a skilled, low-cost, long-horizon self-investor with a low marginal rate can overtake it. In one dated snapshot (Italy, 2025; see `personal-finance-italy`) the break-even ranged from about 13 years at a 23% marginal rate to about 37-39 years at 43%.
- **Mechanism, line choice**: choose by the date the money is needed (position): over 1-2 years an equity line can lose 10%; over 5 years it is rarely negative; over 20 years equity lines were positive and a guaranteed line earned about inflation or less; one 18-year comparison gave about 2.4x against 1.3x. Guarantees trigger only on specific events and cost fees.
- **Mechanism, costs**: 2% a year on a 5% expectation takes about 40%; collective funds often cost near index funds, bank-sold funds 2-4%; fixed per-contribution fees hurt small contributions.
- **Mechanism, exits and annuities**: exit routes exist (benefit at retirement, transfer, partial withdrawals for specified events, advances, bridge annuity) but each has its own tax and conditions, and thresholds on annuitisation apply per fund. A life annuity's value depends on mortality table, technical rate, loading and options; the pure single-life, zero-technical-rate version has coefficient `1/(life expectancy + safety years)`, reduced by loading `L` to `(1-L)/expectancy`. It is insurance against living long, fair on average if there is no known health issue, at the cost of bequest and flexibility.
- **Does not hold when**: no tax is deductible (flat-tax regime or income fully offset) or employer match is absent.

## 14.9 Public pension and buy-back logic
- **Thesis**: under a contributory system the pension is the balance times a transformation coefficient at retirement age, not a share of the last salary.
- **Mechanism**: balance = contributions revalued by a growth index; the coefficient rises with age (about 4.5% at 60 to 6.2% at 70 in one snapshot, Italy 2024). Eligibility gates (age, contribution years, minimum amount) are step functions, so being just below one can justify extra contributions. Buying back study years rarely pays; three levers drive it: years to retirement (shorter favours), return on alternatives (lower favours), and the gap between the marginal rate now and in retirement (larger favours).
- **Does not hold when**: pre-reform contributions follow an earnings-related method.

## 14.10 Liquidity buffers, older investors and heirs
- **Thesis**: age alone does not dictate prudence; effective horizon, projected spending (especially care costs) and the wish to leave assets do.
- **Mechanism**: life expectancy at 70 is around 16-17 years and rises with age survived; heirs lengthen the horizon beyond the owner's. Spending in the next few years can be matched with bonds held to maturity, the remainder bears equity risk if not needed; with very small assets, simplicity and low cost beat any investment account. Bucket and buffer sizing is in ch04, 4.14.
- **Does not hold when**: spending absorbs all income and assets, or health is very poor.

## Common mistakes
- Using an average return to test a withdrawal plan.
- Applying a 30-year rule to a 50-year horizon.
- Comparing a refund with a gross contribution.
- Reading a simulated survival rate as a forecast.

## Links
- ch04 allocation and buckets, ch06 bonds and ladders, ch12 maths, ch13 evidence, `personal-finance-italy` for one country's rules.
