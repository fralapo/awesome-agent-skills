---
name: investing-and-financial-history
description: "Conceptual and historical investing knowledge, not advice: risk and return, market efficiency and price formation, factors and stock picking, diversification and asset allocation (rebalancing, costs), DCF and multiples, bonds (pricing, duration, inflation-linked, callable, credit) and the yield curve and QE, options, leveraged and structured products (mechanism only), behavioural finance, bubbles and crises with case cards, fraud, Ponzi schemes and impersonation, decisions under uncertainty, financial mathematics (compounding, IRR, NPV, drawdown), how to read a backtest (overlapping windows, survivorship, effect size), and retirement saving and decumulation (withdrawal rates, sequence risk). Use when the user asks why a market, bubble, crash or fraud happened, how an instrument works, how to compare returns, whether a study or backtest is reliable, what the evidence says on index funds or value, or wants both sides of a contested claim. No recommendations, no forecasts."
allowed-tools:
  - Read
  - Grep
argument-hint: [concept, historical case, claim to test, or chapter number]
---

# Investing and Financial History
**Chapters**: 14 | **Corpus**: theoretical transcripts, extended with applied-finance material | **Generated**: 2026-11-14

## Role and Boundaries

This skill **explains how investing concepts work and how financial episodes unfolded**: what risk and return mean, why prices behave as they do, what the evidence says on active versus passive and on factors, how valuation, bonds, options and leveraged products work mechanically, how to compute and compare returns, how to read a backtest, how retirement saving and withdrawal behave, how bubbles, runs and frauds are built, and how to judge a decision separately from its outcome. It gives mechanisms, dated figures, case cards with proposed causes, and the strongest case on each side of contested claims.

| This skill decides | This skill hands off |
|---|---|
| Mechanism of a concept (DCF, covered call, yield curve, diversification, duration, drawdown) | Buying, selling, timing or sizing any asset; portfolio, tax or product advice |
| Which causes are proposed for a bubble or crisis and which are contested | Monetary, fiscal and banking macro (banks, QE, inflation, public debt, crises as macro) -> `economics-finance` |
| How strong a statistic is and how old it is | Statistical method and study design in depth -> `scientific-thinking` |
| Warning signs of a fraud, as prompts to verify; how to read a study | Legal, accounting or compliance advice; proving fraud; one country's tax rules and products -> `personal-finance-italy`; digital-asset technology and custody -> `crypto-and-digital-assets` |
| How to separate decision quality from outcome | Company valuation work for deals or pricing strategy -> `pricing-and-sales-negotiation` |

**Stay in lane.** Educational concepts and history only: no investment advice, no forecasts, no "buy this". Figures are dated snapshots and context-bound; re-check before relying on them. General textbook background is marked "general knowledge"; items that could not be confirmed are marked "(unverified)" or omitted. Every chapter opens with a short "educational, not advice" notice.

## Facts vs Positions

- **Mechanism / settled fact**: a bond price moves opposite its yield; a covered call caps upside; the arithmetic of active management before and after costs; idiosyncratic risk can be diversified away.
- **Position**: written "(position)" or "In this model...": whether markets are efficient enough, whether factor premiums are risk or mispricing and whether they persist, whether stock picking can pay, whether the yield curve is a useful signal, whether equal weight beats cap weight, how low a withdrawal rate must be, how much of a crash is mechanical versus psychological, what caused 2008. Each carries the rival view.
- Every concept has **Thesis**, **Mechanism**, **Trade-off**, **Does not hold when**. Read the last field before applying a rule.

## How to Use This Skill

Diagnose before explaining: is the question a concept (what is X), a case (why did Y happen), a claim to test (is Z true), or a decision frame? Ask what time period and market the user means: many statistics are US-centric and date-bound.

