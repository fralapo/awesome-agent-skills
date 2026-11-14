# Chapter 02: Government Bonds

> Educational concepts, not investment, tax or legal advice. Figures are snapshots (Italy, 2023-2026, year stated), to be re-checked against the rule in force.

## Core Idea
In this model, an Italian government bond ("titolo di Stato") is a promise with **dated, known cash flows**, so its return is an internal rate of return (IRR) on net, dated flows, and its risks are price risk (if sold early), inflation timing, and concentration on one sovereign. The 12.5% tax rate is a real advantage but not a reason to ignore yield, liquidity or structure.

## 2.1 The families
| Instrument | Core feature (concept) |
|---|---|
| "BOT" | short discount bill, no coupon; tax is paid upfront at issue and recovered from the buyer by a seller |
| "CTZ" | zero-coupon, medium term; the return is the difference to redemption |
| "BTP" | fixed coupon, medium-long term; the bulk of the market |
| Inflation-linked BTP / retail inflation-linked issue | coupon or principal linked to inflation (see 2.5) |
| "CCT" | floating coupon; stays near par |
| Retail step-up issue | retail issue with step-up coupons and a loyalty bonus (see 2.6); a variant adds an early-redemption option |

Retail issues are placed at a fixed price during the offer; the Treasury pays the placing bank, so the buyer pays no purchase commission. Coupons are set as **minimums** and can be raised by the issuer, never lowered.

## 2.2 Price, yield and the IRR
- **Thesis**: price and yield are two views of the same quantity and move in opposite directions.
- **Mechanism**: coupon equal to market yield gives par (100). Yield above coupon gives a price below 100, recovered as the bond is pulled to par. Quick estimate: price is roughly 100 minus (yield minus coupon) times years left; coupon 2%, yield 3%, 5 years: estimate 95, exact 95.42 (95.39 with semi-annual coupons). The correct return is the IRR of dated net flows; the simple average of coupons is wrong whenever timing differs (step-up 2/2.5/3/3.5/4 yields about 2.97%, not 3%). The shortcut coupon + (100 - price)/years is accurate only for short maturities and low rates (price 73, 10 years: about 5.7% versus 6.8% exact).
- **Trade-off**: IRR assumes reinvestment at the IRR; a modified IRR with an explicit reinvestment rate is more conservative.
- **Does not hold when**: flows are uncertain (floating, linked, callable); IRR is then a scenario output.
- **Worked example**: a "4.60% per year" bond with one coupon at the end of 13 years pays 59.8% in total; IRR is about 3.67%, not 4.60%.

## 2.3 Clean price, accrued interest and the real price you pay
- **Thesis**: quoted prices exclude accrued interest, so cash paid is clean price plus accrued coupon; buying just before a coupon gains nothing.
- **Mechanism**: accrued = coupon x days since last coupon / days in the period. No price drop occurs on coupon day because accrual is handled separately. In the Italian regime the buyer recovers the tax withheld on the accrued part. Platforms differ in showing clean, dirty, gross or net prices; reconstruct the dirty price from total cash divided by quantity.
- **Worked example**: 2% annual coupon, 311 days accrued: about 1.70 per 100, about 1.5 after the 12.5% tax credit.
- **Does not hold when**: inflation-linked bonds, where part of accrued interest is estimated (see 2.5).

## 2.4 Last, bid and ask; retail platform versus market
- **Thesis**: you buy at ask and sell at bid; "last" is only the latest trade and may be days old.
- **Mechanism**: ask exceeds bid. Use ask for yield. On thin bonds the spread can be large: bid 93.96, ask 94.71, three years: yield 3.33% at bid versus 3.03% at ask. A market order matches the best opposite price; a limit order waits in a queue behind earlier orders at the same price (a sell of 1,000 at 100.02 behind 2.3 million nominal executes only after them). Liquidity screens: a price change every day, small spread, adequate volume. Annualised yields on bonds a few days from maturity are headline noise: only the money gained after costs matters (a 12-day bond showing 4.06% annualised gains about 0.04-0.12 per 100).
- **Retail-only structures**: bonds sold only to retail buyers can trade below the yield curve (0.8 to 1.93 points below theoretical in one sample) for reasons not fully confirmed: low liquidity, flagged complexity, collective action clauses, fear of selective treatment of retail holders. For a holder to maturity the pick-up is real; a seller sees the lower price.
- **Does not hold when**: institutions start participating, which closes the gap.

