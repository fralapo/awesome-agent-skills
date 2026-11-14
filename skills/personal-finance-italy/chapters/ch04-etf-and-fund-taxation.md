# Chapter 04: ETF and Fund Taxation

> Educational concepts, not investment, tax or legal advice. Figures are snapshots (Italy, 2023-2025, year stated), to be re-checked against the rule in force.

## Core Idea
In this model, an exchange-traded fund is taxed less by its strategy than by its **legal wrapper and the category of income it produces**. In Italy the same flat 26% hides two legal categories: "redditi di capitale" (capital income: dividends, coupons, deposit interest, gains on harmonised funds and ETFs) that can never be offset by losses, and "redditi diversi" (miscellaneous income: gains on single stocks, certificates, options, commodity and crypto exchange-traded notes) that can. Almost every tax-aware behaviour follows from this asymmetry.

## 4.1 Capital income versus miscellaneous income
- **Thesis**: the asymmetry between the two categories is incoherent but decisive.
- **Mechanism**: a gain on a harmonised ("UCITS") fund is capital income, taxed gross; a **loss** on the same fund is an ordinary miscellaneous loss. The rule was built so accumulating funds could not use losses against dividends. The consequence: losses on a fund help against stock gains, gains on a fund cannot be sheltered by anything.
- **Trade-off**: simplicity for the authority versus an incoherent outcome for the taxpayer.
- **Does not hold when**: a reform unifies the categories (a 2023 enabling law proposed one financial-income basket with full netting; implementation unconfirmed), or the instrument is a **non-harmonised** (non-UCITS) fund, whose income is treated as capital income at ordinary progressive rates, declared in the personal tax return and generally less favourable than the 26% flat rate (verify for the tax year).

## 4.2 Regimes: administered, managed, declarative
- **Thesis**: the default is the administered regime; the declarative regime adds timing and netting flexibility at the cost of paperwork.
- **Mechanism**: in the administered regime ("risparmio amministrato") a domestic intermediary computes and withholds tax and keeps the loss ledger. In the managed regime ("risparmio gestito") tax is levied on the year-end result including unrealised gains (26% for portfolio management, 20% for pension funds). In the declarative regime ("dichiarativo") the investor computes everything; foreign brokers force it; gains and losses of the same year net regardless of order, and payment is one year later (see ch06).
- **Does not hold when**: physical gold is sold (it needs the declarative regime to use financial losses).

## 4.3 Taxation of bond funds: the "white-list" share
- **Thesis**: a fund's tax rate depends on stale composition data.
- **Mechanism**: the rate is the weighted average of 12.5% and 26% using the share of qualifying government bonds in the latest one or two half-yearly reports before the event; with no report it is 26%. Events in the first half of the year use December data, those in the second half June data. A government-only fund listed in spring was taxed at 26% because the reference report showed 0%.
- **Trade-off**: administrative simplicity versus temporary over-taxation of new or recomposed funds.
- **Does not hold when**: the fund has long-standing, up-to-date reports.
- **Tax on the governmental share of money-market type funds**: 12.5% on the governmental share and 26% on the rest, so effective rate depends on composition; fees do not reduce the taxable base and create hard-to-use losses.

## 4.4 Accumulation versus distribution
- **Thesis**: economically equivalent before tax; the difference is when tax is paid and how much flexibility you keep.
- **Mechanism**: a dividend is a sale of the asset: the price falls by about the dividend on the ex-date, so total return is unchanged before tax. Distributing: the dividend is taxed in full at 26% in the year received and the tax cannot be recovered if the position later closes at a loss. Accumulating: units are sold when cash is needed, taxing only (price - basis) x units sold, so effective tax on proceeds is rate x gain fraction; nothing is due if the position ends below basis. The advantage grows with time until the first sale.
- **Worked example**: 100,000 growing at 8% for 20 years becomes about 466,000; tax of 26% on the gain is about 95,000, about 6.8% net a year, against 5.9% if taxed every year. In a one-year-style case the difference was about 0.25% of capital; over 20 years about 0.36% a year.
- **Trade-off**: distribution gives income without selling and may steady behaviour; accumulation maximises compounding.
- **Does not hold when**: fixed commissions bite on small reinvestments, or foreign withholding is not recovered at fund level (single stocks pay foreign plus domestic tax on the gross dividend).

## 4.5 What an ETF contains and where tax meets structure
- **Thesis**: the label (country, theme, size) is not the content; read index, holdings, replication, domicile and liquidity.
- **Mechanism**: replication can be full physical, sampled or synthetic (swap, cheaper, counterparty risk). An exchange-traded note (ETN) is a contract with the issuer tied to an index; an ETF delivers the return of what it holds. Commodity and metal products and crypto notes need not be UCITS and are taxed through the intermediary as miscellaneous income (Italy, snapshot 2023). A tax resident buying a **non-UCITS** ETF faces capital-income treatment at ordinary progressive rates that must be declared and is generally less favourable (verify for the tax year); "professional client" status removes consumer protection and is no fix.
- **Does not hold when**: the position is a small satellite on a diversified core.

