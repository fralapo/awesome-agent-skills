# Chapter 19: Illiquid, Private and Gated Products

> Educational concepts, not advice on any product, fund or manager. Structures and terms change; check the documents in force.

## Core Idea
In this model, the risk of a product that cannot be sold quickly is more than the risk of its assets. It adds the risk of **when the price is set**, **who sets it**, **how long an exit takes** and **what the exit costs**. A stable price line in such a product is often a feature of how it is valued, not evidence that the assets are stable.

## 19.1 Liquidity mismatch
- **Thesis**: a fund that promises frequent redemptions while holding assets that take a long time to sell has a mismatch that works in calm markets and breaks under stress.
- **Mechanism**: redemptions are paid from cash and from the most liquid holdings first. Those who stay hold a more illiquid residue. In a run, sales of the remaining assets come at a discount, and the price falls for those who stay. Early leavers therefore gain at the expense of later ones (general knowledge; the same logic as bank runs, chapter 06, and forced sales, chapter 09).
- **Trade-off**: liquidity buffers cost return. Redemption gates protect the remaining investors but can trap those who want to leave.
- **Does not hold when**: the redemption frequency matches the time the assets take to sell, for example through a long lock-up.

## 19.2 Net asset value, quoted price and the lag
- **Thesis**: net asset value (NAV) is an estimate for assets without a daily market price, and the quoted price of a listed vehicle can differ from it.
- **Mechanism**: a vehicle with illiquid holdings may have NAV struck monthly or quarterly. Between strikes the price is set by trading or by a formula. An investor who buys at the last NAV may buy into a loss that has already happened. An investor who sells at a discount to reported value is accepting the buyer's view of the mark. A daily price on a listed vehicle shows the trading price, not the value of the holdings, unless arbitrage links them, and arbitrage fails when the holdings cannot be traded.
- **Trade-off**: a daily price is informative when arbitrage works. When it does not, it is a trading price.
- **Does not hold when**: the holdings have a reliable and frequent market value.

## 19.3 Valuation by appraisal and smoothing
- **Thesis**: appraised values for real estate or private companies move less often and less sharply than traded prices. That lowers measured volatility and correlation without necessarily lowering risk.
- **Mechanism**: appraisals update with lags and rely on comparables, which spreads a price change over several periods. A series built this way shows low volatility and low correlation with listed markets. Adjusting for the lag (un-smoothing) or comparing with traded proxies typically shows higher risk (general knowledge; a well-known issue in appraisal-based indexes). Illustration only: if an appraised series moves 1–2% a quarter while a traded index of similar assets moves 5–8% in the same quarters, the appraised series is not necessarily less risky; the difference is in when the risk shows up.
- **Trade-off**: appraisals avoid daily noise and reduce the number of decisions forced on holders. They also hide the path of value.
- **Does not hold when**: the asset is traded frequently and its prices are transparent.

## 19.4 Gates, suspensions and side pockets
- **Thesis**: when redemptions exceed what can be paid, a vehicle has three tools, each moving the timing risk to someone else.
- **Mechanism**: a *gate* limits redemptions in a period. A *suspension* stops them. A *side pocket* moves hard-to-value holdings into a separate pool that is paid out later, if at all. A market closure can freeze the value of holdings: during 2022, funds holding a market that stopped trading had to write their exposure down to zero or near it (general knowledge, public event). A liquidation can pay out in cash at a set date or transfer illiquid holdings in kind to the investors who remain.
- **Trade-off**: gates prevent forced sales at the bottom; they shift timing risk onto the investor who wants to leave.
- **Does not hold when**: the terms are clearly disclosed, the investor's horizon matches the lock-up, and the holdings are liquid enough to meet redemptions.

## 19.5 Private markets and their fee structure
- **Thesis**: private equity and private credit funds usually charge a management fee on committed or invested capital, plus a share of profits above a hurdle. The fee layers and the timing of cash flows shape the net return.
- **Mechanism**: commitments are drawn over several years and returned as assets are sold. Early years often show negative reported value, sometimes called the J-curve (general knowledge), because fees are charged while assets are young and carried at marks. The management fee is paid regardless of results. The performance fee is paid after a hurdle, sometimes with a catch-up that gives the manager a larger share once the hurdle is passed. The net return to the investor is below the gross return, and the reported internal rate of return is based on marks until assets are sold (see 19.3).
- **Trade-off**: private assets may add diversification and an illiquidity premium (position). The premium has to cover the fees, the lock-up and the valuation risk.
- **Counter-view**: fees can be justified by active ownership and by selection in less efficient markets; the evidence on whether net returns beat listed alternatives is disputed (position).
- **Does not hold when**: the investor can hold through the whole term and the fee terms are favourable and fully disclosed.

## 19.6 Evergreen and retail-access vehicles (position)
- **Thesis**: vehicles offered to retail investors that hold private assets with periodic redemption windows expand access, and their liquidity promise rests on the fund's ability to meet redemptions in stress.
- **Mechanism**: the vehicle may hold private assets whose marks are smooth (19.3) and whose fees are layered (19.5). Its redemption windows can be limited, suspended or subject to gates (19.4).
- **Position**: some argue retail access broadens choice and diversification. Critics argue that marketing overstates liquidity and that fees and marks are hard for retail investors to assess. An illiquidity premium is claimed for private assets, but the evidence is contested because the marks are smooth.
- **Does not hold when**: the vehicle is institutional and the investor understands and accepts its terms.

## 19.7 Checklist for any illiquid or gated vehicle (educational)
1. How often can money be redeemed, and through which route: cash, a gate, or an in-kind transfer?
2. How long would the underlying take to sell in a stressed market?
3. How is NAV set, how often, and by whom? Is the price a market price or an estimate?
4. Which fees apply at each layer, and when is any performance fee paid?
5. What happens if redemptions are suspended or gated?
6. Which part of the reported return is realised and which is a mark?
7. What share of total wealth would this be, and does it match the date the money is needed (chapter 04, 4.14)?

## Common mistakes
- Treating a stable price line as a stable asset.
- Comparing appraised volatility with traded volatility without adjusting for the lag.
- Assuming a daily listing means the holdings can be sold daily.
- Counting a reported internal rate of return as cash received.
- Ignoring a lock-up when a spending date falls within it.

## Links
- Chapter 04 (liquidity buckets, concentration), chapter 06 (bank runs and mismatch), chapter 09 (runs and forced sales), chapter 11 (decisions under commitment), chapter 12 (return arithmetic, IRR), chapter 13 (smoothing in backtests), chapter 16 (NAV arbitrage in funds), chapter 17 (fee layers). For the dated rules of one country's products, see `personal-finance-italy`.
