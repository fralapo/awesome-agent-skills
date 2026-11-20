# Chapter 10: Options, Certificates and Leveraged Products: Mechanism and Risk

> Educational concepts, not investment advice and not a product recommendation. Product terms, costs, market rules and tax treatment are dated snapshots; read the key information document and re-check current rules.

## Core Idea
In this model, every leveraged or structured product is **a bundle of an exposure, an option-like feature and a credit claim on an issuer or broker**. The useful questions are mechanical: what exactly is the payoff, what event ends it (a barrier, a margin call, a reset), who must pay at the end, what does holding it cost each day, and can it be sold when needed. Product presentations are often sponsored by issuers or brokers; their framing is a position of an interested party. Option theory (the Greeks, covered calls) and daily-reset drag are in `investing-and-financial-history` ch07.

## 10.1 Bought options: defined risk, decaying value
- **Thesis**: buying an option caps loss at the premium; time works against the buyer.
- **Mechanism**: the maximum loss is the premium and no stop is needed; gains can exceed 100% of the premium beyond break-even. The premium grows with time to expiry but less than proportionally (roughly with the square root of time, general knowledge), so the break-even distance widens with maturity. A practical test: compare the move needed to reach break-even with the instrument's ATR (ch02, 2.8); a break-even close to or above the typical daily range makes a short-dated option unlikely to pay. Closing before expiry recovers part of the unused premium. Buying a call and a put together before a major announcement bets on the size of the move, not its direction, and needs a break-even below the expected volatility. Short-dated intraday options around a market open carry wider break-evens.
- **Trade-off**: defined risk against time decay; the seller collects that decay and carries the tail risk.
- **Does not hold when**: implied volatility already prices the event (the move must exceed what is priced).

## 10.2 Knock-out leverage certificates (turbo, mini future, open-ended turbo)
- **Thesis**: a turbo is a leveraged exposure that dies if a barrier is touched.
- **Mechanism**: long or short, listed, with a market maker quoting continuously. To go short one *buys* a short certificate. In a classic **turbo**, strike and knock-out coincide: touching the level (intraday, or through a gap) ends the product at zero, and the loss is the capital invested, not more. In a **mini future** the knock-out sits slightly before the strike, the strike moves daily with financing, and a residual value may be repaid after knock-out. An **open-ended** turbo has no maturity; it lives until knocked out, with the strike adjusted daily for financing (up for longs, down for shorts) and for dividends and futures rolls.
- **Formulas**: theoretical long price = (underlying - strike) / (parity x exchange rate); short = (strike - underlying) / (parity x exchange rate). Market price = intrinsic value + a small, nearly constant gap premium (insurance against gaps, net of expected dividends). Leverage = underlying / (certificate price x parity x exchange rate), roughly `100 / distance-to-barrier %`: underlying 100, strike 90, parity 1 gives a price near 10 and leverage near 10. Leverage rises as price approaches the barrier. Parity converts index points into currency: with parity 10,000, a 950-point index move changes the certificate by 0.095.
- **Costs**: financing, quoted around a few percent a year at the time of the material, erodes open-ended products held for months; a fixed-maturity turbo repays only intrinsic value at expiry, so the gap premium is lost if held to the end; trading stops a few days before expiry; spreads widen around opens.
- **Does not hold when**: the barrier is chosen far away "to avoid being stopped": the loss if wrong is larger, not smaller.

## 10.3 Turbo versus fixed leverage
- **Thesis**: a turbo returns to the same price when the underlying returns to the same level; a daily fixed-leverage product does not.
- **Mechanism**: fixed leverage resets every day. With 7x, the underlying rising 2% then falling 2% ends at 99.96, while the product goes 100 to 114 to 98.04. Sideways volatile markets erode it even if the underlying ends flat. **Intraday reset**: if the underlying moves against the product beyond a threshold (about 17% for 5x), the product loses that leg and restarts on a new strike. Illustration: a 5x short starts at 100; the index rises 17% intraday, the product falls to 15 and resets; the index then closes the day +7.12% from the start, and the product ends near 21.3 (-79%), against about 64.4 (-36%) had no reset occurred. Ranges quoted: fixed leverage typically 2x-7x on listed products, turbos often 20x-30x.
- **Trade-off**: fixed leverage suits one-day views; turbos suit multi-day views with a defined barrier.

## 10.4 Sizing a leveraged certificate
1. Decide the maximum loss in money.
2. Notional = maximum loss / accepted adverse move of the underlying (in %).
3. Capital = notional / leverage.
4. Number of certificates = capital / certificate price.
Example: risk 100 with an accepted move of 1% gives a notional of 10,000; at leverage 10.11 the capital is about 989 and, at 2.13, about 464 certificates; a closer strike (leverage 16.44) needs about 608 for the same risk. The real risk is measured on the notional, not on the capital deposited; the knock-out should sit beyond the stop, never be the stop by default.