## 2.5 Inflation-linked bonds
- **Thesis**: two designs differ in **when** inflation compensation arrives, and both lag.
- **Mechanism**: *Cash design*: a half-year coupon equals real rate/2 plus a revaluation payment equal to nominal x period inflation; the nominal stays at 100. *Accrual design*: the nominal grows with inflation and is paid at maturity. The index lags by about two to three months and the last published value is used. Negative inflation is floored for the coupon; in the old scheme later rises are paid net of the earlier drop, in the newer scheme not. Accrued interest includes already-booked revaluation; the tax credit applies only to the known base part, so pre-paid indexation can be unrecoverable if inflation turns negative.
- **Break-even**: the linked bond beats an equal fixed bond only if realised inflation exceeds the break-even embedded in prices (about 0.65-0.7% Italy, snapshot 2024). Real rate 1.85%: gross about 2.97% at 1% inflation, 3.96% at 2%, versus about 3.06% on an equal fixed bond.
- **Trade-off**: real protection versus price risk if sold early, lag and a bonus lost on sale.
- **Does not hold when**: bought at par on a coupon date, where the accrued-interest effects vanish.

## 2.6 Step-up coupons, loyalty bonus and investor put
- **Thesis**: rising coupons and end-of-life bonuses look generous but are priced close to the market.
- **Mechanism**: compare with a fixed bond of equal maturity on IRR: step-up 3.25% for 3 years then 4% for 3 years plus a 0.70% bonus gives about 3.75% with bonus, 3.64% without. A bonus of 0.5-1% over several years is worth only about 0.1-0.15% a year. The bonus and any investor **put** (right to redeem at par after a set period) exist only under the placement identifier ("ISIN") for those who bought at issue and hold; selling or buying later removes them. A put is worth exercising only if the same bond without it trades below 100; its market value is a few hundredths of a point of yield, but it works as insurance (downgrade, speculative attack).
- **Does not hold when**: the bond trades far from 100 after issue; then use yield to maturity.

## 2.7 Duration and maturity choice
- **Thesis**: price change is roughly minus modified duration times the yield change; long bonds are bets on rates unless held to maturity.
- **Mechanism**: modified duration 5, yields +1 point: about -5%. Prices converge to 100 at maturity, so near-maturity bonds barely move. Extending from 10 to 20 years on a flat curve adds a few tenths of a point, not "three points". For a spending need with a fixed date and amount, a single bond (or a ladder with maturities at 2, 4, 6 years) gives a certain outcome; a constant-duration bond fund or ETF gives the same expected return with a wider distribution (see ch04).
- **Does not hold when**: the holder can and will keep the bond to maturity and the issuer pays.

## 2.8 Taxation: 12.5% versus 26%, stamp duty, net yield
- **Thesis**: net yield depends on tax rate, stamp duty and reinvestment.
- **Mechanism**: government bonds 12.5%, corporate/bank bonds and deposits 26% (Italy, snapshot 2025). Securities stamp duty is 0.2% of year-end market value (a bond below 100 pays less; a purchase just before year-end pays a full year). Gains from price movement are "miscellaneous income" and can be offset by past losses; coupons are capital income and cannot. Losses on government-bond-type income are carried scaled by 12.5/26 (see ch05).
- **Worked example**: gross 3.06%, net of 12.5% tax 2.68%, about 2.47% after duty (Italy, snapshot 2026); on 10,000 nominal: gross 1,840, net 1,610, about 1,490 after duty. Equivalent-yield rule: a corporate 4.29% gross is 3.17% net, equal to a 3.62% gross government bond.
- **Does not hold when**: the holder sells early and the price differs from 100.

## Common mistakes
- Using "last" instead of ask; quoting annualised yield on days-to-maturity bonds.
- Ranking by yield: a very high yield is compensation for a risk (see ch03).
- Assuming a loyalty bonus survives a purchase in the secondary market.

## Links
- ch03 corporate bonds; ch04 bond ETFs and tax; ch05 losses; ch09 inheritance of bonds; ch12 verification.
