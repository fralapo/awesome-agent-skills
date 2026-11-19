# Chapter 11: Scanning and Comparing Structured Products: A Reading Procedure

> Educational procedure, not investment advice and not a product recommendation. Any real product is governed by its final terms, its key information document and the issuer's conditions. Numbers below are illustrative arithmetic, not quotes.

## Core Idea
In this model, a conditional-coupon product is **a bond-like claim plus a short option position on the weakest underlying**, packaged with observation dates, triggers and an issuer. Comparing two products by their headline coupon is the most common error, because the coupon is the price of a set of conditions that differ from product to product. A scan therefore extracts the same fields from every product, computes the same few numbers, and tests each one against the same scenarios. The barrier, memory, autocall and airbag mechanics themselves are described in ch10 (10.5); this chapter is the procedure for reading them side by side.

## 11.1 Fields to extract (the same ones, every time)
- **Structure**: single name, basket, or worst-of basket; the currency of each underlying; whether a basket member can be removed on a set date.
- **Thresholds, kept apart**: the coupon level (the level on an observation date above which a coupon is paid), the bonus or coupon barrier, the redemption barrier at maturity, and the autocall trigger. They are often different numbers. A product can pay no coupon while its capital is still safe above the redemption barrier.
- **Observation schedule**: coupon dates, autocall dates and the final observation. Note whether the redemption barrier is watched only at maturity (European style) or at any moment (American style, intraday touches), because a continuously watched barrier is triggered more often.
- **Memory and step-down**: whether missed coupons are recovered later, and whether thresholds fall over time.
- **Issuer call**: a *callable* product can be redeemed by the issuer on set dates whatever the underlying did; an *autocall* redeems only when the trigger is met. A callable product is usually redeemed when the issuer finds it cheaper to refinance, which tends to be when the holder would prefer to keep it.
- **Fixing**: the reference prices from which all thresholds are computed. A product issued after a fall has thresholds set from lower prices, so the fixing date belongs in the comparison.
- **Coupon basis**: the coupon is paid on nominal (usually 100), not on the price paid; record the periodicity (monthly, quarterly, annual).
- **Dates of detachment**: record date (the holder must own the product before it), ex-date and payment date.
- **Currency**: whether the product is quanto (the conversion rate for payouts is fixed) or exposed to exchange rates.
- **Issuer, liquidity and costs**: issuer credit, the market maker, whether the product is bid-only, spreads and per-order fees.

## 11.2 Put the coupon on one basis before comparing
- Express every coupon per period and then per year by simple multiplication, with no compounding: a 1% monthly coupon is 12% a year before losses and before any change in price.
- Compute the yield from the **market price**, not from nominal: (coupons received + redemption - price paid) / price paid, over a stated horizon. The same coupon on a lower price gives a higher yield, which is also why a low price often signals a higher perceived risk.
- Label every figure as *potential*. A conditional coupon is paid only if the conditions hold on each date. A probability-weighted expectation is meaningful only with stated probabilities that were themselves tested (see 4.10 and ch08 on why such estimates are fragile).

## 11.3 Buffers: how far can each underlying fall?
- For each underlying: buffer to the coupon level = (current price - coupon level) / current price. Repeat for the redemption barrier. For the autocall, the buffer is the rise needed to trigger.
- In a worst-of product the **smallest** buffer governs. Adding names to a basket does not raise that minimum; it adds more names that can become the minimum, and the minimum changes every day.
- Report the minimum buffer as a percentage, and the number of observations at risk. A product 5% above its coupon level is a different risk from one 30% above it, even when the coupon is identical.

## 11.4 Payoff scenarios: four states, one grid
Run the same four states for every product, with generic percentages:
- **A. Autocall**: on an observation date every underlying is above the trigger. The product repays at nominal plus the coupon due and stops. Capital returns early, future coupons are lost and must be reinvested, and any upside beyond the coupon is not captured.
- **B. Coupon paid, capital intact**: the worst name sits between the coupon level and the barrier. The coupon is paid (or recovered later with memory); the capital is still exposed at maturity.
- **C. Coupon missed, capital intact**: the worst name is below the coupon level but above the barrier. No coupon for that period; with memory, the missed amounts may come later. The market price usually falls meanwhile.
- **D. Below the barrier at maturity**: redemption follows the worst performance. With a 40% fall in the worst name, the repayment is about 60 per 100 (illustrative). An airbag measures that fall from the barrier instead of from the start, which reduces the loss but not the risk.