| Task | Start with | Then |
|---|---|---|
| "What does risk mean? Volatility or loss?" | [ch01](chapters/ch01-risk-and-return.md) | ch04, ch11 |
| "Are markets efficient? Can anyone beat them?" | [ch02](chapters/ch02-market-efficiency-and-prices.md) | ch03, ch08 |
| Value, factors, stock picking, active funds: both sides | [ch03](chapters/ch03-factors-value-and-stock-picking.md) | ch02, ch11 |
| Diversification, how many stocks, home bias, stock-bond mix | [ch04](chapters/ch04-diversification-and-asset-allocation.md) | ch01, ch03 |
| Rebalancing, equal vs cap weight, lump sum vs staged entry, hedged funds, fund costs, accumulating vs distributing, buckets by horizon | [ch04](chapters/ch04-diversification-and-asset-allocation.md) (4.7-4.14) | ch12, ch13, ch14 |
| DCF, P/E, multiples, "is it cheap?" | [ch05](chapters/ch05-valuation-dcf-and-multiples.md) | ch02, ch09 |
| Bonds, yield curve inversion, QE | [ch06](chapters/ch06-bonds-yield-curve-and-qe.md) | `economics-finance` |
| Bond price and yield, accrued interest, duration, bond funds vs single bonds, inflation-linked, callable and step-up, credit and currency risk | [ch06](chapters/ch06-bonds-yield-curve-and-qe.md) (6.7-6.14) | ch12, ch14 |
| Options, covered calls, the Greeks (mechanism) | [ch07](chapters/ch07-derivatives-and-options-mechanics.md) | ch09 |
| Leveraged ETFs, futures and margin, autocallable and protected certificates | [ch07](chapters/ch07-derivatives-and-options-mechanics.md) (7.6-7.11) | ch10, ch13 |
| Why do investors act irrationally? | [ch08](chapters/ch08-behavioral-finance.md) | ch02, ch11 |
| Bubbles, crashes, runs: why did it happen? | [ch09](chapters/ch09-anatomy-of-bubbles-and-crises.md) | ch05, ch10 |
| Ponzi schemes, accounting frauds, rogue traders, impersonation scams, pyramid structures, yield platforms, signs | [ch10](chapters/ch10-fraud-ponzi-and-warning-signs.md) | ch08, ch09 |
| Good decision versus good outcome, sticking with a plan | [ch11](chapters/ch11-decisions-under-uncertainty.md) | ch01, ch03 |
| Compounding, annualising, IRR/NPV, log returns, drawdown, volatility, CAPE, adjusting price series | [ch12](chapters/ch12-financial-mathematics-returns-and-uncertainty.md) | ch05, ch13 |
| Is this backtest or study reliable? Overlapping windows, survivorship, tests, market timing | [ch13](chapters/ch13-backtesting-and-historical-evidence.md) | ch02, ch03, `scientific-thinking` |
| FIRE, withdrawal rates, sequence risk, pension fund vs direct investing, annuities | [ch14](chapters/ch14-retirement-saving-and-decumulation.md) | ch04, ch12 |
| Quick lookup | [cheatsheet.md](cheatsheet.md), [patterns.md](patterns.md), [glossary.md](glossary.md) | |

## The Core Principles (recurrence order)

1. **Risk is paid only when it cannot be diversified.** Market risk earns a premium; single-company risk does not.
2. **A premium is an average, not a promise.** Long samples hide lost decades.
3. **Compete against the cheap baseline.** Active management is zero-sum before costs and negative-sum after.
4. **Test claims out of sample.** A pattern needs a reason, persistence across places and times, and a cost-adjusted way to capture it.
5. **You can never test efficiency alone.** Every test includes a model of normal returns.
6. **Valuation is a question, not an answer.** Inputs dominate; use it to read what a price assumes.
7. **Skew punishes concentration.** A few winners make the market's return; a small basket usually misses them.
8. **Bubbles are loops.** Price changes funding, funding changes fundamentals, until reversal.
9. **Leverage and interlinked promises turn losses into crises.**
10. **Fraud needs trust and a flow of new money.** Verify independently; authority is not evidence.
11. **Judge decisions by process at the time, not by outcome.**
12. **Know your limits.** Biases are predictable; rules and pre-commitment beat willpower.
13. **A yield above the market is the price of a risk.** Ask which risk before calling it a bargain.
14. **Count independent observations, not windows.** Overlap, survivorship and many tried rules inflate a backtest.
15. **Saving is a right-tail problem, withdrawing a left-tail one.** The order of returns matters once money leaves.

## Chapter Index

1. [Risk and return](chapters/ch01-risk-and-return.md)
2. [Market efficiency and how prices form](chapters/ch02-market-efficiency-and-prices.md)
3. [Factors, value and stock picking (contested)](chapters/ch03-factors-value-and-stock-picking.md)
4. [Diversification and asset allocation](chapters/ch04-diversification-and-asset-allocation.md)
5. [Valuation: DCF and multiples](chapters/ch05-valuation-dcf-and-multiples.md)
6. [Bonds, the yield curve and QE](chapters/ch06-bonds-yield-curve-and-qe.md)
7. [Derivatives and options: mechanism](chapters/ch07-derivatives-and-options-mechanics.md)
8. [Behavioural finance](chapters/ch08-behavioral-finance.md)
9. [Anatomy of bubbles and crises (case cards)](chapters/ch09-anatomy-of-bubbles-and-crises.md)
10. [Fraud, Ponzi schemes and warning signs](chapters/ch10-fraud-ponzi-and-warning-signs.md)
11. [Decisions under uncertainty](chapters/ch11-decisions-under-uncertainty.md)
12. [Financial mathematics, returns and uncertainty of estimates](chapters/ch12-financial-mathematics-returns-and-uncertainty.md)
13. [Backtesting and historical evidence: how to read a study](chapters/ch13-backtesting-and-historical-evidence.md)
14. [Retirement saving and decumulation](chapters/ch14-retirement-saving-and-decumulation.md)

