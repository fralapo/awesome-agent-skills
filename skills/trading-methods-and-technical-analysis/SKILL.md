---
name: trading-methods-and-technical-analysis
description: "Conceptual knowledge of how trading and market analysis reason, not advice, not signals, not forecasts: trend and levels, indicators, candlesticks and chart figures, Ichimoku, seasonality, positioning and sentiment, strategy families with rules and invalidation, stops, sizing, leverage, ruin and Kelly, drawdown, trader psychology, backtests and claimed results including seller incentives and compounding, fundamental screening with inconsistent thresholds flagged, options, turbos and barrier certificates, structured-product scans, market microstructure (impact, dealers, settlement, index flows), return skew and anomalies, and rate regimes. Use when the user asks how an indicator or pattern works, what a rule's failure modes are, how to size a position, whether a backtest or track record is credible, how a leveraged or structured product fails, or how prices are formed."
allowed-tools:
  - Read
  - Grep
argument-hint: [indicator, pattern, strategy, risk calculation, claim to test, product, market mechanism, or chapter number]
---

# Trading Methods and Technical Analysis
**Chapters**: 13 | **Corpus**: a synthesis of educational material on trading methods, technical and fundamental screening, market microstructure, and leveraged products | **Generated**: 2026-11-16

## Role and Boundaries

This skill **explains how traders reason about markets and where each method breaks**: what an indicator measures, how a pattern or level is defined, what a strategy's entry, exit, size and invalidation rules are, how risk per trade becomes position size, how to judge a backtest or a claimed result, how fundamental screens are built, how leveraged and structured products pay and fail, and how orders, dealers and index rules move prices. It gives mechanisms, worked arithmetic, rule cards and the strongest case on each side of contested claims.

| This skill decides | This skill hands off |
|---|---|
| What a formula measures (RSI, stochastic, ATR, Ichimoku lines, pivots) | Whether to buy, sell or hold anything; signals, entries, price targets; portfolio or product choice |
| A strategy's rules, regime and invalidation, as described | Market efficiency, factor evidence, backtest statistics in depth -> `investing-and-financial-history` (ch02, ch13) |
| Break-even win rate, size from risk, drawdown arithmetic, Kelly and ruin, notional exposure | Behavioural biases in general -> `investing-and-financial-history` ch08, `behavior-and-decision-science` |
| How credible a claimed result is and what a test needs | Statistical method and multiple testing -> `scientific-thinking` |
| Payoff and failure modes of a turbo, barrier certificate or margin product | Tax treatment and national product rules -> `personal-finance-italy`; crypto custody and venues -> `crypto-and-digital-assets` |
| Screening ratios and accounting red flags as hints | Full valuation theory -> `investing-and-financial-history` ch05; macro forecasting, central banks and bond analysis -> `economics-finance` |

**Stay in lane.** Educational concepts only: no investment or trading advice, no signals, no forecasts, no "buy this". Parameters are conventions reported by practitioners, not optimal settings. Figures are dated snapshots or worked examples; product terms, leverage limits, settlement cycles and market rules must be re-checked. Supplements from general knowledge are marked "general knowledge". Every chapter opens with an "educational, not advice" notice.

## Facts vs Positions

- **Mechanism / settled fact**: an indicator is a formula of past prices; a stochastic reading of 80 means the close sits near the top of its range; break-even win rate = 1 / (1 + reward-to-risk); size = money at risk / (stop distance x value per point); a turbo ends at zero on touching its barrier; a daily fixed-leverage product does not return to its start when the underlying does; recovery after a drawdown d needs 1 / (1 - d) - 1; a position with leverage L is wiped out by an adverse move of about 1 / L; the price impact of an order grows less than in proportion to its size.
- **Position**: written "(position)" or "In this model...": whether overbought means anything, which seasonal horizon to use, whether positioning beats seasonality, whether breakouts or pullbacks are better, how much to risk per trade, whether Kelly-style sizing is usable, whether retail sentiment is a contrarian signal, whether dealers' launch behaviour is fair, which solvency thresholds apply. Each carries the rival view when known.
- **The overarching contested claim**: whether technical rules have predictive value net of costs. In this model they organise decisions and enforce discipline; the rival view (weak-form efficiency, data-snooping studies) says past prices do not forecast returns after costs, with partial support only for diversified trend following and momentum at portfolio level (ch08, 8.6; `investing-and-financial-history` ch02, ch13).
- **Inconsistent thresholds** between practitioners (Z-Score, M-Score, debt/equity, seasonal win rates, stop/target ratios, risk per trade, settlement cycles) are marked **inconsistent**, not resolved.
- Every concept has **Thesis**, **Mechanism**, **Trade-off**, **Does not hold when**. Strategy cards also state **Invalidation**. Read the last fields before applying a rule.

## How to Use This Skill

Diagnose first: is the question about a measure, a pattern, a rule, a calculation, a claim to test, a product, or a market mechanism? Ask which instrument, which timeframe and which period, because every reading depends on horizon and many figures are snapshots.

