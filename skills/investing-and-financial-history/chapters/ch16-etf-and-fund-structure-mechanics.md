# Chapter 16: ETF and Fund Structure Mechanics

> Educational concepts, not investment, tax or legal advice. Product rules and figures are dated snapshots; check the prospectus and the key information document in force.

## Core Idea
In this model, the return an investor keeps from an index fund is the index return minus everything that sits between the investor and the index: how the fund holds the index, how its price is set, what happens to securities it lends, where its assets are custodied and which rules the index provider applies. Two funds that track "the same index" can differ on each of these points. The expense ratio captures only one of them. Chapter 04 gives the cost stack; this chapter explains where each layer comes from.

## 16.1 Passive, systematic and active: a spectrum, not a binary
- **Thesis**: "passive" describes how a fund is built, not how an investor behaves. It is a useful archetype rather than a category with sharp edges (position).
- **Mechanism**: even a plain index fund depends on choices: the index provider's rulebook (inclusion, weighting, rebalancing dates), the fund's replication method and its handling of cash and dividends. Three rough positions on a spectrum: (1) replication of a published index with little discretion; (2) rule-based systematic strategies (factor, fundamental-weighted) with rules fixed in advance and no price-based judgement, but with methodology choices that can be revised; (3) discretionary active management, including "enhanced" index funds that make small deliberate deviations. The position of a fund on the spectrum follows its rules and its tracking, not its label.
- **Trade-off**: the spectrum helps compare cost and transparency; the labels mislead. A transparent rule-based fund can be more predictable than some active funds, while costing more than a plain index fund.
- **Does not hold when**: the question is simply the cost and tracking of one broad index fund.

## 16.2 Index providers and rulebooks
- **Thesis**: an index inherits its provider's decisions. They are published, but they can change.
- **Mechanism**: committees or staff decide inclusions, exclusions and exceptions. Exceptions to the normal entry rules for a very large new listing are read by some observers as a sign that discipline gives way to pressure (position). Country classification (developed versus emerging, and within each) differs between providers, so two funds named "World" can hold different countries. Free-float rules, liquidity screens and scheduled reviews create predictable trading dates that other participants can anticipate (general knowledge). Fundamentals-weighted indexes are backtested rule sets that can be revised ("version 2.0" effects); capitalisation-weighted indexes follow a simpler principle that has been used for longer (position on which is better).
- **Trade-off**: committee discretion can respond to real structural change; it also means the index is a choice, not a neutral measure of the market.
- **Does not hold when**: the fund follows an index whose rules rarely change and are fully mechanical.

## 16.3 Replication: full, sampled and synthetic
- **Thesis**: the replication method decides which risks the fund carries beyond the index.
- **Mechanism**: full physical replication holds every constituent in index weights. Sampled replication holds a subset chosen to approximate the index; it lowers trading and custody costs for very large or illiquid indexes but adds tracking noise (general knowledge). Synthetic replication holds a derivative, usually a total-return swap with a bank, backed by collateral. The fund receives the index return against a fee; the investor is then exposed to the swap counterparty and to the value and liquidity of the collateral. Withholding on dividends can also work differently from a physical fund (chapter 18).
- **Trade-off**: synthetic structures can track very closely and can avoid some withholding; they add counterparty and collateral risk. Sampling saves cost and adds variance.
- **Rival view**: counterparty risk is small in practice when collateral is high quality, segregated and the counterparty is strong and regulated. Critics say the structure is opaque and that the exposure grows in stress, when collateral is least liquid.
- **Does not hold when**: the investor can see and accept the collateral, the counterparty and the swap terms and the added complexity is worth the tracking gain.

## 16.4 Creation, redemption and the premium or discount
- **Thesis**: an exchange-traded fund's price is set in the market; arbitrage by authorised participants keeps it near net asset value (NAV) most of the time.
- **Mechanism**: authorised participants create units by delivering the basket (or cash) and redeem by the reverse. If the market price rises above NAV, arbitrage sells units and buys the basket, which pushes the price back. Premiums and discounts widen when the underlying market is closed or thinly traded (the fund then trades on expectations of the unseen prices), and during sharp moves. The measured gap is between the market price and an indicative NAV, which is itself an estimate when holdings are illiquid.
- **Trade-off**: the mechanism works well for liquid baskets. For thin markets the price may trade away from NAV, and the cost falls on whoever trades at that moment.
- **Does not hold when**: the underlying trades continuously and deeply, as large developed-market equity indexes do during normal hours.