## Topic Index

- **Accrued interest, clean and dirty price** -> ch06
- **Accumulating vs distributing funds** -> ch04, ch14
- **Active management arithmetic, persistence** -> ch02, ch03
- **Alpha, factor regression, R-squared** -> ch03
- **Annuities, bridge annuity, public pension formula** -> ch14
- **Asset allocation, risk profile, buckets by horizon** -> ch01, ch04
- **Autocallable and capital-protected certificates** -> ch07
- **Backtest, overlapping windows, survivorship, significance** -> ch13
- **Bank runs 2023, duration mismatch** -> ch06, ch09
- **Behavioural biases (loss aversion, disposition, endowment)** -> ch08
- **Bond price and yield, seniority, junk bonds** -> ch06
- **Bond funds vs single bonds, target-maturity funds** -> ch06
- **Bubble anatomy, reflexivity** -> ch09
- **AI build-out, circular financing, backlog contracts (case card)** -> ch09
- **Margins, buybacks, dilution, asset lives; private stake by comparables** -> ch05.6, ch05.7
- **CAPE, valuation ratios as forecasts** -> ch12, ch13
- **Compounding, annualising, log returns, IRR, NPV** -> ch12
- **Covered calls, delta, gamma, theta** -> ch07
- **Currency hedging, foreign-currency bonds** -> ch04, ch06
- **DCF, terminal value, cost of capital** -> ch05
- **Dot-com, 2008, 1929, 1987, LTCM, South Sea, Mississippi** -> ch09
- **Drawdown, VaR, volatility at the horizon** -> ch12
- **Duration, convexity, rate risk** -> ch06
- **Equal weight vs cap weight** -> ch04
- **Equity risk premium, lost decades** -> ch01
- **Factor ETFs, factor zoo, value premium debate** -> ch03, ch04
- **Fraud warning signs, Ponzi, rogue traders** -> ch10
- **Fund costs, TER, tracking, spread** -> ch04
- **Good decision versus good outcome** -> ch11
- **Impersonation, deepfake endorsements, pyramid structures** -> ch10
- **Inflation-linked bonds, break-even inflation** -> ch06
- **Joint hypothesis, random walk** -> ch02
- **Leveraged ETFs, volatility drag, wipe-out threshold** -> ch07
- **Lump sum vs staged entry, value averaging** -> ch04
- **Market timing, cost of exit rules** -> ch13
- **Multiples (P/E trailing, forward)** -> ch05
- **Pension fund vs direct investing, employer match** -> ch14
- **QE, yield curve inversion** -> ch06
- **Rebalancing** -> ch04
- **Sequence-of-returns risk, withdrawal rates, Monte Carlo** -> ch14
- **Stock skew, catastrophic loss, concentration** -> ch03, ch04
- **Volatility versus risk** -> ch01, ch12

## Related Skills

- `economics-finance`: money creation, central banks and QE mechanics, inflation, public debt, banking and sovereign crises, how to reason in economics.
- `scientific-thinking`: statistical method, evidence quality, study design.
- `personal-finance-italy`: one country's tax rules, savings products, filings and pension products (dated snapshots).
- `crypto-and-digital-assets`: blockchain basics, custody, exchanges, staking and DeFi risks, digital-asset taxation concepts.
- `pricing-and-sales-negotiation`: company valuation for deals, pricing strategy.

## Scope & Limits

Practical theory and history covering market efficiency, index and factor investing, risk, diversification and allocation, valuation, bonds (pricing, duration, options embedded in bonds, credit, currency), options and leveraged products, financial mathematics, backtest reading, retirement saving and withdrawal, behavioural finance, financial crises and frauds. Not covered: any person's portfolio, product selection or sizing, trading signals, digital-asset technology, and the tax rules or regulation of a specific country (those sit in dated, country-specific skills). Statistics come from US, Canadian and other developed-market datasets and from small simulations, quoted with their dates and samples; where a figure comes from a short sample it is labelled as such. Some mechanisms are general knowledge and are marked. Several chapters present contested positions with both sides; none gives a recommendation. Case summaries of frauds describe public, widely reported events briefly and neutrally. The skill gives no legal, tax or investment guarantee.
