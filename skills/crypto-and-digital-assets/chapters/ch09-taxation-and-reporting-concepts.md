# Chapter 09: Taxation and Reporting Concepts

> Educational concepts, not investment, tax or legal advice. Italian figures are snapshots (2023-2025, with 2026 scheduled changes); rules change often. Always check the current law and official guidance, and use a qualified professional. Detailed Italian filing mechanics: see `personal-finance-italy`.

## Core Idea
In this model, tax follows **events, not balances**: a taxable event is a disposal (sale, swap across categories, spending, payment of a fee in the asset) or receipt of income (staking, interest, airdrop, referral bonus). Everything else (buying, holding, moving between your own wallets) is generally not a taxable event, though it may trigger reporting duties. The burden grows with the number of lots, categories and holding days, so record-keeping is the first control.

## 9.1 General concepts
| Concept | Meaning |
|---|---|
| Taxable event | Disposal or receipt of income |
| Cost basis | What you paid, plus allowable costs, per lot |
| Lot matching | Which units are sold first: FIFO, LIFO, average cost (rule set by the jurisdiction) |
| Holding period | Duration; may change the rate or exempt a gain |
| Realised vs unrealised | Tax usually arises only on realisation |
| Income vs gain | Receipts taxed on value at receipt vs disposals taxed on profit |
| Loss offset | Which gains a loss may offset, and for how long |
| Monitoring vs tax | Some systems require declaring holdings independently of gains |
| Residency | Decides which country taxes worldwide income |

Records to keep: date, quantity, price in local currency, counterparty or venue, fees, wallet addresses, transaction identifiers, and the reason for each movement.

## 9.2 Classification (Italy, snapshot 2023-2025)
- **Thesis**: tax treatment depends on whether an asset is a crypto-asset, a financial instrument or neither.
- **Mechanism**: crypto-assets are digital representations of value or rights on a distributed ledger, including collectibles. Futures, options, contracts for difference, leverage and shorts are **financial instruments** with their own rules; wrapped exchange-traded products are not crypto-assets (ch06). A practical test: if the intermediary allows withdrawal on-chain, it is a crypto-asset; otherwise it is likely a derivative. Contracts for difference on crypto are traditional financial instruments.
- **Trade-off**: clear categories versus ambiguity (the law does not define a stablecoin).
- **Does not hold when**: official guidance changes.

## 9.3 The "three buckets" for swaps (Italy, snapshot 2026)
Exchanges between assets "with equal characteristics" are irrelevant for the gain computation: roughly three buckets: (1) volatile coins, (2) stablecoins backed by real or financial assets, (3) collectibles. A swap **across** buckets is a disposal. A swap inside a bucket still matters for the monitoring regime. Fees paid in the asset are disposals; cost basis passes through irrelevant swaps. Interpretations differ on edge cases, so keep the reasoning documented.

## 9.4 Income from staking, interest and promotions (Italy, snapshot 2026)
- Interest, staking rewards and airdrops are taxed as income at market value on receipt, with **zero cost basis** thereafter; the later sale then realises the entire proceeds as gain.
- Cashback is generally a refund and not income (position, to verify).
- Sign-up and referral bonuses are miscellaneous income.
- Worked example: a referral bonus of 10 taxed at a marginal rate of 43% leaves about 5.7.