## 16.5 Trading costs: spread, timing and order type
- **Thesis**: the cost of entering and leaving is paid per trade, not per year, and it depends on liquidity, timing and order type.
- **Mechanism**: half the bid-ask spread is paid on each purchase or sale (chapter 04, 4.12). Spreads widen at the open and close and in volatile sessions. A limit order caps the price and may not fill; a market order fills and may cross a wide spread. A fixed per-trade commission dominates small regular purchases. Liquidity of the fund's units is not the same as liquidity of the underlying holdings, and the number of market makers differs by fund. Arithmetic: a spread of half a percent or more can equal several years of a low expense ratio, so the spread matters most for small, infrequent-trading funds and for frequent small purchases.
- **Trade-off**: large liquid funds have tight spreads; niche funds can cost more to trade in a year than they charge in fees.
- **Does not hold when**: the holding period is long and trades are infrequent and small relative to the spread.

## 16.6 Securities lending and its revenue split
- **Thesis**: lending holdings can add income that offsets part of the cost, but it adds counterparty and collateral exposure, and the income is shared.
- **Mechanism**: the fund lends securities to borrowers (often for short selling) against collateral worth more than the loan, and earns a fee. The lending agent usually takes a share. The net income appears in tracking difference and can offset costs. The risk is that a borrower defaults while the collateral has lost value or cannot be sold at its mark.
- **Trade-off**: lending can reduce net cost in calm markets and raise risk in stress.
- **Does not hold when**: lending is disabled by policy, or the share is stated and the collateral rules are strict and checked.

## 16.7 Custody and the master–feeder structure
- **Thesis**: where and how assets are held determines what an investor can recover if an intermediary fails.
- **Mechanism**: omnibus custody pools many clients' assets in one account, so each client holds a share of the pool. Individual segregation holds each client's assets separately, which protects more at higher cost (position: cost against protection). In a master–feeder structure, a feeder fund invests a large share of its assets in a master fund (for many European funds the rules require a high minimum share; check the fund's rules), and costs can be layered. Whether the layered charges add up, and how, must be read in the documents.
- **Trade-off**: pooled holdings are cheaper and simpler; segregation reduces exposure to co-clients and to the intermediary.
- **Does not hold when**: the legal protection of assets in the relevant jurisdiction has been verified and is clear.

## 16.8 Tracking difference and tracking error
- **Thesis**: tracking difference (fund return minus index return over a period) is the realised cost, and it includes items the expense ratio does not show. Tracking error is a different quantity: the volatility of that difference.
- **Mechanism**: sources include the expense ratio, transaction costs inside the fund, cash drag from uninvested cash, dividend timing and withholding, sampling, index rebalancing costs and securities-lending income, which can be positive. Over short windows the noise dominates; over decades the costs dominate. Position: for two plain index funds on the same index, a difference of a few basis points rarely justifies a switch once the tax on realised gains is counted, because switching realises gains (chapter 18).
- **Trade-off**: long common windows, the same index and the same currency give the cleanest comparison; they also hide what changed in between.
- **Does not hold when**: the difference is smaller than the uncertainty of the estimate, which is the case for short windows.

## Common mistakes
- Reading the expense ratio as the whole cost.
- Assuming two funds on "the same index" hold the same securities or countries.
- Trading large amounts in a thin market at the open or close.
- Treating a synthetic or lending structure as identical to physical holdings.
- Judging a fund on tracking difference over a short window.

## Links
- Chapter 04 (cost stack, currency, factor funds), chapter 07 (synthetic exposure in products), chapter 10 (custody failures and warning signs), chapter 13 (measuring tracking over windows), chapter 18 (withholding and domicile), chapter 19 (illiquid vehicles and NAV). For the dated rules of one country's listed products, see `personal-finance-italy`.