Grid: for worst-of falls of 0%, -20%, -40% and -60% at maturity, and for a path of two years with no autocall, list the total cash received per 100 of nominal. Illustration: 1% a month for 24 months, no autocall, no coupon missed, worst name down 40% at maturity gives 24 + 60 = 84, a loss of 16 before any price effect. If the coupons had been missed for twelve months and never recovered, the total is 12 + 60 = 72. The grid shows where the coupon compensates the capital loss, and where it does not.

Also run the **exit** scenario: a sale before maturity happens at the market price, which can be below the maturity grid when the worst name has fallen. The maturity grid and the exit grid are different questions and should not be mixed.

## 11.5 Price, coupon detachment and fixing effects
- The price includes the coupon until its record date. After detachment it drops by about the coupon amount. A fall over a coupon date mixes two effects, so measure total return: price change plus coupon.
- A price below 100 with redemption at 100 adds a mechanical gain of (100 - price) / price to maturity. That arithmetic is available only if redemption at par actually occurs in the scenario being read.
- Buying after the record date means no coupon for that period, at a lower price. The two are equivalent only if the price drop equals the coupon; it rarely does exactly.
- After a call, the issuer can offer a similar product under a new identifier with barriers reset at a new fixing. The comparison restarts with new fields.

## 11.6 Frictions that change the answer
- **Fees**: an intermediary charges per order. On small tickets the fee can absorb a coupon. Express the cost as a percentage of the amount invested, for purchase and sale.
- **Spreads and bid-only status**: quotes can be wide, and near a barrier or in a stress the issuer may stop quoting buy prices. A product that cannot be sold is held to maturity, and the grid then applies.
- **Quanto and currency**: a quanto feature fixes the conversion rate for payouts. It removes exchange-rate risk from the payout, but not from the market price of the product while it is held, which still moves with the exchange rate for a foreign underlying.
- **Issuer credit**: the payout is an unsecured claim on the issuer. Record the issuer's rating and whether the product carries any protection. If the issuer fails, the grid is replaced by zero (ch10, 10.8).
- **Tax**: not treated here; see `personal-finance-italy`.

## 11.7 Comparison checklist
1. Write down the four thresholds (coupon, barrier, autocall trigger, step-down) for each product.
2. Identify the worst-of name and the minimum buffer today.
3. Compute the coupon yield from the market price over a stated horizon.
4. Run scenarios A to D and the grid, and set the result beside a plain holding of the weakest name.
5. Check whether the product is callable or autocall-only, and what reinvestment follows.
6. Note the record date and what the current price already includes.
7. Compute fees and spread as percentages of the amount.
8. Confirm bid-only status and the liquidity assumed in a stress.
9. Check issuer, quanto, currency and the key information document's risk indicator.
10. Note the fixing date and whether the product is a reissue.
11. Date every number and mark those not re-checked.
12. State what ends the product early or badly: barrier breach, issuer failure, illiquidity.

## 11.8 Contested points (position)
- **Whether the coupon is a fair price for the protection sold.** Several academic studies of retail structured products report sizeable issuer margins embedded in the price (general knowledge; re-check the sources). Proponents argue the coupon compensates a risk the investor would otherwise not accept. This model treats the margin as a cost to be measured, not as a verdict.
- **Whether the minimum buffer is the right metric.** Some practitioners weight the names by volatility. Here the minimum is the decision variable, because the payoff depends on the minimum.
- **Hold or sell before maturity.** This depends on the path and on liquidity. Not settled here.

## Common mistakes
- Comparing products by their headline coupon alone.
- Reading a dated price or buffer as current.
- Treating the price drop at coupon detachment as a loss of value.
- Forgetting that every extra name in a worst-of basket is another way to lose a coupon.
- Treating an autocall as a return of capital with no reinvestment risk.
- Mixing the maturity grid with the exit grid.

## Links
- ch10 (10.5 barrier income mechanics; 10.8 issuer and liquidity), ch06 (loss budget and sizing), ch08 (claimed results and their tests); `investing-and-financial-history` ch07 (structured certificates); `personal-finance-italy` for tax treatment.
