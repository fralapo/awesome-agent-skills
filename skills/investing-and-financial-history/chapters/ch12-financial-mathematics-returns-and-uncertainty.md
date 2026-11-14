# Chapter 12: Financial Mathematics, Returns and Uncertainty of Estimates

> Educational concepts, not investment, tax or legal advice.

## Core Idea
In this model, a return is only meaningful with its **base, its horizon and its error bar**. Over a holding period only three things matter: capital in, capital out, elapsed time. Everything else (compounding, logs, IRR, volatility) is a way to restate or summarise those three, and every forward-looking number built on them is an estimate with a wide margin. Discounting itself is introduced in ch05; this chapter is the arithmetic toolbox.

## 12.1 Simple return, compounding and annualisation
- **Thesis**: returns over consecutive periods multiply; they never add.
- **Mechanism**: simple return = `final/initial - 1`, defined only for a non-zero base, and a percentage must carry its base ("20% then 5% more" can mean 25% or 21%). Chained: `(1+r1)(1+r2) - 1`. Capital after `n` years is `C(1+i)^n`, not `C(1+n·i)`. Annualised = `(1+R)^(1/years) - 1`, or `(1+R)^(365/x) - 1` for `x` days. Splitting 70% over 10 years into 7% a year overstates; 160% over 10 years is `2.6^0.1 - 1`, about 10% a year, not 16%; two years of +57.49% then +20% compound to 88.9% against 77.5% summed. Expanding the binomial, the extra terms are positive and the `i^2` term explains most of the gap at ordinary rates; at 1% for 20 years the difference is 122 against 120.
- **Mechanism, scale**: compounding creates no extra wealth by itself. Reinvesting everything in successive tranches, with no costs, yields the same final value; switching asset at equal expected return loses nothing. With payouts withdrawn and not reinvested, plain division by years is the right approximation.
- **Trade-off**: annualising makes odd horizons comparable but silently assumes the same return can be repeated.
- **Does not hold when**: a one-off offer cannot be renewed (a 9-month term quoted per year), or costs and taxes are paid at each step (180 becomes about 160 with a 26% tax at every step, and about 171.5 with a payout of 6 not reinvested).

## 12.2 Log returns and the geometric mean
- **Thesis**: log returns are not more "true", only more convenient to add and model.
- **Mechanism**: `ln(Pf/Pi)`; intermediate terms cancel, so log returns add across contiguous periods and scale linearly with time. Convert back with `e^r - 1`: logs of 10% and 15% sum to 25%, which is 28.4% simple, while simple 10% and 15% compound to 26.5%. Logs are closer to normally distributed, which many tests assume, and avoid rounding drift when thousands of factors sit near 1. The **geometric mean** is `(prod(1+r_i))^(1/n) - 1`; the arithmetic mean overstates it when returns vary (-10% then +40% averages +15% but compounds to about 12.3% per period).
- **Does not hold when**: returns are large (+40% simple is 0.336 log), or the reader needs a figure for cash received; use simple annualised figures to communicate.

## 12.3 Net present value and IRR
- **Thesis**: flows at different dates are comparable only after moving them to a common date.
- **Mechanism**: `PV = F/(1+i)^n` with `n` possibly fractional (days/365). NPV sums discounted flows with outflows negative. The discount rate is personal, not a universal constant: inflation of your own basket, counterparty risk, lost opportunities. At a zero rate NPV is the plain sum. Conclusions can flip with the rate (NPV -50 at 5% can be +37 at 3%). The **internal rate of return** is the rate that zeroes NPV: the constant annual return of an equivalent account, and for a loan its effective cost.
- **Mechanism, limits**: IRR is unique if flows change sign once; with alternating signs there may be none or several. It assumes intermediate flows are reinvested at the IRR itself; a **modified IRR** compounds coupons at an explicit reinvestment rate (a 4% non-callable bond with net IRR about 2.96% falls to about 2.87% at a 1.48% reinvestment rate, and nearer 2.4% with an early call). Delaying every coupon by 10 days barely moves the result, so the assumption is usually benign. IRR is money-weighted: it depends on the timing of the investor's own flows.
- **Does not hold when**: flows are spent, not reinvested (the sum of flows is then the relevant figure), or scales differ greatly.

## 12.4 Comparing instruments: net, same horizon, no shortcuts
- **Thesis**: compare IRR on dated, net cash flows; never "total gain over capital" and never an average of coupons.
- **Mechanism**: a "4.60% a year" single-coupon bond over 13 years paid 59.8% in total, an IRR of about 3.67%, not 4.60%. The plain sum of flows ranks long maturities as better by construction. Annualised figures over a few days mislead: a few hundredths of a point shifts the annualised rate by several points, so only the absolute gain after costs matters under about 30 days. To compare instruments taxed differently, convert to net, or to the gross yield an equivalent lightly taxed bond would need (`net/(1 - t)`; Italy, snapshot 2024: 4.29% gross taxed at 26% is 3.17% net, equal to 3.62% gross at 12.5%; see `personal-finance-italy`). Sensitivity to discount rate, reinvestment rate and horizon should accompany any single figure.