| Task | Start with | Then |
|---|---|---|
| "Is it in a trend? Where is support? Is this breakout real?" | [ch01](chapters/ch01-market-structure-trend-and-levels.md) | ch03, ch05 |
| What RSI, MACD, stochastic, ATR, ADX or a moving average measures; divergences | [ch02](chapters/ch02-moving-averages-oscillators-and-volatility.md) | ch05, ch08 |
| Candles, head and shoulders, triangles, Ichimoku, cycles, Fibonacci | [ch03](chapters/ch03-candlesticks-chart-patterns-and-ichimoku.md) | ch01, ch08 |
| Seasonality, COT report, retail sentiment, sector rotation, analog statistics, composite readings | [ch04](chapters/ch04-seasonality-positioning-and-sentiment.md) | ch08 |
| Rules and invalidation of trend, mean-reversion, breakout, pair, momentum, intraday methods | [ch05](chapters/ch05-strategy-families-rules-and-invalidation.md) | ch06, ch08 |
| Stops, targets, reward-to-risk, size, leverage, Kelly and ruin, correlation, drawdown | [ch06](chapters/ch06-risk-management-and-position-sizing.md) | ch07, ch10 |
| Discipline, cutting losses, panic, hindsight, routines | [ch07](chapters/ch07-trader-psychology-and-discipline.md) | ch06 |
| "Is this backtest or track record credible?" Who is paid when I follow a seller? Promised returns, compounded | [ch08](chapters/ch08-validation-backtests-and-claimed-results.md) | `investing-and-financial-history` ch13 |
| Ratios, Z-Score, Piotroski, Beneish, fair value, shareholder yield, insiders | [ch09](chapters/ch09-fundamental-screening-and-accounting-red-flags.md) | `investing-and-financial-history` ch05 |
| Options, premium selling, lottery tickets, turbos, fixed leverage, barrier and binary certificates, margin products | [ch10](chapters/ch10-options-certificates-and-leveraged-products.md) | ch06, `investing-and-financial-history` ch07 |
| Side-by-side scan of structured products: thresholds, buffers, coupon basis, scenario grid, checklist | [ch11](chapters/ch11-scanning-and-comparing-structured-products.md) | ch10, ch06 |
| Price impact, market makers and spreads, order routing, settlement, ETF creation, index-rule flows, days to liquidate | [ch12](chapters/ch12-market-microstructure-liquidity-and-flows.md) | ch06, ch10 |
| Return skew, small samples, anomalies and their decay, multiples, rate regimes and duration | [ch13](chapters/ch13-return-distribution-anomalies-and-regimes.md) | ch08, ch09 |
| Quick lookup | [cheatsheet.md](cheatsheet.md), [patterns.md](patterns.md), [glossary.md](glossary.md) | |

## The Core Principles (recurrence order)

1. **No direction without a horizon.** Higher timeframes set context, lower ones timing.
2. **Indicators measure, they do not predict.** Know the formula before reading the signal.
3. **Levels are zones, breaks are closes.** Touches and thin lines produce false signals.
4. **Every rule has a regime.** Trend rules bleed in ranges; range rules break in trends.
5. **Decide the invalidation first.** Then target, then size; never the lot first.
6. **Break-even win rate is 1 / (1 + R).** Hit rate alone says nothing.
7. **Risk follows notional, not margin.** Leverage is exposure, not a multiplier of skill.
8. **Correlated positions are one position.** Correlations jump toward one in stress.
9. **Panic is a sizing error.** Structure beats willpower.
10. **A claimed result is not a measured one.** Fixed rules, out-of-sample data, costs, enough trades.
11. **Confirmations do not add.** Correlated signals count once.
12. **Every product has a death event.** Barrier, margin call, reset or issuer default: find it first.
13. **The average is not your path.** Compounding, ruin and skew decide what a single account experiences.
14. **Read the seller's revenue line first.** It shows what is being sold.

## Chapter Index

1. [Market structure, trend and price levels](chapters/ch01-market-structure-trend-and-levels.md)
2. [Moving averages, oscillators and volatility measures](chapters/ch02-moving-averages-oscillators-and-volatility.md)
3. [Candlesticks, chart patterns, Ichimoku and cycles](chapters/ch03-candlesticks-chart-patterns-and-ichimoku.md)
4. [Seasonality, positioning (COT) and sentiment](chapters/ch04-seasonality-positioning-and-sentiment.md)
5. [Strategy families: rules, parameters and invalidation](chapters/ch05-strategy-families-rules-and-invalidation.md)
6. [Risk management, position sizing, ruin and Kelly](chapters/ch06-risk-management-and-position-sizing.md)
7. [Trader psychology and discipline](chapters/ch07-trader-psychology-and-discipline.md)
8. [Validation, backtests, claimed results, seller incentives and compounding](chapters/ch08-validation-backtests-and-claimed-results.md)
9. [Fundamental screening, fair value and accounting red flags](chapters/ch09-fundamental-screening-and-accounting-red-flags.md)
10. [Options, certificates and leveraged products: mechanism and risk](chapters/ch10-options-certificates-and-leveraged-products.md)
11. [Scanning and comparing structured products: a reading procedure](chapters/ch11-scanning-and-comparing-structured-products.md)
12. [Market microstructure, liquidity and flows](chapters/ch12-market-microstructure-liquidity-and-flows.md)
13. [Return distribution, anomalies and market regimes](chapters/ch13-return-distribution-anomalies-and-regimes.md)

