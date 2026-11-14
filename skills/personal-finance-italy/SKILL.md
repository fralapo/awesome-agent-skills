---
name: personal-finance-italy
description: "Concepts and tax mechanics of Italian personal finance, not advice: savings vehicles and bank products (deposits, cards, stamp duty, deposit guarantee), government bonds (BTP families, accrued interest, inflation-linked, taxation 12.5% versus 26%), corporate, bank and structured bonds (callable, step-up, discount), ETF and fund taxation (capital income versus miscellaneous income, accumulation versus distribution), capital losses and carry-forward, tax filings for foreign brokers (RW, RT, RM, F24), pension products and retirement, real estate and mortgages (amortisation, fixed versus variable, rent versus buy, property taxes), inheritance and gifts, PIR and flat regimes, scams and consumer protection, and how to verify a rule. Use when the user asks how an Italian financial instrument or tax works, how to compare two Italian products net of tax, how to read a figure marked as a snapshot, or how to check the rule in force. No recommendations, no forecasts, no personal tax advice."
allowed-tools:
  - Read
  - Grep
argument-hint: [instrument, tax rule, form, or chapter number]
---

# Personal Finance Italy
**Chapters**: 12 | **Corpus**: ~200 theoretical transcripts on Italian personal finance, plus general knowledge where marked | **Generated**: 2026-11-14

## Role and Boundaries

This skill **explains how Italian personal-finance instruments and their taxation work**: what a BTP, a pension fund, a mortgage or a foreign-broker filing is made of, why a rule produces its result, and how to compare two options on a net, dated-cash-flow basis. It gives mechanisms, worked examples with explicit snapshot years, and the strongest case on each side of contested points.

| This skill decides | This skill hands off |
|---|---|
| Mechanism of an Italian instrument or tax rule (as a snapshot) | Buying, selling, timing or sizing any asset; personal tax, legal or accounting advice |
| How to compare two products net of tax, stamp duty and costs | General market theory, allocation, factors, valuation -> `investing-and-financial-history` |
| What a form section or tax category concept is | Macro: inflation, central banks, public debt, banking crises -> `economics-finance` |
| How to find and date a rule | Statistical method and study design -> `scientific-thinking` |
| Warning signs of scams and product mis-selling | Crypto technology, custody, protocol details -> `crypto-and-digital-assets` |

**Stay in lane.** Educational concepts only. **All figures are snapshots from 2021 to 2026, each tagged with country and year, and must be re-checked against the rule in force.** Italian rules change by budget law, decree and guidance; forms change every year. This is not tax advice and does not replace an accountant, notary or lawyer. General background that is not from the corpus is marked "general knowledge" and should be verified. Every chapter opens with an "educational, not advice" notice.

## Facts vs Positions

- **Mechanism / settled fact**: price and yield move in opposite directions; net = gross x (1 - tax); a loss on an ETF is a miscellaneous-income loss and a gain on the same ETF is capital income; a deposit guarantee covers deposits, not securities.
- **Position**: written "(position)" or "In this model...": whether a pension fund beats a self-managed ETF for a given investor, whether a wrapper is worth its fee, whether renting beats buying, whether the exposure to a single sovereign is acceptable, whether an inflation-linked bond beats a fixed one. Each carries the rival view or the condition that flips it.
- Every concept has **Thesis**, **Mechanism**, **Trade-off**, **Does not hold when**, and often a **Worked example**. Read the last field before applying a rule.

## How to Use This Skill

Diagnose first: which instrument, which person (employee, self-employed, company, minor, heir), which tax year, which event (buy, hold, sell, die, inherit). Then ask whether the question is a concept, a comparison, a form question, or a "is this a scam" question. Quote the snapshot year with every figure.

| Task | Start with | Then |
|---|---|---|
| Current account, deposit, card, stamp duty, guarantee | [ch01](chapters/ch01-savings-vehicles-and-bank-products.md) | ch11, ch12 |
| BTP, BOT, inflation-linked, step-up, accrued interest, bid and ask | [ch02](chapters/ch02-government-bonds.md) | ch03, ch05 |
| Corporate or bank bond, callable, subordinated, foreign currency | [ch03](chapters/ch03-corporate-bank-and-structured-bonds.md) | ch02, ch11 |
| ETF or fund tax, accumulation versus distribution, white-list share | [ch04](chapters/ch04-etf-and-fund-taxation.md) | ch05, ch06 |
| Capital losses, carry-forward, 12.5/26 scaling, order of sales | [ch05](chapters/ch05-capital-losses-and-loss-harvesting.md) | ch04, ch06 |
| Foreign broker: RW, RT, RM, lots, F24, late repair | [ch06](chapters/ch06-tax-filings-for-foreign-brokers.md) | ch05, ch12 |
| Pension fund, TFR, bridge annuity, public pension, annuity | [ch07](chapters/ch07-pension-products-and-retirement.md) | ch10, ch12 |
| Mortgage, fixed versus variable, rent versus buy, rental yield, IMU | [ch08](chapters/ch08-real-estate-mortgages-and-property-taxes.md) | ch10, ch12 |
| Inheritance, gifts, minors, cost basis at death | [ch09](chapters/ch09-inheritance-gifts-and-family-wealth.md) | ch04, ch05 |
| PIR, flat regime, IRPEF, company versus sole proprietor | [ch10](chapters/ch10-pir-flat-regimes-and-income-structures.md) | ch07, ch12 |
| Scams, advice conflicts, insurance, gambling, payments | [ch11](chapters/ch11-scams-consumer-protection-and-payments.md) | ch01, ch12 |
| "Is this rule still valid? Where do I check?" | [ch12](chapters/ch12-how-to-verify-a-rule.md) | every chapter |
| Quick lookup | [cheatsheet.md](cheatsheet.md), [patterns.md](patterns.md), [glossary.md](glossary.md) | |

