# Chapter 06: Notes, Funds and Other Wrappers vs Holding the Asset

> Educational concepts, not investment, tax or legal advice. Regulatory and tax statements are snapshots (Europe/Italy, 2023-2025) to be re-checked.

## Core Idea
In this model, a **wrapper** replaces the operational risk of holding a key with the legal and credit risk of holding a security. The choice is not "safe vs unsafe" but **which failure modes you prefer**: lost keys and fake software, or issuer insolvency, tracking error and cost. This chapter compares the three structures: the physical asset, an exchange-traded note (ETN), and a fund or exchange-traded commodity-style product (ETP).

## 6.1 Definitions
- **Thesis**: a note is a debt claim on an issuer promising to track an asset; a fund owns the asset.
- **Mechanism**: an **ETN** is an unsecured debt security; its payoff depends on the issuer paying. An **ETP** is a general label covering notes and certain asset-backed products. A **fund** (collective investment scheme) holds the underlying assets in segregated custody in the fund's name.
- **Trade-off**: segregation protects against issuer insolvency; debt-style wrappers do not unless collateral is posted.
- **Does not hold when**: a note is fully collateralised with assets held by an independent custodian in a ring-fenced account (then it behaves like a hybrid).

## 6.2 Where each risk sits
| Risk | Self-held asset | Note (ETN) | Asset-backed product | Fund |
|---|---|---|---|---|
| Lost or stolen keys | Yes | No | Indirect (custodian) | Indirect (custodian) |
| Issuer insolvency | No | Yes | Partly (depends on collateral) | Low (segregation) |
| Custodian failure | Only if custodial | Underlying custodian | Yes | Yes |
| Tracking deviation | None | Possible | Possible | Possible |
| Annual cost | Network fees only | Up to about 2% a year | Up to about 2% a year | Fund fee |
| On-chain use, staking | Yes | No | No | No |
| Succession | Hard (ch03) | Standard securities succession | Standard | Standard |

## 6.3 Layering
- **Thesis**: each added layer is another place to fail.
- **Mechanism**: a note that holds bonds of a vehicle that holds the asset at a venue multiplies failure points: the issuer, the vehicle, the venue. A simple note on an asset held by a regulated custodian has fewer. Read the prospectus to identify the legal claim and the custody chain.
- **Does not hold when**: the structure is flat and independently audited.

## 6.4 Tracking and the price-to-NAV gap
- **Thesis**: a note's market price can deviate from the value of the asset it tracks.
- **Mechanism**: creation and redemption by authorised participants keep an exchange-traded fund close to its **net asset value** (NAV). In a note with a looser creation-redemption mechanism, the market price can drift away from the underlying, especially in stress or when the market in the underlying is closed.
- **Trade-off**: access through a securities account at a cost versus a possible persistent premium or discount.
- **Does not hold when**: liquidity is deep and the issuer keeps an active market.

## 6.5 Annual cost compounding
A product costing 2% a year compounds over time: over 10 years it removes roughly 18% of the ending value relative to a zero-cost holding (1 - 0.98^10), before any tracking error. For a volatile asset with a long horizon the self-held option avoids this, while adding operational cost in time and risk. Compare with a one-off purchase fee and network fees.

## 6.6 Regulatory classification (Europe, snapshot 2023-2025)
- A single-asset fund on a crypto-asset cannot, as a harmonised retail fund, be marketed to European retail investors (position under the harmonised-fund framework as applied at the time); notes and commodity-style products are the retail route.
- A **key information document** in the investor's language is required for retail packaged products.
- Rules for crypto-asset service providers and issuers were being phased in during this period; verify the current regime.

## 6.7 Tax treatment of wrappers vs the asset (Italy, snapshot 2023-2025)
- Notes and commodity products generate **miscellaneous income** (*redditi diversi*): gains and losses can offset each other.
- Funds generate **capital income** (*redditi di capitale*): gains cannot be offset by losses.
- A wrapped product held in administered custody needs **no declaration lines**, since the domestic intermediary acts as withholding agent; a direct holding of the asset needs the reporting duties of ch09.
- A wrapped exchange-traded product is **not a crypto-asset** for tax purposes.
- Details and other regimes: see `personal-finance-italy`.

## 6.8 Choosing by the use case (comparison, not advice)
| Use | Wrapper tends to fit | Direct holding tends to fit |
|---|---|---|
| Exposure within an existing brokerage account | Yes | No |
| Simple succession and tax filing | Yes | No |
| Spending, on-chain use, staking, DeFi | No | Yes |
| Concern about issuer or custodian | No | Yes |
| Concern about losing keys | Yes | No |

## 6.9 Common structural questions to ask
- Who is the issuer and what is its credit quality?
- Is the asset held, in whose name, with what segregation?
- What happens to the product if the custodian fails?
- Is there a fee on the product plus a spread on the exchange?
- Are there forced events, such as redemption at the issuer's option?

## Common mistakes
- Believing that "regulated" means "cannot fail".
- Comparing a wrapper's fee to nothing instead of to the real cost of secure self-custody.
- Ignoring the difference between a note and a fund when taxes are computed.

## Links
- ch03 custody trade-offs; ch05 counterparty cases; ch09 tax concepts. See also `investing-and-financial-history` for general ETF costs and `personal-finance-italy` for Italian ETF taxation.
