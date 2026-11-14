# Chapter 06: Tax Filings for Foreign Brokers

> Educational concepts, not investment, tax or legal advice. Forms, rates and deadlines are snapshots (Italy, 2025 unless stated), to be re-checked against the rule in force for the tax year.

## Core Idea
In this model, a foreign broker does not change what is taxed; it changes **who does the work**. With a domestic intermediary acting as withholding agent, tax is computed and paid for you. With a foreign one the regime is declarative: you reconstruct every lot, report income and holdings even without sales, and pay the tax yourself. The cost is accuracy and attention, not only fees.

## 6.1 Why a foreign broker means declarative
- **Thesis**: the compliance cost can exceed the commission saving for small portfolios.
- **Mechanism**: lower fees and wider markets are the draw; the price is a personal return with several sections (monitoring, gains, capital income), a specialist accountant in many cases, and higher audit exposure. A domestic intermediary in the administered regime does it all; with foreign brokers the investor "declares income and foreign holdings even without sales".
- **Trade-off**: lower trading costs versus paperwork and error risk.
- **Does not hold when**: the investor is a high-volume trader on foreign markets with an accountant.

## 6.2 The cost-basis method and the lot ledger
- **Thesis**: using the wrong inventory method produces a false gain.
- **Mechanism**: in the declarative regime LIFO applies to shares, bonds and ETC/ETN, while weighted average cost applies to funds and harmonised ETFs; in the administered regime the intermediary uses average cost (Italy, snapshot 2025; verify for the tax year). For LIFO positions keep one ledger row per purchase lot; a sale consumes the newest lots first. History from the first purchase is required because an old lot may remain open. The broker's gain differs from the fiscal gain because method, currency conversion and fund classification differ. Holding days must be computed per movement and weighted by value for monitoring.
- **Trade-off**: accuracy versus extra work; grouping monthly entries reduces rows.
- **Does not hold when**: all positions are closed at year end and no earlier lots remain.

## 6.3 The sections of the return
| Section (Italian) | Concept | Typical content |
|---|---|---|
| "Quadro RW" | monitoring of foreign assets | holdings abroad, with initial and final value, days held |
| "Quadro RT" | capital gains / losses ("redditi diversi") | gains and losses on shares, ETC/ETN, certificates and bonds, with the 26% substitute tax; gains on harmonised ETFs and funds are capital income (RM) and only their losses go to RT |
| "Quadro RM" | income taxed separately | dividends and capital income from abroad at 26% |
| "Quadro RL / RE" | other income (context) | miscellaneous income, professional (context) |
| "Quadro CE" | foreign tax credit | withholding abroad credited domestically |

These are structural summaries; section numbers and layouts change by year. Always check the instructions for the tax year (ch12).

## 6.4 Foreign-asset monitoring and the annual levy
- **Thesis**: the monitoring schedule is a **flow ledger**, not a balance, so reported values can look huge.
- **Mechanism**: initial value for assets not held on 1 January is the purchase cost, not zero; final value is at year end; the levy on foreign financial assets ("IVAFE", 0.2%, Italy snapshot 2025) is prorated by days; foreign cash without interest is monitored but not levied; joint accounts are reported by share; the prior year's advance must be entered manually.
- **Worked example**: levy on 530,339 final value over 217 days = 530,339 x 0.002 x 217/365 about 630 euro.
- **Does not hold when**: the intermediary is domestic and acts as withholding agent.

## 6.5 Which form carries what
- Dividends from abroad: capital income, taxed 26% via the capital-income section, with a credit for foreign withholding where applicable. Single stocks suffer foreign withholding plus domestic tax on the gross dividend; funds are cleaner because withholding is handled at fund level (Italy, snapshot 2025).
- Gains and losses on sales: the gains section; carry-forward of losses by declaring them (ch05).
- Interest on foreign cash, bond coupons from abroad: capital-income section.
- Holdings: always the monitoring section, even with no sales and no income.

## 6.6 Personal return, payment and deadlines
- **Thesis**: the standard employee form ("730") does not cover everything; investors with sections beyond its scope (verify for the tax year; some foreign-asset lines can also be carried in the employee form, as for crypto-assets since 2024) typically use the full personal return ("Redditi Persone Fisiche").
- **Mechanism (general knowledge, to verify)**: payments run through the unified payment form ("F24") with codes for each tax; balance and first advance are generally due by the end of June of the following year (or shortly after with a small surcharge), the second advance by end of November; an extra year of payment for the declarative regime follows the realisation. Late or wrong filing can be repaired through "ravvedimento operoso": voluntary correction with reduced penalties that shrink the sooner you act, plus interest. Dates move yearly; confirm for the tax year.
- **Trade-off**: reduced penalties versus the cost of a repeat error.
- **Does not hold when**: an audit has already started (ravvedimento rules narrow).

## 6.7 Working method for a clean filing
1. Export the full transaction history from the first purchase, not only the year.
2. Normalise currency using the conversion rule applicable to each flow (date of the transaction).
3. Run the ledger by lot with the right method per instrument type.
4. Compute holding days per movement for monitoring.
5. Net gains and losses of the year regardless of order (declarative), then apply carried-forward losses of the right category within their expiry.
6. Cross-check the result against the broker's statement and explain any gap (method, FX, fund classification).
7. Keep the working file; the substantiation is yours.

## 6.8 Crypto holdings in the same return
For crypto-assets (Italy, snapshot 2025): gains taxed at 26% via the gains section; a separate 0.2% levy on final value x days/365 in the monitoring section, with a code per asset type. Swaps between assets of the same category are irrelevant for the gain but not for the monitoring; fees paid in crypto are disposals; basis is inherited through irrelevant swaps and uses last-in-first-out; staking and promotions are income, not gain. A holder using a domestic intermediary acting as withholding agent (for example for notes) escapes most of this. See `crypto-and-digital-assets` for the asset side.

## Common mistakes
- Treating the monitoring section as a balance sheet and entering year-end values only.
- Using average cost for a share or LIFO for a fund or harmonised ETF in the declarative regime.
- Forgetting the prior-year advance or a foreign tax credit.
- Ignoring holdings that produced no income or sales.

## Links
- ch04 regimes and categories; ch05 losses; ch11 broker choice and fees; ch12 verification; `crypto-and-digital-assets`.