## The Core Principles (recurrence order)

1. **Net, then compare.** Convert everything to net, dated cash flows after tax, stamp duty and costs.
2. **The category of income decides.** Capital income cannot be offset by losses; miscellaneous income can. Funds and stocks sit on different sides.
3. **A loss is an expiring credit**, not cash: rate x loss, realisation year plus four.
4. **Structure beats headline rate.** Call, step-up, subordination, currency and lock-up explain most "high" yields.
5. **The tax wrapper is worth it only if tax avoided exceeds fee and constraints.**
6. **Regime changes who does the work.** Administered is automatic; declarative is yours.
7. **Price and yield are one quantity.** Use ask for buying, bid for selling; IRR on dated flows.
8. **Inflation compensation has a lag and a tax mismatch.**
9. **Deposits are guaranteed; securities are segregated.** Different protections, different failures.
10. **Costs are paid in loss years.** Judge cost against expected return, not capital.
11. **Urgency, irreversible payment and escalating fees mark scams.**
12. **Every number is a snapshot.** Find the rule, date it, write down the source.

## Chapter Index

1. [Savings vehicles and bank products](chapters/ch01-savings-vehicles-and-bank-products.md)
2. [Government bonds](chapters/ch02-government-bonds.md)
3. [Corporate, bank and structured bonds](chapters/ch03-corporate-bank-and-structured-bonds.md)
4. [ETF and fund taxation](chapters/ch04-etf-and-fund-taxation.md)
5. [Capital losses and loss harvesting](chapters/ch05-capital-losses-and-loss-harvesting.md)
6. [Tax filings for foreign brokers](chapters/ch06-tax-filings-for-foreign-brokers.md)
7. [Pension products and retirement](chapters/ch07-pension-products-and-retirement.md)
8. [Real estate, mortgages and property taxes](chapters/ch08-real-estate-mortgages-and-property-taxes.md)
9. [Inheritance, gifts and family wealth](chapters/ch09-inheritance-gifts-and-family-wealth.md)
10. [PIR, flat regimes and income structures](chapters/ch10-pir-flat-regimes-and-income-structures.md)
11. [Scams, consumer protection and payments](chapters/ch11-scams-consumer-protection-and-payments.md)
12. [How to verify a rule](chapters/ch12-how-to-verify-a-rule.md)

## Topic Index

- **Accrued interest, clean and dirty price** -> ch02
- **Accumulation versus distribution** -> ch04
- **Annuity pricing, bridge annuity** -> ch07
- **Bid, ask, spread, order book** -> ch02
- **Callable, step-up, fixed-then-floating** -> ch03
- **Capital income versus miscellaneous income** -> ch04, ch05
- **Cards (debit, credit, prepaid), suspensions** -> ch01
- **Deposit guarantee, securities custody** -> ch01
- **Foreign-currency bonds** -> ch03
- **F24, late-filing repair** -> ch06
- **Inflation-linked bonds, break-even** -> ch02
- **Inheritance, reserved quotas, cost basis at death** -> ch09
- **IVAFE and foreign-asset monitoring** -> ch06
- **Loss carry-forward, 12.5/26 scaling** -> ch05
- **Mortgage amortisation, surroga, fixed versus variable** -> ch08
- **PIR, flat regime, occasional work** -> ch10
- **Pension fund versus ETF, TFR, match** -> ch07
- **Rent versus buy, rental net yield** -> ch08
- **Scams, mis-selling, insurance, gambling** -> ch11
- **Stamp duty** -> ch01, ch02
- **White-list share, bond fund tax** -> ch04
- **Verifying a rule, source hierarchy** -> ch12

## Related Skills

- `investing-and-financial-history`: risk, allocation, valuation, bonds and derivatives mechanics, behaviour, fraud, retirement decumulation.
- `economics-finance`: money, inflation, banking, housing as economics.
- `crypto-and-digital-assets`: what the asset is, custody, taxation concepts beyond Italy.
- `scientific-thinking`: weighing evidence and statistical method.

## Scope & Limits

Practical theory on Italian personal-finance instruments and their taxation, as dated snapshots (2021-2026). Not covered: advice on a person's situation, product selection, forecasts, other jurisdictions in detail (a few Dutch and Belgian reference points appear in ch04 as contrast), commercial product names, and professional accounting or legal work. Where a figure comes from general knowledge rather than the corpus it is marked and should be verified in an official source. The skill gives no legal, tax or investment guarantee, and the rule in force always prevails over any figure here.
