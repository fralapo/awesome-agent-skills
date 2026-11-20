# Chapter 12: Market Microstructure, Liquidity and Flows

> Educational concepts on how orders, dealers and index rules move prices. Not advice, not a trading method and not a forecast. Figures are illustrative arithmetic; market rules (settlement cycles, reporting, fees) are snapshots to re-check against the venue and the regulator.

## Core Idea
In this model, the price printed on a chart is the outcome of who wants to trade, how much they want to trade at once, who stands ready to take the other side, and what rules force buying or selling. A trader who ignores these layers reads the chart as if every order were free and every price were available in full size. Microstructure explains why a large order moves price, why liquidity disappears in stress, why some flows are predictable, and why the same instrument can have different prices on different venues. It does not give a direction.

## 12.1 Price impact and the square-root law
- **Thesis**: a large order moves the price against the trader, and the impact grows less than in proportion to size.
- **Mechanism**: empirical studies across many markets find that impact scales roughly with the square root of the order's size relative to typical daily volume, multiplied by the instrument's volatility (square-root law, general knowledge). Roughly, impact is about `c x volatility x sqrt(Q / V)`, where `Q` is the quantity traded and `V` the average daily volume. Illustration: a trade of 1% of daily volume and a trade of 4% of daily volume differ by a factor of 4 in size, but their impacts differ by a factor of 2 (square roots of 0.01 and 0.04 are 0.1 and 0.2).
- **Trade-off**: splitting an order reduces impact but adds timing risk, because the price can move away while the order is still being worked.
- **Does not hold when**: a single event (news, a margin call, a halt) moves the book faster than any order can be split, or when the book is so thin that the first fill sets the whole price.

