# Chapter 07: Derivatives and Options: Mechanism

> Educational concepts and history, not investment advice or a forecast. This chapter explains how options work and what they cost; it does not recommend strategies.

## Core Idea
In this model, an **option** is a contract that separates the *right* to act from the *obligation* to act and sells the right for a price (the premium). Everything in options is the pricing of that right: what the asset might do, how far away the strike is, and how much time is left.

## 7.1 The basics
- **Thesis**: a call gives the buyer the right (not the duty) to buy at a strike price until expiry; a put gives the right to sell.
- **Mechanism**: the buyer pays the premium upfront; the seller (writer) receives it and takes the obligation. An **out-of-the-money** call has a strike above the current price; it is not profitable to exercise now. Example: a stock at 400, a 30-day call struck at 420 with a premium of 4.
- **Payoff, writer of an uncovered call**: keeps the premium if the price stays flat or falls, but faces losses that grow without limit as the price rises, because the writer must deliver at the strike.
- **Trade-off**: options give leverage: more likely to make a lot or lose it all, and so are riskier than most long-term investors need.
- **Does not hold when**: used as insurance against a specific known exposure.

## 7.2 The Greeks: what moves an option's price
- **Thesis**: each Greek isolates the effect of one factor on the premium.
- **Mechanism**:
  - **Delta**: change in the option price per 1 move in the underlying. Between 0 and 1 for calls, between -1 and 0 for puts. Higher for in-the-money options; used as a rough gauge of the chance of ending in the money.
  - **Gamma**: how much delta changes for each 1 move; highest near the strike, lower deep in or out of the money. Example: a 2.00 option with delta 0.2 and gamma 0.1 rises approximately 0.25 (delta + gamma/2) if the stock rises by 1, and delta becomes 0.3.
  - **Theta**: time decay; each day closer to expiry lowers the value for the buyer and benefits the writer.
  - **Vega** (general knowledge): sensitivity to expected volatility of the underlying; more expected volatility raises premiums.
  - **Rho** (general knowledge): sensitivity to interest rates; usually minor for short-dated options.
- **Trade-off**: the Greeks change as price and time change, so a position's risks move even if you do nothing.
- **Does not hold when**: the underlying jumps (gap risk) so local sensitivities mislead.

## 7.3 Covered calls: the cost of income
- **Thesis**: selling a call on a stock you own turns some upside into current income; it is not a free extra return.
- **Mechanism**: the stock covers the obligation, so the uncapped downside of the uncovered call disappears. Three claimed sources of return: dividends, price appreciation up to the strike, and premium. But the third source is created by **restricting the second**: the payoff is capped. If the stock rises 50% in the 30 days, the covered-call return is limited to the move to the strike plus the premium (about 6% in the example). A flat or falling stock is cushioned by the premium: that is the "downside hedge", which is partial.
- **Other costs**: funds that run the strategy tend to charge higher management fees (a dated example: about 0.60% against 0.03%) and trade more; premiums can be taxed as short-term gains; repeated exercise and repurchase can leave you with fewer shares and realised losses even if the stock is flat; selling calls less likely to be exercised (higher strike, shorter term, lower volatility) pays lower premium, so "safe" income shrinks to pennies while still capping rare large gains. Since a few days drive most of the return, a systematic cap will miss them.
- **Evidence**: a high-yield covered-call fund (about 10% yield) trailed a plain index fund yielding under 2% over one examined period (dated; check current data).
- **Trade-off**: smoother and higher cash payout against lower total return in strong markets; a yield is not a return.
- **Does not hold when**: you want a specific capped payoff or income profile and understand that it is a different payoff, not a better one.

## 7.4 Portfolio insurance as a synthetic option (case link)
- **Thesis**: you can replicate an option's payoff by trading the underlying (selling as prices fall, buying as they rise).
- **Mechanism**: in the 1980s computer-driven strategies promised upside with limited downside; they depended on being able to sell into falling markets, and many acted in batches. If many followers do the same thing, the hedge becomes a source of selling pressure, a feedback loop (ch09, 1987).
- **Does not hold when**: market liquidity vanishes.