## 4.6 Costs: TER, tracking error, hidden costs
- **Thesis**: the expense ratio estimates explicit cost; it is not the whole cost.
- **Mechanism**: ongoing charges are estimated from past costs. Tracking error sources are uninvested cash, underweights that rally, index rebalances. Snapshot 2023: average effective cost near or better than stated, with a wide spread (standard deviation about 1%, monthly outliers -3% to +6%). Transaction costs inside the fund are reported apart (about 0 to 0.3%, bond funds near zero). Add broker commission and half the spread: spread % = (ask - bid)/mid.
- **Worked example**: a fund with 7-12 holdings charging 1.3-1.4% costs four to six times a large-market fund at 0.10-0.30%.
- **Trade-off**: a cheaper fund versus noise in a single year; for a lump sum, size and liquidity can matter more than a few basis points.

## 4.7 Currency hedging has a hidden cost
Hedged share classes protect from currency swings, but the realised cost is far above the visible expense gap: ticker-level gap up to about 0.16%, median realised cost 1-2% a year (data to 2024), hedged dollar bond funds costing nearly 2% and cancelling their higher yield. Currencies are a zero-sum pair; neither version is better a priori.

## 4.8 Bond ETFs: tax and structure effects
- **Thesis**: for a dated liability, a constant-duration bond ETF is not a single bond.
- **Mechanism**: a fund keeps duration roughly constant by selling shortening bonds, converting virtual losses into realised ones; after +2 points in yields a single-bond ladder and an ETF both lose about 4.84%, but at 6 years the ETF returns 3.19% a year versus 3.24% for held singles. A **target-maturity** fund holds bonds expiring around one date and dissolves; near the end it behaves like a single bond but its payoff is estimated (weighted average discount from 100; redemption approximately price x 100/(100 - average discount)). Corporate holdings raise tax to 26% versus 12.5%.
- **Does not hold when**: holding for at least 1-2x the fund's duration (the expected return is nearly locked, but a sharp rise before selling can still produce a loss).

## 4.9 Rebalancing, sale order and average cost
- **Thesis**: sales trigger tax, so rebalance with cash flows.
- **Mechanism**: direct new contributions to underweights; sell only for overweight or cash need. For cash, the position with gain **closest to zero** minimises tax drag in simulations; recycling losses to shield a big sale loses to fees. In the declarative regime, shares, bonds and ETC/ETN use LIFO, while funds and harmonised ETFs use weighted average cost; in the administered regime the intermediary applies average cost (see ch06; verify for the tax year). Buying at a high price to raise average cost brings tax forward rather than avoiding it and can raise euro tax.
- **Does not hold when**: assets trend strongly or fees are large.

## 4.10 Tax at death for funds versus stocks
Death is not a realisation event for funds and ETFs (capital income): no income tax is due at death, the heir inherits the original cost basis with no step-up and pays 26% on the whole gain when selling (verify for the tax year). For instruments producing miscellaneous income (shares, ETC/ETN, ordinary bonds) the basis is generally the value declared for succession tax (verify). A loss lapses in both cases. Succession tax (with its allowances) is a separate levy from income tax. Government bonds are outside the succession-tax base (see ch09).

## 4.11 Contrast: deemed-return taxation abroad
- **Thesis**: taxing a presumed return transfers the burden to low-volatility holders and rewards risky ones.
- **Mechanism (Netherlands, snapshot 2026)**: wealth is split into cash, investments and debts with presumed returns (1.28%, 6%, 2.7%) taxed at 36%, with a disproof option when the actual return is lower. A bond yielding 3% is taxed as if it earned 6%, a levy of about 2.2% of capital, roughly 72% of the real return. A proposed regime from 2028 taxes realised and unrealised gains at 36% with a small allowance. (Belgium, snapshot 2026) previously no tax on private gains; a new 10% on gains above an annual allowance with carry-forward of unused allowance.
- **Trade-off**: presumed returns are simple to administer but unfair in low-return years; mark-to-market taxation taxes gains without liquidity.
- **Does not hold when**: the disproof option is available and the investor records losses. Italy's realisation-based model is the opposite design.

## Common mistakes
- Assuming a loss on an ETF can shelter a gain on another ETF (it cannot).
- Judging an ETF by its name or its TER alone.
- Buying a non-UCITS product without checking the tax category.

## Links
- ch02, ch03 bonds; ch05 losses; ch06 foreign brokers; ch09 inheritance; `investing-and-financial-history` ch04 (allocation).
