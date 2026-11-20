---
name: crypto-and-digital-assets
description: "Conceptual knowledge of crypto-assets, not advice and not forecasts: blockchain, UTXO and account models, Bitcoin issuance, halving, mining and security, wallets and custody (seed phrase, recovery testing, custodial versus self-custody), Lightning, exchange and lender failures as case cards, notes and funds versus holding the asset, digital money as claim versus bearer value, convenience spreads, DeFi (stablecoin pegs, automated market makers, liquidation, staking, impermanent loss), derivatives and on-chain descriptors with cycle claims as testable hypotheses, valuation without cash flows, token launches and memecoin control mechanics, risk for volatile assets, tax concepts (dated Italy snapshot), and scams with compounding checks. Use when the user asks how a crypto mechanism works, what a risk is, how to test a claim, how custody options compare, how a failure happened, or what a token launch or market metric measures. No recommendations, no price forecasts."
allowed-tools:
  - Read
  - Grep
argument-hint: [mechanism, risk, claim to test, case, token launch, or chapter number]
---

# Crypto-Assets and Digital Assets
**Chapters**: 13 | **Corpus**: a synthesis of theoretical material on crypto-assets and digital finance | **Generated**: 2026-11-14

## Role and Boundaries

This skill **explains how crypto-asset mechanisms work, where the risks sit, and how to test claims**: ledger and consensus design, issuance, custody and key management, digital money as claim or bearer value, off-chain payments, counterparty failures, wrappers, DeFi mechanics, token launch controls, statistical weakness of common price claims, tax and reporting logic, and fraud patterns. It gives mechanisms, worked arithmetic, case cards with proposed causes, and the strongest case on each side of contested claims.

| This skill decides | This skill hands off |
|---|---|
| Mechanism of a concept (UTXO, halving, channel, liquidation, impermanent loss, pool control) | Buying, selling, timing or sizing any asset; portfolio, tax or product advice |
| Which risk sits where (key, custodian, issuer, contract) | General investing theory, diversification, behavioural finance -> `investing-and-financial-history` |
| How strong a statistic is and what it can support | Statistical method in depth -> `scientific-thinking` |
| Warning signs of a scam, as prompts to verify | Legal, accounting or compliance work; proving fraud |
| Conceptual tax logic and an Italy snapshot | Italian forms, deadlines, loss rules in detail -> `personal-finance-italy` |
| Central banks, deposits and monetary policy (as context for digital money) | Macro forecasting -> `economics-finance` |

**Stay in lane.** Educational concepts only: no investment advice, no price forecasts, no "buy this". Figures are dated snapshots and context-bound; tax and regulatory statements carry a country and period (for example "Italy, snapshot 2023-2025") and must be re-checked against current law. Projects are described generically, not ranked or named as recommendations. Every chapter opens with an "educational, not advice" notice.

## Facts vs Positions

- **Mechanism / settled fact**: a hash function cannot be inverted in practice; the supply schedule converges below 21 million; a confirmed on-chain transfer cannot be reversed; a channel payment reverts if a hop is offline; liquidation price follows from loan, quantity and threshold; a fixed-supply token cannot be diluted by its issuer, while a token with a retained mint right can; compounding a daily rate gives an annual figure far above the daily one.
- **Position**: written "(position)" or "In this model...": whether a halving moves price, whether energy use is a cost or a security budget, whether self-custody or custodial is better, whether DeFi yields are sustainable, whether a bubble can be identified from data, whether offline digital cash is worth its risk, how a tax classification should be read. Each carries the rival view when known.
- Every concept has **Thesis**, **Mechanism**, **Trade-off**, **Does not hold when**. Read the last field before applying a rule.

## How to Use This Skill

Diagnose first: is the question a mechanism, a risk comparison, a claim to test, a failure case, a reporting concept, or a token launch? Ask which asset, which jurisdiction and which period, because many figures are snapshots.