## 7.5 Credit derivatives and leverage (case link)
- **Thesis**: a derivative can multiply exposure to an event without owning the underlying.
- **Mechanism**: credit default swaps insure against a borrower's default; if many contracts are written on the same mortgages, notional exposure can exceed the insured assets by a large factor (an account from the 2008 case cites growth from about 0.9 trillion to over 60 trillion dollars of insured credit; a dated popular figure). A seller with insufficient capital turns a tool for hedging into a concentrated bet (ch09).
- **Does not hold when**: collateral, clearing and capital rules limit the stack.

## 7.6 Payoff and price decomposition; simple combinations
- **Thesis**: an option's price is intrinsic value plus a time-and-volatility component; the buyer's maximum loss is the premium.
- **Mechanism**: call payoff `max(0, S - K)`, put payoff `max(0, K - S)`; premium = intrinsic + expectation component (days left, volatility). European options exercise only at expiry, American any time (worth more, harder to price); settlement is in cash or by delivery. Worked case: underlying 6.11, strike 6, premium 0.31 (0.11 intrinsic + 0.20 time): break-even 6.31. A move to 7.23 is +18% for the share and about +296% for the call; below 6 the call loses 100%. Wide quoted spreads are normal where many strikes and expiries barely trade.
- **Mechanism, combinations**: a **protective put** on a held asset caps the maximum loss at `price - strike + premium` (minimum profit and loss = `strike - price - premium`) and lowers upside by the premium; its price rises with implied volatility, so insurance bought after a scare is expensive. A **straddle** (call plus put, same strike) profits only from large moves; because most days the market moves little, short-dated straddles tend to lose. A **vertical spread** (buy one call, sell a higher one) caps loss at the net cost and gain at the strike gap minus cost.
- **Trade-off**: lower cost than a naked option, in exchange for giving up part of the payoff.
- **Does not hold when**: the asset is liquid and can simply be sold (insurance is mainly a tool for assets that are hard to sell).

## 7.7 Futures, margin, shorts and contracts for difference
- **Thesis**: symmetric obligations create loss potential beyond the capital.
- **Mechanism**: a future has no upfront price; the daily difference is settled against a margin deposit. A margin call asks for more cash and, if unmet, the broker closes the position. A margin loan, a contract for difference and a short sale behave like a position at the current price with collateral posted (e.g. about 3% on a major currency pair). A purchase loses at most the amount invested; a short has a theoretically unlimited loss, and a lender can recall borrowed shares, forcing purchases that push the price up (a squeeze). Compute returns on blocked margin, not on notional; fees on both sides can erase tiny gains.
- **Does not hold when**: used for hedging, its original purpose, against an offsetting real exposure.

## 7.8 Daily-reset leverage and volatility drag
- **Thesis**: a daily-leveraged product does not deliver leverage times the multi-day return.
- **Mechanism**: each day the return is multiplied by `L` and compounding restarts. Since `(1 + x)(1 - x) = 1 - x^2`, each up-down pair loses `(Lx)^2`. An index going 100 to 110 to 100 leaves 2x near 98 and 3x near 94.5; 100 to 90 to 100 leaves 2x near 97.8 and 3x near 93. In sideways markets capital decays day by day; in strong low-volatility trends it multiplies. Leverage drifts for a margin loan instead of resetting, so the rule does not describe loans.
- **Mechanism, wipe-out**: a single daily fall of `1/L` ends the product; there is no recovery whatever follows.

| Leverage | Fall of the underlying in one day that wipes out |
|---|---|
| x2 | 50% |
| x3 | 33% |
| x4 | 25% |
| x5 | 20% |
| x10 | 10% |

