# Chapter 05: Exchanges, Lending and Counterparty Failures

> Educational concepts, not investment, tax or legal advice. Case cards describe publicly reported events neutrally and without naming firms.

## Core Idea
In this model, the main risk for a holder who leaves assets with a third party is **counterparty failure**, not price. A blockchain transfer is irreversible (ch01), so an account at a venue is an unsecured claim on a company, and when the company fails the claim is paid in a bankruptcy process. Across the cases below the failures share structure: opaque books, mismatched liabilities and assets, related-party exposure, and promises of yield that nobody could explain.

## 5.1 What a deposit at a venue is
- **Thesis**: a balance shown on screen is a database entry, not a coin on a chain you control.
- **Mechanism**: the venue holds keys, pools customer assets in its own wallets, and records each customer's claim internally. Unless the venue segregates assets and proves reserves, customer assets can be lent, pledged or used in proprietary activity. After failure, customers rank as unsecured creditors in the insolvency process; recoveries and timing are decided by the administrator and the court.
- **Trade-off**: convenient trading, recovery by identity and simple tax records versus exposure to the venue's solvency.
- **Does not hold when**: the venue is regulated with segregation rules and audited reserves; this reduces but does not eliminate the risk. Deposit guarantee schemes for bank accounts generally do not cover crypto-assets (position: check the jurisdiction).

## 5.2 Case card A: exchange failure through related-party lending
- **Event type**: a large trading venue failed in 2022 after customer assets were reportedly used to support a related trading firm.
- **Proposed causes**: commingled customer and proprietary assets; collateral valued in the venue's own token; weak or absent controls and board oversight; concentration of related-party exposure.
- **What it shows**: proof of reserves needs liabilities too; a token issued by the same group is poor collateral because its value falls when the group is in trouble.
- **Rival reading**: some argue a stronger regulatory perimeter would have prevented it; others argue the same behaviours existed in traditional finance, and the novel element was the speed.

## 5.3 Case card B: intermediated-yield platform failure
- **Event type**: a lender offering about 8 to 10% on deposits halted withdrawals in 2022.
- **Mechanism**: deposits were pooled and deployed in lending protocols, liquidity pools and exchanges, with liabilities denominated in the very assets invested. Exposure to a collapsed algorithmic stablecoin (ch07) crystallised losses; the group had creditor classes split across related entities, and a high headcount cost.
- **Outcome range**: recoveries in these proceedings were reported at roughly a quarter of liabilities in one case (uncertain figures); administrator costs are paid by creditors.
- **What it shows**: a rate above what the safe asset pays must come from risk; the client bears the strategy's risk plus the intermediary's, and receives only a fraction of the yield.

## 5.4 Case card C: mining-lender and broker cascade
- **Event type**: several lenders and brokers failed within weeks in the same year.
- **Mechanism**: correlated collateral, cross-lending among the same firms, and withdrawal runs. A run on a venue with illiquid assets is the same maturity-mismatch dynamic as a bank run (see `investing-and-financial-history` ch09).
- **What it shows**: contagion travels through shared counterparties, not through the technology.

## 5.5 Structural warning signs
| Sign | Why it matters |
|---|---|
| Yield well above the risk-free rate with no explanation | The return is a risk premium or a transfer |
| No segregation of customer assets | Assets can be used by the operator |
| Reserves shown without liabilities | Solvency is unverified |
| Group token used as collateral | Circular risk |
| Withdrawal "pauses" or "temporary" limits | Liquidity is already impaired |
| Complex entity structure across jurisdictions | Recovery and legal claims are slow |
| Aggressive promotion and referral rewards | Growth depends on new deposits |
| Opaque books and no audited statements | Nothing can be verified |

## 5.6 The anatomy of a run
A run starts with a rumour; withdrawals rise; assets that are not liquid must be sold or are already lent out; the venue halts withdrawals; trust vanishes and the remaining customers become creditors. Speed is higher than for a bank because transfers settle quickly and operate at any hour.

## 5.7 Reading a venue's claims
- **Proof of reserves**: shows some assets; it does not show debts. A balanced proof needs reserves and liabilities, audited by a third party.
- **Audits**: a point-in-time attestation differs from a full audit; check scope and date.
- **Regulatory registration**: registration with a supervisory body means compliance obligations, not that the venue cannot fail.

## 5.8 Practical risk reduction (concepts)
Diversify across custodians if custodial; keep only what you trade on the venue; use withdrawal whitelists with delay (ch03); hold long-term assets in self-custody, accepting the operational risk it brings; prefer venues with segregation and audited statements; treat promotional yield as a risk indicator. These are mechanisms to compare, not instructions.

## 5.9 Trade-offs
Lower operational burden versus counterparty exposure; yield versus transparency; speed versus controls.

## Common mistakes
- Treating an on-screen balance as ownership.
- Comparing a headline rate across products without asking where it comes from.
- Concentrating on one venue because of a promotion.

## Links
- ch03 custody; ch06 notes; ch07 stablecoin and yield mechanics; ch10 impersonation. See also `investing-and-financial-history` ch09 and ch10.