## Topic Index

- **ADX, Parabolic SAR, Bollinger bands** -> ch02
- **Altman Z-Score, Piotroski F-Score, Beneish M-Score** -> ch09
- **ATR stops and targets** -> ch02, ch06
- **Anomalies, decay after publication, capacity** -> ch13
- **Autocall, memory, worst-of, airbag, cash collect** -> ch10, ch11
- **Analog statistics, pattern matching (position)** -> ch04
- **Composite oscillators, correlated components** -> ch04
- **Buffer, coupon basis, record date, quanto, fixing, scenario grid** -> ch11
- **Compounding of promised returns, peak-to-end results** -> ch08
- **Covered calls, premium selling, lottery tickets** -> ch10
- **Days to liquidate, participation rate** -> ch12
- **Duration, bond prices and rate regimes** -> ch13
- **ETF creation and redemption, authorised participants** -> ch12
- **EV/Sales, Rule of 40 for loss-making firms** -> ch09
- **Ergodicity, Kelly fraction, ruin** -> ch06
- **Backtest, overfitting, walk-forward, data snooping** -> ch08
- **Break-even win rate, expectancy** -> ch06, ch08
- **Breakout, false break, retest** -> ch01, ch05
- **Candlestick patterns (doji, hammer, engulfing, star)** -> ch03
- **COT report, open interest, commercials** -> ch04
- **Correlation between positions** -> ch06
- **Divergences, overbought/oversold** -> ch02
- **Drawdown, recovery, losing streaks** -> ch06
- **Fair value, discounting, growth-equals-P/E rule** -> ch09
- **Fixed leverage, intraday reset** -> ch10
- **Head and shoulders, triangles, projections** -> ch03
- **Ichimoku (Tenkan, Kijun, Chikou, cloud)** -> ch03
- **Index inclusion, committees, forced passive flows** -> ch12
- **Leverage, margin, notional, contracts for difference, wipe-out threshold** -> ch06, ch10
- **Market makers, inventory, adverse selection, spreads** -> ch12
- **Mean reversion to an average** -> ch05
- **Momentum ranking** -> ch05
- **Multiple compression, earnings growth versus price** -> ch13
- **Pair trading, long-short spreads** -> ch05, ch06
- **Payment for order flow, order routing, visible stops** -> ch12
- **Pivot points** -> ch01, ch05
- **Position sizing** -> ch06, ch10
- **Price impact, square-root law, order splitting** -> ch12
- **Psychology, disposition effect, hindsight** -> ch07
- **Referral fees, copy trading, performance fees, multi-level sellers** -> ch08
- **Retail sentiment, sector rotation** -> ch04
- **Return skew, median versus mean, luck in small samples** -> ch13
- **Seasonality and its statistics** -> ch04, ch08
- **Settlement cycle, short availability** -> ch12
- **Shareholder yield, buybacks, insider purchases** -> ch09
- **Stay-above, stay-below, corridor certificates** -> ch10
- **Trend (Dow), trendlines, top-down timeframes** -> ch01
- **Turbo, mini future, open-ended turbo** -> ch10
- **Volume, Wyckoff phases** -> ch01

## Related Skills

- `investing-and-financial-history`: market efficiency, factors, options mechanics, behavioural finance, backtest statistics, financial mathematics.
- `scientific-thinking`: statistical method, multiple testing, evidence quality.
- `behavior-and-decision-science`: biases and decision quality.
- `economics-finance`: macro, central banks, rates.
- `crypto-and-digital-assets`: crypto-specific price claims, leverage and custody.
- `personal-finance-italy`: one country's tax rules for certificates, funds and trading gains.

## Scope & Limits

Practical theory covering chart reading, indicators, patterns, seasonality and positioning, strategy rules and their failure modes, risk and sizing arithmetic, psychology, validation of trading claims, fundamental screening, leveraged-product mechanics, market microstructure at the level of impact, spreads, settlement and index flows, and return-distribution and regime concepts. Not covered: live signals, price targets, product or broker selection, personal portfolio construction, tax and legal advice, platform tutorials, macro forecasting and bond analysis beyond duration arithmetic (other skills). Volume analysis, Wyckoff, Elliott waves and correlation between positions are covered only briefly; supplements are general knowledge to re-check. Parameters, thresholds and market rules are practitioner conventions or snapshots, several inconsistent between sources and flagged as such. Results quoted in ch08 are anonymised claims, not verified performance. The skill gives no investment, trading, tax or legal guarantee.