## 12.2 Order splitting and persistent order flow
- **Thesis**: trades in the same direction tend to follow each other, because large orders are executed in pieces; yet prices move in a way close to a random walk, because part of each trade's impact is reversed.
- **Mechanism**: each trade leaves a permanent part of its impact and a temporary part that decays. The net effect is that buying pressure is persistent in the flow, while the price path stays hard to predict in direction (propagator models, general knowledge). A market can therefore show clear trade-by-trade autocorrelation with no reliable price direction at a useful horizon.
- **Trade-off**: flow persistence explains why a move can continue after the first trade, but it cannot tell whether the flow is an informed view or a mechanical execution. The same tape pattern comes from both.
- **Position**: whether the decay of impact reflects liquidity provision (dealers reverting) or information (the market learning the trade's reason) is contested. The rival view is that most decay comes from liquidity provision, which would make persistence a cost-of-execution effect rather than information.
- **Does not hold when**: the flow is executed by a single known participant with a fixed schedule; the persistence then reflects that schedule, not market-wide information.

## 12.3 Market makers: spread, inventory and adverse selection
- **Thesis**: the bid-ask spread is the price of immediacy. It compensates the dealer for carrying inventory and for trading against better-informed counterparties.
- **Mechanism**: a dealer buys at the bid and sells at the ask. A round trip at a flat price earns the spread on the quantity turned over, but only if the inventory is reversed. Inventory risk is the loss if the price moves against the held position before it is reversed. Adverse selection is the loss to traders who know more. A dealer therefore widens quotes when volatility rises or when order flow looks one-sided. Market makers also have quoting obligations, which relax in stress: spreads widen, quoted sizes shrink, and quotes can be withdrawn.
- **Trade-off**: tight spreads in calm markets look like abundant liquidity; the depth that disappears in stress is what matters for a stop or an exit. Liquidity is a state of the market that can change within minutes.
- **Does not hold when**: a venue has designated, well-capitalised makers with binding obligations in all conditions, which is rare in its strong form.

## 12.4 Order routing, execution quality and visible stops
- **Thesis**: where and how an order is routed is part of its cost, and the parties who see the order have information about it.
- **Mechanism**: in some markets brokers sell retail order flow to dealers, who then fill it; the execution price can differ from the public quote by a small amount, and the net effect on retail is difficult to measure (position: some find it small, others find it meaningful in aggregate). Stop orders sent to a dealer or visible to a venue can cluster around known levels; a concentration of stops near a level is a known target, though its frequency is hard to measure in public data. Spoofing (placing orders with no intent to execute, to move the book) is prohibited in most regulated markets (general knowledge).
- **Trade-off**: a limit order caps the execution price but may not fill; a market order fills but accepts whatever the book offers. Routing choices trade price against certainty and speed.
- **Does not hold when**: execution is at a regulated benchmark with best-execution reporting that shows small differences.

## 12.5 Settlement, short availability and the ETF creation mechanism
- **Thesis**: the trade date and the settlement date differ, and an exchange-traded fund's price stays near its net asset value only through creation and redemption by large intermediaries.
- **Mechanism**: settlement follows a cycle of a few business days (T+N; the cycle is a snapshot and has been shortening in many markets, re-check the current rule). Until settlement, delivery and reversal depend on the clearing system, which exists to limit reversibility and to run controls. A short sale needs a lender; if the share cannot be borrowed, the position cannot be opened or, in some cases, closed on demand. For a fund, an authorised participant creates new units when the fund trades above its net asset value and redeems units when it trades below; this arbitrage keeps the price close to the value while the underlying is liquid and the creation process works.
- **Trade-off**: creation and redemption make the fund cheap and liquid for holders, but the arbitrage depends on the underlying being tradable. In illiquid underlyings or in stress, the fund can trade at a wider premium or discount for longer.
- **Does not hold when**: the underlying market is closed (different hours, a holiday, a halt), so the arbitrage cannot run until it reopens.

## 12.6 Thin books, auctions and new listings
- **Thesis**: when the book is thin, the first trades set the price, and a market order can execute far from the expected value.
- **Mechanism**: an opening or listing price is often set by an auction that matches the orders accumulated in advance. If few shares are offered for sale to the public (small float) and retail demand is high, the price can gap upward and then fall as the float grows. A market order walks the book: each unit is filled at the next available price. A stop order that triggers in a thin book can fill far below its trigger.
- **Trade-off**: a limit order protects the price and risks no fill; the cost of protection is the chance of missing the move.
- **Does not hold when**: the listing has deep institutional interest and a large float; the opening volatility is then smaller and shorter.

## 12.7 Flows, index rules and forced buying
- **Thesis**: rules that govern index membership create predictable, large flows, and prices respond to flows as well as to information.
- **Mechanism**: index providers include or exclude securities through published rules (minimum size, free float, a seasoning period since listing, sometimes profitability) and, in some indices, by committee decisions. Funds that track the index must buy when a security enters and sell when it leaves. The timing is known in advance, so traders trade ahead of it, and the price response can be large and temporary. Cap-weighted indices allocate more passive money to the largest names, so index rules concentrate flows in the largest and most-owned companies.
- **Position**: the inelastic-market view holds that prices respond to flows more than to fundamentals, at least in the short run, so passive demand moves prices in a lasting way. The rival view is that arbitrageurs supply near-infinite elastic capital at fair value, so any flow effect is temporary.
- **Trade-off**: passive investing is cheap and broad, but its demand depends on index rules that the investor does not control, and rule changes can alter flows. A rule change that brings a security in early creates a precedent as well as a flow.
- **Does not hold when**: the index rule is not binding (a security is already held by the relevant funds) or the flow is small relative to daily volume.

## 12.8 Concentration of holdings relative to volume
- **Thesis**: a position that is large compared with daily volume cannot be sold quickly without moving the price, so its risk is partly a liquidity risk.
- **Mechanism**: days to liquidate = position / (average daily volume x share of volume you can trade without moving the price). Illustration: a position of 525 million with average volume of 150 million a day, traded at 20% of volume, needs 525 / (150 x 0.2) = 17.5 trading days, and a sale that fast still moves the price (illustrative numbers). Concentrated funds that hold such positions can see flows reverse, which forces sales into the same thin volume.
- **Trade-off**: a higher participation rate shortens the exit but raises impact (12.1); a lower rate lengthens the exposure to adverse moves.
- **Does not hold when**: the position is in a deep, liquid market where the participation rate needed is trivial.

## Common mistakes
- Treating a quoted price as a price available in full size.
- Assuming liquidity in normal markets is still there in stress.
- Reading order-flow persistence as proof of information.
- Ignoring settlement and short-availability constraints in a plan.
- Forgetting that a passive fund buys on a known calendar, which others also know.

## Links
- ch01 (volume and phases of supply and demand), ch05 (strategy families and their regimes), ch06 (sizing, stops and correlation in stress), ch08 (testing a rule with realistic costs and impact), ch10 (issuer market making and stress liquidity); `investing-and-financial-history` ch02 (market efficiency) and ch07 (ETFs and funds); `economics-finance` for market structure at the level of central banks and clearing.