| Task | Start with | Then |
|---|---|---|
| "How does a blockchain stop double spending? What is a UTXO?" | [ch01](chapters/ch01-blockchain-ledgers-and-utxo.md) | ch02 |
| "What is a halving? Why 21 million? How secure is mining?" | [ch02](chapters/ch02-bitcoin-issuance-mining-security.md) | ch08 |
| Seed phrase, passphrase, hardware wallet, custodial vs self-custody | [ch03](chapters/ch03-wallets-and-custody.md) | ch05, ch10 |
| Lightning, channels, small payments | [ch04](chapters/ch04-lightning-and-payments.md) | ch01 |
| Why did an exchange or lender fail? Warning signs | [ch05](chapters/ch05-exchanges-lending-and-counterparty-failures.md) | ch07, ch10 |
| Notes and funds versus holding the asset | [ch06](chapters/ch06-etns-etps-vs-holding-the-asset.md) | ch09, ch03 |
| Stablecoins, AMMs, lending, staking, yield, impermanent loss | [ch07](chapters/ch07-defi-staking-and-yield.md) | ch05, ch08 |
| Do halvings or cycles predict price? Is waiting for a dip better? Is there any anchor for the price? Leverage and hedging | [ch08](chapters/ch08-price-drivers-statistics-and-weak-tests.md) | `scientific-thinking` |
| What is taxable? Reporting duties? Step-up logic? | [ch09](chapters/ch09-taxation-and-reporting-concepts.md) | `personal-finance-italy` |
| Phishing, deepfakes, pyramid schemes, promised returns, 2FA | [ch10](chapters/ch10-scams-and-security-hygiene.md) | ch03, ch12 |
| Funding, open interest, liquidation cascades, on-chain holder and realised-price metrics, fund flows, cycle hypotheses, sizing volatile assets | [ch11](chapters/ch11-derivatives-on-chain-descriptors-and-cycle-hypotheses.md) | ch08, ch05 |
| Digital money: claim versus bearer value, offline cash, central-bank digital currencies, convenience spreads | [ch12](chapters/ch12-digital-money-claims-and-convenience-costs.md) | ch01, ch07 |
| Token launches, mint and freeze controls, pool depth, insiders and snipers, creator fees, unlocks | [ch13](chapters/ch13-token-launches-memecoins-and-insider-advantage.md) | ch07, ch10 |
| Quick lookup | [cheatsheet.md](cheatsheet.md), [patterns.md](patterns.md), [glossary.md](glossary.md) | |

## The Core Principles (recurrence order)

1. **Irreversibility moves risk to the user.** Mistakes, theft and lost keys have no recourse.
2. **Custody is a choice of failure mode.** Keys you hold fail by error; keys others hold fail by their solvency.
3. **A yield is a risk premium or a transfer.** Ask where it comes from.
4. **Wrappers swap operational risk for legal and credit risk.**
5. **Each layer is another place to fail.** Count the layers.
6. **Few events cannot prove a cycle.** Test with non-overlapping samples and controls for time.
7. **Leverage is judged by drawdown, not average return.**
8. **Hedging a high-drift asset usually costs more than it protects.**
9. **Tax follows events; records are the control.**
10. **Scams run on urgency and irreversible payment.** Verify through a channel you opened.
11. **Rehearse with worthless coins.** Untested procedures fail.
12. **A secret nobody can recover is a loss waiting to happen.** Plan succession.
13. **Leverage shows up in funding, open interest and liquidations.** Read each with its definition, venue and lag.
14. **Speculation has no anchor: size it, do not value it.** Without cash flows, the loss budget is the tool.
15. **Launch mechanics decide who pays first.** Supply controls, pool depth and fees come before the story.

## Chapter Index

1. [Blockchain, ledgers and the UTXO and account models](chapters/ch01-blockchain-ledgers-and-utxo.md)
2. [Bitcoin issuance, halving, mining and security](chapters/ch02-bitcoin-issuance-mining-security.md)
3. [Wallets and custody](chapters/ch03-wallets-and-custody.md)
4. [Payment channels, Lightning and payments](chapters/ch04-lightning-and-payments.md)
5. [Exchanges, lending and counterparty failures (case cards)](chapters/ch05-exchanges-lending-and-counterparty-failures.md)
6. [Notes, funds and other wrappers versus holding the asset](chapters/ch06-etns-etps-vs-holding-the-asset.md)
7. [DeFi, staking, stablecoins and yield](chapters/ch07-defi-staking-and-yield.md)
8. [Price drivers, statistics, weak tests and valuation without cash flows](chapters/ch08-price-drivers-statistics-and-weak-tests.md)
9. [Taxation and reporting concepts](chapters/ch09-taxation-and-reporting-concepts.md)
10. [Scams, promised returns and security hygiene](chapters/ch10-scams-and-security-hygiene.md)
11. [Derivatives and on-chain descriptors, and cycles as hypotheses](chapters/ch11-derivatives-on-chain-descriptors-and-cycle-hypotheses.md)
12. [Digital money, claims on issuers and convenience costs](chapters/ch12-digital-money-claims-and-convenience-costs.md)
13. [Token launches, memecoins and insider advantage](chapters/ch13-token-launches-memecoins-and-insider-advantage.md)

