# Chapter 11: Derivatives and On-Chain Descriptors, and Cycles as Hypotheses

> Educational descriptions of market data and metrics, not advice, signals or forecasts. Many metrics are estimates by commercial providers with different definitions and labels; the readings below are the common descriptions, and every reading needs its definition, source and lag stated.

## Core Idea
In this model, derivatives and on-chain data describe **positioning and holding behaviour**: who is leveraged, who holds, who is moving coins. They do not predict prices. A reading is informative only with its definition attached, and only after it has been tested on the market it is applied to. Cycle claims are hypotheses to be tested (8.1), not inputs to a decision.

## 11.1 Perpetual futures and funding
- **Thesis**: a perpetual contract has no expiry. A periodic payment between the two sides keeps its price near the spot price.
- **Mechanism**: at a fixed interval, one side pays the other. When the funding rate is positive, longs pay shorts, which means the contract trades above spot and leveraged longs dominate. The rate is computed from a premium term and an interest term, and differs by venue. A high positive rate sustained for many periods is a steady cost to longs, and a fall in price can force them out in a cascade (11.3).
- **Trade-off**: funding is a cheap, continuous read on crowding, but it lags, depends on the venue and can stay positive for the whole length of a trend.
- **Does not hold when**: rate caps, fee structures and settlement rules differ between venues, so an average across venues is a different metric from one venue's rate.

## 11.2 Open interest
- **Thesis**: open interest counts contracts not yet closed. It measures commitment, not turnover.
- **Mechanism**: open interest rising with price means new positions are being opened on the upside; rising with price falling means new shorts. Open interest falling during a move means positions are closing, through profit-taking or forced closes. Expressed in coin units or in currency, the same series can change because of price alone; the two measures must not be mixed.
- **Trade-off**: high open interest with the two sides balanced says less than one-sided build-up. Most venues show the total but not the split between longs and shorts.
- **Does not hold when**: contracts are coin-settled (inverse) and a currency-denominated series is used without adjustment.

## 11.3 Liquidation cascades and liquidation maps
- **Thesis**: a leveraged position closes automatically when collateral falls to its maintenance level. The forced sale adds to the move and can trigger further closes.
- **Mechanism**: a position opened at about ten times leverage has a maintenance level roughly 10% from its entry, less maintenance margin and fees, and the figure varies by venue. The liquidation engine sells at market into a book that may be thin. A cascade is a sequence of such closes. Liquidation maps are models: they assume a distribution of leverage and entry prices, estimated by the provider. The clusters they show are not observed positions.
- **Position**: that price moves toward dense liquidation clusters is a popular claim. In this model it is a hypothesis, to be tested with observed liquidation events and a control for volatility. Cascades are observed; their use as a predictor is not shown.
- **Trade-off**: observed liquidation totals describe a past event. Maps describe a possible one.
- **Does not hold when**: margin is cross-margined, so that losses in one position are absorbed by collateral held for others. With isolated margin, a position's loss is limited to its own collateral. Venues that socialise losses or deleverage winners by rule behave differently again.

## 11.4 Basis, skew and deleveraging
- **Basis**: futures price minus spot, annualised. A high positive basis indicates demand for leveraged exposure. A negative basis (backwardation) is rarer and indicates spot demand or stress.
- **Options skew**: implied volatility of puts against calls at equal distance from spot. A steep put skew indicates demand for downside protection (general knowledge; ch10 gives the Greeks in words).
- **Deleveraging**: a fall in open interest together with a fall in funding after a sell-off suggests leverage has been reduced. Some read this as the end of a downward move (position); no test is shown here.

## 11.5 On-chain descriptors
Each descriptor is an estimate built from the ledger plus labels. Labels are incomplete, and definitions differ between providers.
- **Supply in profit and loss**: the share of circulating supply whose last movement took place at a price below or above the current price. Each coin is valued at the price when it last moved. The figure depends on the chain's price history and on how many coins sit in reused addresses.
- **Realised price and bands**: realised price is the aggregate value of all coins at the price where each last moved, divided by supply; the total is the realised capitalisation. The ratio of market capitalisation to realised capitalisation compares market value with the aggregate cost basis. Some read high bands as distribution zones and low bands as value zones (position). Bands move with the cost base, so no fixed level is meaningful across years.
- **Realised profit and loss**: the sum, over coins moved, of the gain or loss between the price of the move and the price at which each coin last moved. Transfers between wallets owned by the same holder must be filtered out or they inflate the figure.
- **Holder cohorts**: long-term holders (coins unmoved for a long period, with cut-offs that vary by provider) and short-term holders. Sales by long-term holders are read as distribution (position). The cut-off defines the result.
- **Exchange balances and stablecoin supply**: coins in addresses labelled as exchange, and the supply of dollar stablecoins. Both are read as proxies: exchange balances for available supply, stablecoin supply for purchasing power parked in crypto. Labels are incomplete, and a stablecoin can serve non-trading uses. Some read a rise as liquidity coming in; others read it as dry powder that may or may not be deployed. Neither reading has been tested here.

