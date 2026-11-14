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

## Common mistakes
- Believing a yield from selling options is "extra".
- Ignoring that selling options without cover has unlimited loss.
- Treating delta as a certain probability.

## Links
- ch05 valuation, ch09 crises, ch11 decisions.