## Topic Index

- **51% attack, confirmations, reversal** -> ch02
- **AMM, slippage, impermanent loss** -> ch07
- **Bearer value versus claim on an issuer** -> ch12
- **Bubble, valuation without cash flows, cost basis as anchor** -> ch08, ch11
- **Cost basis, lot matching, step-up** -> ch09
- **Compounding promised returns, daily rates** -> ch10
- **Convenience spreads, kiosks, instant-buy** -> ch12
- **Creator fees, mint and freeze authority, admin keys** -> ch13
- **Custodial vs self-custody** -> ch03, ch05
- **Funding rate, open interest, liquidation cascades, basis, skew** -> ch11
- **Insiders, snipers, first blocks after launch** -> ch13
- **Liquidity pool depth, liquidity-provider tokens, market value versus sellable depth** -> ch13
- **Offline payments, double spend in cash-like systems** -> ch12
- **Realised price, MVRV, long-term holders, supply in profit or loss** -> ch11
- **Exchange balances, stablecoin supply as a proxy (position)** -> ch11
- **ETF creations and redemptions, cumulative flows, filing lag** -> ch06, ch11
- **Dominance and rotation (position)** -> ch11
- **Cycle claims, falsifiers, event lag** -> ch08, ch11
- **Loss budget, position cap, drawdown planning for volatile assets** -> ch08, ch11
- **Death spiral, algorithmic stablecoin** -> ch07, ch05
- **Central-bank digital currency, deposits versus wallets** -> ch12
- **Deepfake, impersonation, phishing** -> ch10
- **Derivation path, passphrase, seed phrase** -> ch03
- **Fees, mempool, replace-by-fee** -> ch01
- **Halving, 21 million, disinflationary** -> ch02, ch08
- **Hash, nonce, difficulty** -> ch01, ch02
- **Hedging cost, puts, shorts** -> ch08
- **Lightning, revocation, routing** -> ch04
- **Liquidation price, LTV** -> ch07, ch08
- **Monitoring duty, value levy, substitute tax (Italy, snapshot 2025)** -> ch09
- **Mint right, freeze function, token contract controls** -> ch13
- **Notes vs funds** -> ch06
- **Ponzi and pyramid arithmetic** -> ch10
- **Proof of reserves** -> ch05
- **Spurious correlation, small samples** -> ch08
- **Staking, slashing** -> ch07
- **Token unlocks, concentration of supply** -> ch13
- **UTXO, change, clustering** -> ch01

## Related Skills

- `investing-and-financial-history`: risk and return, diversification, behavioural finance, bubbles and fraud cases, discounting.
- `economics-finance`: money, banks, central banks, stablecoins as monetary instruments.
- `scientific-thinking`: statistical method and evidence quality.
- `personal-finance-italy`: Italian filing and tax mechanics in detail.
- `trading-methods-and-technical-analysis`: sizing and ruin (ch06), market microstructure and liquidity (ch12), structured products (ch10, ch11).

## Scope & Limits

Practical theory covering ledger design, issuance, custody, digital money, off-chain payments, counterparty failures, wrappers, DeFi, token launch mechanics, statistical testing of price claims, tax logic and scams. Token launches are described generically; no project is assessed. Not covered: specific products or venues, trading signals, price targets, portfolio construction for a person, legal advice, jurisdiction-specific rules beyond the dated Italy snapshot. Numbers come from worked examples and dated samples and are illustrative. The skill gives no legal, tax or investment guarantee.
