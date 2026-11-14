# Chapter 03: Corporate, Bank and Structured Bonds

> Educational concepts, not investment, tax or legal advice. Figures are snapshots (Italy, 2024-2026, year stated), to be re-checked against the rule in force.

## Core Idea
In this model, a bond that yields much more than a comparable government bond is paying for something: credit risk, an embedded option, a currency, subordination or illiquidity. Italian tax then widens the gap: coupons are taxed at 26% (not 12.5%) and the way return is split between coupon and price decides how much of the tax can be softened by losses. Read the structure before the rate.

## 3.1 Excess yield is compensation for a risk
- **Thesis**: bond markets are consistent; if one bond yields far more than comparable ones, ask what is being paid for.
- **Mechanism**: same issuer and maturity imply the same yield. Higher yield signals higher issuer risk, an unstable currency, optionality or a distorted annualisation. Lists sorted by yield are dominated by these cases. Funds meant to cover expected expenses are exposed to a binary loss if they hold foreign-currency or fragile-issuer bonds, which is the cost of the extra yield.
- **Trade-off**: higher expected income versus a binary loss (default, devaluation).
- **Does not hold when**: short, high-grade bonds with transient mispricing exist but are small in money terms.
- **Worked example**: a bond at 39% in a fragile currency, or a euro bond at 4.06% annualised because maturity is 12 days away.

## 3.2 Callable bonds and reinvestment risk
- **Thesis**: a call is an advantage handed to the issuer; the investor is repaid exactly when rates have fallen.
- **Mechanism**: the issuer calls when it can refinance cheaper, when credit has improved, or when it has cash. A call premium (+50% of a coupon in year 3, +25% in year 4, none in year 5) partly compensates and signals when calling is cheapest. Compute IRR, net IRR and modified IRR in call and no-call cases: IRR can rise while the total euro gain falls (about 1,480 down to 740 per 10,000 net in one example).
- **Worked example**: corporate coupon 4.5% for 5 years: gross IRR 4.47%, net about 3.11% at 26% if held; if called and reinvested at 3%, net about 2.78%, below a comparable government bond at about 2.88% net (Italy, snapshot 2024).
- **Does not hold when**: rates rise and the call is not exercised; the investor is then locked in below market.

## 3.3 Step-up coupons and the arithmetic-average error
- **Thesis**: a step-up schedule looks generous, but the mean coupon overstates the yield.
- **Mechanism**: high coupons arrive late, low ones early, so IRR is below the mean. Coupons 4.25%, 4.65%, 5.05%, 5.45%, 5.85% (two years each): mean 5.05%, gross IRR about 4.97%, net about 3.69% at 26%. Step-ups appeal to retail buyers because increases are far away; step-downs are almost never offered.
- **Call plus step-up**: structurally unfavourable. If rates fall the issuer calls just before the large coupons; if they rise the investor is stuck. Analogy: paying a car in instalments of 500, 600, 700 with the buyer free to return it at any time; it comes back after the smallest instalment.
- **Does not hold when**: non-callable and held to maturity; then IRR is exact.

## 3.4 Fixed-then-floating with cap and floor
- **Thesis**: after a high fixed period, a capped floating coupon is a distribution of outcomes whose mean is usually below an equivalent fixed bond.
- **Mechanism**: coupon = min(max(floor, k x benchmark + margin), cap). The cap truncates good scenarios; the floor protects only against negative rates. Estimate by resampling historical monthly rate paths (hundreds of draws) and reporting mean, median and quartiles. "Sell after the high-coupon period" fails: with low rates the price falls below par, with high rates it is better to hold.
- **Worked example**: 4.85% for 2 years then 2 x rate with cap 4.85%: net IRR range 0.68%-3.58%, median about 2.18%, versus about 3.2% net on a comparable government bond.
- **Does not hold when**: the history of large rate rises is tiny (3-5 episodes), so tails are statistically weak.

## 3.5 Subordination, ranking and bank bonds
- **Thesis**: the claim's rank in the creditor queue matters as much as the issuer's name.
- **Mechanism**: subordinated debt absorbs losses before senior debt; a bank's customer claims (deposits) can be senior to bondholders and leave nothing. Under the post-2016 EU resolution framework, bank creditors can be bailed in (general knowledge; Italy, snapshot 2026). Ratings lag: large institutions were top-rated until just before default. Features not meant for retail: very large minimum denominations, subordination, foreign currency, very long maturities, ignored call clauses.
- **Trade-off**: higher coupon versus loss-absorbing position.
- **Does not hold when**: the bond is senior, short and from a well-capitalised issuer, where the difference is small.