## 11.6 Flow data: funds, filings and off-book buying
- **Net flows into a spot fund** equal creations minus redemptions. Creation requires the authorised participant to deliver the asset or cash (ch06, 6.1-6.2). A single day is noisy; read cumulative flows over a stated window.
- **Institutional holdings filings** for US managers arrive quarterly, with a delay of weeks. They describe past positions, not current ones, and they cover only the reporting entities.
- **Over-the-counter (OTC) buying** happens away from the public order book. Price can react late, after large buyers have executed off-book, and the reaction is then uneven.

## 11.7 Dominance and rotation (position)
- **Dominance** is the largest asset's market capitalisation divided by the total crypto market capitalisation. A "rotation" claim says that capital moves from the largest asset to others when dominance falls, and that a dominance level marks the change. The levels named by commentators are conventions. Test the claim against the total market and against a control for overall risk appetite. The evidence is mixed and the relation is unstable.

## 11.8 Cycle logic as a hypothesis
- **Thesis**: prices repeat a multi-year pattern linked to a supply event, a calendar or a fixed interval.
- **Mechanism, stated as a hypothesis**: a testable cycle claim must specify the event, the lag from event to effect, the expected amplitude, the period, how a peak and a trough are defined, and what would falsify it. Without these, a match with a few past episodes is a story.
- **Testing**: fix the list of events before looking at prices; measure the lag across all episodes; compare the result with the same number of random dates (8.1); check whether the effect survives changes in the window or the asset's age; and note structural breaks, such as new custody and fund channels, that could end a periodicity.
- **Trade-off**: a cycle is a useful frame for planning and for setting a loss budget. It is weak as a timing rule, and a few episodes cannot separate a cycle from chance.
- **Does not hold when**: a single cycle is used to set a horizon or a price level, or when a cycle is invoked after the fact to explain a move.
- **Position**: some hold that a widely followed cycle becomes self-fulfilling through the attention it attracts. This cannot be excluded, and a few episodes cannot measure it.

## 11.9 Risk management for volatile assets
- **Loss budget first**: decide the most money to be lost in an asset before any price is considered, then size from it (trading ch06 gives the arithmetic).
- **Position cap**: a fixed share of total capital, set before entry and reviewed on a calendar. It is not set from the expected return.
- **Drawdown planning**: the largest assets have had drawdowns above 70% in past cycles (general knowledge). Plan the position so that a fall of that size is survivable. Recovery needs `1 / (1 - d) - 1`: 70% needs about 233%.
- **Leverage and collateral**: a loan secured on crypto needs a buffer between the current loan-to-value ratio and the liquidation threshold. A fall equal to that buffer forces sales (8.7).
- **Liquidity and custody**: the position must be sellable in stress, on a venue that is solvent and by a method that is tested (ch03, ch05). Custody is part of the risk, not an administrative detail.
- **Rebalancing rule**: written in advance. Averaging into a fall without a limit is how a position grows into the asset that goes to zero (8.6).
- **Hedging**: a short hedge on a volatile asset costs carry and can be liquidated in a rally (8.8).
- **Does not hold when**: the position is larger than the loss budget, or the venue risk and the custody risk are not tracked.

## Common mistakes
- Quoting a funding rate from one venue as if it described the market.
- Reading liquidation maps as observed positions.
- Mixing coin-denominated and currency-denominated open interest.
- Treating a single cycle, or a dominance threshold, as a rule.
- Setting a position from expected return rather than from a loss budget.

## Links
- ch02 (mining and issuance), ch03 (custody), ch05 (exchanges and counterparty failure), ch06 (flows and wrappers), ch07 (DeFi liquidation), ch08 (price drivers, statistics and risk); `trading-methods-and-technical-analysis` ch06 (sizing) and ch08 (validation); `scientific-thinking` for multiple testing and evidence quality.