- **Mechanism, cost**: the expense ratio understates the true cost. Compare the real product with a frictionless replica (index x `L`, day by day) over rolling N-year windows, never cumulatively since launch: the gap estimates financing, swap and tracking costs, and grows with volatility (in a dated backtest, about 7 points a year for 3x on a volatile growth index and about 1 point for 2x on a broad index). A short history without such a move is weak evidence for a decade-long hold.
- **Does not hold when**: held for a single day, or the real product beats the replica through data errors or favourable tracking.

## 7.9 Other forms of leverage and temporary hedges
- **Thesis**: borrowing against a portfolio avoids a daily reset and adds margin-call risk.
- **Mechanism**: with securities pledged and a line capped at a share of their value (60% in one example), a margin call triggers when usage reaches roughly 70-75%; interest is a short-term rate plus a spread. Using the line for temporary liquidity avoids realising gains. In this model (position) a sensible maximum is around 1.5x, because interest is certain and returns are not; historical simulations favour leverage in most windows but losses cluster in crises with high rates. A fund holding shares with a cash margin and bond futures on top (say 90% shares, 10% margin, 60% notional in futures) is implicitly about 6x on the bond sleeve; the rough gain is `60% x bond yield - 10% x equity return`, and a rule of thumb says complex strategies need about 20 years of data.
- **Mechanism, hedging**: covering a position for a few days with a fixed-leverage short product (notional about `V/L`) can be cheaper than selling and re-entering, but decays with oscillation, has financing and spread costs, and a 13-14% adverse move nearly wipes out 7x.
- **Does not hold when**: collateral is concentrated or illiquid, or the holder starts from financial fragility.

## 7.10 Structured certificates
- **Thesis**: coupons and repayment depend on thresholds, so payoffs have cliffs.
- **Mechanism, autocallable**: on observation dates a coupon is paid if all underlyings are above a coupon threshold (a *memory* feature recovers missed coupons); if all are above a trigger the product redeems early (the trigger often steps down); at maturity, above the barrier the nominal is repaid, below it the worst performer sets repayment. With a barrier at 60%, a worst performer at 59.9% repays 59.9, a cliff against 100. Correlation among underlyings concentrates the tail. *Cash-collect* products (general knowledge) pay conditional periodic coupons with a barrier at maturity but no early redemption; the same logic applies.
- **Mechanism, capital protection**: the certificate tracks the unadjusted price, so the holder receives no dividends, and the issuer hedges by keeping them; participation is calibrated to expected dividends (participation 1.45 on +80% gives 216, but a share paying 6% a year rises far less unadjusted). Protection holds only at maturity and subject to issuer solvency; market value before then may be below nominal.
- **Mechanism, issuer**: the issuer sets terms, makes the market and earns the spread; costs sit in the price (entry about 1%, exit up to about 2% in one product). If the issuer fails the certificate can be lost whatever the underlying did.
- **Trade-off**: high coupon against tail risk and issuer risk; wins in a deep crisis, loses in rising or high-dividend markets.
- **Does not hold when**: the product is bought at a price above nominal, or underlyings are uncorrelated.

## 7.11 Replaying a payoff on history
- **Thesis**: a distribution of outcomes can stand in for closed-form pricing as a diagnostic.
- **Mechanism**: replay every historical start date with barriers and triggers rescaled to today's levels; keep sequence and correlation (resample in blocks, not single days); use unadjusted prices if the product pays no dividends. Early redemptions create enormous annualised returns that distort averages. Resampling daily log returns gives many paths, a payoff per path, and the share of paths paying zero. The result is a historical expectation, not a signal (ch13).
- **Does not hold when**: volatility regimes shift or the history is back-filled or short.

## Common mistakes
- Believing a yield from selling options is "extra".
- Ignoring that selling options without cover has unlimited loss.
- Treating delta as a certain probability.
- Reading "3x" as "three times the multi-day return".
- Judging a certificate by its coupon without the barrier and the issuer.

## Links
- ch05 valuation, ch09 crises, ch11 decisions, ch12 compounding, ch13 backtests.