## 3.6 Distressed bonds: expected return needs scenarios
- **Thesis**: for a bond far below par, yield to maturity is the return only if the issuer survives.
- **Mechanism**: list scenarios (full repayment, immediate default, default after a year, partial recovery), give each an explicit probability, compute outcomes in euros (some rates are undefined), take the weighted average, divide by outlay and annualise (1+R)^(1/years) - 1. The probabilities are subjective, and the average is attainable only across many bonds.
- **Worked example**: outlay 60; 80% full repayment, 15% partial with 20% recovery, 1% total loss, 4% default after a year: expected gain about +66% over 5 years, about 10.6% a year versus 13.5% in the good case.
- **Does not hold when**: recovery depends on creditor ranking and customers rank first.

## 3.7 Issuer concentration and what diversification is for
- **Thesis**: for a bond held to maturity, volatility is irrelevant; the reason to diversify is default.
- **Mechanism**: spread across issuers, countries and maturities in blocks (a new issuer above 5,000-10,000 per position; around ten issuers of about A quality or better); stagger maturities to match staggered spending. Below roughly 1,000 euro of need, cash is simpler.
- **Does not hold when**: the amount is small enough that fees dominate.

## 3.8 Foreign-currency bonds
- **Thesis**: extra yield in another currency is not free.
- **Mechanism**: flows are converted at the date's rate; tax is computed after conversion; compute IRR only on euro net flows. Percentage moves are asymmetric (+100% on one currency is -50% on the other). Fragile currencies pay high yields as compensation; the pick-up pays off only if the premium exceeds two to three points and still adds risk. Simulate by sampling historical rate paths over the bond's life; overlapping windows are not independent.
- **Worked example**: a dollar bond with 5.78% gross IRR at a fixed 1.07 shows about 5.3-5.5% net versus 3.69% for the euro equivalent; if the euro rises to 1.55 the return turns negative; the simulation gave mean 4.36%, standard deviation 5.2%, worse than the euro bond in 43% of paths.
- **Does not hold when**: the investor has liabilities in the same foreign currency.

## 3.9 Tax: coupon asymmetry, discount bonds, above par
- **Thesis**: at equal gross yield, structure changes net yield because coupons are taxed as capital income while price gains are "miscellaneous income" (Italy, snapshot 2025).
- **Mechanism**: markets equalise **gross** yield; a bond above par pays tax on large coupons and then holds a capital loss usable only against same-category gains within about four years (not against fund gains). Coupons 5%, 3%, 1% priced 109.22, 100, 90.8 at the same gross IRR near 3%: net about 2.42%, 2.64%, 2.65%. For a bond **issued below par**, the difference to par is capital income by exponential interpolation: theoretical price = issue price x (redemption/issue)^(elapsed/total days); redemption minus theoretical price is taxed outright, theoretical minus purchase price is a gain or loss. Theoretical price 91.53, buying at 94: capital income 8.47 taxed plus a 2.47 loss that only helps against future gains.
- **Government versus corporate compounding**: simple-interest government 12.5% versus accumulating 26% fund; at equal gross yield the corporate accumulation wins only after many years (3% about 12 years; 7% about 6); with +0.5 point extra yield within 3-5 years.
- **Does not hold when**: the investor has large realised gains to offset, which makes the loss immediately valuable.

## 3.10 Bonds inside a portfolio and cash buckets
Bonds lower the dispersion of a long-horizon result mostly by cutting upside: each +10% in bonds costs about 0.2-0.3 points of average return; a meaningful drawdown reduction needs around 30%. Liquid reserves and dated spending belong in fixed euro amounts, not percentages (see ch01 and the bonds chapters of `investing-and-financial-history`).

## Common mistakes
- Averaging step-up coupons.
- Treating a call premium as pure generosity.
- Counting a capital loss as cash instead of an expiring credit (ch05).

## Links
- ch02 government bonds; ch04 bond ETFs; ch05 losses; ch11 mis-selling; `investing-and-financial-history` ch06 (mechanics).