## 10.5 Barrier income certificates
- **Thesis**: conditional coupons are paid for selling downside protection on the worst underlying.
- **Mechanism**: **strike** = initial price; **barrier** = a percentage of it (50-70% common); a **conditional coupon** is paid on each observation date if the underlying (in a basket, the **worst-of**) is above the coupon level; **memory** recovers missed coupons later; **autocall** redeems early at nominal plus coupon if all underlyings are above the trigger. At maturity, above the barrier the nominal is repaid; below it, the worst performance applies (a 40% fall repays 600 of 1,000). With a 70% barrier, a breach means at least -30%. Variants: **cash collect** (three cases per date: above strike, early redemption; between barrier and strike, coupon; below barrier, nothing), fixed-coupon versions (unconditional coupons that form a cushion, for example 1% a month for 24 months), **step-down** triggers, **airbag** (below the barrier, loss measured from the barrier: barrier 60%, underlying -50%, repayment about 83 instead of 50, against lower coupons), low-barrier versions (lower yield), variants that drop the worst name from the basket on set dates, and variants that set the strike at the lowest of several initial dates.
- **Pricing logic**: more volatile underlyings pay higher coupons ("no magic"); the holder does not receive dividends, so high-dividend underlyings mark down at ex-dates; worst-of prices drift toward the weakest name. Yield from a market price `X`: (nominal - X) / X plus coupons, which are paid on nominal, not on the price paid.
- **Does not hold when**: markets rise strongly (the share does better) or crash through the barrier; deep barriers reduce but do not remove risk.

## 10.6 Discount certificates
A discount buys the underlying below its price in exchange for a cap: maximum return = cap / purchase price - 1; no dividends (they fund the discount); no capital protection. It is equivalent to a long zero-strike call and a short call at the cap, so volatility and time affect its price. A loss cannot be "rolled": it is realised and the underlying can be rebought.

## 10.7 Range binary certificates (stay-above, stay-below, corridor)
- **Mechanism**: value between 0 and 10; one barrier below (stay-above), above (stay-below) or both (corridor). If no barrier is touched by expiry, 10 is repaid; a touch, even intraday, through a gap or a dividend detachment on an unadjusted share price, ends it at zero. Yield to expiry = (10 - price) / price; maximum loss = 100% of the price. The price reads as a market-implied probability of no touch: at 8.88 the yield is 12.6% and the implied probability about 89%; at 4.32 the yield exceeds 130% with lower odds. Longer maturity means a lower price; price moves little mid-range and sharply near a barrier.
- **Sizing**: risk 200 at an ask of 1.22 buys about 164 certificates, repaying 1,640 if no touch (gain 1,440, about 7:1), with a high chance of losing the 200.
- **Greeks in words**: these products gain as time passes (positive theta) and lose when volatility rises (negative vega), the opposite of directional leverage products.

## 10.8 Issuer risk, liquidity and market stress
- **Thesis**: a certificate is the issuer's debt; a fund holds segregated assets.
- **Mechanism**: if the issuer fails, the certificate can be lost whatever the underlying did. Liquidity depends on the issuer's market making, with quoting obligations that loosen in stress (wider spreads, smaller sizes allowed). In a crash, prices may be missing because the underlying is not trading, moves too fast for the pricing engine, or an exchange volatility interruption suspends trading for minutes; the issuer cannot quote outside the venue then.
- **Hedging**: a short knock-out certificate on an index can offset a portfolio's index exposure: notional of the hedge ≈ portfolio value x beta; it is accurate only for portfolios that track the index; higher leverage uses less capital but raises the chance of losing the hedge in a rally; currency exposure of a foreign index is an extra risk.

## 10.9 Margin products: futures, contracts for difference, binary options
- **Mechanism**: gains and losses follow the notional; margin is a deposit, leverage = 100 / margin %. Over-the-counter contracts for difference can lose more than the deposit in a gap (the abrupt removal of a currency floor is the standard example); a margin call closes positions but does not prevent severe losses; a stop limits loss before the margin call, except through gaps. Financing (swap) is charged or credited daily; a credit can vanish when the futures curve changes shape. Binary options paying 81 on a win and losing 100 on a loss need a 55% win rate to break even (100 / 181); they are now heavily restricted for retail clients in Europe (snapshot). Regulatory disclosures report that a large majority of retail accounts lose money on contracts for difference (figures around 70-85% in various disclosures, dated); a broker-supplied lower figure is not comparable.
- **Does not hold when**: used as a hedge against an offsetting real exposure.

## 10.10 Premium selling and lottery tickets
- **Thesis**: a strategy's win rate says little about its expectancy; the shape of the loss distribution carries the result.
- **Mechanism**: selling far out-of-the-money options, repeatedly and short-dated, collects a small premium on most trades and loses a large amount on a few. Illustration: 20 trades, each collecting 1 of premium; 19 expire worthless (+19) and one moves through the strike and costs 30: net -11, a 95% win rate that loses money. The result depends on the size of the rare loss. A short call has no loss cap beyond the premium; a short put loses up to the strike minus the premium. Buying far out-of-the-money, short-dated options (lottery tickets) inverts the profile: frequent small losses, rare large gains. Expected value is near zero or negative after the bid-ask spread, which on small premiums can be a large share of the price. Covered calls (holding the asset and selling calls above it) give premium income and give up the upside above the strike; the outcome distribution changes, and whether the expected return changes depends on whether the premium exceeds the value of the upside surrendered (position: some hold that premiums are systematically rich, others that the upside is priced in the same way).
- **Trade-off**: steady income with rare large losses versus frequent small losses with rare large gains. Both shapes need a worst-case scenario, not an average.
- **Does not hold when**: the short premium is defined-risk (a spread whose long leg caps the loss), or a hedge is in place and tested.

## Common mistakes
- Measuring risk on the capital deposited instead of the notional.
- Holding an open-ended turbo for months without counting financing.
- Judging a certificate by its coupon without the barrier, worst-of and issuer.
- Using the knock-out as the stop by default.

## Links
- ch02 ATR, ch06 sizing, ch08 claims; ch11 for a side-by-side scan of structured products; `investing-and-financial-history` ch07 (options, daily-reset leverage, structured certificates), ch10 (fraud warning signs); `personal-finance-italy` for tax treatment of certificates.