## 12.5 Volatility, tails and drawdown
- **Thesis**: a dispersion number is meaningless without the mean, horizon, frequency and shape.
- **Mechanism**: variance is the mean squared deviation (divide by `n - 1` for a sample); volatility is its root and needs a stated period (daily figures scale by `sqrt(252)` only under independence). The "68% within one deviation" rule is valid only for normal data; the mean-versus-median gap reveals skew (0,0,0,0,+50 has mean +10%, median 0). Ratios of mean to deviation are unstable and meaningless with a negative mean. **Value at risk** at 5% is the 5th percentile of returns (about 5 months in 96); **conditional VaR** is the mean beyond it and lies between VaR and the minimum. VaR locates the start of the tail, not its depth; the history may lack the worst case. **Drawdown** is measured from the running peak: 100 to 120 to 90 is a 25% drawdown while the loss from cost is 10%. Recovery needs `1/(1-p) - 1`: -20% needs +25%, -50% needs +100%; after a return `x` the break-even rebound is `1/(1+x) - 1`.
- **Mechanism, horizon**: for someone who holds to the end, risk is the dispersion of terminal annualised outcomes across entry dates, not daily volatility (−10%, +12%, −10%, +12% is volatile daily and regular annually). Volatility persists over time, returns do not, so volatility is a better forecast input than past return (ch01, 1.2 for the two definitions of risk).
- **Does not hold when**: the holder cannot sit through the path, or the dataset covers a single regime.

## 12.6 Portfolio variance
- **Thesis**: portfolio risk is not the weighted average of asset risks.
- **Mechanism**: `Var = w1^2 V1 + w2^2 V2 + 2 w1 w2 Cov`, with `Cov = rho·s1·s2`. Two assets that each average 10% with 40% deviation and opposite states (+50/-30, -30/+50) give 10% with zero deviation at 50/50 (correlation -1). Adding an uncorrelated asset reduces risk only if its own variance is not far larger than the portfolio's; cash has zero variance but dilutes return. Two highly correlated series (correlation near 0.92) do not diversify each other.

## 12.7 Valuation ratios and the uncertainty of expected return
- **Thesis**: a smoothed earnings yield correlates strongly with later multi-year returns yet gives few independent signals.
- **Mechanism**: CAPE is price over the average of 10 years of real earnings; its inverse is the real earnings yield (CAPE 35 is 2.86%); excess yield subtracts a real bond yield. In one dataset the correlation with the next 10 years' real return was about -0.85 for CAPE and +0.67 for excess yield. A fitted exit rule fired about once in the sample (the late 1990s) and missed 2008 unless loosened (ch13).
- **Mechanism, expected return as estimate**: an expected return is a mean of a wide distribution. A track record of three annual results (+10%, +40%, +5%) cannot exclude -15% next year; five or six years are weak evidence. Costs apply even in loss years, so cost relative to expected return (2% of a 5% expectation takes 40%) is the useful ratio. Present any projection as a range, labelled as "in this sample", never as a forecast.

## 12.8 Adjusting price series; cost basis
- **Thesis**: a series must be adjusted before analysis, and the method matters.
- **Mechanism**: on the ex-date the price falls by about the dividend `D`. Four adjustments: subtract `D` from earlier prices (can turn negative); add `D` to later prices (distorts the real price); reinvest `D` at `P0`, so later prices times `(1 + D/P0)` give a total-return series; multiply earlier prices by `(1 - D/P0)`, the common provider convention, close to reinvestment and failing for large dividends. A **rights issue** conserves value: theoretical ex-rights price = (market cap + proceeds)/new total shares, and the right is worth that price minus the subscription price (cap 847 + proceeds 399 over 322 shares gives 3.866; at a 2.62 subscription price the right is worth about 1.24). Splits need correction factors, else a false crash appears. Average cost = `(old basis x old quantity + new cost incl. fees)/(old + new quantity)`; a sale leaves it unchanged. For foreign assets record cost in the home currency; an "average exchange rate" does not exist because the mean of ratios is not the ratio of means.
- **Does not hold when**: the product pays no dividends to holders (use unadjusted prices) or a provider applies a factor inconsistently.

## Common mistakes
- Dividing a total return by the number of years.
- Averaging prices of an equal-weight index instead of returns.
- Reading a high IRR as a promise when coupons cannot be reinvested at it.
- Quoting a figure without its horizon and base.

## Links
- ch01 risk, ch04 allocation, ch05 discounting, ch06 bond yields, ch13 evidence, ch14 withdrawals.
