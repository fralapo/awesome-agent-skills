# Chapter 06: Bonds, the Yield Curve and Quantitative Easing

> Educational concepts and history, not investment advice or a forecast.

## Core Idea
In this model, a bond is a loan packaged as a tradable asset: a **fixed schedule of payments** whose price moves inversely with the market interest rate. The **yield curve** plots yields across maturities and is read as the market's collective expectation and risk premium. Central-bank balance-sheet policy such as QE acts mainly on this curve.

## 6.1 What a bond is
- **Thesis**: companies and governments borrow by selling bonds, a contract to pay a coupon each period and repay the principal at maturity.
- **Mechanism**: terms run from short to 30 years or more. The promised rate depends on the borrower's ability to pay: a riskier borrower must offer more, the basic risk-return rule (ch01). Seniority matters: in bankruptcy, senior bonds recover first and junior bonds are compensated with a higher coupon.
- **Mechanism, categories**: government bonds (lowest yield; considered virtually risk-free in the borrower's own currency because the state can tax, a simplification, see 6.5); corporate bonds of large stable firms (a bit more); high-yield ("junk") bonds of new or unstable firms (much more, with a real chance of loss).
- **Trade-off**: lower expected return than stocks in exchange for lower typical volatility and priority in bankruptcy.
- **Does not hold when**: the issuer is in distress or the currency collapses.

## 6.2 Yield and price move in opposite directions
- **Thesis**: yield is the coupon as a percentage of the current price.
- **Mechanism**: a bond paying 60 a year with a price of 1,000 yields 6%; if the price falls to 950 the yield rises to about 6.3%, because a new buyer gets the same payments for less. If you hold to maturity the interim price moves do not change what you receive (absent default); if you sell, they do.
- **Mechanism, duration (general knowledge)**: price sensitivity to rates rises with maturity; long bonds lose more when rates rise.
- **Trade-off**: lower credit risk does not remove **interest-rate risk**; a safe long-dated bond can still fall sharply in price.
- **Does not hold when**: you can match payments to liabilities and hold to maturity.

## 6.3 The yield curve
- **Thesis**: the curve of government yields by maturity summarises expectations of future short rates plus a premium for tying money up.
- **Mechanism**: typically upward-sloping. One explanation is the **liquidity premium**: a long bond leaves you with fewer options if better rates appear. Holder of a two-year bond at 18 months waits six months to redeploy, holder of a ten-year bond must sell at a discount or wait over eight years, so long bonds pay more. Other theories exist (expectations, market segmentation; general knowledge).
- **Mechanism, shape**: **flat** or **inverted** curves (short yields above long yields) have often preceded recessions, hence its use as a leading indicator. A flattening during rising policy rates is a common headline.
- **Position (contested)**: the signal is imperfect: the lead time may be a quarter or years, the curve can re-steepen without a recession, and structural factors (central bank holdings, savings flows) may change what it means. Past regularities do not guarantee future ones.
- **Trade-off**: an easily available indicator whose timing is unusable for trading.
- **Does not hold when**: policy distorts the long end (QE, 6.4).

## 6.4 Quantitative easing
- **Thesis**: when policy rates approach zero, a central bank can still ease conditions by buying assets with newly created reserves.
- **Mechanism**: the central bank credits itself electronic reserves and buys government (and sometimes other) bonds from banks in the market. This raises bank reserves, lowers longer-term yields and credit costs, and expands the central bank's balance sheet. It is "printing" only in a loose sense: mostly digital, via open market operations. Aim: ease credit when banks are reluctant to lend and short rates cannot fall further. It was used after 2008 in the US, UK, euro area and Japan.
- **Position (contested, general knowledge)**: supporters say it lowers long yields and supports activity; critics say it inflates asset prices, increases inequality, and blurs fiscal and monetary roles. The size of effects is debated.
- **Trade-off**: lower borrowing costs now versus a large balance sheet to unwind and possible distortions.
- **Does not hold when**: the constraint is not the cost of credit but demand for it.
- **Link**: the monetary mechanics and schools of thought sit in `economics-finance` (central banks, QE, inflation).

## 6.5 Risk-free? Caveats
- **Thesis (general knowledge)**: "risk-free" means free of default risk in the issuer's own currency, not of inflation or price risk.
- **Mechanism**: sovereign credit risk differs by country, currency and borrowing in foreign currency; see `economics-finance` for sovereign debt crises.

## 6.6 Bank runs: duration mismatch (case link)
- **Thesis**: a bank finances long, illiquid assets with short, redeemable deposits, so confidence is part of its capital.
- **Mechanism, 2023 regional bank failures (dated)**: some banks held long-dated, low-rate bonds or fixed-rate mortgages whose market value fell when rates rose; deposits above insurance limits left quickly when customers feared losses, forcing asset sales and crystallising the losses. One failed in the first quarter of 2023; another lost over 100 billion dollars of deposits in a quarter (more than half) and was sold to a larger bank with a loss-sharing arrangement. A crypto-focused bank had concentrated deposits from one industry that withdrew when that industry slid. Cases are in ch09.
- **Does not hold when**: deposit insurance and a lender of last resort stop the run early.

## 6.7 Price, yield-to-maturity and quoting conventions
- **Thesis**: a fixed-rate bond's price is the present value of its flows at the yield the market requires for that maturity and risk (ch05 discounting).
- **Mechanism**: coupon equal to market yield gives par (100); a higher required yield gives a price below 100, and the discount is recovered as the bond is pulled to par. Quick estimate: price is about `100 - (required yield - coupon) x years left`; for a 2% coupon, 3% yield and 5 years that is 95 against an exact 95.42 (95.39 with semi-annual coupons; the shortcut ignores compounding). **Yield to maturity** is the single rate that discounts all flows to the price paid; it assumes coupons are reinvested at that same rate (ch12, 12.3). A fairer price discounts each flow at its own maturity's rate from the government curve; a bond persistently below that value while similar bonds sit on the curve is "off-curve".
- **Mechanism, quotes**: quoted prices are **clean**; cash paid is clean plus **accrued interest** (`coupon x days since last payment / days in period`, often a 30/360 convention). The buyer pays accrued to the seller and recovers it with the full coupon, so buying the day before a coupon gains nothing. Unlike a share dividend, a coupon causes no ex-date price drop, because accrual is handled separately. Platforms differ in showing clean, dirty, gross or net-of-tax figures: reconstruct dirty price as total cash over quantity. If an issuer quotes an annual rate, the semi-annual coupon may be compounded (`(1+r)^(1/2) - 1`, 3.80% at r = 7.75%) rather than `r/2`.
- **Does not hold when**: the bond has embedded options (6.11) or the issuer's credit changes.

## 6.8 Duration and interest-rate risk
- **Thesis**: for small yield moves, the percentage price change is about minus modified duration times the change in yield.
- **Mechanism**: **Macaulay duration** is the weighted-average time of payments (weights are discounted flows); modified duration is that divided by `(1 + yield)`. A zero-coupon bond has duration equal to maturity; coupons shorten it; at maturity it falls to zero. With duration 6 at a 3% yield, modified duration is 5.8 and a one-point rise cuts the price about 5.8%. The linear estimate is good for about a point; beyond that **convexity** makes the true price curve lie above the tangent, so falls are slightly smaller and rises slightly larger. Rising yields also hurt long bonds with low coupons most: a 1.7% thirty-year bond priced near 62 (yield about 3.9%) loses about 11 points on a one-point rise, to roughly 50-51. In this model (position), forecasting rates beyond three to four years is closer to guessing than analysis, so a long bond held without a need to wait for maturity is a leveraged rate position. The extra yield for extending is often only a few tenths of a point on a flat curve.
- **Mechanism, single bond versus bond fund**: a single bond's duration shrinks to zero, so its outcome is locked if held to maturity (absent default). A fund or index keeps duration roughly constant by selling shortened bonds, at a loss if rates rose, and buying new ones; the interim loss becomes realised and is not made back, only reinvested at higher coupons. In a worked case of seven 3% bonds and a 2-point rise, both lost 4.8% but after six years the fund returned 3.19% a year against 3.24% for the singles. A duration-4 fund bought at 1% and sold seven years later at 5% showed a price loss above 12%; a corporate fund of duration about 5 fell about 20% between 2020 and 2022 (dated). A **target-maturity** fund (holdings clustered around one date, dissolved then) behaves near the end like a single bond, at the cost of thin liquidity, tracking error and opaque redemption value; its payoff is estimated, not promised.
- **Trade-off**: a fund gives diversification and small tickets; a single bond gives a defined end value but needs many issuers for large sums.
- **Does not hold when**: the horizon is about 10 to 20 years (rate swings average out and a fund held for at least its duration locks most of the return), or in high-yield funds, where coupons compensate.

## 6.9 Quote quality, liquidity and retail-only bonds
- **Thesis**: the "last" price is only the latest trade; you buy at the ask and sell at the bid.
- **Mechanism**: the spread is the cost of an instant exit (bid 93.96, ask 94.71 at three years is about 0.3 points of yield a year); a bond bought at 103 resaleable at 96 loses 7 points at once. Screening for liquidity: a trade every day, small spread, adequate volume. Annualised yield means little under roughly 30 days: a bond 12 days from maturity can show 4% annualised for a gain of a few hundredths of a point per 100, before fees. In an order book a market order walks the book; a limit order queues behind earlier ones at that price. Bonds sold only to small buyers can quote below the curve; explanations (low liquidity, flagged complexity, collective action clauses, fear of unequal treatment) were each tested and none fully confirmed. For a holder to maturity the extra yield is real; a seller gets the lower price.
- **Does not hold when**: the bond is held to maturity and the spread is paid once.

## 6.10 Inflation-linked bonds
- **Thesis**: two designs differ in when inflation compensation arrives, and both lag the index.
- **Mechanism**: design A pays, each period, a real coupon plus a revaluation of principal (coefficient = index now over index at the last coupon); design B accrues inflation into principal, paid at maturity. A pays earlier and so compounds; B defers everything and is more rate-sensitive. Monthly index data come with a two-to-three-month lag; a **floor** prevents negative coupons, and whether the next period recovers a past drop depends on the scheme (inflation -2% then +3% pays about +1% under a "recover from the lowest level" scheme and 3% under a reset scheme). Accrued interest includes revaluation already realised. An inflation-linked bond beats a fixed one only if realised inflation exceeds the **break-even** implied by prices (e.g. about 0.7% in one snapshot, where at 2% inflation the linked bond paid about a point more). A loyalty bonus, if offered, goes only to those who buy at issue and hold to maturity, and is worth about 0.1-0.15 points a year on long terms.
- **Trade-off**: protection of purchasing power against price risk if sold early; inflation is the basket's average, not your own.
- **Does not hold when**: inflation forecasts are needed (they are unreliable beyond a year or two).

## 6.11 Embedded options and structured coupons
| Feature | Who holds the option | Effect on the holder | Watch for |
|---|---|---|---|
| Callable | issuer | repaid when rates have fallen; reinvests at worse terms | call premium (e.g. +50% of a coupon in year 3, +25% in year 4) partly compensates; not exercised if rates rise |
| Step-up | none (schedule) | high coupons come late; IRR is below the arithmetic mean (5.05% mean, about 4.97% IRR) | with a call, the issuer redeems just before the large coupons |
| Putable | investor | right to redeem at par on a date; small value, useful if rates rise or credit falls | lost if sold, or if bought outside the offer |
| Floater with cap/floor | issuer/investor | coupon = `min(max(floor, k x rate + margin), cap)`; cap truncates good scenarios | best read as a simulated distribution (resampled rate paths), not one number |
- **Mechanism**: a callable step-up is "buying a car in instalments you can end at any time": it comes back after the smallest one. A strong early coupon followed by a capped floating tail usually has a mean below an equivalent fixed bond; with only 3-5 large rate-rise episodes in history, conclusions about the tail are weak (ch13). Compute return in each call and no-call case, and with reinvestment at rates one or two points lower, never higher.
- **Does not hold when**: the call is far out of the money or the issuer cannot refinance.

## 6.12 Credit, ranking and what bond diversification is for
- **Thesis**: excess yield is compensation for a risk; ask which.
- **Mechanism**: same issuer and maturity imply the same yield, so a much higher yield signals credit risk, an unstable currency, optionality or a distorted annualisation. A typical recovery in default is about 10% of principal (illustrative); claims rank, and subordinated or junior holders may get nothing while senior or customer claims are paid. Ratings lag (large institutions were top-rated until shortly before default) and markets also weigh repayment history. For a distressed bond, yield to maturity is the return only if the issuer survives: list scenarios (full repayment, partial recovery, default now, default later), assign explicit probabilities, compute outcomes in money, weight, and annualise: an expected gain of +66% over 5 years is about 10.6% a year against 13.5% in the good case. The probabilities are subjective, and a single holder never receives the average. For a bond held to maturity, volatility is irrelevant and diversification is only about default: spread across issuers, countries and maturities (staggered to match staggered spending). In this model (position), around ten investment-grade issuers in sizable blocks is a workable minimum; a small need is simpler in cash.
- **Does not hold when**: the issuer is large enough that recovery depends on policy rather than ranking.

## 6.13 Foreign-currency bonds
- **Thesis**: extra yield in another currency is paid for in exchange-rate risk.
- **Mechanism**: flows are converted at each date's rate and tax follows conversion, so compute return on converted net flows. Moves are asymmetric (+100% on one side is -50% on the other). Fragile currencies pay high yields as compensation. Resampling historical rate paths (overlapping windows are not independent) in one example gave a mean near 4.4% with a standard deviation of 5.2%, worse than the home-currency bond in 43% of paths; a rise of the home currency to 1.55 made the return negative.
- **Does not hold when**: the holder has liabilities in the same foreign currency.

## 6.14 Bonds inside a portfolio and cash substitutes
- **Thesis**: for a long-horizon holder, risk is the dispersion of the terminal result, and bonds lower it mostly by cutting upside.
- **Mechanism**: in historical rolling-window tests of one country's equity index, each +10% in bonds cost about 0.2-0.3 points of average annual return; the mean of the worst 10% of outcomes improved up to roughly 70/30-80/20 and then worsened; with a diversified world index and a 20-year horizon bonds added little. A 10% sleeve does little; a meaningful drawdown reduction needs about 30%. A threshold backtest (hold bonds only when net yield exceeds a level) cut dispersion at moderate thresholds but missed equity rallies at high ones, and depended on the sample by about half a point.
- **Mechanism, cash substitutes**: compare a fixed deposit, short government bills and money-market funds on net return over the same term, including the early-exit rate, eligibility conditions, fees and year-end duty; a 0.5% fee on entry and exit can cancel six months of yield. Guarantees cover deposits up to a ceiling (in the EU, 100,000 per depositor per bank); money-market funds track an overnight benchmark plus a few basis points and are meaningful only when policy rates exceed zero.
- **Does not hold when**: the horizon is under about 10 years (bonds are then the target asset) or the investor would sell in panic.

## Common mistakes
- Equating "government bond" with "no price risk".
- Treating an inverted curve as a timing tool.
- Reading QE as simply giving cash to the public.
- Quoting a simple average of step-up coupons as the yield.
- Treating a high yield as a bargain instead of a price for risk.

## Links
- ch01 risk-return, ch05 discounting, ch07 options, ch09 crises, ch12 IRR and NPV, ch14 ladders and withdrawals, `economics-finance` for central banks and public debt.