## 9.5 Two separate duties in Italy (snapshot 2023-2025)
- **Monitoring plus a value-based levy.** Initial value (market value on 1 January, or purchase price), final value (sale proceeds or market value on 31 December) and days held (difference + 1). Each trade splits a lot into rows; rows may be aggregated using sums and a weighted-average number of days. Value levy: **0.2% x final value x days/365**, nothing due under 12 euro. Worked example: a final value of 530,339 euro held for 217 days gives 530,339 x 0.002 x 217/365 = about 630 euro.
- **Substitute tax on gains.** Gross proceeds minus acquisition cost (fees not deductible; LIFO matching; no documents means zero cost); losses offset only gains from crypto-assets. For 2023-2024 net gains or losses below 2,000 euro in absolute value were neither declared nor taxed; from 2025 the threshold is removed. The rate is 26% through 2025, with 33% scheduled from 2026 (subject to change). Payment is due by 30 June, or 30 July with a 0.40% surcharge.
- **Declaration layout** changed in 2024 (verify for the tax year): monitoring and capital-income lines can sit in the employee return, with the supplementary return keeping the gains line, though some sections may still require the full personal return; debts for substitute taxes are not offset automatically against income-tax credits.
- **Exchanges** registered with the supervisory body report quarterly balances, conversions and transfers to the tax authority; self-custody wallets are outside this reporting, but retroactive requests are possible.
- **Does not hold when**: the taxpayer is not Italian-resident for the whole year.

## 9.6 The cost-basis step-up decision (Italy, snapshot 2025 only)
- **Thesis**: a step-up pays tax on the whole value to avoid tax on the future gain; it favours low cost bases and near-term sales.
- **Mechanism**: the option paid 18% of the 1 January 2025 value (not of the gain) by 30 November 2025, after which the new cost basis equals that value. Break-even for selling everything: (P - C) x r > P x 18%, where r is the substitute-tax rate on gains. At r = 26% (rate through 2025) this means P/C > 3.25; at r = 33% (scheduled from 2026, and sales fall in 2026 or later) it means P/C > about 2.2. With a price of 93,000 the cost basis must be below about 28,600 at 26%, or about 42,300 at 33%. With a basis of 50,000 and value 100,000 (P/C = 2), the step-up costs 18,000 against 13,000 of tax on sale at 26% or 16,500 at 33%. Beyond that, the decision depends on the cost basis, the share to be sold soon, and assumed growth: at 62% annual growth over three years, not stepping up was about 50,000 ahead; at 25% about even. The step-up is **per asset**, not partial, and may disallow later loss realisation. Holders with a high basis can instead sell and repurchase. Procedure: first simulate "sell everything now"; if the step-up fails there, it fails in every scenario.
- **Trade-off**: certain upfront tax versus uncertain future tax.
- **Does not hold when**: rates or rules change; it is not an amnesty for undeclared holdings.

## 9.7 Large sales: execution and logistics
- Read the **order book** depth on the bid side rather than the last price; the realistic price is the average across levels consumed; over-the-counter trades avoid moving the book.
- Resting orders ("maker") usually pay lower fees than orders that take liquidity ("taker").
- Warn the receiving bank about large transfers and keep tax documentation ready.
- Means-tested benefits: a principle in a budget law does not by itself change the list of assets in a regulation; an implementing act is needed, and a lower-ranking act cannot exceed the law.

## 9.8 Prediction markets (legal reading, position)
A contract that pays 1 if an event occurs trades at the crowd's implied probability, weighted by money staked: two outcomes priced to sum to about 1 (0.62 = 62%). Resolution depends on an oracle; if resolution is by token-holder vote, the outcome equals consensus, not necessarily truth. Legally, non-economic events resemble gambling and economic ones resemble derivatives (binary options are banned for retail in Italy). Tax reading (position, unsettled): resold before expiry it is a crypto-asset gain; held to expiry on a non-economic event it is a gambling win taxed on the gross amount at progressive rates without deducting the stake. Classification is unsettled.

## 9.9 Practical process (concepts)
1. Keep a ledger from day one, per lot.
2. Classify each movement: transfer, swap in bucket, swap across buckets, income, spend.
3. Compute gains by the required matching method.
4. Compute the value levy per asset.
5. Use software for many swaps; spreadsheets suffice for simple histories.
6. Fewer, larger operations reduce compliance cost.

## Common mistakes
- Deducting fees where the rule disallows it.
- Forgetting the monitoring duty when no sale occurred.
- Treating a self-custody wallet as invisible: it is declarable.
- Missing a lot, which sets the basis at zero.

## Links
- ch03 custody (affects records); ch06 wrapper tax; ch07 income from DeFi; `personal-finance-italy` for forms, deadlines and loss rules.
